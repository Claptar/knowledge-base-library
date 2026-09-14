---
title: Linear regression in matrix form
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd
source_file: sources/statomics-sga21/recapGeneralLinearModel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Linear regression in matrix form

**Source:** [`recapGeneralLinearModel.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Scalar form

- Consider a vector of predictors $\mathbf{x}=(x_1,\ldots,x_p)^T$ and
- a real-valued response $Y$
- then the linear regression model can be written as
$$
Y=f(\mathbf{x}) +\epsilon=\beta_0+\sum\limits_{j=1}^p x_j\beta_j + \epsilon
$$
with i.i.d. $\epsilon\sim N(0,\sigma^2)$

## Matrix form

- $n$ observations $(\mathbf{x}_1,y_1) \ldots (\mathbf{x}_n,y_n)$
- Regression in matrix notation
$$\mathbf{Y}=\mathbf{X\beta} + \mathbf{\epsilon}$$
with $\mathbf{Y}=\left[\begin{array}{c}y_1\\ \vdots\\y_n\end{array}\right]$,
$\mathbf{X}=\left[\begin{array}{cccc} 1&x_{11}&\ldots&x_{1p}\\
\vdots&\vdots&&\vdots\\
1&x_{n1}&\ldots&x_{np}
\end{array}\right]$,
$\mathbf{\beta}=\left[\begin{array}{c}\beta_0\\ \vdots\\ \beta_p\end{array}\right]$ and
$\mathbf{\epsilon}=\left[\begin{array}{c} \epsilon_1 \\ \vdots \\ \epsilon_n\end{array}\right]$

## Least Squares (LS)
- Minimize the residual sum of squares
\begin{eqnarray*}
RSS(\mathbf{\beta})&=&\sum\limits_{i=1}^n e^2_i\\
&=&\sum\limits_{i=1}^n \left(y_i-\beta_0-\sum\limits_{j=1}^p x_{ij}\beta_j\right)^2
\end{eqnarray*}
- or in matrix notation
\begin{eqnarray*}
RSS(\mathbf{\beta})&=&(\mathbf{Y}-\mathbf{X\beta})^T(\mathbf{Y}-\mathbf{X\beta})\\
&=&\Vert \mathbf{Y}-\mathbf{X\beta}\Vert^2_2
\end{eqnarray*}
with the $L_2$-norm of a $p$-dim. vector $v$ $\Vert \mathbf{v} \Vert=\sqrt{v_1^2+\ldots+v_p^2}$
$\rightarrow$ $\hat{\mathbf{\beta}}=\text{argmin}_\beta \Vert \mathbf{Y}-\mathbf{X\beta}\Vert^2_2$

---

### Minimize RSS
$$
\begin{array}{ccc}
\frac{\partial RSS}{\partial \mathbf{\beta}}&=&\mathbf{0}\\\\
\frac{(\mathbf{Y}-\mathbf{X\beta})^T(\mathbf{Y}-\mathbf{X\beta})}{\partial \mathbf{\beta}}&=&\mathbf{0}\\\\
-2\mathbf{X}^T(\mathbf{Y}-\mathbf{X\beta})&=&\mathbf{0}\\\\
\mathbf{X}^T\mathbf{X\beta}&=&\mathbf{X}^T\mathbf{Y}\\\\
\hat{\mathbf{\beta}}&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}
\end{array}
$$

---

### Geometrical Interpretation

Toy Example: fit without intercept

- n=3 and p=2
$$
\mathbf{X}=\left[\begin{array}{cc}
2&0\\
0&2\\
0&0
\end{array}\right]
$$

```r
set.seed(4)
x1 <- c(2,0,0)
x2 <- c(0,2,0)
y <- x1*0.5 + x2*0.5 + rnorm(3,2)
fit <- lm(y~-1+x1+x2)
```

#### Visualise fit

```r

---

[← General Linear Model](04-general-linear-model.md) · [Up: contents](index.md) · [predict values on regular xy grid →](06-predict-values-on-regular-xy-grid.md)
