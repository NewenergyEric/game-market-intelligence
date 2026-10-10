# 国内外游戏研究来源目录

共 75 个研究入口/资料路径；包含品牌、官方披露门户、渠道及自有资料，并非 75 个独立数据集或已接通连接器。

按研究问题选源；列表可用 CLI 按地区、平台和 topic 检索。`entry_checked` = 核读过官方入口；`limited` = 登录/JS/读取受限；`candidate` = 保留候选待核；`file_import` = 用户资料。商业账户与接口均需另做实际接入验证。

机器清单：[sources.json](../data/sources.json)。口径说明：[research-method.md](research-method.md)。所有链接指向对应官方或原发布入口；具体报告应再引用条目原文。

## 单款与竞争情报

| 来源 | 用途 | 已核实层级 | 关键限制 |
|---|---|---|---|
| [Sensor Tower（含 data.ai 历史入口）](https://sensortower.com/) | revenue, engagement, ads, market | limited | 第三方单款指标为估算；商店、广告收入与渠道覆盖按字段核对 |
| [AppMagic](https://appmagic.rocks/) | revenue, market, product | limited | 保留 IAP、广告、分成与地域口径；与同集团来源独立性另核 |
| [七麦数据](https://www.qimai.cn/) | revenue, engagement, product | limited | 中国 iOS 与 Android 渠道覆盖分开；本次主页读取受限，账号/字段待核 |
| [点点数据](https://www.diandian.com/) | revenue, engagement, market | limited | 官网解决方案可核读；本次主站超时，估算及 API 具体字段需账号验证 |
| [DataEye](https://www.dataeye.com/api.html) | ads, market, product | entry_checked | 官方营销 API 候选；素材/买量信号不直接等于实际流水 |
| [蝉大师](https://www.chandashi.com/) | engagement, ads, product | limited | 当前主页需 JavaScript；具体游戏/应用数据产品和权限仍待验证 |
| [GameRefinery](https://www.gamerefinery.com/) | product, market, revenue | entry_checked | 功能/LiveOps 与表现研究；不同套餐和 API 权限分开核对 |
| [Similarweb App Intelligence](https://www.similarweb.com/corp/apps/) | engagement, revenue, market | entry_checked | 模型/面板与具体样本覆盖需记录；非发行商实际财务 |

## PC与主机

| 来源 | 用途 | 已核实层级 | 关键限制 |
|---|---|---|---|
| [Steam 官方 Web API](https://partner.steamgames.com/doc/webapi_overview) | product, engagement, own-data | entry_checked | 公开信息与发行商授权数据分开，不提供他人真实营收 |
| [SteamDB](https://steamdb.info/faq/) | engagement, product | entry_checked | 活跃/价格/历史参照，不是销量流水工具；不自动抓取 |
| [SteamSpy](https://steamspy.com/about) | engagement, market | entry_checked | 拥有者抽样估算不是净销量，误差与区间不能抹掉 |
| [VG Insights / VGI](https://app.sensortower.com/vgi/) | revenue, market, product | entry_checked | 第三方销量/收入估算；与 Sensor Tower 数据链关系需核实 |
| [Gamalytic](https://gamalytic.com/) | revenue, market | entry_checked | 保留第三方估算标签；具体 API 与权限未验证 |
| [GameDiscoverCo](https://gamediscover.co/docs/mcp/getting-started) | revenue, market, product | entry_checked | Pro/已开通 MCP 才可接；数据估算与发行商披露区分 |
| [VGChartz](https://www.vgchartz.com/) | revenue, market | candidate | 按单条注明官方披露/估算及 sell-in/sell-through；方法页本次读取未完成 |
| [Metacritic](https://www.metacritic.com/about-us/) | sentiment, product | entry_checked | 评价与口碑来源，不提供可靠的单款流水结论 |
| [Circana Video Games](https://www.circana.com/industries/video-games) | market, revenue, engagement | entry_checked | 报告/商业数据的地区、零售与数字参与范围需要原文口径 |
| [Famitsu / Fami通](https://www.famitsu.com/ranking/game-sales/) | market, revenue | candidate | 榜单范围和实体/数字覆盖逐期核实；入口候选尚未实测 |

## 行业大盘

| 来源 | 用途 | 已核实层级 | 关键限制 |
|---|---|---|---|
| [中国音数协游戏工委](https://new.cgigc.com.cn/report.html) | market | entry_checked | 读取原版报告并记录统计范围；联合发布内容不重复当作多源 |
| [伽马数据（CNG）报告](https://new.cgigc.com.cn/report.html) | market | limited | 暂用工委正式报告入口追溯联合报告；CNG 独立官网/API 未核实，按具体署名确认 |
| [艾瑞咨询](https://www.iresearch.com.cn/report.shtml?classId=90) | market, engagement | entry_checked | 报告年份与手游/小游戏范围单列；预测与统计不混用 |
| [易观 / 易观千帆](https://app.analysys.cn/) | engagement, market | entry_checked | 面板活跃/用户数据不是收入；试用数据时间可能不同 |
| [QuestMobile](https://www.questmobile.com.cn/) | engagement, market | entry_checked | 面板样本/终端/应用覆盖按报告记录 |
| [Newzoo](https://newzoo.com/) | market, engagement, revenue | entry_checked | 宏观、品类、平台数据不自动适用于我方细分；商业权限待核 |
| [Niko Partners](https://nikopartners.com/) | market, engagement | entry_checked | 地区调查/市场模型按原方法使用 |
| [Statista](https://www.statista.com/topics/868/video-games/) | market | entry_checked | 聚合页回溯原来源，Market Insights 预测和已发生数据分开 |
| [ESA](https://www.theesa.com/) | market, engagement | entry_checked | 美国行业与玩家研究；原调查样本及时间窗需记录 |
| [Video Games Europe / GSD](https://www.videogameseurope.eu/) | market, revenue | entry_checked | 欧洲报告与 GSD 样本参与范围分开；目录入口不是全市场覆盖保证 |
| [Ukie](https://ukie.org.uk/) | market | entry_checked | 英国行业报告与榜单；转载数据追踪原发布方 |
| [KOCCA 韩国内容振兴院](https://www.kocca.kr/) | market | candidate | 白皮书/调查入口候选，具体游戏报告与翻译待核 |
| [CESA 日本游戏产业协会](https://www.cesa.or.jp/) | market | candidate | 白皮书/行业研究入口候选，具体年度与许可待核 |
| [IGEA](https://igea.net/) | market, engagement | candidate | 澳新市场与玩家报告入口候选，按具体报告样本核对 |

## 财报与一手披露

| 来源 | 用途 | 已核实层级 | 关键限制 |
|---|---|---|---|
| [巨潮资讯](https://www.cninfo.com.cn/) | financials | entry_checked | 公司/分部、会计期间和审计状态按原文，不自行拆分单款 |
| [港交所披露易](https://www.hkexnews.hk/) | financials | entry_checked | 原公司公告及年报；币种、分部和期间统一后比较 |
| [SEC EDGAR](https://www.sec.gov/search-filings) | financials | entry_checked | 法定披露/API；公司事实不能当作未披露产品数据 |
| [腾讯 IR](https://www.tencent.com/investors/) | financials | entry_checked | 业务分部与游戏数据只按公司实际披露使用 |
| [网易 IR](https://ir.netease.com/) | financials | entry_checked | 保留游戏与相关增值服务的实际口径 |
| [三七互娱公告（002555）](https://www.cninfo.com.cn/) | financials | entry_checked | 在巨潮按公司/代码检索正式报告，不视为独立于巨潮的第二来源 |
| [完美世界公告（002624）](https://www.cninfo.com.cn/) | financials | entry_checked | 同公司不同业务按分部披露，不由集团收入反推单游戏 |
| [吉比特公告（603444）](https://www.cninfo.com.cn/) | financials | entry_checked | 公告中的运营、财务与估算分开登记 |
| [Nintendo IR](https://www.nintendo.co.jp/ir/en/) | financials, revenue | entry_checked | 硬件/软件、出货/销售、财年口径分别记录 |
| [Sony IR](https://www.sony.com/en/SonyInfo/IR/) | financials, revenue | entry_checked | 游戏分部收入不直接对应单游戏销量 |
| [Microsoft IR](https://www.microsoft.com/en-us/Investor/) | financials | candidate | Gaming/Xbox 内容服务按实际披露；入口候选待具体报告核读 |

## 买量创意与需求

| 来源 | 用途 | 已核实层级 | 关键限制 |
|---|---|---|---|
| [Meta Ad Library](https://www.facebook.com/ads/library/) | ads | candidate | 公开库与 API 覆盖不同，当前 API 权限未验证 |
| [TikTok Creative Center](https://ads.tiktok.com/business/creativecenter/) | ads, product | entry_checked | 登录/地区限制与相对互动信号需记录，不能推断真实 ROAS |
| [Google Ads Transparency Center](https://adstransparency.google.com/) | ads | entry_checked | 广告透明信息，不是完整花费或转化数据库 |
| [SocialPeta](https://socialpeta.com/en) | ads, market | entry_checked | 商业广告情报；素材数量和投放观察不等于收入 |
| [AppGrowing](https://appgrowing.cn/) | ads, market | entry_checked | 国内/海外产品覆盖分别核对；账号与导出待验证 |
| [巨量引擎](https://www.oceanengine.com/) | ads, own-data | entry_checked | 官方报告/创意与我方广告后台区分，不含他人后台财务 |
| [腾讯广告](https://e.qq.com/) | ads, own-data | candidate | 我方账号实际数据可导出，公开行业材料另登记；入口候选 |
| [Google Trends](https://trends.google.com/) | engagement, market | entry_checked | 相对搜索热度不是用户数/营收；API 访问资格另核 |
| [百度指数](https://index.baidu.com/) | engagement, market | limited | 关键词/采样与相对指数口径；页面依赖登录/JavaScript |

## 玩家与产品观察

| 来源 | 用途 | 已核实层级 | 关键限制 |
|---|---|---|---|
| [Steam 官方评论 API](https://partner.steamgames.com/doc/store/getreviews) | sentiment | entry_checked | 评论样本、语言、购买类型和时间窗可造成偏差 |
| [Apple App Store](https://apps.apple.com/) | product, sentiment | candidate | 地区页面、版本、评分不等于完整用户群；不含后台营收 |
| [Google Play](https://play.google.com/store/games) | product, sentiment | candidate | Google Play 覆盖不包含全部中国 Android 渠道 |
| [TapTap](https://www.taptap.cn/) | product, sentiment | candidate | 社区评分/预约与活跃样本不代表全市场 |
| [哔哩哔哩游戏内容](https://www.bilibili.com/) | sentiment, product | candidate | 录屏/评论的版本、样本与转载链需要定位 |
| [YouTube Data API](https://developers.google.com/youtube/v3) | sentiment, product | entry_checked | 配额与具体端点需验证；公开视频样本不是整体玩家意见 |
| [Reddit 开发者入口](https://developers.reddit.com/) | sentiment | candidate | 当前数据 API/商业访问范围待核；公开评论按样本解释 |
| [Discord 开发者入口](https://discord.com/developers/docs/intro) | sentiment, own-data | candidate | 仅有访问范围的频道/导出，私人社区不属于默认公开语料 |

## 自有运营与渠道

| 来源 | 用途 | 已核实层级 | 关键限制 |
|---|---|---|---|
| [GameAnalytics](https://docs.gameanalytics.com/) | own-data, engagement | entry_checked | 我方事件、漏斗、留存；benchmark 与自己实际数据分开 |
| [AppsFlyer](https://support.appsflyer.com/) | own-data, ads | candidate | 归因窗/隐私模型和我方账号范围，非竞品真实财务 |
| [Adjust](https://help.adjust.com/) | own-data, ads | candidate | 我方授权归因/报表路径，具体访问与字段待核 |
| [Firebase Analytics](https://firebase.google.com/docs/analytics) | own-data, engagement | candidate | 自有事件与用户定义，未埋点的数据不能补造 |
| [App Store Connect](https://developer.apple.com/app-store-connect/) | own-data, revenue | entry_checked | 仅账号有权管理的 App 数据，不是竞品流水入口 |
| [Google Play Developer API](https://developers.google.com/android-publisher) | own-data, revenue | entry_checked | 我方账号资源，具体经营指标按 Console/API 实際范围核对 |
| [微信小游戏开发者平台](https://developers.weixin.qq.com/minigame/dev/guide/) | own-data, product | limited | 我方后台/公开说明，当前文档读取受限 |
| [抖音开放平台](https://developer.open-douyin.com/) | own-data, product | entry_checked | 小游戏与小程序的具体后台及字段分别核对 |
| [华为开发者联盟](https://developer.huawei.com/consumer/cn/) | own-data, product | entry_checked | 可访问自己的分发/经营数据；不能代表竞品所有渠道 |
| [OPPO 开放平台](https://open.oppomobile.com/) | own-data, product | limited | 入口可访问，账号内报表和字段尚未验证 |
| [vivo 开放平台](https://dev.vivo.com.cn/) | own-data, product | limited | 入口可访问，账号内报表和字段尚未验证 |
| [小米开放平台](https://open.mi.com/) | own-data, product | candidate | 入口本次读取未完成，具体后台和权限待核 |
| [应用宝开放平台](https://open.qq.com/) | own-data, product | candidate | 使用自有发行商授权资料；入口及具体报表待验证 |
| 团队自有项目资料 | own-data, product, financials | file_import | 用户提供的真实成本、任务、试玩、代码和经营导出；分享范围随材料 |

## 监管与发行环境

| 来源 | 用途 | 已核实层级 | 关键限制 |
|---|---|---|---|
| [国家新闻出版署游戏审批结果](https://www.nppa.gov.cn/bsfw/jggs/yxspjg/) | regulation, product | entry_checked | 审批条目不代表市场表现、许可解释或上市时间 |

## 接入顺序

Merge／社区研究优先：现有策划/试玩 → GameRefinery 的功能与 LiveOps → Sensor Tower/AppMagic/点点/七麦中已有权限的数据 → DataEye/广告库的创意线索 → 财报与行业报告交叉核对。平台未确定时不预设只有手游。

先支持网页与用户导出；API/MCP 在字段、权限、额度和样例核验后逐一接通。主机/PC、大盘、评论、渠道后台按问题启用。未取得的数据保持 unknown，不自动补零。
