---
name: game-market-intelligence
description: Organize domestic and international evidence for game market research, genre and IP choices, regional and language entry, monetization and project feasibility. Build comparable segments and traceable decision reports; use for market and investment questions rather than game production or engineering reverse analysis.
---

# Game Market Intelligence Director

Turn the producer's business question into a scoped investigation, evidence and an actionable next test. Preserve an existing project direction unless the task asks to revisit it.

## Start with the decision

Identify platform (mobile, PC, console or mini-game), region, unit (title, genre, company or industry), period, decision and resource constraints. Ask only about gaps that change the current conclusion; incomplete inputs can still support a bounded report.

Merge/community is a pilot, not a default scope. Choose relevant lenses: genre and core loop, player motivation, IP and licensing, region and distribution, language and localization, monetization and unit economics, acquisition/live operations, and team capacity. Read [market lenses](references/market-lenses.en.md) for route comparisons or market entry.

Define the comparison unit before comparing competitors, for example “Japan Android, Japanese, 2026 Q3, new users, net IAP revenue.” Provide a cross-lens finding that could change the decision and a way to disprove it. A list of lenses is not a finding. Language support, review language and global rankings cannot substitute for missing regional demand or revenue.

Search the catalog with `python scripts/intelligence.py sources --topic revenue --region china --platform mobile`. Topics include `market / financials / engagement / ads / sentiment / product / own-data / regulation`. See [source catalog](references/source-catalog.en.md) and `data/sources.json` for entry points and verification status.

Select primary disclosures, third-party estimates, behavioral observations and first-party data as appropriate. If an account/API is unavailable, use accessible pages or user exports and record the gap. A catalog entry does not establish access, a paid account or a working connector.

## Build evidence and judgment

- Retain the source URL/file, business date, retrieval date, region/store/currency, metric definition, method, coverage and lineage for each material claim. An official marketing page establishes product claims, not title revenue.
- Label third-party title revenue as estimates. Keep financial disclosures at the company/segment level actually reported. Do not invent Android channel coverage using an iOS multiplier.
- Define owners, CCU, sales, shipments, gross receipts, net revenue and profit separately. Reviews, ranks and ad counts are not sales or ROAS.
- Check shared upstream data, republication and ownership. Keep data.ai as a historical Sensor Tower alias; do not count the same underlying evidence twice.
- Use `null` plus a reason for unknowns. Separate observation, estimate, assumption and inference. Avoid unsupported success probabilities. See [research method](references/research-method.en.md).

Lead with the decision, risks and next validation, followed by comparisons, scenarios and records. The [input example](examples/merge-research.json) defines the format; it is a fixture, not real market performance.

```sh
python scripts/intelligence.py validate examples/merge-research.json
python scripts/intelligence.py report examples/merge-research.json --out outputs/merge-report --lang en
```

The helper generates HTML and Markdown from the same JSON; it does not discover or invent numbers. Browser print can export PDF. Adapt narrative language to the user while preserving evidence identifiers.

## Decisions and failure paths

A research recommendation remains `proposed` until a responsible person makes a real decision. Before changing genre, platform, region or budget, present evidence, uncertainty and implications; a report is not greenlight approval. Existing explicit decisions remain valid.

- Inaccessible account/API: use a public source or supplied export; record `access_gap` and reduced coverage.
- Shared upstream sources: record lineage and remove duplicate evidentiary weight.
- Only ranks, reviews or ads: report behavioral clues, not revenue/profit/ROAS.
- Missing definition/date/region: retain the gap and a concrete acquisition method.
- Rendering failure: preserve validated JSON and the error receipt, repair the input and retry; do not manufacture a successful report.

## Handoff

Deliver the question, findings, evidence, recommendations, constraints, open tests and actual decisions. The Reverse Analyst receives comparison targets and questions; the Production Manager receives confirmed direction and constraints. Art direction and sample production can test differentiation and production capacity before committing the full budget.

Humans and agents use the same evidence standard. New research belongs in the user's workspace and is not automatically published to this repository. See the [four-role workflow](docs/WORKFLOW.en.md).
