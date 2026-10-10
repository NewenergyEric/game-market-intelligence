# Merge＋社区公开信号研究

[English](README.md) · [机器可读底稿](report.zh.json) · [英文看板](dashboard-en.png)

[![Merge＋社区公开信号看板](dashboard-zh.png)](dashboard-zh.png)

**研究问题：** 沿用 Merge／社区方向时，公开市场信号能否支持直接立项，还是只足以支持下一轮验证？

**结论：** Merge 在益智品类中的收入份额从 2024 年的 14% 增至 2025 年的 20%，但前十产品掌握约 80% 的品类收入。公开证据支持“市场真实且头部强势”，不支持直接 GO。建议先验证一个“剧情优先的社区入口”，并保持状态为 `proposed`。

## 证据表

| 信号 | 性质 | 观察值 | 解释 |
|---|---|---:|---|
| Merge 占益智品类 IAP 收入 | 第三方估算 | 20%（2025） | 全球 App Store＋Google Play IAP；不含网页商店和其他收入 |
| Merge 前十产品收入集中度 | 第三方估算 | 约 80%（2025） | 市场有规模，但进入窗口集中在少数强产品 |
| Gossip Harbor 年收入 | 第三方估算 | 5.5 亿美元（2025） | 约占 Merge 品类 33%；不是财报披露 |
| Gossip Harbor Google Play | 商店观察 | 5000 万+ 下载；4.3 分 | 商店量级与当前评价快照，不等于全渠道安装或留存 |
| Merge Mansion 生命周期 | 发行商一方披露 | 8 亿美元+；全球下载 6500 万+ | 生命周期口径；没有地区、渠道或年度拆分 |
| 我方 CPI／LTV／D1／D7／产能 | 未知 | — | 没有一方数据，不能用竞品估算代替 |

## 下一次验证

1. 做一个剧情优先、社区关系可见的窄原型。
2. 先测教程完成率、D1／D7、剧情解锁转化和体力卡点。
3. 同时补齐目标地区 CPI、可接受 LTV 和团队产能基线。
4. 指标和产能达到负责人预设门槛后，再把建议从 `proposed` 改为 `confirmed`。

## 复现

```text
python scripts/intelligence.py validate case-studies/merge-community-public-signals/report.json
python scripts/intelligence.py report case-studies/merge-community-public-signals/report.json --out outputs/merge-community-public-signals
```

## 来源与口径

- [InvestGame, *Mobile Market Landscape 2026*](https://investgame.net/wp-content/uploads/2026/02/2026-02-06-upload_Reports_EN_MobileMarkeLandscape2026.pdf)，第 39–42 页；报告说明估算基于 AppMagic。
- [Gossip Harbor · Google Play](https://play.google.com/store/apps/details?hl=en-US&id=com.mergegames.gossipharbor)、[Merge Mansion · Google Play](https://play.google.com/store/apps/details?hl=en-US&id=com.everywear.game5)、[Travel Town · Google Play](https://play.google.com/store/apps/details?hl=en-US&id=io.randomco.travel)，快照核对日期 2026-10-10；商店信号会变化。
- [Metacore 官方新闻](https://metacoregames.com/news/metacore-appoints-jose-saarniniemi-as-general-manager-of-merge-mansion)，2026-06-12；8 亿美元+和 6500 万+为发行商披露。

本案例只使用公开、可分享资料。看板中的估算、观察和未知有明确标签；没有声称接入付费 API，也没有发布商业项目原始数据。
