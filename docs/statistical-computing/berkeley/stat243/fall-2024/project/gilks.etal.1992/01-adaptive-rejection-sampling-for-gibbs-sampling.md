---
title: Adaptive Rejection Sampling for Gibbs Sampling
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf
source_file: sources/berkeley-stat243/fall-2024/project/gilks.etal.1992.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`project/gilks.etal.1992.pdf`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Adaptive Rejection Sampling for Gibbs Sampling

By W. R. GILKS†
*Medical Research Council Biostatistics Unit, Cambridge, UK*

and P. WILD
*National Institute for Research and Safety in Occupational Health, Vandoeuvre, France*

[Received March 1990. Final revision February 1991]

## SUMMARY

We propose a method for rejection sampling from any univariate log-concave probability density function. The method is adaptive: as sampling proceeds, the rejection envelope and the squeezing function converge to the density function. The rejection envelope and squeezing function are piecewise exponential functions, the rejection envelope touching the density at previously sampled points, and the squeezing function forming arcs between those points of contact. The technique is intended for situations where evaluation of the density is computationally expensive, in particular for applications of Gibbs sampling to Bayesian models with non-conjugacy. We apply the technique to a Gibbs sampling analysis of monoclonal antibody reactivity.

*Keywords:* Adaptive rejection sampling; Bayesian inference; Gibbs sampling; Log-concave density; Non-conjugate Bayesian models; Simulation

---

†Address for correspondence: Medical Research Council Biostatistics Unit, Fair View Lodge, 5 Shaftesbury Road, Cambridge, CB2 2BW, UK.

© 1992 Royal Statistical Society
0035-9254/92/41337 \$2.00

---

---

[Up: contents](index.md) · [1. Introduction →](02-1-introduction.md)
