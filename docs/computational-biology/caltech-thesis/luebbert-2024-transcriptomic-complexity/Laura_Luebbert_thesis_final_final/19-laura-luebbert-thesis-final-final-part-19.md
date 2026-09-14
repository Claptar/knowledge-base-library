---
title: Laura Luebbert thesis final final Part 19 —
source: https://thesis.library.caltech.edu/16368/
source_file: sources/luebbert-2024-transcriptomic-complexity/Laura_Luebbert_thesis_final_final.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Laura Luebbert thesis final final Part 19 —

**Source:** `Laura_Luebbert_thesis_final_final.pdf` from [luebbert-2024-transcriptomic-complexity](https://thesis.library.caltech.edu/16368/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **Preamble**

While transcriptomics technologies have revolutionized the study of RNA expression in healthcare, the heterogeneity of data obtained from different patients with varying medical histories, in addition to the technical and biological noise inherent to sequencing data, results in substantial and unique data analysis challenges. The data presented in the previous subchapter was derived from 12 prostate cancer patients at varying time points of CAR T therapy from CAR T product, peripheral blood, and solid tumor tissue using two different sequencing technologies, single-cell gene expression and V(D)J immune repertoire sequencing, resulting in a total of 32 multiplexed datasets for each sequencing technology. In this subchapter, I will describe additional data analysis approaches, expanding on the methods and results described in the previous subchapter and emphasizing the consequences of data heterogeneity and complexity.

#### **Methods and Results**

_Detection of transgenes from single-cell RNA sequencing data_

Since the single-cell RNA sequencing data described in the previous subchapter was generated from patients who were treated with transgenic T cells, we can detect these cells in the sequencing data based on their expression of the transgenic CAR product. This can be achieved by manually adding the CAR sequence to the reference genome (excluding any endogenous sequences such as CD19). The detection rate of transgenes is low. Hence, this approach works best for samples with a high copy number of transgenes, such as the


**Figure 5.6** UMI counts of the CAR transgene and the number of CAR+ cells obtained for each donor.

124


**Figure 5.7** The number of transgenic CAR+ cells per donor at each treatment time point.

CAR T product (Figure 5.6). Interestingly, transgenic CAR T cells were only detected in the peripheral blood samples of the two patients that showed the most promising treatment response (Figure 5.7).

#### _Data quality control and filtering_

Following the alignment of raw sequencing data to a reference genome, the data quality needs to be assessed and low-quality cells removed. Knee and library saturation plots are often generated to evaluate data quality. A ‘knee plot’ shows the number of unique reads (each read tagged with a Unique Molecular Identifier (UMI)) observed for each cell and is used to determine a threshold above which cells are considered valid. Cells with relatively few reads are considered low-quality and removed before further analysis. A library saturation plot shows the number of genes detected over the total read count for each cell. The library plot plateaus as the introduction of more UMIs does not lead to the detection of new genes, thereby indicating a saturation with UMIs. Extended Data Figure 5.1 shows the knee and library saturation plots for all 32 gene expression datasets obtained from the 12 prostate cancer patients throughout different time points. Several of these datasets are multiplexed across patients. The data quality and barcode filtering threshold differ greatly between datasets (Extended Data Figure 5.1). Due to the heterogeneity in quality between datasets, it is crucial to independently assess data quality and filter cells for each dataset. Otherwise, some datasets would be filtered too conservatively, while others would have introduced low-quality cells into the analysis.

#### _Batch correction and clustering_

Following data quality assessment and filtering, the datasets were concatenated, and log(CP10k +1) normalized for further analysis. Given that datasets spanning different patients, time points, and sequencing runs were combined, we considered batch correction to remove experimental biases and batch effects prior to clustering. However, after batch correction using single-cell variational inference (scVI)<sup>1</sup> , the gene expression profiles were incorrectly homogenized across the datasets. This was easily identified by the suddenly widespread expression of the transgenic CAR construct in cell types other than T cells. Instead, we clustered the combined dataset using Leiden clustering<sup>2</sup> without prior batch correction and examined whether the clustering was best explained by sequencing batches

125


<!-- Start of picture text -->
A<br>Time point<br>B<br>Dataset<br>T<br>AD<br>AA<br>AC<br>Z<br>X<br>V<br>U<br>Y<br>C<br>Time point<br><!-- End of picture text -->

**Figure 5.8 A** The fraction of cells obtained for each time point per Leiden cluster. **B** The fraction of cells from each sequencing batch (dataset) in each Leiden cluster. **C** The fraction of cells obtained for each time point per donor.

or the expected biological groups. Figure 5.8 shows the fraction of cells in each Leiden cluster from the different sequencing batches (Figure 5.8 B) and different treatment time points (Figure 5.8 A). As expected, cells from similar treatment time points cluster into the same clusters across sequencing batches and donors. This is also true for cells originating from the CAR T product (infusion product (IP)), which is expected to show similar gene expression across donors. Given that the clustering was better explained by experimental

126


**Figure 5.9** Expression of cell type marker genes in each Leiden cluster labeled with the corresponding cell type.

condition than sequencing batch, we decided to continue the analysis without batch correction to avoid the biases introduced by batch correction.

The Leiden clusters can subsequently be assigned cell types based on the expression of marker genes. Figure 5.9 shows the expression of cell type marker genes per Leiden cluster obtained without batch correction labeled with the corresponding cell type assignment. The clear separation of clusters by cell type marker genes and the similarity in gene expression space between clusters of the same cell type (see the dendrogram in Figure 5.9) further indicates that the clustering captured biological rather than batch effects. As expected, only T cells expressed the CAR transgene. Moreover, the presence of the CAR transgene correlated with the expression of CD19, which is not usually expressed in T cells. These CD19 counts likely originated from the CAR transgene, which also contains a copy of human CD19, rather than corresponding to endogenous expression of the CD19 gene as observed in B cells (Figure 5.9).

_Comparison of gene expression results between donors_

Using an approach similar to the assignment of cell types to Leiden clusters based on cell type marker genes, as discussed above, T cells can be further broken down into immune

127


**Figure 5.10** Expression of immune sub-cell type marker genes in groups of different T cell types.

sub-cell types based on marker genes for different types of T cells. Instead of re-clustering the T cells and assigning sub-cell types to smaller Leiden clusters, we assigned the sub-cell type labels to each individual T cell using a custom reiterative algorithm that increases marker gene expression thresholds with each round of sub-cell type assignment. This resulted in groups of immune sub-cell types with clearly defined expression of the corresponding marker genes (Figure 5.10).

This sub-cell type assignment allowed us to follow different populations of immune cells over time, as is shown for donor 388 in Figure 5.3f in the previous subchapter. The comparison of these results across several donors is hindered by the data heterogenicity between donors, partly caused by different medical histories, and the uneven distribution of time point data per donor (Figure 5.8 C). However, we hypothesized that global trends, such as changes in the fraction of cells occupied by each immune sub-cell type, may be reproducible across donors. Figure 5.11 shows the fraction of T cells occupied by each immune sub-cell type for donors 375, 394, and 376 over time. Although the number of available T cells per donor differs between time points, an expansion of effector CD8+ T cell subsets can be observed for all patients between 0- and 29-days post-infusion. This coincides with the results presented for donor 388 in Figure 5.3f in the previous subchapter.

#### _Analysis of the V(D)J immune repertoire across donors_

The expression of antigen binding domains from the V(D)J immune repertoire sequencing data was quantified using the V(D)J algorithm of 10x Genomics Cell Ranger v7.1.0. Interestingly, the expansion of clonotypes 28 days post-infusion, as observed for donor 388 (Figure 5.3g in the previous subchapter), could not be reproduced for donor 375 (Figure 7A). Figure 5.12 B shows the number of clonotypes contained in different fractions of cells at 28 days post-infusion, further visualizing that the clonotypes in donor 388 are split into dominating clonotypes present in large fractions of cells and fewer clonotypes occupying small fractions of cells. By contrast, the fractions of cells occupied by clonotypes in donor 375 are more evenly distributed (Figure 5.12 B).

128

**A**

**B**


<!-- Start of picture text -->
C<br><!-- End of picture text -->

**Figure 5.11** Fraction of T cells occupied by each immune sub-cell type for donors 375 ( **A** ), 394 ( **B** ), and 376 ( **C** ) over time. The numbers above each bar delineate the total number of T cells at that time point.

129

**A**


<!-- Start of picture text -->
B<br><!-- End of picture text -->


<!-- Start of picture text -->
C<br>Expanding  Expanding<br>Contracting  Contracting<br><!-- End of picture text -->

**Figure 5.12 A** The fraction of clonotypes occupied by individual clonotypes over time in the peripheral blood of donor 375. **B** The number of clonotypes occupying different fractions of cells for donors 375 and 388 at 28 days post-infusion. **C** The percentage of cells occupied by each individual clonotype at 28 days post-infusion over the percentage at 0 days post-infusion for donors 388 (left) and donor 375 (right).

In contrast to donor 388, donor 375 did not undergo lymphodepletion prior to infusion with CAR T product, which potentially prevented individual evolving clonotypes from inhabiting large fractions of the overall clonotype population as seen in donor 388. To investigate whether there were any expanding clonotypes over time in donor 375, we visualized the percentage of cells each clonotype was expressed at 0- and 28-days postinfusion (Figure 5.12 C). In this plot, expanding clonotypes are underrepresented at 0 days post-infusion, while contracting clonotypes are underrepresented at 28 days post-infusion.

130

Donor 388 showed two separate populations of expanding and contracting clonotypes, with only a single clonotype remaining stable over time. In contrast, all clonotypes in donor 375 remained stable with only slight changes in the percentage of cells occupied by each clonotype between 0- and 28-days post-infusion, suggesting that donor 375 did not show any expansion of clonotypes.

#### **Code availability**

The code to reproduce the figures and analysis, as well as supplementary methods, can be found here: <u>https://github.com/pachterlab/DBALLSMRDMCMGWSTPMBDKPFP_2023</u>

#### **References**

1. Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep generative modeling for single-cell transcriptomics. _Nat. Methods_ **15** , 1053–1058 (2018).

2. Traag, V. A., Waltman, L. & van Eck, N. J. From Louvain to Leiden: Guaranteeing well-connected communities. _Sci. Rep._ **9** , 1–12 (2019).

131


132


<!-- Start of picture text -->
133<br><!-- End of picture text -->


**Extended Data Figure 5.1** Knee and library saturation plots for 32 gene expression datasets derived from prostate cancers patients at different time points of treatment with CAR T therapy. The dashed grey lines indicate the data quality threshold for barcode filtering.

134

_C h a p t e r 6_

---

[← PSCA-CAR T cells for Metastatic Castration-resistant Prostate Cancer: A Phase 1 Trial](18-psca-car-t-cells-for-metastatic-castration-resistant-prostat.md) · [Up: contents](index.md) · [CONCLUSION AND OUTLOOK →](20-conclusion-and-outlook.md)
