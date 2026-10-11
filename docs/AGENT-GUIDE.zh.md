# Agent 使用说明 · game-market-intelligence

[English](AGENT-GUIDE.en.md)

## 入口与读取顺序

先读 `SKILL.md`，再按问题读取 `references/research-method.md`、`references/source-catalog.md` 和 `data/sources.json`。只有需要渲染报告时才调用 `scripts/intelligence.py`。

## 标准工作流

1. 从请求提取平台、地区、对象、时间窗、指标、决策和证据预算。
2. 用 `sources` 路由来源，并记录每个来源的访问状态、独立性和限制。
3. 将事实、估算、推断、建议和未知分开写入输入 JSON。
4. 用 `validate` 检查必需字段，再用 `report` 生成 HTML、Markdown 和原 JSON。
5. 输出决定摘要、证据链、风险、下一步验证与交接问题。

## 失败分支

- 如果账号/API 无法访问 → 使用公开页面或用户导出，并将 `access_gap` 写入报告；不要声称自动采集成功。
- 如果多个来源重复上游数据 → 标记数据血缘，禁止重复计权。
- 如果只有估算没有方法 → 保留估算标签和限制，不升级为确认事实。
- 如果关键字段缺失 → 输出 `null`、缺口和补数方法，不用常识补齐。
- 如果结论会改变立项范围 → 停在负责人确认点，交给项目经理，不自动改需求。

## 输出契约

最少包含 `decision_summary`、`evidence`、`risks`、`next_validation` 和 `handoff_questions`。引用必须带来源、业务日期、采集时间、地区/平台、指标定义和覆盖缺口。

## 不要做

不要把来源目录当作已连接 API；不要把 Metacritic 评分当收入；不要把 SteamDB 活跃曲线当销量；不要把公司财报摊成单款流水；不要把市场建议直接当制作任务。

## 深度案例入口

[Protocol](../references/market-lenses.md) · [Case](../case-studies/cross-market-entry/README.md)

```sh
python scripts/intelligence.py validate case-studies/cross-market-entry/report.json
python scripts/intelligence.py report case-studies/cross-market-entry/report.json --out outputs/cross-market
```

## 工具输入格式

上面的输出契约描述面向人的报告内容，不是 intelligence.py 接收的 JSON schema。CLI 输入字段为 id、title、question、scope、claims、recommendation、unknowns，可选 comparison。每个比较单元以 claim_ids 指向 claims；以 case-studies/cross-market-entry/report.json 为可运行范本，不把 decision_summary 等报告栏目直接当作 CLI 字段。
