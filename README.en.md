[中文](README.md)

# Game Market Intelligence Director

### Read the market. Choose the next move.

A market decision connects audience and genre with IP, regional channels, culture, payment, competition and team capacity. This Skill guides your agent through evidence-backed comparisons and turns critical gaps into concrete research tasks.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-en.png?v=depth-v4">
  <img src="assets/readme/hero-en.webp?v=depth-v4" width="100%" alt="Compare genre, IP, region, language and monetization in one evidence-led decision.">
</picture>

[Download the full 24-second introduction · MP4](assets/readme/hero-en.mp4?raw=true) · [GIF](assets/readme/hero-en.gif) · [Transcript](assets/readme/transcript-en.md)

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

[Human guide](docs/HUMAN-GUIDE.en.md) · [Agent guide](docs/AGENT-GUIDE.en.md) · [SKILL.md](SKILL.md) · [Tests and review](evals/) · [Motion source](motion/README.md)

```sh
python -m unittest discover -s tests -v
python scripts/check_presentation.py
```

</details>

[MIT License](LICENSE) · Made by Eric and Agents.
