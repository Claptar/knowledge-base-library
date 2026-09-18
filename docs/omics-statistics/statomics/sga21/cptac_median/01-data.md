---
title: Data
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_median.Rmd
source_file: sources/statomics-sga21/cptac_median.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`cptac_median.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_median.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Data

[](https://creativecommons.org/licenses/by-nc-sa/4.0)

This is part of the online course [Proteomics Data Analysis 2021 (PDA21)](https://statomics.github.io/PDA21/)

## Background
This case-study is a subset of the data of the 6th study of the Clinical
Proteomic Technology Assessment for Cancer (CPTAC).
In this experiment, the authors spiked the Sigma Universal Protein Standard
mixture 1 (UPS1) containing 48 different human proteins in a protein background
of 60 ng/$\mu$L Saccharomyces cerevisiae strain BY4741.
Two different spike-in concentrations were used:
6A (0.25 fmol UPS1 proteins/$\mu$L) and 6B (0.74 fmol UPS1 proteins/$\mu$L) [5].
We limited ourselves to the data of LTQ-Orbitrap W at site 56.
The data were searched with MaxQuant version 1.5.2.8, and
detailed search settings were described in Goeminne et al. (2016) [1].
Three replicates are available for each concentration.

- NOTE THAT MEDIAN SUMMARISATION IS SUBOPTIMAL!
- THIS IS FOR DIDACTICAL PURPOSES ONLY.

We first import the data from peptideRaws.txt file. This is the file containing
your peptideRaw-level intensities. For a MaxQuant search [6],
this peptideRaws.txt file can be found by default in the
"path_to_raw_files/combined/txt/" folder from the MaxQuant output,
with "path_to_raw_files" the folder where the raw files were saved.
In this vignette, we use a MaxQuant peptideRaws file which is a subset
of the cptac study. This data is available in the `msdata` package.
To import the data we use the `QFeatures` package.

We generate the object peptideRawFile with the path to the peptideRaws.txt file.
Using the `grepEcols` function, we find the columns that contain the expression
data of the peptideRaws in the peptideRaws.txt file.

```r
library(tidyverse)
library(limma)
library(QFeatures)
library(msqrob2)
library(plotly)

peptidesFile <- "https://raw.githubusercontent.com/statOmics/SGA2020/data/quantification/cptacAvsB_lab3/peptides.txt"

ecols <- grep(
  "Intensity\\.",
  names(read.delim(peptidesFile))
  )

pe <- readQFeatures(
  table = peptidesFile,
  fnames = 1,
  ecol = ecols,
  name = "peptideRaw", sep="\t")

colnames(pe)
```

In the following code chunk, we can extract the spikein condition from the raw file name.

```r
cond <- which(
  strsplit(colnames(pe)[[1]][1], split = "")[[1]] == "A") # find where condition is stored

colData(pe)$condition <- substr(colnames(pe), cond, cond) %>%
  unlist %>%
  as.factor
```

We calculate how many non zero intensities we have per peptide and this
will be useful for filtering.

```r
rowData(pe[["peptideRaw"]])$nNonZero <- rowSums(assay(pe[["peptideRaw"]]) > 0)
```

Peptides with zero intensities are missing peptides and should be represent
with a `NA` value rather than `0`.
```r
pe <- zeroIsNA(pe, "peptideRaw") # convert 0 to NA
```

### Data exploration

`r format(mean(is.na(assay(pe[["peptideRaw"]])))*100,digits=2)`% of all peptide
intensities are missing and for some peptides we do not even measure a signal
in any sample.

---

[Up: contents](index.md) · [Preprocessing →](02-preprocessing.md)
