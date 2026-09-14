---
title: number of DE genes
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# number of DE genes

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

padjMat <- apply(pvalMat, 2, p.adjust, method="fdr")
colSums(padjMat <= 0.05 )
```

We are finding low numbers of DE genes between treatments at a 5\% FDR level. This was already reflected in the the MDS plots.

### Visualization

Let's visualize some results for the DPN vs control at 48h contrast.

```r
library(scales) # for scales::alpha()
deGenes <- p.adjust(lrtList[[2]]$table$PValue, "fdr") <= 0.05

## volcano plot
plot(x = lrtList[[2]]$table$logFC,
     y = -log10(lrtList[[2]]$table$PValue),
     xlab = "log Fold-change",
     ylab = "-log10 P-value",
     pch = 16, col = alpha(deGenes+1, .4),
     cex=2/3, bty='l')
legend("topright", c("DE", "not DE"),
       col = 2:1, pch=16, bty='n')

## MD-plot
plot(x = lrtList[[2]]$table$logCPM,
     y = lrtList[[2]]$table$logFC,
     xlab = "Average log CPM",
     ylab = "Log fold-change",
     pch = 16, col = alpha(deGenes+1, .4),
     cex=2/3, bty='l')
legend("topright", c("DE", "not DE"),
       col = 2:1, pch=16, bty='n')
abline(h=0, col="orange", lwd=2, lty=2)

```

 ---

```r

---

[← p-value histograms](31-p-value-histograms.md) · [Up: contents](index.md) · [extract all DE genes →](33-extract-all-de-genes.md)
