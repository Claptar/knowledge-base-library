---
title: Introduction
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd
source_file: sources/gtpb-psls20/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(include = TRUE, comment = NA, echo = TRUE,
                      message = FALSE, warning = FALSE)
library(tidyverse)
library(Rmisc)
set.seed(140)
```


#Intro

Inference was only correct if distributional assumptions were satisfied

- e.g Normal distribution
- equal variance

-  The $p$-value: $\text{P}_0\left[ \vert T\vert \geq \vert t \vert \right]$.

	- Calculated using the null distribution of $T$ that we derived under the assumptions
	- In correct if assumptions are violated

-  $95\%$ CI also builds upon these assumptions. If they are invalid then the intervals will not contain the population parameter with 95% probability.

- Asymptotic theory is more difficult to place: the $t$-test is asymptotically non-parametric because for very large samples the distributional assumptions of normality are no longer important.

- If assumptions hold the parametric approach

	- more efficient: larger power with same sample size + smaller CI.
	- more flexible: easier to analyse data with complex designs

---

## Cholesterol voorbeeld

- Cholesterol concentration in blood measured for
  - 5 patients (group=1) two days upon a stroke
  - 5 healthy subject (groep=2).

- Is cholesterol concentration of hart patients and healthy subjects on average different?

```r
chol <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/chol.txt")
chol$group <- as.factor(chol$group)
nGroups <- table(chol$group)
n <- sum(nGroups)
chol
```

---


```r
chol %>%  ggplot(aes(x=group,y=cholest)) + geom_boxplot(outlier.shape=NA) + geom_point(position="jitter")

chol %>% ggplot(aes(sample=cholest)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~group)
```

- Possibly outliers
- Difficult to assess distributional assumptions when only 5 observations are available.

---

[Up: contents](index.md) · [Rank Tests →](02-rank-tests.md)
