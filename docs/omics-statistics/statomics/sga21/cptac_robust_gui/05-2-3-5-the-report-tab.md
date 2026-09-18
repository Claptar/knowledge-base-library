---
title: 2.3.5. The Report Tab
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd
source_file: sources/statomics-sga21/cptac_robust_gui.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`cptac_robust_gui.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2.3.5. The Report Tab

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

## 2.3.6. Evaluate Summarization

We further explore the difference between summarization methods.
We first assess the quality of the fold change estimates for the robust summarization.
We will make use of the boxplot at the bottom of the quantification tab.

1. If you untick the option `only significant features in table` all proteins are shown in the table. The boxplot below the table visualizes the log2 fold change (FC) estimates for all proteins in the table.

2. We can now filter the ups proteins by typing "ups" in the search field above the table. Now all yeast proteins are removed from the results table and a boxplot of the ups protein log2 FCs will be made.

![Figure 15. msqrob2 Inference tab with Fold Change Boxplot for all UPS proteins](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiRobustUps.png)

[2.3.6.a] We know the real FC for the spike in proteins (see description of the data 2.2). Note, that the boxplot is showing the log2 FC. What do you observe?

[2.3.6.b] Now select all yeast proteins. What is the real fold change and what do you observe?

[2.3.6.c] Repeat this for the median summarization method. What do you observe, how does that compare to the robust summarisation and try to explain this?

## Final remark

- Note, that the shiny app is an interface to the statistical programming software R.

- The analysis can also be conducted using scripts, which gives you much more functionality and the ability to streamline, automate and document your analyses in a reproducible way.

---

[← 2.3.4. The Model tab](04-2-3-4-the-model-tab.md) · [Up: contents](index.md)
