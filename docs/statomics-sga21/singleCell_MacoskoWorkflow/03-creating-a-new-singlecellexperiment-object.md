---
title: Creating a new SingleCellExperiment object
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Creating a new SingleCellExperiment object

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
sceNew <- SingleCellExperiment(assays = list(counts = assays(sce)$counts))
sceNew

rm(sceNew)
```

---

[← Accessing data from a SingleCellExperiment object](02-accessing-data-from-a-singlecellexperiment-object.md) · [Up: contents](index.md) · [Storing (meta)data in a SingleCellExperiment object →](04-storing-meta-data-in-a-singlecellexperiment-object.md)
