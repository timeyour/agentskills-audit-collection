const $ = (id) => document.getElementById(id);

function setStatus(text) {
  $("status").textContent = text;
}

function readNarrationFromForm() {
  return {
    enabled: $("narrationEnabled").checked,
    mode: $("narrationMode").value,
    task: $("narrationTask").value,
    targetLocale: $("targetLocale").value.trim() || "zh",
    sourceLocale: "auto",
    direct: {
      endpoint: $("directEndpoint").value.trim(),
      model: $("directModel").value.trim(),
      apiKey: $("directApiKey").value.trim(),
    },
  };
}

function fillNarrationForm(n) {
  const cfg = n || {};
  $("narrationEnabled").checked = !!cfg.enabled;
  $("narrationMode").value = cfg.mode || "passthrough";
  $("narrationTask").value = cfg.task || "none";
  $("targetLocale").value = cfg.targetLocale || "zh";
  $("directEndpoint").value = cfg.direct?.endpoint || "";
  $("directModel").value = cfg.direct?.model || "";
  $("directApiKey").value = cfg.direct?.apiKey || "";
}

async function load() {
  const cfg = await chrome.storage.local.get({
    stateUrl: "",
    relayUrl: "http://127.0.0.1:8766",
    overlayEnabled: true,
    narration: {
      enabled: false,
      mode: "passthrough",
      task: "none",
      targetLocale: "zh",
    },
  });
  $("stateUrl").value = cfg.stateUrl || "";
  $("relayUrl").value = cfg.relayUrl || "http://127.0.0.1:8766";
  $("overlayEnabled").checked = cfg.overlayEnabled !== false;
  fillNarrationForm(cfg.narration);
}

async function save() {
  const narration = readNarrationFromForm();
  if (narration.enabled && narration.task !== "none" && narration.mode === "passthrough") {
    narration.mode = "relay";
    $("narrationMode").value = "relay";
  }
  await chrome.storage.local.set({
    stateUrl: $("stateUrl").value.trim(),
    relayUrl: $("relayUrl").value.trim(),
    overlayEnabled: $("overlayEnabled").checked,
    narration: { ...narration, relayUrl: $("relayUrl").value.trim() },
  });
  chrome.runtime.sendMessage({ type: "ASW_RELOAD_CONFIG" });
  const hint =
    narration.enabled && narration.task !== "none"
      ? `已保存 · 旁白 ${narration.task}（${narration.mode}）`
      : "已保存，正在轮询 run-state…";
  setStatus(hint);
}

$("save").addEventListener("click", save);

$("openWorkbench").addEventListener("click", () => {
  const stateUrl = $("stateUrl").value.trim();
  let rel = stateUrl;
  try {
    rel = new URL(stateUrl).pathname.replace(/^\//, "");
  } catch {
    rel = rel.replace(/^\//, "");
  }
  const q = rel ? `?state=${encodeURIComponent(rel)}` : "?demo=1";
  chrome.tabs.create({ url: `http://127.0.0.1:8765/workbench/live/${q}` });
});

load();
