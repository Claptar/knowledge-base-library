---
title: StagewiseTesting Part 03 —
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf
source_file: sources/statomics-sga21/docs/stagewiseTesting.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`docs/stagewiseTesting.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# StagewiseTesting Part 03 —

Koen Van den Berge$^{1,2}$, Charlotte Soneson$^{3,4}$, Mark D. Robinson$^{3,4}$ and Lieven Clement$^{1,2*}$

## Abstract

RNA sequencing studies with complex designs and transcript-resolution analyses involve multiple hypotheses per gene; however, conventional approaches fail to control the false discovery rate (FDR) at gene level. We propose stageR, a two-stage testing paradigm that leverages the increased power of aggregated gene-level tests and allows post hoc assessment for significant genes. This method provides gene-level FDR control and boosts power for testing interaction effects. In transcript-level analysis, it provides a framework that performs powerful gene-level tests while maintaining biological interpretation at transcript-level resolution. The procedure is applicable whenever individual hypotheses can be aggregated, providing a unified framework for complex high-throughput experiments.

**Keywords:** RNA-sequencing, Stage-wise testing, Differential transcript usage, Differential expression

## Background

High-throughput sequencing (HTS) technology has become the dominant platform for transcriptome profiling. It is agnostic of genomic annotation, has a broad dynamic range and allows data aggregation on different biological levels (basepair, exon, gene) [1–4]. Recent developments in read alignment provide fast transcript-level quantification [3, 5, 6], opening the way to assess differential transcript expression (DTE) and differential transcript usage (DTU), which for instance has been shown to be associated with Parkinson’s disease [7] and resistance to prostate cancer treatment [8]. In DTE, differential expression between conditions is assessed at the individual transcript level, while in DTU the relative expression of the isoforms of a gene are compared between conditions; i.e. a DTU analysis aims at discovering differences in the proportions of the expressed isoforms of a gene.

*Correspondence: lieven.clement@ugent.be
$^1$Department of Applied Mathematics, Computer Science and Statistics, Ghent University, Krijgslaan 281, S9, 9000 Ghent, Belgium
$^2$Bioinformatics Institute Ghent, Ghent University, 9000 Ghent, Belgium
Full list of author information is available at the end of the article

The dramatic sequencing cost reduction has also enabled researchers to set up studies with complex experimental designs involving many samples [9]. Analysis of DTU, DTE or traditional RNA-seq studies with complex designs typically involves multiple hypotheses of interest for each gene, e.g. for each transcript in a DTU and DTE context or for every treatment effect at each timepoint and the treatment-time interactions in time course differential gene expression (DGE) studies. The current consensus is to control the false discovery rate (FDR) on the hypothesis level, which we argue to be suboptimal with respect to statistical power and the downstream biological interpretation and validation that typically occur on a gene level. Soneson et al. [10] have shown that DTE analysis has higher performance when evidence on all individual transcripts is aggregated at the gene level due to the different null hypothesis and the larger amount of data that is available than for tests at the individual hypothesis level. This also occurs for DTU (see Fig. 1). Inference using p values of a DEXSeq [2] analysis on transcript counts also has a lower power than aggregating transcript-level p values to the gene level prior to FDR calculation. But, the latter does not provide identification of the specific transcripts that are differentially used; thus, higher sensitivity comes at the cost of a lower biological resolution.

In differential expression (DE) studies with complex designs, it is common practice to adopt multiple testing at the hypothesis level. This results in low power for discovering interaction effects since their standard error is typically much larger than for the main effects. Testing the treatment-time interaction effect in the cross-sectional time-series RNA-seq study from Hammer et al. (2010) [11] with limma-voom [12], for instance, returns no significant genes at a 5% FDR level, while more than 6000 genes are flagged when testing for treatment effects within a particular timepoint. Hence, the higher resolution on the hypothesis level comes at the expense of a low power for the interaction effect. In addition, FDR control on the hypothesis level does not guarantee FDR control on the gene level, because multiple hypotheses are assessed per gene, and the expected ratio of the number of genes with at least one false positive (false positive genes) to all positive genes in the union across hypotheses will be larger than the target FDR. For example, if three hypotheses are assessed with 5% false positives in the top-list for every contrast, then the aggregated top-lists will still contain 5% false positives. However, since the false positives in the different contrasts may be derived from different genes, the number of genes with false positives will increase with the number of hypotheses tested, while the total number of genes remains fixed. Thus, the gene-level FDR will be inflated if multiple hypotheses are of interest. This can lead to lower success rates of subsequent validation, since many genes without true treatment effects may be considered significant. In the RNA-seq literature, however, there is no consensus on how to combine the enhanced power of aggregation with an adequate resolution for the biological problem at hand. We argue that the multiple hypotheses at the gene level can be exploited in a two-stage testing procedure (Fig. 2) [13–15]. In the screening stage, genes with effects of interest are prioritised using an omnibus test, e.g. a global F test, a global likelihood ratio test or by aggregating p values. Assessing the aggregated null hypothesis has the advantages of (1) high sensitivity in a DTU/DTE context; (2) enriching for genes with significant interaction effects in complex DE studies, thereby boosting power; and (3) providing gene-level FDR control. In the confirmation stage, individual hypotheses are assessed for genes that pass the screening stage. Hence, it has the merit to combine the high power of aggregated hypothesis tests in stage I with the high resolution of individual hypothesis testing in stage II.

The suggested strategy positions itself in the larger framework of stage-wise testing procedures for high-throughput experiments. Lu et al. [16] previously proposed a two-stage strategy for microarrays based on mixed models, which is inapplicable to HTS data due to the violation of the distributional assumptions. Jiang and Doerge [13] proposed a generic two-stage DE analysis procedure where the first stage corresponds to testing a global null hypothesis, i.e. testing whether at least one hypothesis is false, after which post hoc tests are considered only for the significant genes. Their algorithm,

---

[← Power Issue Transcript Level Analysis](02-power-issue-transcript-level-analysis.md) · [Up: contents](index.md)
