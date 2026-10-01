---
title: 2 Two models for gene expression
source: https://doi.org/10.1101/2020.09.25.312868/
source_file: sources/papers/gorin-pachter-2020-intrinsic-extrinsic/gorin-pachter-2020-intrinsic-extrinsic.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2020-intrinsic-extrinsic.pdf` from [papers/gorin-pachter-2020-intrinsic-extrinsic](https://doi.org/10.1101/2020.09.25.312868/) — papers · gorin-pachter-2020-intrinsic-extrinsic, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Two models for gene expression

It is well-known that the common two-state model of gene expression [11] gives rise to a negative
binomial (NB) distribution of mRNA counts in the short-burst limit [12]. However, a recent study
shows that constitutive transcription in a cell population with a gamma-distributed production
rate parameter also yields a negative binomial distribution of mRNA counts [13]. Although there are
both experimental and theoretical arguments favoring a bursting model for eukaryotic transcription
[14–17] – current theories posit that superstructure modifications are responsible for occlusion
and exposure of the gene locus [18, 19] – a comprehensive model should account for all relevant
sources of noise, as well as provide both a quantitative and qualitative understanding of their
effects.

A current limitation of existing models is that processes downstream of eukaryotic mRNA
production, such as export and/or splicing processes [20, 21], are generally ignored. However,
promising new technologies and experiments, based on fluorescence [22, 23] and sequencing [24]
methods, can distinguish nascent from mature mRNA, thus providing essential data for studying model
of increasing complexity. In particular, the maturation of these methods and the availability of
resulting multimodal data naturally suggests the potential of fitting otherwise poorly identifiable
models [9].

As a first step, and to gain a qualitative understanding of the effects of intrinsic and
extrinsic noise in the context of downstream processing, we compare solutions of two simple
two-stage models of transcription that include downstream processing at steady state. Both models
assume that nascent mRNA (unspliced or pre-mRNA) is converted to mature mRNA (spliced mRNA) after
an exponentially-distributed delay, corresponding to splicing. This is followed by another
exponentially-distributed delay that models the mature mRNA being degraded. The splicing rate
$\beta$ and degradation rate $\gamma$ are deterministic. The gene locus dynamics are modeled by
either bursts, with stochastic burst size $B \sim Geom(b)$ and deterministic burst initiation
frequency $k_i$ [20], or constitutive, with stochastic but constant transcription rate
$K \sim Gamma(\alpha,\eta)$. The model parametrizations are illustrated in Figure 1. We calculate
lower moments and cross-moments, and show how these can be used to differentiate between
distributions and statistics resulting from the two models.

**Figure 1:** (a) Schema of the intrinsic noise model ($k_i$: burst frequency; $B$: burst size
drawn from a geometric distribution; $\beta$: pre-mRNA splicing rate; $\gamma$: mRNA degradation
rate. Uniform shade of green indicates identical parameter values across all cells). (b) Schema of
the extrinsic noise model ($K$: transcription rate; $\beta$: pre-mRNA splicing rate; $\gamma$: mRNA
degradation rate. Different shades of green indicate different values of $K$ across cells).

Schema: (a) Intrinsic noise model: Gene $\xrightarrow{k_i}$ (burst $B\times$) Pre-mRNA
$\xrightarrow{\beta}$ mRNA $\xrightarrow{\gamma} \emptyset$. (b) Extrinsic noise model: Gene
$\xrightarrow{K}$ Pre-mRNA $\xrightarrow{\beta}$ mRNA $\xrightarrow{\gamma} \emptyset$.

---

[← 1 Background](01-1-background.md) · [Up: contents](index.md) · [3 Notation →](03-3-notation.md)
