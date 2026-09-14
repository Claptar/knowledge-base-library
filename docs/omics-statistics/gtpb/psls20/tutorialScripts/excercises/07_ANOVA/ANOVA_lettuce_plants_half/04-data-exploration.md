---
title: Data exploration
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data exploration

**Source:** [`tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
## Count the number of observations per treatment
lettuce %>%
  count(treatment)
```

Make a plots to explore the data
```r
#...
```

Interpret the boxplots!

1. How will you model the data.
2. Translate the research question into parameters of the model.
3. Check the assumptions.
4. If the assumptions are fulfilled you can fit model
5. Further assess differences between the treatments in a posthoc analysis if applicable.

---

[← Data import](03-data-import.md) · [Up: contents](index.md)
