---
title: Linear regression in matrix form
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd
source_file: sources/statomics-sga21/recapGeneralLinearModel.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`recapGeneralLinearModel.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Linear regression in matrix form

### Scalar form

- Consider a vector of predictors $\mathbf{x}=(x_1,\ldots,x_p)^T$ and
- a real-valued response $Y$
- then the linear regression model can be written as

$$
Y=f(\mathbf{x}) +\epsilon=\beta_0+\sum\limits_{j=1}^p x_j\beta_j + \epsilon
$$

with i.i.d. $\epsilon\sim N(0,\sigma^2)$

### Matrix form

- $n$ observations $(\mathbf{x}_1,y_1) \ldots (\mathbf{x}_n,y_n)$
- Regression in matrix notation

$$
\mathbf{Y}=\mathbf{X\beta} + \mathbf{\epsilon}
$$

with $\mathbf{Y}=\left[\begin{array}{c}y_1\\ \vdots\\y_n\end{array}\right]$,
$\mathbf{X}=\left[\begin{array}{cccc} 1&x_{11}&\ldots&x_{1p}\\
\vdots&\vdots&&\vdots\\
1&x_{n1}&\ldots&x_{np}
\end{array}\right]$,
$\mathbf{\beta}=\left[\begin{array}{c}\beta_0\\ \vdots\\ \beta_p\end{array}\right]$ and
$\mathbf{\epsilon}=\left[\begin{array}{c} \epsilon_1 \\ \vdots \\ \epsilon_n\end{array}\right]$

### Least Squares (LS)
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

#### Minimize RSS

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

#### Geometrical Interpretation

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

##### Visualise fit

```r
# predict values on regular xy grid
x1pred <- seq(-1, 3, length.out = 10)
x2pred <- seq(-1, 3, length.out = 10)
xy <- expand.grid(x1 = x1pred,
x2 = x2pred)
ypred <- matrix (nrow = 30, ncol = 30,
data = predict(fit, newdata = data.frame(xy),
interval = "prediction"))

library(plot3D)


# fitted points for droplines to surface
th=20
ph=5
scatter3D(x1,
  x2,
  y,
  pch = 16,
  col="darkblue",
  cex = 1,
  theta = th,
  ticktype = "detailed",
  xlab = "x1",
  ylab = "x2",
  zlab = "y",
  colvar=FALSE,
  bty = "g",
  xlim=c(-1,3),
  ylim=c(-1,3),
  zlim=c(-2,4))

for (i in 1:3)
  lines3D(
    x = rep(x1[i],2),
    y = rep(x2[i],2),
    z = c(y[i],fit$fitted[i]),
    col="darkblue",
    add=TRUE,
    lty=2)

z.pred3D <- outer(
  x1pred,
  x2pred,
  function(x1,x2)
  {
    fit$coef[1]*x1+fit$coef[2]*x2
  })

x.pred3D <- outer(
  x1pred,
  x2pred,
  function(x,y) x)

y.pred3D <- outer(
  x1pred,
  x2pred,
  function(x,y) y)

surf3D(
  x.pred3D,
  y.pred3D,
  z.pred3D,
  col="blue",
  facets=NA,
  add=TRUE)
```

#### Projection

- We can also interpret the fit as the projection of the $n\times 1$ vector $\mathbf{Y}$ on the column space of the matrix $\mathbf{X}$.

- So each column in $\mathbf{X}$ is also an $n\times 1$ vector.

- For the toy example n=3 and p=2.
So the column space of X is a plane in the three dimensional space.

$$
\hat{\mathbf{Y}} = \mathbf{X} (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}
$$

1. Plane spanned by column space:
```r
arrows3D(0,0,0,x1[1],x1[2],x1[3],xlim=c(0,5),ylim=c(0,5),zlim=c(0,5),bty = "g",theta=th,col=2,xlab="row 1",ylab="row 2",zlab="row 3")
text3D(x1[1],x1[2],x1[3],labels="X1",col=2,add=TRUE)
arrows3D(0,0,0,x2[1],x2[2],x2[3],add=TRUE,col=2)
text3D(x2[1],x2[2],x2[3],labels="X2",col=2,add=TRUE)
```

2. Vector of Y:
```r
arrows3D(0,0,0,x1[1],x1[2],x1[3],xlim=c(0,5),ylim=c(0,5),zlim=c(0,5),bty = "g",theta=th,col=2,xlab="row 1",ylab="row 2",zlab="row 3")
text3D(x1[1],x1[2],x1[3],labels="X1",col=2,add=TRUE)
arrows3D(0,0,0,x2[1],x2[2],x2[3],add=TRUE,col=2)
text3D(x2[1],x2[2],x2[3],labels="X2",col=2,add=TRUE)
arrows3D(0,0,0,y[1],y[2],y[3],add=TRUE,col="darkblue")
text3D(y[1],y[2],y[3],labels="Y",col="darkblue",add=TRUE)
```

3. Projection of Y onto column space
```r
arrows3D(0,0,0,x1[1],x1[2],x1[3],xlim=c(0,5),ylim=c(0,5),zlim=c(0,5),bty = "g",theta=th,col=2,xlab="row 1",ylab="row 2",zlab="row 3")
text3D(x1[1],x1[2],x1[3],labels="X1",col=2,add=TRUE)
arrows3D(0,0,0,x2[1],x2[2],x2[3],add=TRUE,col=2)
text3D(x2[1],x2[2],x2[3],labels="X2",col=2,add=TRUE)
arrows3D(0,0,0,y[1],y[2],y[3],add=TRUE,col="darkblue")
text3D(y[1],y[2],y[3],labels="Y",col="darkblue",add=TRUE)
arrows3D(0,0,0,fit$fitted[1],fit$fitted[2],fit$fitted[3],add=TRUE,col="darkblue")
segments3D(y[1],y[2],y[3],fit$fitted[1],fit$fitted[2],fit$fitted[3],add=TRUE,lty=2,col="darkblue")
text3D(fit$fitted[1],fit$fitted[2],fit$fitted[3],labels="fit",col="darkblue",add=TRUE)

```

- Note, that it is also clear from the equation in the derivation of the LS that the residual is orthogonal on the column space:

$$
-2 \mathbf{X}^T(\mathbf{Y}-\mathbf{X}\boldsymbol{\beta}) = 0
$$

---

### Variance Estimator?

$$
\begin{array}{ccl}
\hat{\boldsymbol{\Sigma}}_{\hat{\mathbf{\beta}}}
&=&\text{var}\left[(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}\right]\\\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\text{var}\left[\mathbf{Y}\right]\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\\\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T(\mathbf{I}\sigma^2)\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}
\\\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{I}\quad\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\sigma^2\\\\
%\hat{\boldmath{\Sigma}}_{\hat{\mathbf{\beta}}}&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\var\left[\mathbf{Y}\right](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\sigma^2\\\\
&=&(\mathbf{X}^T\mathbf{X})^{-1}\sigma^2
\end{array}
$$

---

### Contrasts

Hypotheses often involve linear combinations of the model parameters!

e.g.

- $H_0: \log_2{FC}_{g3n1-g1n1}= \beta_{g3} + \hat\beta_{g3n1}=0$ $\rightarrow$ "grade3+grade3:node1 = 0"

- Let

$$
\boldsymbol{\beta} = \left[
\begin{array}{c}
\beta_{0}\\
\beta_{g3}\\
\beta_{n1}\\
\beta_{g3:n1}
\end{array}
\right]]
- we can write that contrast using a contrast matrix:
[
\mathbf{L}=\left[\begin{array}{c}0\\1\\0\\1\end{array}\right] \rightarrow \mathbf{L}^T\boldsymbol{beta}
$$

- Then the variance becomes:

$$
\text{var}_{\mathbf{L}^T\boldsymbol{\hat\beta}}= \mathbf{L}^T \boldsymbol{\Sigma}_{\boldsymbol{\hat\beta}}\mathbf{L}
$$

---

## Homework: Adopt the gene analysis on log scale in matrix form!

1. Study the solution of the exercise to understand the analysis in R

2. Calculate
- model parameters and contrasts of interest
- standard errors, standard errors on contrasts
- t-test statistics on the model parameters and contrasts of interest

3. Compare your results with the output of the lm(.) function

---

### Inspiration

Tip: details on the implementation can be found in the book of Faraway (chapter 2). https://people.bath.ac.uk/jjf23/book/

- Design matrix

```r
X <- model.matrix(~grade*node,data=gene)
```

- Transpose of a matrix: use function t(.)

```r
t(X)
```

- Matrix product %\*% operator

```r
t(X)%*%X
```

- Degrees of freedom of a model?

$$ df =  n-p$$

```r
summary(lm1)
dfRes <- (nrow(X)-ncol(X))
dfRes
```

- Variance estimator: MSE

$$
\hat \sigma^2 = \frac{\sum\limits_{i=1}^n\epsilon_i^2}{n-p}
$$

- Invert matrix: use function solve(.)

- Diagonal elements of a matrix: use function diag(.)

```r
t(X)%*%X
diag(t(X)%*%X)
```

---

[← General Linear Model](04-general-linear-model.md) · [Up: contents](index.md)
