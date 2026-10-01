---
title: Results
source: https://doi.org/10.64898/2026.01.13.699237/
source_file: sources/papers/cargnelli-2026-benchmarking-decontamination/cargnelli-2026-benchmarking-decontamination.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `cargnelli-2026-benchmarking-decontamination.pdf` from [papers/cargnelli-2026-benchmarking-decontamination](https://doi.org/10.64898/2026.01.13.699237/) — papers · cargnelli-2026-benchmarking-decontamination, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Results

## Strategy for benchmarking ambient RNA removal methods

Because ambient RNA contamination is pervasive in single-cell and single-nucleus RNA-sequencing
(sxRNA-seq) data, and because it can systematically bias cell-type identification and gene-level
inference, a careful benchmarking of ambient RNA removal methods is necessary to understand
their practical impact on downstream analyses. Accordingly, we benchmarked the ability of
CellBender, DecontX, FastCAR, scAR, scCDC, SoupX, and CellClear$^{3,6-11}$ to remove ambient RNA
while preserving endogenous gene expression. Further, we evaluated how ambient RNA removal
influences biological interpretation by evaluating clustering, label transfer, and marker gene quality
(Figure 1). To define ground truth profiles, we simulated datasets with varying levels of ambient RNA
and analyzed strain-mixing and genotype-mixing experiments, leveraging the different biological
origin of each read to establish ground truth (Supplemental Table S1).

Following incorporation of computational decontamination methods into standardized scRNA-seq
preprocessing workflows, such as nf-core$^{12}$, they are increasingly being applied as a routine
background correction step. While this has improved accessibility, it has also lowered the threshold
for applying probabilistic background correction without proper prior dataset-specific evaluation,
raising the risk of over-correction. To explicitly assess the consequences of applying ambient RNA
removal methods without prior evidence of contamination, we also simulated datasets without
contamination and included a smart-seq2-based dataset$^{13}$ as negative controls. This allowed us to
assess distortion of gene expression and downstream biological interpretation in settings where
decontamination is not warranted.

## Ubiquitously expressed messenger RNAs contribute most to ambient RNA

We started out by investigating how variable ambient RNA contamination is between cells in the
same dataset and between datasets. To that end, we calculated the ambient load (the fraction of
total UMIs derived from an ambient source) in the three species-mixing datasets, as well as the
murine strain-mixing dataset. We found that the ambient load is generally higher in the
single-nucleus RNA-seq samples (average: 11.80%) than the single-cell RNA-seq samples
(average: 7.79%) consistent with previous observations$^{16}$. Moreover, we found that the fraction of
ambient RNA per cell after quality control varies significantly within samples (average quartile
coefficient of dispersion (QCD) = 0.314), between samples within the same study (average QCD =
0.319), and between studies (average QCD = 0.171) (Figure 2A). Across features, the ambient RNA
load (i.e., the fraction of UMIs derived from ambient RNA molecules) is strongly and positively
correlated (average R = 0.857) with the average expression level of the same feature in "empty"
droplets (Figure 2B), as well as with average expression level across all cells (Supplemental Figure
1A). The ambient RNA load is also non-linearly associated with endogenous expression frequency
(Figure 2C), as the 10% most frequently expressed features contribute 82.30% of ambient RNA on
average. We observed a similar non-linear association with the fraction of UMIs derived from exons
(Supplemental Figure 1B), where the features with 10% highest exonic fractions contribute 24.60%
of ambient RNA on average. This suggests that ubiquitously expressed mature cytoplasmic
messenger RNAs is the major source of ambient RNA.

Across cells, the ambient load is generally only weakly associated to commonly used cell quality
metrics, such as fraction of UMIs derived from exons, or from either mitochondrial or ribosome
genes. However, for two datasets, there is a strong association to the fraction of UMIs derived from
protein-coding genes, and for all datasets, there is an inverse association with the number of UMIs
and the number of unique features (Figure 2D, Supplemental Figure 1C-D). Thus, ambient RNA can
be reduced through increasingly stringent quality filtering, but the problem cannot be resolved, as
even among the cells with the 10% largest number of UMIs, 2.64% are strongly affected (>10% of
UMIs) by ambient RNA.

## Balance of ambient RNA removal and endogenous RNA retainment

To compare different methods for ambient RNA removal, we calculated two scores for each dataset
(see Methods), one for removal of ambient RNA and one for retaining endogenous RNA. Both scores
range between 0 and 1, where 1 is the best possible performance and 0 is the worst possible
performance. In terms of ambient RNA removal, scAR (average = 0.679) and CellBender (average =
0.604) have the best performance (Figure 3A-B, Supplemental Table S2). However, scAR also
removes a substantial proportion (average = 0.445) of endogenous RNA signal, especially from
lowly expressed genes (Figure 3C). Generally, we observe a positive association between the
expression level of genes and ambient RNA removal (i.e., ambient RNA is predominantly removed
from highly expressed genes) (Supplemental Figure 2), while we found a negative association with
endogenous RNA retainment (i.e., endogenous signal is predominantly removed from lowly
expressed genes) (Supplemental Figure 3). In control datasets without ambient RNA, all methods
remove approximately the same amount of signal from endogenous RNA, as compared to datasets
with ambient RNA.

An important distinction between the methods is whether they require access to the full count matrix
or can be applied using only the filtered matrix (subset of the full matrix where low quality and
empty droplets have been removed), as the full count matrix may not be readily available from public
datasets where access to the raw data is restricted. Of the 7 methods, four (SoupX, DecontX, scAR,
and scCDC) are applicable to datasets with access to filtered count matrices only, whereof scAR,
SoupX and DecontX can be run either using the full count matrix or in a reduced mode using only
the filtered matrix. For scAR, the computational resources required to run in full mode were
intractable and the analysis did not finish. SoupX in reduced mode removes more ambient RNA
compared to full mode, and retains approximately the same amount of endogenous RNA, while
DecontX in reduced mode removes slightly less ambient RNA, but retains more endogenous RNA
than full mode.

## Effect of decontamination on biological interpretation

To investigate how ambient RNA removal tools impact biological interpretation, we initially evaluated
the synthetic sample with the largest ambient RNA load. Only CellBender improves the ability to
separate the ground truth cell types using unsupervised clustering relative to using uncorrected
counts (Figure 4A). DecontX does not impact cell type recovery, while the remaining methods all
perform worse than using uncorrected counts. In terms of marker gene expression, we observed that
only DecontX and scAR improves the module scores to approximately the ground truth level (Figure
4B), while most other methods do not significantly improve module scoring above the uncorrected
counts. These methods also improved average modules scores in the absence of ambient RNA
contamination (Supplemental Figure 4A) indicating a bias towards cell type-specific gene
expression.

To more comprehensively evaluate how computational decontamination methods affect biological
interpretation, we evaluated cellular neighborhoods, marker genes, batch integration and label
transfer for both contaminated and negative control datasets (Supplemental Table S3-4). For
evaluating the quality of cellular neighborhoods, we used species or cell type labels to calculate the
purity and local inverse Simpsons index (LISI) for the nearest neighbors of each cell and found that
CellBender, scAR, SoupX and DecontX improves the quality of cellular neighborhoods in
contaminated datasets and have a negligible impact when applied to negative controls relative to
using uncorrected counts (Figure 4C). In terms of marker genes, especially scAR and CellBender
leads to more focal expression of marker genes in reduced dimensional space as indicated by
improved entropy score (i.e., neighbors have more similar expression patterns), improved Moran's I
(i.e., higher spatial autocorrelation) and Gini coefficient (i.e., markers are expressed by a more
selective set of cells) relative to uncorrected counts (Figure 4D). Next, we integrated samples using
Harmony$^{14}$ and evaluated integration quality using the average silhouette width across batches
(bASW), the batch LISI, principal component regression (PCR) and the maximum adjusted Rand
index (ARI) between unsupervised clustering and batch labels. We observed that most methods did
not significantly improve batch integration relative to using uncorrected counts, but especially scAR
led to worse integration, and had a significant impact on integration of negative control datasets
without ambient RNA (Figure 4E). Finally, we evaluated the impact of ambient RNA correction on
label transfer using Azimuth$^{15}$. We evaluated the purity of transferred labels in local cellular
neighborhoods, the average silhouette width (cASW) of transferred labels, the ability to recover them
using unsupervised clustering, and the expression similarity between cells assigned to the same cell
type label as measured by the root-mean-square-error (RMSE) between each cell and the average
profile of all cells within a label. We found that especially, scAR, CellBender, DecontX and CellClear
improved label transfer relative to using uncorrected counts, but that scAR had a significant impact
on label transfer in datasets without ambient RNA contamination (Figure 4F).

---

[← Introduction](02-introduction.md) · [Up: contents](index.md) · [Discussion →](04-discussion.md)
