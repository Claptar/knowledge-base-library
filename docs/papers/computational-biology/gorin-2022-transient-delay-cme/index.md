---
title: "Gorin, Yoshida & Pachter 2022 — Transient and delay chemical master equations"
paper: "summary"
source: "https://doi.org/10.1101/2022.10.17.512599"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Gorin, G., Yoshida, S., & Pachter, L. (2022). Transient and delay chemical master equations. bioRxiv. https://doi.org/10.1101/2022.10.17.512599 ([original](https://doi.org/10.1101/2022.10.17.512599)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# Transient and delay chemical master equations

**[Read the full text](full-text/index.md)**

## What this covers

Analytical and numerical recipes for solving the *transient* (time-dependent) probability
distributions of RNA copy numbers under chemical master equations that mix ordinary Markovian
reactions with deterministically delayed ones (delay CMEs, or DCMEs). The method is then used to
ask whether single-cell and single-nucleus RNA sequencing data require non-Markovian models of
nuclear export and splicing, or whether the usual memoryless assumption still suffices. Speaks to
stochastic modeling of transcription, splicing and RNA processing in computational biology.

## The question

Models of transcriptional bursting and splicing are usually built assuming every step — promoter
switching, splicing, export, degradation — is Markovian (exponentially distributed waiting times),
mainly for tractability. This fits single-cell RNA-seq (scRNA-seq) data reasonably well, since it
mostly measures rapidly-exported cytoplasmic RNA. Single-nucleus RNA-seq (snRNA-seq) instead
samples nuclear content and captures far more unspliced RNA, which forces a question the authors'
own earlier models had sidestepped: is nuclear export fast enough to treat as instantaneous and
memoryless, or does it need an explicit, non-Markovian waiting time? More broadly: do
single-nucleus data *require* qualitatively different models from single-cell data, is Markovian
splicing consistent with data at all given that splicing is now known to often occur
co-transcriptionally, and how well can either data type even distinguish between competing
hypotheses? Answering this needed tools that largely did not exist — full transient solutions of
DCMEs were previously tractable only in special cases, such as the "linear chain trick" for a
single constant delay.

## The approach

The authors extend the generating-function (PGF) machinery they had already built for purely
Markovian bursty and multi-state promoter systems, in which a system's PGF comes from solving a
linear ODE for a set of auxiliary "characteristics" and integrating a promoter/burst generating
function along them. They show that a reaction with a fixed delay $\tau$ simply contributes a
different, two-piece analytic characteristic (built from indicator functions marking whether the
delay has elapsed) in place of the usual exponential-decay characteristic, and that this slots into
the same ODE/integration recipe used for Markovian systems — for an arbitrary directed-acyclic
network of monomolecular interconversion and degradation reactions, with any number of promoter
states, and no feedback. The recipe is further extended to Erlang-distributed delays (recovering
the deterministic case as a limit) and, more speculatively, to general waiting-time distributions
via their survival functions. A modified Gillespie stochastic simulation algorithm, adapted to
queue and release delayed events in the correct order, validates the solutions against simulation
on a four-promoter-state, four-species test network.

The toolkit is then fit to real data. For a two-species (unspliced/spliced) system, four models are
compared by maximum likelihood (gradient descent, via the authors' *Monod* software): standard
bursty Markovian; deterministically delayed efflux (splicing/export lumped together); "extrinsic
noise" with a gamma-distributed transcription rate; and deterministically delayed splicing. These
are fit gene-by-gene to paired single-cell and single-nucleus datasets (mouse cortex, human liver),
and compared via per-gene log-likelihood ratios against the bursty Markovian model.

## What it found

The ODE recipe reproduces simulated trajectories for the four-state/four-species test network,
matching promoter-state and molecule-count marginals at several time points. Closed-form moments
(and, for two models, full log-PGFs) show the delayed-splicing model's unspliced and spliced counts
factorize into independent marginals, unlike the Markovian and delayed-efflux models, which both
induce nonzero covariance between the species.

Fitting to real data: single-cell data gave only modest evidence favoring the bursty Markovian
model over delayed efflux, and stronger evidence against the extrinsic-noise and delayed-splicing
alternatives. Single-nucleus data showed the same ranking but with much smaller log-likelihood-ratio
magnitudes — delayed efflux could barely be distinguished from the Markovian model at all in nuclear
data. The reason is an identifiability limit rather than necessarily a biological one: the bursty
Markovian, delayed-efflux and extrinsic models all predict essentially the same negative-binomial
marginal for unspliced counts, so telling them apart needs enough *spliced* RNA, which
single-nucleus data have little of by construction. Delayed splicing remained more distinguishable
in nuclear data because it predicts a qualitatively different (geometric-Poisson/Pólya–Aeppli-type)
unspliced marginal. Overall, single-nucleus data showed no systematic signature favoring a
non-Markovian export model, and were broadly consistent with Markovian, one-step splicing and
export — with the caveat that low spliced counts in nuclear data limit what any comparison there can
resolve.

## Limits and context

The authors call this investigation non-comprehensive: technical sequencing noise, cell-cycle and
cell-size effects are not modeled, and the cell-type labels used to split data are themselves
derived partly from spliced-count-based clustering, introducing some circularity. The result
favoring the Markovian hypothesis is a statement about what single-nucleus data *can* distinguish,
not proof that nuclear export is in fact Markovian — the paper frames it as the more parsimonious
working hypothesis given the evidence, not a settled mechanistic claim. The general method is
currently restricted to monomolecular networks with no feedback (no autoregulation or
protein-mediated control), and while the recipe extends formally to general waiting-time
distributions via survival functions, only a few (exponential, deterministic, Erlang, plus
illustrative half-Cauchy and Pareto cases) are worked out in closed form — and some of those
illustrative cases turn out to lack a stationary distribution at all, underscoring that
"intermediate" non-Markovian waiting times need case-by-case treatment rather than a universal
closed form.

## Citation

Gorin, G., Yoshida, S., & Pachter, L. (2022). Transient and delay chemical master equations.
bioRxiv. https://doi.org/10.1101/2022.10.17.512599
