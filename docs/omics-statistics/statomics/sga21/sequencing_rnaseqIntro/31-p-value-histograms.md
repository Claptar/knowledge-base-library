---
title: p-value histograms
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# p-value histograms

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

pvalList <- lapply(lrtList, function(x) x$table$PValue)
pvalMat <- do.call(cbind,  pvalList)
colnames(pvalMat) <- colnames(L)
par(mfrow=c(3,3))
sapply(1:ncol(pvalMat), function(ii) hist(pvalMat[,ii],
                                          main = colnames(pvalMat)[ii],
                                          xlab = "p-value"))
```

### Multiple testing

```r

---

[← OHT DPN interaction](30-oht-dpn-interaction.md) · [Up: contents](index.md) · [number of DE genes →](32-number-of-de-genes.md)
