---
title: Sum of squares and Anova-table
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd
source_file: sources/gtpb-psls20/theory/06-linearRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Sum of squares and Anova-table

**Source:** [`theory/06-linearRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

##Total sum of squares
$$\text{SSTot} = \sum_{i=1}^n (Y_i-\bar{Y})^2.$$

- SStot can be used to estimate the variance of the **marginal distribution** of the response.

- In this chapter we focused on the **conditional distribution** $f(Y\vert X=x)$.

- We known that MSE is a good estimate of the variance of the conditional distribution of  $Y\vert X=x$.


```r
brca$log2ESR1<-log2(brca$ESR1)
brca$log2S100A8<-log2(brca$S100A8)
plot(log2S100A8~log2ESR1,data=brca,xlab="ESR1 expressie (log2)",ylab="S100A8 expressie (log2)",cex.axis=1.5,cex.main=1.5,cex.lab=1.5,col=4)
abline(h=mean(brca$log2S100A8))
for (i in 1:length(brca$log2S100A8)) lines(rep(brca$log2ESR1[i],2),c(mean(brca$log2S100A8),brca$log2S100A8[i]),lty=2,col=4)
```

## Sum of squares of the regression SSR

$$\text{SSR} = \sum_{i=1}^n (\hat{Y}_i - \bar{Y})^2 = \sum_{i=1}^n (\hat{g}(x_i) - \bar{Y})^2.$$

- Is a measure for the deviation of the predictions on the regression line and the marginal mean of the response.

- Another interpretation: difference between two models

    - Estimated model $\hat{g}(x)=\hat\beta_0+\hat\beta_1x$
    - Estimated model without predictor (only intercept): $g(x)=\beta_0$ $\rightarrow$ $\beta_0$ will be equal to $\bar{Y}$.

- SSR measures the size of the effect of the predictor

```r
plot(log2S100A8~log2ESR1,brca,xlab="ESR1 expressie (log2)",ylab="S100A8 expressie (log2)",cex.axis=1.5,cex.main=1.5,cex.lab=1.5)
abline(h=mean(brca$log2S100A8))
abline(lm2,col=2)
points(brca$log2ESR1,lm2$fitted,pch=2,col=2)
for (i in 1:length(brca$log2S100A8)) lines(rep(brca$log2ESR1[i],2),c(mean(brca$log2S100A8),lm2$fitted[i]),lty=2,col=2)
```


## Sum of Squares of the Error

$$ \text{SSE} = \sum_{i=1}^n (Y_i-\hat{Y}_i )^2 = \sum_{i=1}^n \left\{Y_i-\hat{g}\left(x_i\right)\right\}^2.$$

- The smaller SSE the better the fit.


- Least squares method!

---

```r
plot(log2S100A8~log2ESR1,brca,xlab="ESR1 expressie (log2)",ylab="S100A8 expressie (log2)",cex.axis=1.5,cex.main=1.5,cex.lab=1.5)
abline(lm2,col=2)
points(brca$log2ESR1,lm2$fitted,pch=2,col=2)
for (i in 1:length(brca$log2S100A8)) lines(rep(brca$log2ESR1[i],2),c(brca$log2S100A8[i],lm2$fitted[i]),lty=2)
```

We can show that SST can be decomposed in
\begin{eqnarray*}
  \text{SSTot}
    &=&  \sum_{i=1}^n (Y_i-\bar{Y})^2 \\
    &=&  \sum_{i=1}^n (Y_i-\hat{Y}_i+\hat{Y}_i-\bar{Y})^2 \\
    &=&  \sum_{i=1}^n (Y_i-\hat{Y}_i)^2+\sum_{i=1}^n(\hat{Y}_i-\bar{Y})^2 \\
    &=&  \text{SSE }+\text{SSR}
  \end{eqnarray*}

-  Total variability in the data (SSTot) is partially explained by the predictor (SSR).
- Variability that we cannot explain with the regression model is the residual variability (SSE).


## Determination coefficient

$$ R^2 = 1-\frac{\text{SSE}}{\text{SSTot}}=\frac{\text{SSR}}{\text{SSTot}}.$$

- *Fraction of total variability of the sample outcomes explained by the model*.

- Large $R^2$ indicates that the model has the potential to make good predictions  (small SSE).

- Not very indicative for p-value of the test $H_0:\beta_1=0$ vs $H_1:\beta_1\neq0$.

  - p-value is largely determined by SSE and sample size $n$, but not by SSTot.
  - $R^2$ is determined by SSE and SSTot but not by sample size $n$.
- Model with low $R^2$ is still useful to study associations as long as the association is modelled correctly!

### Breast cancer example

```r
summary(lm2)
```

## F-Test in simple linear model

- Sum of squares are the bases for $F$-tests
$$  F  = \frac{\text{MSR}}{\text{MSE}}$$

with  $\text{MSR} = \frac{\text{SSR}}{1} \text{ and } \text{MSE} = \frac{\text{SSE}}{n-2}.$

- MSR mean sum of squares of the regression,

- denominators 1 en $n-2$ are the degrees of freedom of SSR and SSE.

- Under $H_0: \beta_1=0$
$$H_0:F = \frac{\text{MSR}}{\text{MSE}} \sim F_{1,n-2},$$
- F-test is always two-sided! $H_1:\beta_1\neq 0$
$$  p = P_0\left[F\geq f\right]=1-F_F(f;1,n-2)$$


```r
summary(lm2)
```


```r
grid<-seq(0,10,.1)
plot(grid,df(grid,1,30),type="l",xlab="F",ylab="Density",main="F-distribution with 1 df in the nominator and 30 in the denominator",cex.main=1.5,cex.axis=1.5,cex.lab=1.5)
```


## Anova Table


| |Df|Sum Sq|Mean Sq|F value|Pr(>F)|
|---|---|---|---|---|---|
|Regression|degrees of freedom SSR|SSR|MSR|f-statistic|p-value|
|Error|degrees of freedom SSE|SSE|MSE| | |

```r
anova(lm2)
```


## Dummy variables

- Linear regression model  can also be used to compare two group means.
- brca: difference in average age between patients with unaffected and affected lymph nodes.

- Define dummy variabele
$$x_i = \left\{ \begin{array}{ll}
1 & \text{affected lymph nodes} \\
0 & \text{unaffected lymph nodes} \end{array}\right.$$

- group with $x_i=0$ is referred to as the  **reference group**.

- Regression model remains unaltered,
$$Y_i = \beta_0 + \beta_1 x_i +\epsilon_i$$
with $\epsilon_i \text{ iid } N(0,\sigma^2)$


Because $x_i$ only can take two values, we can study the regression model for each value of  $x_i$ separately:
$$ \begin{array}{lcll}
   Y_i &=& \beta_0 +\epsilon_i &\text{unaffected lymph nodes} (x_i=0) \\
   Y_i &=& \beta_0 + \beta_1 +\epsilon_i &\text{ affected lymph nodes} (x_i=1) .
 \end{array}$$
So
 \begin{eqnarray*}
   E\left[Y_i\mid x_i=0\right] &=& \beta_0 \\
   E\left[Y_i\mid x_i=1\right] &=& \beta_0 + \beta_1,
\end{eqnarray*}

 Hence, the interpretation of $\beta_1$:
$$   \beta_1 = E\left[Y_i\mid x_i=1\right]-E\left[Y_i\mid x_i=0\right]$$

$\beta_1$ is the average age difference between patients with affected and patients with unaffected lymph nodes (reference group).

With notation $\mu_0= E\left[Y_i\mid x_i=0\right]$ and $\mu_1= E\left[Y_i\mid x_i=1\right]$ this becomes
$$\beta_1 = \mu_1-\mu_0.$$

We can show that
$$\begin{array}{ccll}
 \hat\beta_0
   &=& \bar{Y}_1&\text{ (sample mean of reference group)} \\
 \hat\beta_1
   &=& \bar{Y}_2-\bar{Y}_1&\text{(estimator of effect size)} \\
 \text{MSE}
   &=& S_p^2 .
\end{array}$$

Tests $H_0:\beta_1=0$ vs.  $H_1:\beta_1\neq0$ can be used to assess the null hypothesis of the  two-sample $t$-test, $H_0:\mu_1=\mu_2$ vs $H_1:\mu_1\neq\mu_2$.


```r
brca$node <- as.factor(brca$node)
t.test(age~node,brca,var.equal=TRUE)
```

```r
lm3 <- lm(age~node,brca)
summary(lm3)
```

```r
plot(lm3)
```


```r
brca %>% ggplot(aes(x=node%>%as.factor,y=age)) +
  geom_boxplot()
```


```r
par(mfrow=c(3,3))
set.seed(354)
for(i in 1:9) plot(rnorm(32)~node,brca,ylab="iid N(0,1)")
```


## Observational study

- We cannot conclude that age causes a higher risk for affected lymph nodes.
- Possibly **confounding**: no randomisation $\rightarrow$ groups of patients with affected and unaffected lymph nodes. They can also differ in other characteristics.

- We can only conclude that there is an association between lymph node status and age.

- However, the association does not have to be causal!


- Note, that this is also the case for the linear model for $\log_2$-S100A8-expression.

    - Because we were not able to fix the  ESR1-expression experimentally we cannot conclude that a higher ESR1-expression causes a decrease in the S100A8-expression.
    - We can only conclude that there is a negative association.
    - To assess the impact of a gene on other gene typically knockout mutants are used in the lab.


---

---

[← Prediction-intervals](07-prediction-intervals.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) →](09-home-https-gtpb-github-io-psls20.md)
