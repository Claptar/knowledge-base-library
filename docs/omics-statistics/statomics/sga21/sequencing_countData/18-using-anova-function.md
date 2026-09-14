---
title: using anova function
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# using anova function

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

anova(mReduced, mFull, test = "Chisq") # note test statistic is identical
```

### Linearly dependent contrasts

Below, we show how one may be able to derive independent contrasts from their contrast matrix for statistical inference.
We also show that attempting to use linearly dependent contrasts results in an issue, since the variance-covariance matrix of our contrasts will be singular and therefore non-invertible.

```r
C <- matrix(0, nrow=3, ncol=length(coef(mSimple)))
colnames(C) <- names(coef(mSimple))
C[1, "(Intercept)"] <- 1
C[2, "workingday"] <- 1
C[3,c("(Intercept)", "workingday")] <- c(1,1)
C

---

[← manual LRT](17-manual-lrt.md) · [Up: contents](index.md) · [doesn't work because we have a singular matrix →](19-doesn-t-work-because-we-have-a-singular-matrix.md)
