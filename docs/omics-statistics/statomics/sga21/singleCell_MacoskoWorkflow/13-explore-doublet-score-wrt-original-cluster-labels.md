---
title: explore doublet score wrt original cluster labels
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# explore doublet score wrt original cluster labels

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

boxplot(log1p(sce$scDblFinder.score) ~ factor(colData(sce)$cluster, exclude=NULL))

tab <- table(sce$scDblFinder.class, sce$cluster,
      exclude=NULL)
tab
t(t(tab) / colSums(tab))

barplot(t(t(tab) / colSums(tab))[2,],
        xlab = "Cluster", ylab = "Fraction of doublets")

# remove doublets
sce <- sce[,!sce$scDblFinder.class == "doublet"]
```


# Normalization

For normalization, the size factors $s_i$ computed here are simply scaled library sizes:
$$ N_i = \sum_g Y_{gi} $$
$$ s_i = N_i / \bar{N}_i $$

```r
sce <- logNormCounts(sce)

# note we also returned log counts: see the additional logcounts assay.
sce

# you can extract size factors using
sf <- librarySizeFactors(sce)
mean(sf) # equal to 1 due to scaling.
plot(x= log(colSums(assays(sce)$counts)),
     y=sf)
```

# Feature selection

```r
library(scran)
dec <- modelGeneVar(sce)
fitRetina <- metadata(dec)
plot(fitRetina$mean, fitRetina$var,
     xlab="Mean of log-expression",
    ylab="Variance of log-expression")
curve(fitRetina$trend(x), col="dodgerblue", add=TRUE, lwd=2)

# get 10% highly variable genes
hvg <- getTopHVGs(dec, prop=0.1)
head(hvg)

# plot these
plot(fitRetina$mean, fitRetina$var,
     col = c("orange", "darkseagreen3")[(names(fitRetina$mean) %in% hvg)+1],
     xlab="Mean of log-expression",
    ylab="Variance of log-expression")
curve(fitRetina$trend(x), col="dodgerblue", add=TRUE, lwd=2)
legend("topleft",
       legend = c("Selected", "Not selected"),
       col = c("darkseagreen3", "orange"),
       pch = 16,
       bty='n')
```

# Dimensionality reduction

Note that, below, we color the cells using the known, true cell type label as defined in the metadata, to empirically evaluate the dimensionality reduction. In reality, we don't know this yet at this stage.

---

[← visualize these scores](12-visualize-these-scores.md) · [Up: contents](index.md) · [The most basic DR →](14-the-most-basic-dr.md)
