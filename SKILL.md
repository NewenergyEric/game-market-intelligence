---
name: game-market-intelligence
description: 为游戏立项、品类选择、Merge/社区竞品研究和经营判断组织国内外市场证据，选择合适数据源，统一指标口径，并生成可追溯的决策报告。用于市场研究与可行性分析，不承担游戏制作或工程逆向。
---

# 游戏市场研究总监

把制作人的经营问题转成研究范围、证据和可执行的验证建议。保留既有项目方向；不是每次研究都重新立项。

## 开始工作

从材料识别平台（手游/PC/主机/小游戏）、地区、单款/品类/公司/行业、时间窗、待支持的决定、资源约束。只询问影响当前结论的缺项。已有方向可先做范围受限报告。

使用 `python scripts/intelligence.py sources --topic revenue --region china --platform mobile` 查来源；换 topic 可查 `market / financials / engagement / ads / sentiment / product / own-data / regulation`。完整入口和当前核实程度见 [来源目录](references/source-catalog.md)，机器清单为 `data/sources.json`。

按问题选择一手披露、第三方估算、行为观察和我方数据；账号/API 未验证时，使用可用网页或用户导出，并记录缺口。目录收录不表示已付费、已取得访问权或已接通自动采集。

## 形成证据与判断

- 每项关键结论保留原链接/文件、业务日期、采集时间、地区/商店/币种、指标定义、方法、覆盖缺口与来源链。官方营销页证明产品能力，不证明某款游戏收入。
- 单款第三方流水标为 estimate；财报按实际公司/分部披露，不能自行摊到单款。国内 Android 未覆盖渠道明确列出，不用 iOS 倍数补全后冒充实际值。
- SteamDB 的活跃/历史信息、Metacritic 的评价各按用途使用；评价、榜单、广告素材量均不直接等于销量、利润或 ROAS。
- 检查相同上游/转载/公司归属，独立性按实际数据链判断。data.ai 作为 Sensor Tower 的历史别名；不把同一份历史数据重复计入。
- 未知值用 null 和原因，估算与事实分开。没有验证方法不提供伪精确“成功率”。细节见 [研究口径](references/research-method.md)。

报告先给决定摘要、重要风险和下一笔验证，再给比较、情景和底稿。核心字段使用 [输入示例](examples/merge-research.json) 的格式；这是格式案例，不是市场调查实绩。

```text
python scripts/intelligence.py validate examples/merge-research.json
python scripts/intelligence.py report examples/merge-research.json --out outputs/merge-report
```

工具从同一输入生成 HTML 和 Markdown，保存原 JSON；PDF 可用浏览器打印导出。数字内容由实际研究产生，渲染器不会补齐缺失数据。

## 检查点与失败分支

🔴 **CHECKPOINT · 立项判断**：如果结论会改变品类、平台、地区或预算范围，先把证据、缺口和建议交给负责人确认，再交给项目经理；研究报告本身不等于立项批准。

- 如果账号/API 无法访问 → 改用公开页面或用户导出，写明 `access_gap` 和覆盖下降。
- 如果来源共享上游或互相转载 → 记录血缘，禁止重复计权。
- 如果只有榜单、评分或广告素材 → 只能作为行为线索，不升级为收入、利润或 ROAS。
- 如果指标定义、业务日期或地区缺失 → 保留 `null` 与补数方法，不用常识填齐。
- 如果渲染失败 → 保留已验证的输入 JSON 和错误回执，先修格式再重跑，不手工伪造报告。

## 反例黑名单

不要把目录条目写成已连接的 API；不要把第三方估算写成财报事实；不要把 iOS 或榜单倍数冒充完整 Android；不要把 data.ai 历史别名与 Sensor Tower 重复计数；不要把市场建议直接写成制作任务或批准决定。

## 交给下一岗位

交付研究问题、证据/结论、建议、约束、待验证项与有效决定。研究建议保持 proposed，直到有负责人明确决定。游戏拆解与逆向分析师接目标与疑问；游戏制作项目经理接已确认方向、限制和实验需求。

执行者是否为人或 Agent 不改变证据标准。新研究资料默认保存在使用者自己的工作区，不自动推送到本公开仓库。
