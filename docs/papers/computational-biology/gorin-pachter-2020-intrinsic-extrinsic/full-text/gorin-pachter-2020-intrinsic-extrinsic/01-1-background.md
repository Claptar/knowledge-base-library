---
title: 1 Background
source: https://doi.org/10.1101/2020.09.25.312868/
source_file: sources/papers/gorin-pachter-2020-intrinsic-extrinsic/gorin-pachter-2020-intrinsic-extrinsic.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2020-intrinsic-extrinsic.pdf` from [papers/gorin-pachter-2020-intrinsic-extrinsic](https://doi.org/10.1101/2020.09.25.312868/) — papers · gorin-pachter-2020-intrinsic-extrinsic, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Background

Gennady Gorin$^1$ and Lior Pachter$^2$

$^1$Division of Chemistry and Chemical Engineering, California Institute of Technology, Pasadena, CA, 91125

$^2$Division of Biology and Biological Engineering & Department of Computing and Mathematical Sciences, California Institute of Technology, Pasadena, CA, 91125

*Address correspondence to Lior Pachter (lpachter@caltech.edu)

September 25, 2020

## Abstract

Intrinsic and extrinsic noise sources in gene expression, originating respectively from
transcriptional stochasticity and from differences between cells, complicate the determination of
transcriptional models. In particularly degenerate cases, the two noise sources are altogether
impossible to distinguish. However, the incorporation of downstream processing, such as the mRNA
splicing and export implicated in gene expression buffering, recovers the ability to identify the
relevant source of noise. We report analytical copy-number distributions, discuss the noise
sources' qualitative effects on lower moments, and provide simulation routines for both models.

Recent improvements in single-cell transcriptomics, including increasingly sensitive
fluorescence- and sequencing-based methods, have begun to provide data useful for discriminating
between competing biophysical models. One immediate application of interest is that of
*intrinsic* and *extrinsic* cellular gene expression noise, which has already been studied directly
from mRNA reporter statistics [1, 2]. While experimental and statistical methods for measuring the
relative contributions of intrinsic and extrinsic noise are relatively advanced [3, 10],
microscopic models of cell-to-cell variability are less well developed. These models are necessary
in light of recent methods for measuring the molecular state of cells, which offer routes to better
mechanistic understanding, but present a number of new challenges in controlling noise sources.

While the introduction of single-cell RNA sequencing (scRNA-seq) data with unique molecular
identifiers (UMIs) provides measurements of a substantial fraction of transcripts in individual
cells [7], the resulting copy-number data are discrete, and thus challenging to model with existing
methods that largely focus on continuous-valued fluorescence readouts. The biochemistry of
scRNA-seq also generally relies on the capture of polyadenylated sequences in fixed media [8],
which limits the scope of assays, and is not directly compatible with *in vivo* experimental methods
relying on the integration of multiple fluorescent reporters to distinguish between the sources of
noise [3]. Furthermore, the analysis of lower moments of gene expression has been shown to be
insufficient for the identification of biophysical parameters even for purely intrinsic noise
models [9], suggesting that full copy-number distributions are necessary for modeling more complex
systems with multiple sources of noise.

Another challenge lies in theory; ideally, analytical results will be available to provide
qualitative interpretability and guide computational approaches, but many current methods are
purely numerical. For example, while methods for the explicit description of extrinsic noise are
formally available, in the context of a transcriptional model, the incorporation of extrinsic noise
typically corresponds to the construction of a mixture model with parameter values drawn from a
distribution [2, 3, 10]. Under this construction, full analytical solutions are only available in
the simplest cases.

---

[Up: contents](index.md) · [2 Two models for gene expression →](02-2-two-models-for-gene-expression.md)
