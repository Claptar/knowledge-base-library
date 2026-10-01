---
title: Discussion
source: https://doi.org/10.1093/gigascience/giaa151/
source_file: sources/papers/young-behjati-2020-soupx/young-behjati-2020-soupx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `young-behjati-2020-soupx.jats` from [papers/young-behjati-2020-soupx](https://doi.org/10.1093/gigascience/giaa151/) — papers · young-behjati-2020-soupx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Discussion

We have shown that cell-free RNA is omnipresent in droplet-based scRNA-seq data and have proposed a method to identify, quantify, and remove its contaminating effect. We find that accounting for contamination improves the specificity of marker genes, identifies new markers, and is essential for the correct biological interpretation of complex experiments.

We have shown some potential misinterpretations of kidney tumour and fetal liver data driven by ambient mRNA contamination, but examples are sure to abound in other tissues. For instance, in endocrine tissues, it is crucial to understand which cell types secrete a particular hormone. The misassigned expression of even a single hormone gene can fundamentally change how investigators think about a cell type. Such problems will become increasingly common as efforts to compare similar cell types across tissues progress.

The best case for applying SoupX occurs when the user can specify a set of genes and cells where there is no cell endogenous expression, i.e., a set of genes and cells where it is safe to assume that the only source of expression for these genes is from background contamination. The expectation is that biological knowledge of the experiment being performed will guide this choice. Where such a set of genes and cells can be provided, this will yield the best results.

For example, solid-tissue experiments are frequently highly contaminated with red blood cells and red cell lysis is used to prepare the samples [15]. As such, haemoglobin genes are often ubiquitously present in the background. Furthermore, red blood cells are the only cells that produce haemoglobin under normal physiological conditions, so for the set of haemoglobin genes, it is safe to assume that there is no cell endogenous expression for cells that are not red blood cells. Finally, red blood cells express haemoglobin genes in such extreme abundance that they can be trivially identified by comparing the ratio of observed haemoglobin genes to that present in the background contamination (Supplementary Fig. S10). These properties make haemoglobin genes a sensible choice for most solid-tissue experiments.

Heuristics, such as the bimodal expression ranking in Supplementary Fig. S5, can help aid biologically motivated gene selection. However, we recognize that selecting an appropriate set of genes to estimate contamination will not always be possible. To address this issue, we include an automated contamination estimation procedure. By using all high-quality marker genes identified in the data to independently estimate the contamination fraction, this method estimates the true contamination fraction by assuming that inaccurate estimates of the contamination fraction are not strongly correlated (i.e., there is no preferred, incorrect estimate). We show that this automation gives comparable results to the manual method. Although this procedure requires cells to be clustered, clustering information is used primarily to identify marker genes. As such, consistent estimates of the contamination fraction will be obtained for any sensible clustering of the data.

It is also possible to manually specify the contamination fraction, which can be useful when the aforementioned estimation procedures are deemed inaccurate or it is desirable to overcorrect the data. For most applications, the consequences of manually setting an unrealistically high contamination rate are likely to be minimal. Contamination is preferentially removed from genes closest to the background expression (i.e., genes with low levels of expression), meaning that setting a higher global contamination rate is unlikely to completely remove the expression of genes that are truly markers of a cell. Thus in some applications it may be preferable to overcorrect for background contamination and remove a small amount of genuine signal to ensure that all the background contamination has been removed. We also find that our method is robust to small inaccuracies in the estimation of the global contamination rate (Supplementary Fig. S4).

Since SoupX was first released, several other tools have been developed that aim to remove background contamination. SoupOrCell [21] uses the identification of conflicting genotypes to identify ambient RNA contamination, limiting its application to mixed-genotype experiments. Cell Bender [22] uses a deep generative model to estimate shared expression patterns likely to represent distinct cell types while simultaneously removing contamination. This deep generative model comes with a heavy computational cost compared to other tools, and the output of the model (which in effect estimates *m_(g,\ c)* for each cell type) provides an imputed cell profile rather than raw counts with the background “subtracted off,” which SoupX provides. Finally, DecontX [23] relies on accurate clustering of the data to estimate and remove the background without the need for gene counts from empty droplets. This allows DecontX to be applied when empty droplet counts are not available but also means that the results are potentially heavily dependent on the accuracy of the clustering provided. By contrast, SoupX can be applied generally, is computationally inexpensive, and does not depend heavily on accurate pre-annotation of input data.

To make our method easily applicable, we provide an R package, SoupX, which can be used to estimate and remove ambient mRNA contamination. This package is available on the Comprehensive R Archive Network (CRAN) and is provided with a vignette to assist the user in understanding how best to apply the method. The output of the SoupX package is a corrected table of counts, which can be used as input for standard workflows, and running SoupX does not add appreciably to the computational cost of standard single-cell analyses. We envision background correction forming a standard part of droplet-based scRNA-seq analysis pipelines.

## Data Availability {#h1content1608223168049}

The 10X species-mixing dataset was the mixture of the human cell line 293T and the mouse cell line 3T3 described in [2]. We used the data mapped and quantified using Cell Ranger 1.1.0 from . The DropSeq species-mixing data were obtained from [14], specifically SRR1748411. The PBMC data were taken from [2]. The kidney tumour dataset was taken from [15]. The fetal liver data [16] are available from ArrayExpress with accession code E-MTAB-7407. The mapped datasets supporting the results of this article are available in the GigaDB repository [24].

## Availability of Supporting Code and Requirements {#h1content1608223212567}

Project name: SoupX

Project home page:

Operating systems: Platform indepdent

Programming language: R

Other requirements: R 3.5.0 or higher

License: GNU GPL

RRID:

biotools ID: soupx

The SoupX R package is also available from CRAN at , the scripts to reproduce this analysis are at , and a Docker image containing all code and data needed to generate the results in this article can be obtained from .

---

[← Ambient RNA Confounds Interpretation in Complex Experiments](05-ambient-rna-confounds-interpretation-in-complex-experiments.md) · [Up: contents](index.md) · [Additional Files →](07-additional-files.md)
