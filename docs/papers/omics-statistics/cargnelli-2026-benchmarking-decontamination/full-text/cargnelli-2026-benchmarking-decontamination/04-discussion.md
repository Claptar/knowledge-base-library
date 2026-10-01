---
title: Discussion
source: https://doi.org/10.64898/2026.01.13.699237/
source_file: sources/papers/cargnelli-2026-benchmarking-decontamination/cargnelli-2026-benchmarking-decontamination.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `cargnelli-2026-benchmarking-decontamination.pdf` from [papers/cargnelli-2026-benchmarking-decontamination](https://doi.org/10.64898/2026.01.13.699237/) — papers · cargnelli-2026-benchmarking-decontamination, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Discussion

Ambient RNA is pervasive. Across 97.357 cells and nuclei in 49 real samples, we found that 81.56%
of cells and nuclei contain some level of ambient RNA. The level varies between cells or nuclei
within a sample, between samples within a dataset and between datasets. We found that the
ambient load is generally higher in the single-nucleus RNA-seq samples (average: 11.80%) than the
single-cell RNA-seq samples (average: 7.79%) consistent with previous observations$^{16}$. Within
samples, we did not find any community-standard cell quality parameters that were strongly
predictive of the ambient load within an individual cell or nucleus suggesting that ambient RNA load
is a stochastic sampling process that is not directly related to the quality of the nuclei or cell.
However, the profile of ambient RNA can be accurately estimated using aggregated expression of
both empty droplets and non-empty droplets, and it is associated with the expression frequency and
exon fraction in non-empty drops.

Across datasets, we found that scCDC and FastCAR primarily removes ambient RNA from highly
expressed genes. This skew leads to percentage of ambient RNA being removed, but
simultaneously also limits removal of endogenous RNA. We did not observe a positive impact on
biological interpretation after applying these methods, which could be due to their expression level
bias. CellClear exhibits a similar low ambient RNA removal but has the inverse bias removing
ambient RNA primarily from lowly expressed genes. CellClear also significantly alters the
endogenous profile, removing approximately as many endogenous RNA counts as ambient RNA
counts. DecontX and SoupX rank in the middle in terms of ambient RNA removal and overall,
preserves endogenous RNA well. Although SoupX has a slightly larger bias towards being more
effective at removing ambient RNA from highly expressed genes than DecontX, they both exhibit a
low bias, and they both can improve biological interpretation. Finally, CellBender and scAR are the
most effective at removing ambient RNA. Both methods tend to introduce new counts for lowly
expressed genes, but unlike CellBender, which generally preserves endogenous RNA and positively
impacts biological interpretation, scAR aggressively removes endogenous RNA counts leading to
removal of a large percentage of cells in several samples and does not have a strong positive impact
on biological interpretation.

In conclusion, we advise the use of either CellBender, DecontX in full mode or SoupX in reduced
mode. The choice between the three should be guided by several criteria: expected performance,
prior expectation for contamination, usability and scalability (Figure 5, Supplemental Table S5). All
methods have adequate documentation. However, only SoupX in reduced mode can be applied to
datasets without access to a full count matrix, and CellBender has the highest demand for
computational resources, requiring access to a GPU, long processing times, higher peak memory
requirements and calls putative cell-containing droplets. The prior expectation for contamination is
important, as CellBender and DecontX in full mode are more prone to over-correction in the absence
of ambient RNA than SoupX in reduced mode. The prior expectation should be informed
experimentally, for example single-nucleus RNA-seq generally have more ambient RNA
contamination than single-cell RNA-seq$^{17}$ and potentially computationally, where methods such as
AmbiQuant$^{17}$ may be used to infer sample-level contamination. Finally, the expected performance
can be inferred from our benchmark, and although no method is universally best, CellBender has the
best overall performance, which is driven by ambient RNA removal and retaining endogenous RNA
(Figure 5) followed closely by DecontX in full mode, which removes less ambient RNA, but improves
biological interpretation more than CellBender and then SoupX in reduced mode. Thus, for a
contaminated dataset, we recommend CellBender or DecontX in full mode. Finally, if there is no prior
expectation for contamination, or only filtered count matrices are available, we recommend SoupX in
reduced mode. However, we do note that applying these methods does not always improve data
quality, even in contaminated datasets.

In addition to guiding method choice, our benchmark can serve to guide developers to build better
computational decontamination methods. To that end, we have made our approaches entirely open
source, such that the benchmark can be continuous, adding new tools and updating existing ones
as they are evolving, as well as open for parameter optimization.

In addition to algorithmic advances, a key limitation in building better decontamination methods is
the availability of suitable datasets, where ambient RNA can be quantified in an unbiased manner.
Here, we have used multiple complementary approaches for defining ground truth, each with distinct
strengths and limitations. We used synthetic data generated by sampling reads from pure cell line
expression profiles, mixed in defined ratios. While this provides a well-defined ground truth, the
sampling approach might be too simplistic as it does not capture higher-order structures, such as
gene-gene covariance, that are present in real data, which may influence decontamination
performance. We also used species mixing experiments, where cells or tissues originating from
different species are mixed prior to performing the experiment. The data is aligned to a hybrid
genome, and ambient RNA is quantified using reads mapping to species X genes within cells
assigned to species Y. This provides a robust ground truth if ambitiously aligned reads are excluded.
However, the feature spaces of endogenous and contaminating RNA molecules do not overlap,
which differs from real datasets and may bias decontamination performance. Finally, we used a
strain mixing experiment, where tissues from different strains of mice were mixed prior to the
experiment. Here, ambient RNA is identified through strain-specific SNPs detected in cells from
another strain. This enables accurate measurement of contamination, but only for a subset of genes,
limited by expression levels and genetic variation, which may also introduce bias. Taken together,
these complementary strategies help mitigate individual limitations and enable more balanced
performance assessment. However, further progress will require new experimental designs in which
endogenous and ambient RNA share the same feature space, while contamination can still be
measured accurately and without bias across all genes.

---

[← Results](03-results.md) · [Up: contents](index.md) · [References →](05-references.md)
