---
title: "Thomas, Popović & Grima, 2014 — Phenotypic switching in gene regulatory networks"
paper: "summary"
source: "https://doi.org/10.1073/pnas.1400049111"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Thomas P, Popović N, Grima R (2014). Phenotypic switching in gene regulatory networks. Proceedings of the National Academy of Sciences, 111(19), 6994-6999. ([original](https://doi.org/10.1073/pnas.1400049111)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Phenotypic switching in gene regulatory networks

## What this covers
This paper, in computational systems biology, asks how the stochastic distribution of gene
expression products (mRNA, protein) across a population of genetically identical cells can be
computed in closed form for gene regulatory networks whose promoters switch slowly between
multiple states, even when the corresponding deterministic (mean-field) model has only a single
stable state.

## The question
Isogenic cell populations often show multimodal (e.g. bimodal) protein-abundance distributions
- distinct subpopulations corresponding to different phenotypes - even for circuits whose
deterministic models predict a single steady state. The chemical master
equation (CME) can in principle produce such multimodal distributions, but it is analytically
solvable only for a handful of very simple network architectures. The standard linear noise approximation (LNA), which approximates the CME by a single
multivariate Gaussian, cannot reproduce multimodality by construction, since its assumption that
every species is abundant fails for promoters, which exist in only one or two copies per cell.
The authors want a general, closed-form method predicting when and how strongly a network
produces multimodal expression, without solving or simulating the full CME each time.

## The approach
The key move is to treat the discrete promoter states exactly, while invoking a Gaussian
(LNA-type) approximation only for the gene-product species, conditional on each promoter state.
This is justified when promoter switching is much slower than the reactions that make and degrade
gene products, so that, conditional on a given promoter configuration, gene products reach a
quasi-steady Gaussian distribution before the promoter switches again. The overall distribution is
then a weighted mixture of Gaussian components, one per promoter state, with weights equal to the
stationary probability of that state. The authors derive closed-form expressions for all three
ingredients: the mixture weights, obtained from a reduced Markov chain over promoter states after
averaging the fast conditional fluctuations out of the CME; the mean (mode) of each Gaussian
component, from a set of conditional deterministic rate equations; and its covariance, from a
linear matrix equation analogous to the standard LNA fluctuation-dissipation relation. They also
give an interpolation formula bridging this "conditional LNA," valid for slow promoters, and the
conventional LNA, valid for fast promoters, to cover the intermediate regime where switching and
gene-product timescales are comparable.

## What it found
For a single two-state promoter, the conditional LNA reproduces the known bimodal protein
distribution, and the interpolation formula tracks simulation across the full range of
switching-to-expression timescale ratios, including the intermediate regime neither limit covers. Applied to a two-gene mutually repressive (toggle-switch) motif with both
transcriptional and translational control, the method shows that translational feedback alone
cannot change which promoter is multimodal and yields at most two protein modes, whereas combining
transcriptional and translational ("global") regulation generates up to four coexisting modes in
the same species - a tetramodal distribution not produced by either regulation type alone - and
that the mutual information between the two protein species, used as a measure of regulation
strength, peaks (around 2 bits in their example) when transcriptional and post-translational
regulation are tuned jointly rather than either alone. In a model of a genetic oscillator (an
ultrasensitive kinase cascade driven by a slowly switching promoter under irradiation-induced DNA
damage and repair), slow promoter switching produces birhythmicity - two distinct oscillation
frequencies in an upstream kinase that are not present in the promoter's own switching signal,
visible in the power spectrum though the stationary distribution of the downstream output kinase
shows only a single frequency because of near-complete depletion in the off state. In a
hypothetical induction experiment with a non-cooperative, non-bistable negative-feedback circuit,
ramping a transcription factor up versus down produces hysteresis in the resulting transient
bimodality even though the deterministic system is not bistable; the degree of hysteresis is given
in closed form by the ratio of the induction ramp timescale to the promoter switching timescale,
$\tau_r/\tau_f = 1 + [\mathrm{TF}]/K_{eq}$, identifying a specific timescale window in which
transient bimodality and hysteresis should be observable experimentally.

## Limits and context
The authors emphasise that none of these effects require deterministic multistability - they
present slow stochastic promoter switching as an alternative mechanism to the usual assumption
that switching, oscillatory, or hysteretic phenotypes need bistability or highly cooperative,
ultrasensitive interactions. They describe the conditional LNA as, to their knowledge, the first general method giving
closed-form gene-product distributions for this network class, filling a gap left by prior
approaches (factorization methods for specific promoter models, or conditional-moment methods)
that need strict timescale separation, become intractable with bimolecular interactions, or stop
short of full distributions for abundant species. They flag two explicit limitations of their own method: the Gaussian (LNA) component can
become inaccurate when some gene products of interest are present at very low copy number, even
though the promoter-level treatment itself is exact; and the framework is gene-centric and does
not incorporate cell growth and division, so it cannot capture phenotypic variability that arises
from those processes.

## Citation
Thomas P, Popović N, Grima R (2014). Phenotypic switching in gene regulatory networks.
*Proceedings of the National Academy of Sciences*, 111(19), 6994-6999.
https://doi.org/10.1073/pnas.1400049111. Open access via PNAS; cached in the
knowledge-base-library paper collection.
