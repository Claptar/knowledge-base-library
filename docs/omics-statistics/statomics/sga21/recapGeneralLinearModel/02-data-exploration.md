---
title: Data Exploration
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd
source_file: sources/statomics-sga21/recapGeneralLinearModel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Exploration

**Source:** [`recapGeneralLinearModel.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Import

```r
library(tidyverse)
gene <- read.table("https://raw.githubusercontent.com/statOmics/SGA21/master/data/kpna2.txt",header=TRUE)
head(gene)
```

We will transform the variable grade and node to a factor

```r
gene$grade <- as.factor(gene$grade)
gene$node <- as.factor(gene$node)
```

## Summary statistics

```r
geneSum <- gene %>%
  group_by(grade) %>%
  summarize(mean = mean(gene),
            sd = sd(gene),
            n=length(gene)
            ) %>%
  mutate(se = sd/sqrt(n))
geneSum
```

## Visualisation

```r
gene %>%
  ggplot(aes(x=grade,y=gene)) +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter()
```

We can also save the plots as objects for later use!

```r
p1 <- gene %>%
  ggplot(aes(x=grade,y=gene)) +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter()

p2 <- gene %>%
  ggplot(aes(sample=gene)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~grade)

p1
p2
```


## Research questions

Researchers want to assess the association of the histological grade on KPNA2 gene expression


![](https://raw.githubusercontent.com/statOmics/SGA21/master/figures/statGenomicsGent201718-6.jpeg)

---

## Estimation of effect size and standard error

```r
effectSize <- tibble(
  delta = geneSum$mean[2]- geneSum$mean[1],
  seDelta = geneSum %>%
    pull(se) %>%
    .^2 %>%
    sum %>%
    sqrt
  )
effectSize
```

---

[← Breast cancer example](01-breast-cancer-example.md) · [Up: contents](index.md) · [Statistical Inference →](03-statistical-inference.md)
