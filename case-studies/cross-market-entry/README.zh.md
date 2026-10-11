# 把一个方向拆成六个会改变决定的视角

[English](README.en.md)

**制作人的问题：** “社区体验还能怎样做？手游 Merge、授权 IP 社交和 PC 买断，应该用什么标准比较？先测英语、日语还是简中？”

这是一次实际完成的公开来源研究，2026-10-11 检索。商店抓取缓存与发布时点保留；没有购买地区流水数据，也没有运行用户测试。

| 产品 | 类型 / 玩家循环 | IP / 权利信息 | 地区 / 渠道口径 | 语言 / 本地化 | 付费方式 | 内容 / 供给压力 |
|---|---|---|---|---|---|---|
| Gossip Harbor | Merge＋剧情＋餐厅修复 | 权属与外部 IP 授权关系未在本轮核定 | Google Play 英文页；不据此推断美国收入 | 商店展示英文；游戏支持语言表待实机或官方资料核对 | 含广告与内购；比例未知 | 公开更新说明出现每周新章节；当前产能与成本未知 |
| MONOPOLY GO! | 社交掷骰＋建造＋贴纸收集 | 官方确认 Scopely 与 Hasbro 合作 | 官方宣布全球 iOS/Android 发布；国家表现未披露 | 本轮没有核定完整的游戏内语言支持表 | 免费下载＋内购；付费漏斗未知 | 官方列出活动与贴纸等持续内容；不能据此推算团队人数 |
| Stardew Valley | 乡村生活 RPG / 模拟；经营与关系 | 商店列开发商与发行商 ConcernedApe；不等于我方授权 | 本轮 Steam 意大利区英文页面；不是全球统一定价 | 12 种界面语言，含英/日/简中；非完整语音支持 | 买断本体 €13.99；意区页面快照，音轨另售 | 内容与合作玩法由官方列明；我方内容成本需另算 |

## 三个交叉判断

1. **类型 × 付费：** 手游内购/广告和 PC 买断分别建经济模型。不能拿下载量、评价数量或商品价格直接比利润。
2. **IP × 地区 × 产能：** Hasbro 合作是事实；我方拿得到什么条款、要多少审批和活动内容仍未知。立项比较必须先补商务与供给约束。
3. **语言 × 地区：** Stardew 的 12 种界面语言是供给证据，不是 12 个成功市场。英语/日语/简中测试需独立标国家、渠道和玩家队列。

## 接下来如何验证

| 假设 | 实际动作 | 交给谁 | 决策所需证据 |
|---|---|---|---|
| 社区叙事能支持持续留存 | 用已有方向做窄原型，记录内容制作时间与玩家卡点 | 主策、研究员、主美 | 分语言的理解度、留存与内容吞吐；阈值由负责人事先确定 |
| 授权 IP 能改善获客 | 先取得合法商务范围，再设计与原创题材相同口径的素材实验 | 商务、投放、制作人 | 授权报价/限制、同渠道测试及增量成本 |
| 本地化投入可承担 | 对同一任务做英/日/简中测试，国家与语言分开招募 | 本地化、UX、发行 | 文本膨胀、字体、客服与地区漏斗；不能拿评论语言代替 |

## 来源与可复核文件

- [Gossip Harbor · Google Play](https://play.google.com/store/apps/details/Gossip_Harbor_Merge_Story?hl=en_US&id=com.mergegames.gossipharbor)
- [MONOPOLY GO! · Scopely / Hasbro launch](https://www.scopely.com/en/news/its-time-to-take-that-chance-monopoly-go-is-here)
- [MONOPOLY GO! · Google Play](https://play.google.com/store/apps/details?gl=US&hl=en_US&id=com.scopely.monopolygo)
- [Stardew Valley · Steam Italy / English](https://store.steampowered.com/app/413150/Stardew_Valley/?cc=it&l=english)

[report.json](report.json) · [comparison.csv](comparison.csv)

```sh
python scripts/intelligence.py validate case-studies/cross-market-entry/report.json
python scripts/intelligence.py report case-studies/cross-market-entry/report.json --out outputs/cross-market-entry
```

输出报告、矩阵和底稿；建议保持 proposed。旧的 [Merge 收入下钻](../merge-community-public-signals/README.md)仍可结合使用。
