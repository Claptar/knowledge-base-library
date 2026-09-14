---
title: Introduction
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

# Import data

The `scRNAseq` package provides convenient access to several datasets. See the [package Bioconductor page](http://bioconductor.org/packages/release/data/experiment/html/scRNAseq.html) for more information.

```r
# install BiocManager package if not installed yet.
# BiocManager is the package installer for Bioconductor software.
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

# install packages if not yet installed.
pkgs <- c("SingleCellExperiment", "DropletUtils", "scRNAseq", "scater", "scuttle", "scran", "BiocSingular", "scDblFinder", "glmpca", "uwot")
notInstalled <- pkgs[!pkgs %in% installed.packages()[,1]]
if(length(notInstalled) > 0){
  BiocManager::install(notInstalled)
}

# Code below might ask you to create an ExperimentHub directory.
# Type 'yes' and hit Enter, to allow this.
suppressPackageStartupMessages(library(scRNAseq))
sce <- MacoskoRetinaData()
```

# A `SingleCellExperiment` object


```r
sce
```

---

[Up: contents](index.md) · [Accessing data from a SingleCellExperiment object →](02-accessing-data-from-a-singlecellexperiment-object.md)
