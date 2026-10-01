---
title: "9. Reading: Adaptive Rejection Sampling for Gibbs Sampling"
course: "Berkeley Stat 243"
chapter: 9
source: "https://doi.org/10.2307/2347565"
licence: "summary only \u2014 the paper is not reproduced"
written: "2026-10-01"
---

> **Summary of a paper.** Gilks, W. R. and Wild, P. (1992), "Adaptive Rejection Sampling for Gibbs Sampling", Journal of the Royal Statistical Society. Series C (Applied Statistics), 41(2), 337-348. ([original](https://doi.org/10.2307/2347565)). The paper is © its rights holder and is not reproduced here: this is a short account of it in our own words, standing in for it in the reading of Berkeley Stat 243.

# 9. Reading: Adaptive Rejection Sampling for Gibbs Sampling

## What this covers

This paper introduces adaptive rejection sampling (ARS), a black-box method for drawing
independent samples from any univariate log-concave probability density. It was developed to make
Gibbs sampling practical when the full conditional distributions needed at each step have no
standard, closed form.

## The question

Gibbs sampling updates each parameter in turn by drawing from its full conditional distribution,
and in a model of any size this means thousands of such draws over a run. When a Bayesian model is
not fully conjugate, a full conditional is a product of several "model conditional" terms and in
general has no recognisable distributional form, so it cannot simply be sampled from directly. The
authors needed an efficient way to draw from exactly such conditionals, which arose for them in a
Gibbs sampling analysis of flow cytometry data on monoclonal antibody reactivity against a cell
surface antigen (NCAM), fitted with a non-conjugate hierarchical model. A general rejection sampler
would work but typically needs an envelope function built around the density's mode, found by
numerical optimisation for every one of those thousands of draws — expensive when the density
itself is costly to evaluate.

## The approach

Standard rejection sampling sandwiches the target density $f(x)$ between an envelope $g_u(x)$,
sampled from directly, and optionally a cheaper squeezing function $g_l(x)$ that lets most proposals
be accepted or rejected without evaluating $f(x)$ at all. Building a good envelope ordinarily needs
the mode. ARS instead exploits log-concavity: if $h(x) = \ln g(x)$ is concave, then tangent lines
to $h$ at a current set of evaluated points form a piecewise-linear *upper hull*, whose exponential
is a valid piecewise-exponential envelope that needs no mode-finding; chords between the same points
form a *lower hull* giving the squeezing function. Table 2 shows most commonly used densities are
log-concave in their natural or a transformed parameterisation, so the assumption is not
restrictive in practice.

The method is adaptive in a specific sense: whenever a proposed point is rejected (or passes only
the more expensive rejection test), $h$ and $h'$ have been evaluated there, so that point is folded
into the set of abscissae and both hulls are rebuilt, tightening the envelope around the true
density. The paper proves this still yields exact, independent draws from $f(x)$ (Section 2.3), and
argues informally (Section 2.4) that new evaluations concentrate where the envelope and squeeze
disagree most, so the bounds improve efficiently. For Gibbs sampling specifically, Section 3 shows
that if every model-conditional term contributing to a full conditional is log-concave in the
parameter being updated, the full conditional's log is a sum of concave terms and so is itself
concave — meaning ARS can be applied to it directly, term-product and all, without ever deriving its
form. Multivariate full conditionals are handled by applying univariate ARS one component at a
time.

## What it found

For the standard normal density, ARS needs only a handful of evaluations of $h$ and $h'$ per sampled
point — typically three to five — almost regardless of how the starting abscissae are chosen, and
two starting points were found sufficient in general (Table 1). Across densities more broadly, the
number of evaluations needed to draw $n$ points grows roughly as $n^{1/3}$.

Applied to the antibody data — 13 antibodies tested against 15 cell types, modelled through a
logistic-based hierarchical model with location and precision parameters and corresponding
hyperpriors (equations 7–13) — the full conditionals for the location parameters and the precision
$\tau_y$ have no closed form but are log-concave, so ARS was used for all of them inside 1000 Gibbs
iterations. Only about three evaluations of $h$ were needed per draw on average, with more than four
required in only about 5% of iterations, and the sampler converged within ten iterations. The
resulting posterior summaries (Table 3) pointed to substantial variability across cell types in
NCAM expression but comparatively little variability in antibody affinity for the antigen, with
some evidence that one antibody (antibody 12) has distinctly lower affinity.

## Limits and context

ARS applies only where the domain is connected and the log-density is continuous, differentiable
and concave throughout — not every density of interest qualifies, though the authors argue the
common ones typically do. They note that a real implementation needs care to avoid numerical
problems for densities that are extremely concentrated or skewed, and mention a Fortran program
(available on request from the authors) that handles such cases and extends straightforwardly to
truncated distributions. They position the method against Devroye (1986), which contains related
piecewise-exponential envelope constructions but none that are adaptive in this sense, and against
contemporaneous alternatives such as rejection sampling from a fixed normal envelope centred at the
conditional's mode, which ARS is intended to avoid needing.

## Sources

- Full text read: `sources/berkeley-stat243/fall-2024/project/gilks.etal.1992.pdf`

## Citation

Gilks, W. R. and Wild, P. (1992), "Adaptive Rejection Sampling for Gibbs Sampling", Journal of the
Royal Statistical Society. Series C (Applied Statistics), 41(2), 337–348.
DOI: [10.2307/2347565](https://doi.org/10.2307/2347565). Rights holder: the Royal Statistical
Society; not openly licensed, so this record is a summary only, standing in for the paper.

---

[← 8. Reading: Infovis and Statistical Graphics](08-reading-infovis-and-statistical-graphics.md) · [Contents](index.md) · [10. Installing Git →](10-installing-git.md)
