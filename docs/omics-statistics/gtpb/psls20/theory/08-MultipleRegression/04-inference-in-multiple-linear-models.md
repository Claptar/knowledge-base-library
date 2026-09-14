---
title: Inference in multiple linear models
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd
source_file: sources/gtpb-psls20/theory/08-MultipleRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Inference in multiple linear models

**Source:** [`theory/08-MultipleRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

If data are representative than the least squares estimators for the intercept and slopes are unbiased.
$$E[\hat \beta_j]=\beta_j,\quad j=0,\ldots,p-1.$$

- Gain insight in the distribution of the parameter estimators so as to generalize the effect in the sample to the population.

- Additional assumptions are needed for inference.

1. *Linearity*

2. *Independence*

3. *Homoscedasticity* of *equal variance*
4. *Normality*: residuals $\epsilon_i$ are normally distributed.

Under these assumptions:
$$\epsilon_i \sim N(0,\sigma^2).$$
en
$$Y_i\sim N(\beta_0+\beta_1 X_{i1}+\ldots+\beta_{p-1} X_{ip-1},\sigma^2)$$

---

- Slopes are again more precise if the predictor values have a larger range.

- Conditional variance ($\sigma^2$) can again be estimated based on the *mean squared error* (MSE):

$$\hat\sigma^2=MSE=\frac{\sum\limits_{i=1}^n \left(y_i-\hat\beta_0-\hat\beta_1 X_{i1}-\ldots-\hat\beta_{p-1} X_{ip-1}\right)^2}{n-p}=\frac{\sum\limits_{i=1}^n e^2_i}{n-p}.$$

Again hypothesis tests and confidence intervals by
$$T_k=\frac{\hat{\beta}_k-\beta_k}{SE(\hat{\beta}_k)} \text{ met } k=0, \ldots, p-1.$$

If all assumptions are satisfied than the statistics $T_k$ t-distributed with $n-p$ degrees of freedom.

---

When normality thus not hold, but lineariteit, independence and homoscedasticity are valid we can again adopt the CLT that states that statistic $T_k$ is approximately normally distributed in large samples.

---

We can build confidence intervals on the slopes by:
$$[\hat\beta_j - t_{n-p,\alpha/2} \text{SE}_{\hat\beta_j},\hat\beta_j + t_{n-p,\alpha/2} \text{SE}_{\hat\beta_j}]$$.

```r
confint(lmVWS)
```

---

Formal hypothesis tests:
$$H_0: \beta_j=0$$
$$H_1: \beta_j\neq0$$

With test statistic
$$T=\frac{\hat{\beta}_j-0}{SE(\hat{\beta}_j)}$$
which follows a t-distribution with $n-p$ degrees of freedom under $H_0$

---

```r
summary(lmVWS)
```

---

## Assess the model assumptions

```r
plot(lmVWS)
```

---

## The non additive multiple linear model
### Interaction between two continuous variables

The previous model is additive because the contribution of the cancer volume on lpsa does not depend on the height of the prostate weight and the svi status.

The slope for lcavol does not depend on log prostate weight and svi.

$$
\beta_0 + \beta_v (x_{v}+\delta_v) + \beta_w x_{w} +\beta_s x_{s} - \beta_0 - \beta_v x_{v} - \beta_w x_{w} -\beta_s x_s = \beta_v \delta_v
$$

The svi status and the log-prostategewicht ($x_w$) do not influence the contribution of the log-tumor volume ($x_v$) to the average log-PSA and vice versa.

---

- It is however possible that the association of lpsa and lcavol depends on the prostate weight.
- The average difference in lpsa for patients that differ in one unit of the log-tumor volume can for instance can be higher for patients wiht a high tumor weight then for those with a low tumor weight.
- The effect of the tumor volume on the PSA depends on the prostate weight.

To model this **interactie** or **effect modification** we can add a product term of both variables to the model

$$
Y_i = \beta_0 + \beta_v x_{iv} + \beta_w x_{iw} +\beta_s x_{is} + \beta_{vw} x_{iv}x_{iw} +\epsilon_i
$$

This term quantifies the *interactie-effect* of predictors $x_v$ en $x_w$ on the mean outcome.

Terms $\beta_vx_{iv}$ and $\beta_wx_{iw}$ are referred to as *main effects* of predictors $x_v$ and $x_w$.

---

The difference in lpsa for patients that differ 1 unit in $X_v$ and have an equal log prostate weight and the same svi status now becomes:

$$
\begin{array}{l}
E(Y | X_v=x_v +1, X_w=x_w, X_s=x_s) - E(Y | X_v=x_v, X_w=x_w, X_s=x_s) \\
\quad = \beta_0 + \beta_v (x_{v}+1) + \beta_w x_w +\beta_s x_{s} + \beta_{vw} (x_{v}+1) x_w - \beta_0 - \beta_v x_{v} - \beta_w x_w -\beta_s x_{s} - \beta_{vw} (x_{v}) x_w \\
\quad = \beta_v +  \beta_{vw} x_w
 \end{array}
 $$

---

```r
lmVWS_IntVW <- lm(lpsa~lcavol + lweight + svi + lcavol:lweight ,prostate)
summary(lmVWS_IntVW)
```

---


```r
par(mfrow=c(1,2))
library(plot3D)
grid.lines = 10
x<-prostate$lcavol
y<-prostate$lweight
z<-prostate$lpsa
fit<-lm(z~x+y+svi,data=prostate)
x.pred <- seq(min(x), max(x), length.out = grid.lines)
y.pred <- seq(min(y), max(y), length.out = grid.lines)

---

[← fitted points for droplines to surface](03-fitted-points-for-droplines-to-surface.md) · [Up: contents](index.md) · [fitted points for droplines to surface →](05-fitted-points-for-droplines-to-surface.md)
