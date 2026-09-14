---
title: Invalid assumptions
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd
source_file: sources/gtpb-psls20/theory/06-linearRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Invalid assumptions

**Source:** [`theory/06-linearRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Transformation of predictor does not change distribution of Y for given X:

    - not useful to obtain homoscedasticity or Normal distribution
    - useful for linearity when normality and homoscedasticity are valid
    - Often inclusion of higher order terms: $X^2$, $X^3$, ...
    $$Y_i=\beta_0+\beta_1X_i+\beta_2X_i^2+ ... + \epsilon_i$$


- Transformation of response Y can be useful to obtain normality and homoscedasticity

-  $\sqrt(Y)$, $\log(Y)$, 1/Y, ...


## Breast cancer example

Problems with

- heteroscedasticity
- possibly deviations from normality (skewed to the right)
- negative concentration predictions are theoretically impossible
- non-linearity

This is often the case for concentration and intensity measurements

- These are often log-normal distributed (normal distribution upon log-transformatie)
- We also observed a kind of exponential relation with the smoother
- In gene expression literature often $\log_2$ transformation is adopted
- gene-expression on log scale: differences on log scale are fold changes on original scale!


```r
brca %>% ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_smooth()
```

```r
brca %>% ggplot(aes(x=ESR1%>%log2,y=S100A8%>%log2)) +
  geom_point() +
  geom_smooth()
```

```r
lm2<-lm(S100A8%>%log2 ~ ESR1 %>% log2, brca)
plot(lm2)
summary(lm2)
```


```r
confint(lm2)
```


### Interpretation 1

A patient with an ESR1 expression that is one unit on $\log_2$ scale higher than that of another patient on average has a $\log_2$ expression for S100A8 that is `r abs(round(lm2$coef[2],2))` units lower (95% CI [`r paste(round(confint(lm2)[2,],2),collapse=",")`]).

$$\log_2 \hat\mu_1=23.401  -1.615 \times \text{logESR}_1,\text{ } \log_2 \hat\mu_2=23.401  -1.615 \times \text{logESR}_2 $$
$$\log_2 \hat\mu_2-\log_2 \hat\mu_1=  -1.615 (\log_2 \text{ESR}_2-\log_2 \text{ESR}_1) = -1.615 \times 1 = -1.615$$

### Interpretatie 2

Model on log-scale: upon back-transformation we obtain geometric means

\begin{eqnarray*}
\sum\limits_{i=1}^n \frac{\log x_i}{n}&=&\frac{\log x_1 + \ldots + \log x_n}{n}\\\\
&\stackrel{(1)}{=}&\frac{\log(x_1 \times \ldots \times x_n)}{n}=\frac{\log\left(\prod\limits_{i=1}^n x_i\right)}{n}\\\\
&\stackrel{(2)}{=}&\log \left(\sqrt[\leftroot{-1}\uproot{2}\scriptstyle n]{\prod\limits_{i=1}^n x_i}\right)
\end{eqnarray*}

- Population mean $\mu$ is estimated as a geometric mean
- Logarithmic transformation is monotone: we can backtransform confidence intervals on log-scale!


```r
2^lm2$coef[2]
2^-lm2$coef[2]
2^-confint(lm2)[2,]
```

A patient with an ESR1 expression that is 2 times the expression of that of another patient will on average have an  S100A8 expression that is `r round(2^-lm2$coef[2]
,2)` times lower (95\% CI [`r paste(sort(round(2^-confint(lm2)[2,],2)),collapse=",")`]).


$$\log_2 \hat\mu_1=23.401  -1.615 \times \text{logESR}_1,\text{ } \log_2 \hat\mu_2=23.401  -1.615 \times \text{logESR}_2 $$
$$\log_2 \hat\mu_2-\log_2 \hat\mu_1=  -1.615 (\log_2 \text{ESR}_2-\log_2 \text{ESR}_1) $$
$$\log_2 \left[\frac{\hat\mu_2}{\hat\mu_1}\right]=  -1.615 \log_2\left[\frac{ \text{ESR}_2}{\text{ESR}_1}\right] $$
$$\frac{\hat\mu_2}{\hat\mu_1}=\left[\frac{ \text{ESR}_2}{\text{ESR}_1}\right]^{-1.615}=2^ {-1.615} =0.326$$
or
$$\frac{\hat\mu_1}{\hat\mu_2}=2^{1.615} =3.06$$


### Interpretation 3

A patient with an ESR1 expression that is 1\% higher than that of another patient will on average have  an expression-level for S100A8 gen  that is approximately `r round(lm2$coef[2],2)`% lower (95\% CI [`r paste(round(confint(lm2)[2,],2),collapse=",")`])%.

$$\log_2 \hat\mu_1=23.401  -1.615 \times \text{logESR}_1,\text{ } \log_2 \hat\mu_2=23.401  -1.615 \times \text{logESR}_2 $$
$$\log_2 \hat\mu_2-\hat\log_2 \mu_1=  -1.615 (\log_2 \text{ESR}_2-\log_2 \text{ESR}_1) $$
$$\log_2 \left[\frac{\hat\mu_2}{\hat\mu_1}\right]=  -1.615 \log_2\left[\frac{ \text{ESR}_2}{\text{ESR}_1}\right] $$
$$\frac{\hat\mu_2}{\hat\mu_1}=\left[\frac{ \text{ESR}_2}{\text{ESR}_1}\right]^{-1.615}=1.01^ {-1.615} =0.984 \approx -1.6\%$$

This is valid for low to moderate values of $\beta_1$:
$$-10<\beta_1<10 \rightarrow 1.01^{\beta_1} -1 \approx \frac{\beta_1}{100}.$$


## Inference on the mean outcome

- A regression model can also be used for prediction
- Inference on average outcome for a given value of $X=x$, i.e.
$$\hat{g}(x)= \hat{\beta}_0 + \hat{\beta}_1 x$$
- $\hat{g}(x)$ is an estimator of the conditional mean $E[Y\vert X=x]$
- Parameter estimators are Normally distributed and unbiased $\rightarrow$ estimator $\hat{g}(x)$ is also Normally distributed and unbiased.

$$\text{SE}_{\hat{g}(x)}=\sqrt{MSE\left\{\frac{1}{n}+\frac{(x-\bar X)^2}{\sum\limits_{i=1}^n (X_i-\bar X)^2}\right\}}.$$

$$T=\frac{\hat{g}(x)-g(x)}{SE_{\hat{g}(x)}}\sim t_{n-2}$$

- Mean response and confidence intervals for the mean response in R via de `predict(.)` functie.
- `newdata` argument: predictor values (x-values) at which we want to calculate the mean response
- `interval="confidence"` argument to obtain CI.
- Without newdata argument we perform predictions for all predictor values in the dataset used to fit the model.

```r
grid <- 140:4000
g <- predict(lm2,newdata=data.frame(ESR1=grid), interval="confidence")
head(g)
```

Note, that we do not have to transform the new data that we specified for the ESR1 expression because we fitted the model with a call to the `lm` function and specified the transformation within the lm formula using the pipe command!

```r
brca %>% ggplot(aes(x=ESR1%>%log2,y=S100A8%>%log2)) +
  geom_point() +
  geom_smooth(method="lm")
```

## Back-transformation
```r
newdata<-data.frame(cbind(grid,2^g))
brca %>% ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_line(aes(x=grid,y=fit),newdata) +
  geom_line(aes(x=grid,y=lwr),newdata,color="grey") +
  geom_line(aes(x=grid,y=upr),newdata,color="grey")
```

---

[← Assess assumptions](05-assess-assumptions.md) · [Up: contents](index.md) · [Prediction-intervals →](07-prediction-intervals.md)
