---
title: Accessing data from a SingleCellExperiment object
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Accessing data from a SingleCellExperiment object

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Please see [Figure 4.1 in OSCA](http://bioconductor.org/books/release/OSCA/data-infrastructure.html) for an overview of a `SingleCellExperiment` object.

```r
# Data: assays
assays(sce)
assays(sce)$counts[1:5, 1:5]

# Feature metadata: rowData
rowData(sce) # empty for now

# Cell metadata: colData
colData(sce)

# Reduced dimensions: reducedDims
reducedDims(sce) # empty for now
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Creating a new SingleCellExperiment object →](03-creating-a-new-singlecellexperiment-object.md)
