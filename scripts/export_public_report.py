#!/usr/bin/env python3
"""M4: Export customer-facing HTML from audit-report.schema.json."""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = ROOT / "validation" / "golden" / "audit-report.example.json"
DEFAULT_OUT = ROOT / "reports" / "demo-site-audit.html"


def sev_class(sev: str) -> str:
    return f"asw-sev-{html.escape(sev or 'S4')}"


def benchmark_lookup(data: dict) -> dict[str, dict]:
    by_id: dict[str, dict] = {}
    for ref in data.get("benchmarkRefs") or []:
        cid = ref.get("caseId")
        if cid:
            by_id[cid] = ref
    if not by_id:
        index_path = ROOT / "validation" / "cases" / "index.json"
        if index_path.is_file():
            for c in json.loads(index_path.read_text(encoding="utf-8")).get("cases", []):
                by_id[c["caseId"]] = c
    return by_id


def render_benchmark_link(case_id: str | None, benchmarks: dict[str, dict]) -> str:
    if not case_id:
        return ""
    ref = benchmarks.get(case_id)
    if not ref:
        return f"<p class='asw-muted'>Reference: {html.escape(case_id)}</p>"
    url = ref.get("url") or ""
    title = ref.get("title") or case_id
    if url:
        return (
            f"<p class='asw-benchmark'>参考案例：<a href='{html.escape(url)}' rel='noopener' target='_blank'>"
            f"{html.escape(title)}</a> — {html.escape(ref.get('summary', ''))}</p>"
        )
    return f"<p class='asw-benchmark'>参考案例：{html.escape(title)} — {html.escape(ref.get('summary', ''))}</p>"


def render_checklist_section(title: str, block: dict | None) -> str:
    if not block:
        return ""
    rows = ""
    for item in block.get("checklist") or []:
        rows += (
            f"<tr><td>{html.escape(str(item.get('item', '')))}</td>"
            f"<td><span class='asw-pill'>{html.escape(str(item.get('status', '')))}</span></td>"
            f"<td>{html.escape(str(item.get('notes', '')))}</td></tr>"
        )
    return f"""
    <section>
      <h2>{html.escape(title)}</h2>
      <p>Status: <span class="asw-pill">{html.escape(block.get('status', 'UNKNOWN'))}</span></p>
      <table class="asw-data"><thead><tr><th>Check</th><th>Status</th><th>Notes</th></tr></thead>
      <tbody>{rows}</tbody></table>
    </section>"""


def render_report(data: dict) -> str:
    target = data.get("target") or {}
    verdict = data.get("finalVerdict") or {}
    evidence = data.get("evidence") or {}
    issues = data.get("issueCards") or []
    regression = data.get("regressionChecks") or []
    deploy = data.get("deploymentReadiness") or {}
    fix_pack = data.get("copyableFixPack") or {}
    progress = data.get("auditProgress") or {}
    security = data.get("securityReadiness")
    data_ready = data.get("dataReadiness")
    benchmarks = benchmark_lookup(data)

    score_rows = ""
    for item in deploy.get("checklist") or []:
        score_rows += (
            f"<tr><td>{html.escape(str(item.get('item', '')))}</td>"
            f"<td><span class='asw-pill'>{html.escape(str(item.get('status', '')))}</span></td>"
            f"<td>{html.escape(str(item.get('notes', '')))}</td></tr>"
        )

    findings_html = ""
    for card in issues:
        ev = card.get("evidence") or {}
        findings_html += f"""
        <article class="asw-issue-card">
          <div class="asw-issue-meta">
            <span class="asw-sev {sev_class(card.get('severity', 'S4'))}">{html.escape(card.get('severity', ''))}</span>
            <span class="asw-pill">{html.escape(card.get('id', ''))}</span>
          </div>
          <h3>{html.escape(card.get('title', ''))}</h3>
          <table class="asw-kv">
            <tr><th>Evidence</th><td>{html.escape(ev.get('summary', '—'))} <em>({html.escape(ev.get('level', 'UNKNOWN'))})</em></td></tr>
            <tr><th>Impact</th><td>{html.escape(card.get('impact', '—'))}</td></tr>
            <tr><th>Fix</th><td>{html.escape(card.get('fix', '—'))}</td></tr>
            <tr><th>Regression</th><td>{html.escape(card.get('regressionCheck', '—'))}</td></tr>
          </table>
          {render_benchmark_link(card.get('benchmarkCaseId'), benchmarks)}
        </article>"""

    reg_html = ""
    for check in regression:
        reg_html += (
            f"<li><input type='checkbox' disabled /> "
            f"<strong>{html.escape(check.get('issueId', ''))}</strong> — "
            f"{html.escape(check.get('check', ''))} "
            f"<span class='asw-muted'>({html.escape(check.get('status', 'pending'))})</span></li>"
        )

    combined = fix_pack.get("combinedPrompt") or ""

    progress_html = ""
    if progress:
        steps = progress.get("completedSteps") or []
        steps_li = "".join(f"<li>{html.escape(s)}</li>" for s in steps)
        progress_html = f"""
    <section>
      <h2>检测过程摘要</h2>
      <p><strong>{html.escape(progress.get('label', '—'))}</strong>
         <span class="asw-pill">{html.escape(progress.get('status', ''))}</span></p>
      <p class="asw-muted">已完成步骤：</p>
      <ul>{steps_li or '<li class="asw-muted">—</li>'}</ul>
    </section>"""

    pillars_html = f"""
    <section>
      <h2>四维验收概览</h2>
      <div class="asw-pillars">
        <div><span>审美</span><strong>{html.escape(str(verdict.get('visualScore', '—')))}</strong></div>
        <div><span>功能</span><strong>{html.escape(str(verdict.get('functionalScore', '—')))}</strong></div>
        <div><span>安全</span><strong>{html.escape(str(verdict.get('securityScore', '—')))}</strong></div>
        <div><span>数据</span><strong>{html.escape(str(verdict.get('dataScore', '—')))}</strong></div>
      </div>
    </section>"""

    benchmark_html = ""
    if benchmarks and data.get("benchmarkRefs"):
        cards = ""
        for ref in data.get("benchmarkRefs") or []:
            url = ref.get("url") or ""
            title = ref.get("title") or ref.get("caseId", "")
            rel = ref.get("relevance") or ref.get("summary") or ""
            link = (
                f"<a href='{html.escape(url)}' rel='noopener' target='_blank'>{html.escape(title)}</a>"
                if url
                else html.escape(title)
            )
            cards += f"<li>{link} — {html.escape(rel)}</li>"
        benchmark_html = f"""
    <section>
      <h2>优秀网站对照</h2>
      <p class="asw-muted">供目标用户理解「好的交付大概长什么样」。</p>
      <ul>{cards}</ul>
    </section>"""

    ev_rows = ""
    for item in evidence.get("items") or []:
        ev_rows += (
            f"<tr><td>{html.escape(item.get('type', ''))}</td>"
            f"<td>{html.escape(item.get('status', ''))}</td>"
            f"<td>{html.escape(item.get('notes', ''))}</td></tr>"
        )

    title = target.get("url") or "Website Audit Report"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)} — Delivery Audit</title>
  <style>
    .asw-public {{
      --primary:#12324A; --accent:#2F7D68; --accent-soft:#DDF2EA;
      --canvas:#F6F8FA; --surface:#fff; --ink:#17202A; --body:#344054;
      --muted:#667085; --border:#D8E0E7;
      --s0:#7A1E1E; --s1:#B42318; --s2:#92400E; --s3:#3B5B73; --s4:#475467;
      font-family: Inter, ui-sans-serif, system-ui, sans-serif;
      font-size: 16px; line-height: 1.6; color: var(--ink); background: var(--canvas); margin: 0;
    }}
    .asw-public * {{ box-sizing: border-box; }}
    .asw-public .asw-wrap {{ max-width: 960px; margin: 0 auto; padding: 40px 24px 64px; }}
    .asw-public .asw-hero {{
      background: var(--primary); color: #fff; margin: -40px -24px 32px; padding: 40px 24px 32px;
    }}
    .asw-public .asw-eyebrow {{ font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--accent-soft); }}
    .asw-public h1.asw-title {{ margin: 8px 0 12px; font-size: clamp(28px, 4vw, 40px); font-weight: 650; line-height: 1.15; }}
    .asw-public .asw-meta {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; margin-top: 20px; font-size: 14px; }}
    .asw-public .asw-meta div {{ background: rgba(255,255,255,.1); padding: 10px 12px; border-radius: 6px; }}
    .asw-public h2 {{ font-size: 22px; font-weight: 650; margin: 36px 0 14px; }}
    .asw-public p {{ color: var(--body); margin: 0 0 12px; }}
    .asw-public .asw-sev {{ display: inline-block; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 999px; color: #fff; }}
    .asw-public .asw-sev-S0 {{ background: var(--s0); }}
    .asw-public .asw-sev-S1 {{ background: var(--s1); }}
    .asw-public .asw-sev-S2 {{ background: var(--s2); }}
    .asw-public .asw-sev-S3 {{ background: var(--s3); }}
    .asw-public .asw-sev-S4 {{ background: var(--s4); }}
    .asw-public .asw-pill {{ font-size: 12px; padding: 2px 8px; border-radius: 999px; background: var(--surface-soft); color: var(--body); font-weight: 600; }}
    .asw-public .asw-issue-card {{
      background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
      padding: 20px; margin-bottom: 16px;
    }}
    .asw-public .asw-issue-card h3 {{ margin: 10px 0 8px; font-size: 18px; }}
    .asw-public .asw-issue-meta {{ display: flex; gap: 8px; align-items: center; }}
    .asw-public table.asw-kv {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    .asw-public table.asw-kv th {{ text-align: left; width: 120px; color: var(--muted); font-weight: 600; padding: 6px 8px 6px 0; vertical-align: top; }}
    .asw-public table.asw-kv td {{ padding: 6px 0; }}
    .asw-public table.asw-data {{ width: 100%; border-collapse: collapse; font-size: 14px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }}
    .asw-public table.asw-data th, .asw-public table.asw-data td {{ padding: 10px 12px; border-bottom: 1px solid var(--border); text-align: left; }}
    .asw-public table.asw-data th {{ background: var(--surface-soft); color: var(--muted); font-size: 12px; text-transform: uppercase; }}
    .asw-public .asw-prompt {{
      background: #101828; color: #EAECF0; padding: 16px; border-radius: 8px;
      font-family: ui-monospace, monospace; font-size: 13px; white-space: pre-wrap;
    }}
    .asw-public ul {{ padding-left: 20px; }}
    .asw-public .asw-muted {{ color: var(--muted); font-size: 14px; }}
    .asw-public a {{ color: var(--accent); }}
    .asw-public .asw-benchmark {{ font-size: 14px; margin-top: 10px; padding: 10px 12px; background: var(--accent-soft); border-radius: 6px; }}
    .asw-public .asw-pillars {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }}
    .asw-public .asw-pillars div {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 14px; text-align: center; }}
    .asw-public .asw-pillars span {{ display: block; font-size: 12px; color: var(--muted); margin-bottom: 6px; }}
    .asw-public .asw-pillars strong {{ font-size: 22px; }}
    .asw-public footer {{ margin-top: 48px; padding-top: 16px; border-top: 1px solid var(--border); font-size: 13px; color: var(--muted); }}
  </style>
</head>
<body class="asw-public">
  <div class="asw-wrap">
    <header class="asw-hero">
      <p class="asw-eyebrow">Delivery acceptance report</p>
      <h1 class="asw-title">{html.escape(verdict.get('summary', 'Website audit')[:120])}</h1>
      <div class="asw-meta">
        <div><strong>Target</strong><br>{html.escape(target.get('url', '—'))}</div>
        <div><strong>Risk</strong><br><span class="asw-sev {sev_class(verdict.get('overallRisk', 'S4'))}">{html.escape(verdict.get('overallRisk', '—'))}</span></div>
        <div><strong>Evidence</strong><br>{html.escape(evidence.get('overallGrade', '—'))}</div>
        <div><strong>Delivery ready</strong><br>{'Yes' if verdict.get('deliveryReady') else 'No'}</div>
      </div>
    </header>

    <section>
      <h2>Executive summary</h2>
      <p>{html.escape(verdict.get('summary', data.get('scope', {}).get('summary', '—')))}</p>
      <p class="asw-muted">Fix first: {html.escape(str(verdict.get('fixFirst', '—')))}</p>
    </section>

    {progress_html}
    {pillars_html}
    {benchmark_html}

    <section>
      <h2>Deployment readiness</h2>
      <p>Status: <span class="asw-pill">{html.escape(deploy.get('status', 'UNKNOWN'))}</span></p>
      <table class="asw-data"><thead><tr><th>Check</th><th>Status</th><th>Notes</th></tr></thead><tbody>{score_rows}</tbody></table>
    </section>

    <section>
      <h2>Evidence quality</h2>
      <table class="asw-data"><thead><tr><th>Type</th><th>Status</th><th>Notes</th></tr></thead><tbody>{ev_rows}</tbody></table>
    </section>

    {render_checklist_section("Security readiness", security)}
    {render_checklist_section("Data & privacy readiness", data_ready)}

    <section>
      <h2>Top findings</h2>
      {findings_html or '<p class="asw-muted">No issues recorded.</p>'}
    </section>

    <section>
      <h2>Regression checklist</h2>
      <ul>{reg_html}</ul>
    </section>

    <section>
      <h2>Copyable fix prompt</h2>
      <div class="asw-prompt">{html.escape(combined)}</div>
    </section>

    <footer>
      Generated by AgentSkills Audit Workbench · schema {html.escape(data.get('schemaVersion', '0.1.0'))}
      · {html.escape(data.get('generatedAt', ''))}
    </footer>
  </div>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_IN)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)

    if not args.input.is_file():
        print(f"error: missing {args.input}", file=sys.stderr)
        return 1

    data = json.loads(args.input.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_report(data), encoding="utf-8")
    print(f"Wrote {args.output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
