---
title: library size distribution
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# library size distribution

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

hist(colSums(assays(se)$counts)/1e6, breaks=10)
boxplot(colSums(assays(se)$counts)/1e6 ~ treatment)
boxplot(colSums(assays(se)$counts)/1e6 ~ time)
boxplot(colSums(assays(se)$counts)/1e6 ~ patient)
boxplot(colSums(assays(se)$counts)/1e6 ~ interaction(treatment, time))

---

[← Create new SummarizedExperiment](11-create-new-summarizedexperiment.md) · [Up: contents](index.md) · [MDS plot →](13-mds-plot.md)
