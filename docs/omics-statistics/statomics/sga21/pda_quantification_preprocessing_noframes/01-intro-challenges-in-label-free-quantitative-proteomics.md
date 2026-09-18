---
title: 'Intro: Challenges in Label-Free Quantitative Proteomics'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing_noframes.Rmd
source_file: sources/statomics-sga21/pda_quantification_preprocessing_noframes.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`pda_quantification_preprocessing_noframes.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing_noframes.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Intro: Challenges in Label-Free Quantitative Proteomics

[](https://creativecommons.org/licenses/by-nc-sa/4.0)

- [Playlist PDA Preprocessing](https://www.youtube.com/playlist?list=PLZH1hP8_LbJJXQeQ_KYDNoq-AXyFBG6nX)

## Outline {-}

1. Introduction

2. Preprocessing

    - Log-transformation
    - Filtering
    - Normalization
    - Summarization

Note, that the R-code is included for learners who are aiming to develop R/markdown scripts to automate their quantitative proteomics data analyses.
According to the target audience of the course we either work with a graphical user interface (GUI) in a R/shiny App msqrob2gui (e.g. Proteomics Bioinformatics course of the EBI and the Proteomics Data Analysis course at the Gulbenkian institute) or with R/markdowns scripts (e.g. Bioinformatics Summer School at UCLouvain or the Statistical Genomics Course at Ghent University).

---

### MS-based workflow

```r
knitr::include_graphics("./figures/ProteomicsWorkflow.png")
```

- Peptide Characteristics

  - Modifications
  - Ionisation Efficiency: huge variability
  - Identification
    - Misidentification $\rightarrow$ outliers
    - MS$^2$ selection on peptide abundance
    - Context depending missingness
    - Non-random missingness

$\rightarrow$ Unbalanced pepide identifications across samples and messy data

---

### Level of quantification

- MS-based proteomics returns peptides: pieces of proteins

```r
knitr::include_graphics("./figures/challenges_peptides.png")
```

- Quantification commonly required on the protein level

```r
knitr::include_graphics("./figures/challenges_proteins.png")
```

---

### Label-free Quantitative Proteomics Data Analysis Workflows

```r
knitr::include_graphics("./figures/proteomicsDataAnalysis.png")
```

---

### CPTAC Spike-in Study

```r
knitr::include_graphics("./figures/cptacLayoutLudger.png")
```

- Same trypsin-digested yeast proteome background in each sample
- Trypsin-digested Sigma UPS1 standard: 48 different human proteins spiked in at 5 different concentrations (treatment A-E)
- Samples repeatedly run on different instruments in different labs
- After MaxQuant search with match between runs option

  - 41\% of all proteins are quantified in all samples
  - 6.6\% of all peptides are quantified in all samples

$\rightarrow$ vast amount of missingness

### Maxquant output

```r
knitr::include_graphics("./figures/maxquantOutputDir.png")
```

---

---

[Up: contents](index.md) · [Import the data in R →](02-import-the-data-in-r.md)
