---
title: "Grima, Schmidt & Newman 2012 — Steady-state fluctuations of a genetic feedback loop: an exact solution"
paper: "summary"
source: "https://doi.org/10.1063/1.4736721"
licence: "arXiv non-exclusive distribution licence — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** R. Grima, D. R. Schmidt, and T. J. Newman, "Steady-state fluctuations of a genetic feedback loop: an exact solution," Journal of Chemical Physics 137, 035104 (2012). ([original](https://doi.org/10.1063/1.4736721)). Rights: arXiv non-exclusive distribution licence — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Steady-state fluctuations of a genetic feedback loop: an exact solution

## What this covers

How the protein copy number in a single self-regulating gene fluctuates at steady state, treating
the feedback loop as a genuinely non-equilibrium stochastic process rather than an approximation.
It speaks to stochastic gene expression and chemical master-equation theory in systems biology.

## The question

A gene whose own protein product binds its promoter and alters transcription is the simplest
non-trivial regulatory motif, common to metabolism, signalling, somitogenesis and circadian clocks.
As a chemical master equation it has two features that make an exact solution hard: production
depends on whether the promoter is bound or free, which breaks detailed balance, and protein-promoter
binding is a bimolecular (second-order) reaction. Exact master-equation solutions had previously been
found only for networks obeying detailed balance or composed solely of first-order reactions —
conditions real intracellular feedback loops do not meet. A prior paper (Hornos et al., 2005) had
claimed an exact solution for the case where bound and free protein degrade at the same rate, and
several follow-ups used it; the authors set out to solve the general problem (arbitrary bound-protein
degradation rate) and, in doing so, check that earlier claim.

## The approach

The model tracks only the number of free proteins and the promoter's state (bound or unbound),
without explicitly modelling transcription or mRNA. Protein is produced at one rate when the
promoter is unbound and another when bound, free protein degrades at rate $k_f$, bound protein can
independently degrade (at rate $k_b$, returning the promoter to the unbound state), and protein
binds to and unbinds from the promoter at given rates. This becomes a pair of coupled master
equations for the two conditional probability distributions (promoter bound / unbound).

The steady-state equations are solved exactly with the probability generating function method:
eliminating variables in a particular order yields a single second-order ODE for the "promoter
bound" generating function with coefficients linear in its argument. That linearity lets the
equation be transformed into Kummer's equation, whose physically admissible solution is a confluent
hypergeometric function. From this, exact series expressions for both conditional probability
distributions are obtained for arbitrary parameter values, with one singular parameter combination
treated separately. The results are checked against direct numerical solution of the master
equations.

A central part of the approach is a line-by-line re-derivation of the master equation that keeps
track of exactly which molecular process each term represents — in particular how bound-protein
degradation is handled — and this bookkeeping is used to re-examine the master equations underlying
the earlier Hornos et al. solution.

## What it found

An exact, closed-form steady-state solution exists for arbitrary production, degradation, binding
and unbinding rates — the first such solution reported for a gene-regulatory feedback network,
despite broken detailed balance and a bimolecular step. Several special cases reduce to simple
explicit forms, including the detailed-balance limit (equal production rates, no bound-protein
degradation), where the protein distribution is exactly Poisson and the known Hill-function relation
between time spent "off" and mean protein number is recovered.

Away from detailed balance, that Hill relation need not hold: for strong promoter binding, the
off-time fraction versus mean protein number instead takes a piecewise-linear form, unlike the Hill
form predicted by a deterministic (mean-field) version of the same network, which the paper shows
has no bistability. Evaluating the exact solution numerically also shows the steady-state
distribution can be bimodal — peaks near the production rate characteristic of each promoter state
— purely from slow switching between states with sufficiently different production rates, turning
unimodal as switching speeds up. Comparing with the Hornos et al. solution (equal degradation rates)
shows the two disagree; the paper traces this to the earlier master equation implicitly describing
bound-protein degradation as instantaneous rebinding of a free protein to the promoter at a rate
independent of free-protein number — a process the authors argue has no physical realisation.
Numerical comparison of the two master equations shows this produces qualitatively wrong behaviour
(a spurious unimodal-bimodal-unimodal transition) over a range of parameters where bound-protein
degradation is appreciable.

## Limits and context

The generating function for the "promoter unbound" distribution cannot generally be written in
closed form (only as a derivative/integral expression), though the probabilities themselves can
still be obtained explicitly; normalisation in the general case is done numerically. The paper does
not extend its method to feedback by protein dimers or to networks beyond this single-gene motif,
noting such variants have been treated elsewhere with approximate or special-case methods (e.g. a
slow/rapid-switching approximation by Qian et al., which the exact solution here confirms within its
regime). It argues explicitly against the Hornos et al. (2005) solution and its follow-ups for the
equal-degradation-rate case, attributing the disagreement to an unphysical master-equation
formulation rather than a calculational slip. The authors frame their result as a benchmark for
approximate methods (moment closures, system-size expansion) used at low copy numbers with
bimolecular steps, rather than a full account of noise statistics such as the Fano factor, which
they flag as a direction for later work.

## Citation

R. Grima, D. R. Schmidt, and T. J. Newman, "Steady-state fluctuations of a genetic feedback loop: an
exact solution," *Journal of Chemical Physics* 137, 035104 (2012).
https://doi.org/10.1063/1.4736721. Available via the publisher (AIP Publishing) and as arXiv:1206.1571.
