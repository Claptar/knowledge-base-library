---
title: Import the data in R
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd
source_file: sources/statomics-sga21/pda_quantification_preprocessing.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Import the data in R

**Source:** [`pda_quantification_preprocessing.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Data infrastructure

<details><summary> Click to see background on data infrastructure used in R to store proteomics data </summary><p>
- We use the `QFeatures` package that provides the infrastructure to
  - store,
  - process,
  - manipulate and
  - analyse quantitative data/features from mass spectrometry
experiments.

- It is based on the `SummarizedExperiment` and
`MultiAssayExperiment` classes.


```r
knitr::include_graphics("./figures/SE.png")
```

- Assays in a QFeatures object have a
hierarchical relation:

  - proteins are composed of peptides,
  - themselves produced by spectra
  - relations between assays are tracked and recorded throughout data processing

```r
par(mar = c(0, 0, 0, 0))
plot(NA, xlim = c(0, 12), ylim = c(0, 20),
     xaxt = "n", yaxt = "n",
     xlab = "", ylab = "", bty = "n")
for (i in 0:7)
    rect(0, i, 3, i+1, col = "lightgrey", border = "white")
for (i in 8:12)
    rect(0, i, 3, i+1, col = "steelblue", border = "white")
for (i in 13:18)
    rect(0, i, 3, i+1, col = "orange", border = "white")
for (i in 19)
    rect(0, i, 3, i+1, col = "darkgrey", border = "white")
for (i in 5:7)
    rect(5, i, 8, i+1, col = "lightgrey", border = "white")
for (i in 8:10)
    rect(5, i, 8, i+1, col = "steelblue", border = "white")
for (i in 11:13)
    rect(5, i, 8, i+1, col = "orange", border = "white")
for (i in 14)
    rect(5, i, 8, i+1, col = "darkgrey", border = "white")
rect(9, 8, 12, 8+1, col = "lightgrey", border = "white")
rect(9, 9, 12, 9+1, col = "steelblue", border = "white")
rect(9, 10, 12, 10+1, col = "orange", border = "white")
rect(9, 11, 12, 11+1, col = "darkgrey", border = "white")
segments(3, 8, 5, 8, lty = "dashed")
segments(3, 6, 5, 7, lty = "dashed")
segments(3, 4, 5, 6, lty = "dashed")
segments(3, 0, 5, 5, lty = "dashed")
segments(3, 10, 5, 9, lty = "dashed")
segments(3, 11, 5, 10, lty = "dashed")
segments(3, 13, 5, 11, lty = "dashed")
segments(3, 14, 5, 12, lty = "dashed")
segments(3, 16, 5, 13, lty = "dashed")
segments(3, 19, 5, 14, lty = "dashed")
segments(3, 20, 5, 15, lty = "dashed")
segments(8, 5, 9, 8, lty = "dashed")
segments(8, 8, 9, 9, lty = "dashed")
segments(8, 11, 9, 10, lty = "dashed")
segments(8, 14, 9, 11, lty = "dashed")
segments(8, 15, 9, 12, lty = "dashed")
```

</p></details>

## Import data in R


### Load libraries

<details><summary> Click to see code </summary><p>
```r
library(tidyverse)
library(limma)
library(QFeatures)
library(msqrob2)
library(plotly)
library(ggplot2)
```
</p></details>

### Read data

<details><summary> Click to see background and code </summary><p>
1. We use a peptides.txt file from MS-data quantified with maxquant that
contains MS1 intensities summarized at the peptide level.
```r
peptidesFile <- "https://raw.githubusercontent.com/statOmics/PDA21/data/quantification/fullCptacDatasSetNotForTutorial/peptides.txt"
```

2. Maxquant stores the intensity data for the different samples in columnns that start with Intensity. We can retreive the column names with the intensity data with the code below:

```r
ecols <- grep("Intensity\\.", names(read.delim(peptidesFile)))
```

3. Read the data and store it in  QFeatures object

```r
pe <- readQFeatures(
  table = peptidesFile,
  fnames = 1,
  ecol = ecols,
  name = "peptideRaw", sep="\t")
```
</p></details>

### Explore object

<details><summary> Click to see background and code </summary><p>
- The rowData contains information on the features (peptides) in the assay. E.g. Sequence, protein, ...

```r
rowData(pe[["peptideRaw"]])
```

- The colData contains information on the samples

```r
colData(pe)
```

- No information is stored yet on the design.


```r
pe %>% colnames
```

- Note, that the sample names include the spike-in condition.
- They also end on a number.

  - 1-3 is from lab 1,
  - 4-6 from lab 2 and
  - 7-9 from lab 3.

- We update the colData with information on the design

```r
colData(pe)$lab <- rep(rep(paste0("lab",1:3),each=3),5) %>% as.factor
colData(pe)$condition <- pe[["peptideRaw"]] %>% colnames %>% substr(12,12) %>% as.factor
colData(pe)$spikeConcentration <- rep(c(A = 0.25, B = 0.74, C = 2.22, D = 6.67, E = 20),each = 9)
```

- We explore the colData again

```r
colData(pe)
```

</p></details>

---

---

[← Intro: Challenges in Label-Free Quantitative Proteomics](03-intro-challenges-in-label-free-quantitative-proteomics.md) · [Up: contents](index.md) · [Preprocessing →](05-preprocessing.md)
