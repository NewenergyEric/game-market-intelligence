# Agent Guide · game-market-intelligence

[中文](AGENT-GUIDE.zh.md)

## Read order

Read `SKILL.md` first, then open `references/research-method.md`, `references/source-catalog.md`, and `data/sources.json` as needed. Call `scripts/intelligence.py` only when routing sources, validating input, or rendering a report.

## Standard workflow

1. Extract platform, region, subject, period, metrics, decision, and evidence budget.
2. Route sources and record access state, independence, lineage, and limits.
3. Keep facts, estimates, inferences, recommendations, and unknowns separate in the input JSON.
4. Run `validate`, then `report` to create HTML, Markdown, and the preserved JSON.
5. Return a decision summary, evidence chain, risks, next validation, and handoff questions.

## Failure branches

- Account or API unavailable: use a public page or user export and record the access gap.
- Sources share upstream data: document lineage and do not double-count them.
- Estimate has no method: preserve the estimate label and limit; do not promote it to fact.
- Critical field missing: return `null`, a reason, and a collection path.
- Finding changes project scope: stop at accountable-lead confirmation before production handoff.

## Output contract

At minimum include `decision_summary`, `evidence`, `risks`, `next_validation`, and `handoff_questions`. Every citation needs source, business date, collection time, region/platform, metric definition, and coverage gap.

Do not present the catalog as connected APIs, ratings as revenue, Steam activity as sales, company financials as title-level revenue, or a market proposal as an approved production task.

## Depth-case entry

[Protocol](../references/market-lenses.en.md) · [Case](../case-studies/cross-market-entry/README.en.md)

```sh
python scripts/intelligence.py validate case-studies/cross-market-entry/report.en.json
python scripts/intelligence.py report case-studies/cross-market-entry/report.en.json --out outputs/cross-market --lang en
```

## Tool input schema

The output contract above describes human-facing report content, not the JSON schema accepted by intelligence.py. CLI fields are id, title, question, scope, claims, recommendation and unknowns, with optional comparison. Each comparison cell references claims through claim_ids. Use case-studies/cross-market-entry/report.en.json as the executable example; do not substitute report section names such as decision_summary for CLI fields.
