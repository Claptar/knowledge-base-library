---
title: Discussion
source: https://doi.org/10.1186/s13059-024-03284-w/
source_file: sources/papers/wang-2024-sccdc/wang-2024-sccdc.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `wang-2024-sccdc.jats` from [papers/wang-2024-sccdc](https://doi.org/10.1186/s13059-024-03284-w/) — papers · wang-2024-sccdc, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Discussion

Here, we developed a computational method, scCDC, to identify GCGs and correct the counts of GCGs, without requiring experimental spike-in controls or empty droplets. Our results indicate that ambient RNA contamination warrants attention, and scCDC effectively identified GCGs and corrected their contamination in scRNA-seq and snRNA-seq data. Compared to the existing computational methods, scCDC avoids the under-correction issue of DecontX, CellBender, and SoupX-automated on highly contaminating genes and the over-correction on other genes by SoupX-manual and scAR, via the detection of GCGs (Table 1), ensuring robust correction for varying levels of contamination.

Among the existing computational methods, SoupX, CellBender, and scAR estimated the contaminative count distribution from empty droplets. However, these three methods have two limitations. First, it is too simplistic to assume that ambient RNA levels have the same distribution in empty droplets and in cell- or nucleus-containing droplets. The two reasons are (1) empty droplets only contain ambient RNAs randomly distributed in the cell suspension, but cell- or nucleus-containing droplets may also contain ambient RNAs specifically attached to or absorbed by cells or nucleus; (2) unlike cell- or nucleus-containing droplets, in empty droplets, the lack of endogenous RNAs may lead to more amplification of ambient RNAs and thus over-estimation of the contamination, e.g., the over-correction by SoupX and scAR on the scRNA-seq datasets. Second, these three methods are inapplicable to the processed gene-by-cell count matrices, which are common in public datasets and do not contain empty-droplet data.

In contrast, scCDC avoids these limitations by estimating the distribution of contaminated counts from real cells or nuclei, so scCDC can be applied to processed count matrices. Although DecontX can also be applied to processed count matrices, the correction efficacy of DecontX is low on highly contaminating genes. We speculate that the DecontX algorithm’s convergence and iteration setting require further optimization. However, scCDC also has its own limitation in that it may not be capable of identifying certain lowly contaminating genes as GCGs and, therefore, does not offer correction for these genes. For datasets with both highly and lowly contaminating genes, we recommend a combined use of scCDC and DecontX to harness the complementary advantages of both methods to achieve an effective correction for all genes.

What mainly distinguishes scCDC from the existing methods is that scCDC detects GCGs and only corrects the expression counts of GCGs. This gene-specific strategy, which was also used in scImpute for the imputation problem, minimizes data alteration to avoid the over-correction issue of SoupX and scAR [41]. In correcting the counts of GCGs, scCDC, SoupX-manual, and scAR are all effective methods, correcting the median expression of GCGs in eGCG − cells to around zero in most datasets (Fig. 4A). Nevertheless, none of the methods could clear all the counts of GCGs in eGCG − cells, leaving certain contaminative counts of GCGs in a small population of eGCG − cells (Additional file 3: Table S2), which may slightly affect cell clustering and other analyses. Of note, we were able to design scCDC to clear the counts of GCGs in eGCG − cells aggressively. However, this strategy will alter the natural count distribution of GCGs in the entire dataset and may hinder the combined use of scCDC with other methods.

It is noted that scCDC and DecontX require the pre-clustering of cells, an issue we discussed in the Method Appendix (Additional file 1). Notably, identifying known cell types is not significantly affected by ambient RNA contamination, at least in the datasets we have tested. This is verified by examination of cluster ARI before and after iterative correction by scCDC (Additional file 5: Table S4). And a number of cell-type annotation tools (Azimuth [42], SingleR [43], Cell Blast [44], SciBet [45]) and databases (CellMarker [46], PanglaoDB [47]) have been developed to help define cell types in a supervised way. For example, the NIH HuBMAP consortium has released Azimuth, which provides reference cell types for many human tissues (). Moreover, novel tools like scDesign3 can be used to justify the preclustering accuracy. In contrast to DecontX and scCDC, SoupX, CellBender, and scAR do not require cell pre-clustering (Table 1). However, we noticed that manually pre-defining contaminating genes after preclustering strikingly improved the correction accuracy of SoupX in all datasets we tested. In the automated setting, SoupX failed to provide sufficient correction, consistent with the result in a recent report [48]. These results again suggest the necessity of cell pre-clustering before contamination correction.

Similar to scRNA-seq and snRNA-seq data, single-cell proteomics data were also found to have contamination [11]. Accordingly, decontamination methods such as dbs were developed [49]. Although we focused on correcting the contamination in scRNA-seq and snRNA-seq data in this study, scCDC is also applicable to single-cell proteomics data in theory. The performance of scCDC on single-cell proteomics data can be benchmarked in a future study.

## Conclusions {#Sec11}

Contamination by ambient RNAs is ubiquitous in single-cell and single-nuclei RNA-seq assays. We proposed scCDC as a novel computational method to detect global contamination-causing genes and correct these genes’ expression data. The gene-specific correction strategy enables scCDC to correct highly contaminating genes and be less likely to over-correct lowly/non-contaminating genes, compared to the existing computational methods. Decontamination by scCDC improves marker gene identification and gene network construction.

---

[← Results](02-results.md) · [Up: contents](index.md) · [Methods →](04-methods.md)
