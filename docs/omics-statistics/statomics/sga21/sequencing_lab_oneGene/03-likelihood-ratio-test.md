---
title: Likelihood ratio test
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.Rmd
source_file: sources/statomics-sga21/sequencing_lab_oneGene.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Likelihood ratio test

**Source:** [`sequencing_lab_oneGene.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Implementing these contrasts using a likelihood ratio test is possible, but is not trivial.
It would require a reparameterization of our model using the contrasts of interest. In this reparameterization, one variable may correspond to one contrast. We may then compare a full to an alternative model, dropping this variable, using a likelihood ratio test.
While it is important to know that this is possible, we will not implement the reparameterization ourselves as it is considered outside the scope of this course.

# Residuals

## Deviance residuals

```r
## residual deviance
sum(2*(dnbinom(x=y, mu=y, size=mNB$theta, log=TRUE) - dnbinom(x=y, mu=fitted(mNB), size=mNB$theta, log=TRUE)))

## deviance residual
devResid <- sign(y-fitted(mNB)) * sqrt(2*(dnbinom(x=y, mu=y, size=mNB$theta, log=TRUE) -
                      dnbinom(x=y, mu=fitted(mNB), size=mNB$theta, log=TRUE)))

range(devResid - resid(mNB, type="deviance"))
plot(devResid, resid(mNB, type="deviance")) ; abline(0,1, col="red")

```

## Pearson residuals

```r
pearsResid <- (y - fitted(mNB)) / sqrt(fitted(mNB) + 1/mNB$theta * fitted(mNB)^2)
range(pearsResid - resid(mNB, type="pearson"))
plot(x=pearsResid, y=resid(mNB, type="pearson")) ; abline(0,1, col="red")
```


## Goodness-of-fit

```r
X2 <- sum(pearsResid^2)
1-pchisq(X2, df=length(y) - length(coef(mNB)))
```

# Re-analysis upon basic normalization

A very simple normalization would use an offset to account for sequencing depth.
Verify if our hypothesis test results remain upon using this basic normalization.

```r
seqDepth <- colSums(assays(se)$counts)
```

## Statistical inference

# Negative binomial model, corrected for sequencing depth

```r
library(MASS)
mNBOffset <- glm.nb(y ~ treatment*time + patient +
                offset(log(seqDepth)))
plot(mNBOffset)
summary(mNBOffset)
```

## Wald tests

```r
betaOffset <- matrix(coef(mNBOffset), ncol = 1)
waldStatsOffset <- c()
for(ll in 1:ncol(L)){
  curL <- L[,ll,drop=FALSE]
  curWald <- t(curL) %*% betaOffset %*% solve(t(curL) %*% vcov(mNBOffset) %*% curL) %*% t(betaOffset) %*% curL
  waldStatsOffset[ll] <- curWald
}

waldStatsOffset

pvaluesOffset <- 1-pchisq(waldStatsOffset, df=1)
pvaluesOffset
```

---

[← Wald test](02-wald-test.md) · [Up: contents](index.md)
