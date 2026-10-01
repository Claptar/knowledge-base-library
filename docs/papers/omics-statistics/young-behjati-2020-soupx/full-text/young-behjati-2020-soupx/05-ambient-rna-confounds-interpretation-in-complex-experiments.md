---
title: Ambient RNA Confounds Interpretation in Complex Experiments
source: https://doi.org/10.1093/gigascience/giaa151/
source_file: sources/papers/young-behjati-2020-soupx/young-behjati-2020-soupx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `young-behjati-2020-soupx.jats` from [papers/young-behjati-2020-soupx](https://doi.org/10.1093/gigascience/giaa151/) — papers · young-behjati-2020-soupx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Ambient RNA Confounds Interpretation in Complex Experiments

As a further test of the biological utility of our method we considered an experiment combining 7 kidney tumours processed across 10 channels (Supplementary Table S1). As with the PBMCs, we analysed corrected and uncorrected data using the Seurat package; Fig. 4A shows a tSNE plot of the uncorrected data. Haemoglobin genes were used to estimate the contamination fraction in most channels (Supplementary Fig. S10). This choice of gene set for estimating contamination was motivated by the ubiquitous presence of red blood cells (with red cell lysis forming part of the tissue treatment protocol) in these samples, together with the knowledge that haemoglobin genes are highly specific to red blood cells. We compared the resulting estimates of the contamination fraction with those obtained by applying the automated method and found good agreement (Supplementary Fig. S6).

![](https://doi.org/10.1093/gigascience/giaa151/)

The application of SoupX to complex, multi-channel data. **A**, A tSNE representation of the data, with cluster boundaries shown by density contours and shaded according to the cell type they represent. ccRCC: clear-cell renal cell carcinoma cells; pRCC: papillary cell renal cell carcinoma cells; RBC: red blood cells; MNP: mononuclear phagocytes. **B**, The fraction of cells shared between clusters determined with the same parameters before and after application of SoupX. **C**, The improvement in marker sensitivity for the gene *HBB*, which is a marker for red blood cells. The colour scale represents the fraction of *HBB* expression that has been removed by SoupX. **D**, Same as **C** but for *COL1A1*. **E**, The cross-batch entropy before and after SoupX has been applied. The entropy measures the level of local mixing (100 nearest neighbours) for 100 cells selected from each cluster [20]. **F**, The distribution of *HBB* expression (y-axis, log scale) in the fetal liver data by cell type (x-axis), with the erythroid lineage marked in boldface. For each cell type, the expression distribution is shown before (right) and after (left) application of SoupX. Dots represent individual cells and box plots show the distribution of expression values where the central line is the median, box boundaries are the first and third quartiles, and the whiskers extend to 1.5 times the interquartile range.

Applying SoupX and re-analysing the kidney tumour data revealed that, in contrast to the PBMC data, many cells changed cluster and with the same clustering parameters 2 fewer clusters were identified in the corrected data (Fig. 4B). Furthermore, we found that the expression ratio of marker genes between the cluster they mark and all other cells increased systematically after correction for background contamination (Supplementary Fig. S7).

We found that the correction of background contamination changed the distribution of expression of many genes across cells in a way that would alter the biological interpretation. For example, while it is unlikely to be biologically misinterpreted, SoupX completely removes the expression of haemoglobin genes from all cells except red blood cells (Fig. 4C).

In other cases, the misattribution of gene expression to cell types that do not truly express them could lead to false conclusions. An example of this is the cluster of T and MNPs in Fig. 4A and D, which express the collagen genes *COL1A1*, *COL1A2*, and *COL3A1* before background correction. The expression of collagen genes might be interpreted as evidence that the leukocytes are resident in the tissue. However, our method identifies that a high fraction of this expression is due to contamination (Fig. 4D).

Because the ambient mRNA expression profile is experiment specific, we reasoned that background contamination likely creates batch effects. That is, 2 identical cells captured in different experiments will appear different owing to differences in their cell-free RNA composition. We therefore calculated the cross-batch entropy of the kidney tumour data before and after background correction [20]. This analysis shows that the batch-mixing entropy is increased after background correction, indicating better mixing between samples (Fig. 4E).

As a further example of the biological utility of SoupX, we applied SoupX to 40 channels of human fetal liver data (Supplementary Fig. S8). Before correction for background contamination, a large number of cells outside the erythroid (red blood cell) lineage express erythroid markers such as *HBB* in combination with other cell type markers. This widespread expression of multiple distinct markers could potentially indicate the presence of doublets. Application of SoupX allows this explanation to be ruled out, showing that *HBB* is only truly expressed in erythroid cell types (Fig. 4F).

Application of SoupX is also able to identify those cell types where biologically unexpected combinations of genes represent genuine biological phenomena. One example of this is the expression of the erythroid gene *GYPA* in the EI macrophage populations, which could be the consequence of either contamination or a biological phenomenon. Application of SoupX confirms that this expression represents genuine gene expression and not ambient RNA contamination (Supplementary Fig. S9).

---

[← Application of SoupX to PBMC Data](04-application-of-soupx-to-pbmc-data.md) · [Up: contents](index.md) · [Discussion →](06-discussion.md)
