---
title: 'Non-linear dimensionality reduction: UMAP'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Non-linear dimensionality reduction: UMAP

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
sce <- runUMAP(sce, dimred = 'PCA', external_neighbors=TRUE)
plotUMAP(sce,
         colour_by = "cluster")
```

# Clustering

```r
# Build a shared nearest-neighbor graph from PCA space
g <- buildSNNGraph(sce, use.dimred = 'PCA')
# Louvain clustering on the SNN graph, and add to sce
colData(sce)$label <- factor(igraph::cluster_louvain(g)$membership)

# Visualization.
plotUMAP(sce, colour_by="label")
```

---

[← A generalization of PCA for exponential family distributions.](16-a-generalization-of-pca-for-exponential-family-distributions.md) · [Up: contents](index.md)
