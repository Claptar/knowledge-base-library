---
title: Data
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.Rmd
source_file: sources/statomics-sga21/cptac_robust.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data

**Source:** [`cptac_robust.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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


## Data exploration

`r format(mean(is.na(assay(pe[["peptideRaw"]])))*100,digits=2)`% of all peptide
intensities are missing and for some peptides we do not even measure a signal
in any sample.

---

[← Background](01-background.md) · [Up: contents](index.md) · [Preprocessing →](03-preprocessing.md)
