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

th=20
ph=5
scatter3D(x, y, z, pch = 16,col=c("darkblue","red")[as.double(prostate$svi)], cex = .75,
    theta = th, phi = ph, ticktype = "detailed",
    xlab = "lcavol", ylab = "lweight", zlab = "lpsa",
   colvar=FALSE,bty = "g")

for (i in 1:nrow(prostate))
lines3D(x=rep(prostate$lcavol[i],2),y=rep(prostate$lweight[i],2),z=c(prostate$lpsa[i],lmVWS$fit[i]),col=c("darkblue","red")[as.double(prostate$svi)[i]],add=TRUE,lty=2)

z.pred3D <- outer(x.pred, y.pred, function(x,y) {lmVWS$coef[1]+lmVWS$coef[2]*x+lmVWS$coef[3]*y})
x.pred3D <- outer(x.pred,y.pred,function(x,y) x)
y.pred3D <- outer(x.pred,y.pred,function(x,y) y)
surf3D(x.pred3D,y.pred3D,z.pred3D,col="blue",facets=NA,add=TRUE)
z2.pred3D <- outer(x.pred, y.pred, function(x,y) {lmVWS$coef[1]+lmVWS$coef[4]+lmVWS$coef[2]*x+lmVWS$coef[3]*y})
surf3D(x.pred3D,y.pred3D,z2.pred3D,col="red",facets=NA,add=TRUE)
```

---

---

[← Additive multiple linair model](02-additive-multiple-linair-model.md) · [Up: contents](index.md) · [Inference in multiple linear models →](04-inference-in-multiple-linear-models.md)
