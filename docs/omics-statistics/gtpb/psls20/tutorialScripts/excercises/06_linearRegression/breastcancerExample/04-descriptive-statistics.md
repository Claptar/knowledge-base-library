---
title: Descriptive statistics
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Descriptive statistics

**Source:** [`tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

We first calculate the Pearson and Spearman correlation based on the original data and the log2 transformed data

Pearson  correlation
```r
brca %>%
  select(S100A8,ESR1) %>%
  mutate(S100A8Log2=S100A8%>%log2,ESR1Log2=ESR1%>%log2) %>%
  cor
```

Spearman correlation
```r
brca %>%
  select(S100A8,ESR1) %>%
  mutate(S100A8Log2=S100A8%>%log2,ESR1Log2=ESR1%>%log2) %>%
  cor(,method = "spearman")
```

Both the Pearson and Spearman correlation are negative. Note, that the Spearman correlation is much larger in absolute value than the Pearson correlation on the original expression measurements. Indeed, the Pearson correlation is affected by the non linear association at the original scale.

On the log scale the Pearson correlation is much higher.
The spearman correlation, however, remains because it is based on rank transformed data.

---

[← Data exploration](03-data-exploration.md) · [Up: contents](index.md) · [Model →](05-model.md)
