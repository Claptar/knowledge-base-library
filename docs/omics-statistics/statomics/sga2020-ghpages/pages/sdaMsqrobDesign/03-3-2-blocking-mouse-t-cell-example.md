---
title: '3.2 Blocking: Mouse T-cell example'
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/sdaMsqrobDesign.md
source_file: sources/statomics-sga2020-ghpages/pages/sdaMsqrobDesign.md
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3.2 Blocking: Mouse T-cell example

**Source:** [`pages/sdaMsqrobDesign.md`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/sdaMsqrobDesign.md) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.md` (lossless)

Duguet et al. 2017 compared the proteomes of mouse regulatory T cells (Treg) and conventional T cells (Tconv) in order to discover differentially regulated proteins between these two cell populations. For each biological repeat the proteomes were extracted for both Treg and Tconv cell pools, which were purified by flow cytometry. The data in data/quantification/mouseTcell on the SGA2019Data repository are a subset of the data [PXD004436](https://www.ebi.ac.uk/pride/archive/projects/PXD004436) on PRIDE.

![Figure 4. Design Mouse Study](https://raw.githubusercontent.com/statOmics/SGA2020/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/figs/mouseTcell_RCB_design.png)

Three subsets of the data are avialable:


- peptidesCRD.txt: contains data of Tconv cells for 4 bio-repeats and Treg cells for 4 bio-repeats
- peptidesRCB.txt: contains data for 4 bio-repeats only, but for each bio-repeat the Treg and Tconv proteome is profiled.
- peptides.txt: contains data of Treg and Tconv cells for 7 bio-repeats

Adjust the script [cptac.html](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/cptac_median.html) for the analysis. Do not forget to alter the summarisation!

##### 3.2.1. How would you analyse the CRD data?

##### 3.2.2. How would you analyse the RCB data?

##### 3.2.3. Try to explain the difference in the number of proteins that can be discovered with both designs?

<br/><br/>

---

[← 3.1 Basic Statistical Concepts](02-3-1-basic-statistical-concepts.md) · [Up: contents](index.md) · [3.3 Heart dataset →](04-3-3-heart-dataset.md)
