---
title: EDA
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# EDA

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

High-quality cells should have many features expressed, and a low contribution of mitochondrial genes. Here, we see that several cells have a very low number of expressed genes, and where most of the molecules are derived from mitochondrial genes. This indicates likely damaged cells, presumably because of loss of cytoplasmic RNA from perforated cells, so we'd want to remove these for the downstream analysis.

```r
# Number of genes vs library size
plotColData(sce, x = "sum", y="detected", colour_by="cluster")

# Mitochondrial genes
plotColData(sce, x = "detected", y="subsets_Mito_percent")
```

---

[← add the QC variables to sce object](06-add-the-qc-variables-to-sce-object.md) · [Up: contents](index.md) · [QC using adaptive thresholds →](08-qc-using-adaptive-thresholds.md)
