---
title: identify the linearly independent contrasts
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# identify the linearly independent contrasts

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Ct <- t(C)
CtIndep <- Ct[,qr(Ct)$pivot[1:qr(Ct)$rank]]
CIndep <- t(CtIndep)

---

[← doesn't work because we have a singular matrix](19-doesn-t-work-because-we-have-a-singular-matrix.md) · [Up: contents](index.md) · [try again →](21-try-again.md)
