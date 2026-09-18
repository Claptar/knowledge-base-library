---
title: 2.3.4. The Model tab
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd
source_file: sources/statomics-sga21/cptac_robust_gui.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`cptac_robust_gui.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2.3.4. The Model tab

When you click the Model tab, the following screen is obtained:

![Figure 10. msqrob2 Model tab](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiModel.png)

The Model tab shows information on the experimental design (annotation) in the right panel.
In the left panel we have to propose the model to model the intensities of the preprocessed and summarized data.

msqrob2 makes use of linear models for assessing differential expression.
The models for are specified symbolically.
The formula is build using the names of the design variables.
A typical model has the form ‘ ~ terms’ where ‘terms’ is a series of terms which specifies a linear model.

- A terms specification of the form ‘variable1’ will model the preprocessed intensities in function of the design variable ‘variable1’. If ‘variable1’ is a continuous variable this will result in a linear model with an intercept and a slope for the variable treatment.
If ‘variable1’ is a factor variable it will result in a linear model with an intercept for the reference class and slope parameters with the interpretation of the average difference between the preprocessed intensity of the current class and the reference class.

- A terms specification of the form ‘variable1 + variable2’ indicates the inclusion of the main effects (terms for all slope terms) for ‘variable1’ and ‘variable2’.

- A specification of the form ‘variable1:variable2’ indicates the set of terms obtained by taking the interactions of all terms in ‘variable1’ with all terms in ‘variable2’, i.e. the effect of ‘variable1’ can be altered according to the value of ‘variable2’.

- The specification ‘variable1\*variable’ indicates the *cross* of ‘variable1’ and ‘variable2’. This is the same as ‘variable1 + variable2 + variable1:variable2’.

Here, we only have one factor 'treatment' in the experimental design with two levels: spikein treatment A and B.

1. So we will define the formula as

`~ treatment`

Note that as soon as we do that, the design is visualised.

![Figure 11. msqrob2 Model tab with design](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiModel2.png)

This visualisation shows the different group means that are modelled.

- Here we see that the group mean for the treatment A is modelled using the parameter
```(Intercept)```

- The group mean for the treatment B is modelled using a linear combination of the two model parameters
```(Intercept) + treatmentB```

Hence the average difference in preprocessed protein expression value between both conditions equals
```treatmentB```

Remember that we log-transformed the intensities:

$$
\log_2FC_\text{B-}=\log_2 B - \log_2 A = \log_2\frac{B}{A} = \text{treatmentB}
$$

Note that a linear combination of model parameters is als referred to as a contrast in statistics.
This contrast has the interpretation of a log2 fold change between condition 6B and condition 6A. Positive estimates denote that the abundance of the protein is on average higher in condition B, negative estimates denote that the abundance is on average higher in condition A. An estimate equal to 0 indicates that the estimated abundances are equal.

A log2 FC = 1 indicates that the average abundance in condition B is 2 x higher than the average abundance in condition A, i.e. an 2 fold upregulation in condition B as compared to condition A.

2. We now have to click the `Fit Model!` button to fit the models for each protein.

We are now ready for assessing differential abundance of each protein using formal hypothesis testing.

### 2.3.4. The Inference tab

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

## 2.3.4 The DetailPlots Tab

1. Select one protein in the table or by clicking on a point in the volcano-plot

2. Clicking on the DetailPlot tab is visualising the data for your selected protein.

![Figure 14. msqrob2 DetailPlot tab](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/guiDetailPlot.png)

3. You can further modify the plot by coloring the data according to a design variable or by splitting the data horizontally or vertically according to design variables.

---

[← 2.3.2. The Preprocessing tab](03-2-3-2-the-preprocessing-tab.md) · [Up: contents](index.md) · [2.3.5. The Report Tab →](05-2-3-5-the-report-tab.md)
