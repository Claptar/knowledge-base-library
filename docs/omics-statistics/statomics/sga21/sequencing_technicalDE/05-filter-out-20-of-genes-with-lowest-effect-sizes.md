---
title: filter out ~20% of genes with lowest effect sizes
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# filter out ~20% of genes with lowest effect sizes

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

mean(filterStatEffectSize > 1)
hist(filterStatEffectSize, breaks=40)
abline(v=1, col="red")
keepEffectSize <- filterStatEffectSize > 1
## conditional distribution: very different!
plot(density(testStat$statistic[keepEffectSize], na.rm=TRUE),
     xlab = "Test statistic",
     main = "Conditional distribution")


## in same plot
plot(density(testStat$statistic, na.rm=TRUE),
     xlab = "Test statistic",
     col = "orange",
     main = "Test statistics before and after filtering on mean difference",
     lwd = 2)
lines(density(testStat$statistic[keepEffectSize], na.rm=TRUE),
     xlab = "Test statistic",
     main = "Conditional distribution",
     col = "steelblue",
     lwd = 2)
legend("topright", c("Unconditional", "Conditional"),
       col=c("orange", "steelblue"), lwd=2, bty='n')
```


## An independent test statistic

```r
filterStatGlobalMean <- rowMeans(simCounts)

---

[← All defaults](04-all-defaults.md) · [Up: contents](index.md) · [we remove a similar fraction of ~20% genes →](06-we-remove-a-similar-fraction-of-20-genes.md)
