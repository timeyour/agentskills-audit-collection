/**
 * In-page overlay: shows activeAnnotation from run-state (via background poll).
 * Does not assign severity or write audit rules — Skills + Agent own that.
 */

(function () {
  if (window.__aswOverlayMounted) return;
  window.__aswOverlayMounted = true;

  const ROOT_ID = "asw-audit-root";

  function el(tag, className, text) {
    const n = document.createElement(tag);
    if (className) n.className = className;
    if (text != null) n.textContent = text;
    return n;
  }

  function ensureRoot() {
    let root = document.getElementById(ROOT_ID);
    if (root) return root;

    root = el("div");
    root.id = ROOT_ID;
    root.className = "asw-hidden";

    const panel = el("div", "asw-panel");
    const head = el("div", "asw-head");
    head.innerHTML =
      '<span><span class="asw-live-dot"></span><strong>AgentSkills 审计旁白</strong></span><span aria-hidden="true">▾</span>';
    head.addEventListener("click", () => root.classList.toggle("asw-collapsed"));

    const body = el("div", "asw-body");
    const stages = el("div", "asw-stages");
    const progress = el("div", "asw-progress");
    progress.appendChild(el("span"));
    const meta = el("div", "asw-meta");
    const annotation = el("div", "asw-annotation", "在扩展弹窗中配置 run-state.json URL 后显示旁白。");
    const findings = el("div", "asw-findings");
    const err = el("div", "asw-err");
    err.style.display = "none";

    body.append(stages, progress, meta, annotation, findings, err);

    const foot = el("div", "asw-foot");
    const btnCapture = el("button", "", "截图留证");
    const btnWorkbench = el("button", "asw-secondary", "完整看板");
    const btnHide = el("button", "asw-secondary", "隐藏");
    foot.append(btnCapture, btnWorkbench, btnHide);

    btnCapture.addEventListener("click", async (e) => {
      e.stopPropagation();
      btnCapture.textContent = "截取中…";
      btnCapture.disabled = true;
      try {
        const res = await chrome.runtime.sendMessage({
          type: "ASW_CAPTURE_SCREENSHOT",
          note: annotation.textContent?.slice(0, 120) || "",
        });
        if (res?.saved) btnCapture.textContent = "已保存";
        else if (res?.queued) btnCapture.textContent = "已排队";
        else btnCapture.textContent = res?.error ? "失败" : "已截取";
      } catch {
        btnCapture.textContent = "失败";
      }
      setTimeout(() => {
        btnCapture.textContent = "截图留证";
        btnCapture.disabled = false;
      }, 2000);
    });

    btnWorkbench.addEventListener("click", (e) => {
      e.stopPropagation();
      chrome.storage.local.get({ stateUrl: "" }, (cfg) => {
        let rel = cfg.stateUrl || "";
        try {
          rel = new URL(rel).pathname.replace(/^\//, "");
        } catch {
          rel = rel.replace(/^\//, "");
        }
        const q = rel ? `?state=${encodeURIComponent(rel)}` : "?demo=1";
        window.open(`http://127.0.0.1:8765/workbench/live/${q}`, "_blank");
      });
    });

    btnHide.addEventListener("click", (e) => {
      e.stopPropagation();
      root.classList.add("asw-hidden");
    });

    panel.append(head, body, foot);
    root.appendChild(panel);
    document.documentElement.appendChild(root);

    root._refs = { stages, progress, meta, annotation, findings, err, progressBar: progress.firstChild };
    return root;
  }

  function renderStages(container, state) {
    container.textContent = "";
    const list = state?.stages || [];
    if (!list.length) return;
    const title = el("div", "", "阶段");
    title.style.fontWeight = "600";
    title.style.marginBottom = "4px";
    container.appendChild(title);
    list.forEach((st) => {
      const row = el("div", "asw-stage-line" + (st.id === state.currentStageId ? " active" : ""));
      row.textContent = (st.order ? st.order + ". " : "") + (st.label || st.id) + " · " + (st.status || "");
      container.appendChild(row);
    });
  }

  function renderFindings(container, list) {
    container.textContent = "";
    if (!list?.length) return;
    const title = el("div", "", "已发现问题预览");
    title.style.fontSize = "11px";
    title.style.color = "#667085";
    title.style.marginBottom = "4px";
    container.appendChild(title);
    for (const f of list.slice(0, 3)) {
      const row = el("div", "asw-finding");
      const sev = el("span", `asw-sev asw-sev-${f.severity || "S4"}`, f.severity || "?");
      row.append(sev, document.createTextNode(f.title || ""));
      container.appendChild(row);
    }
  }

  function applyPayload(payload) {
    chrome.storage.local.get({ overlayEnabled: true }, (cfg) => {
      const root = ensureRoot();
      if (!cfg.overlayEnabled) {
        root.classList.add("asw-hidden");
        return;
      }
      root.classList.remove("asw-hidden");
      const { state, error, percent } = payload;
      const r = root._refs;

      if (error) {
        r.err.style.display = "block";
        r.err.textContent = `无法读取 run-state：${error}`;
      } else {
        r.err.style.display = "none";
      }

      if (!state) {
        r.meta.textContent = "未连接 run-state";
        r.annotation.textContent = "请先运行 audit-run-init.sh，并在扩展弹窗填入 state URL。";
        r.progressBar.style.width = "0%";
        return;
      }

      const hostMatch =
        state.target?.url &&
        location.href &&
        (() => {
          try {
            return new URL(state.target.url).hostname === location.hostname;
          } catch {
            return false;
          }
        })();

      r.progressBar.style.width = `${percent || 0}%`;
      r.meta.textContent = [
        state.progress?.label || "—",
        state.status || "",
        hostMatch ? "· 当前页匹配审计目标" : "· 当前页非目标域（旁白仍显示）",
      ].join(" ");
      r.annotation.textContent =
        state.activeAnnotation || "（Agent 未设置 activeAnnotation）";
      renderStages(r.stages, state);
      renderFindings(r.findings, state.findingsPreview);
    });
  }

  chrome.runtime.onMessage.addListener((msg) => {
    if (msg.type === "ASW_RUN_STATE") applyPayload(msg);
  });

  chrome.storage.local.get({ overlayEnabled: true }, (cfg) => {
    if (cfg.overlayEnabled) {
      ensureRoot();
      chrome.runtime.sendMessage({ type: "ASW_GET_STATE" }, (res) => {
        if (res?.state) applyPayload({ state: res.state, percent: 0, error: null });
      });
    }
  });
})();
