<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme/hero-dark.svg">
  <img src="assets/readme/hero-light.svg" width="100%" alt="Brandon Shay, AI Engineer in Orange County, CA. I design AI systems end to end: the spec, the evals and the gates. I build with coding agents and own what ships. Loop: spec and slices (me), build with TDD (agent), tests and judges (agent), eval gate (me), approve and commit (me), with lessons feeding the next spec.">
</picture>

<p align="center">
  <a href="https://linkedin.com/in/brandonpshay"><img alt="LinkedIn: brandonpshay" src="https://img.shields.io/badge/LinkedIn-brandonpshay-0A66C2?style=flat-square&logo=linkedin&logoColor=white"></a>
  <img alt="Open to AI Engineer roles" src="https://img.shields.io/badge/Open_to-AI_Engineer_roles-1f8a5b?style=flat-square">
</p>

**Enterprise systems by background. AI engineering with evals and gates by practice.** I'm an Enterprise IT Systems Engineer (GCP, Workato, Google Workspace) moving full-time into AI engineering. I build with Claude Code as my pair and keep the judgment calls: what to build, how it is proven and what is allowed to ship.

## How I work

- **I own the decisions.** The problem, the spec, the architecture and when to stop. Margin Invest went live with a handful of test users, then I shut it down when the market was not there.
- **Agents build inside gates I set.** Spec, vertical slices, TDD with a captured failing test, a judge panel, then my approval before anything commits. I packaged that loop as [assay](https://github.com/ShadyBad/assay) and use it on my current work.
- **Evals decide what ships.** Golden sets with hand-labelled cases, LLM-as-judge with pinned prompts, and pass thresholds enforced in code.
- **Observable and typed by default.** Pydantic at the boundaries, lint and pytest gates in CI, cost metered per LLM call.
- **I learn the fundamentals by hand.** I work through a structured AI engineering curriculum writing the Python myself, so I can read, debug and own what agents produce.

## Work

<p>
<a href="https://github.com/ShadyBad/margin_invest"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/card-margin-invest-dark.svg"><img src="assets/readme/card-margin-invest-light.svg" width="100%" alt="Margin Invest: deterministic equity research platform, shipped then retired in May 2026. Pipeline: 3,056 tickers, 7 elimination filters, 4 scoring pillars, a 10-K risk factor diff judged by Claude, then human approval before publishing. 546 tests, 95% engine coverage gate, a 106-case eval set, 2,038 commits."></picture></a><br><a href="https://github.com/ShadyBad/assay"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/card-assay-dark.svg"><img src="assets/readme/card-assay-light.svg" width="50%" alt="assay: a Claude Code plugin that assays AI-written code before it merges with spec, TDD, judges and gates. My call: a test that never failed proves nothing. 29 judges, 175 tests, MIT."></picture></a><a href="https://github.com/ShadyBad/notionIQ"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/card-notioniq-dark.svg"><img src="assets/readme/card-notioniq-light.svg" width="50%" alt="notionIQ: classifies a Notion workspace with Claude and recommends a cleanup. My call: cost controls ship with the features. 50 tests, mypy and pytest in CI, 3 LLM providers."></picture></a><br><a href="https://github.com/ShadyBad/ai-jobs"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/card-ai-jobs-dark.svg"><img src="assets/readme/card-ai-jobs-light.svg" width="50%" alt="ai-jobs: a Claude Code workspace that searches US job boards, scores fit, tailors the CV and preps interviews. My call: your profile never leaves your machine. 89 tests, BLS salary data, Typer and httpx."></picture></a><a href="https://github.com/ShadyBad/it-automation-tools"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/card-it-automation-tools-dark.svg"><img src="assets/readme/card-it-automation-tools-light.svg" width="50%" alt="it-automation-tools: endpoint automation for Windows and macOS fleets managed with Intune, SCCM and Kandji. My call: native OS tools, minimal dependencies. PowerShell, Bash, Python with Polars."></picture></a>
</p>

## Shipped with

Every row links to public code that uses it.

| Area | Tools | Proof |
|---|---|---|
| AI | Claude API (prompt caching, per-call cost metering), Voyage embeddings, LLM-as-judge evals, Claude Code skills, subagents, hooks and plugins | [margin_invest](https://github.com/ShadyBad/margin_invest), [assay](https://github.com/ShadyBad/assay), [notionIQ](https://github.com/ShadyBad/notionIQ) |
| Backend | Python 3.13, FastAPI, Pydantic, SQLAlchemy, Postgres, Redis + ARQ workers, Typer, httpx | [margin_invest](https://github.com/ShadyBad/margin_invest), [ai-jobs](https://github.com/ShadyBad/ai-jobs) |
| Frontend | Next.js, React, TypeScript | [margin_invest/web](https://github.com/ShadyBad/margin_invest/tree/main/web) |
| Quality | pytest, Ruff, mypy, coverage gates, GitHub Actions | [margin_invest](https://github.com/ShadyBad/margin_invest), [assay](https://github.com/ShadyBad/assay), [notionIQ](https://github.com/ShadyBad/notionIQ), [ai-jobs](https://github.com/ShadyBad/ai-jobs) |
| Ops | uv, Docker, Railway, Vercel, Sentry, PostHog | [margin_invest](https://github.com/ShadyBad/margin_invest) |
| Enterprise | GCP, Google Workspace, Workato, Intune, Kandji, PowerShell | day job, [it-automation-tools](https://github.com/ShadyBad/it-automation-tools) |

## Let's talk

I'm open to AI Engineer roles. The fastest way to reach me is [LinkedIn](https://linkedin.com/in/brandonpshay).

<sub>Built with Claude Code. Every claim on this page was checked against public code before it shipped.</sub>
