---
title: Introduction
source: https://doi.org/10.1093/gigascience/giaa151/
source_file: sources/papers/young-behjati-2020-soupx/young-behjati-2020-soupx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `young-behjati-2020-soupx.jats` from [papers/young-behjati-2020-soupx](https://doi.org/10.1093/gigascience/giaa151/) — papers · young-behjati-2020-soupx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

Droplet-based single-cell RNA sequencing (scRNA-seq) has enabled quantification of the transcriptomes of hundreds of thousands of cells in single experiments [1,2]. This technology underpins recent advances in understanding normal and pathological cell behaviour [3–8]. Moreover, large-scale efforts to create a ”Human Cell Atlas" critically depend on the accuracy and cellular specificity of the transcriptional readout produced by droplet-based scRNA-seq [9,10].

A core assumption of droplet-based scRNA-seq is that each droplet, within which molecular tagging and reverse transcription take place, contains messenger RNA (mRNA) from a single cell. Violations of this assumption, which may distort the interpretation of scRNA-seq data, are common in practice. Clear examples include droplets that contain multiple cells (doublets), and empty droplets. Attempts to detect and remove doublets are an active area of research [11–13].

Another phenomenon that violates this assumption is the sequencing of cell-free RNA from the input solution, admixed with a cell in its enclosing droplet. It is recognized that these contaminating non-endogenous RNAs are present even within datasets of the highest quality [2]. Here, we show that this "soup" of cell-free mRNAs is ubiquitous and non-negligible in magnitude. Because the character and extent of ambient mRNA contamination varies by experiment, with increased contamination in necrotic or complex samples, ambient mRNAs may significantly confound the biological interpretation of scRNA-seq data. We present SoupX, a method for quantifying the extent of ambient mRNA contamination whilst purifying the true, cell-specific signal from the observed mixture of cellular and exogenous mRNAs.

In this article we begin by briefly describing the SoupX method. Following this we consider a range of datasets, summarized in Supplementary Table S1. We first investigate 2 “species mixing” datasets run on the Chromium 10X [2] and DropSeq [14] platforms, which allow us to directly identify contaminating mRNAs and test our method’s accuracy. We then demonstrate how SoupX can be applied in practice using a dataset of peripheral blood mononuclear cells (PBMCs) [2]. We further explore the biological benefits of SoupX using a complex "kidney tumour" dataset, which consists of 12 kidney tumour biopsies [15]. As a final test, we apply our method to human fetal liver data [16]. We conclude with some general remarks about ambient RNA contamination, other tools to correct for its effect, and the consequences of failing to account for the presence of ambient RNAs.

---

[Up: contents](index.md) · [The SoupX Method →](02-the-soupx-method.md)
