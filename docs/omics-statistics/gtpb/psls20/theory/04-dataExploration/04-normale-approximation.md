---
title: Normale approximation
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd
source_file: sources/gtpb-psls20/theory/04-dataExploration.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Normale approximation

**Source:** [`theory/04-dataExploration.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Biological and chemical data are often Normally distributed upon transformation.

- If this is the case we can get a lot of insight in the data using just two descriptive statistics: mean $\mu$ and standard deviation $\sigma$.

---

## Evaluation with QQ-plots

If your analysis build upon the assumption that the data are Normally distributed, it has to be verified.

We use *QQ-plots* or *quantile-quantile plots*.

- Observed quantiles from the observations in the sample are plotted against quantiles from the Normal distribution.

- If the data are Normally distributed both quantiles have to be in line.

- Dots in the plot are expected on a straight line.

- Systematic deviations of the straight line indicate that the data are not Normally distributed.

- Note, that we will always observe some random deviations from the straight line in the plot because of random biological variability, which is not indicative for deviations from Normality.

- So it is important to train yourself to learn to distinguish systematic from random deviations.

---

### Normal data
- We will first simulate data from the Normal distribution to show how the plots look like for data that is meeting the assumptions.

- We will simulate data from 9 samples with a mean of 18 and standard deviation of 9.

```r
n <- 20
mu <- 18
sigma <- 9
nSamp <-9

normSim <- matrix(rnorm(n*nSamp,mean=mu,sd=sigma),nrow=n) %>% as.data.frame

normSim %>% gather(samp,data) %>%
ggplot(aes(x=data)) +
geom_histogram(aes(y=..density.., fill=..count..),bins=30) +
geom_density(aes(y=..density..)) +
  facet_wrap(~samp)

normSim %>% gather(samp,data) %>%
  ggplot(aes(sample=data)) +
  geom_qq() +
  geom_qq_line() +
facet_wrap(~samp)
```

So even for Normal data we observe some deviations due to sampling variability!

---

### Real data

```r
NHANES %>% filter(Gender=="female"&!is.na(BMI)) %>%
  ggplot(aes(x=BMI))+
   geom_histogram(aes(y=..density.., fill=..count..)) +
   xlab("BMI") +
   ggtitle("All females in study") +
  geom_density(aes(y=..density..))

NHANES %>% filter(Gender=="female"&!is.na(BMI)) %>%
  ggplot(aes(sample=BMI)) +
  geom_qq() +
  geom_qq_line()
```

The QQ-plot shows that the quantiles of the data

- are larger (above the line) than these from the Normal in the left tail: compression of the lower tail,
- are larger (above the line) than these from the Normal in the right tail: long tail to the right.

We can clearly see that the data are skewed.

---

---

[← Univariate exploration of quantitative variables](03-univariate-exploration-of-quantitative-variables.md) · [Up: contents](index.md) · [Two continuous variables: Correlation →](05-two-continuous-variables-correlation.md)
