---
title: Additional Files
source: https://doi.org/10.1093/gigascience/giaa151/
source_file: sources/papers/young-behjati-2020-soupx/young-behjati-2020-soupx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `young-behjati-2020-soupx.jats` from [papers/young-behjati-2020-soupx](https://doi.org/10.1093/gigascience/giaa151/) — papers · young-behjati-2020-soupx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Additional Files

**Supplementary Table S1**. Sample information for the different datasets used in this article.

**Supplementary Table S2**. Pearson correlation coefficient between the background contamination profile and all cells in a channel averaged, after removing the genes above the 99th expression quantile.

**Supplementary Figure S1**. Schematic illustrating the procedure used to estimate the global contamination rate using the gene *IGHD* on the PBMC data. On the left, individual cells are marked red when their expression of *IGHD* is higher than would be possible even if the cell were nothing but contamination. That is, cells where *IGHD* must be endogenously expressed are marked red. Any cluster containing such a cell is excluded, and the global contamination fraction is estimated using cells in the remaining clusters (right of plot).

**Supplementary Figure S2**. The correlation between "true background," which is defined by aggregating across mouse transcripts in human cells and vice versa, with the background expression profile derived using only droplets. Total number of UMIs is given on the x-axis.

**Supplementary Figure S3**. The ratio of human to mouse transcripts on a log₁₀ scale (y-axis) for all droplets in the DropSeq species-mixing experiment. Droplets containing cells are marked in black. The x-axis gives the average number of UMIs between human and mouse for each cell.

**Supplementary Figure S4**. The x-axis gives the true contamination rate measured using the cross-species transcripts in each cell. The y-axis gives the effective contamination rate obtained by applying SoupX at the cluster level using a constant global contamination rate, calculated as the fraction of removed counts by the application of SoupX. The line shows perfect correlation, and red and blue dots represent the 10X and DropSeq species-mixing experiments, respectively.

**Supplementary Figure S5**. Distribution of expression relative to background for genes in the PBMC data. The red line indicates the global estimate of the contamination fraction that would be obtained if just that gene were used to estimate contamination. Genes that are most useful for contamination estimation have a bimodal distribution, with cells genuinely expressing the gene yielding a value on the y-axis >0 and cells that do not express the gene having a value clustered around the true contamination rate.

**Supplementary Figure S6**. Comparison of the contamination fraction estimated by the automated method (x-axis) and by manually supplying a gene set (y-axis), for each channel in the kidney tumour data. The dashed line indicates perfect correlation, and the Pearson correlation is shown in the upper left.

**Supplementary Figure S7**. The improvement in marker specificity following application of SoupX to the kidney tumour data. Note the different scale of the y-axis compared to Fig. 3. All genes that are markers of a cluster either before or after correction are identified, and their expression log fold change (FC) relative to the clusters that they do not mark is calculated before and after correction. The y-axis of this plot shows the fractional change in log FC after applying SoupX for all genes. Genes are grouped into bins for ease of representation, with the number of genes in each bin given by the colour scale. The marginal distribution across all genes is shown on the right, and the dotted line corresponds to no change in marker specificity after correction.

**Supplementary Figure S8**. Uniform manifold approximation and projection (UMAP) representation of the single-cell fetal data. Each point is coloured by its cell type and a cell type label is placed at the position of the average cell.

**Supplementary Figure S9**. Normalized gene expression of *GYPA* (y-axis) in fetal liver data by cell type before and after ambient RNA removal by SoupX (x-axis). The cell types on the x-axis represent the different cell types as annotation in Supplementary Fig. S8. For each cell type, box plots indicate the median, quartiles, and 1.5 times the interquartile range for cells after SoupX correction (left) and before (right). For each distribution, each cell's expression is also shown with horizontal jitter and transparency inversely proportional to the number of cells of that type. The 2 EI Macrophage populations are emphasized in boldface.

**Supplementary Figure S10**. The fractional expression of haemoglobin genes in each cell, relative to the rate of expression in the background in 1 of the kidney tumour channels. This fraction is given by the colour of each point on a log scale. Points that have been determined to not endogenously express haemoglobin genes are marked with a green outline. The x- and y-axis are the tSNE coordinates supplied by cellranger for this channel.

**Supplementary Methods**.A more verbose description of the SoupX method and details of data processing of the different datasets used in this article.

## Abbreviations {#h1content1608223419529}

IG: immunoglobulin; MNP: mononuclear phagocyte; mRNA: messenger RNA; PBMC: peripheral blood mononuclear cell; scRNA-seq: single-cell RNA sequencing; SRA: Sequence Read Archive; tSNE: t-distributed stochastic neighbour embedding; UMI: unique molecular identifier.

## Competing Interests {#h1content1608223103780}

The authors declare that they have no competing interests.

## Funding {#h1content1608223061136}

We acknowledge funding from Wellcome, Sam Behjati fellowship, and core funding to the Sanger Institute.

## Authors' Contributions {#h1content1608222995751}

M.D.Y. conceived the project, developed the method, and wrote the manuscript. S.B. contributed to the method development.

## Supplementary Material

Shreejoy Tripathy -- 2/18/2020 Reviewed

Chris L Plaisier, Ph.D -- 2/21/2020 Reviewed

### ACKNOWLEDGEMENTS {#ack1}

We thank William Heaton and Valentine Svensson for discussions about droplet sequencing; Sarah Teichmann for discussions about the methodology; Sarah Teichmann, Aaron Lun, and Manasa Ramakrishna for comments and review of the manuscript; and Manasa Ramakrishna for improvements to the figures and their layout. We thank Martin Prete for help with creating a Docker version of the code. We thank Justin McManus and Mia Jaffe for discussions about all aspects of the paper, particularly around ways to automate estimation of contamination.

## References

---

[← Discussion](06-discussion.md) · [Up: contents](index.md)
