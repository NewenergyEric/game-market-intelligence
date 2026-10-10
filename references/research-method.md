[中文](research-method.zh.md)

# Research method and source use

Organize evidence around the decision rather than exhausting every provider first.

| Question | Useful starting points | Preserve |
|---|---|---|
| Mobile title performance | Sensor Tower, AppMagic, Qimai, Diandian | Estimate status, store/region/date, IAP/ads, taxes/fees and channel coverage |
| Acquisition strategy | DataEye, SocialPeta, AppGrowing, platform ad libraries | Observed creatives/placements do not establish actual spend or profit |
| PC/console | Official Steam, VGI, Gamalytic, SteamSpy, GDC, Circana, platform IR | Owners, CCU, sales, shipments and net revenue are different metrics |
| China industry | Game industry committee, CNG, iResearch, Analysys, QuestMobile | Sample, co-publishers, modeled estimates and mini-game inclusion |
| International industry | Newzoo, Niko, Statista, regional associations | Region, player definition, forecast versus actual |
| Primary financials | CNINFO, HKEX, SEC EDGAR, company IR | Disclosed granularity, accounting period, audit status; do not invent title splits |
| Player motivation | Reviews, recordings, communities, actual play | Sampling bias and target version; qualitative findings are not population percentages |
| Our retention/cost/channel | Authorized internal dashboards/exports | Account scope, event definitions, completeness, attribution window and budget |

## Comparisons and scenarios

Use meaningful successful, middle and low-performing samples. Align period, geography and business model; otherwise show differences side by side without a false average.

Low/base/high scenarios retain inputs, formulas and evidence. Avoid double counting development, subscriptions, model calls, operations, platform fees, acquisition and rework. Missing CPI/LTV/retention leads to a validation plan. Business recommendations and formal greenlight decisions remain separate.

Claim fields: `id / statement / kind / value / unit / period / scope / source_ids / evidence / unknown_reason`. `kind` is `observed`, `estimate`, `assumption` or `inference`. Null values need a reason. Evidence identifies the actual location and method, not just a vendor homepage.

## Source access status

`entry_checked` means an official entry point was inspected. `limited` means a JavaScript/login/retrieval limitation. `candidate` needs verification. None means a data account is connected.

API/MCP entries are candidate access methods with supporting documentation. Current helpers implement catalog search, package validation and report rendering. Each real connector still needs authentication, fields, quotas, failure behavior and a real sample.

Historical ownership references: [Sensor Tower's data.ai acquisition announcement](https://sensortower.com/press/press-release-sensor-tower-acquires-market-intelligence-platform-data-ai) and [AppMagic's official blog](https://appmagic.rocks/blog/). Shared ownership does not prove identical models; different brand names do not prove independent evidence. Reverify ownership for a new research date.

Do not assume iOS estimates are universally accurate or that private companies can only have estimated data. Judge the specific disclosure and coverage. [Metacritic metric definition](https://metacritichelp.zendesk.com/hc/en-us/articles/14478499933079-How-do-you-compute-METASCORES) and [SteamDB FAQ](https://steamdb.info/faq/) explain their intended use.
