---
title: 2.3.4. The Inference tab
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd
source_file: sources/statomics-sga21/cptac_robust_gui.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.3.4. The Inference tab

**Source:** [`cptac_robust_gui.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

When you click the Model tab, the following screen is obtained:

![Figure 12. msqrob2 Inference tab](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiInference.png)

In the statistical analysis we will want to test the null hypothesis that

$$ H_0: \log_2 B-\log_2 6A = 0 $$

Against the alternative that
$$ H_1: \log_2 B - \log_2 A \neq 0 $$

1. We can specify the nulhypothesis as a linear combination of the model parameters, i.e.

```treatmentB = 0```

This is what we have to fill in the field null hypothesis.

We will falsify this null hypothesis for each protein separately based on the linear model. So, under the null hypothesis we reason that there is no effect of the spike-in treatment on the abundance of a specific protein. The p-value of the statistical test than indicates the probability to observe an effect (fold change), that is as extreme or more extreme (equally or more up or down regulated) than what is observed in the sample, by random change (when the null hypothesis is true and when there is in reality no effect of the treatment).


2. As soon as you specified the Null Hypothesis the window is updated

![Figure 13 msqrob2 Inference tab with contrast](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiInference2.png)

and a volcano plot appears that gives you a view on statistical significance in the y-axis, i.e. the $-\log_{10}$ transformed p-value: a value of 1 equals to a p-value of 0.1, a value of 2 equals a p-value of 0.01, etc against biological relevance/the effect size in the x-axis, which is the $\log_2FC$.

You also get a table with selected feature. By default this are all proteins that are significant with the specified significance level in the `Significance field`.
You also obtain a boxplot of the log2-fold changes for all proteins that are selected in the table.

Note that 20 proteins are displayed. The majority of them are UPS proteins that were spiked-in. Only one yeast protein is recovered in the top 20.

3. If you untick the option `only significant features in table` all proteins are shown in the table.

4. You can also select proteins by selecting an area on the volcano plot.

  - Click on the left mouse button and keep the button pressed and drag the mouse: a blue area appears

  - Double click to zoom in now the proteins are selected in the results table.   - Double click on an unselected area to reset the plot window.

5.  Selecting a protein(s) in the “Results table” results in selecting it on the Volcano plot.

6. You can search for specific proteins in the list by using the search field above the table. E.g. type `ups`.

7. If you select one protein in the table or by clicking on a point in the volcano-plot you can also explore the underlying normalised peptide intensities and protein intensities of the underlying data in the tab DetailPlots.

---

[← 2.3.4. The Model tab](05-2-3-4-the-model-tab.md) · [Up: contents](index.md) · [2.3.4 The DetailPlots Tab →](07-2-3-4-the-detailplots-tab.md)
