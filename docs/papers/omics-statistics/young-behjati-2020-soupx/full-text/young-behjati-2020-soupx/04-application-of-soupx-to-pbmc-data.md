---
title: Application of SoupX to PBMC Data
source: https://doi.org/10.1093/gigascience/giaa151/
source_file: sources/papers/young-behjati-2020-soupx/young-behjati-2020-soupx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `young-behjati-2020-soupx.jats` from [papers/young-behjati-2020-soupx](https://doi.org/10.1093/gigascience/giaa151/) — papers · young-behjati-2020-soupx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Application of SoupX to PBMC Data

Next we tested our method on a dataset consisting of PBMCs, measured in a single channel [2]. We used the Seurat package [18,19] to produce a *t*-distributed stochastic neighbour embedding (tSNE) representation of the data and annotated clusters of cells based on the expression of canonical marker genes (Fig. 3A).

![](https://doi.org/10.1093/gigascience/giaa151/)

The PBMC dataset and how it changes when background correction is applied. **A**, A tSNE representation of the data, with cluster boundaries shown by density contours and shaded according to the cell type they represent. MNP: mononuclear phagocytes; NK: natural killer cells. **B**, The same tSNE representation, but cells are now coloured by their rate of expression of immunoglobulin (IG) genes compared to the rate at which IG is expressed in the background on a log₁₀ scale. Positive values correspond to higher IG expression in a cell than in the background, with values significantly >0 only possible if the cell endogenously expresses IG. The density contours of the clusters with no cell that endogenously expresses IG (as determined by a Poisson test) are marked in boldface and used to estimate the global contamination ratio. **C**, The fraction of cells shared between clusters determined with the same parameters before and after application of SoupX. **D**, The improvement in marker specificity following application of SoupX. All genes that are markers of a cluster either before or after correction are identified and their expression log fold change (FC) relative to the clusters they do not mark is calculated before and after correction. The y-axis of this plot shows the fractional change in log FC after applying SoupX for all genes. Genes are grouped into bins for ease of representation, with the number of genes in each bin given by the colour scale. The marginal distribution across all genes is shown on the right and the dotted line corresponds to no change in marker specificity after correction. **E**, The improvement in marker sensitivity for the gene *LYZ*, which is a marker for mononuclear phagocytes (MNPs). The corrected and uncorrected expression levels are shown split by cells labelled as MNPs and all others. **F**, This same change in expression shown on the tSNE map, where the colour scale represents the fraction of *LYZ* expression that has been removed by SoupX.

Applying the automated procedure (see Supplementary Methods) to estimate the contamination fraction produced a background contamination rate of $6\%$. To confirm the accuracy of this estimate, we also calculated the background contamination rate using a set of genes that could be assumed to be unexpressed in some cells (i.e., where *m_(g,\ c)* = 0).

To aid appropriate selection of such a gene set, we reasoned that the ideal genes for estimating the contamination rate would be ubiquitously present at a low level in all droplets due to high expression in the ambient RNA. They would also be present at a high level when a cell endogenously expresses the gene, allowing us to unambiguously separate droplets with endogenously expressing cells (i.e., where *m_(g,\ c)* > 0) from those where the expression is solely due to contamination (*m_(g,\ c)* = 0).

Based on this reasoning, we developed a heuristic that ranks the 500 genes with the highest expression in the background by their bimodality of expression across all droplets in a channel. A plot based on applying this heuristic to the PBMC data shows the expression distribution across all cell-containing droplets in the dataset (Supplementary Fig. S5). This heuristic suggests that immunoglobulin (IG) genes, such as *IGKC* and *IGLC2*, are both highly expressed in the soup and highly specific in their expression, making them good candidates for estimating the contamination fraction in this dataset.

To select a precise set of cells for which we could use IG genes to estimate the contamination, we identified all cells whose IG expression was significantly greater than in the background contamination (Poisson test, false discovery rate 0.05; Supplementary Materials). These represent cells endogenously expressing IG. We only used cells from clusters with no cells identified as endogenously expressing IG to estimate the contamination rate (Fig. 3B). For the PBMC data, this identified IG expression in T cells as purely due to contamination and calculated a background contamination rate of $\sim 5\%$.

Having calculated the global contamination rate for the PBMC data, we then corrected the PBMC data for background mRNA contamination and re-analysed the data with Seurat using the same settings. Comparing cluster membership before and after correction revealed that the same number of clusters was identified, but some cells changed which cluster they belonged to (Fig. 3C).

Next we identified marker genes for each cluster in both the corrected and uncorrected PBMC data using a Wilcoxon rank sum test and calculated the expression fold change between the cluster and all other cells. We compared the fold changes for the same genes in the same clusters before and after correction and found that correction for background contamination systematically increased the fold change contrast for marker genes (Fig. 3D). That is, correction for background contamination made marker genes more specific to the cluster they were markers of. Furthermore, additional genes were found as markers in the corrected data that were not identified in the uncorrected data.

As a specific example, we found that correction of ambient RNA contamination changes the pattern of expression of *LYZ* in the PBMC data (Fig. 3E and F). This improved the specificity of *LYZ* as a marker gene for mononuclear phagocytes (MNPs) (Fig. 3E) by removing its expression from all other cell types, while leaving its expression in MNPs unchanged (Fig. 3F).

---

[← Properties of Ambient RNA](03-properties-of-ambient-rna.md) · [Up: contents](index.md) · [Ambient RNA Confounds Interpretation in Complex Experiments →](05-ambient-rna-confounds-interpretation-in-complex-experiments.md)
