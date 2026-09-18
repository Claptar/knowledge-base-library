---
title: Negative binomial model
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.Rmd
source_file: sources/statomics-sga21/sequencing_lab_oneGene.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_lab_oneGene.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Negative binomial model

```r
library(MASS)
mNB <- glm.nb(y ~ treatment*time + patient)
plot(mNB)
summary(mNB)
```

### Statistical inference

We will test seven different contrasts.

```r
L <- matrix(0, nrow = length(coef(mNB)), ncol = 7)
rownames(L) <- names(coef(mNB))
colnames(L) <- c("DPNvsCON24", "DPNvsCON48",
                 "OHTvsCON24", "OHTvsCON48",
                 "DPNvsCONInt", "OHTvsCONInt",
                 "OHTvsDPNInt")
# DPN vs control at 24h
L[2,"DPNvsCON24"] <- 1
# DPN vs control at 48h
L[c(2,8),"DPNvsCON48"] <- 1
# OHT vs control at 24h
L[3,"OHTvsCON24"] <- 1
# OHT vs control at 48h
L[c(3,9),"OHTvsCON48"] <- 1
# DPN control interaction
L[8,"DPNvsCONInt"] <- 1
# OHT control interaction
L[9,"OHTvsCONInt"] <- 1
# OHT DPN interaction
L[c(9,8),"OHTvsDPNInt"] <- c(1, -1)

L
```

#### Wald test

```r
beta <- matrix(coef(mNB), ncol = 1)
waldStats <- c()
for(ll in 1:ncol(L)){
  curL <- L[,ll,drop=FALSE]
  curWald <- t(curL) %*% beta %*% solve(t(curL) %*% vcov(mNB) %*% curL) %*% t(beta) %*% curL
  waldStats[ll] <- curWald
}

waldStats

pvalues <- 1-pchisq(waldStats, df=1)
pvalues
```

#### Likelihood ratio test

Implementing these contrasts using a likelihood ratio test is possible, but is not trivial.
It would require a reparameterization of our model using the contrasts of interest. In this reparameterization, one variable may correspond to one contrast. We may then compare a full to an alternative model, dropping this variable, using a likelihood ratio test.
While it is important to know that this is possible, we will not implement the reparameterization ourselves as it is considered outside the scope of this course.

## Residuals

### Deviance residuals

```r
## residual deviance
sum(2*(dnbinom(x=y, mu=y, size=mNB$theta, log=TRUE) - dnbinom(x=y, mu=fitted(mNB), size=mNB$theta, log=TRUE)))

## deviance residual
devResid <- sign(y-fitted(mNB)) * sqrt(2*(dnbinom(x=y, mu=y, size=mNB$theta, log=TRUE) -
                      dnbinom(x=y, mu=fitted(mNB), size=mNB$theta, log=TRUE)))

range(devResid - resid(mNB, type="deviance"))
plot(devResid, resid(mNB, type="deviance")) ; abline(0,1, col="red")

```

### Pearson residuals

```r
pearsResid <- (y - fitted(mNB)) / sqrt(fitted(mNB) + 1/mNB$theta * fitted(mNB)^2)
range(pearsResid - resid(mNB, type="pearson"))
plot(x=pearsResid, y=resid(mNB, type="pearson")) ; abline(0,1, col="red")
```

### Goodness-of-fit

```r
X2 <- sum(pearsResid^2)
1-pchisq(X2, df=length(y) - length(coef(mNB)))
```

## Re-analysis upon basic normalization

A very simple normalization would use an offset to account for sequencing depth.
Verify if our hypothesis test results remain upon using this basic normalization.

```r
seqDepth <- colSums(assays(se)$counts)
```

### Statistical inference

## Negative binomial model, corrected for sequencing depth

```r
library(MASS)
mNBOffset <- glm.nb(y ~ treatment*time + patient +
                offset(log(seqDepth)))
plot(mNBOffset)
summary(mNBOffset)
```

### Wald tests

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

← Introduction · Up: contents
