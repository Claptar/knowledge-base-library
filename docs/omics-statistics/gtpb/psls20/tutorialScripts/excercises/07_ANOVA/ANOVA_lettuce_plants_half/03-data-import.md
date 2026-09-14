---
title: Data import
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data import

**Source:** [`tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
lettuce <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/freshweight_lettuce.txt")
```

Take a glimpse at the data

```r
glimpse(lettuce)
```

```r
## treatment to factor
lettuce <- lettuce %>%
  mutate(treatment = as.factor(treatment))
```

---

[← The lettuce dataset](02-the-lettuce-dataset.md) · [Up: contents](index.md) · [Data exploration →](04-data-exploration.md)
