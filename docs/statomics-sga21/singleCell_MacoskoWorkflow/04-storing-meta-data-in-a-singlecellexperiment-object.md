---
title: Storing (meta)data in a SingleCellExperiment object
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Storing (meta)data in a SingleCellExperiment object

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
fakeGeneNames <- paste0("gene", 1:nrow(sce))
rowData(sce)$fakeName <- fakeGeneNames
head(rowData(sce))
# Remove again by setting to NULL
rowData(sce)$fakeName <- NULL

assays(sce)$logCounts <- log1p(assays(sce)$counts)
assays(sce)
assays(sce)$logCounts[1:5, 1:5]
assays(sce)$logCounts <- NULL
```

# Filtering non-informative genes

```r
keep <- rowSums(assays(sce)$counts > 0) > 10
table(keep)

sce <- sce[keep,]
```


# Quality control

---

[← Creating a new SingleCellExperiment object](03-creating-a-new-singlecellexperiment-object.md) · [Up: contents](index.md) · [Calculate QC variables →](05-calculate-qc-variables.md)
