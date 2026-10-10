# Game Market Intelligence Director · Human guide

[中文](HUMAN-GUIDE.md)

Turn a greenlight question into sourced findings and a practical next test.

## Bring your materials

Give your agent the idea, target market and decision you need to make.
Incomplete material is fine to start; missing inputs that affect the next step stay visible.

## I have a direction. What should we research?

> Use `$game-market-intelligence`. We are exploring Merge + community for overseas mobile markets. Frame the research, check public signals, and show the opportunity, key risks and what to test next.

A research scope, sourced findings, missing inputs and a proposed validation plan. The agent asks only for information that affects the current call.

## I have several reports. Are the numbers comparable?

> Check these competitor reports for region, platform, period and metric definitions. Separate publisher disclosures, third-party estimates and unknowns. Build a table of what we can actually compare.

A comparable evidence table, original sources, numbers that cannot be added or compared directly, and a plan for filling gaps.

## We need a review brief for the team

> Turn this research into a decision brief. Lead with the recommendation, risks and next test; attach sources, definitions and unknowns. List the decisions that need an owner.

A readable report and a structured record another agent can continue. After the owner decides, hand the direction to analysis or production planning.

## How to review

The catalog contains 77 domestic and international research sources across mobile, PC/console, industry reports, company disclosures, advertising and player observations. A catalog entry is a research route; accounts, paid data and API access come from the working environment.

Third-party revenue stays estimated, financial disclosures keep their stated scope, and missing values remain unknown. The owner makes the final decision.

## Outputs and handoff

- **Research call:** the project question, opportunity, risks and next validation.
- **Evidence record:** traceable sources, dates, regions, platforms and definitions.
- **Shareable report:** HTML, Markdown and JSON generated from one input.

Research supplies evidence and open questions. The [Reverse Analyst](https://github.com/NewenergyEric/game-reverse-analyst) explains competitor structure. The [Production Manager](https://github.com/NewenergyEric/game-production-manager) turns confirmed direction into tasks. [Art Director](https://github.com/NewenergyEric/art-director-skill) builds the professional visual rules.

## Technical entry for your agent

Python 3.10+; the core uses the standard library. Six deterministic tests cover evidence requirements, unknowns, HTML escaping and source routing.

```sh
python scripts/intelligence.py validate case-studies/merge-community-public-signals/report.json
python scripts/intelligence.py report case-studies/merge-community-public-signals/report.json --out outputs/merge-report
```
