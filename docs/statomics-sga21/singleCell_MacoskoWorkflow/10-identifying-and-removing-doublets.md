---
title: Identifying and removing doublets
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Identifying and removing doublets

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We will use [scDblFinder](https://bioconductor.org/packages/3.14/bioc/html/scDblFinder.html) to detect doublet cells.


```r

---

[← Identifying and removing empty droplets](09-identifying-and-removing-empty-droplets.md) · [Up: contents](index.md) · [perform doublet detection →](11-perform-doublet-detection.md)
