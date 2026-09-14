---
title: Prostacyclin Example
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Prostacyclin Example

**Source:** [`tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Researchers study the effect of arachidonic acid on prostacyclin level in blood plasma. They use 3 different concentrations of arachidonic acid:

- low,
- medium and
- high dose

Each treatment is adopted to 12 rats. They measure the prostacyclin levels in blood plasma using an ELOSA fluorescence measurement.


```r
prostacyclin <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/prostacyclin.txt")
```

```r
head(prostacyclin)
```

```r
prostacyclin <- prostacyclin %>%
  mutate(dose = as.factor(dose))
```


##Data exploration

We assess if distribution of the prostacyclin concentration for each of the arachidonic acid treatments using a boxplot. We also assess if the data are normally distributed in each treatment group using QQ-plots.

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


The data in the three groups are approximately Normally distributed with equal variance:
$$Y_i \vert \text{group j} \sim N(\mu_j,\sigma^2),$$
with $j= \text{1, 2, 3}$

## Research question

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

We can assess this omnibus hypothesis using ANalysis of VAriance (ANOVA).

---

[Up: contents](index.md) · [Analyse of Variance →](02-analyse-of-variance.md)
