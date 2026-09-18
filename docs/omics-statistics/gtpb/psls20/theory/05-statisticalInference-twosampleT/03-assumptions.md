---
title: Assumptions
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference-twosampleT.Rmd
source_file: sources/gtpb-psls20/theory/05-statisticalInference-twosampleT.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`theory/05-statisticalInference-twosampleT.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference-twosampleT.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Assumptions

Validity of t-test depends on distributional assumptions:

- Independence (design)
- One-sample t-test: normality of the observations
- Paired t-test: normality of the difference
- Two-sample t-test: Normality of the observations in both groups, and equal variances.

If the assumptions are not met, the null distribution does not follow a t-distribution, and, the p-values and critical values are incorrect.

To construct confidence intervals we also rely on these assumptions.

- We used quantiles from the t-distribution to calculate the lower and upper limit.

- The correct coverage of the CI depends on these assumptions

---

### Evaluate normality

 - Boxplots and histograms: shape of distribution and outliers

 - QQ-plots

There also exist hypothesis tests (goodness-of-fit test), but their null hypothesis is that the data are normally distributed so we make a weak conclusion!

  - Kolmogorov-Smirnov, Shapiro-Wilk en Anderson-Darling.
  - In small samples they have a low power
  - In large samples they often flag very small deviations as significant

Recommendation

- Start with graphical exploration of the data and keep the sample size in mind to avoid overinterpretation of the plots.

- If you have doubts, use simulation where you simulate data with the same sample size from a Normal distribution with the same mean and variance as the one that you observed in the sample

- If you observed deviations of normality check in the literature how sensitive your method is such deviations of normality. (e.g. T-tests for instance are rather insensitive to deviations as long as the distribution of the data is symmetric.)

- In large samples you can resort to the central limit theorem.

- You might resort to transformations of the response.

---

### Homoscedasticity

- Boxplots: The box size is the inter quartile range (IQR) a robust estimator of the variance.

- If the differences are not large $\rightarrow$ homoscedasticiteit

- Again you can use simulation to get insight in the differences you can expect.

- Formal F-test can be used to compare the variances, but again under the null you assume equal variances, so the same criticism as for normality tests applies here.

---

### Welch modified t-test

If the data are heteroscedastic, you can use a Welch two-sample T-test, which no longer uses the pooled variance estimator.

$$T =  \frac{\bar{Y}_1 - \bar{Y}_2}{\sqrt{\frac{S^2_1}{n_1}+\frac{S^2_2}{n_2}}}$$
with $S^2_1$ en $S^2_2$ the sample variances in both groups.

This statistic follows approximately a t-distribution with a number of degrees of freedom between  $\text{min}(n_1-1,n_2-1)$ and $n_1+n_2-2$.

In R the degrees of freedom are estimated using the Welch- Satterthwaite approximation. You can do this by using the `t.test` function with argument `var.equal=FALSE`.

```r
t.test(rel~trt,data=ap,var.equal=FALSE)
```

Note that you can see that the Welch T-test is adopted in the title. The adjusted degrees of freedom are $df = 17.876$ $\pm$ to that of the conventional T-test, because the variances are approximately equal.

---

## How to report?

- In the scientific literature there is too much attention for p-values

- It is much more informative to combine an estimate with its confidence interval.

**Rule of thumb**:

Report an estimate together with its  confidence interval (and its p-value)

1. The result of the test can be derived of the confidence interval
2. It allows the reader to judge **scientific relevance**.

```r
t.test(rel~trt,data=ap)
```

The result of an $\alpha$-level t-test is equivalent with comparing the effect size under $H_0$ with the $1-\alpha$ CI.

An effect can be extremely statistically significant, but scientifically irrelevant. With a CI you will spot this.

---

## [Home](https://gtpb.github.io/PSLS20/) {-}

---

[← Two sample T-test](02-two-sample-t-test.md) · [Up: contents](index.md)
