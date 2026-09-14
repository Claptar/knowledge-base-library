---
title: Single-cell RNA-sequencing intro
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd
source_file: sources/statomics-sga21/singleCell_intro1.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Single-cell RNA-sequencing intro

**Source:** [`singleCell_intro1.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
if(!"BiocManager" %in% installed.packages()[,1]){
  install.packages("BiocManager")
}
if(!"scRNAseq" %in% installed.packages()[,1]){
  BiocManager::install("scRNAseq")
}
```


```r
suppressPackageStartupMessages(library(scRNAseq))
sce <- MacoskoRetinaData()
sce
class(sce)
counts(sce)[1:5,1:5]
head(colData(sce))

# filter cells
sce <- sce[,!is.na(colData(sce)$cluster)]
sce
```


 - Explore this dataset. What do you think is different to these data as compared to a bulk RNA-seq dataset?
 - Try visualizing the structure of this dataset using tools we have worked with before. For example, make a PCA and MDS plot. You can color the cells according to the cluster labels in the `colData`.
 - Try visualizing the structure of this dataset using any tool you want.


After trying:

 Are you able to recapitulate the structure (e.g., cell type clusters)? What are the issues you are encountering, and **why** do you think these are happening?

---

[Up: contents](index.md)
