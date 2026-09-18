---
title: Dimensionality reduction
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Dimensionality reduction

Note that, below, we color the cells using the known, true cell type label as defined in the metadata, to empirically evaluate the dimensionality reduction. In reality, we don't know this yet at this stage.

### The most basic DR

Just by looking at the top two genes based on our feature selection criterion, we can already see some separation according to the cell type!

```r
colData(sce)$cluster <- as.factor(colData(sce)$cluster)
cl <- colData(sce)$cluster

par(bty='l')
plot(x = assays(sce)$counts[hvg[1],],
     y = assays(sce)$counts[hvg[2],],
     col = as.numeric(cl),
     pch = 16, cex = 1/3,
     xlab = "Most informative gene",
     ylab = "Second most informative gene",
     main = "Cells colored acc to cell type")
```

### Linear dimensionality reduction: PCA

We are able to recover quite some structure.
However, many cell populations remain obscure, and the plot is overcrowded.

```r
set.seed(1234)
sce <- runPCA(sce, ncomponents=30, subset_row=hvg)
plotPCA(sce, colour_by = "cluster")
```

#### PCA without feature selection

```r
set.seed(1234)
sceNoFS <- runPCA(sce, ncomponents=30, subset_row=1:nrow(sce))
plotPCA(sceNoFS, colour_by = "cluster")
rm(sceNoFS)
```

### A generalization of PCA for exponential family distributions.

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

### Non-linear dimensionality reduction: UMAP

```r
sce <- runUMAP(sce, dimred = 'PCA', external_neighbors=TRUE)
plotUMAP(sce,
         colour_by = "cluster")
```

## Clustering

```r
# Build a shared nearest-neighbor graph from PCA space
g <- buildSNNGraph(sce, use.dimred = 'PCA')
# Louvain clustering on the SNN graph, and add to sce
colData(sce)$label <- factor(igraph::cluster_louvain(g)$membership)

# Visualization.
plotUMAP(sce, colour_by="label")
```

---

[← Quality control](02-quality-control.md) · [Up: contents](index.md)
