# Agent Guide · game-market-intelligence

[中文](AGENT-GUIDE.md)

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
