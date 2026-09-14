---
title: Statistical inference
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd
source_file: sources/gtpb-psls20/theory/06-linearRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Statistical inference

**Source:** [`theory/06-linearRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

To draw conclusions based on the regression model
$$E(Y|X)=\beta_0+\beta_1 X$$
we need to know

- How the least squares parameter estimators vary from sample to sample, and
- how they deviate under the null hypothesis that there is no association between predictor and response
- Requires a statistical model

- Model the distribution of $Y$ given $X$ explicitly: f_{Y|X}(y)

## Modelling distribution of Y?

1. Besides *Linearity* we need additional assumptions!
2. *Independence*: Observations $(X_1,Y_1), ...,  (X_n,Y_n)$ are made for n independent subjects (is required to estimate the variance)
3. *Homoscedasticity* or *equal variances*: observations vary with equal mean around the regression line
    - Residuals $\epsilon_i$ have equal variance for each $X_i=x$
    - $\text{var}(Y\vert X=x) = \sigma^2$ for each $X=x$
    - $\sigma$ is referred to as the *residual standard deviation*
4. *Normality*: the residuals $\epsilon_i$ are normally distributed

![](https://raw.githubusercontent.com/GTPB/PSLS20/gh-pages/assets/figs/RegModel3.png){width=100%}


- Given 2, 3 and 4
$$\epsilon_i \text{ i.i.d.} N(0,\sigma^2).$$
- Together with 1 this implies:
$$Y_i\vert X_i\sim N(\beta_0+\beta_1 X_i,\sigma^2),$$

- We can show that given these assumption
$$\sigma^2_{\hat{\beta}_0}=\frac{\sum\limits_{i=1}^n X^2_i}{\sum\limits_{i=1}^n (X_i-\bar X)^2} \times\frac{\sigma^2}{n} \text{ en } \sigma^2_{\hat{\beta}_1}=\frac{\sigma^2}{\sum\limits_{i=1}^n (X_i-\bar X)^2}$$
- and the parameter estimators are also normally distributed
$$\hat\beta_0 \sim N\left(\beta_0,\sigma^2_{\hat \beta_0}\right) \text{ en } \hat\beta_1 \sim N\left(\beta_1,\sigma^2_{\hat \beta_1}\right)$$

## High spread of $X$ improves the precision

$$\sigma^2_{\hat{\beta}_1}=\frac{\sigma^2}{\sum\limits_{i=1}^n (X_i-\bar X)^2}$$

![](https://raw.githubusercontent.com/GTPB/PSLS20/gh-pages/assets/figs/spread.png){ width=100% }

- Conditional variance ($\sigma^2$) is unknown
- Estimate using *mean squared error* (MSE)
$$\hat\sigma^2=MSE=\frac{\sum\limits_{i=1}^n \left(y_i-\hat\beta_0-\hat\beta_1\times x_i\right)^2}{n-2}=\frac{\sum\limits_{i=1}^n e^2_i}{n-2}.$$
- This estimator is based on independence (assumption 2) and equality of the variance (assumption 3).
- Devide by $n-2$

Upon the estimation of $\sigma^2$ we obtain following standard errors:

$$\text{SE}_{\hat{\beta}_0}=\hat\sigma_{\hat{\beta}_0}=\sqrt{\frac{\sum\limits_{i=1}^n X^2_i}{\sum\limits_{i=1}^n (X_i-\bar X)^2} \times\frac{\text{MSE}}{n}} \text{ en } \text{SE}_{\hat{\beta}_1}=\hat\sigma_{\hat{\beta}_1}=\sqrt{\frac{\text{MSE}}{\sum\limits_{i=1}^n (X_i-\bar X)^2}}$$

- Again we can construct tests and confidence intervals using
$$T=\frac{\hat{\beta}_k-\beta_k}{SE(\hat{\beta}_k)} \text{ with } k=1,2.$$

- If all assumptions are valid $T$ follows t-verdeling with n-2 degrees of freedom.
\vspace{15pt}
- If no normality, but independence, linearity, equality of mean and large dataset
$$\rightarrow \text{Central Limit theorem}$$


### Breast cancer example

- Negative association between S100A8 and ESR1 gene expression.

- Generalize effect in sample to population using the confidence interval on the mean:
$$[\hat\beta_1 - t_{n-2,\alpha/2} \text{SE}_{\hat\beta_1},\hat\beta_1 + t_{n-2,\alpha/2} \text{SE}_{\hat\beta_1}]$$.

```r
confint(lm1)
```

- Negative association is significant on 5% significance level.


## Hypothesis test

- Translate the research question to assess the association between the S100A8 and ESR1 gene expression to parameters in the model.

- Under the null hypothesis of the absence of an association in the expression of both genes:
$$H_0: \beta_1=0$$

- Under the alternative hypothesis, there is an association between the expression of both genes :
$$H_1: \beta_1\neq0$$
\vspace{15pt}
- Test statistic
$$T=\frac{\hat{\beta}_1-0}{SE(\hat{\beta}_k)}$$
\vspace{15pt}
- Under $H_0$ the statistics follows a t-distribution with n-2 degrees of freedom.

###brca dataset

```r
summary(lm1)
```


- The association between the S100A8 and ESR1 expression is extremely significant  (p<<0.001).
- But, we first have to check all assumptions!
- Otherwise the conclusions based on the statistical test and the CI can be incorrect.

---

[← Parameter estimation](03-parameter-estimation.md) · [Up: contents](index.md) · [Assess assumptions →](05-assess-assumptions.md)
