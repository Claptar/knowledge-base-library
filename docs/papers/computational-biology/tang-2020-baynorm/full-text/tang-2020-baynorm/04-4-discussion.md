---
title: 4 Discussion
source: https://doi.org/10.1093/bioinformatics/btz726/
source_file: sources/papers/tang-2020-baynorm/tang-2020-baynorm.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `tang-2020-baynorm.jats` from [papers/tang-2020-baynorm](https://doi.org/10.1093/bioinformatics/btz726/) — papers · tang-2020-baynorm, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 4 Discussion

We introduced bayNorm, a versatile Bayesian approach for implementing global scaling that simultaneously provides imputation of missing values and true counts recovery of scRNA-seq data. Bayesian methods have been applied to different aspects of RNA-seq data analysis before (Hardcastle and Kelly, 2010; Huang *et al.*, 2018; Kharchenko *et al.*, 2014; Vallejos *et al.*, 2015). We showed that using the binomial model and an empirical Bayes approach to estimating gene expression priors across cells results in simulated data almost identical to experimental scRNA-seq measurements. Importantly, this suggests that zero-inflated models are not required to explain the frequency of dropout observed in scRNA-seq (see also Svensson, 2019; Soneson and Robinson, 2018). Although designed initially for UMI-containing scRNA-seq protocols, a simple scaling factor makes bayNorm applicable to non-UMI data as well. This flexibility will allow using this approach with most present scRNA-seq datasets. We showed using datasets that combine smFISH and scRNA-seq, that bayNorm is accurately recovering true gene expression across a wide range of expression levels. This approach could therefore be particularly useful for quantitative analysis of more difficult scRNA-seq datasets, such as those generated from small quiescent cells or microbes, for instance. In fact, we have recently used bayNorm successfully in the first scRNA-seq study of fission yeast (Saint *et al.*, 2019).

One of the most powerful features of bayNorm is its use of gene expression priors directly calculated from gene expression values across cells. We showed that grouping cells according to experiment design or phenotypic features increased significantly the robustness and sensitivity of DE analysis. This removes almost completely the sequencing depth and capture efficiency biases, and reduces batch effects. Critically, this approach preserved accurate and sensitive detection of benchmark DE genes in contrast to some recently developed methods of batch correction. Also, where there is no prior knowledge available for cell types, using a global approach does not affect clustering of cell types. The clustering results could be improved if priors are iteratively improved using a method of simultaneous normalization and clustering as proposed in Prabhakaran *et al.* (2016).

Bayesian methods have been applied to different aspects of RNA-seq data analysis before (Hardcastle and Kelly, 2010; Huang *et al.*, 2018; Kharchenko *et al.*, 2014; Prabhakaran *et al.*, 2016; Vallejos *et al.*, 2015). The approach most related to bayNorm is taken by SAVER, which uses a Poisson-Gamma model and pooling information across genes for true count recovery (Huang *et al.*, 2018). In contrast, bayNorm uses a binomial model of mRNA capture as likelihood and achieves similar or improved performance relative to SAVER on real and simulated data (Figs 2–4).

Accurate estimation of cell capture efficiencies (or scaling factors) is central to most scRNA-seq normalization methods including bayNorm. Interestingly, we observed that the choice of cell-specific capture efficiencies affect how closely simulated data recovers statistics of real data. We therefore propose that comparison of drop-out rates per cell in simulated datasets and experimental data could be used as a tool to inform appropriate choice of global scaling factors and mean capture efficiency estimates. The option to tailor bayNorm priors based on phenotypic information about cell subpopulations will be a powerful asset for discovery of gene expression programs associated with specific phenotypic features of single cells such as cell size (Saint *et al.*, 2019). Finally, the concepts and mathematical framework behind bayNorm will be useful if combined with other emerging theoretical approaches such as deep learning (for instance Ding *et al.*, 2018; Eraslan *et al.*, 2019; Grønbech *et al.*, 2018; Lopez *et al.*, 2018; Wang and Gu, 2018). Overall, bayNorm provides a simple and integrated solution to remove the technical biases typical of scRNA-seq approaches, while enabling robust and accurate detection of cell-specific changes in gene expression. bayNorm has been made freely available as an R package () released in Bioconductor (Gentleman *et al.*, 2004).

---

[← 3 Results](03-3-results.md) · [Up: contents](index.md) · [Supplementary Material →](05-supplementary-material.md)
