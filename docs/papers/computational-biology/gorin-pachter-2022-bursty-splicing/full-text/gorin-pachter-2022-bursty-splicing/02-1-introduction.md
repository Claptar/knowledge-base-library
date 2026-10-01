---
title: 1 Introduction
source: https://doi.org/10.1101/2021.03.24.436847/
source_file: sources/papers/gorin-pachter-2022-bursty-splicing/gorin-pachter-2022-bursty-splicing.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2022-bursty-splicing.pdf` from [papers/gorin-pachter-2022-bursty-splicing](https://doi.org/10.1101/2021.03.24.436847/) — papers · gorin-pachter-2022-bursty-splicing, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Introduction

Recent advances in the analysis of single-cell RNA sequencing [1] and fluorescence microscopy
[2] enable the quantification of pre-mRNA molecules alongside mature mRNA. These techniques
provide an opportunity to infer the topologies and biophysical parameters governing the processes
of mRNA transcription, splicing, export, and degradation in living cells. In particular, they provide
a novel approach to inferring and studying the dynamics of splicing cascades [3].

However, drawing mechanistic conclusions from transcriptomics requires overcoming numerous statistical
and computational challenges. Living cells contain mRNA in low copy numbers, and transient
nascent species are even less abundant, leading to potential pitfalls if the discrete nature of
the data is not appropriately modeled [4]. One approach to modeling dynamics from count data
is to utilize detailed Markov models based on the chemical master equation (CME) [5–7]. Such
modeling can, in principle, yield analytical solutions for the dynamics of genes affected by arbitrary
splicing networks, thus circumventing tractability problems arising with matrix- and simulationbased methods that can be impractical for large numbers of species [8]. Several classes of analytical
solutions to the CME are available [9], but their derivation tends to be *ad hoc*, with limited generalization
to more complex systems.

Starting with the approach of Singh and Bokes to the problem of bursty transcription coupled to
nuclear export and degradation of mRNA [10], we develop a class of solutions for gene dynamics
affected by arbitrary splicing networks under the physiologically relevant assumption of bursty
production of mRNA [11]. Fundamentally, the generating function of a Markov chain describing the
evolution of molecules in a splicing cascade can be automatically computed, numerically integrated
in time, and then inverted by Fourier transformation at an overall computational complexity of
$O(\mathcal{N}\log\mathcal{N})$ in state space size. We begin with the example of splicing described by a path graph,
where the order of intron removal is deterministic, extend the procedure to a much broader class
of splicing graphs and driving burst processes, and subsequently demonstrate the existence of the
solutions and their isomorphism to a class of moving average processes.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Methods →](03-2-methods.md)
