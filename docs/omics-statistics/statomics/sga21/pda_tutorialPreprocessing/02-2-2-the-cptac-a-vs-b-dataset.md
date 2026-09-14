---
title: 2.2 The CPTAC A vs B dataset
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialPreprocessing.Rmd
source_file: sources/statomics-sga21/pda_tutorialPreprocessing.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.2 The CPTAC A vs B dataset

**Source:** [`pda_tutorialPreprocessing.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialPreprocessing.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Our first case-study is a subset of the data of the 6th study of the Clinical Proteomic Technology Assessment for Cancer (CPTAC). In this experiment, the authors spiked the Sigma Universal Protein Standard mixture 1 (UPS1) containing 48 different human proteins in a protein background of 60 ng/μL Saccharomyces cerevisiae strain BY4741 (MATa, leu2Δ0, met15Δ0, ura3Δ0, his3Δ1). Two different spike-in concentrations were used: 6A (0.25 fmol UPS1 proteins/μL) and 6B (0.74 fmol UPS1 proteins/μL) [5].

We limited ourselves to the data of LTQ-Orbitrap W at site 56. The data were searched with MaxQuant version 1.5.2.8, and detailed search settings were described in [@goeminne2016]. Three replicates are available for each concentration.

- The raw data files can be downloaded from https://cptac-data-portal.georgetown.edu/cptac/public?scope=Phase+I (Study 6)

-  The MaxQuant data can be downloaded [zip file with data](https://github.com/statOmics/PDA21/archive/refs/heads/data.zip). The peptides.txt file can be found in data/quantification/cptacAvsB_lab3.

- Note, that participants who use R/Rmarkdown scripts do not have to download the data as they can directly import the data from the web in R within their script.


[2.3.a] Participants can perform an analysis using the [GUI](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.html) or an [Rmarkdown script](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.html)

Follow the steps in the GUI or in the script and try to understand each of the analysis steps. We know the real FC for the spike in proteins and the yeast proteins (see description of the data). What do you observe?

[2.3.b] Repeat the analysis for the median summarization method. What do you observe, how does that compare to the robust summarisation and try to explain this?

---

[← 2.1 The CPTAC A vs B dataset](01-2-1-the-cptac-a-vs-b-dataset.md) · [Up: contents](index.md) · [2.3 Breast cancer example →](03-2-3-breast-cancer-example.md)
