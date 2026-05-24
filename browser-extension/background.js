/**
 * Polls run-state.json and broadcasts to content scripts.
 * Optional POST of screenshots to scripts/browser-relay.py (port 8766).
 * Optional second model for displayAnnotation only — narration/enhance.js
 */

importScripts("narration/enhance.js");

const DEFAULT_POLL_MS = 1000;
const DEFAULT_RELAY = "http://127.0.0.1:8766";

/** @type {object | null} */
let lastState = null;
let pollTimer = null;

async function getConfig() {
  return chrome.storage.local.get({
    stateUrl: "",
    relayUrl: DEFAULT_RELAY,
    overlayEnabled: true,
    pollMs: DEFAULT_POLL_MS,
    narration: {
      enabled: false,
      mode: "passthrough",
      task: "none",
      targetLocale: "zh",
      sourceLocale: "auto",
    },
  });
}

async function fetchRunState(stateUrl) {
  if (!stateUrl) return null;
  const res = await fetch(stateUrl, { cache: "no-store" });
  if (!res.ok) throw new Error(`run-state HTTP ${res.status}`);
  return res.json();
}

function progressPercent(state) {
  const p = state?.progress;
  if (!p || !p.total) return 0;
  return Math.min(100, Math.round((p.current / p.total) * 100));
}

async function resolveDisplayAnnotation(state) {
  if (!state?.activeAnnotation) {
    return { text: "", mode: "passthrough" };
  }
  const cfg = await getConfig();
  const narration = {
    ...(cfg.narration || {}),
    relayUrl: cfg.relayUrl || DEFAULT_RELAY,
  };
  return ASW_enhanceCaption(state.activeAnnotation, narration, state);
}

async function broadcastState(state, error) {
  const tabs = await chrome.tabs.query({});
  let displayAnnotation = state?.activeAnnotation || "";
  let displayAnnotationMode = "passthrough";
  if (state?.activeAnnotation) {
    try {
      const enhanced = await resolveDisplayAnnotation(state);
      displayAnnotation = enhanced.text;
      displayAnnotationMode = enhanced.mode;
    } catch {
      displayAnnotation = state.activeAnnotation;
    }
  }
  const payload = {
    type: "ASW_RUN_STATE",
    state,
    error: error || null,
    percent: state ? progressPercent(state) : 0,
    displayAnnotation,
    displayAnnotationMode,
  };
  for (const tab of tabs) {
    if (!tab.id || !tab.url?.startsWith("http")) continue;
    try {
      await chrome.tabs.sendMessage(tab.id, payload);
    } catch {
      /* content script not ready */
    }
  }
}

async function pollOnce() {
  const { stateUrl, overlayEnabled } = await getConfig();
  if (!overlayEnabled || !stateUrl) {
    await broadcastState(null, null);
    return;
  }
  try {
    lastState = await fetchRunState(stateUrl);
    await broadcastState(lastState, null);
  } catch (e) {
    await broadcastState(lastState, String(e.message || e));
  }
}

async function restartPolling() {
  if (pollTimer) clearInterval(pollTimer);
  const { pollMs, overlayEnabled, stateUrl } = await getConfig();
  if (!overlayEnabled || !stateUrl) return;
  pollTimer = setInterval(pollOnce, Math.max(500, pollMs || DEFAULT_POLL_MS));
  pollOnce();
}

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "ASW_GET_STATE") {
    sendResponse({ state: lastState });
    return false;
  }
  if (msg.type === "ASW_CAPTURE_SCREENSHOT") {
    handleCapture(sender.tab?.id, msg.note || "")
      .then(sendResponse)
      .catch((e) => sendResponse({ ok: false, error: String(e.message || e) }));
    return true;
  }
  if (msg.type === "ASW_RELOAD_CONFIG") {
    restartPolling().then(() => sendResponse({ ok: true }));
    return true;
  }
  return false;
});

async function handleCapture(tabId, note) {
  if (!tabId) throw new Error("No active tab");
  const dataUrl = await chrome.tabs.captureVisibleTab(null, { format: "png" });
  const tab = await chrome.tabs.get(tabId);
  const { relayUrl, stateUrl } = await getConfig();
  const runId = lastState?.runId || guessRunIdFromStateUrl(stateUrl);
  const body = {
    runId,
    note,
    url: tab.url || "",
    pngDataUrl: dataUrl,
    stageId: lastState?.currentStageId || null,
    stepId: lastState?.currentStepId || null,
    capturedAt: new Date().toISOString(),
  };

  if (relayUrl && runId) {
    try {
      const res = await fetch(`${relayUrl.replace(/\/$/, "")}/api/evidence`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      const json = await res.json();
      if (!res.ok) throw new Error(json.error || res.statusText);
      return { ok: true, saved: true, path: json.path || null };
    } catch (e) {
      await queueEvidenceFallback(body);
      return { ok: true, saved: false, queued: true, error: String(e.message || e) };
    }
  }
  await queueEvidenceFallback(body);
  return { ok: true, saved: false, queued: true };
}

function guessRunIdFromStateUrl(stateUrl) {
  if (!stateUrl) return "";
  const m = stateUrl.match(/validation\/artifacts\/([^/]+)\//);
  return m ? m[1] : "";
}

async function queueEvidenceFallback(body) {
  const { evidenceQueue = [] } = await chrome.storage.local.get({ evidenceQueue: [] });
  evidenceQueue.push(body);
  await chrome.storage.local.set({ evidenceQueue });
}

chrome.storage.onChanged.addListener((changes, area) => {
  if (area !== "local") return;
  if (changes.stateUrl || changes.overlayEnabled || changes.pollMs || changes.narration) {
    restartPolling();
  }
});

restartPolling();
