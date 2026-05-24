/**
 * Optional second model for overlay caption only.
 * Does not modify run-state.json or audit findings.
 * @global ASW_enhanceCaption
 */

const ASW_NARRATION_CACHE_MS = 60_000;
/** @type {Map<string, { text: string, at: number, mode: string }>} */
const captionCache = new Map();

function cacheKey(text, narration, state) {
  return [
    state?.runId || "",
    state?.currentStageId || "",
    state?.currentStepId || "",
    narration.task || "none",
    narration.targetLocale || "zh",
    text,
  ].join("|");
}

function defaultNarration(cfg) {
  return {
    enabled: false,
    mode: "passthrough",
    task: "none",
    targetLocale: "zh",
    sourceLocale: "auto",
    relayUrl: cfg?.relayUrl || "http://127.0.0.1:8766",
    direct: { endpoint: "", model: "", apiKey: "" },
    ...(cfg?.narration || {}),
  };
}

/**
 * @param {string} text
 * @param {object} narration
 * @param {object|null} state
 * @returns {Promise<{ text: string, mode: string, provider?: string|null }>}
 */
async function ASW_enhanceCaption(text, narration, state) {
  const n = defaultNarration({ narration });
  const raw = (text || "").trim();
  if (!raw || !n.enabled || n.task === "none" || n.mode === "passthrough") {
    return { text: raw, mode: "passthrough" };
  }

  const key = cacheKey(raw, n, state);
  const hit = captionCache.get(key);
  if (hit && Date.now() - hit.at < ASW_NARRATION_CACHE_MS) {
    return { text: hit.text, mode: hit.mode };
  }

  try {
    let result;
    if (n.mode === "relay") {
      result = await enhanceViaRelay(raw, n, state);
    } else if (n.mode === "direct") {
      result = await enhanceViaDirect(raw, n, state);
    } else {
      result = { text: raw, mode: "passthrough" };
    }
    captionCache.set(key, { text: result.text, mode: result.mode, at: Date.now() });
    return result;
  } catch {
    return { text: raw, mode: "passthrough" };
  }
}

async function enhanceViaRelay(text, narration, state) {
  const base = (narration.relayUrl || "http://127.0.0.1:8766").replace(/\/$/, "");
  const res = await fetch(`${base}/api/narrate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      text,
      task: narration.task,
      targetLocale: narration.targetLocale,
      sourceLocale: narration.sourceLocale,
      context: {
        runId: state?.runId,
        stageId: state?.currentStageId,
        stepId: state?.currentStepId,
        status: state?.status,
      },
    }),
  });
  const json = await res.json();
  if (!res.ok || !json.ok) throw new Error(json.error || res.statusText);
  return {
    text: json.text || text,
    mode: json.mode || "relay",
    provider: json.provider || null,
  };
}

async function enhanceViaDirect(text, narration, state) {
  const direct = narration.direct || {};
  const endpoint = (direct.endpoint || "").trim();
  const apiKey = (direct.apiKey || "").trim();
  const model = (direct.model || "").trim();
  if (!endpoint || !apiKey || !model) throw new Error("direct mode missing endpoint/model/apiKey");

  const system =
    narration.task === "summarize"
      ? "Summarize this audit narration in one short sentence. Keep severity codes and URLs. Output only the summary."
      : `Translate this audit narration to ${narration.targetLocale || "zh"}. Keep technical tokens. Output only the translation.`;

  const res = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      model,
      messages: [
        { role: "system", content: system },
        { role: "user", content: text },
      ],
      max_tokens: 256,
    }),
  });
  const json = await res.json();
  const out = json?.choices?.[0]?.message?.content?.trim();
  if (!res.ok || !out) throw new Error(json?.error?.message || res.statusText);
  return { text: out, mode: "direct", provider: endpoint };
}
