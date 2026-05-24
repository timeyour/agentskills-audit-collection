# Live Audit Workbench

实时查看 `/audit` 正在执行哪一阶段、哪一步，以及侧边 **activeAnnotation** 标注。

## 启动

```bash
cd agentskills-audit-collection
python3 -m http.server 8765
```

浏览器打开：

| URL | 说明 |
| --- | --- |
| http://localhost:8765/workbench/live/?demo=1 | 加载 golden 示例 + 演示动画 |
| http://localhost:8765/workbench/live/?state=validation/golden/audit-run.example.json | 静态示例 |
| http://localhost:8765/workbench/live/?state=validation/artifacts/&lt;runId&gt;/run-state.json | 真实审计进行中 |

勾选 **自动轮询** 后，页面每 1 秒读取 `run-state.json`（与 Cursor `/loop` 轮询思路相同，但针对审计状态文件）。

## Cursor Hooks（自动打开浏览器）

在仓库根目录已配置 `.cursor/hooks.json`：

| 事件 | 行为 |
| --- | --- |
| 发送含 `/audit`、审计、交付验收 的 prompt | 启动 `python3 -m http.server 8765` 并打开 Live 页 |
| 执行 `audit-run-init.sh` 后 | 打开对应 `run-state.json` 路径 |

若 workspace 是上级 `cursorskils`，使用根目录 `.cursor/hooks.json`（指向本子目录脚本）。

**验证：** Cursor → Settings → Hooks，或 Hooks 输出通道。修改 `hooks.json` 后若未生效请重启 Cursor。

## 与 Agent 配合

```bash
# 1. 初始化 run 目录
./scripts/audit-run-init.sh "https://yoursite.com"

# 2. 在 Claude/Cursor 中：
#    Use /audit on https://yoursite.com
#    Follow live-run-protocol.md — update RUN_DIR/run-state.json after each stage.

# 3. 打开 workbench 上打印的 STATE_URL

# 4. 可选：追加事件
./scripts/audit-run-emit.sh validation/artifacts/<runId> step_update \
  stageId=live-functional stepId=cta-primary status=in_progress \
  annotation='正在点击 Primary CTA'
```

## 数据文件

| 文件 | Schema |
| --- | --- |
| `run-state.json` | [schemas/audit-run.schema.json](../../schemas/audit-run.schema.json) |
| `run-events.ndjson` | 见 [live-run-protocol.md](../../.claude/skills/audit/references/live-run-protocol.md) |
| `audit-report.json` | 结束时写入 [audit-report.schema.json](../../schemas/audit-report.schema.json) |

## 设计参考

- [docs/live-audit-workflow.md](../../docs/live-audit-workflow.md) — 架构与 [markdown-viewer/skills](https://github.com/markdown-viewer/skills) BPMN/时间线对照
- [DESIGN.md](../../DESIGN.md) — 颜色与排版 token
