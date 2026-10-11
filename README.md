[English](README.en.md)

# 游戏市场研究总监

### 看清市场，决定下一步。

决定一个游戏怎么进入市场，要把玩家与玩法、IP、地区渠道、语言文化、付费方式、竞争和团队产能放在一起看。这个 Skill 引导 Agent 建比较底稿，保留证据，再把关键缺口变成验证任务。

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-zh.png?v=depth-v4">
  <img src="assets/readme/hero-zh.webp?v=depth-v4" width="100%" alt="把类型、IP、地区、语言和付费方式，放进同一轮有证据的决策。">
</picture>

[下载完整介绍 · 24 秒 MP4](assets/readme/hero-zh.mp4?raw=true) · [GIF](assets/readme/hero-zh.gif) · [文字版](assets/readme/transcript-zh.md)

## 装好，然后直接说

```sh
npx skills add https://github.com/NewenergyEric/game-market-intelligence
```

在支持 Agent Skills 的工具中安装，例如 Codex、Claude Code、Cursor；将资料放进 Agent 能读取的位置，再描述问题。

### 跨类型选择

> 我们擅长社区叙事。比较 Merge 手游、IP 社交和买断模拟：各自适合谁、靠什么收入、对内容产能要求如何？

得到六维对照、可核对来源、差异与缺口；不会把跨平台收入直接排成名次。

### 进入新地区

> 同一玩法进日本、北美、巴西，语言、支付、渠道、文化适配和竞争分别要验证什么？

按地区建立研究计划与证据表。付费数据库或本地指标不可用时，明确标为未知。

### 从观察到下一轮实验

> 支持 12 种语言能说明什么？我们还缺哪些证据才适合立项？

区分语言能力与市场表现，把 CPI/LTV、IP 条款、内容与本地化产能交给对应负责人验证。

## 看一个具体案例

**真实公开研究：Gossip Harbor、MONOPOLY GO!、Stardew Valley。** 三款产品 × 六个比较维度，18 个带证据 ID 的单元；覆盖类型、IP、地区、语言、付费与产能。保留原 Merge 行业案例，新增跨类型比较。

[完整分析与可下载底稿](case-studies/cross-market-entry/README.md)

[![游戏市场研究总监](case-studies/cross-market-entry/dashboard-zh.png?v=depth-v4)](case-studies/cross-market-entry/dashboard-zh.png)

[继续看 Merge 行业的收入、增长与集中度案例](case-studies/merge-community-public-signals/README.md)

## 最后交给团队什么

- 跨类型比较底稿 — `comparison.csv`
- 可分享研究报告 — `report.html`
- 结论、来源与缺口 — `report.json`

<details>
<summary>能力边界、说明书与验证</summary>

79 个国内外数据源入口不等于 79 个已连接 API。单款估算、财报分部、商店观察分别保留口径；语言不等于地区收入，授权 IP 不等于获得我方使用权。公开比较不包含投放实验或未取得的付费数据。

核心工具使用 Python 3.10+ 标准库；动画源码是可选的 Remotion 工程。

[人类说明书](docs/HUMAN-GUIDE.md) · [Agent guide](docs/AGENT-GUIDE.md) · [SKILL.md](SKILL.md) · [Tests and review](evals/) · [Motion source](motion/README.md)

```sh
python -m unittest discover -s tests -v
python scripts/check_presentation.py
```

</details>

[MIT License](LICENSE) · Made by Eric and Agents.

## 四个岗位，共同做出值得做的游戏

个人制作者可以轮流承担四个岗位；团队通过同一份资料交接：什么值得做、竞对做了什么、资源和体量如何评估，以及如何创作自己的核心美术。

[岗位如何交接证据、范围与美术资产](docs/WORKFLOW.md) · [Art Director](https://github.com/NewenergyEric/art-director-skill)

![市场研究、竞品拆解、项目评估与核心美术创作；样板与成本反馈推动前序决定修订。](assets/readme/workflow-zh.png)
