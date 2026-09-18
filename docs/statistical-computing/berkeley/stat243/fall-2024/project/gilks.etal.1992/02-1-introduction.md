---
title: 1. Introduction
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf
source_file: sources/berkeley-stat243/fall-2024/project/gilks.etal.1992.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`project/gilks.etal.1992.pdf`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1. Introduction

We present a black box technique for sampling from any univariate log-concave probability density function $f(x)$. Our method is based on rejection sampling and does not require a determination of the mode of $f(x)$. It is adaptive: the envelope function and the squeezing function (which form upper and lower bounds to $f(x)$) converge to the density $f(x)$ as sampling proceeds. The envelope and squeezing functions are piecewise exponentials. The adaptive nature of our technique enables samples to be drawn with few evaluations of $f(x)$; it will therefore be useful in situations where the evaluation of $f(x)$ is computationally expensive. We describe adaptive rejection sampling in Section 2.

Although not contained in Devroye (1986), adaptive rejection sampling has some points of contact with methods of Devroye (1986). In particular, in chapter 4.5, Devroye (1986) discusses rejection sampling using a sequence of envelope and squeezing functions which converge to the density; however, the approach is not adaptive as the bounding functions are determined in advance. In chapter 7.2, Devroye (1986) discusses non-adaptive black box methods for log-concave densities which require the location of the mode of the density; in particular he presents an algorithm for rejection sampling using a piecewise exponential envelope comprising three pieces, the centre piece touching the density at its mode. In chapter 7.3, Devroye (1986) discusses non-adaptive methods which take advantage of particular properties of unimodal densities. An exercise in chapter 8.2 of Devroye (1986) concerns an adaptive rejection sampling algorithm in which the rejection envelope is a histogram.

Adaptive rejection sampling grew out of an analysis of patterns of reactivity of monoclonal antibodies. Our data for this analysis were in the form of percentages, rounded to the nearest integer. This discretization would not have been a problem except that much of the data were concentrated at or close to the extremes of the percentage scale. The complexity of our model and data led us to a Gibbs sampling analysis (Geman and Geman, 1984), for which we needed to be able to sample efficiently from densities of complicated algebraic form. In Section 4 we present an analysis of these data using adaptive rejection sampling and Gibbs sampling.

Gibbs sampling is a Markovian updating scheme originally developed by Geman and Geman (1984) as a tool for image reconstruction. However, its applicability to statistical modelling has recently been demonstrated (Gelfand and Smith, 1990). The enormous potential of Gibbs sampling in complex statistical modelling is now being realized. Applications currently include Bayesian cluster analysis (Gilks *et al.*, 1989), changepoint problems (Carlin *et al.*, 1991), genetic linkage analysis (Mack *et al.*, 1990; Thomas, 1991), model selection from normal scale mixture densities (Carlin and Polson, 1991a), influence diagnostics (Carlin and Polson, 1991b), hierarchical models, variance components and errors in variables (Gelfand and Smith, 1990), missing data, ordered means and growth curve models (Gelfand *et al.*, 1990), outlier detection (Verdinelli and Wasserman, 1991), generalized linear models with random effects (Zeger and Karim, 1991) and analysis of frailty in survival analysis (Clayton, 1991). We are also aware of many other applications of Gibbs sampling, currently in the form of unpublished manuscripts. We describe Gibbs sampling in Section 3.

Whereas the application of Gibbs sampling is straightforward for fully conjugate Bayesian models (Gelfand and Smith, 1990; Gelfand *et al.*, 1990), non-conjugacy can cause computational difficulties. In applying Gibbs sampling to the estimation of generalized linear models with random effects, Zeger and Karim (1991) deal with non-conjugacy by rejection sampling from a normal envelope centred at the mode of the sampling density. We show in Section 3 that adaptive rejection sampling is well suited to handling non-conjugacy in applications of Gibbs sampling, as it requires neither the mode of the sampling density nor a rejection envelope that corresponds to a standard density.

---

[← Adaptive Rejection Sampling for Gibbs Sampling](01-adaptive-rejection-sampling-for-gibbs-sampling.md) · [Up: contents](index.md) · [2. Adaptive Rejection Sampling →](03-2-adaptive-rejection-sampling.md)
