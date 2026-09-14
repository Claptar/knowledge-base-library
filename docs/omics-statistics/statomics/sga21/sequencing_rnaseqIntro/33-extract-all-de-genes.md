---
title: extract all DE genes
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# extract all DE genes

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

deGenes <- rownames(lrtList[[2]]$table)[p.adjust(lrtList[[2]]$table$PValue, "fdr") <= 0.05]
deGenes

---

[← number of DE genes](32-number-of-de-genes.md) · [Up: contents](index.md) · [order according to absolute fold-change →](34-order-according-to-absolute-fold-change.md)
