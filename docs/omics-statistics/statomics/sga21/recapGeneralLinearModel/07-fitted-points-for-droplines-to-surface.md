---
title: fitted points for droplines to surface
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd
source_file: sources/statomics-sga21/recapGeneralLinearModel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# fitted points for droplines to surface

**Source:** [`recapGeneralLinearModel.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

### Projection

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

## Variance Estimator?
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

## Contrasts

Hypotheses often involve linear combinations of the model parameters!

e.g.

- $H_0: \log_2{FC}_{g3n1-g1n1}= \beta_{g3} + \hat\beta_{g3n1}=0$ $\rightarrow$ "grade3+grade3:node1 = 0"

- Let $$
\boldsymbol{\beta} = \left[
\begin{array}{c}
\beta_{0}\\
\beta_{g3}\\
\beta_{n1}\\
\beta_{g3:n1}
\end{array}
\right]$$
- we can write that contrast using a contrast matrix:
$$
\mathbf{L}=\left[\begin{array}{c}0\\1\\0\\1\end{array}\right] \rightarrow \mathbf{L}^T\boldsymbol{beta} $$

- Then the variance becomes:
$$
\text{var}_{\mathbf{L}^T\boldsymbol{\hat\beta}}= \mathbf{L}^T \boldsymbol{\Sigma}_{\boldsymbol{\hat\beta}}\mathbf{L}
$$


---

---

[← predict values on regular xy grid](06-predict-values-on-regular-xy-grid.md) · [Up: contents](index.md) · [Homework: Adopt the gene analysis on log scale in matrix form! →](08-homework-adopt-the-gene-analysis-on-log-scale-in-matrix-form.md)
