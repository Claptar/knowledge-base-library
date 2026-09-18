---
title: Independent filtering
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Independent filtering

```r
# A function for captioning and referencing images
fig <- local({
    i <- 0
    ref <- list()
    list(
        cap=function(refName, text) {
            i <<- i + 1
            ref[[refName]] <<- i
            paste("Figure ", i, ": ", text, sep="")
        },
        ref=function(refName) {
            ref[[refName]]
        })
})
```

```r
suppressPackageStartupMessages({
  library(knitr)
  library(rmarkdown)
  library(ggplot2)
})
```

Independent filtering, where genes/transcripts/proteins are filtered out prior to statistical analysis, is a common practice in 'omics experiments. Typically, lowly expressed features are filtered out, and one can argue that these features' expression is too low to be deemed biologically relevant. In addition, low-count features are also associated with a low statistical power for differential expression (remember relative uncertainty of counts, and `edgeR`'s BCV plot), and will increase the number of tests performed, and therefore lead to a more severe multiple testing correction.

```r
# All defaults
include_graphics("./images_sequencing/independentFiltering.png")
```

 ---

Independent filtering has been formalized by [Bourgon *et al.* (2010)](https://www.pnas.org/content/107/21/9546), and the concept can be summarized as follows.

 - For each feature we calculate two statistics, $S_F$ and $S_T$, respectively used for two stages: filtering and testing (e.g., differential expression).
 - In order for a feature to be deemed significant, both of its statistics must be greater than some cut-off.
 - We want to control the type I error rate of the second stage (testing). But note that **the second stage is conditional on the first stage**, as we only test features passing the filter, and basically ignore the fact that filtering was performed. Indeed, one criticism is that computing and correcting the $p$-values as if filtering had not been performed may lead to overoptimistic adjusted $p$-values.
 - [Bourgon *et al.* (2010)](https://www.pnas.org/content/107/21/9546) show that filtering is only appropriate (i.e., does not inflate type I error rate) if the conditional null distribution of test statistics for features passing the filter is the same as the unconditional null distribution. Therefore, **filtering is appropriate if the statistic used for filtering is independent of the statistic used for testing under the null hypothesis**. A good filtering statistic, however, is also informative under the alternative hypothesis. Indeed, a filtering statistic that is independent of the test statistic under both the null- and alternative hypothesis will amount to a random filter, hence deteriorate the quality of the analysis.

```r
# All defaults
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

# filter out ~20% of genes with lowest effect sizes
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
# we remove a similar fraction of ~20% genes
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

[Up: contents](index.md) · [Aliasing →](02-aliasing.md)
