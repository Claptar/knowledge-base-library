---
title: we remove a similar fraction of ~20% genes
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# we remove a similar fraction of ~20% genes

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

mean(filterStatGlobalMean > 5)
keepGlobalMean <- filterStatGlobalMean > 5

## unconditional distribution
plot(density(testStat$statistic, na.rm=TRUE),
     xlab = "Test statistic",
     main = "Unconditional distribution")

## conditional distribution: the same.
plot(density(testStat$statistic[keepGlobalMean], na.rm=TRUE),
     xlab = "Test statistic",
     main = "Conditional distribution")


## in same plot
plot(density(testStat$statistic, na.rm=TRUE),
     xlab = "Test statistic",
     col = "orange",
     main = "Test statistics before and after filtering on global mean",
     lwd = 2)
lines(density(testStat$statistic[keepGlobalMean], na.rm=TRUE),
     xlab = "Test statistic",
     main = "Conditional distribution",
     col = "steelblue",
     lwd = 2)
legend("topright", c("Unconditional", "Conditional"),
       col=c("orange", "steelblue"), lwd=2, bty='n')
```

---

[← filter out ~20% of genes with lowest effect sizes](05-filter-out-20-of-genes-with-lowest-effect-sizes.md) · [Up: contents](index.md) · [Aliasing →](07-aliasing.md)
