---
title: OHT DPN interaction
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# OHT DPN interaction

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

L[c(9,8),"OHTvsDPNInt"] <- c(1, -1)
L

fit <- lmFit(v, design)
fit2 <- contrasts.fit(fit, L)
fit2 <- eBayes(fit2)
head(fit2$coefficients) # one coefficient is one contrast

---

[← OHT control interaction](23-oht-control-interaction.md) · [Up: contents](index.md) · [loop over all contrasts of interest →](25-loop-over-all-contrasts-of-interest.md)
