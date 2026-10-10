# 研究口径与来源使用

按要支持的决定组织材料，不固定要求先查完全部平台。

| 问题 | 优先入口 | 必须保留的边界 |
|---|---|---|
| 单款手游表现 | Sensor Tower、AppMagic、七麦、点点 | 估算、商店/地区/日期、IAP/广告、税费/分成、渠道覆盖 |
| 买量策略 | DataEye、SocialPeta、AppGrowing、平台广告库 | 观察到的创意/投放信号不等于实际花费和盈利 |
| PC/主机 | Steam 官方、VGI、Gamalytic、SteamSpy、GDC、Circana、平台 IR | owner、CCU、销量、出货、净收入分别定义 |
| 国内大盘 | 游戏工委、伽马报告、艾瑞、易观、QuestMobile | 样本、联合发布方、是否模型推算、是否包含小游戏 |
| 海外大盘 | Newzoo、Niko、Statista、地区行业协会 | 区域、用户定义、预测与实绩分开 |
| 经营一手披露 | 巨潮、披露易、SEC EDGAR、公司 IR | 原文披露层级、会计期间、审计状态；不拆分未披露单款 |
| 玩家动机与问题 | 评论、录屏、社区、实际试玩 | 样本偏差、观察版本、定性发现不可伪装成总体比例 |
| 我方留存/成本/渠道 | 自有后台与运营导出 | 账号范围、事件定义、完整性、归因窗与实际预算 |

## 比较与三情景

选择有解释力的成功、中位及低表现样本。对齐时间/地区/商业模式后才比较；无法对齐时保留并列差异，不计算假平均。

低/基准/高情景列出输入、公式与依据；研发、订阅、模型调用、运维、平台分成、获客及返工不重复计费。没有 CPI/LTV/留存证据时输出验证计划。经营建议与正式立项决定分开。

每个 Claim：`id / statement / kind / value / unit / period / scope / source_ids / evidence / unknown_reason`。`kind` 为 observed、estimate、assumption、inference；空值需要原因。`evidence` 是该结论的具体位置与方法，不能仅写一个供应商首页。

## 来源与接入状态

`entry_checked` 表示已核读官方入口；`limited` 表示 JS/登录/抓取限制；`candidate` 表示待进一步核实。三者都不表示数据账号已接通。

目录中的 API/MCP 只是有官方依据的候选接入方式；第一版工具仅实现目录检索、研究包校验和报告渲染。正式连接器逐个补认证、字段、额度、失败状态与真实样本。

data.ai 收购依据：[Sensor Tower 官方公告](https://sensortower.com/press/press-release-sensor-tower-acquires-market-intelligence-platform-data-ai)。AppMagic 归属更新见 [AppMagic 官方博客](https://appmagic.rocks/blog/)。企业归属相同不自动证明指标模型相同，也不能据两个品牌名称宣称证据独立。

没有普遍适用的“iOS 一定准确”或“未上市公司只能估算”规则；应依据具体记录、披露与覆盖判断。[Metacritic 指标定义](https://metacritichelp.zendesk.com/hc/en-us/articles/14478499933079-How-do-you-compute-METASCORES) 与 [SteamDB FAQ](https://steamdb.info/faq/) 是用途及访问方式的依据。
