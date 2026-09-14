---
title: QC using adaptive thresholds
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# QC using adaptive thresholds

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Below, we remove cells that are outlying with respect to

 1. A low sequencing depth (number of UMIs);
 2. A low number of genes detected;
 3. A high percentage of reads from mitochondrial genes.

We remove a total of $3423$ cells, most of which because of an outlyingly high percentage of reads from mitochondrial genes.

```r
lowLib <- isOutlier(df$sum, type="lower", log=TRUE)
lowFeatures <- isOutlier(df$detected, type="lower", log=TRUE)
highMito <- isOutlier(df$subsets_Mito_percent, type="higher")

table(lowLib)
table(lowFeatures)
table(highMito)

discardCells <- (lowLib | lowFeatures | highMito)
table(discardCells)
colData(sce)$discardCells <- discardCells

# visualize cells to be removed
plotColData(sce, x = "detected", y="subsets_Mito_percent", colour_by = "discardCells")

```

---

[← EDA](07-eda.md) · [Up: contents](index.md) · [Identifying and removing empty droplets →](09-identifying-and-removing-empty-droplets.md)
