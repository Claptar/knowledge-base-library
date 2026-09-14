---
title: 2.3.4. The Model tab
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd
source_file: sources/statomics-sga21/cptac_robust_gui.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.3.4. The Model tab

**Source:** [`cptac_robust_gui.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[← 2.3.3. The Summarization tab](04-2-3-3-the-summarization-tab.md) · [Up: contents](index.md) · [2.3.4. The Inference tab →](06-2-3-4-the-inference-tab.md)
