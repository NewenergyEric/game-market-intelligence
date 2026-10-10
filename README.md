[English](README.en.md)

# 游戏市场研究总监

### 看清市场，决定下一步。

**给制作人一个能继续行动的答案。**

输入项目方向、目标市场和要做的决定。Agent 帮你选来源、对齐竞品口径、整理机会与风险，最后给出一轮具体的验证建议。已有研究可以接着补，资料不齐也能先写清已知与缺口。

<a href="assets/readme/hero-zh.mp4"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-zh.png?v=workflow-v3">
  <img src="assets/readme/hero-zh.gif?v=workflow-v3" width="100%" alt="把一个立项问题，变成有来源的判断和下一轮验证。">
</picture></a>

[24 秒，走完一次完整工作 · 播放 MP4](assets/readme/hero-zh.mp4) · [文字版](assets/readme/transcript-zh.md)

## 装好，然后直接说

在支持 Agent Skills 的工具中安装，例如 Codex、Claude Code 或 Cursor：

```sh
npx skills add https://github.com/NewenergyEric/game-market-intelligence
```

把资料放进 Agent 能读取的文件夹，再说出要解决的问题。文件整理和命令由 Agent 处理。

### 我有一个方向，想知道先查什么

> 使用 `$game-market-intelligence`。我们沿用 Merge＋社区方向，目标是海外手游。先帮我整理研究问题，核对公开市场信号，告诉我机会、主要风险和下一步最值得验证的事。

**你会得到：** 研究范围、带来源的判断、待补问题和验证建议。Agent 只补问影响当前结论的资料。

### 我拿到几份数据，想知道能不能放在一起比较

> 这些是竞品数据和报告。帮我核对地区、平台、时间与指标定义，分清一方披露、第三方估算和未知，把真正可比的内容整理成表。

**你会得到：** 可比较的证据表、原始出处、不能直接相加或对比的数字，以及补数方法。

### 准备开评审会，要把研究交给团队

> 把这轮研究整理成决策简报。先说建议、风险和下一次验证，再附来源、口径和未知项；把需要负责人决定的内容单列。

**你会得到：** 人能阅读的报告与 Agent 能继续处理的底稿。负责人确认后，再交给拆解或项目管理岗位。

## 最后交给团队什么

- **研究判断：** 项目问题、机会、主要风险与下一次验证。
- **证据底稿：** 来源、日期、平台、地区和指标定义都可追溯。
- **可分享报告：** HTML、Markdown 和 JSON 来自同一份输入。

## 看一份真实研究：Merge＋社区

[公开信号案例](case-studies/merge-community-public-signals/README.md)从 Google Play、Metacore 披露与 AppMagic 支持的行业报告出发，得到一个具体判断：品类份额扩大，但头部收入集中，下一步应验证切入方式。

2025 年的品类数字保留估算标签；商店快照和生命周期披露分开使用。我方 CPI、LTV、留存和产能仍是待补项。

[![看一份真实研究：Merge＋社区](case-studies/merge-community-public-signals/dashboard-zh.png?v=workflow-v3)](case-studies/merge-community-public-signals/dashboard-zh.png)

## 和其他岗位一起用

市场研究给出证据与待验证问题；[拆解分析师](https://github.com/NewenergyEric/game-reverse-analyst)理解竞品结构；[项目经理](https://github.com/NewenergyEric/game-production-manager)把确认后的方向拆成执行工作；[Art Director](https://github.com/NewenergyEric/art-director-skill)建立专业美术规范。

<details>
<summary><strong>安装要求、技术文档与验证</strong></summary>

Python 3.10+，核心工具仅用标准库。6 项确定性测试验证证据要求、未知保留、HTML 转义及来源路由。

[人类详细说明](docs/HUMAN-GUIDE.md) · [Agent 调用说明](docs/AGENT-GUIDE.md) · [Skill 入口](SKILL.md) · [验证与审查](evals/)

```sh
python scripts/intelligence.py validate case-studies/merge-community-public-signals/report.json
python scripts/intelligence.py report case-studies/merge-community-public-signals/report.json --out outputs/merge-report
```

[CI](https://github.com/NewenergyEric/game-market-intelligence/actions) · [Motion source](motion/README.md)

</details>

<details>
<summary><strong>能力边界与资料使用</strong></summary>

来源目录收录 77 个国内外研究入口，涵盖手游、PC／主机、行业报告、一方披露、买量和玩家观察。收录表示可研究的来源；账号、付费数据与 API 权限由使用环境提供。

第三方流水保持估算标签，财报按原披露范围使用；未知值不补成数字。研究建议交给负责人决定。

</details>

[MIT License](LICENSE) · 由 Eric 与 Agents 一起制作。
