# 游戏市场研究总监 · 使用说明

[English](HUMAN-GUIDE.en.md)

把一个立项问题，变成有来源的判断和下一轮验证。

## 准备资料

给 Agent 项目方向、目标市场和你要做的决定。
资料不齐也可以开始；影响下一步的缺项会单列，不以猜测填充。

## 我有一个方向，想知道先查什么

> 使用 `$game-market-intelligence`。我们沿用 Merge＋社区方向，目标是海外手游。先帮我整理研究问题，核对公开市场信号，告诉我机会、主要风险和下一步最值得验证的事。

研究范围、带来源的判断、待补问题和验证建议。Agent 只补问影响当前结论的资料。

## 我拿到几份数据，想知道能不能放在一起比较

> 这些是竞品数据和报告。帮我核对地区、平台、时间与指标定义，分清一方披露、第三方估算和未知，把真正可比的内容整理成表。

可比较的证据表、原始出处、不能直接相加或对比的数字，以及补数方法。

## 准备开评审会，要把研究交给团队

> 把这轮研究整理成决策简报。先说建议、风险和下一次验证，再附来源、口径和未知项；把需要负责人决定的内容单列。

人能阅读的报告与 Agent 能继续处理的底稿。负责人确认后，再交给拆解或项目管理岗位。

## 如何复核

来源目录收录 77 个国内外研究入口，涵盖手游、PC／主机、行业报告、一方披露、买量和玩家观察。收录表示可研究的来源；账号、付费数据与 API 权限由使用环境提供。

第三方流水保持估算标签，财报按原披露范围使用；未知值不补成数字。研究建议交给负责人决定。

## 输出与交接

- **研究判断：** 项目问题、机会、主要风险与下一次验证。
- **证据底稿：** 来源、日期、平台、地区和指标定义都可追溯。
- **可分享报告：** HTML、Markdown 和 JSON 来自同一份输入。

市场研究给出证据与待验证问题；[拆解分析师](https://github.com/NewenergyEric/game-reverse-analyst)理解竞品结构；[项目经理](https://github.com/NewenergyEric/game-production-manager)把确认后的方向拆成执行工作；[Art Director](https://github.com/NewenergyEric/art-director-skill)建立专业美术规范。

## 给 Agent 的技术入口

Python 3.10+，核心工具仅用标准库。6 项确定性测试验证证据要求、未知保留、HTML 转义及来源路由。

```sh
python scripts/intelligence.py validate case-studies/merge-community-public-signals/report.json
python scripts/intelligence.py report case-studies/merge-community-public-signals/report.json --out outputs/merge-report
```
