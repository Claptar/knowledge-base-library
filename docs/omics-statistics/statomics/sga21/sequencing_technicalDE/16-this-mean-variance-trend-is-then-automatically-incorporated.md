---
title: this mean-variance trend is then automatically incorporated into the usual
  limma pipeline
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# this mean-variance trend is then automatically incorporated into the usual limma pipeline

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

fit <- lmFit(v, design)
fit <- eBayes(fit)
tt <- topTable(fit, coef=(ncol(design-1):ncol(design)), number=nrow(dge)) # test interaction effects
head(tt) #similar as in edgeR, we find no DE
```

### Testing contrasts using limma-voom

When working with limma-voom, we cannot immediately test a contrast using a contrast matrix just like we did in `edgeR`.
Instead, we will reparametrize our model according to the contrasts, such that each parameter corresponds to a specific contrast, using the `contrasts.fit` function.

```r

---

[← fit the mean-variance trend used to calculate weights](15-fit-the-mean-variance-trend-used-to-calculate-weights.md) · [Up: contents](index.md) · [contrast matrix we used before →](17-contrast-matrix-we-used-before.md)
