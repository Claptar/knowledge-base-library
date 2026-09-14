---
title: Parameter estimation
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd
source_file: sources/gtpb-psls20/theory/06-linearRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Parameter estimation

**Source:** [`theory/06-linearRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Least squares

```r
brcaSubset %>%
  ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_smooth(se=FALSE,col="grey") +
  geom_smooth(method="lm",se=FALSE)
```

- Parameters $\beta_0$ en $\beta_1$ are unknown.

- Estimate them using sample

- Best fitting line

    - Point on regression line for a given $x_i$: $(x_i, \beta_0 + \beta_1 x_i)$ as close as possible $(x_i, y_i)$
    - Choose $\beta_0$ and $\beta_1$ so that the sum between predicted and observed points becomes as small as possible.

$$SSE=\sum_{i=1}^n (y_i-\beta_0-\beta_1 x_i)^2=\sum_{i=1}^n e_i^2$$

with residuals $e_i$ the vertical distances from the observations to the fitted regression line

## Estimators that minimise SSE

$$\hat{\beta_1}= \frac{\sum\limits_{i=1}^n (y_i-\bar y)(x_i-\bar x)}{\sum\limits_{i=1}^n (x_i-\bar x_i)^2}=\frac{\mbox{cor}(x,y)s_y}{s_x} $$

$$\hat{\beta_0}=\bar y - \hat{\beta}_1 \bar x $$

Note, that the slope of the least squares fit is proportional to the correlation between the response and the predictor.

Fitted model allows to:

  - predict the response for subjects with a given value $x$ for the predictor:
$$\text{E} [ Y | X = x]=\hat{\beta}_0+\hat{\beta}_1x$$

  - Assess how the mean response differs between two groups of subjects that differ $\delta$ units in the predictor:

$$\text{E}\left[Y|X=x+\delta\right]-\text{E}\left[Y|X=x\right]= \hat{\beta}_1\delta$$

### Breast cancer example

```r
lm1 <- lm(S100A8~ESR1,brcaSubset)
summary(lm1)
```

$$E(Y|X=x)=`r round(lm1$coef[1],2)`-`r abs(round(lm1$coef[2],3))` x$$

- Expected S100A8 expression is on average  `r abs(round(lm1$coef[2],3)*1000)` units lower for patients with ESR1 expression level that is 1000 units higher

- Expected S100A8 expression level for patients with an ESR1 expression level of 2000:
$$`r round(lm1$coef[1],2)`-`r abs(round(lm1$coef[2],3))`\times 2000=`r round(lm1$coef[1]+lm1$coef[2]*2000,2)`$$

- Expected S100A8 expression level for patients with an ESR1 expression level of 4000:
$$`r round(lm1$coef[1],2)`-`r abs(round(lm1$coef[2],3))`\times 4000=`r round(lm1$coef[1]+lm1$coef[2]*4000,2)`$$
- Be careful when you extrapolate! (We can only assess the assumption of linearity within the range of the data).

---

[← Lineair Regression](02-lineair-regression.md) · [Up: contents](index.md) · [Statistical inference →](04-statistical-inference.md)
