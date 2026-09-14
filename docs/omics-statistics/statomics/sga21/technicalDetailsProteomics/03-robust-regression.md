---
title: Robust regression
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd
source_file: sources/statomics-sga21/technicalDetailsProteomics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Robust regression

**Source:** [`technicalDetailsProteomics.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

- With msqrob2 we perform robust regression to estimate the model parameters of the regression model

- No normality assumption needed
- Robust fit minimises the maximal bias of the estimators
- CI and statistical tests are based on asymptotic theory
- If $\epsilon$ is normal, the M-estimators have a high efficiency!
- ordinary least squares (OLS): minimize loss function $$\sum\limits_{i=1}^n (y_i-\mathbf{x}_i^T\boldsymbol{\beta})^2$$

- M-estimation: minimize loss function
$$\sum\limits_{i=1}^n  \rho\left(y_i-\mathbf{x}_i^T\boldsymbol{\beta}\right)$$
with

  - $\rho$ is symmetric, i.e. $\rho(z)=\rho(-z)$
  - $\rho$ has a minimum at $\rho(0)=0$, is positive for all $z\neq 0$
  - $\rho(z)$ increases as $\vert z\vert$ increases

---

 The estimator $\hat{\mu}$ is also the solution to the equation
 $$
   \sum_{i=1}^n \Psi(y_i - \mathbf{x}_i\boldsymbol{\beta}) =0,
 $$
 where $\Psi$ is the derivative of $\rho$. For $\hat{\beta}$ possessing the robustness property, $\Psi$ should be bounded.

---

 Example: least squares

 - $\rho(z) = z^2$, and thus $\Psi(z)=2z$ (unbounded!). Not robust!

- $\hat{\boldsymbol{\beta}}$ is the solution of
 $$
   \sum_{i=1}^n 2 \mathbf{x}_i (y_i - \mathbf{x}_i^T\boldsymbol{\beta}) = 0 \text{ or } \hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}\mathbf{y}
 $$
 with $\mathbf{X}=[\mathbf{x}_1 \ldots \mathbf{x}_G]^T$

---

 When a location and a scale parameter, say $\sigma$, have to be estimated simultaneously, we write
 $$
   (\hat{\boldsymbol{\beta}},\hat{\sigma}) = \text{ArgMin}_{\boldsymbol{\beta},\sigma} \sum_{i=1}^n \rho\left(\frac{y_i - \mathbf{x}_i^T\boldsymbol{\beta}}{\sigma}\right)
   \text{ and } \sum_{i=1}^n \Psi\left(\frac{y_i - \mathbf{x}_i^T\boldsymbol{\beta}}{\sigma}\right) =0.
 $$

 Define $u_i = \frac{y_i - \mathbf{x}_i^T\boldsymbol{\beta}}{\sigma}$. The last estimation equation is equivalent to
 $$
   \sum_{i=1}^n w(u_i) u_i = 0 ,
 $$
 with weight function $w(u)=\Psi(u)/u$. This is the typical form that appears when solving the
 *iteratively reweighted least squares problem*,
 $$
   (\hat{\boldsymbol{\beta}},\hat{\sigma}) = \text{ArgMin}_{\mu,\sigma} \sum_{i=1}^n w(u_i^{(k-1)}) \left(u_i^{(k)}\right)^2 ,
 $$
 where $k$ represents the iteration number.

---

## Some Examples of Robust Functions

![](https://raw.githubusercontent.com/statOmics/SGA2020/gh-pages/assets/TableRobust.PNG)

PhD thesis Bolstad 2004

---

## The $\rho$ functions

![](https://raw.githubusercontent.com/statOmics/SGA2020/gh-pages/assets/RhoRobust.PNG)

PhD thesis Bolstad 2004

---

### Common $\Psi$-Functions
![](https://raw.githubusercontent.com/statOmics/SGA2020/gh-pages/assets/robustRegressionPsi.png)

PhD thesis Bolstad 2004

---

### Corresponding Weight Functions
![](https://raw.githubusercontent.com/statOmics/SGA2020/gh-pages/assets/robustRegressionWeights.png)

PhD thesis Bolstad 2004

---

```r
library("MASS")
rfit <- rlm(y ~ location * tissue + patient, colData(pe), maxit=1)
qplot(fit$coefficient[-1],
  rfit$coefficient[-1],
  xlab="fit",
  ylab="robust fit") +
  geom_abline() +
  xlim(range(c(fit$coefficient[-1],rfit$coefficient[-1]))) +
  ylim(range(c(fit$coefficient[-1],rfit$coefficient[-1])))
```

---

```r
rfit$w
plot(
  rfit$fitted,
  rfit$res,
  cex=rfit$w,
  pch=19,col=2,
  cex.lab=1.5,
  cex.axis=1.5,
  ylab="residuals",
  xlab="fit")
points(rfit$fitted, rfit$res , cex= 1.5)
```

---

```r
summary(fit)
summary(rfit)
rowData(pe[["proteinRobust"]])$msqrobModels[[2]] %>% getCoef
```

---

## Understanding implementation of robust regression

### Simulate 20 observations from a linear model with errors that follow a normal distribution

```r
set.seed <- 112358
nobs <- 20
sdy <- 1
xsim <- seq(0, 1, length.out = nobs)
ysim <- 10 + 5*xsim + rnorm(nobs, sd = sdy)
```

### add outlier at high leverage point

```r
ysim[nobs] <- 7
```

### fit linear model

```r
ols <- lm(ysim ~ xsim)
```

### fit robust linear model

```r
library(MASS)
mEst <- rlm(ysim ~ xsim)
```

#### plot results

```r
plot(xsim, ysim)
abline(ols, lwd = 2)
abline(mEst, col = "red", lwd = 2)
legend("topleft",
  legend = c("OLS", "M-estimation"),
  lwd = 2,
  col = 1:2)
round(mEst$w,3)
```

The plot clearly shows that the outlier has a high impact on the slope estimate.
This is because the outlier is at a high leverage point, i.e. far from the average covariate pattern.

### Implement it yourself
#### start from ols fit

```r
lmMod <- ols
```

#### Use robust variance estimator to calculate the z

```r
res <- lmMod$res
stdev <- mad(res)
stdev
median(abs(res-median(res)))*1.4826
z <- res/stdev
```

#### Calculate weights use psi.huber function

```r
w <- psi.huber(z)
plot(xsim, ysim)
plot(xsim, lmMod$res, cex = w, pch = 19, col = "red")
points(xsim,lmMod$res, cex = 1.5)
```

#### Perform a weighted regression use lm with weights=w

```r
lmMod <- lm(ysim~xsim, weights = w)
```

#### Plot results

```r
plot(xsim, ysim)
abline(ols, lwd = 2)
abline(mEst, col = "red", lwd = 2)
abline(lmMod, col = "blue", lwd = 2)
legend("topleft",
  legend = c("OLS","M-estimation","Our Impl"),
  lwd = 2,
  col = c("black", "red", "blue"))
```

#### Repeat this many times
```r
lmMod <- ols
for (k in 1:3)
{
######repeat this part several times until convergence
#use robust variance estimator to calculate the z
res <- lmMod$res
stdev <- mad(res)
median(abs(res-median(res)))*1.4826

z <- res/stdev

#calculate weights
#use psi.huber function
w <- psi.huber(z)

#perform a weighted regression use lm with weights=w
lmMod <- lm(ysim ~ xsim, weights = w)

#plot results
plot(xsim,ysim)
abline(ols, lwd = 2)
abline(mEst, col = "red", lwd = 2)
abline(lmMod, col = "blue", lwd = 2)
legend("topleft",
  legend = c("OLS","M-estimation","Our Impl"),
  lwd = 2,
  col = c("black", "red", "blue")
  )
####################################
}
```

---

[← Linear regression](02-linear-regression.md) · [Up: contents](index.md) · [Empirical Bayes/Moderated $t$-test. →](04-empirical-bayes-moderated--test.md)
