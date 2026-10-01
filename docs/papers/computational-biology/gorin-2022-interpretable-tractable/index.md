---
title: "Gorin et al. 2022 — Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments"
paper: "summary"
source: "https://doi.org/10.1038/s41467-022-34857-7"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Gorin, G., Vastola, J. J., Fang, M., & Pachter, L. (2022). Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments. Nature Communications, 13, 7620. https://doi.org/10.1038/s41467-022-34857-7 ([original](https://doi.org/10.1038/s41467-022-34857-7)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments

**[Read the full text](full-text/index.md)**

## What this covers

How much the fine biophysical detail of transcription — whether a gene's transcription rate
varies because of DNA mechanics or because of a fluctuating regulator — leaves a signature in
single-cell RNA count data, and how to design models that are detailed enough to test that against
real data while still being mathematically solvable. The question sits at the intersection of
stochastic modelling of gene expression and the design of single-cell transcriptomic experiments.

## The question

Single-cell RNA counts vary because of a mix of processes — DNA supercoiling, regulator binding,
RNA processing — and it is unclear how much can be learned about which of these processes is
actually driving a gene from counts alone. The field's usual descriptive, phenomenological fits
(e.g. negative-binomial-like distributions) summarize data without making a specific mechanistic
claim, while detailed biophysical models of transcription are mechanistic but usually too complex
to analyze and too underdetermined to let two competing hypotheses be told apart from data. The
authors wanted models that are simultaneously **interpretable** (parameters map onto concrete
biophysical mechanisms) and **tractable** (fully analyzable), so that one can work out in advance
which experiment would best discriminate between two specific hypotheses about transcription,
rather than fitting a generic distribution after the fact.

## The approach

The paper builds models in which a continuous, randomly fluctuating transcription rate $K(t)$
drives a standard discrete birth-death process of nascent (unspliced) and mature (spliced) RNA —
an SDE (for the rate) coupled to a CME (for the discrete molecule counts). $K(t)$ is modelled as a
one-dimensional mean-reverting stochastic process whose stationary distribution is chosen to be a
gamma distribution, which is what makes negative-binomial-like RNA counts fall out naturally. Two
specific, biologically motivated choices of driving process are compared: a gamma
Ornstein–Uhlenbeck (Γ-OU) process, standing in for transcription rate variation caused by the
mechanical/supercoiling state of DNA, and a Cox–Ingersoll–Ross (CIR) process, standing in for
variation driven by fluctuations in the copy number of an abundant regulator. Both reduce to
simpler, well-known models (the constitutive model and the "mixture" model) in limiting regimes,
which lets the new framework be checked against, and shown to unify, results already in the
literature. The authors derive exact analytical solutions for the joint nascent/mature RNA
distributions, moments and autocorrelation functions of both models (using an SDE–CME isomorphism
for the Γ-OU case and a stochastic path-integral method that generalizes further), simulate both
processes to validate the analytics, and then use Bayes factors and likelihood-ratio model
selection to ask, first in simulation and then on real data, whether the two models can actually be
told apart.

## What it found

Despite their different biological motivations, the Γ-OU and CIR models have **identical** means,
variances, covariances and autocorrelation functions for nascent and mature RNA — so ordinary
summary statistics, and any technology that only reports population averages (e.g. bulk RNA-seq),
cannot in principle distinguish them. Comparing full joint (nascent + mature) count distributions
does distinguish the models: in simulation, around 1,000 cells were enough to separate them over
most of parameter space using a log Bayes factor criterion, and using the joint distribution rather
than either marginal alone improved distinguishability by roughly an order of magnitude. A
parameter-recovery experiment showed the biophysically meaningful parameters (the mean-reversion
rate $\kappa$ and gain $\theta$) are fairly identifiable from simulated data when the distribution
is overdispersed, though not when it is close to Poisson-like. Applied to real single-cell
transcriptomic data from glutamatergic neurons of four mice (31,649 genes after pseudoalignment),
a filtering step selected 80 genes for full model fitting; 73 of these converged, and their
likelihood-ratio model assignments (Γ-OU-like, CIR-like, or mixture-like) were consistent across
the four biological replicates and broadly consistent with a slower, fully Bayesian fit done for a
subset of 12 genes. This is presented as a proof of principle that existing single-cell data can
be rich enough to support Bayesian discrimination between distinct noise-generating mechanisms,
with specific candidate genes identified for each regime.

## Limits and context

The real-data analysis is explicitly a proof of principle, not a mechanistic claim: the authors
note that interpreting the biochemical meaning of specific gene assignments is difficult without
also accounting for technical noise and additional downstream RNA processing, which the models
presented here omit (though the supplement discusses extensions). Of the 80 filtered genes, 7 were
discarded for having an absolute log-likelihood ratio above 150, which the authors took as a sign
of failing to converge to a satisfactory optimum rather than as a genuine model comparison.
The paper is also explicit that it does not implement the full "rational experiment design" closed
loop it motivates in the introduction — it builds the mathematical and computational foundation for
that loop (solving the models, showing which kind of data distinguishes them) without running the
follow-up wet-lab experiment. The slow-reversion ("mixture") limit is flagged as attractive but
potentially biologically implausible, since matching it would require a driving process with an
autocorrelation time of weeks given typical mRNA lifetimes. Orthogonal, targeted experiments are
described as necessary to confirm whether the models assigned to specific genes actually
correspond to the live-cell mechanism, rather than being just the better-fitting of two candidates.

## Citation

Gorin, G., Vastola, J. J., Fang, M., & Pachter, L. (2022). Interpretable and tractable models of
transcriptional noise for the rational design of single-molecule quantification experiments.
*Nature Communications*, 13, 7620. https://doi.org/10.1038/s41467-022-34857-7
