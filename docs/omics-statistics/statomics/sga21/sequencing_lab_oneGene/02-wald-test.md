---
title: Wald test
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.Rmd
source_file: sources/statomics-sga21/sequencing_lab_oneGene.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Wald test

**Source:** [`sequencing_lab_oneGene.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Likelihood ratio test →](03-likelihood-ratio-test.md)
