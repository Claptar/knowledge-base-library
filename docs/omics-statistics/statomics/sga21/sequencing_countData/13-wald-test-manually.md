---
title: Wald test manually
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Wald test manually

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

W <- summSimple$coefficients["workingday", "Estimate"] / summSimple$coefficients["workingday", "Std. Error"]
pval <- 2*(1 - pnorm(W))
W
pval

---

[← calculate estimated average number of bikers](12-calculate-estimated-average-number-of-bikers.md) · [Up: contents](index.md) · [Wald test through a contrast →](14-wald-test-through-a-contrast.md)
