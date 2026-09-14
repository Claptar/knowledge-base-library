---
title: 2.2 The CPTAC A vs B dataset
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/sdaMsqrobSimple.md
source_file: sources/statomics-sga2020-ghpages/pages/sdaMsqrobSimple.md
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.2 The CPTAC A vs B dataset

**Source:** [`pages/sdaMsqrobSimple.md`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/sdaMsqrobSimple.md) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.md` (lossless)

Our first case-study is a subset of the data of the 6th study of the Clinical Proteomic Technology Assessment for Cancer (CPTAC). In this experiment, the authors spiked the Sigma Universal Protein Standard mixture 1 (UPS1) containing 48 different human proteins in a protein background of 60 ng/μL Saccharomyces cerevisiae strain BY4741 (MATa, leu2Δ0, met15Δ0, ura3Δ0, his3Δ1). Two different spike-in concentrations were used: 6A (0.25 fmol UPS1 proteins/μL) and 6B (0.74 fmol UPS1 proteins/μL) [5]. The raw data files can be downloaded from https://cptac-data-portal.georgetown.edu/cptac/public?scope=Phase+I (Study 6), the processed data can be downloaded by zipping the github repository [https://github.com/statOmics/SGA2019/tree/data](https://github.com/statOmics/SGA2019/tree/data), in the folder data/quantification/cptacAvsB_lab3. We limited ourselves to the data of LTQ-Orbitrap W at site 56. The data were searched with MaxQuant version 1.5.2.8, and detailed search settings were described in Goeminne et al. (2016) [1]. Three replicates are available for each concentration.


[2.3.a] [cptac.html](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/cptac_median.html) is a script with the entire workflow when median summarisation is adopted. Study the script and try to understand each of the analysis steps. We know the real FC for the spike in proteins and the yeast proteins (see description of the data). What do you observe?

[2.3.b] Repeat the analysis for the robust summarization method. What do you observe, how does that compare to the median summarisation and try to explain this?

[2.3.c] Repeat the analysis using MaqLFQ summarization. You can use the proteinGroups.txt file for this purpose. Note, that the summarization has already be conducted by the MaxQuant software. So only log2 transformation and normalisation has to be conducted.  What do you observe, how does that compare to the robust summarisation and try to explain this?


#### 2.3 The Francisella dataset
A study on the facultative pathogen Francisella tularensis was conceived by Ramond et al. (2015) [12]. F. tularensis enters the cells of its host by phagocytosis. The authors showed that F. tularensis is arginine deficient and imports arginine from the host cell via an arginine transporter, ArgP, in order to efficiently escape from the phagosome and reach the cytosolic compartment, where it can actively multiply. In their study, they compared the proteome of wild type F. tularensis (WT) to ArgP-gene deleted F. tularensis (knock-out, D8). For this exercise, we use a subset of the F. tularensis dataset where bacterial cultures were grown in biological triplicate and each sample was run on a nanoRSLC-Q Exactive PLUS instrument. The data were searched with MaxQuant version 1.4.1.2.
The data can be found on [https://github.com/statOmics/SGA2019/tree/data](https://github.com/statOmics/SGA2019/tree/data).

Which contrast do we want to test now? [2.4.a]

Give the interpretation of the contrast for your top hit? [2.4b]

#### 2.4 Breast cancer example

Eighteen Estrogen Receptor Positive Breast cancer tissues from from patients treated with tamoxifen upon recurrence have been assessed in a proteomics study. Nine patients had a good outcome (or) and the other nine had a poor outcome (pd).
The proteomes have been assessed using an LTQ-Orbitrap  and the thermo output .RAW files were searched with MaxQuant (version 1.4.1.2) against the human proteome database (FASTA version 2012-09, human canonical proteome).

Three peptides txt files are available:

1. For a 3 vs 3 comparison
2. For a 6 vs 6 comparison
3. For a 9 vs 9 comparison

The data can be found at [https://github.com/statOmics/SGA2019/tree/data](https://github.com/statOmics/SGA2019/tree/data).
in the folder data/quantification/cancer

Perform an MSqRob analysis for each peptide file. What are the differences and try to explain why.

---

[← 2. Statistical analysis with MSqRob for simple designs](01-2-statistical-analysis-with-msqrob-for-simple-designs.md) · [Up: contents](index.md)
