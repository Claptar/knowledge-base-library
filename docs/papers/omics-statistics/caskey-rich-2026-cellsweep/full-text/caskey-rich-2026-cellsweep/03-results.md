---
title: Results
source: https://doi.org/10.64898/2026.03.04.709349/
source_file: sources/papers/caskey-rich-2026-cellsweep/caskey-rich-2026-cellsweep.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `caskey-rich-2026-cellsweep.pdf` from [papers/caskey-rich-2026-cellsweep](https://doi.org/10.64898/2026.03.04.709349/) — papers · caskey-rich-2026-cellsweep, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Results

**Model.** CellSweep models the observed counts corresponding to a given barcode as a mixture of
three biologically interpretable sources: cell-type expression $\boldsymbol{p}^k$, ambient
contamination $\boldsymbol{a}$, and bulk contamination $\boldsymbol{m}$ (Fig. 1B), where
$\boldsymbol{p}^k$, $\boldsymbol{a}$, and $\boldsymbol{m}$ are vectors where each entry is the
count assigned to that gene. We assume that all barcodes share a global bulk contamination
fraction $\beta$ and that each barcode $i$ also has an individual ambient contamination fraction
$\alpha_i$. For a cellular barcode $i$, with one-hot encoded cell-type assignment $\gamma_i$, the
expected expression distribution is:

$$\chi_i = (1-\beta)\left[\alpha_i \boldsymbol{a} + (1-\alpha_i)\sum_{k=1}^{K}\gamma_i^k
\boldsymbol{p}^k\right] + \beta \boldsymbol{m}. \qquad (1)$$

Conditioning on the total UMI count $T_i$, we model the observed counts as:

$$\boldsymbol{C}_i \sim \text{Multinomial}(T_i, \chi_i), \qquad (2)$$

similar in spirit to the multinomial formulations in DecontX, SoupX, and scAR (Fig. 1B).

The CellSweep model assumes that cell-types are defined prior to inference with an arbitrary
clustering or annotation method. Throughout this paper, we use CellTypist (Conde et al., 2022) to
initialize the cell-type labels and determine the number of cell-types $K$ unless otherwise
specified.

Following approaches such as scAR and SoupX, CellSweep exploits the large number of non-cellular
barcodes in typical datasets to obtain an empirical estimate of the ambient RNA profile. Since
non-cellular barcodes contain only background RNA, their aggregated feature distribution provides
a high-precision ambient estimate. After identifying non-cellular barcodes (e.g., via EmptyDrops
or a hard threshold based on the knee-plot) (Lun et al., 2019), CellSweep normalizes their counts
to obtain the ambient profile $\boldsymbol{a}$, yielding a stable and unbiased estimator.

A central distinguishing feature of CellSweep is its use of the classical
expectation–maximization (EM) algorithm for parameter inference (Dempster et al., 2018). In
contrast to models such as CellBender, DecontX, and scAR, which rely on variational inference or
deep generative architectures to approximate complex posteriors, CellSweep adopts a fully
tractable generative likelihood that admits closed-form E- and M-steps. This yields substantial
computational advantages: the E-step decomposes independently across cells and can therefore be
parallelized with near-perfect scalability, while the M-step consists of simple normalized updates
for the mixture components. As a result, the optimization procedure is both faster and more stable
than variational approaches, without the need for stochastic gradient updates, neural-network
architectures, or amortized inference. Although methods such as SoupX also avoid variational
inference, their heuristics do not provide a unified probabilistic treatment of all sources of
contamination. CellSweep thus achieves a balance of interpretability, computational efficiency,
and modeling flexibility that distinguishes it from existing decontamination frameworks.

**An Alternative Model for Datasets without Non-Cellular Barcodes.** The default CellSweep model
assumes the presence of a sufficient number of non-cellular barcodes to obtain a reliable
estimate of the ambient RNA profile. However, not all single-cell RNA-seq technologies produce
non-cellular barcodes. In particular, well-based protocols such as Smart-seq2 may contain no
non-cellular barcodes at all, yet still exhibit substantial ambient or bulk contamination. To
broaden the applicability of CellSweep across scRNA-seq technologies, we introduce an alternative
model that does not require non-cellular barcodes for inference.

In this alternative formulation, inspired by the approach used in DecontX, we assume that ambient
background RNA arises from a mixture of cell-type expression profiles. Specifically, we model the
ambient profile as a combination of the inferred cell-type profiles,

$$\boldsymbol{a} = \sum_{k=1}^{K} u^k \boldsymbol{p}^k, \qquad (3)$$

These mixture weights $u^k$ are treated as latent parameters and are iteratively updated within
the expectation–maximization (EM) framework.

This formulation is motivated by the observation that the ambient pool originates from lysed
cells and therefore should approximate a mixture of cell-type expression profiles. However, it
does not account for features that may be disproportionately represented in the ambient pool,
such as mitochondrial transcripts released through organelle lysis (Gorin and Goodman, 2026).

**Background removal in mixed-species experiments.** Background contamination in single-cell
genomics data is readily identifiable in mixed-species experiments, when cells from two distinct
species are processed and sequenced together. Ideally, all the reads associated with a barcode
should originate from a single species. In practice, ambient contamination results in substantial
off-target species counts.

We applied CellSweep and other methods to a publicly available human–mouse mixture dataset from
10x Genomics (Fig. 2). We removed doublets prior to analysis for all methods (see Supplementary
Methods). This preprocessing step ensures that residual off-target counts primarily reflect
ambient and bulk contamination rather than true biological mixtures. Most cells exhibit a small
but meaningful amount of contamination, with a mean contamination of 1.25% for human cells and
2.93% for mouse cells. An ideal background-removal method would eliminate such cross-species
counts while preserving same-species signal, although some removal of same-species counts is
expected due to non–species-specific contamination.

**Fig. 1.** CellSweep overview. (A) Sources of ambient noise in "shell"/droplet technologies
(top), "cell"/combinatorial barcode technologies (middle), and "well" technologies (bottom). (B)
Diagram of the CellSweep model. Observed variables are shown as squares and latent variables as
circles. The lower half shows the plate diagram for the multinomial generative model, and the
upper half depicts the decomposition of $\chi_i$ into ambient, cell-type, and bulk components.

Fig. 2A-B summarizes the performance of CellSweep, and Fig. S1 summarizes the performance of
SoupX, CellBender, DecontX, and scAR. For each approach, we show (i) the remaining cross-species
counts per cells after denoising and (ii) the change in human and mouse UMI counts for each cell.
Scatterplots describing the effect of each tool on the matrix entries, cells, and genes before vs.
after processing are described in Fig. S2.

CellSweep removes cross-species contamination more consistently than all other methods tested
(Fig. 2, Fig. S1). Across all cells, CellSweep reduces mouse gene contamination by 98.84% and
human gene contamination by 98.59%, while retaining 97.85% of true-species counts in human cells
and 98.46% in mouse cells. All other methods retain at least 97% of true species counts for both
mouse and human, but fail to decontaminate all cells. CellBender and scAR substantially reduce
cross-species contamination for most cells. CellBender removes 94.52% of mouse gene contamination
and 97.29% of human gene contamination (Fig. S1C-D), while scAR removes 98.88% and 98.86%,
respectively (Fig. S1G-H). However, both CellBender and scAR have a small handful of cells where
over 90% of noise is retained. SoupX and DecontX remove relatively little cross-species
contamination overall and display greater variability across cells. SoupX removes 87.97% of
mouse gene contamination and only 66.65% of human contamination (Fig. S1A-B), while DecontX
removes 81.57% and 68.25%, respectively (Fig. S1E-F). DecontX exhibits additional failures. After
decontamination, DecontX retains cross-species noise directly proportional to the number of
true-species counts, resulting in cells that appear to lie along a 45 degree line on the scatter
plot. DecontX also removes nearly all counts from a small handful of cells and very little from
others (Fig. S1F).

**Fig. 2.** CellSweep effectively removes noise from human-mouse mixture data. (A) Histogram of
total cross-species counts across all genes per cell after processing with CellSweep in a 10x
dataset. (B) Joint scatterplot of mouse vs. human total counts per cell after processing with
CellSweep in a 10x dataset. (C-D) Same as (A-B) in a Smart-seq2 dataset. (E-F) Same as (A-B) but
in an ATAC-seq dataset. Light orange = mouse cells, raw; light blue = human cells, raw; dark
orange = mouse cells, processed; dark blue = human cells, processed.

To further assess the performance of CellSweep, we computed the area under the curve (AUC) of
off-target UMIs across cells for both mouse contamination in human cells and human contamination
in mouse cells. In the raw data, these AUC values were 3,433,952.69 and 19,332,043.67,
respectively. CellSweep reduced these values to 958.64 and 1279.02, which is substantially lower
than those achieved by SoupX (159,153.52 and 392,445.66), CellBender (136,480.40 and 456,481.74),
DecontX (154694.48 and 11136.65), and scAR (83,604.30 and 110,136.32).

In addition to droplet-based technologies, the alternative CellSweep model can be used to remove
noisy counts from well-based data. CellSweep reduces cross-species noise while retaining nearly
all signal in a human-mouse mixture 685 cell scRNA-seq dataset generated with Smart-Seq 2
technology (Fig. 2C-D). On average, CellSweep retain 99.98% of signal in human cells and 99.80% of
signal in mouse cells, while reducing human cell noise from 0.13% to 0.08%, and reducing mouse
cell noise from 0.17% to 0.06%. Because of the nature of Smart-seq2 technology, many more counts
are observed per cell compared to a typical cell from a 10x technology (on the order of 100,000
vs. 10,000 counts per cell, respectively), although both technologies have an average of
approximately 1% ambient noise in these cells.

CellSweep is also useful for genomics assays other than scRNA-seq. We applied CellSweep to a 10X
Genomics human-mouse mixture single-cell ATAC-seq dataset (Fig. 2E-F), and found that, just as
with single-cell RNA-seq, CellSweep can reduce cross-species noise in ATAC-seq.

**Spatial transcriptomics.** We ran CellSweep on a human/mouse Visium HD dataset in which cells
from a human colorectal cancer cell line were grafted in a mouse. As with non-spatial
droplet-based scRNAseq data, this dataset demonstrated a knee plot with a sharp inflection point,
indicating hundreds of thousands of cells with fewer than 10 UMI counts (Fig 3A). After running
CellSweep, much of the cross-species gene contamination is removed from human cells, with very
little signal removed (Fig. 3B). Most of the 249,802 cells have a predicted ambient noise fraction
$\alpha_i$ near 0, although 40% of cells have a fraction over 0.1, and 9% of cells have a fraction
over 0.5 (Fig. 3C). When visualizing predicted ambient noise fraction over spatial location, cells
with a high $\alpha_i$ tend to lie along the edge of the tissue, indicating edge artifacts
(Kummerfeld et al., 2025). In contrast, cells with a low $\alpha_i$ aggregated near the center of
the tissue (Fig 3D).

**Fig. 3.** CellSweep predicts spatial localization of ambient noise in a human-mouse colorectal
cancer xenograft Visium HD dataset. (A) Knee plot. (B) Joint scatterplot of mouse vs. human total
counts per cell after processing with CellSweep. Light orange = mouse cells, raw; light blue =
human cells, raw; dark orange = mouse cells, processed; dark blue = human cells, processed. (C)
Histogram of alpha_hat (CellSweep's predicted fraction of ambient noise per cell). (D) Spatial
heatmap of binned alpha_hat values.

**Fig. 4.** CellSweep effectively removes noise from a human PBMC 8k dataset. (A) Scatterplot of
matrix values after vs. before processing with CellSweep. (B) Scatterplot of total cell counts
after vs. before processing with CellSweep. (C) Dotplots of markers from monocytes/neutrophils,
monocytes/pDCs, and broad expression in raw (left) and processed (right) data with CellSweep.
(D-F) Same as (A-C) but with SoupX.

**Increased Cell-Type Marker Specificity in PBMC Data.** Background contamination in scRNA-seq
data reduces marker specificity and introduces spurious off-target expression that can propagate
into downstream analyses (Janssen et al., 2023). To assess the impact of CellSweep and similar
background-removal tools on biologically meaningful signal recovery, we evaluated performance on
a publicly available 8,000-cell PBMC dataset, following a benchmarking strategy similar to that
of Fleming et al. (2023) (Figs. 4, -S6).

Prior to background correction, several well-known immune marker genes exhibit broad,
non-specific expression across clusters. In particular, S100A8, S100A9, LYZ, CST3, and PTPRC
appear at appreciable levels in nearly all clusters (Fig. 4C, left). However, S100A8 and S100A9
are canonical neutrophil markers, while LYZ and CST3 are primarily associated with monocytes and
plasmacytoid dendritic cells. Their ubiquitous expression in the uncorrected data therefore
reflects technical contamination rather than true biological signal. All tools succeed in removing
counts of monocyte/dendritic cell/neutrophil marker genes from clusters that likely represent
other cell types (Fig. 4C,F, S3C, S3F, S3I). In contrast, PTPRC, a pan-leukocyte marker that is
expected to be broadly expressed across immune cell types, is retained uniformly across clusters
after denoising.

In our benchmark, each tool removes counts to different degrees. The fewest mean counts per cell
removed was by CellBender at 121.29 counts, followed by SoupX at 315.45, CellSweep at 667.88,
DecontX at 770.32, and scAR at 2,647.38. Notably, because of its conservative removal of counts,
CellBender appears to have been the least successful at eliminating marker contamination. SoupX
was the only tool that did not noticeably alter any cells in terms of total counts compared to
the raw matrix (Fig.4E). Overall, scAR was the most agressive denoiser and removed more counts
per cell than any other tool (Fig. S3H).

Comparison of the changes in counts to matrix, total cell, and total gene counts between
CellSweep and other tools reveals that all tools share similarities in their output (Fig. S5). In
descending order of similarity with other tools, CellSweep most resembles DecontX, followed by
SoupX, CellBender, and finally scAR. scAR consistently removes more counts in nearly all cells
compared to CellSweep; all other tools do not possess any considerable trends.

**Noise reduction in a complex multiplexed experiment.** We applied CellSweep to the 8 cubed
founder and Trem2 datasets. These datasets serve as valuable controls because, unlike the
previously-analyzed datasets, they (1) were generated with the Parse Biosciences Evercode WT v2
assay (i.e., non-droplet), (2) are derived exclusively from mouse (i.e., non-human), (3) involve
eight different tissues, (4) are larger and more complex in scale (600,000-900,000 cells per
plate), and (5) demonstrate well-characterized noise (Rebboah et al., 2026).

The 8 cubed founder experiment is designed so that each plate contains two different tissues,
allowing for more accurate downstream quantification of batch effects and plate-specific
contamination (Fig. 5A). CellSweep almost entirely eliminates cross-tissue marker contamination
while retaining tissue-specific markers. We present two representative examples of this result
with the cortex/hippocampus marker Snap25 on plate igvf_003 (Fig. 5B-C) and the adrenal marker
Star on plate igvf_009 (Fig. 5D-E).

The Trem2 dataset, which contains 161,200 cells from all eight tissues sequenced on a single
plate, serves as an additional control. In this data set, CellSweep reduces the count of the liver
marker albumin in all non-liver tissues while leaving counts in the liver relatively intact.
CellSweep demonstrates similar success on the Trem2 dataset with the muscle markers Myh4 and
titin (Fig. S7).

**Idempotency.** As a control, we investigated the performance of programs when run repeatedly on
the same dataset. Ideally, once a dataset is denoised, further denoising should not identify new
noise, i.e. tools should be idempotent. Idempotency indicates model stability and ensures that
cleaned data are not progressively eroded with repeated application.

We evaluated idempotency for CellSweep and other methods by reapplying each tool three additional
times to the 8,000-cell PBMC dataset after an initial denoising step. As shown in Fig. 6 and Fig.
S8, CellSweep, SoupX, and DecontX demonstrate near idempotency, with only minor changes observed
after the second iteration. In contrast, CellBender removes additional counts upon reapplication,
and scAR continues to alter thousands of cells even after two iterations, indicating less stable
behavior.

In the event that noncellular barcodes are unavailable, the alternative CellSweep model
demonstrates a loss in idempotency (Fig. S8G-H).

**Runtime.** CellSweep exhibits faster runtimes than existing background-removal methods, able to
run on full datasets in under a minute. Fig. 7 summarizes the runtime of each method on the
8,000-cell PBMC dataset. When run on a single CPU thread, CellSweep completes in approximately 5
minutes. Using 16 CPU threads reduces runtime to 10 times faster at 25 seconds, making CellSweep
over twice as fast as DecontX and SoupX under comparable conditions. Switching to the alternative
CellSweep model in the absence of non-cellular barcodes does not appreciably change runtime. In
contrast, neural-network-based methods such as CellBender and scAR require substantially longer
runtimes, on the order of hours on CPU and between 10-30 minutes on GPU.

**Simulation.** In order to test these tools on a dataset with a clearly-defined ground truth, we
developed a simulation of an scRNA-seq experiment, and generated a count matrix for a 10,000
gene, 10,000 cell dataset with 90,000 non-cellular barcodes and 12 artificially constructed
cell-types (Fig. 8A). Simulated data were generated assuming negative binomial–distributed
cell-type expression and Poisson-distributed ambient noise, consistent with both empirical
observations and established probabilistic models of scRNA-seq count data (Hafemeister and
Satija, 2019; Gorin and Goodman, 2026; Fleming et al., 2023). Bulk noise was additionally modeled
as a random redistribution of counts across cells (see Supplementary Methods for additional
details).

Compared to real datasets, the simulated data exhibit little contamination, with a global bulk
contamination of 5% and a median ambient contamination of 3%. Using the expression of the 20 most
contaminating cell-type markers across cell-types, the dotplot of the raw data shows clear marker
expression and little marker contamination (Fig. 8B).

CellSweep, SoupX, CellBender, and DecontX all effectively remove noise while removing minimal
signal (Fig. 8C-F, Fig. S12A-D, Fig. S13). scAR, on the other hand, fails to decontaminate the
simulated data. Instead, it adds noisy counts and removes signal, as can be seen by the
disappearance of expression of genes 6031, 4646, and 927 in cell type 4; 6544 in cell type 8; and
5794 in cell type 10 (Fig. S12E-F). Moreover, scAR has the lowest positive predictive value (PPV)
at 0.67, indicating that scAR aggressively removes true signal across the dataset. All other
tools have a PPV of 0.98 or greater. CellSweep was effective at removing off-target counts of
marker genes while retaining on-target counts, reducing the median number of off-target counts
per cell 23 to 3.85, while only reducing median signal from 733 to 730.53 (Fig. 8C-D). SoupX,
CellBender, and DecontX performed similarly well, reducing noisy counts per cell from 23 to 4.02,
3.00, and 3.47, respectively (Fig. 8E-F, Fig. S12A-D).

**Fig. 5.** Cellsweep reduces cross-tissue contamination from marker genes in 8 cubed founder
data. (A) Schematic of 8 cubed founder scRNA-seq setup. Color = tissue. (B) Scatterplot of total
gene counts of Snap25 (a cortex/hippocampus marker) in processed vs. raw cells with CellSweep in
atrial cardiac myocyte heart cells from plate igvf_003 (cortex/hippocampus and heart). (C)
Scatterplot of total gene counts of Snap25 (a cortex/hippocampus marker) in processed vs. raw
cells with CellSweep in glutamatergic neuron cortex cells from plate igvf_003
(cortex/hippocampus and heart). (D) Scatterplot of total gene counts of Star (an adrenal marker)
in processed vs. raw cells with CellSweep in proximal tubule epithelial kidney cells from plate
igvf_009 (adrenal and kidney). (E) Scatterplot of total gene counts of Star (an adrenal marker) in
processed vs. raw cells with CellSweep in zona fasciculata adrenal cells from plate igvf_009
(adrenal and kidney).

**Fig. 6.** CellSweep demonstrates idempotency. (A-B) Total count difference (A) and number of
cells differing by more than 100 counts (B) across iterations. Points have been connected for
ease of visualization only (i.e., no interpolation). Blue = CellSweep; orange = CellBender; green
= DecontX; red = scAR; purple = SoupX. (C) Histogram of per-cell count differences after
processing with CellSweep. Blue = between iteration 0 (raw) and 1; orange = between iteration 1
and 2; green = between iteration 2 and 3; red = between iteration 3 and 4. (D) Knee plots after
processing with CellSweep. Gray = iteration 0 (raw). Blue = iteration 1; orange = iteration 2;
green = iteration 3; red = iteration 4. (E-F) Same as (C-D) but with SoupX. Analysis performed on
the PBMC 8k dataset.

**Fig. 7.** Runtime analysis. Analysis performed on the PBMC 8k dataset. Inset = log scale with
tools under 30 minutes. Blue = CellSweep; orange = CellBender; green = DecontX; red = scAR;
purple = SoupX.

**Fig. 8.** CellSweep removes noise in simulation. (A) Diagram of model for simulated dataset,
assuming three cell-types (1 (red), 2 (green), and 3 (purple)) and cell-type assignment of 2 to
cell $i$. Striped boxes represent the artificially constructed cell-type profiles $p_k$ with red,
green, and purple indicating the respective cell-type markers and blue boxes indicating
house-keeping genes. Varying color intensities illustrate varying levels of gene expression. The
gray box represents a uniform distribution of counts across all genes. The simulation assumes
that a count matrix is the sum of Poisson distributed noise and negative-binomial distributed
cell-type expression. Bulk noise is introduced by random movement of counts from one cell to
another. (B) Dotplot of the twenty most highly contaminating marker genes across all cell-types
in the simulated data. (C) Joint scatterplot of noise and signal total marker counts per cell
after processing with CellSweep. Light blue = raw; dark blue = CellSweep. (D) Same as (B) but
after denoising with CellSweep. (E-F) Same as (C-D) but with SoupX.

---

[← Introduction](02-introduction.md) · [Up: contents](index.md) · [Discussion →](04-discussion.md)
