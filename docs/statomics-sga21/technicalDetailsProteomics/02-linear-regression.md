---
title: Linear regression
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd
source_file: sources/statomics-sga21/technicalDetailsProteomics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Linear regression

**Source:** [`technicalDetailsProteomics.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

- Consider a vector of predictors $\mathbf{x}_i=(x_1,\ldots,x_{p-1})$ and
- a real-valued response $Y_i$
- with $i = 1, \ldots, n$
- then the linear regression model can be written as
$$
Y_i=f(\mathbf{x}) +\epsilon=\beta_0+\sum\limits_{j=1}^{p-1} x_{ij}\beta + \epsilon_i
$$
with i.i.d. $\epsilon_i\sim N(0,\sigma^2)$

---

- $n$ observations $(\mathbf{x}_1,y_1) \ldots (\mathbf{x}_n,y_n)$
- Regression in matrix notation
$$\mathbf{Y}=\mathbf{X\beta} + \boldsymbol{\epsilon}$$
with $\mathbf{Y}=\left[\begin{array}{c}y_1\\ \vdots\\y_n\end{array}\right]$,
$\mathbf{X}=\left[\begin{array}{cccc} 1&x_{11}&\ldots&x_{1p-1}\\
\vdots&\vdots&&\vdots\\
1&x_{n1}&\ldots&x_{np-1}
\end{array}\right]$,
$\boldsymbol{\beta}=\left[\begin{array}{c}\beta_0\\ \vdots\\ \beta_{p-1}\end{array}\right]$ and
$\boldsymbol{\epsilon}=\left[\begin{array}{c} \epsilon_1 \\ \vdots \\ \epsilon_n\end{array}\right]$

---

## Least Squares (LS)

- Minimize the residual sum of squares
\begin{eqnarray*}
RSS(\boldsymbol{\beta})&=&\sum\limits_{i=1}^n e^2_i\\
&=&\sum\limits_{i=1}^n \left(y_i-\beta_0-\sum\limits_{j=1}^p x_{ij}\beta_j\right)^2
\end{eqnarray*}
- or in matrix notation
\begin{eqnarray*}
RSS(\boldsymbol{\beta})&=&(\mathbf{Y}-\mathbf{X\beta})^T(\mathbf{Y}-\mathbf{X\beta})\\
&=&\Vert \mathbf{Y}-\mathbf{X\beta}\Vert^2
\end{eqnarray*}
with the $L_2$-norm of a $p$-dim. vector $v$ $\Vert \mathbf{v} \Vert=\sqrt{v_1^2+\ldots+v_p^2}$

- $\rightarrow$ $\hat{\boldsymbol{\beta}}=\text{argmin}_\beta \Vert \mathbf{Y}-\mathbf{X\beta}\Vert^2$}


---

### Minimize RSS
$$
\begin{array}{ccc}
\frac{\partial RSS}{\partial \boldsymbol{\beta}}&=&\mathbf{0}\\\\
\frac{(\mathbf{Y}-\mathbf{X\beta})^T(\mathbf{Y}-\mathbf{X\beta})}{\partial \boldsymbol{\beta}}&=&\mathbf{0}\\\\
-2\mathbf{X}^T(\mathbf{Y}-\mathbf{X\beta})&=&\mathbf{0}\\\\
\mathbf{X}^T\mathbf{X\beta}&=&\mathbf{X}^T\mathbf{Y}\\\\
\hat{\boldsymbol{\beta}}&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}
\end{array}
$$

---

#### Heart example

```r
y <- assay(pe[["proteinRobust"]])[2,]
fit <- lm(y ~ location*tissue + patient, data = colData(pe), x = TRUE)
head(fit$x,4)
```

The model matrix can also be obtained without fitting the model:

```r
X <- model.matrix(~ location * tissue + patient, colData(pe))
head(X,4)
```

Least squares:
```r
betas <- solve(t(X)%*%X) %*% t(X) %*% y
cbind(fit$coef, betas)
```

---

### Variance Estimator?
$$
\begin{array}{ccl}
\hat{\boldsymbol{\Sigma}}_{\hat{\boldsymbol{\beta}}}
&=&\text{var}\left[(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}\right]\\\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\text{var}\left[\mathbf{Y}\right]\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\\\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T(\mathbf{I}\sigma^2)\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}
\\\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{I}\quad\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\sigma^2\\\\
%\hat{\boldmath{\Sigma}}_{\hat{\boldsymbol{\beta}}}&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\var\left[\mathbf{Y}\right](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\sigma^2\\\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\sigma^2
\end{array}
$$

---

#### heart example


```r
summary(fit)$cov.unscaled * sigma(fit)^2
```

```r
n <- nrow(X)
p <- ncol(X)
mse <- sum((y-X%*%betas)^2)/(n-p)
SigmaBeta <- solve(t(X)%*%X) * mse
SigmaBeta
range(SigmaBeta - summary(fit)$cov.unscaled * sigma(fit)^2)
```

```r
data.frame(summary(fit)$coef[,1:2], betas = betas, seBetas = diag(SigmaBeta)^.5)
```

## Contrasts

When we assess a contrast we assess a linear combination of model parameters:

$$ H_0: \mathbf{L^T\beta} = 0 \text{ vs } H_1: \mathbf{L^T\beta} \neq 0 $$

Estimator of Contrast?

$$\mathbf{L}^T\hat{\boldsymbol{\beta}}$$


Variance?

$$
\boldsymbol{\Sigma}_{\mathbf{L}\hat{\boldsymbol{\beta}}}=\mathbf{L}^T\boldsymbol{\Sigma}_{\hat{\boldsymbol{\beta}}}\mathbf{L}
$$

---

### heart example

```r
L <- makeContrast(
  c(
    "tissueV = 0",
    "tissueV + locationR:tissueV = 0",
    "tissueV + 0.5*locationR:tissueV = 0","locationR:tissueV = 0"),
  parameterNames =
    rowData(pe[["proteinRobust"]])$msqrobModels[[2]] %>%
    getCoef %>%
    names
  )
L
```

```r
contrasts <- t(L) %*% betas
SigmaContrasts <- t(L) %*% SigmaBeta %*% L
seContrasts <- SigmaContrasts %>%
  diag %>%
  sqrt
```

Comparison with lm and glht results

```r
library(multcomp)
fitGlht <- glht(fit, linfct = t(L))
summary(fitGlht, test = adjusted("none"))
data.frame(contrasts, seContrasts)
```

- Note, that the power for assessing $\log_2$ FC between ventriculum and atrium  left and right is the same. Indeed, the standard errors are equal for both effects.


- Note, that the power for assessing $\log_2$ FC between ventriculum and atrium over both heart regions is higher than when assessing the effect left or right.

  - Indeed, the standard error is a factor $\sqrt{2}$ smaller for the former effect
  - We intuitively can explain this because we can use all samples (double the number of samples) to assess the average effect.
  - Hence the variance is a factor two smaller, and the se with a factor $\sqrt{2}$

- Note, that we have the lowest power to pick up an interaction effect. Indeed, the se is a factor $\sqrt{2}$ larger than for the ventriculum - atrium effect left or right and a factor 2 larger than for the average effect between ventriculum and atrium.

```r
seContrasts / seContrasts[1]
sqrt(2)
1/sqrt(2)
```

### t-tests

 - When the assumptions of the linear model hold
$$
\hat{\boldsymbol{\beta}} \sim MVN\left[\boldsymbol{\beta},\left(\mathbf{X}^T\mathbf{X}\right)^{-1}\sigma^2\right]
$$
- Hence,
$$
\mathbf{L}^T\hat{\boldsymbol{\beta}} \sim MVN\left[\mathbf{L}^T\boldsymbol{\beta},\mathbf{L}^T\left[\left(\mathbf{X}^T\mathbf{X}\right)^{-1}\sigma^2\right]\mathbf{L}\right]
$$
- We estimate $\sigma^2$ by MSE
$$\hat{\sigma}^2=\frac{\mathbf{e}^T\mathbf{e}}{n-p} \rightarrow \hat{\boldsymbol{\Sigma}}_{\hat{\boldsymbol{\beta}}}=\left(\mathbf{X}^T\mathbf{X}\right)^{-1}\hat\sigma^2$$

- When we test one contrast at the time (e.g. the $k^\text{th}$ contrast) the statistic reduces to

$$T=\frac{\mathbf{L}_k^T\hat{\boldsymbol{\beta}}}{\sqrt{\left(\mathbf{L}^T_k\hat{\boldsymbol{\Sigma}}_{\hat{\boldsymbol{\beta}}}\mathbf{L}_k\right)}} \underset{H_0}{\sim} t_{n-p}$$
follows a t distribution with n-p degrees of freedom under $H_0: \mathbf{L}^T_k\hat{\boldsymbol{\beta}}=0$

---

#### heart example

```r
tContrasts <- contrasts/seContrasts
pContrasts <- pt(abs(tContrasts),
  df = n - p,
  lower.tail = FALSE) * 2
```

Comparison with lm and glht results

```r
summary(fitGlht, test = adjusted("none"))
data.frame(contrasts, seContrasts, tContrasts, pContrasts)
```


---

### Omnibus test

- We can also assess all contrasts simultaneously with the omnibus null hypothesis:
$$H_0: \mathbf{L}^T\hat{\boldsymbol{\beta}}=\mathbf{0}$$

- Statistic
$$\mathbf{F}=\frac{\hat{\boldsymbol{\beta}}^T\mathbf{L}\left(\mathbf{L}^T\hat{\boldsymbol{\Sigma}}_{\hat{\boldsymbol{\beta}}}\mathbf{L}\right)^{-1}\mathbf{L}^T\hat{\boldsymbol{\beta}}}{n_c} \underset{H_0}{\sim} F_{n_c,n-p}$$
follows an F distribution with $n_c$ and n-p degrees of freedom under the omnibus null hypothesis.
- Note, that $n_c$ equals the number of contrasts, and
- $\mathbf{L}$ is assumed to be full rank

---


If the matrix \mathbf{L} is not full rank, but has rank $r < n_c$

- i.e. some of the contrasts can be written as linear combinations of other contrasts,
- the inverse of the variance covariance matrix of the contrasts does not exist
- we can then decompose L in $r$ orthogonal contrasts $\mathbf{Q}$ with
$$\mathbf{Q}_j^T \mathbf{Q}_k^T = \delta_{jk},$$

- $j,k \in 1,\ldots,r$,

- $\delta{jk} = 0$ and if $j\neq k$ $\delta{jk} = 1$

- Decomposition can be done using the QR decomposition

- We can than assess the omnibus null hypothesis using the statistic:
$$\mathbf{F}=\frac{\hat{\boldsymbol{\beta}}^T\mathbf{Q}_r\left(\mathbf{Q}^T_r\hat{\boldsymbol{\Sigma}}_{\hat{\boldsymbol{\beta}}}\mathbf{Q}_r\right)^{-1}\mathbf{Q}^T_r\hat{\boldsymbol{\beta}}}{r} \underset{H_0}{\sim} F_{r,n-p}$$

---

#### Heart example

```r
try(solve(SigmaContrasts))
```

- We cannot invert the variance matrix of the contrasts!
- Indeed, the contrasts are linear combinations of two parameters and the contrast matrix $\mathbf{L}$ will thus have rank 2
- We calculate orthogonal contrasts:

```r
qrL <- qr(L)
r <- qrL$rank
r
Q <- qr.Q(qrL)[,1:r]
rownames(Q) <- rownames(L)
Q
```

- Q is orthonormal

```r
t(Q)%*%Q
```

Exploring Q shows that assessing the omnibus hypothesis is thus equivalent to assessing if the null hypothesis that
$$H_0: \beta_\text{tissue} = \beta_\text{tissue:location} = 0$$

```r
est <- t(Q) %*% betas
SigmaEst <- t(Q) %*% SigmaBeta %*% Q
Fstat <- t(est) %*% solve(SigmaEst) %*% est / r
pOmnibus <- pf(Fstat, r, p, lower.tail = FALSE)
```

- Comparison with lm results
- We can assess the omnibus hypothesis also by comparing two models
    - model with location, tissue, location - tissue interaction and patient effect
    - null model: model with location and patient effect

```r
fit0 <- lm(y ~ location + patient, colData(pe))
anova(fit, fit0)
Fstat
pOmnibus
```

---

[← Preamble](01-preamble.md) · [Up: contents](index.md) · [Robust regression →](03-robust-regression.md)
