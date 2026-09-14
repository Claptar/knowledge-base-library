---
title: Data tidying
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Non_parametric_shrimps.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Non_parametric_shrimps.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data tidying

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Non_parametric_shrimps.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Non_parametric_shrimps.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
shrimps <- shrimps %>%
  mutate(group = as.factor(group))
```

---

[← Initial exploration of the data](03-initial-exploration-of-the-data.md) · [Up: contents](index.md) · [Goal →](05-goal.md)
