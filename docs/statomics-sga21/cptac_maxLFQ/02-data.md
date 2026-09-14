---
title: Data
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_maxLFQ.Rmd
source_file: sources/statomics-sga21/cptac_maxLFQ.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data

**Source:** [`cptac_maxLFQ.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_maxLFQ.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We first import the data from proteinGroups.txt file. This is the file containing
maxLFQ summarized protein-level intensities. For a MaxQuant search [6],
this proteinGroups.txt file can be found by default in the
"path_to_raw_files/combined/txt/" folder from the MaxQuant output,
with "path_to_raw_files" the folder where the raw files were saved.
In this vignette, we use a MaxQuant proteinRaws file which is a subset
of the cptac study.
To import the data we use the `QFeatures` package.

We generate the object proteinRawFile with the path to the proteinGroups.txt file.
Using the `grepEcols` function, we find the columns that contain the LFQ expression
data of the proteinRaws in the proteinGroups.txt file.


```r
library(tidyverse)
library(limma)
library(QFeatures)
library(msqrob2)
library(plotly)
library(gridExtra)

proteinsFile <- "https://raw.githubusercontent.com/statOmics/PDA21/data/quantification/cptacAvsB_lab3/proteinGroups.txt"

ecols <- grep("LFQ\\.intensity\\.", names(read.delim(proteinsFile)))

pe <- readQFeatures(
    table = proteinsFile, fnames = 1, ecol = ecols,
    name = "proteinRaw", sep = "\t"
)
```

In the following code chunk, we can extract the spikein condition from the raw file name.

```r
cond <- which(
  strsplit(colnames(pe)[[1]][1], split = "")[[1]] == "A") # find where condition is stored

colData(pe)$condition <- substr(colnames(pe), cond, cond) %>%
  unlist %>%
  as.factor
```


We calculate how many non zero intensities we have per protein and this
will be useful for filtering.

```r
rowData(pe[["proteinRaw"]])$nNonZero <- rowSums(assay(pe[["proteinRaw"]]) > 0)
```


Proteins with zero intensities are missing and should be represent
with a `NA` value rather than `0`.
```r
pe <- zeroIsNA(pe, "proteinRaw") # convert 0 to NA
```


## Data exploration

`r format(mean(is.na(assay(pe[["proteinRaw"]])))*100,digits=2)`% of all peptide
intensities are missing and for some proteins we do not even measure a signal
in any sample.

---

[← Background](01-background.md) · [Up: contents](index.md) · [Preprocessing →](03-preprocessing.md)
