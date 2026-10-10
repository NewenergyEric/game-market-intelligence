# Human Guide · Game Market Intelligence Director

[中文](HUMAN-GUIDE.md)

## What this role solves

It turns “Is this Merge/community game worth pursuing, what should we test first, who should we compare, and where is the risk?” into dated, scoped, sourced research. It supports decisions; it does not buy data automatically or approve a project for the accountable lead.

## 30-second start

1. Give the agent the project brief, platform, region, target audience, and decision to support.
2. Ask it to read `SKILL.md`, then run:

   ```text
   python scripts/intelligence.py sources --topic market --region china --platform mobile
   python scripts/intelligence.py validate case-studies/merge-community-public-signals/report.json
   python scripts/intelligence.py report case-studies/merge-community-public-signals/report.json --out outputs/merge-report
   ```

3. Read the decision summary, risks, and next validation before the comparison tables.
4. Only a lead-confirmed decision may enter the production manager's execution baseline.

## What you provide

Platform and region, research target, time window, competitor scope, budget or resource constraints, and the decision the research must support. Public sources and user exports are acceptable when paid access is unavailable, but the report must state the gap.

## What you receive

Research scope, source routing, metric definitions, evidenced observations, separated facts and estimates, risks, unknowns, and handoff questions. Missing values remain `null`; the role does not invent revenue or success probabilities.

## Review before use

Check business date, region, platform, currency, sample coverage, source independence, and estimation method. Any number that can change the project decision should retain either first-party disclosure or a clear third-party method statement.
