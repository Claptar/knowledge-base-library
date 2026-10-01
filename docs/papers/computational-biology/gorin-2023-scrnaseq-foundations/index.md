---
title: "Gorin 2023 — Stochastic foundations for single-cell RNA sequencing"
paper: "summary"
source: "https://thesis.library.caltech.edu/16062/"
licence: "CC BY-NC-ND 4.0 — no adaptation permitted, not reproduced"
written: "2026-10-02"
---

> **Summary of a thesis.** Gennady Gorin. "Stochastic foundations for single-cell RNA sequencing." PhD thesis, California Institute of Technology, 2023 (defended May 19, 2023; advisor Lior Pachter). ([original](https://thesis.library.caltech.edu/16062/)). Rights: CC BY-NC-ND 4.0 — no adaptation permitted, not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Stochastic foundations for single-cell RNA sequencing

## What this covers

A PhD thesis arguing that single-cell RNA sequencing (scRNA-seq) analysis should be grounded in
stochastic models of the underlying molecular biophysics rather than in purely descriptive
statistics, and building the mathematics and software to do so. It speaks to computational biology
and biophysics, specifically the interpretation of transcript count data.

## The question

scRNA-seq has been widely adopted, and a wide variety of analysis methods has grown up around it,
but with comparatively little systematic scrutiny of what those methods assume — which the author
argues produces real discrepancies in interpretation. A concrete case motivates the project: the
negative binomial distribution is the default model for gene counts in sequencing analyses, where
its overdispersion is usually attributed to technical and compositional effects, while the same
distribution appears in single-molecule fluorescence imaging, where overdispersion is attributed to
genuinely bursty transcription. The two fields use the same mathematics but attach incompatible
meanings to it, and the thesis sets out to resolve this by deriving the distribution, and its
relatives, from an explicit, falsifiable stochastic model of transcription, splicing and
measurement, so biological and technical variability are both represented rather than one masking
the other.

## The approach

The method treats transcription, RNA processing and the sequencing measurement itself as one
continuous-time Markov chain, formalised by a chemical master equation and solved with probability
generating functions. Generating functions compose: a model of bursty production, a model of
splicing, and a model of cell-to-cell technical capture can each be written separately, then
multiplied, convolved or integrated into one joint prediction for what an experiment should observe
in both nascent (intron-containing) and mature transcript counts. These predictions are fit to real
count data by maximum likelihood and compared against each other, or against competing mechanistic
hypotheses, with likelihood ratios and information criteria, rather than relying on nonparametric
summaries. Because exact generating-function inversion needs numerically expensive grid quadrature
that scales poorly with the number of species, the thesis also develops faster approximations —
truncated special-function series and a neural-network surrogate — packaged as software (*Monod*)
so the framework runs at the scale of real datasets.

## What it found

**Negative binomial meaning.** The same bursty-transcription master equation that explains
single-molecule fluorescence data also reproduces the negative binomial distributions seen in
sequencing data, so the two fields' shared distribution can have one biophysical origin rather than
two incompatible ones.

**A generating-function formalism** for transcription, splicing, degradation and technical capture,
built so biological and technical sub-models compose modularly into one joint prediction for nascent
and mature counts — with faster special-function and neural-network approximations developed
because exact quadrature does not scale.

**A critique of RNA velocity.** Checking *velocyto* and *scVelo* against the mechanistic framework
shows their preprocessing and dynamical assumptions are largely incompatible with each other and
with the physical model: on the same forebrain dataset they infer qualitatively different, at times
reversed, differentiation directions, and smoothing, normalization and nonlinear embedding are shown
to distort the cell relationships the method relies on. A proposed self-consistent alternative
recovers some parameters from snapshot data but has limited power to identify the true underlying
process architecture.

**Model identifiability.** Single-modality (mature-only) distributions often cannot distinguish
mechanistically distinct causes of overdispersion — e.g. bursty transcription versus cell-to-cell
variation in a continuous rate — that look identical marginally but differ jointly; multimodal data
make many, not all, of these cases distinguishable, which is used to classify real genes by likely
regime and to test Markovian against deterministically-delayed splicing and degradation.

**Technical-noise sub-models.** Background RNA in "empty" droplets behaves like pseudobulk Poisson
contamination; a pervasive, counterintuitive gene-length bias in nascent counts is better explained
by length-dependent capture than length-independent capture; and discordant raw counts between 10x
chemistry versions, and between single-cell and single-nucleus protocols, can be reconciled by
fitted technical parameters while holding biology fixed — suggesting the discordance is largely
technical.

**Differential expression.** Standard normalization and comparison-of-averages practice is examined
and a "mechanistic" alternative proposed: comparing fitted biophysical parameters, such as burst
size and frequency, between conditions, argued to be more interpretable and more sensitive given
multimodal data.

**Multi-gene covariation.** Candidate model classes for gene–gene correlation — discrete or
continuous cell-type mixtures, an Ising/Glauber-dynamics analogy for fast transcript–transcript
coupling, and a preliminary variational-autoencoder model for slower covariation — are compared,
concluding that representing explicit regulatory feedback within this framework remains
computationally intractable at genome scale.

**Other multiomic data.** The framework is sketched for RNA–protein data ("protein velocity"), for
chromatin accessibility via an Ising-like open/closed-state analogy to transcriptional bursting, and
for spatial transcriptomics via a compositional model of cell-type mixture, bead capture and spatial
background; the chromatin and spatial extensions are presented as preliminary, unpublished work.

## Limits and context

The author is explicit that this is a first step, not a finished theory. The binary nascent/mature
read classification is acknowledged as an approximation omitting transcript elongation, imperfect
capture and assignment ambiguity. Explicit regulatory feedback is excluded throughout because it
makes the mathematics intractable and because the protein data needed to constrain it is usually
unavailable. Genome-wide joint modelling of many interacting genes is called currently impractical
with this toolbox, requiring new solvers. The multi-gene, chromatin-accessibility and
spatial-transcriptomics material is flagged as preliminary or unpublished rather than settled. The
thesis argues against treating nonparametric, normalization-heavy pipelines — graph-based
clustering, RNA velocity's dynamics inference — as neutral defaults, since their compatibility with
single-molecule noise is unclear or demonstrably violated, but stops short of claiming the
mechanistic approach resolves these questions: it presents itself as groundwork "meant to enable
rigorous investigations by trained statisticians" rather than a completed statistical framework.

## Citation

Gennady Gorin. *Stochastic foundations for single-cell RNA sequencing.* PhD thesis, California
Institute of Technology, 2023 (defended May 19, 2023; advisor Lior Pachter). Available at
<https://thesis.library.caltech.edu/16062/>.
