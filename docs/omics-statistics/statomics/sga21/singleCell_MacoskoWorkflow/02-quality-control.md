---
title: Quality control
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Quality control

### Calculate QC variables

```r
library(scater)
is.mito <- grepl("^MT-", rownames(sce))
sum(is.mito) # 28 mitochondrial genes
df <- perCellQCMetrics(sce, subsets=list(Mito=is.mito))
## add the QC variables to sce object
colData(sce) <- cbind(colData(sce), df)
# the QC variables have now been added to the colData of our SCE object.
colData(sce)
```

### EDA

High-quality cells should have many features expressed, and a low contribution of mitochondrial genes. Here, we see that several cells have a very low number of expressed genes, and where most of the molecules are derived from mitochondrial genes. This indicates likely damaged cells, presumably because of loss of cytoplasmic RNA from perforated cells, so we'd want to remove these for the downstream analysis.

```r
# Number of genes vs library size
plotColData(sce, x = "sum", y="detected", colour_by="cluster")

# Mitochondrial genes
plotColData(sce, x = "detected", y="subsets_Mito_percent")
```

### QC using adaptive thresholds

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

### Identifying and removing empty droplets

Note that the removal of cells with low sequencing depth using the adaptive threshold procedure above is a way of removing empty droplets.
Other approaches are possible, e.g., removing cells by statistical testing using `emtpyDrops`.
This does require us to specify a lower bound on the total number of UMIs, below which all cells are considered to correspond to empty droplets.
This lower bound may not be trivial to derive, but the `barcodeRanks` function can be useful to identify an elbow/knee point.

```r
library(DropletUtils)
bcrank <- barcodeRanks(counts(sce))

# Only showing unique points for plotting speed.
uniq <- !duplicated(bcrank$rank)
plot(bcrank$rank[uniq], bcrank$total[uniq], log="xy",
    xlab="Rank", ylab="Total UMI count", cex.lab=1.2)

abline(h=metadata(bcrank)$inflection, col="darkgreen", lty=2)
abline(h=metadata(bcrank)$knee, col="dodgerblue", lty=2)
abline(h=350, col="orange", lty=2) # picked visually myself

legend("topright", legend=c("Inflection", "Knee", "Empirical knee point"),
        col=c("darkgreen", "dodgerblue", "orange"), lty=2, cex=1.2)

set.seed(100)
limit <- 350
all.out <- emptyDrops(counts(sce), lower=limit, test.ambient=TRUE)
# p-values for cells with total UMI count under the lower bound.
hist(all.out$PValue[all.out$Total <= limit & all.out$Total > 0],
    xlab="P-value", main="", col="grey80")

# but note that it would remove a very high number of cells
length(which(all.out$FDR <= 0.001))

# so we stick to the more lenient adaptive filtering strategy
# remove cells identified using adaptive thresholds
sce <- sce[, !colData(sce)$discardCells]
```

### Identifying and removing doublets

We will use [scDblFinder](https://bioconductor.org/packages/3.14/bioc/html/scDblFinder.html) to detect doublet cells.

```r
## perform doublet detection
library(scDblFinder)
set.seed(211103)
sampleID <- unlist(lapply(strsplit(colData(sce)$cell.id, split="_"), "[[", 1))
table(sampleID)
sce <- scDblFinder(sce, returnType="table",
                 samples = factor(sampleID))
table(sce$scDblFinder.class)


## visualize these scores
## explore doublet score wrt original cluster labels
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

## Normalization

For normalization, the size factors $s_i$ computed here are simply scaled library sizes:

$$
N_i = \sum_g Y_{gi} ]
[ s_i = N_i / \bar{N}_i
$$

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

## Feature selection

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

---

← Import data · [Up: contents](index.md) · [Dimensionality reduction →](03-dimensionality-reduction.md)
