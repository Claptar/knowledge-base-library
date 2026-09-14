---
title: 2.3.5. The Report Tab
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd
source_file: sources/statomics-sga21/cptac_robust_gui.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.3.5. The Report Tab

**Source:** [`cptac_robust_gui.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

A reproducible Rmarkdown script and html report with the analysis you performed with the GUI can be downloaded in the novel report tab.

![Figure 14. msqrob2 DetailPlot tab](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiReport.png)

1. You can select the number of detail plots you want to generate in the report. The default is 10, which indicates that detail plots will be constructed for the 10 most significant protein in your top list.
Note, that the number of detail plots can be smaller if there are less than 10 proteins significant at the specified FDR-level.

2. Hit the `Generate report` button and a report will be compiled. Note, that this will take a while because all analysis steps from each of the tabs have to be conducted again. You will see a progress bar and when it is finished a zip file will be downloaded that contains:

  - features.txt: A tab delimited file with the raw intensity data
  - annotation.xlsx: An excel file with the annotation of the design
  - report.Rmd: R/markdown file with the code for the report. If you open the file in Rstudio and if you hit the knit button the report will be compiled to html.
  - report.html: The compiled report.

So, your analysis is stored in a fully reproducible way.

---

[← 2.3.4 The DetailPlots Tab](07-2-3-4-the-detailplots-tab.md) · [Up: contents](index.md) · [2.3.6. Evaluate Summarization →](09-2-3-6-evaluate-summarization.md)
