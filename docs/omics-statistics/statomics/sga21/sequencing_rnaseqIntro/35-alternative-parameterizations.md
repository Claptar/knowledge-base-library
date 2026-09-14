---
title: Alternative parameterizations
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Alternative parameterizations

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

While our design matrix here was parameterized as `~ treatment*time + patient` alternative, equivalent parameterizations are also possible.
Below, we demonstrate another parameterization that could work, too, and can be more intuitive. In this parameterization, we estimate a mean for each experimental condition, without an intercept, which can be convenient to think about how to set up contrasts.

```r
treatTime <- as.factor(paste0(treatment, time))
table(treatTime)

design2 <- model.matrix(~ 0 + treatTime + patient)

dge2 <- calcNormFactors(se)
dge2 <- estimateDisp(dge2, design2)
plotBCV(dge2)
fit2 <- glmFit(dge2, design2)
head(fit2$coefficients)

## for example: the estimate for the DPN24h vs control 24h is still the same,
## but requires a different combination of parameters
plot(fit$coefficients[,"treatmentDPN"],
     fit2$coefficients[,"treatTimeDPN24h"] - fit2$coefficients[,"treatTimeControl24h"],
     xlab="Intercept model estimate", ylab="No intercept model estimate")

---

[← order according to absolute fold-change](34-order-according-to-absolute-fold-change.md) · [Up: contents](index.md) · [Let's implement the DPNvsCON48 contrast →](36-let-s-implement-the-dpnvscon48-contrast.md)
