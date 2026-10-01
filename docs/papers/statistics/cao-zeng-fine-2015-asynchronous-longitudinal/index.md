---
title: "Cao, Zeng & Fine 2015 — Regression analysis of sparse asynchronous longitudinal data"
paper: "summary"
source: "https://doi.org/10.1111/rssb.12086"
licence: "© Royal Statistical Society — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Cao, H., Zeng, D. and Fine, J. P. (2015). Regression analysis of sparse asynchronous longitudinal data. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 77(4), 755–776. ([original](https://doi.org/10.1111/rssb.12086)). Rights: © Royal Statistical Society — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Regression analysis of sparse asynchronous longitudinal data

## What this covers

This paper is from biostatistics, and it answers a narrow but practical question: how do you fit a
regression model to longitudinal data when the response and the covariates are never measured at
the same time points within a subject.

## The question

Longitudinal regression methods almost all assume "synchronous" data: the response $Y(t)$ and the
covariates $X(t)$ for a subject are observed together, at the same visit. In practice this often
fails. In the HIV cohort the authors use as a motivating example, viral load and CD4 cell count were
measured at separate laboratory visits on different days, so for any given patient there is no time
point at which both are actually recorded. The common workaround is to carry the most recently
observed covariate value forward to match each response time ("last value carried forward," LVCF)
and then apply ordinary synchronous methods. The authors show this is not just a minor
approximation: in their own simulations and in the HIV data, LVCF is biased enough to miss, or even
reverse the sign of, an association that other methods confirm is present. The paper sets out to
build an estimator that uses the asynchronous observations directly, without this substitution, and
to work out what performance is actually achievable once synchrony is given up.

## The approach

The regression target is a generalized linear model relating the conditional mean of $Y(t)$ given
$X(t)$ through a known link function, with a coefficient that is either constant over time or itself
a smooth function $\beta(t)$. Because no observation of $X$ coincides exactly with an observation of
$Y$, the authors replace the usual (synchronous) estimating equation with a kernel-weighted version:
every pairing of a response observation and a covariate observation from the same subject
contributes to the estimating equation, weighted by a kernel that downweights pairs whose
observation times are far apart. For the time-varying coefficient, two kernels are used, one
weighting the response's distance from the target time point and one weighting the covariate's
distance from it. The observation process itself (which times the response and covariates happen to
be recorded at) is formalised as a bivariate counting process, which lets the authors state precise
conditions — on how often response and covariate times nearly coincide, and on the smoothness of the
covariate process — under which the resulting estimating equations behave well. The estimating
equations are solved by standard Newton–Raphson, so the computational side is no harder than fitting
an ordinary generalized linear model once the kernel weights are fixed. Because standard
cross-validation does not apply to non-synchronous data, the paper also proposes its own
data-adaptive bandwidth selection procedure, based on splitting the sample and estimating the bias
and variance of the estimator as functions of the bandwidth.

## What it found

For the time-invariant coefficient, the estimator is consistent and asymptotically normal, but the
achievable rate of convergence is slower than the usual parametric $n^{1/2}$ rate that synchronous
data gives: convergence is of order $o(n^{2/5})$, driven by the need for the bandwidth to shrink more
slowly than $n^{-1/2}$ to control bias while not vanishing too fast for the variance. For the
time-varying coefficient $\beta(t)$, estimated pointwise at a fixed time, the rate is even slower,
$o(n^{1/3})$, against the faster nonparametric rate obtainable with synchronous data. Simulation
studies spanning sample sizes from 100 to 900 subjects, for both linear and logistic link functions,
show that bias is well controlled, model-based and empirical standard errors agree, and confidence
interval coverage approaches the nominal 95% level as sample size grows, including with the
automatic bandwidth selector. Over the same simulations, the LVCF approach shows a bias in the
coefficient estimate that does not shrink as the sample size grows, so its confidence interval
coverage actually worsens with more data — the authors report cases where coverage collapses to 0%.
Applied to the HIV cohort (190 patients), the proposed method recovers a negative association
between CD4 count and viral load across a range of bandwidths, consistent with prior clinical
findings, whereas LVCF applied to the same data gives a weak association in the wrong (positive)
direction. Fitting the time-varying version of the model shows the negative association is roughly
stable over the follow-up period, with little evidence favouring the more flexible model over the
simpler constant-coefficient one.

## Limits and context

The authors are explicit that the slower convergence rates are not an artefact of their particular
estimator but reflect a genuine information limit of sparse asynchronous data relative to
synchronous data: because response and covariate times are "never 'perfectly' matched," the
estimator's variance depends on how quickly the observation times for the two processes accumulate
near each other, which is inherently a weaker signal than observing both simultaneously. The method
requires the covariate process's covariance structure to be twice continuously differentiable, which
rules out some processes with independent increments (such as Poisson processes or Brownian motion)
without further modification, and the paper notes that relaxing this assumption would introduce
additional bias and require new theoretical work it does not carry out. The pointwise confidence
intervals for the time-varying coefficient are not extended to simultaneous bands or formal
hypothesis tests across time, which the authors flag as a direction for future work. They also do
not treat models where some coefficients are time-invariant and others time-varying together
(partial linear models), and they leave open whether global (basis-function or spline) estimation
approaches could achieve efficiency gains over their local, kernel-based method, given the already
slow rates of convergence involved.

## Citation

Cao, H., Zeng, D. and Fine, J. P. (2015). Regression analysis of sparse asynchronous longitudinal
data. *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, 77(4),
755–776. DOI: [10.1111/rssb.12086](https://doi.org/10.1111/rssb.12086). Available via Wiley Online
Library / JSTOR, or through institutional access; a copy is held in this library's source cache
under `berkeley-stat243/stat243-fall-2022/ps/cao_etal_2015.pdf`.
