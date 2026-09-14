---
title: perform doublet detection
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# perform doublet detection

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

library(scDblFinder)
set.seed(211103)
sampleID <- unlist(lapply(strsplit(colData(sce)$cell.id, split="_"), "[[", 1))
table(sampleID)
sce <- scDblFinder(sce, returnType="table",
                 samples = factor(sampleID))
table(sce$scDblFinder.class)

---

[← Identifying and removing doublets](10-identifying-and-removing-doublets.md) · [Up: contents](index.md) · [visualize these scores →](12-visualize-these-scores.md)
