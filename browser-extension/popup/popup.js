const $ = (id) => document.getElementById(id);

function setStatus(text) {
  $("status").textContent = text;
}

async function load() {
  const cfg = await chrome.storage.local.get({
    stateUrl: "",
    relayUrl: "http://127.0.0.1:8766",
    overlayEnabled: true,
  });
  $("stateUrl").value = cfg.stateUrl || "";
  $("relayUrl").value = cfg.relayUrl || "http://127.0.0.1:8766";
  $("overlayEnabled").checked = cfg.overlayEnabled !== false;
}

async function save() {
  await chrome.storage.local.set({
    stateUrl: $("stateUrl").value.trim(),
    relayUrl: $("relayUrl").value.trim(),
    overlayEnabled: $("overlayEnabled").checked,
  });
  chrome.runtime.sendMessage({ type: "ASW_RELOAD_CONFIG" });
  setStatus("已保存，正在轮询 run-state…");
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
