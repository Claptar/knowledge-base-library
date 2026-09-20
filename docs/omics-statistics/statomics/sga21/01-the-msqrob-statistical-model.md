---
title: "1. The MSqRob Statistical Model"
course: "StatOmics Sga21"
chapter: 1
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. The MSqRob Statistical Model

## What this covers

This chapter reconstructs the statistical appendix behind the course's proteomics
differential-expression pipeline — the model implemented in the R package **MSqRob**. It answers one
question: given peptide-level intensities measured across many runs, how do you build one model per
protein that (a) shares information across correlated peptides and runs, (b) is not thrown off by a
handful of outlying peptide measurements, and (c) still gives honest p-values when each protein
individually has very few replicates? It assumes the general and mixed linear model — fixed and random
effects, BLUP estimation, and the idea of degrees of freedom from a hat matrix — since the material here
builds a penalized, robustified version of that model rather than introducing it from scratch. Four short
source files make up the supplied appendix; the first survives its PDF conversion only as a numbered
reference list rather than as prose, so the exposition below is built almost entirely from the other
three.

## The peptide-level model, one protein at a time

Mass-spectrometry intensities, once preprocessed, are treated as log-normal, so the analysis works on
log-intensities, which are then approximately normal. For a single protein, following Daly et al. (2008),
each peptide-run intensity is modelled as

$$y_{pr} = \boldsymbol{x}_{pr}\boldsymbol{\beta} + \beta_p^{\text{peptide}} + u_r^{\text{run}} + \varepsilon_{pr}.$$

Here $y_{pr}$ is the log-intensity of peptide $p$ in run $r$; $\boldsymbol{x}_{pr}$ is the row of
covariates of interest (treatment, condition, and so on) with fixed-effect vector $\boldsymbol\beta$
covering $G$ covariates and $M = \sum_g M_g$ parameters in total; $\beta_p^{\text{peptide}}$ is a
peptide-specific fixed shift, needed because different peptides from the same protein ionize and get
detected with different efficiency; $u_r^{\text{run}} \sim \mathrm N(0,\sigma_u^2)$ is a random run effect
that absorbs the correlation among every peptide measured together in the same run; and
$\varepsilon_{pr}\sim \mathrm N(0,\sigma^2)$ is left-over noise.

This model is fit separately for every protein, using only that protein's own peptides. That is the root
of the two problems the rest of the chapter exists to fix: with only a handful of peptides and runs per
protein, the peptide and covariate effects are estimated on very little data, and the residual variance
$\hat\sigma^2$ is itself a noisy quantity.

## Ridge regression as a prior on the fixed effects

The number of fixed-effect parameters — one shift per peptide, plus the covariates of interest — can be
large relative to how many observations a single protein contributes. The fix is the classical link
between ridge regression and mixed models: instead of estimating a coefficient freely, give it a Gaussian
prior centred at zero, and estimating under that prior turns out to be exactly the same computation as
ridge-penalizing the coefficient.

Concretely, except for the intercept $\beta_0$, every parameter belonging to covariate group $g$ is given
a prior $\beta_{m_g}^g \sim \mathrm N(0, \sigma^2/\lambda_g)$, and every peptide effect is given
$\beta_p^{\text{peptide}} \sim \mathrm N(0,\sigma^2/\lambda_{\text{peptide}})$. Larger $\lambda$ means a
tighter prior and hence stronger shrinkage toward zero — exactly the role a ridge penalty plays. Stacking
the fixed effects, peptide effects and run effects into one vector, the resulting best linear unbiased
predictor (BLUP) has closed form

$$\begin{bmatrix} \hat{\boldsymbol{\beta}} \\ \hat{\boldsymbol{\beta}}^{\text{peptide}} \\ \hat{\boldsymbol{u}}^{\text{run}} \end{bmatrix} = (\boldsymbol{C}^{\mathrm{T}}\boldsymbol{C} + \boldsymbol{B})^{-1} \boldsymbol{C}^{\mathrm{T}}\boldsymbol{y},$$

where $\boldsymbol C$ stacks, for every peptide-run observation, the covariate row $\boldsymbol x_{pr}$
together with one-hot dummies for that peptide and that run, and $\boldsymbol B$ is a diagonal matrix of
penalties: $0$ for the intercept, $\lambda_g$ for each covariate parameter, $\lambda_{\text{peptide}}$ for
each peptide dummy, and — for the run dummies — the variance ratio $\hat\sigma_u^2/\hat\sigma^2$. That last
entry is the same idea wearing its original clothes: a random effect *is* a ridge-penalized fixed effect,
with the penalty set by how much variance is attributed to the random-effect distribution versus the
residual.

The point of routing shrinkage through the mixed-model machinery rather than writing a separate ridge
solver is that software for fitting mixed models can then be reused directly to fit a penalized
regression. (The appendix points to "section 4.2.4" for the derivation of that equivalence; that section
was not part of the supplied material, so only the applied result — the BLUP formula above — is used
here.)

## Robustifying against outlying peptides

Shrinkage does not protect against a genuinely bad peptide measurement — one that is misidentified, that
ionizes poorly, or that is contaminated by a co-eluting species. For that, the appendix uses weighted
maximum likelihood with Huber weights, following Zhou (2009): maximize

$$\sum_{j=1}^J w_j\, l(y_j,\boldsymbol\beta,\boldsymbol u)$$

over all $J$ individual peptide-run observations, each carrying its own weight $w_j$. This weighted
log-likelihood is solved by alternating two steps: fit the mixed model with the weights held fixed, then
recompute every weight from that fit's residuals — scaled by the residual standard deviation — using
Huber's weight function, and repeat until the weights and the estimates stop changing.

<figure>
<svg viewBox="0 0 380 260" role="img" aria-label="The iteratively reweighted fitting loop: fit the mixed model, recompute Huber weights from the residuals, and repeat until convergence.">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="30" y="20" width="220" height="55" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="140" y="43" text-anchor="middle" font-size="12" fill="currentColor">Fit mixed model</text>
  <text x="140" y="60" text-anchor="middle" font-size="12" fill="currentColor">with weights held fixed</text>

  <rect x="30" y="150" width="220" height="55" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="140" y="173" text-anchor="middle" font-size="12" fill="currentColor">Recompute weights: Huber</text>
  <text x="140" y="190" text-anchor="middle" font-size="12" fill="currentColor">function of scaled residuals</text>

  <line x1="140" y1="75" x2="140" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 250 195 C 330 195, 330 45, 250 55" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="300" y="125" text-anchor="middle" font-size="11" fill="currentColor">repeat</text>

  <line x1="30" y1="230" x2="10" y2="230" stroke="none"/>
  <text x="140" y="235" text-anchor="middle" font-size="12" fill="currentColor">until weights and estimates stop changing</text>
</svg>
<figcaption>The two steps of the robust fit alternate — model fit, then reweight by residual size — until
convergence; the final iterate is the weighted BLUP below.</figcaption>
</figure>

Once the loop has converged, the weighted BLUP is the same formula as before, with a diagonal weight
matrix inserted:

$$\begin{bmatrix} \hat{\boldsymbol{\beta}} \\ \hat{\boldsymbol{\beta}}^{\text{peptide}} \\ \hat{\boldsymbol{u}}^{\text{run}} \end{bmatrix} = (\boldsymbol{C}^{\mathrm{T}}\boldsymbol{W}\boldsymbol{C} + \boldsymbol{B})^{-1} \boldsymbol{C}^{\mathrm{T}}\boldsymbol{W}\boldsymbol{y}, \qquad \boldsymbol W = \mathrm{diag}(w_1,\dots,w_J).$$

The reason to reweight rather than, say, discard outlying peptides outright: Zhou (2009) shows the
weighted estimator has better bias and efficiency than the unweighted one whenever some observations
really are outliers, while costing nothing when the model is correctly specified and there are no
outliers at all — it has the same asymptotic efficiency there. Down-weighting is therefore a strictly
safer default than not weighting. The appendix also notes that the identical Huber-weighting idea is used
to robustify the negative binomial model in the RNA-seq package edgeR — the same down-weight-and-refit
trick recurring on the count-data side of the course.

## Empirical Bayes variance shrinkage and the moderated t-test

A problem generic to high-throughput data remains even after a robust fit: every protein $i$ has its own
noise variance $\sigma_i^2$, estimated from only that protein's peptides and runs, so the individual
estimates $\hat\sigma_i^2$ are themselves noisy. Some proteins will look artificially "quiet" — a tiny
estimated variance purely by chance — and get implausibly small p-values as a result. The fix borrowed
here is limma's empirical Bayes variance estimation (the appendix points to "section 4.2.2" for the
account of limma itself, which is not part of the supplied material).

limma assumes a prior, shared across all $I$ proteins, on each protein's precision:

$$\frac{1}{\sigma_i^2} \sim \frac{1}{d_0\sigma_0^2}\chi^2_{d_0},$$

with $\sigma_0^2$ a prior variance and $d_0$ controlling how tightly variances are assumed to cluster
around it. Combining a protein's own estimate $\hat\sigma_i^2$ (based on $d_i$ degrees of freedom) with
that prior gives the posterior, moderated standard deviation

$$\tilde s_i = \sqrt{\frac{d_i\hat\sigma_i^2 + d_0\hat\sigma_0^2}{d_i+d_0}}$$ —

a weighted average of the protein's own variance and the shared prior variance, weighted by their
respective degrees of freedom. A protein with little usable data (small $d_i$) is pulled hard toward the
common $\sigma_0^2$; a protein with plenty of data is barely moved.

Plugging $\tilde s_i$ in for the raw estimate in the usual standard-error formula for a coefficient
$\hat\beta_{m_g}^g$ (dropping the protein index $i$ for readability):

$$\tilde\sigma_{\hat\beta_{m_g}^g} = \tilde s\sqrt{(\boldsymbol C^{\mathrm T}\boldsymbol W\boldsymbol C + \boldsymbol B)^{-1}_{m_g,m_g}},$$

using the $m_g$-th diagonal entry of the same penalized, weighted normal-equations matrix that produced
the point estimate. This supports a moderated t-test,

$$\tilde t_{im_g} = \frac{\hat\beta_{im_g}^g}{\tilde\sigma_{\hat\beta_{im_g}^g}},$$

referred to a t-distribution not with the protein's own $d_i$ degrees of freedom, but with $d_i + d_0$ —
borrowing extra degrees of freedom from the shared prior, exactly as the variance estimate itself borrowed
strength from the other proteins.

$d_i$ is not simply "number of observations minus number of parameters" in the ordinary least-squares
sense, because both the ridge shrinkage and the reweighting change how many parameters are "really" being
fit. Instead it is read off the hat matrix

$$\boldsymbol H = \boldsymbol C(\boldsymbol C^{\mathrm T}\boldsymbol W\boldsymbol C+\boldsymbol B)^{-1}\boldsymbol C^{\mathrm T}\boldsymbol W, \qquad d_i = J - \mathrm{tr}(\boldsymbol H).$$

The trace of $\boldsymbol H$ is the effective number of parameters the penalized, weighted fit actually
uses — smaller than the raw parameter count, because shrinkage "spends" less than one full parameter per
peptide or run dummy — and the degrees of freedom left over for estimating variance is whatever
observations remain.

## Putting it together: what MSqRob fits

The implementation builds on the R package lme4 for the mixed-model machinery. Shrinkage on the fixed
effects is obtained exactly as described above: the parameters that should be shrunk are encoded as
random effects rather than fixed ones, so `lmer` estimates them with the penalty already built in. Around
that sits the outer loop from the robustness section: after each `lmer` fit, Huber weights are computed
from the residuals scaled by the residual standard deviation, and passed back into `lmer`'s weights
argument for the next fit, repeating until convergence.

So the model that gets fit to a real dataset is three ideas nested inside one loop: mixed-model machinery
supplies the ridge shrinkage "for free," an outer reweighting loop supplies robustness to outlying
peptides, and the empirical Bayes step is applied only afterward, at the inference stage, once the
(robust, shrunk) point estimate is already fixed.

## Sources

- **Ridge regression as a mixed model** — `02-ridge-regression.md`, the peptide-level model, the prior on
  fixed effects, and the BLUP formula with matrices $\boldsymbol C$ and $\boldsymbol B$. Cites Daly et al.
  (2008) for the base model and points to the course's own "section 4.2.4" for the ridge/mixed-model
  equivalence, which is not part of the supplied material.
- **Robust M-estimation** — `03-robust-regression-with-m-estimation.md`, the weighted log-likelihood, the
  fit/reweight loop, and the weighted BLUP formula. Cites Zhou (2009) for the bias/efficiency result and
  the parallel with edgeR's robust weighting for RNA-seq count data.
- **Empirical Bayes variance estimation and implementation** —
  `04-empirical-bayes-variance-estimation.md`, the limma-style prior on $1/\sigma_i^2$, the moderated
  standard deviation and t-test, the hat-matrix degrees of freedom, and the description of MSqRob's
  lme4-based implementation. Points to the course's own "section 4.2.2" on limma, not part of the supplied
  material. Its reference list (in the file) cites Daly et al. (2008), Zhou (2009), Zhou, Lindsay &
  Robinson (2014) for edgeR's robust weighting, and Bates et al. for lme4.
- **`01-introduction.md`** — headed "Introduction," but the text that survived PDF conversion is only a
  numbered reference list (entries 26–50: Huber's 1964 robust-location paper, the MaxQuant and MaxLFQ
  papers, limma, Benjamini–Hochberg, and others) followed by a bare "9.1.9. Appendix" heading. No
  introductory prose survived the conversion, so none is reconstructed here; the file is not otherwise
  used.

All four files carry the note that they were reconstructed by a model from a PDF with no usable text
layer, and that every equation in them is unverified against the original — the equations above should be
read with that caveat, and checked against
[the original PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf)
before being relied on.

---

[Contents](index.md) · [2. From Peptides to Differential Expression →](02-from-peptides-to-differential-expression.md)
