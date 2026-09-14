---
title: A generalization of PCA for exponential family distributions.
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# A generalization of PCA for exponential family distributions.

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
library(glmpca)
set.seed(211103)
poipca <- glmpca(assays(sce)$counts[hvg,],
                 L=2, fam="poi",
                 minibatch="stochastic")
reducedDim(sce, "PoiPCA") <- poipca$factors
plotReducedDim(sce,
               dimred="PoiPCA",
               colour_by = "cluster")
```

---

[← Linear dimensionality reduction: PCA](15-linear-dimensionality-reduction-pca.md) · [Up: contents](index.md) · [Non-linear dimensionality reduction: UMAP →](17-non-linear-dimensionality-reduction-umap.md)
