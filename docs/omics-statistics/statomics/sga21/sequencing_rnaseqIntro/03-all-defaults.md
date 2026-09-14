---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/expDesign_para.png")
```

## Data import and exploration

We will be importing the dataset using the [parathyroidSE](https://www.bioconductor.org/packages/release/data/experiment/html/parathyroidSE.html) data package from [Bioconductor](https://bioconductor.org/).

```r
if (!requireNamespace("BiocManager", quietly = TRUE)){
  install.packages("BiocManager")
}
if(!"SummarizedExperiment" %in% installed.packages()[,1]){
  BiocManager::install("SummarizedExperiment")
}

---

[← Experimental design, data import and data exploration](02-experimental-design-data-import-and-data-exploration.md) · [Up: contents](index.md) · [install package if not installed. →](04-install-package-if-not-installed.md)
