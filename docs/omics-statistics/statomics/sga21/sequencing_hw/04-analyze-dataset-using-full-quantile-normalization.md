---
title: Analyze dataset using full-quantile normalization
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_hw.Rmd
source_file: sources/statomics-sga21/sequencing_hw.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Analyze dataset using full-quantile normalization

**Source:** [`sequencing_hw.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_hw.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Implement and apply full-quantile normalization

```r
### implement FQ normalization
FQnorm <- function(counts){
  ...
}

### normalize the data using FQ

```

## Visualize effect of FQ normalization

Visualize the distributions of `log1p`-transformed counts (use the `density` function) to compare sample-specific count distributions before and after FQ normalization.
What's the impact of FQ normalization on the differences in distribution between samples?

## `edgeR` analysis using full-quantile normalized data

Don't forget to remove the `calcNormFactors` step in the `edgeR` analysis as data have already been normalized when using FQ-normalized counts as input!

```r
### use FQ-normalized data as input to the edgeR analysis
```

## Compare DE genes at 5% FDR

```r
### Get list of DE genes using TMM and FQ normalization

### Compare list using, e.g., a Venn diagram
```

---

[← Impact of blocking](03-impact-of-blocking.md) · [Up: contents](index.md)
