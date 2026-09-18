---
title: Robust regression with M estimation
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf
source_file: sources/statomics-sga21/docs/backgroundProteomicsDataAnalysis.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`docs/backgroundProteomicsDataAnalysis.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Robust regression with M estimation

To robustify our procedure against outliers, we use a weighted maximum likelihood method with Huber weights, as proposed by Zhou (2009) [2].

$$\sum_{j=1}^J w_j \, l(y_j, \boldsymbol{\beta}, \boldsymbol{u}),$$

with $j = 1, \dots, J$ an indicator for observation. This weighted log-likelihood is solved iteratively. The mixed model is fitted while the weights are kept constant. Then, the weights are recomputed using Huber's weight function on the residuals scaled with the residual standard deviation. This procedure is repeated until convergence. After convergence, the weighted BLUP estimator is given by:

$$\begin{bmatrix} \hat{\boldsymbol{\beta}} \\ \hat{\boldsymbol{\beta}}^{\text{peptide}} \\ \hat{\boldsymbol{u}}^{\text{run}} \end{bmatrix} = (\boldsymbol{C}^{\mathrm{T}}\boldsymbol{W}\boldsymbol{C} + \boldsymbol{B})^{-1} \boldsymbol{C}^{\mathrm{T}}\boldsymbol{W}\boldsymbol{y},$$

with $\boldsymbol{W} = [w_1 \dots w_j \dots w_J]\boldsymbol{I}_{J \times J}$ and $w_1$ to $w_J$ the weights corresponding to these observations and $\boldsymbol{I}_{J \times J}$ a $J \times J$ unity matrix. Zhou (2009) [2] showed that the weighted BLUP estimator is better than the unweighted one in terms of bias and efficiency when the data contains some outliers but provides the same asymptotic efficiency when the model is correctly specified. Robust M estimation with Huber weights has also been used to robustify the negative binomial model in the popular RNA sequencing R package EdgeR [3].

---

[← Ridge regression](02-ridge-regression.md) · [Up: contents](index.md) · [Empirical Bayes variance estimation →](04-empirical-bayes-variance-estimation.md)
