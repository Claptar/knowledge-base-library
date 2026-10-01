---
title: Benchmarking computational decontamination of ambient RNA
source: https://doi.org/10.64898/2026.01.13.699237/
source_file: sources/papers/cargnelli-2026-benchmarking-decontamination/cargnelli-2026-benchmarking-decontamination.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `cargnelli-2026-benchmarking-decontamination.pdf` from [papers/cargnelli-2026-benchmarking-decontamination](https://doi.org/10.64898/2026.01.13.699237/) — papers · cargnelli-2026-benchmarking-decontamination, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Benchmarking computational decontamination of ambient RNA

## Author list

Cecilie Bøgh Cargnelli$^1$, Jakob Vennike Nielsen$^1$, Jesper Grud Skat Madsen$^{1,2,3\dagger}$

## Affiliations

$^1$ Department of Biochemistry and Molecular Biology, University of Southern Denmark, Odense M, 5230, Denmark

$^2$ Center for Functional Genomics and Tissue Plasticity (ATLAS), Odense M, 5230, Denmark

$^3$ The Novo Nordisk Foundation Center for Genomic Mechanisms of Disease, Broad Institute of MIT and Harvard, Cambridge, MA 02142, USA

† Corresponding author. Email: jgsm@bmb.sdu.dk

## Abstract

Gene expression profiling of single cells using single-cell and single-nucleus RNA sequencing
(sxRNA-seq) enables researchers to characterize cellular heterogeneity and unraveling complex
biological processes at unprecedented resolution. However, sxRNA-seq faces challenges due to the
presence of ambient RNA, extraneous RNA molecules not originating from the cells of interest.
Sample preparation is a major source of ambient RNA, where harsh conditions can lead to cell
lysis and the release of intracellular RNA. This inescapable inclusion of ambient RNA can cause
erroneous results and hinder downstream analyses. To address this issue, various methodologies
have been developed to identify, quantify, and remove ambient RNA. Here, we rigorously evaluate 7
state-of-the-art methodologies for ambient RNA removal using simulated datasets, species-mixing
experiments of varying complexities, and genotype-mixing experiments. We find that no single
method performs the best across all datasets and metrics, but CellBender, DecontX and SoupX
generally perform well.

---

[Up: contents](index.md) · [Introduction →](02-introduction.md)
