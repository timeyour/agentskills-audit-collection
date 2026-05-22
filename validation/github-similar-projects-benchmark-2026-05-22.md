# GitHub Similar Projects Benchmark

Date: 2026-05-22

This benchmark compares AgentSkills Audit Collection against nearby GitHub projects. The goal is not to prove that this repository is another generic skills list. The goal is to clarify where it fits:

```text
AI-built product acceptance system
= audit skills + workflow checks + physical browser evidence + severity + regression + lessons
```

## Summary

Most similar repositories fall into four groups:

1. Agent skills collections.
2. Claude Code command and workflow frameworks.
3. Security or engineering audit skill packs.
4. Browser automation and DESIGN.md support tools.

None of the reviewed projects has the same center of gravity as this repository: end-to-end acceptance for AI-built websites and apps, with source evidence, live evidence, physical browser proof, S0-S4 severity, fix prompts, regression checks, and lessons.

## Comparable Projects

| Project | Category | Similarity | What to learn | What not to copy |
| --- | --- | --- | --- | --- |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Agent skills index | Large curated skill collection with clear taxonomy. | Use strong README categories, badges, and discovery paths. | Do not become a broad awesome list without a product thesis. |
| [trailofbits/skills](https://github.com/trailofbits/skills) | Security audit skill marketplace | Professional audit skills, verification language, and evidence mindset. | Borrow the plugin marketplace clarity, audit seriousness, and "bugs found" proof pattern. | Do not narrow this repo to only security review. |
| [hashicorp/agent-skills](https://github.com/hashicorp/agent-skills) | Enterprise product skills | Product-scoped skills for Terraform and Packer. | Use product grouping, installation clarity, and enterprise trust language. | Do not over-specialize around one vendor ecosystem. |
| [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | Claude Code workflow framework | Commands, agents, modes, MCP, and lifecycle orchestration. | Study routing, command discoverability, and lifecycle coverage. | Do not copy framework bloat; this repo should stay acceptance-focused. |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | AI agile workflow method | Structured roles, workflows, planning depth, and implementation stages. | Borrow stage gates, role clarity, and adaptive workflow depth. | Do not turn audit skills into a full project-management operating system. |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | DESIGN.md library | Reusable design-system documents for AI UI generation. | Use DESIGN.md as a visible, copyable source of design truth. | Do not claim design mimicry equals product acceptance. |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | Browser automation for agents | CLI plus skills for token-efficient real browser operations. | Strengthen `/physical-flow-test` around real execution and artifact handoff. | Do not replace acceptance reports with raw automation commands. |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Browser MCP | Browser automation through structured page snapshots. | Keep MCP as an optional physical-verification layer. | Do not depend on MCP-only flows for portability. |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | AI browser agent | Real-world browser task execution and benchmarking. | Borrow benchmark framing and real-task language. | Do not confuse autonomous browsing with deterministic product acceptance. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code ecosystem index | Broad directory of Claude Code resources. | Use ecosystem-navigation patterns and related-project positioning. | Do not dilute the repo into a general Claude Code resource list. |

## Positioning Gap

The ecosystem already has many projects that answer:

```text
What skills exist?
How do I install more commands?
How do I automate a browser?
How do I make AI-generated UI look better?
How do I structure AI-assisted development?
```

This repository should answer a narrower and more useful delivery question:

```text
Can this AI-built product be trusted, fixed, retested, and delivered?
```

That means the repository should emphasize:

- source vs live evidence separation
- real workflow checkpoints
- physical browser proof for critical paths
- visual quality and AI-slop detection
- deployment readiness
- S0-S4 delivery severity
- copyable fix prompts
- regression checks
- lessons that become reusable guardrails

## Benchmark Lessons

### 1. Add ecosystem proof, not just internal claims

Projects such as Trail of Bits Skills and HashiCorp Agent Skills feel more credible because they show installation paths, project structure, and professional usage boundaries. This repository should keep adding validation reports and short case-study summaries so users see proof, not only promises.

### 2. Keep the repo narrower than a generic skills marketplace

VoltAgent and Awesome Claude Code are useful indexes. AgentSkills Audit Collection should not compete as a larger index. Its advantage is a sharper workflow:

```text
audit -> flow-test -> physical-flow-test -> deploy-check -> accept-five -> lessons
```

### 3. Make `/physical-flow-test` the differentiator

Playwright CLI, Playwright MCP, and browser-use prove that real browser operation is becoming a core agent capability. This repository should connect browser execution to acceptance evidence, not just browser control.

### 4. Treat DESIGN.md as a support layer

awesome-design-md is useful for visual consistency. In this repository, `DESIGN.md` should guide audit report surfaces, workbench UI, screenshots, and examples. It should not replace visual QA, accessibility checks, or live workflow proof.

### 5. Borrow "marketplace clarity" without marketplace bloat

The best comparable repos make their entry points obvious. This repository should keep the skills list short, explain when to use each skill, and keep references behind progressive disclosure.

## Recommended Repository Additions

### P0

- Keep this benchmark linked from `CASE_STUDIES.md`.
- Keep the README positioning sentence focused on acceptance, not general coding.
- Keep `/physical-flow-test` visible in the quick-start path.

### P1

- Add a short "Comparable Projects" section to `PRODUCT.md`.
- Add one screenshot or trace artifact sample from `examples/physical-flow-demo/`.
- Add a "Why not just use Playwright MCP?" note inside `/physical-flow-test` references.

### P2

- Add optional benchmark labels to future validation reports:
  - `skill-marketplace-comparable`
  - `browser-proof-comparable`
  - `design-md-comparable`
  - `audit-skill-comparable`
  - `workflow-framework-comparable`

## Strategic Conclusion

The closest external analog is not one repo. It is the intersection of:

```text
Trail of Bits audit skill seriousness
+ VoltAgent skill/design discovery
+ Playwright real-browser execution
+ BMAD/SuperClaude workflow orchestration
```

AgentSkills Audit Collection should own the acceptance layer between vibe-coded output and real product delivery.
