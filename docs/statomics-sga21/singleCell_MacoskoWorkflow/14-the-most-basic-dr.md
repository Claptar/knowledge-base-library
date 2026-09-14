---
title: The most basic DR
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The most basic DR

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[← explore doublet score wrt original cluster labels](13-explore-doublet-score-wrt-original-cluster-labels.md) · [Up: contents](index.md) · [Linear dimensionality reduction: PCA →](15-linear-dimensionality-reduction-pca.md)
