---
title: '3.2 Blocking: Mouse T-cell example'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialDesign.Rmd
source_file: sources/statomics-sga21/pda_tutorialDesign.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3.2 Blocking: Mouse T-cell example

**Source:** [`pda_tutorialDesign.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialDesign.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Duguet et al. 2017 compared the proteomes of mouse regulatory T cells (Treg) and conventional T cells (Tconv) in order to discover differentially regulated proteins between these two cell populations. For each biological repeat the proteomes were extracted for both Treg and Tconv cell pools, which were purified by flow cytometry. The data in data/quantification/mouseTcell on the [PDA21-data repository](https://github.com/statOmics/PDA21/archive/refs/heads/data.zip) are a subset of the data [PXD004436](https://www.ebi.ac.uk/pride/archive/projects/PXD004436) on PRIDE.

![Figure 2. Design Mouse Study](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/mouseTcell_RCB_design.png)

Three subsets of the data are avialable:


- peptidesCRD.txt: contains data of Tconv cells for 4 bio-repeats and Treg cells for 4 bio-repeats
- peptidesRCB.txt: contains data for 4 bio-repeats only, but for each bio-repeat the Treg and Tconv proteome is profiled.
- peptides.txt: contains data of Treg and Tconv cells for 7 bio-repeats

Adjust the script [cptac.html](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.html) for the analysis or perform the analysis with the [GUI](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.html) .

#### 3.2.1. How would you analyse the CRD data?

#### 3.2.2. How would you analyse the RCB data?

#### 3.2.3. Try to explain the difference in the number of proteins that can be discovered with both designs?

<br/><br/>

---

[← 3.1 Basic Statistical Concepts](02-3-1-basic-statistical-concepts.md) · [Up: contents](index.md) · [3.3 Heart dataset →](04-3-3-heart-dataset.md)
