---
title: Prostacyclin Example
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd
source_file: sources/gtpb-psls20/theory/07-Anova.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Prostacyclin Example

**Source:** [`theory/07-Anova.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Researchers study the effect of arachidonic acid on prostacyclin level in blood plasma. They use 3 different concentrations of arachidonic acid:

- low,
- medium and
- high dose

Each treatment is adopted to 12 rats. They measure the prostacyclin levels in blood plasma using an elisa fluorescence measurement.


```r
prostacyclin <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/prostacyclin.txt")
prostacyclin$dose <- as.factor(prostacyclin$dose)
head(prostacyclin)
```

---

##Data exploration

```r
prostacyclin %>%
  ggplot(aes(x=dose,y=prostac,fill=dose)) +
  geom_boxplot() +
  geom_point(position="jitter") +
  ylab("prostacyclin (ng/ml)")

prostacyclin %>%
  ggplot(aes(sample=prostac)) +
  geom_qq() +
  geom_qq_line() +
  facet_grid(~dose)
```


The data in the three groups is approximately Normally distributed with equal variance:
$$Y_i \vert \text{group j} \sim N(\mu_j,\sigma^2),$$
with $j= \text{1, 2, 3}$

## Research Question

Research question can translated in the following hypotheses

- $H_0$: the arachidonic acid concentration has no effect on the mean prostacyclin level in blood plasma in rats
$$
  H_0:\mu_1=\mu_2 = \mu_3
$$

- $H_1$: the arachidonic acid concentration has an effect on the mean prostacyclin level in blood plasma in rats, which implies that the at least two means are different.

In terms of the model parameters this becomes

$$
  H_0:\mu_1=\mu_2 = \mu_3
$$
and
$$H_1: \exists\ j,k \in \{1,\ldots,g\} : \mu_j\neq\mu_k$$


Alternative approach: split null hypothesis in partial hypotheses:
$$
  H_{0jk}: \mu_j=\mu_k \text{ versus } H_{1jk}: \mu_j \neq \mu_k
$$

Each hypothesis can be tested via two-sample t-tests $\rightarrow$ multiple testing problem + loss of power.

$\rightarrow$ assess $H_0:\mu_1=\mu_2=\mu_3$ with a *single test*.

---

[Up: contents](index.md) · [Analyse of Variance →](02-analyse-of-variance.md)
