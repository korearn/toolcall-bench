# DEVLOG

Newest entry first. One entry per work session: what was done, decisions, next step.

## 2026-11-12 — Milestone 0: scaffold

**Done**

- Chose the project: a deterministic tool-calling eval harness for local models (Ollama, 16 GB VRAM).
- Created the repo with `src/` layout, uv, ruff, pytest and a GitHub Actions workflow (lint, format check, tests).
- Added a `tcb` CLI entry point with `--version` and two smoke tests.
- Wrote the README skeleton (problem, architecture diagram, quickstart) and the MIT license.

**Decisions**

- Scoring is deterministic (schema + exact match), no LLM-as-judge: results must be reproducible and cheap to rerun.
- Ollama native `/api/chat` over the OpenAI-compatible endpoint: the native response carries the token counts and durations needed for tokens/s.
- Model calls run sequentially: one GPU, and concurrency would distort latency numbers.
- Out of scope for v0.1: web UI, cloud providers, multi-step agent loops, backends other than Ollama.

**Next step**

- Milestone 1: Pydantic models for `Case` / `ToolSpec` / `Expected`, a YAML suite loader, and `tcb validate suites/core` with 5 sample cases.
