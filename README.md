<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme/hero-dark.svg">
  <img src="assets/readme/hero-light.svg" width="100%" alt="~ $ whoami. I build AI systems and the evals that measure them. Orange County, CA. Open to AI Engineer roles.">
</picture>

<br>

```python
brandon = {
    "from": "Enterprise IT Systems Engineering",
    "builds_with": ["Claude Code", "Codex"],
    "owns": ["the spec", "the tests", "what ships"],
}
```

<br>

<a href="https://github.com/bshay13/margin_invest"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/link-margin-invest-dark.svg"><img src="assets/readme/link-margin-invest-light.svg" width="100%" alt="Margin Invest"></picture></a>

Equity research on 3,056 tickers. Seven elimination filters, four sector-neutral scoring pillars, a 13F smart-money overlay, then Kelly sizing.

Claude read each 10-K for risk factors that changed, with an eval harness of 106 labelled filing pairs to score it. Nothing reached a user without my approval. 2,038 commits and 8,034 tests, retired in 2026 when the market wasn't there.

Every formula is tested against a real filing.

```python
# engine/tests/fixtures/golden_apple_2024.py
EXPECTED = {
    "gross_margin_2024": 0.4621,  # 180683 / 391035
    "revenue_growth":    0.0202,  # (391035 - 383285) / 383285
    "roa_2024":          0.2568,  # 93736 / 364980
}
```

A model trains on 20 seeds and stages only if the whole spread clears the gate. One lucky seed can't ship.

```python
# engine/src/margin_engine/ml/seed_validation.py
@dataclass
class SeedValidationThresholds:
    min_median_rank_ic: float = 0.15
    max_rank_ic_cv: float = 0.50
    min_worst_seed_ic: float = 0.05
```

<br>

<a href="https://github.com/bshay13/assay"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/link-assay-dark.svg"><img src="assets/readme/link-assay-light.svg" width="100%" alt="assay"></picture></a>

A review gate for AI-written code, built as a Claude Code plugin. I scope the work and test it by hand. The middle runs on its own, and nothing commits without my sign-off.

```console
$ /spec          # grill the goal into a PRD, one question at a time
$ /to-tickets    # cut it into vertical slices with a blocked_by DAG
$ /implement     # red, green, judges, a 9-check done gate, then stop
$ /qa            # I test it by hand; findings become new tickets
```

Risk sets how hard each diff gets reviewed, from no judges up to 29.

```python
JUDGES = {
    "TRIVIAL":  "none",                # typo, formatting, comments
    "LOW":      "1-2 Tier 1",          # rename, test-only change
    "MEDIUM":   "3-5 Tier 1",          # new function, business logic
    "HIGH":     "Tier 1 + two Tier 2", # scoring formula, auth, migration
    "CRITICAL": "Tier 1 + 2 + 3",      # prod deploy, money-moving path
}
```

<br>

### Smaller tools

<p><a href="https://github.com/bshay13/notionIQ"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/tool-notioniq-dark.svg"><img src="assets/readme/tool-notioniq-light.svg" width="33.33%" alt="notionIQ. Claude reads a Notion workspace and proposes a cleanup. 50 tests."></picture></a><a href="https://github.com/bshay13/ai-jobs"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/tool-ai-jobs-dark.svg"><img src="assets/readme/tool-ai-jobs-light.svg" width="33.33%" alt="ai-jobs. My job search, run from Claude Code. Listings, fit scores, tailored CVs. 89 tests."></picture></a><a href="https://github.com/bshay13/it-automation-tools"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/tool-it-automation-tools-dark.svg"><img src="assets/readme/tool-it-automation-tools-light.svg" width="33.33%" alt="it-automation-tools. Zscaler cert trust, weekly restarts and Edge repair for Windows and Mac. 5 scripts."></picture></a></p>

<br>

<a href="https://linkedin.com/in/brandonpshay"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/readme/link-linkedin-dark.svg"><img src="assets/readme/link-linkedin-light.svg" width="100%" alt="Say hello on LinkedIn"></picture></a>
