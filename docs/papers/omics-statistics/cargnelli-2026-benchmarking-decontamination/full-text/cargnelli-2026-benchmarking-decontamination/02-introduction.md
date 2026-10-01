---
title: Introduction
source: https://doi.org/10.64898/2026.01.13.699237/
source_file: sources/papers/cargnelli-2026-benchmarking-decontamination/cargnelli-2026-benchmarking-decontamination.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `cargnelli-2026-benchmarking-decontamination.pdf` from [papers/cargnelli-2026-benchmarking-decontamination](https://doi.org/10.64898/2026.01.13.699237/) — papers · cargnelli-2026-benchmarking-decontamination, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Introduction

In recent years, single-cell and single-nucleus RNA-sequencing (sxRNA-seq) have revolutionized
the field of genomics by enabling the interrogation of gene expression profiles at the resolution of
individual cells. This technology enables researchers to unravel cellular heterogeneity, identify rare
cell populations, and shed light on dynamic cellular processes. However, despite its transformative
potential, sxRNA-seq faces several significant hurdles.

One of hurdles is the presence of ambient RNA. Ambient RNA is defined as extraneous RNA
molecules that are present in the experimental environment, but do not originate from the cell of
interest. It is likely that especially during sample preparation, where harsh experimental conditions
using enzymatic digestion, physical shearing or detergents can lead to unintentional cell lysis or
membrane damage, contaminating intra-cellular RNA molecules may be released. Additional sources
of contamination include barcode swapping in multiplexed experiments, where molecules from one
sample can be incorrectly labelled with a cell barcode from another sample$^1$, cross contamination
between wells$^{2,3}$ and contamination from the environment, such as media or reagents.

The inadvertent inclusion of ambient RNA in sxRNA-seq data can lead to spurious results, impede
accurate cell classification, and confound downstream analyses$^{4,5}$. To tackle the challenge of
ambient RNA in sxRNA-seq, datasets can be improved by computational decontamination which
aims to identify and quantify ambient RNA, distinguishing it from endogenous RNA, and ultimately
remove it to minimize its impact on results. While several decontamination methods have been
introduced, no independent benchmark covering all currently available methods across multiple
datasets is available to highlight their strengths and limitations. This is important for developers to
pinpoint critical areas for further development, and for researchers to select the appropriate tool for
the task.

Here, we present a comprehensive and independent benchmarking of 7 computational
decontamination methods (CellBender, DecontX, FastCAR, scAR, scCDC, SoupX, and
CellClear)$^{3,6-11}$ using both real and synthetic datasets of different complexities, as well as negative
control datasets without ambient contamination. We evaluate the ability of each method to remove
ambient RNA and preserve endogenous biological signals, and the effect thereof on biological
findings. No single method performs the best across all datasets and metrics, yet we recommend
using either CellBender, DecontX or SoupX depending on compute environment, data availability
and prior expectation.

---

[← Benchmarking computational decontamination of ambient RNA](01-benchmarking-computational-decontamination-of-ambient-rna.md) · [Up: contents](index.md) · [Results →](03-results.md)
