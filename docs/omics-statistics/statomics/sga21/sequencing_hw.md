---
title: 'Sequencing: Bulk RNA-seq homework'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_hw.Rmd
source_file: sources/statomics-sga21/sequencing_hw.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_hw.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_hw.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Sequencing: Bulk RNA-seq homework

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
if(!"BiocManager" %in% installed.packages()[,1]){
  install.packages("BiocManager")
}
if(!"limma" %in% installed.packages()[,1]){
  BiocManager::install("limma")
}
if(!"edgeR" %in% installed.packages()[,1]){
  BiocManager::install("edgeR")
}
```

## Default `edgeR` analysis

Analyze the data using `edgeR`, by using the code in the RNA-seq analysis intro lecture.
**In all analyses, focus on the contrast comparing DPN treatment to control at 48h.**

## Impact of blocking

Assess the difference in number of DE genes when not blocking on patient, i.e., removing the `patient` effect of the model.
Compare the p-value distributions between these two models (i.e., with and without blocking).

## Analyze dataset using full-quantile normalization

### Implement and apply full-quantile normalization

```r
### implement FQ normalization
FQnorm <- function(counts){
  ...
}

### normalize the data using FQ

```

### Visualize effect of FQ normalization

Visualize the distributions of `log1p`-transformed counts (use the `density` function) to compare sample-specific count distributions before and after FQ normalization.
What's the impact of FQ normalization on the differences in distribution between samples?

### `edgeR` analysis using full-quantile normalized data

Don't forget to remove the `calcNormFactors` step in the `edgeR` analysis as data have already been normalized when using FQ-normalized counts as input!

```r
### use FQ-normalized data as input to the edgeR analysis
```

### Compare DE genes at 5% FDR

```r
### Get list of DE genes using TMM and FQ normalization

### Compare list using, e.g., a Venn diagram
```

---

[Up: contents](index.md)
