---
title: Assess assumptions
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd
source_file: sources/gtpb-psls20/theory/06-linearRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Assess assumptions

**Source:** [`theory/06-linearRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Independence: design
- Linearity: inference is useless if the association is not linear
- Homoscedasticity: inference/p-value is incorrect if data are heteroscedastic
- Normality: inference/p-value is incorrect if data are not normally distributed in small samples


## Linearity

```r
brcaSubset %>%
  ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_smooth(se=FALSE,col="grey") +
  geom_smooth(method="lm",se=FALSE)
```


### Residual analysis

- Assumption of linearity is typically assessed using *residual plot*. (Especially if the lineair model has multiple covariates, later chapters)
- predictor of predictions $\hat\beta_0+\hat\beta_1 x$ on $X$-axis
- *residuals* on $Y$-as
$$e_i=y_i-\hat{g}(x_i)=y_i-\hat\beta_0-\hat\beta_1\times x_i,$$

```r
plot(lm1)
```

## Homoscedasticity (equal variances)

- Residuals and squared residuals cary information on the residual variability

- Association with predictors $\rightarrow$ indication of heteroscedasticity.
- Scatterplot of $e_i$ vs $x_i$ or predictions $\hat \beta_0+ \hat \beta_1 x_i$.
- Scatterplot van standardized residual versus $x_i$ or predictions.

## Normality

- If the sample size is large the estimators are normally distributed even if the observations are not normally distributed: central limit theorem
- How many observations? $\rightarrow$ depends on shape and magnitude of deviations
- Assumption: Data are Normally distributed conditional on X:
$$Y_i\vert X_i\sim N(\beta_0+\beta_1X_i,\sigma^2)$$
- QQ-plot of response Y is misleading and useless: distribution of $Y_i$ are different because they have a different conditional mean!

- QQ-plot of the residuals $e_i$

```r
set.seed=200
par(mfrow=c(1,3))
x=rep(1:10,each=20)
y=x+rnorm(length(x))
boxplot(y~x)
qqnorm(y, main="Original observations")
qqline(y)
lmH<-lm(y~x)
plot(lmH,which=2,main="Residuals")
```


```r
plot(lm1,which=2)
```

---

[← Statistical inference](04-statistical-inference.md) · [Up: contents](index.md) · [Invalid assumptions →](06-invalid-assumptions.md)
