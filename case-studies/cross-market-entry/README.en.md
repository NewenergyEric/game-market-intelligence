# Six lenses that change a product decision

[中文](README.zh.md)

**Producer question:** “What are our community-game options? How do we compare Merge mobile, licensed-IP social and premium PC? Which region/language test should come first?”

Public-source research performed on 2026-10-11. Cached storefront and original announcement scopes are retained. No country-revenue dataset or user experiment was purchased/run.

| 产品 | Genre / loop | IP / rights evidence | Region / channel scope | Language / localization | Monetization | Content / supply implications |
|---|---|---|---|---|---|---|
| Gossip Harbor | Merge, story and restaurant restoration | Rights and external IP terms not established | English Google Play listing; not US revenue | English listing; in-game language support unverified | Ads and IAP listed; revenue mix unknown | Captured update notes mention weekly chapters; capacity and cost unknown |
| MONOPOLY GO! | Social dice, building and sticker collection | Scopely and Hasbro collaboration disclosed | Worldwide iOS/Android launch; country performance absent | Full in-game language coverage unverified | Free download and IAP; payer funnel unknown | Events and stickers imply recurring content; no staffing estimate |
| Stardew Valley | Country-life RPG / simulation; farming and relationships | ConcernedApe listed as developer/publisher; no license granted to us | Steam Italy storefront in English; not a worldwide price | 12 interface languages incl. English/Japanese/Simplified Chinese; not full voice | €13.99 paid base game in Italy snapshot; soundtrack sold separately | Content and co-op listed; our production cost needs its own estimate |

## Three cross-lens decisions

1. **Genre × monetization:** model mobile IAP/ads and premium PC separately. Downloads, review counts and sticker prices cannot rank profitability.
2. **IP × region × capacity:** the Hasbro partnership is disclosed; our terms, approval workload and recurring-content capacity are unknown.
3. **Language × region:** twelve interface languages show localization supply, not success in twelve markets. English/Japanese/Simplified Chinese tests must tag country, channel and player cohort independently.

## What to test next

| Hypothesis | Action | Receiving role | Decision evidence |
|---|---|---|---|
| Community narrative sustains engagement | Test the existing narrow direction and record content hours and player friction | Design / research / art | Language-specific comprehension, retention and content throughput; owner sets thresholds in advance |
| Licensed IP improves acquisition | Establish lawful terms, then compare creatives with the same channel/cohort | BD / UA / producer | Quotes, restrictions, incremental cost and controlled results |
| Localization is affordable | Test the same task in EN/JA/zh-Hans, recruit country and language separately | Localization / UX / publishing | Text expansion, fonts, support and local funnel; not review-language proxies |

## Sources and reproducible files

- [Gossip Harbor · Google Play](https://play.google.com/store/apps/details/Gossip_Harbor_Merge_Story?hl=en_US&id=com.mergegames.gossipharbor)
- [MONOPOLY GO! · Scopely / Hasbro launch](https://www.scopely.com/en/news/its-time-to-take-that-chance-monopoly-go-is-here)
- [MONOPOLY GO! · Google Play](https://play.google.com/store/apps/details?gl=US&hl=en_US&id=com.scopely.monopolygo)
- [Stardew Valley · Steam Italy / English](https://store.steampowered.com/app/413150/Stardew_Valley/?cc=it&l=english)

[report.json](report.json) · [comparison.csv](comparison.csv)

```sh
python scripts/intelligence.py validate case-studies/cross-market-entry/report.json
python scripts/intelligence.py report case-studies/cross-market-entry/report.json --out outputs/cross-market-entry
```

Produces the report, comparison matrix and source record. The recommendation remains proposed. Keep the [Merge revenue drill-down](../merge-community-public-signals/README.md) for a narrower question.
