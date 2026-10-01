---
title: "Gorin & Pachter 2021 — Analytical solutions of the chemical master equation with bursty production and isomerization reactions"
paper: "summary"
source: "https://doi.org/10.1101/2021.03.24.436847"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Gennady Gorin and Lior Pachter. "Analytical solutions of the chemical master equation with bursty production and isomerization reactions." bioRxiv preprint, posted 2021-06-30 (originally submitted 2021-03-24). https://doi.org/10.1101/2021.03.24.436847 ([original](https://doi.org/10.1101/2021.03.24.436847)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# Analytical solutions of the chemical master equation with bursty production and isomerization reactions

**[Read the full text](full-text/index.md)**

## What this covers

How splicing — the stepwise, irreversible conversion of a transcript into downstream isoforms —
reshapes the statistics of mRNA counts produced in transcriptional bursts. It belongs to the
chemical master equation (CME) literature in computational biology / stochastic gene expression.

## The question

Single-cell RNA-seq and imaging now routinely report counts of pre-mRNA and mature mRNA together,
and the authors want to use that joint information to infer the biophysical parameters governing
transcription, splicing and degradation. Doing so needs a model whose full time-dependent joint
distribution over all intermediate and terminal transcript species can actually be written down,
for splicing cascades more general than a single linear chain. Prior analytical CME solutions for
bursty transcription covered only a basic nuclear-export/degradation chain, with other solved cases
built ad hoc and hard to generalize. A second, separate question motivates the second half of the
paper: single-cell data shows strong co-expression between genes, and the authors ask how much of
that correlation a simple, physically interpretable multi-gene model can actually produce.

## The approach

The authors model bursty transcription (geometrically-distributed burst sizes, Poisson-timed burst
arrivals) feeding into a splicing network that is any directed acyclic graph (DAG) with a single
source — a path graph (one linear order of intron removal), a tree, or a graph with convergent paths
where order is non-deterministic. Reaching the CME through its probability generating function (PGF),
log-transformed and solved by the method of characteristics, reduces the problem to linear ODEs for
"exponential sum" functions describing each species' dependence on the upstream driving process. They
give a backward recursive algorithm, propagating from terminal (degraded) species up to the source,
that builds these exponential sums for an arbitrary splicing DAG, then obtains the full generating
function by quadrature and the probability mass function by Fourier inversion, at a stated cost of
$O(\mathcal{N}\log\mathcal{N})$ in state-space size. A parallel continuous-state formulation recasts
the system as an SDE for the Poisson intensities and identifies the splicing chain as an iterated
moving-average process, an independent cross-check via known SDE properties. They establish
existence and finiteness of all moments and cross-moments, and show the marginals are unimodal and
infinitely divisible. To address gene-gene correlation, they extend the construction to
"synchronized" multi-gene models — genes whose bursts fire at the same time, from the same or
different, possibly correlated, burst-size distributions — and derive closed-form Pearson
correlations under several coupling assumptions (independent, fully correlated, and anti-correlated
burst sizes, plus a fast-splicing limit of a single source transcript). They validate the DAG
algorithm against Gillespie simulation on a randomly generated seven-species splicing network, and
apply the fast-processing multi-gene model to long-read single-cell sequencing data (FLT-seq, mouse
stem cells), fitting marginal transcript distributions and comparing predicted to observed pairwise
correlations.

## What it found

The backward recursion correctly reproduces simulated marginal distributions and all pairwise
covariances for the test splicing graph. Analytically, synchronized bursting with geometrically
distributed burst sizes can only reach a Pearson correlation up to $1/2$ between two gene products,
attained only as burst sizes grow large with matched downstream rates; coupling the burst sizes
themselves (not just their timing) lifts this cap substantially. Synchronized bursts with geometric
burst sizes can never produce a negative transcript-transcript correlation, however anti-correlated
the burst-size pairing is — but a more dispersed, negative-binomial-like burst-size law does permit
negative correlations, so the achievable sign and magnitude depend on the burst-size distribution's
shape, not just its timing. Fitting the fast-processing multi-gene model to the FLT-seq dataset
(4,362 transcripts after quality filtering) showed the predicted correlation exceeded the observed
value for about 95% of transcript pairs and fell short for the remaining ~5%, consistent with
reading the theoretical number as an upper bound that real correlations fall short of because of
technical noise, unresolved intermediate splicing steps and model mis-specification — most visibly
for a cluster of pairs with near-zero or negative observed correlation the model cannot capture.

## Limits and context

The authors are explicit that no current sequencing technology meets all three prerequisites their
inference approach needs: single-cell, single-molecule counts at steady state; full causal
annotation of the splicing graph and which species degrade; and close-to-saturated,
quantification-noise-aware transcriptome coverage. The multi-gene correlation results apply strictly
to models with disjoint downstream splicing graphs — extending the covariance formula to genes whose
products eventually converge is noted as possible but is not carried out, as the notation becomes
unwieldy. The method does not treat general multidimensional diffusion, since that violates the
acyclic-graph assumption, though the authors note a link to percolation on DAGs (e.g. modeling RNA
polymerase movement along DNA). A supplementary note extends the framework toward delay
(non-Markovian) master equations for the simplest deterministic-delay and constitutive cases, but
finds the general bursty, delayed case intractable by the same methods — an open problem. The
empirical comparison is framed only as a constraint check, not confirmation that the model is the
correct mechanism: the authors attribute the systematic overestimation of correlation to the
combined, unresolved effects of technical noise and biophysical detail missing from the
fast-processing approximation, rather than treating the 95% success rate as validation.

## Citation

Gennady Gorin and Lior Pachter. "Analytical solutions of the chemical master equation with bursty
production and isomerization reactions." bioRxiv preprint, posted 2021-06-30 (originally submitted
2021-03-24). https://doi.org/10.1101/2021.03.24.436847
