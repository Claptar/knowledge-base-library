---
title: manual LRT
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# manual LRT

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

llFull <- logLik(mFull)
llReduced <- logLik(mReduced)

lrt <- as.numeric(2 * (llFull - llReduced))
lrt
pval <- 1 - pchisq(lrt, df=1)
pval

---

[← finally, we can also read the Wald test result from the summary of the model](16-finally-we-can-also-read-the-wald-test-result-from-the-summa.md) · [Up: contents](index.md) · [using anova function →](18-using-anova-function.md)
