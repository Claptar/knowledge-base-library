---
title: 'Intro: Challenges in Label-Free Quantitative Proteomics'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd
source_file: sources/statomics-sga21/pda_quantification_preprocessing.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`pda_quantification_preprocessing.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Intro: Challenges in Label-Free Quantitative Proteomics

## MS-based workflow

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

## Level of quantification

- MS-based proteomics returns peptides: pieces of proteins

```r
knitr::include_graphics("./figures/challenges_peptides.png")
```

- Quantification commonly required on the protein level

```r
knitr::include_graphics("./figures/challenges_proteins.png")
```

---

## Label-free Quantitative Proteomics Data Analysis Workflows

```r
knitr::include_graphics("./figures/proteomicsDataAnalysis.png")
```

---

## CPTAC Spike-in Study

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

## Maxquant output

```r
knitr::include_graphics("./figures/maxquantOutputDir.png")
```

---

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Import the data in R →](03-import-the-data-in-r.md)
