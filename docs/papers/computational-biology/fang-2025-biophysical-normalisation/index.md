---
title: "Fang 2025 — A biophysical approach to normalization and trajectory inference in single-cell RNA sequencing data analysis"
paper: "summary"
source: "https://doi.org/10.7907/asek-t904"
licence: "all rights reserved — not reproduced"
written: "2026-10-02"
---

> **Summary of a thesis.** Fang, Meichen (2025). "A biophysical approach to normalization and trajectory inference in single-cell RNA sequencing data analysis." PhD thesis, California Institute of Technology. Defended May 28, 2025. ([original](https://doi.org/10.7907/asek-t904)). Rights: all rights reserved — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# A biophysical approach to normalization and trajectory inference in single-cell RNA sequencing data analysis

## What this covers

A PhD thesis in biological engineering arguing that two routine steps of single-cell RNA
sequencing (scRNA-seq) analysis, normalization and trajectory inference, should be built on
explicit stochastic models of gene expression rather than the heuristic procedures that dominate
current pipelines.

## The question

Early single-cell studies of gene expression, before scRNA-seq existed, fitted mechanistic
stochastic models — the telegraph and bursty promoter models, solved via the chemical master
equation (CME) — to small numbers of genes measured by imaging. The author frames this, after
Breiman's "two cultures" of statistical modeling, as a *data model* culture: positing a stochastic
mechanism and prioritizing interpretability. Once scRNA-seq made genome-wide profiling possible,
the field's standard workflow — filter by total counts, normalize by dividing by a cell's total
counts, apply a $\log(1+x)$ transform, select variable genes, embed and infer pseudotime from
distances — largely abandoned that grounding for an *algorithmic* culture, chosen because it
scales and predicts well rather than because it describes how the data arose. The thesis asks what
is gained by returning to an explicit generative model for these two steps: what normalization and
"pseudotime" actually mean once a mechanism and a measurement model are stated, and what static
snapshot data can and cannot support as a result.

## The approach

A background chapter reviews the CME and its standard large-volume approximations (system-size
expansion/linear noise approximation, WKB), recounting the known result that their infinite-time
and infinite-volume limits do not commute, so neither holds uniformly in time. It then sketches a
preliminary, explicitly incomplete attempt, via the positive Poisson representation, to build an
approximation for bimolecular reactions valid uniformly in time.

The normalization chapter models the variability across cells and genes as the product of a
per-cell biological scaling factor (cell size, cycle phase, similar global effects) and a technical
factor from Bernoulli sampling of transcripts during library preparation. This gives an algebraic
identity linking the normalized covariance between genes, this combined "extrinsic noise," and the
overdispersion seen in genes whose counts are intrinsically close to Poisson. The identity lets
near-Poisson "control" genes be identified from data alone and used, rather than total counts over
all genes, as a principled cell-size factor.

The trajectory chapter introduces Chronocell, which places each cell at a latent (lineage, process
time) position on a directed graph of discrete states, each with its own constant transcription
rate; nascent and mature RNA counts follow the known analytic solution of a constant-rate
birth-death CME, with a sequencing-noise layer on top. Parameters and process time are fit by
variational inference, competing topologies are compared by AIC/BIC, and a per-gene
goodness-of-fit check flags genes the model does not capture — replacing the usual fit-then-test
pipeline, which the thesis argues is circular because it tests genes against a pseudotime built
from those same genes.

## What it found

The CME chapter's time-uniform approximation is left unfinished: it shows a stable fixed point
cannot exist off the real axis in the complex-domain rate equation, but does not complete the
construction.

The normalization model, validated on synthetic dilution data, was applied to human-mouse mixing
experiments, where ambient mRNA from the other species gave an independent read on technical
noise. Biological and technical extrinsic noise were both substantial and comparable (e.g.
technical noise around 0.15 against total noise around 0.24 in one dataset), and often under a
fifth of genes had mature-mRNA counts consistent with Poisson statistics. Size factors built from
these genes correlated closely with conventional total-count size factors ($r \approx 0.99$) in
one dataset but diverged, with consequences for differential expression, when cell-type
composition was skewed. The Bernoulli assumption held for mature mRNA in several 10x datasets but
failed on a STORM-seq dataset, so the model needs validating per protocol.

Chronocell recovered simulated ground-truth process time to within about 5% of trajectory
duration, estimated the fast-switching transcription rate more accurately than splicing and
degradation rates, correctly selected the true topology over wrong alternatives by AIC/BIC, and
correctly flagged non-dynamic genes. On real data it recovered a cyclic topology for a cell-cycle
dataset, with degradation-rate estimates moderately correlated with two metabolic-labeling
techniques, and on a time-stamped neuron dataset its process time tracked experimental time better
than four widely used alternatives, only one of which captured the trend at all. Comparator
methods failed on data simulated under Chronocell's own assumptions; on more generic simulations
Chronocell was comparable to or better, though no method recovered exact timing.

A short closing chapter argues both models are deliberately simplified — a single scalar
biological noise factor, bursting-free piecewise-constant transcription — and calls for closing
the loop between mechanistic modeling and experimental design, so scRNA-seq technical variability
could eventually be characterized as reproducibly as a physical constant.

## Limits and context

The thesis states that its CME approximation is unfinished, that its normalization model collapses
biological extrinsic noise into one per-cell number and cannot be checked where Bernoulli sampling
fails, and that Chronocell's transcription model undershoots real transcriptional noise and
assumes a trajectory topology chosen by model selection rather than discovered from scratch. It
argues against purely similarity/distance-based pseudotime, which it says cannot be given a
physical interpretation, and against testing gene association with a pseudotime inferred from the
same data, calling that circular. It does not claim a comprehensive benchmark, since comparisons
across methods built on different generative assumptions are not strictly like for like.

## Citation

Fang, Meichen (2025). *A biophysical approach to normalization and trajectory inference in
single-cell RNA sequencing data analysis*. PhD thesis, California Institute of Technology.
Defended May 28, 2025. DOI: [10.7907/asek-t904](https://doi.org/10.7907/asek-t904). Available
from the Caltech Thesis Library.
