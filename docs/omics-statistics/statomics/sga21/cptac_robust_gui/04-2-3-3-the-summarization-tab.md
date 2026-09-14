---
title: 2.3.3. The Summarization tab
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd
source_file: sources/statomics-sga21/cptac_robust_gui.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.3.3. The Summarization tab

**Source:** [`cptac_robust_gui.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

The preprocessing tab features different summarization options. When you click the preprocessing tab, the following screen is obtained:

![Figure 9. msqrob2 Summarization tab](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiSummarization.png)

When robust summarization is applied, the novel and much faster two-stage approach is used to fit the MSqRob model. Mean and median summarization are also implemented, but mainly for didactical reasons and to show the problems related to naive summarization methods. You always have to invoke the “Start Summarization!” button in order to create an object needed for downstream quantification. Depending on the method, summarization might take a while.

1. We first select the naive median summarization method and hit the “Start Summarization!” button. When the summarization is finished an MDS plot is generated based on the summarized intensities.

2. We then select the robust method, which we will use in the downstream data analysis method so as to implement the two-stage MSqRob procedure.

What do you see upon summarization with the robust method and why would that be the case? [2.3.3.a]

---

[← 2.3.2. The Preprocessing tab](03-2-3-2-the-preprocessing-tab.md) · [Up: contents](index.md) · [2.3.4. The Model tab →](05-2-3-4-the-model-tab.md)
