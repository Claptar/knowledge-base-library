---
title: Calculate QC variables
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Calculate QC variables

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
library(scater)
is.mito <- grepl("^MT-", rownames(sce))
sum(is.mito) # 28 mitochondrial genes
df <- perCellQCMetrics(sce, subsets=list(Mito=is.mito))

---

[← Storing (meta)data in a SingleCellExperiment object](04-storing-meta-data-in-a-singlecellexperiment-object.md) · [Up: contents](index.md) · [add the QC variables to sce object →](06-add-the-qc-variables-to-sce-object.md)
