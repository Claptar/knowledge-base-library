---
title: doesn't work because we have a singular matrix
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# doesn't work because we have a singular matrix

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

W2 <- try(t(C %*% beta) %*% solve(C %*% Sigma %*% t(C)) %*% C %*% beta)
W2 # errrors

---

[← using anova function](18-using-anova-function.md) · [Up: contents](index.md) · [identify the linearly independent contrasts →](20-identify-the-linearly-independent-contrasts.md)
