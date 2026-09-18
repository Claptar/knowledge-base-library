---
title: Data
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.Rmd
source_file: sources/statomics-sga21/heartMainInteractionStageR.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`heartMainInteractionStageR.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Data

Researchers have assessed the proteome in different regions of the heart for 3 patients (identifiers 3, 4, and 8). For each patient they sampled the left atrium (LA), right atrium (RA), left ventricle (LV) and the right ventricle (RV). The data are a small subset of the public dataset PXD006675 on PRIDE.

Suppose that researchers are mainly interested in comparing the ventricular to the atrial proteome. Particularly, they would like to compare the left atrium to the left ventricle, the right atrium to the right ventricle, the average ventricular vs atrial proteome and if ventricular vs atrial proteome shifts differ between left and right heart region.

We first import the peptides.txt file. This is the file that contains your peptide-level intensities. For a MaxQuant search [6], this peptides.txt file can be found by default in the "path_to_raw_files/combined/txt/" folder from the MaxQuant output, with "path_to_raw_files" the folder where raw files were saved. In this tutorial, we will use a MaxQuant peptides file from MaxQuant that can be found in the data tree of the SGA2020 github repository https://github.com/statOmics/SGA2020/tree/data/quantification/heart .

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

peptidesFile <- "https://raw.githubusercontent.com/statOmics/PDA21/data/quantification/heart/peptides.txt"

ecols <- grep("Intensity\\.", names(read.delim(peptidesFile)))

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
colData(pe)$location <- substr(
  colnames(pe[["peptideRaw"]]),
  11,
  11) %>%
  unlist %>%
  as.factor

colData(pe)$tissue <- substr(
    colnames(pe[["peptideRaw"]]),
    12,
    12) %>%
    unlist %>%
    as.factor

colData(pe)$patient <- substr(
  colnames(pe[["peptideRaw"]]),
  13,
  13) %>%
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
in any sample. The missingness is similar across samples.

---

[Up: contents](index.md) · [Preprocessing →](02-preprocessing.md)
