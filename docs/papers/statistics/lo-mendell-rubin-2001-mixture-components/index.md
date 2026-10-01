---
title: "Lo, Mendell & Rubin 2001 — Testing the number of components in a normal mixture"
paper: "summary"
source: "https://doi.org/10.1093/biomet/88.3.767"
licence: "© Biometrika Trust — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Lo, Y., Mendell, N. R., & Rubin, D. B. (2001). Testing the number of components in a normal mixture. Biometrika, 88(3), 767-778. ([original](https://doi.org/10.1093/biomet/88.3.767)). Rights: © Biometrika Trust — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Testing the number of components in a normal mixture

## What this covers

A statistics paper on how to decide how many components belong in a normal mixture model — a
recurring question wherever a population is modelled as a blend of several normal subgroups, such
as clustering, classification and latent-class analysis.

## The question

A finite normal mixture represents data as drawn from a weighted blend of several normal
distributions, but in practice the number of components $k$ is usually not known and must be
decided from the data. The natural approach is a likelihood ratio test of a $k_0$-component
mixture against a $k_1$-component mixture, but the authors point out that the standard
chi-squared theory behind such tests breaks down for mixtures: under the null hypothesis the
mixing proportions of the extra components sit on the boundary of the parameter space, and the
parameters needed to describe where those components would be are not identifiable. Several
earlier authors had shown pieces of an asymptotic theory for special cases, but a general,
workable null distribution for the likelihood ratio statistic in this setting was still missing,
and that gap is what this paper sets out to close.

## The approach

The authors build on a theorem of Vuong (1989), which supplies an asymptotic distribution for a
likelihood ratio statistic comparing two possibly misspecified, non-nested or nested models,
using the Kullback-Leibler information criterion as the yardstick for which model is closer to
the truth. They extend that theorem to the specific case of a $k_0$-component normal mixture
nested inside a $k_1$-component normal mixture. The key result is that, under a set of regularity
conditions carried over from Vuong's framework, twice the log-likelihood ratio statistic
converges in distribution to a weighted sum of independent chi-squared random variables with one
degree of freedom each, rather than to a single chi-squared distribution with a fixed number of
degrees of freedom. The weights are eigenvalues of a matrix built from the information and
cross-information matrices of the two competing models, and the resulting distribution function
can be computed numerically by inverting the relevant characteristic function. Because this exact
distribution converges only slowly in finite samples, the authors propose an ad hoc correction
that rescales the likelihood ratio statistic by a factor depending on the degrees-of-freedom
difference between the two models and the sample size, intended to speed convergence toward the
asymptotic distribution. They test the theory and the correction through simulation: generating
samples under models with one, two or three components and computing both the raw and the
corrected test statistic's simulated significance levels and power across a range of sample
sizes, mixing proportions and degrees of separation between the components.

## What it found

The simulations show that the raw (unadjusted) likelihood ratio statistic approaches its
theoretical asymptotic null distribution only slowly, so that nominal significance levels (for
example 0.05) are not well matched by the actual rejection rate at small or moderate sample
sizes. The proposed adjustment brings the simulated significance levels substantially closer to
the nominal levels across the sample sizes examined, for both a single-normal-versus-two-component
test and a two-component-versus-three-component test. Power is strongly governed by how well
separated the mixture components are: when components are well separated, reasonable power is
achieved with sample sizes around 100 or more, while power is low when the components are close
together or the sample is small, regardless of which mixing proportion is used. For the
two-versus-three-component comparison, both the spacing between the first and second components
and the spacing between the second and third govern power, and the adjusted test needs larger
spacings or larger samples to reach comparable power to the simpler single-versus-two-component
case.

## Limits and context

The authors are explicit that their asymptotic result requires no explicit restriction on the
parameter space other than what is needed for identifiability, but they note this generality has a
cost: when the parameter space is unbounded, the likelihood ratio statistic can diverge to
infinity in probability under the null, so the asymptotic theory given here does not apply without
some restriction (for example bounding the separation between components) once that divergence
is in play. The simulation studies are confined to homoscedastic mixtures, where all components
share a common variance, and the authors flag investigating mixtures with unequal
component variances as a priority for future work, since they expect the rate of convergence to
the limiting distribution to depend on how that case is handled. They also note, without settling
the comparison themselves, that it would be useful to see how their test performs against
alternative approaches such as the parametric bootstrap and Bayesian posterior predictive checks,
and that extending the Vuong-based theorem to other mixture families — gamma, exponential,
binomial or Poisson mixtures — remains open. The empirical correction to the test statistic is
presented as an ad hoc fix justified by its simulated performance, not as something derived from
the asymptotic theory itself.

## Citation

Lo, Y., Mendell, N. R., & Rubin, D. B. (2001). Testing the number of components in a normal
mixture. *Biometrika*, 88(3), 767-778. DOI:
[10.1093/biomet/88.3.767](https://doi.org/10.1093/biomet/88.3.767). Published by Oxford University
Press on behalf of the Biometrika Trust; available via JSTOR.
