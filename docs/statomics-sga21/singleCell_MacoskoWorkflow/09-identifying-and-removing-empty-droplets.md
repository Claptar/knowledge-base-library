---
title: Identifying and removing empty droplets
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Identifying and removing empty droplets

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[← QC using adaptive thresholds](08-qc-using-adaptive-thresholds.md) · [Up: contents](index.md) · [Identifying and removing doublets →](10-identifying-and-removing-doublets.md)
