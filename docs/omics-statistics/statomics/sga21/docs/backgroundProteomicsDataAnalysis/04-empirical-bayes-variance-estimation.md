---
title: Empirical Bayes variance estimation
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf
source_file: sources/statomics-sga21/docs/backgroundProteomicsDataAnalysis.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`docs/backgroundProteomicsDataAnalysis.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Empirical Bayes variance estimation

Finally, we robustify our inference with limma's empirical Bayes variance estimation (see section 4.2.2). In brief, limma assumes the following prior distribution on the error variance $\sigma_i^2$ for each protein $i$ ($i = 1, \dots, I$):

$$\frac{1}{\sigma_i^2} \sim \frac{1}{d_0\sigma_0^2} \chi_{d_0}^2,$$

with $\sigma_0^2$ a prior variance and $\chi_{d_0}^2$ a $\chi^2$ distribution with $d_0$ degrees of freedom. A maximum a posteriori residual standard deviation $\tilde{s}_i$ for each protein is given by:

$$\tilde{s}_i = \sqrt{\frac{d_i\hat{\sigma}_i^2 + d_0\hat{\sigma}_0^2}{d_i + d_0}}$$

We then plug in this posterior residual standard deviation in the estimator for the standard deviation of the model parameter of interest, $\hat{\beta}_{m_g}^g$ (suppressing the indicator $i$ for notational convenience):

$$\tilde{\sigma}_{\hat{\beta}_{m_g}^g} = \tilde{s} \sqrt{(\boldsymbol{C}^{\mathrm{T}}\boldsymbol{W}\boldsymbol{C} + \boldsymbol{B})^{-1}_{m_g, m_g}}$$

Herein, $m_g, m_g$ denotes the $m_g$th diagonal element of the matrix. This enables statistical inference with a moderated t-test with $d_i + d_0$ degrees of freedom:

$$\tilde{t}_{im_g} = \frac{\hat{\beta}_{im_g}^g}{\tilde{\sigma}_{\hat{\beta}_{im_g}^g}}$$

Herein, $d_i$ is calculated as $J - \mathrm{tr}(\boldsymbol{H})$, with $J$ the total number of observations and $\boldsymbol{H}$ the hat matrix, which is calculated as follows:

$$\boldsymbol{H} = \boldsymbol{C}(\boldsymbol{C}^{\mathrm{T}}\boldsymbol{W}\boldsymbol{C} + \boldsymbol{B})^{-1} \boldsymbol{C}^{\mathrm{T}}\boldsymbol{W}$$

## Implementation

MSqRob builds on the lme4 R package for parameter estimation and statistical inference [4]. Shrinkage on fixed effect parameters is obtained by encoding them as random effects. To allow for robust M-estimation, a loop is placed around the model fitting procedure: after model fitting, Huber weights are calculated on the residuals scaled with the residual standard deviation. These weights are provided as arguments to the lmer function of the lme4 package, which allows to estimate the parameters via weighted log-likelihood. This procedure is repeated until convergence.

## References for the Appendix

1. Daly, D.S. et al., *Mixed-Effects Statistical Model for Comparative LC−MS Proteomics Studies*. Journal of Proteome Research, 2008. **7**(3): p. 1209-1217.
2. Zhou, T., *Weighting Method for a Linear Mixed Model*. Communications in Statistics - Theory and Methods, 2009. **39**(2): p. 214-227.
3. Zhou, X., H. Lindsay, and M.D. Robinson, *Robustly detecting differential expression in RNA sequencing data using observation weights*. Nucleic Acids Research, 2014. **42**(11): p. e91-e91.
4. Bates, D. et al., *Fitting Linear Mixed-Effects Models Using lme4*. Journal of Statistical Software; Vol 1, Issue 1 (2015), 2015.

---

[← Robust regression with M estimation](03-robust-regression-with-m-estimation.md) · [Up: contents](index.md)
