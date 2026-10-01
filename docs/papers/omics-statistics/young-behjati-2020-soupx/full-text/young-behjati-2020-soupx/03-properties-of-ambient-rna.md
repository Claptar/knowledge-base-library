---
title: Properties of Ambient RNA
source: https://doi.org/10.1093/gigascience/giaa151/
source_file: sources/papers/young-behjati-2020-soupx/young-behjati-2020-soupx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `young-behjati-2020-soupx.jats` from [papers/young-behjati-2020-soupx](https://doi.org/10.1093/gigascience/giaa151/) — papers · young-behjati-2020-soupx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Properties of Ambient RNA

We next investigate the properties of ambient RNA contamination in data where ground truth is available, the “species-mixing” experiments combining mouse and human cell lines using 10X [2] and Drop-Seq technologies [14]. Figure 2A shows the relative abundance of human and mouse mRNAs in each droplet in the 10X data. Droplets containing human (top right) and mouse (bottom right) cells show that ∼1% of observed transcripts are cross-species contamination. This rate of cross-species contamination provides a lower bound on the total rate of ambient mRNA contamination because there will also be an additional contribution due to contaminating mRNAs from the same species (we later show that the true contamination rate is $\sim 2\%$). A similar effect is seen in the Drop-Seq–based species-mixing data (Supplementary Fig. S3). These observations demonstrate that cell-free mRNA contamination is present even in highly controlled experiments.

![](https://doi.org/10.1093/gigascience/giaa151/)

The properties of the cell-free mRNA soup as determined using species-mixing datasets. **A**, The log₁₀ ratio of the number of UMIs mapping to human and mouse mRNAs for each droplet in the species-mixing dataset (10X). Droplets determined to contain cells by cellranger are marked in black. **B**, The correlation of the counts in the background compared to counts averaged across cells for each gene. Counts have been subsampled so that the total number of counts in the background and averaged cell population are the same. **C**, The estimated contamination fraction as a function of number of UMIs in each droplet in individual cells in the species-mixing dataset. Red and blue dots represent cells from the 10X/DropSeq experiments, respectively. The distribution on the left shows the marginal distribution across all cells. **D**, The fractional change in contaminating and genuine expression levels after applying SoupX for the 2 technologies. The distribution across cells is summarized by box plots, where the central line is the median, box boundaries are the first and third quartiles, and the whiskers extend to 1.5 times the interquartile range.

To investigate the composition of cell-free mRNAs, we compared the aggregate expression profile of all droplets containing cells to all droplets with ≤10 UMIs, which we assumed to contain only ambient mRNAs. These 2 profiles were highly correlated in the 10X species experiment (Fig. 2B) with a high correlation found in all other datasets considered (Pearson correlation 0.71–0.96, median 0.86; Supplementary Table S2). The strength of the correlation implies that cell-free contamination represents an approximately uniform sampling of the cells in the sequencing batch (i.e., channel).

Next we estimated the contamination fraction, the fraction of expression derived from the cell-free mRNA background in each cell. In each cell we identify a set of genes that must have originated from the ambient mRNA: human transcripts in mouse cells and vice versa. For these genes/cells it is assumed that *m_(g,\ c)* = 0 and the contamination fraction is calculated using Equation 4. Figure 2C reveals that there is little variation in the contamination fraction within a channel, in both the 10X and DropSeq data.

In most experiments there is less power to determine cell-specific contamination fractions and so SoupX assumes a constant contamination fraction within a channel. When clustering information is provided, the redistribution of counts from cluster level to individual cells automatically removes more counts from contaminated cells, even when only a global estimate of the contamination is given (Supplementary Fig. S4; Supplementary Methods). Where a cell-specific expression estimate is needed, SoupX uses a hierarchical Bayes method to share information between cells (Supplementary Methods).

It may be hypothesized that the absolute number of contaminating mRNA molecules is the quantity that is approximately constant and that the contamination should vary with the number of mRNA molecules contributed by the captured cell. That is, that contamination fraction should vary as a function of cellular mRNA contribution, with the number of detected UMIs being a proxy for this. Consistent with this, Fig. 2C shows that the greatest contamination occurs in droplets with the fewest UMIs. However, the contamination fraction is still approximately constant across most of the UMI range. This is likely a consequence of the fact that the capture efficiency of molecules in droplet-based experiments varies by as much as an order of magnitude [17]. Thus variation due to capture efficiency is likely to swamp variation due to “cell size” in most experiments, making constant contamination fraction a reasonable approximation.

To test the accuracy of SoupX in removing contaminating counts while retaining those due to endogenous expression we compared the fraction of expression from cross-species and within-species genes before and after SoupX contamination correction. This analysis revealed (Fig. 2D) that mouse expression in human cells (and vice versa) was decreased by a factor of ≥2 and usually an order of magnitude by the SoupX contamination removal in both 10X and DropSeq experiments. By contrast the fraction of expression derived from genes corresponding to the correct species was effectively unchanged for all cells.

---

[← The SoupX Method](02-the-soupx-method.md) · [Up: contents](index.md) · [Application of SoupX to PBMC Data →](04-application-of-soupx-to-pbmc-data.md)
