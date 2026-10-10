[中文](README.md)

# Game Market Intelligence Director

### Read the market. Choose the next move.

**Give the producer an answer they can act on.**

Bring a project direction, target market and decision. Your agent selects sources, aligns competitor definitions, identifies opportunities and risks, and proposes a concrete next test. Continue existing research; incomplete inputs can still produce a useful first pass with visible gaps.

<a href="assets/readme/hero-en.mp4"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-en.png?v=workflow-v3">
  <img src="assets/readme/hero-en.gif?v=workflow-v3" width="100%" alt="Turn a greenlight question into sourced findings and a practical next test.">
</picture></a>

[24 seconds through one complete workflow · Watch MP4](assets/readme/hero-en.mp4) · [Transcript](assets/readme/transcript-en.md)

## Install, then ask your agent

Install in an Agent Skills-compatible tool, such as Codex, Claude Code or Cursor:

```sh
npx skills add https://github.com/NewenergyEric/game-market-intelligence
```

Put the materials where your agent can read them, then describe the problem. Your agent handles file organization and commands.

### I have a direction. What should we research?

> Use `$game-market-intelligence`. We are exploring Merge + community for overseas mobile markets. Frame the research, check public signals, and show the opportunity, key risks and what to test next.

**You get:** A research scope, sourced findings, missing inputs and a proposed validation plan. The agent asks only for information that affects the current call.

### I have several reports. Are the numbers comparable?

> Check these competitor reports for region, platform, period and metric definitions. Separate publisher disclosures, third-party estimates and unknowns. Build a table of what we can actually compare.

**You get:** A comparable evidence table, original sources, numbers that cannot be added or compared directly, and a plan for filling gaps.

### We need a review brief for the team

> Turn this research into a decision brief. Lead with the recommendation, risks and next test; attach sources, definitions and unknowns. List the decisions that need an owner.

**You get:** A readable report and a structured record another agent can continue. After the owner decides, hand the direction to analysis or production planning.

## What the team receives

- **Research call:** the project question, opportunity, risks and next validation.
- **Evidence record:** traceable sources, dates, regions, platforms and definitions.
- **Shareable report:** HTML, Markdown and JSON generated from one input.

## Read a real study: Merge + community

The [public-signal case](case-studies/merge-community-public-signals/README.en.md) uses Google Play, Metacore disclosures and an AppMagic-backed industry report. Its call is specific: category share expanded, leaders retain a concentrated share, and the entry point needs a test.

2025 genre figures remain estimates. Store snapshots and lifetime disclosures keep separate definitions. Our CPI, LTV, retention and capacity remain open questions.

[![Read a real study: Merge + community](case-studies/merge-community-public-signals/dashboard-en.png?v=workflow-v3)](case-studies/merge-community-public-signals/dashboard-en.png)

## Work with the other roles

Research supplies evidence and open questions. The [Reverse Analyst](https://github.com/NewenergyEric/game-reverse-analyst) explains competitor structure. The [Production Manager](https://github.com/NewenergyEric/game-production-manager) turns confirmed direction into tasks. [Art Director](https://github.com/NewenergyEric/art-director-skill) builds the professional visual rules.

<details>
<summary><strong>Requirements, technical docs and validation</strong></summary>

Python 3.10+; the core uses the standard library. Six deterministic tests cover evidence requirements, unknowns, HTML escaping and source routing.

[Human guide](docs/HUMAN-GUIDE.en.md) · [Agent guide](docs/AGENT-GUIDE.en.md) · [Skill entry](SKILL.md) · [Validation and review](evals/)

```sh
python scripts/intelligence.py validate case-studies/merge-community-public-signals/report.json
python scripts/intelligence.py report case-studies/merge-community-public-signals/report.json --out outputs/merge-report
```

[CI](https://github.com/NewenergyEric/game-market-intelligence/actions) · [Motion source](motion/README.md)

</details>

<details>
<summary><strong>Capability boundaries and material use</strong></summary>

The catalog contains 77 domestic and international research sources across mobile, PC/console, industry reports, company disclosures, advertising and player observations. A catalog entry is a research route; accounts, paid data and API access come from the working environment.

Third-party revenue stays estimated, financial disclosures keep their stated scope, and missing values remain unknown. The owner makes the final decision.

</details>

[MIT License](LICENSE) · Made by Eric and Agents.
