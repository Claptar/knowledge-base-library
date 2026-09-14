---
title: Data exploration
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data exploration

**Source:** [`tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

There are many variables in the data, we will plot all variables in a scatterplot matrix using the GGally package.

```r
#install.packages("GGally")
library(GGally)
brca[,-(1:4)] %>% ggpairs()
```

We now focus on the association between S100A8 expression and the ESR1 expression.

```r
brca %>%
  ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_smooth(se=FALSE,col="grey") +
  geom_smooth(method="lm",se=FALSE)
```

The association of S100A and ESR1 does not appear to be linear.

- Concentration measurements are often skewed.
- We will log2 transform the data.

```r
brca %>%
  ggplot(aes(x=ESR1 %>% log2,y=S100A8 %>% log2)) +
  geom_point() +
  geom_smooth(se=FALSE,col="grey") +
  geom_smooth(method="lm",se=FALSE)
```

Upon log transformation the data are showing a linear association. Is this association strong enough to be able to conclude that the S100A8 gene expression is associated to the ESR1 gene expression?

---

[← Research question](02-research-question.md) · [Up: contents](index.md) · [Descriptive statistics →](04-descriptive-statistics.md)
