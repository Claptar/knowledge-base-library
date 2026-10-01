---
title: "Gorin & Pachter 2020 — Intrinsic and extrinsic noise are distinguishable in a synthesis – export – degradation model of mRNA production"
paper: "summary"
source: "https://doi.org/10.1101/2020.09.25.312868"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Gennady Gorin and Lior Pachter (2020). "Intrinsic and extrinsic noise are distinguishable in a synthesis – export – degradation model of mRNA production." bioRxiv preprint, posted 25 September 2020. https://doi.org/10.1101/2020.09.25.312868 ([original](https://doi.org/10.1101/2020.09.25.312868)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# Intrinsic and extrinsic noise are distinguishable in a synthesis – export – degradation model of mRNA production

**[Read the full text](full-text/index.md)**

## What this covers

Whether intrinsic noise (the inherent randomness of transcription itself) and extrinsic noise
(static differences between cells) can be told apart once downstream mRNA processing — splicing
and export — is included in the model. Speaks to stochastic gene expression modelling and the
interpretation of single-cell RNA-seq copy-number data.

## The question

Gene expression varies from cell to cell for two very different reasons: the intrinsic
stochasticity of transcription (bursts of mRNA production happening at random times, even with
identical kinetics in every cell) and extrinsic variability (systematic differences between cells —
in transcription factor levels, cell size, cell-cycle stage — that are effectively static within a
cell's lifetime). Telling these apart matters for building correct biophysical models, and the
question is newly pressing because single-cell RNA-seq gives discrete per-cell molecule counts
across large populations, unlike the continuous fluorescence readouts classical dual-reporter assays
use, and existing analyses of mRNA distributions alone are not always enough to pin down the
mechanism. In particular, a simple one-stage transcription model already has a known degeneracy: a
bursty (intrinsic) model and a constitutive model with a cell-to-cell varying production rate
(extrinsic) can produce the exact same steady-state negative binomial mRNA count distribution. The
authors ask whether adding a second, downstream stage — producing a joint distribution of nascent
and mature mRNA rather than a single mRNA count — breaks this degeneracy.

## The approach

Two minimal two-stage models are compared, each consisting of a transcription step feeding into a
splicing step (nascent to mature mRNA, rate $\beta$) and a degradation step (mature mRNA removal,
rate $\gamma$). In the intrinsic-noise model, every cell has identical transcription kinetics: the
gene fires in bursts of geometrically-distributed size at a fixed frequency, so all cell-to-cell
variability comes from the randomness of this bursting process itself. In the extrinsic-noise model,
transcription is constitutive (a simple Poisson process) within each cell, but the production rate is
drawn once per cell from a Gamma distribution, so all variability is a static, between-cell
difference rather than within-cell stochasticity. The authors derive exact analytical results for
both models: known moment formulas for the bursty model's joint nascent/mature distribution, and a
full analytical solution of the chemical master equation for the Gamma-mixed constitutive model,
which turns out to be a multivariate negative binomial distribution. They then ask what happens when
both models are constrained to produce the same nascent mRNA marginal distribution — which, for
either model, is always negative binomial — and compare the resulting mature mRNA distributions,
variances and nascent-mature correlations.

## What it found

Using only the nascent mRNA distribution, the two models are not distinguishable at all: any
negative binomial nascent distribution can be produced by either model, with an explicit one-to-one
mapping between their parameters. Bringing in the mature mRNA distribution — available only once
the downstream processing step is modelled — breaks this degeneracy. Holding the degradation rate
fixed, the two models can match the mature mRNA mean exactly, yet their mature mRNA variances and
their nascent-mature correlations never agree: the extrinsic model is always more overdispersed in
mature mRNA than the intrinsic model, while the intrinsic model's nascent-mature correlation is
always larger relative to the extrinsic model's, under these constraints. The reverse constraint —
fixing the mature mRNA variance and solving for the degradation rate each model implies — gives a
mirror result: the degradation rate required under the extrinsic model is always higher than under
the intrinsic model, with the ratio of the two confined to the open interval (0,1) and never
reaching equality. Gillespie simulations using matched nascent distributions for both models
confirm this qualitatively: the extrinsic model's simulated joint distribution is visibly more
correlated and has a longer mature-mRNA tail than the intrinsic model's. The overall conclusion is
that a single additional observable — the nascent/mature split, already accessible through several
existing experimental methods — is sufficient in principle to recover identifiability that is lost
when only total mRNA counts are used. The paper also notes that, where joint nascent/mature
copy-number data are available, a likelihood-ratio test between the two models' maximum-likelihood
fits (seeded from the closed-form moment estimates it derives) can be used in practice to pick the
better-supported noise source.

## Limits and context

The two models are deliberately minimal, chosen for qualitative insight rather than as
general-purpose biophysical models, and no full analytical solution is available for the bursty
model's joint distribution — only for its low-order moments, which is what the comparison relies
on. The authors survey the experimental routes to nascent/mature or spatial copy-number data the
argument needs — spatial transcriptomics, intron-targeted fluorescent probes, nucleoside-analogue
labelling, intron-aligned sequencing reads — and note all are currently complex, hard to scale
genome-wide, or biased by the common reliance on capturing polyadenylated tails, which
under-represents the nascent molecules of interest. They also push back on a specific published
claim that heavy-tailed mature mRNA distributions, as seen in standard 10x scRNA-seq data, are by
themselves sufficient evidence of extrinsic noise: that comparison used a one-stage model unsuited
to mammalian splicing and export, the models compared have their own non-identifiability issues, and
uncharacterised technical biases from raw-count normalisation choices could alone produce the
attributed heavy tail. They close by arguing that progress on measuring the nascent transcriptome
genome-wide, combined with this discrete, biophysically-interpretable modelling framework, should
make identifying noise sources genome-wide more tractable.

## Citation

Gennady Gorin and Lior Pachter (2020). "Intrinsic and extrinsic noise are distinguishable in a
synthesis – export – degradation model of mRNA production." bioRxiv preprint, posted 25 September
2020. https://doi.org/10.1101/2020.09.25.312868
