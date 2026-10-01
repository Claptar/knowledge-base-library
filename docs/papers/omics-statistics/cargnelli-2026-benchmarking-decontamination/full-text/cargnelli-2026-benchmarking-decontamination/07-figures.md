---
title: Figures
source: https://doi.org/10.64898/2026.01.13.699237/
source_file: sources/papers/cargnelli-2026-benchmarking-decontamination/cargnelli-2026-benchmarking-decontamination.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `cargnelli-2026-benchmarking-decontamination.pdf` from [papers/cargnelli-2026-benchmarking-decontamination](https://doi.org/10.64898/2026.01.13.699237/) — papers · cargnelli-2026-benchmarking-decontamination, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Figures

## Figure 1: Setup for benchmarking ambient RNA removal methods.

Schematic diagram showing the benchmarking workflow. Three species-mixing, genotype-mixing,
simulated, and negative control datasets were processed using 7 state-of-the-art ambient RNA
removal tools and evaluated in terms of their ability to remove ambient RNA, conserve endogenous
gene expression and effect on cell type labelling, clustering, and markers. Based on these, we
provide recommendations for different methods depending on which types of data are available.

The diagram shows three columns: "Ground truth strategy" (Species mixing, with varying Complexity;
Genotype mixing; Synthetic data; Control, Smart-seq2), feeding into "Computational decontamination
tools" (CellBender, scAR, FastCAR, DecontX, SoupX, scCDC, CellClear), feeding into "Evaluation"
(Remove ambient / retain endogenous; Neighborhood similarity, Marker genes, Cluster quality; Label
transfer, Species labels).

## Figure 2: Characteristics of ambient RNA.

**A)** Histogram or ridge plots of ambient load (fraction of total UMIs not derived from the cell) for
each cell for the indicated datasets and samples. **B)** Scatterplot showing the ambient load on
genes and their expression level in empty droplets. **C)** Scatterplot showing ambient load on genes
and their endogenous expression frequency. **D)** Barplot showing the percentage of variance in
ambient load across cells explained by cellular parameters, including the fraction of UMIs mapped to
exons (Exons), mitochondrial genes (Mito), to protein-coding genes (PC), to ribosomal genes (Ribo),
as well as the total number of UMIs (UMIs) and features detected (Feat).

The panel row A shows, from left to right, a histogram and three ridge plots of "Percent of cells" /
"Samples" against "Ambient load (%)" for four datasets. Row B shows four scatterplots of
log(ambient expr.) against log(background expr.). Row C shows four scatterplots of log(ambient
expr.) against endogenous expr. freq. Row D shows four barplots of "Explained variance (%)" against
cellular parameters (Exons, Feat, Mito, PC, Ribo, UMIs).

## Figure 3: Method performance.

**A)** Dotplot of ambient removal scores (shown by color) and endogenous retain scores (shown by
dot size) for all seven methods. For SoupX and DecontX, reduced mode (RED) runs were also
included that only use filtered matrices across all seven datasets. **B)** Scatterplot showing the
fraction of endogenous RNA retained and ambient RNA removed for all datasets. The color of the dot
indicates the method. **C)** Scatterplot showing the fraction of endogenous RNA retained and the
logged sum of UMIs for each gene after scAR correction in the low complexity species-mixing
dataset.

Panel A is a dotplot with methods (CellBender, CellClear, FastCAR, DecontX, SoupX, DecontX$^{RED}$,
SoupX$^{RED}$, scAR, scCDC) as rows and dataset categories (Low/Med/High species mixing, Strain
mixing, Syn/SS2 synthetic, Negative control) as columns, with a color scale for "Ambient removal
score" (Best to Worst) and a size scale for "Endogenous retain score" (Best to Worst). Panel B plots
"Fraction endogenous RNA retained" (y-axis) against "Fraction ambient RNA removed" (x-axis), with
points colored by method (SoupX$^{RED}$, SoupX, FastCAR, DecontX$^{RED}$, scCDC, CellClear, CellBender,
scAR, DecontX). Panel C plots "Fraction endogenous RNA retained" (y-axis, from -1.00 to 1.00)
against "log UMIs" (x-axis, 0 to 15).

## Figure 4: Influence of ambient RNA on biological interpretation.

**A)** UMAP embeddings of a synthetic dataset showing the ground truth, as well as the observed
data after ambient contamination (uncorrected) and after correction of the observed data for the
indicated methods. Each dot was colored in cell type colors if correctly assigned using unsupervised
clustering, or in red if misassigned. **B)** Barplot showing average module scores for marker genes
defined in the ground truth dataset from A. **C-F)** Dotplots showing the average of the indicated
metrics relative to the uncorrected data for contaminated or control datasets across four different
tasks: cellular neighborhood similarity (C), marker gene selectivity (D), batch integration (E) and
label transfer (F).

Panel A shows UMAP embeddings (labelled UMAP1 vs UMAP2) for: Ground truth, Uncorrected
(ARI = 0.92), CellBender (ARI = 0.94), CellClear (ARI = 0.44), scAR (ARI = 0.87), DecontX
(ARI = 0.91); and in a second row: DecontX$^{RED}$ (ARI = 0.92), SoupX (ARI = 0.81), SoupX$^{RED}$
(ARI = 0.81), FastCAR (ARI = 0.69), scCDC (ARI = 0.90). Cells are colored by labels HCC1500,
HS578T, MCF12A, or Misassignment. Panel B is a barplot of "Average module score" (y-axis, 0 to
0.6) for Uncorrected, scAR, CellBender, SoupX, SoupX$^{RED}$, DecontX, DecontX$^{RED}$, CellClear, scCDC,
FastCAR, with a dashed reference line near 0.5. Panels C-F are dotplots of methods (scAR,
CellBender, SoupX, SoupX$^{RED}$, DecontX, DecontX$^{RED}$, CellClear, scCDC, FastCAR) against
"Contaminated" and "Controls" columns, for metrics Purity/LISI (C), Entropy/Moran's I/Gini (D),
LISI/bASW/PCR/ARI (E), and Purity/RMSE/cASW/ARI (F), each colored by "Relative to uncorrected"
score.

## Figure 5: Summary of benchmark.

Qualitative and quantitative characteristics of each tested methods summarized across datasets and
tasks.

| Method | CellBender | CellClear | scAR | DecontX | DecontX$^{RED}$ | SoupX | SoupX$^{RED}$ | FastCAR | scCDC |
|---|---|---|---|---|---|---|---|---|---|
| Runtime (h:mm:ss) | 1:11:15 | 1:58:51 | 29:06 | 3:14 | 5:11 | 1:44 | 1:21 | 0:30 | 8:04 |
| Uses GPU | Yes | No | Yes | No | No | No | No | No | No |
| Peak memory (Gigabytes) | 22.54 | 50.56 | 27.19 | 10.75 | 7.45 | 15.02 | 12.99 | 5.39 | 29.53 |
| Documentation | Excellent | Very poor | Excellent | Good | Good | Good | Good | Fine | Good |
| Language | Python | Python | Python | R | R | R | R | R | R |
| Input format | Raw | Raw / Filtered | Filtered* | Raw / Filtered | Filtered | Raw / Filtered | Filtered* | Raw / Filtered | Filtered* |
| Ambient removal | 0.604 ± 0.328 | 0.100 ± 0.130 | 0.679 ± 0.240 | 0.391 ± 0.242 | 0.370 ± 0.278 | 0.297 ± 0.188 | 0.361 ± 0.224 | 0.198 ± 0.442 | 0.201 ± 0.446 |
| Endogenous retainment | 0.877 ± 0.084 | 0.662 ± 0.301 | 0.444 ± 0.200 | 0.890 ± 0.085 | 0.950 ± 0.049 | 0.939 ± 0.062 | 0.944 ± 0.058 | 0.927 ± 0.144 | 0.983 ± 0.046 |
| Biological interpretation | 0.524 | 0.527 | 0.473 | 0.741 | 0.505 | 0.396 | 0.440 | 0.167 | 0.428 |
| Overcorrection score | 0.712 | 0.439 | 0.137 | 0.804 | 0.836 | 0.818 | 0.842 | 0.420 | 0.720 |
| Overall | 1 | 9 | 7 | 2 | 4 | 5 | 3 | 8 | 6 |

---

[← Methods and materials](06-methods-and-materials.md) · [Up: contents](index.md)
