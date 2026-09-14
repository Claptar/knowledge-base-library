---
title: 'Linear dimensionality reduction: PCA'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Linear dimensionality reduction: PCA

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We are able to recover quite some structure.
However, many cell populations remain obscure, and the plot is overcrowded.

```r
set.seed(1234)
sce <- runPCA(sce, ncomponents=30, subset_row=hvg)
plotPCA(sce, colour_by = "cluster")
```

### PCA without feature selection

```r
set.seed(1234)
sceNoFS <- runPCA(sce, ncomponents=30, subset_row=1:nrow(sce))
plotPCA(sceNoFS, colour_by = "cluster")
rm(sceNoFS)
```

---

[← The most basic DR](14-the-most-basic-dr.md) · [Up: contents](index.md) · [A generalization of PCA for exponential family distributions. →](16-a-generalization-of-pca-for-exponential-family-distributions.md)
