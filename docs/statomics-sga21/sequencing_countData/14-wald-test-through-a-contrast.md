---
title: Wald test through a contrast
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Wald test through a contrast

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

C <- matrix(0, nrow=1, ncol=length(coef(mSimple)))
colnames(C) <- names(coef(mSimple))
C[, "workingday"] <- 1
C
beta <- matrix(coef(mSimple), ncol=1)
Sigma <- vcov(mSimple)

W2 <- C %*% beta %*% solve(C %*% Sigma %*% t(C)) %*% t(beta) %*% t(C)
W2

---

[← Wald test manually](13-wald-test-manually.md) · [Up: contents](index.md) · [note this being equal to →](15-note-this-being-equal-to.md)
