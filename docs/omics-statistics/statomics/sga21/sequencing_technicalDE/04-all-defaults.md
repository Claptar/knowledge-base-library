---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/independentFiltering2.png")
```
  ---

Let's try a couple of examples to get some intuition using simulated data.

```r
suppressPackageStartupMessages(library(DESeq2))
set.seed(24)
dds <- DESeq2::makeExampleDESeqDataSet()
simCounts <- counts(dds)
group <- dds$condition
```

## A dependent test statistic

```r
## filter based on difference in means
filterStatEffectSize <- abs(rowMeans(simCounts[,group == "A"]) - rowMeans(simCounts[,group == "B"]))
## calculate t-test results for each gene
testStat <- genefilter::rowttests(simCounts, group)

## unconditional distribution of test statistics prior to filtering
plot(density(testStat$statistic, na.rm=TRUE),
     xlab = "Test statistic",
     main = "Unconditional distribution")

---

[← All defaults](03-all-defaults.md) · [Up: contents](index.md) · [filter out ~20% of genes with lowest effect sizes →](05-filter-out-20-of-genes-with-lowest-effect-sizes.md)
