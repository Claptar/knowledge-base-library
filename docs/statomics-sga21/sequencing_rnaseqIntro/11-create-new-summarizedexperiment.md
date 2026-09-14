---
title: Create new SummarizedExperiment
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Create new SummarizedExperiment

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

se <- SummarizedExperiment(assays = list("counts" = newCounts),
                            colData = newCD,
                            metadata = metadata(se1))

treatment <- colData(se)$treatment
table(treatment)
time <- colData(se)$time
table(time)
patient <- colData(se)$patient
table(patient)

table(patient, treatment, time) # agrees with paper.

```

 - After summing the technical replicates and appropriately updating the sample information, we again create a `SummarizedExperiment` object, which is essentially a data container that contains all relevant information about your experiment. Please see the [vignette](https://bioconductor.org/packages/release/bioc/vignettes/SummarizedExperiment/inst/doc/SummarizedExperiment.html) for more information on how to use this class.
 - By directly matching columns (samples) and rows (genes) to their relevant metadata, the `SummarizedExperiment` class avoids mistakes by mis-matching columns and rows with each other (provided you haven't mismatched them when you create the object).
 - The `SummarizedExperiment` class is modular and extendable, and extensions exist for example for the analysis of single-cell RNA-seq data, i.e., the `SingleCellExperiment` class.
 - Due to their convenient organization and widely supported usage within Bioconductor, we will typically work with such classes in the analysis of RNA-seq data.

## Independent filtering

Independent filtering is a strategy to remove features (in this case, genes) prior to the analysis. Removal of these features may lower the multiple testing correction for other genes that pass the filter. We try to remove genes that have a low power to be found statistically significant, and/or that are biologically less relevant.
A common filtering strategy is to remove genes with a generally low expression, as low counts have lower relative uncertainty (hence lower statistical power), and may be considered biologically less relevant.

```r
suppressPackageStartupMessages({
  library(limma)
  library(edgeR)
})

keep <- rowSums(cpm(se) > 2) >= 3
table(keep)
se <- se[keep,]
```

## Data exploration

```r

---

[← remove after summing counts (otherwise IDs get mixed up)](10-remove-after-summing-counts-otherwise-ids-get-mixed-up.md) · [Up: contents](index.md) · [library size distribution →](12-library-size-distribution.md)
