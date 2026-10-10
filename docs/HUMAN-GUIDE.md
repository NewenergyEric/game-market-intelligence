# 人类使用说明 · 游戏市场研究总监

## 这份岗位解决什么问题

把“这个 Merge／社区游戏值不值得做、先做什么、对标谁、风险在哪里”转成有来源、有日期、有口径的研究结论。它是研究与决策支持岗位，不是自动购买数据，也不是替负责人拍板。

## 30 秒开始

1. 给 Agent 项目简述、平台、地区、目标玩家和要支持的决定。
2. 要求它先读 `SKILL.md`，再运行：

   ```text
   python scripts/intelligence.py sources --topic market --region china --platform mobile
   python scripts/intelligence.py validate examples/merge-research.json
   python scripts/intelligence.py report examples/merge-research.json --out outputs/merge-report
   ```

3. 先看决定摘要、风险和下一笔验证，再看比较表与底稿。
4. 只有负责人确认的结论才能进入项目经理的执行基线。

## 你需要提供

平台与地区、研究对象、时间窗、竞品范围、预算或资源限制，以及“研究结果要支持哪个决定”。没有付费数据权限时，允许使用公开来源和用户导出，但报告必须标出缺口。

## 你会收到

研究范围、来源目录、指标口径、带证据的观察、估算与事实分离的结论、风险、待验证项和给拆解/项目经理的交接问题。未知值保留为 `null`，不会为了填表虚构流水或成功率。

## 关键边界

- Sensor Tower、AppMagic、七麦、点点等单款数据按第三方估算处理；财报只按披露的公司或分部口径使用。
- SteamDB、Metacritic、广告素材量和评论不能直接当销量、利润或 ROAS。
- 目录中的 75 个入口是可研究来源，不代表账号、API 或自动采集已经接通。
- 不把竞品研究结论直接写成我方已批准玩法；需要负责人确认后再交给项目经理。

## 推荐的人类复核

核对业务日期、地区、平台、币种、样本覆盖、来源独立性与估算方法。任何影响立项的数字至少保留一个一手披露或明确的第三方方法说明。
