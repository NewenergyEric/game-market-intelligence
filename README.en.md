[中文](README.md)

[**Game Dev Skills**](https://github.com/NewenergyEric/NewenergyEric/blob/main/GAME-DEV-SKILLS.en.md) · [Market research](https://github.com/NewenergyEric/game-market-intelligence/blob/main/README.en.md) · [Reverse analysis](https://github.com/NewenergyEric/game-reverse-analyst/blob/main/README.en.md) · [Production planning](https://github.com/NewenergyEric/game-production-manager/blob/main/README.en.md) · [Art direction](https://github.com/NewenergyEric/art-director-skill/blob/main/README.en.md)

# Game Market Intelligence Director

### Read the market. Choose the next move.

A market decision connects audience and genre with IP, regional channels, culture, payment, competition and team capacity. This Skill guides your agent through evidence-backed comparisons and turns critical gaps into concrete research tasks.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-en.png?v=depth-v4">
  <img src="assets/readme/hero-en.webp?v=depth-v4" width="100%" alt="Compare genre, IP, region, language and monetization in one evidence-led decision.">
</picture>

[Download the full 24-second introduction · MP4](assets/readme/hero-en.mp4?raw=true) · [GIF](assets/readme/hero-en.gif) · [Transcript](assets/readme/transcript-en.md)

## Why this exists

**A greenlight needs a comparison you can reason about.**

Charts, storefronts and industry reports each tell part of the story. The decision connects audience, genre, region, payment and the team’s content capacity. Research should leave sources, meaningful differences and the next questions to test.

This is the market role in Game Dev Skills. Narrow the directions worth studying, hand the questions to reverse analysis, and carry evidence and gaps into production assessment. A solo creator can wear all four hats; a team can hand off by role.

## Install, then ask your agent

```sh
npx skills add https://github.com/NewenergyEric/game-market-intelligence
```

Install in an Agent Skills-compatible tool such as Codex, Claude Code or Cursor. Put your materials where the agent can read them, then describe the question.

### Compare product routes

> Our team knows community storytelling. Compare Merge mobile, IP-led social and paid simulation: audience, revenue model and content workload.

Receive a six-axis comparison with sources, differences and open questions; no cross-platform revenue ranking.

### Enter a new region

> What should we validate for Japan, North America and Brazil: language, payment, distribution, culture and competitors?

Build a regional research plan and evidence table. Unavailable paid data and local metrics remain explicitly unknown.

### Turn observations into tests

> What does support for 12 languages establish? What evidence is still missing before greenlighting?

Separate product capability from commercial performance; assign CPI/LTV, IP terms and localization capacity research to accountable roles.

## See a concrete case

**Real public-source research: Gossip Harbor, MONOPOLY GO! and Stardew Valley.** Three products × six lenses, with 18 evidence-linked cells covering genre, IP, region, language, payment and capacity. The original Merge industry case remains available.

[Full analysis and downloadable records](case-studies/cross-market-entry/README.en.md)

[![Game Market Intelligence Director](case-studies/cross-market-entry/dashboard-en.png?v=depth-v4)](case-studies/cross-market-entry/dashboard-en.png)

[Explore the existing Merge revenue, growth and concentration case](case-studies/merge-community-public-signals/README.en.md)

## What the team receives

- Cross-genre comparison — `comparison.csv`
- Shareable research report — `report.html`
- Findings, sources and gaps — `report.json`

<details>
<summary>Boundaries, guides and validation</summary>

79 domestic and international source entries are not 79 connected APIs. Title estimates, company segments and storefront observations retain their own scope. Language support is not regional revenue; a licensed competitor IP does not grant us usage rights. This case contains no ad experiment or unavailable paid data.

Core helpers use Python 3.10+ and the standard library. Remotion is optional presentation tooling.

[Human guide](docs/HUMAN-GUIDE.en.md) · [Agent guide](docs/AGENT-GUIDE.en.md) · [SKILL.md](SKILL.en.md) · [Tests and review](evals/) · [Motion source](motion/README.md)

```sh
python -m unittest discover -s tests -v
python scripts/check_presentation.py
```

</details>

[MIT License](LICENSE) · Made by Eric and Agents.

## Tell me where the handoff breaks

After trying one task, share the goal, public inputs, actual output and what was still missing.

[Share feedback or a case](https://github.com/NewenergyEric/game-market-intelligence/issues/new?template=use-case.yml)

## Four roles. One game worth making.

For a solo creator these are four hats; for a team they are connected responsibilities. Explore what is worth making, what competitors do, the resources it requires, and the original art that defines it.

[How the roles exchange evidence, scope and visual assets](docs/WORKFLOW.en.md) · [Explore all four roles](https://github.com/NewenergyEric/NewenergyEric/blob/main/GAME-DEV-SKILLS.en.md)

| Your question | Start here | Carry forward |
|---|---|---|
| What is worth making? | [Market research](https://github.com/NewenergyEric/game-market-intelligence/blob/main/README.en.md) | Options, sources and validation gaps |
| How does it work? | [Reverse analysis](https://github.com/NewenergyEric/game-reverse-analyst/blob/main/README.en.md) | Rules, implementation evidence and asset BOM |
| Can we scope and deliver it? | [Production planning](https://github.com/NewenergyEric/game-production-manager/blob/main/README.en.md) | SOW, work packages, dependencies and acceptance |
| What defines the art? | [Art direction](https://github.com/NewenergyEric/art-director-skill/blob/main/README.en.md) | Shared rules, representative samples and project pack |

**Solo creator:** start with the question blocking you and switch roles as needed. **Team:** hand off actual reports, BOMs, work packages and art rules, keeping sources, versions and open decisions visible.

This is a collaboration method; it does not include an orchestrator that automatically runs four agents in sequence.

![Market intelligence → competitor analysis → production assessment → original art direction; prototype and cost feedback revise earlier decisions.](assets/readme/workflow-en.png)
