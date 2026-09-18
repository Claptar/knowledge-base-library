---
title: Inference in multiple linear models
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd
source_file: sources/gtpb-psls20/theory/08-MultipleRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`theory/08-MultipleRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Inference in multiple linear models

If data are representative than the least squares estimators for the intercept and slopes are unbiased.
$$E[\hat \beta_j]=\beta_j,\quad j=0,\ldots,p-1.$$

- Gain insight in the distribution of the parameter estimators so as to generalize the effect in the sample to the population.

- Additional assumptions are needed for inference.

1. *Linearity*

2. *Independence*

3. *Homoscedasticity* of *equal variance*
4. *Normality*: residuals $\epsilon_i$ are normally distributed.

Under these assumptions:
$$\epsilon_i \sim N(0,\sigma^2).$$
en
$$Y_i\sim N(\beta_0+\beta_1 X_{i1}+\ldots+\beta_{p-1} X_{ip-1},\sigma^2)$$

---

- Slopes are again more precise if the predictor values have a larger range.

- Conditional variance ($\sigma^2$) can again be estimated based on the *mean squared error* (MSE):

$$\hat\sigma^2=MSE=\frac{\sum\limits_{i=1}^n \left(y_i-\hat\beta_0-\hat\beta_1 X_{i1}-\ldots-\hat\beta_{p-1} X_{ip-1}\right)^2}{n-p}=\frac{\sum\limits_{i=1}^n e^2_i}{n-p}.$$

Again hypothesis tests and confidence intervals by
$$T_k=\frac{\hat{\beta}_k-\beta_k}{SE(\hat{\beta}_k)} \text{ met } k=0, \ldots, p-1.$$

If all assumptions are satisfied than the statistics $T_k$ t-distributed with $n-p$ degrees of freedom.

---

When normality thus not hold, but lineariteit, independence and homoscedasticity are valid we can again adopt the CLT that states that statistic $T_k$ is approximately normally distributed in large samples.

---

We can build confidence intervals on the slopes by:
$$[\hat\beta_j - t_{n-p,\alpha/2} \text{SE}_{\hat\beta_j},\hat\beta_j + t_{n-p,\alpha/2} \text{SE}_{\hat\beta_j}]$$.

```r
confint(lmVWS)
```

---

Formal hypothesis tests:
$$H_0: \beta_j=0$$
$$H_1: \beta_j\neq0$$

With test statistic
$$T=\frac{\hat{\beta}_j-0}{SE(\hat{\beta}_j)}$$
which follows a t-distribution with $n-p$ degrees of freedom under $H_0$

---

```r
summary(lmVWS)
```

---

## Assess the model assumptions

```r
plot(lmVWS)
```

---

## The non additive multiple linear model
### Interaction between two continuous variables

The previous model is additive because the contribution of the cancer volume on lpsa does not depend on the height of the prostate weight and the svi status.

The slope for lcavol does not depend on log prostate weight and svi.

$$
\beta_0 + \beta_v (x_{v}+\delta_v) + \beta_w x_{w} +\beta_s x_{s} - \beta_0 - \beta_v x_{v} - \beta_w x_{w} -\beta_s x_s = \beta_v \delta_v
$$

The svi status and the log-prostategewicht ($x_w$) do not influence the contribution of the log-tumor volume ($x_v$) to the average log-PSA and vice versa.

---

- It is however possible that the association of lpsa and lcavol depends on the prostate weight.
- The average difference in lpsa for patients that differ in one unit of the log-tumor volume can for instance can be higher for patients wiht a high tumor weight then for those with a low tumor weight.
- The effect of the tumor volume on the PSA depends on the prostate weight.

To model this **interactie** or **effect modification** we can add a product term of both variables to the model

$$
Y_i = \beta_0 + \beta_v x_{iv} + \beta_w x_{iw} +\beta_s x_{is} + \beta_{vw} x_{iv}x_{iw} +\epsilon_i
$$

This term quantifies the *interactie-effect* of predictors $x_v$ en $x_w$ on the mean outcome.

Terms $\beta_vx_{iv}$ and $\beta_wx_{iw}$ are referred to as *main effects* of predictors $x_v$ and $x_w$.

---

The difference in lpsa for patients that differ 1 unit in $X_v$ and have an equal log prostate weight and the same svi status now becomes:

$$
\begin{array}{l}
E(Y | X_v=x_v +1, X_w=x_w, X_s=x_s) - E(Y | X_v=x_v, X_w=x_w, X_s=x_s) \\
\quad = \beta_0 + \beta_v (x_{v}+1) + \beta_w x_w +\beta_s x_{s} + \beta_{vw} (x_{v}+1) x_w - \beta_0 - \beta_v x_{v} - \beta_w x_w -\beta_s x_{s} - \beta_{vw} (x_{v}) x_w \\
\quad = \beta_v +  \beta_{vw} x_w
 \end{array}
 $$

---

```r
lmVWS_IntVW <- lm(lpsa~lcavol + lweight + svi + lcavol:lweight ,prostate)
summary(lmVWS_IntVW)
```

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

# fitted points for droplines to surface
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

# fitted points for droplines to surface
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
z2.pred3D <- outer(x.pred, y.pred, function(x,y) {lmVWS$coef[1]+lmVWS$coef[4]+lmVWS$coef[2]*x+lmVWS$coef[3]*y})
surf3D(x.pred3D,y.pred3D,z2.pred3D,col="orange",facets=NA,add=TRUE)


scatter3D(x, y, z, pch = 16,col=c("darkblue","red")[as.double(prostate$svi)], cex = .75,
    theta = th, phi = ph, ticktype = "detailed",
    xlab = "lcavol", ylab = "lweight", zlab = "lpsa",
   colvar=FALSE,bty = "g",main="Model met lcavol:lweight interactie")

for (i in which(prostate$svi=="healthy"))
lines3D(x=rep(prostate$lcavol[i],2),y=rep(prostate$lweight[i],2),z=c(prostate$lpsa[i],lmVWS_IntVS_WS$fit[i]),col=c("darkblue","red")[as.double(prostate$svi)[i]],add=TRUE,lty=2)

z.pred3D <- outer(x.pred, y.pred, function(x,y) {lmVWS_IntVS_WS$coef[1]+lmVWS_IntVS_WS$coef[2]*x+lmVWS_IntVS_WS$coef[3]*y})
x.pred3D <- outer(x.pred,y.pred,function(x,y) x)
y.pred3D <- outer(x.pred,y.pred,function(x,y) y)
surf3D(x.pred3D,y.pred3D,z.pred3D,col="blue",facets=NA,add=TRUE)
z2.pred3D <- outer(x.pred, y.pred, function(x,y) {lmVWS_IntVS_WS$coef[1]+lmVWS_IntVS_WS$coef[4]+lmVWS_IntVS_WS$coef[2]*x+lmVWS_IntVS_WS$coef[3]*y+lmVWS_IntVS_WS$coef[5]*x+lmVWS_IntVS_WS$coef[6]*y})
surf3D(x.pred3D,y.pred3D,z2.pred3D,col="orange",facets=NA,add=TRUE)
```

---

---

[← Additive multiple linair model](02-additive-multiple-linair-model.md) · [Up: contents](index.md) · [ANOVA Tabel →](04-anova-tabel.md)
