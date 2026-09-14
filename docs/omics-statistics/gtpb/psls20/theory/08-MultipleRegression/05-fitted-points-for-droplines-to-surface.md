---
title: fitted points for droplines to surface
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd
source_file: sources/gtpb-psls20/theory/08-MultipleRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# fitted points for droplines to surface

**Source:** [`theory/08-MultipleRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

th=-25
ph=5
scatter3D(x, y, z, pch = 16,col=c("darkblue","red")[as.double(prostate$svi)], cex = .75,
    theta = th, phi = ph, ticktype = "detailed",
    xlab = "lcavol", ylab = "lweight", zlab = "lpsa",
   colvar=FALSE,bty = "g",main="Additive model")

for (i in which(prostate$svi=="healthy"))
lines3D(x=rep(prostate$lcavol[i],2),y=rep(prostate$lweight[i],2),z=c(prostate$lpsa[i],lmVWS$fit[i]),col=c("darkblue","red")[as.double(prostate$svi)[i]],add=TRUE,lty=2)

z.pred3D <- outer(x.pred, y.pred, function(x,y) {lmVWS$coef[1]+lmVWS$coef[2]*x+lmVWS$coef[3]*y})
x.pred3D <- outer(x.pred,y.pred,function(x,y) x)
y.pred3D <- outer(x.pred,y.pred,function(x,y) y)
surf3D(x.pred3D,y.pred3D,z.pred3D,col="blue",facets=NA,add=TRUE)


scatter3D(x, y, z, pch = 16,col=c("darkblue","red")[as.double(prostate$svi)], cex = .75,
    theta = th, phi = ph, ticktype = "detailed",
    xlab = "lcavol", ylab = "lweight", zlab = "lpsa",
   colvar=FALSE,bty = "g",main="Model met lcavol:lweight interactie")

for (i in which(prostate$svi=="healthy"))
lines3D(x=rep(prostate$lcavol[i],2),y=rep(prostate$lweight[i],2),z=c(prostate$lpsa[i],lmVWS_IntVW$fit[i]),col=c("darkblue","red")[as.double(prostate$svi)[i]],add=TRUE,lty=2)

z.pred3D <- outer(x.pred, y.pred, function(x,y) {lmVWS_IntVW$coef[1]+lmVWS_IntVW$coef[2]*x+lmVWS_IntVW$coef[3]*y+lmVWS_IntVW$coef[5]*x*y})
x.pred3D <- outer(x.pred,y.pred,function(x,y) x)
y.pred3D <- outer(x.pred,y.pred,function(x,y) y)
surf3D(x.pred3D,y.pred3D,z.pred3D,col="blue",facets=NA,add=TRUE)
```

---

- Note that the interaction effect that is observed is not statistically significant (p=`r round(summary(lmVWS_IntVW)$coef[5,4],2)`).
- The main effects that are involved in the interaction cannot be interpreted separately from one another.
- We will therefore remove non-significant interaction terms from the model.
- Upon removal of non-significant interaction terms the main effects can be interpreted.

---

## Interaction between a continuous variable and a factor variable

Interaction between lcavol $\leftrightarrow$ svi and lweight $\leftrightarrow$ svi.

The model becomes

$$Y=\beta_0+\beta_vX_v+\beta_wX_w+\beta_sX_s+\beta_{vs}X_vX_s + \beta_{ws}X_wX_s +\epsilon$$

---

```r
lmVWS_IntVS_WS <- lm(lpsa ~ lcavol + lweight + svi + svi:lcavol + svi:lweight,data=prostate)
summary(lmVWS_IntVS_WS)
```

---

Because $X_S$ is a dummy variabele we obtain to distinct regression planes:

1. Model for $X_s=0$: $$Y=\beta_0+\beta_vX_v+\beta_wX_w + \epsilon$$ where the main effects are the slope for lcavol and lweight
2. and model for $X_s=1$:
   $$\begin{array}{lcl}
   Y&=&\beta_0+\beta_vX_v+\beta_s+\beta_wX_w+\beta_{vs}X_v + \beta_{ws}X_w +\epsilon\\
  &=& (\beta_0+\beta_s)+(\beta_v+\beta_{vs})X_v+(\beta_w+\beta_{ws})X_w+\epsilon
  \end{array}$$
with intercept $\beta_0+\beta_s$ and slopes $\beta_v+\beta_{vs}$ and $\beta_w+\beta_{ws}$

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

[← Inference in multiple linear models](04-inference-in-multiple-linear-models.md) · [Up: contents](index.md) · [fitted points for droplines to surface →](06-fitted-points-for-droplines-to-surface.md)
