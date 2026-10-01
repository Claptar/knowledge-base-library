---
title: Background
source: https://doi.org/10.1186/s13059-024-03284-w/
source_file: sources/papers/wang-2024-sccdc/wang-2024-sccdc.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `wang-2024-sccdc.jats` from [papers/wang-2024-sccdc](https://doi.org/10.1186/s13059-024-03284-w/) — papers · wang-2024-sccdc, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Background

Received 2023 Jan 30; Accepted 2024 May 16; Collection date 2024.

## Background {#Sec1}

Single-cell RNA-seq (scRNA-seq) is a widely used technique for studying cell heterogeneity in organs. Various studies and large databases, such as the human cell atlas, have taken advantage of scRNA-seq, especially droplet-based platforms such as Chromium X, BD Rhapsody, and inDrop [1–3]. Droplet-based scRNA-seq requires every cell to be sealed with a barcoded bead in a droplet so that the cell’s mRNAs can be labeled by the specific barcode. However, ambient RNA contamination is ubiquitous [4–7]: ambient RNA molecules in the solution would cause systematic contamination by inflating the measured expression levels of endogenous genes in cells, thus impeding the identification of cell-type marker genes. In parallel to scRNA-seq, single-nucleus RNA-seq (snRNA-seq) has been developed to investigate cells that are too fragile or difficult to dissociate into single cells [8, 9]. Yet, ambient RNA contamination is likely more common in snRNA-seq than in scRNA-seq because the nuclei extraction procedure would cause many RNAs in the cytoplasm to be released into the solution. Although enzymatic degradation is theoretically possible to remove ambient RNAs, it is often too challenging to perform experimentally, especially for snRNA-seq, because endogenous RNAs are difficult to protect against degradation. Hence, ambient RNA contamination needs to be corrected in a post hoc manner in most cases.

Various experimental and computational strategies have been developed to correct the contamination in scRNA-seq and snRNA-seq data. Sanchez et al. developed an experimental approach that uses spike-in cells as a reference to correct the contamination [6]. However, this approach complicates the experimental procedure and has not been integrated into common commercial platforms. Several computational methods have been developed for decontamination, including SoupX [5], CellBender [10], and scAR [11], whose common idea is to first estimate the distribution of ambient RNA levels from empty droplets and then use the estimated distribution to correct the gene expression levels in cells. However, since SoupX, CellBender, and scAR require empty-droplet data, they are inapplicable to processed data in which empty droplets have been removed. Although another computational method, DecontX [4], does not require empty-droplet data, it and the three above methods alter all genes’ expression levels, possibly leading to an over-correction of the genes that did not cause the contamination. Such over-correction, especially for lowly expressed genes, will likely result in the missingness of informative genes in relevant cell types. However, the field lacks a comprehensive evaluation of computational decontamination methods for correcting genes at varying contamination levels.

In this study, we performed snRNA-seq assays in mouse mammary glands at the virgin and lactation stages. In our snRNA-seq datasets, we observed sample-specific contamination by ambient RNAs. To correct the contamination, we applied the above computational methods but found that DecontX and CellBender exhibited an under-correction of highly contaminating genes, while SoupX and scAR over-corrected many genes, including housekeeping genes (Fig. 1).

![](https://doi.org/10.1186/s13059-024-03284-w/)

![](https://doi.org/10.1186/s13059-024-03284-w/)

Performance evaluation of existing methods on correcting contaminated mammary gland snRNA-seq data. **A** The cell clusters identified in L5 and virgin mammary gland datasets are shown in UMAP plots. **B** Heatmap of the expression of selected marker genes in L5 and virgin mammary gland datasets. Notably, highlighted genes supposed to express exclusively in a cluster are widely detected in all the cells. **C** The expression of *Wap* and *Acaca* in the nucleus are shown in UMAP plots. **D**, **E** The violin plots show the normalized expression levels of the selected marker genes (**D**) and housekeeping genes (**E**) before and after correction using the indicated methods by the default Seurat (V3). Adipo, adipocytes; AlveoProg, alveolar progenitors; AlveoDiff, differentiated alveolar cells; Bas/Myo, basal cells/myoepithelial cells; Endo, endothelial cells; Fibro, fibroblasts; HormSens, hormone sensing cells; HormSensDiff, differentiated hormone sensing cells; HormSensProg, hormone sensing progenitors; Immune, immune cells; LumProg, luminal progenitors; SkelMusc, skeleton muscle cells

Motivated by this result, we developed scCDC (single-cell Contamination Detection and Correction), which first detects the “contamination-causing genes,” which encode the most abundant ambient RNAs, and then only corrects these genes’ measured expression levels. We show that scCDC successfully corrected the contamination in our in-house snRNA-seq datasets. Moreover, scCDC improved the accuracy of identifying cell-type marker genes and constructing gene co-expression networks. Compared with DecontX, SoupX, CellBender, and scAR on synthetic datasets and real datasets, scCDC excelled in robustness and decontamination accuracy for correcting highly contaminating genes, while it avoids over-correction for lowly/non-contaminating genes. Not requiring empty-droplet data, scCDC has general applicability to all processed scRNA-seq and snRNA-seq datasets in public repositories. In addition, scCDC can be used in combination with DecontX to remove the remaining low contamination not caused by the contamination-causing genes scCDC identifies, by leveraging the complementary advantages of the two methods.

---

[Up: contents](index.md) · [Results →](02-results.md)
