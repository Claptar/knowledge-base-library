---
title: Data
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd
source_file: sources/statomics-sga21/cancer2_6x6.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data

**Source:** [`cancer2_6x6.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We first import the peptides.txt file. This is the file that contains your peptide-level intensities. For a MaxQuant search [6], this peptides.txt file can be found by default in the "path_to_raw_files/combined/txt/" folder from the MaxQuant output, with "path_to_raw_files" the folder where raw files were saved. In this tutorial, we will use a MaxQuant peptides file from MaxQuant that can be found in the data tree of the SGA2020 github repository https://github.com/statOmics/SGA2020/tree/data/quantification/cancer .

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

peptidesFile <- "https://raw.githubusercontent.com/statOmics/SGA2020/data/quantification/cancer/peptides6vs6.txt"

ecols <- grep(
  "Intensity\\.",
  names(read.delim(peptidesFile))
  )

pe <- readQFeatures(
  table = peptidesFile,
  fnames = 1,
  ecol = ecols,
  name = "peptideRaw", sep="\t")

pe
pe[["peptideRaw"]]
```

We will make use from data wrangling functionalities from the tidyverse package.
The %>% operator allows us to pipe the output of one function to the next function.

```r
colData(pe)$outcome <- substr(
  colnames(pe[["peptideRaw"]]),
  11,
  12) %>%
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
