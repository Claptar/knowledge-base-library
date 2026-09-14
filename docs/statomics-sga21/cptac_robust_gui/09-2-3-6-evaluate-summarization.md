---
title: 2.3.6. Evaluate Summarization
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd
source_file: sources/statomics-sga21/cptac_robust_gui.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.3.6. Evaluate Summarization

**Source:** [`cptac_robust_gui.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We further explore the difference between summarization methods.
We first assess the quality of the fold change estimates for the robust summarization.
We will make use of the boxplot at the bottom of the quantification tab.

1. If you untick the option `only significant features in table` all proteins are shown in the table. The boxplot below the table visualizes the log2 fold change (FC) estimates for all proteins in the table.

2. We can now filter the ups proteins by typing "ups" in the search field above the table. Now all yeast proteins are removed from the results table and a boxplot of the ups protein log2 FCs will be made.

![Figure 15. msqrob2 Inference tab with Fold Change Boxplot for all UPS proteins](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiRobustUps.png)

[2.3.6.a] We know the real FC for the spike in proteins (see description of the data 2.2). Note, that the boxplot is showing the log2 FC. What do you observe?

[2.3.6.b] Now select all yeast proteins. What is the real fold change and what do you observe?

[2.3.6.c] Repeat this for the median summarization method. What do you observe, how does that compare to the robust summarisation and try to explain this?

---

[← 2.3.5. The Report Tab](08-2-3-5-the-report-tab.md) · [Up: contents](index.md) · [Final remark →](10-final-remark.md)
