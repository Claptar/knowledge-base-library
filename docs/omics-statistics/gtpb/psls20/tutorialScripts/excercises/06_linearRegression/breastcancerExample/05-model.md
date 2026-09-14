---
title: Model
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Model

**Source:** [`tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

We will model the data on the log2 scale and we assume the following statistical model:

$$Y_i\vert X_i\sim N(\beta_0+\beta_1X_i,\sigma^2)$$

with $Y_i$ the log2 transformed S100A8 gene expression and $X_i$ the log2 transformed ESR1 gene expression.

## Model fitting

We fit the model to the data using the lm function and we first assess the assumptions. Because the subjects were selected at random from the population they are independent. We still have to check the following assumptions.

1. Linearity
2. Equality of the variance
3. The residuals are normally distribution.

```r
lm2<-lm(S100A8%>%log2 ~ ESR1 %>% log2, brca)
plot(lm2)
summary(lm2)
```

In the residuals vs fitted values plot we observe that the residuals are nicely spread around zero with more or less the same variance and we do not observed a trend in the residuals so there is no indication on deviations from linearity and homoscedasticity.

The QQ-plot further shows no substantial deviations from normality. So the assumptions hold.

We can now assess a formal hypothesis test to for the linear association between the S100A8 gene and the ESR1 gene expression at the log2 scale.

We can translate the hypothesis that there is an association between the S100A8 and ESR1 gene expression in terms of the slope of the model, so under the alternative hypothesis $\beta_1$ is different from zero.
$$H_1: \beta_1 \neq 0$$

With data we can never prove a hypothesis, so we therefore falsify the opposite: the null hypothesis the there is no association between the expression of both genes:

$$H_0: \beta_0 = 0$$
We can do this by adopting a t-test on the slope and by using confidence intervals on the slope.

```r
summary(lm2)
confint(lm2)
```

Both the t-test and the confidence interval indicate that association is extremely significant.
The interval moreover shows that the association is biologically relevant.

We will transform slope and the confidence interval back to the original scale to interpret the results in terms of fold changes.

```r
2^(lm2$coef)
```

```r
2^confint(lm2)
```

---

[← Descriptive statistics](04-descriptive-statistics.md) · [Up: contents](index.md) · [Conclusion →](06-conclusion.md)
