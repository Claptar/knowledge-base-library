---
title: 2.1 The CPTAC A vs B dataset
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialPreprocessing.Rmd
source_file: sources/statomics-sga21/pda_tutorialPreprocessing.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.1 The CPTAC A vs B dataset

**Source:** [`pda_tutorialPreprocessing.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialPreprocessing.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

The result of a quantitative analysis is a list of peptide and/or protein abundances for every protein in different samples, or abundance ratios between the samples. In this chapter we will describe a generic workflow for differential analysis of quantitative datasets with simple experimental designs.

In order to extract relevant information from these massive datasets, we will use our [msqrob2](https://www.bioconductor.org/packages/release/bioc/html/msqrob2.html) software tool [@goeminne2016], [@goeminne2020] and [@sticker2020].

The tutorial can be done using R/Rmarkdown scripts or using the graphical user interface that is provided by the `msqrob2gui` Shiny App.

---

[Up: contents](index.md) · [2.2 The CPTAC A vs B dataset →](02-2-2-the-cptac-a-vs-b-dataset.md)
