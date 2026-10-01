---
title: "Paulsson 2004 — Summing up the noise in gene networks"
paper: "summary"
source: "https://doi.org/10.1038/nature02257"
licence: "© publisher — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Paulsson, J. (2004). Summing up the noise in gene networks. Nature, 427(6973), 415–418. https://doi.org/10.1038/nature02257 ([original](https://doi.org/10.1038/nature02257)). Rights: © publisher — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Summing up the noise in gene networks

## What this covers

How to compare noise in gene expression across different experiments. It speaks to the physics
of stochastic gene networks and single-cell biology, at the point where several independent GFP
studies had just produced measurements that looked hard to reconcile with one another.

## The question

By the early 2000s several groups had measured cell-to-cell variability in gene expression using
GFP reporters, each targeting a different stage of the central dogma: plasmid replication,
transcriptional autorepression, and chromosomal expression in bacteria, yeast and two
simultaneously-tagged genes in *E. coli*. The studies used different models, different noise
measures and different biological systems, and seemed to point to different conclusions — for
instance, about whether autorepression suppresses noise, where noise actually originates, and
whether eukaryotes differ fundamentally from prokaryotes in how noise arises. Paulsson's question
is whether these apparently conflicting pictures are really describing different phenomena, or
whether they are special cases of one underlying relationship that the separate analyses obscured.

## The approach

Paulsson models a generic two-species system — a fluctuating "environment" species $X_1$ (for
example mRNA or an upstream regulator) driving the births and deaths of a second species $X_2$
(for example protein or plasmid copies) as a birth-and-death Markov process. Applying the
$\Omega$-expansion, whose first two orders recover the macroscopic rate equations and a linear-noise
(fluctuation-dissipation) approximation around a stable steady state, he derives a single compact
equation for the relative variance of $n_2$. It separates into an intrinsic term set by the average
copy number of $X_2$ and a logarithmic gain $H_{22}$ (how strongly $X_2$'s own production and
elimination respond to its own abundance — a scale-free elasticity borrowed from metabolic control
analysis), and an extrinsic term built from $X_1$'s own noise, a ratio of logarithmic gains
$H_{21}/H_{22}$ that measures how much a change in $X_1$ is transmitted to $X_2$ relative to how
strongly $X_2$ corrects itself, and a time-averaging factor that depends on how the relaxation time
of $X_2$ compares with the correlation time of $X_1$. Because the logarithmic gains are properties
of the reaction rates themselves, they can often be read directly off the proposed kinetic model for
a given system, which lets the same equation be reinterpreted for plasmid replication, transcription,
translation or autorepression simply by substituting the appropriate gains.

## What it found

Applying this single relation to the published studies, Paulsson argues that much of the apparent
disagreement dissolves. Autorepression of plasmid replication and of transcription both reduce noise
for the same two reasons in the model — faster normalized adjustment toward steady state suppresses
intrinsic fluctuations, and reduced susceptibility to the upstream environment suppresses extrinsic
fluctuations — which reconciles the replication and transcription experiments under one mechanism
despite their different biology. For the transcriptional autorepression data, the predicted gain
ratio ($H_{21}/H_{22}\approx1/4$ under autorepression versus $1$ without it) matches the observed
roughly twofold drop in relative standard deviation. For chromosomal expression in *Bacillus
subtilis*, a burst-size model with no free parameters predicts relative variance $\approx 1+b$,
where $b$ is the average number of proteins made per transcript, and this fits the measured
translation-dependence of the noise. Across systems, fully induced genes show relative standard
deviations as low as 15% in both a prokaryote (*B. subtilis*) and a eukaryote (*S. cerevisiae*),
and Paulsson argues the differences reported between studies trace mostly to differences in network
design — which rate constants and upstream inputs were varied — rather than to a fundamental
difference between how noise arises in prokaryotic and eukaryotic systems.

## Limits and context

The unifying equation is a linear, first-order approximation valid near a stable fixed point; it is
not built to capture genuinely nonlinear or dynamically disordered regimes, such as unstable
self-replication without a template. Paulsson is explicit that some comparisons remain unsettled:
the non-monotonic relation between transcription rate and noise reported for *S. cerevisiae* could
reflect extra mechanisms specific to eukaryotes, such as chromatin remodelling or transcriptional
reinitiation, but he states plainly that alternative explanations involving random association and
dissociation of activators or repressors are equally consistent with the same data, and that "there
are at this point no reasons to favour one interpretation over another." He also cautions that GFP
is an imperfect reporter of single-cell plasmid copy number, limiting what the replication study can
establish about mechanism, and that normalized noise measures can make the same underlying data look
either monotonic or non-monotonic depending on which quantity is held fixed. He argues against the
claim that eukaryotic and prokaryotic gene expression differ in kind, holding that no principled
difference has actually been demonstrated by the data assembled so far, and calls for further
experiments — including real-time tracking rather than population snapshots — to distinguish between
the remaining candidate explanations.

## Citation

Paulsson, J. (2004). Summing up the noise in gene networks. *Nature*, 427(6973), 415–418.
https://doi.org/10.1038/nature02257. Available via Nature (subscription/institutional access) or
from the library catalogue entry for this source.
