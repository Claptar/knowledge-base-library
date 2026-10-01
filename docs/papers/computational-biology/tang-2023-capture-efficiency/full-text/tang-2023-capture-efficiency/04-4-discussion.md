---
title: 4 Discussion
source: https://doi.org/10.1093/bioinformatics/btad395/
source_file: sources/papers/tang-2023-capture-efficiency/tang-2023-capture-efficiency.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `tang-2023-capture-efficiency.jats` from [papers/tang-2023-capture-efficiency](https://doi.org/10.1093/bioinformatics/btad395/) — papers · tang-2023-capture-efficiency, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 4 Discussion

In this article, we revisited the problem of inferring the burst kinetics of gene expression from scRNA-seq data. We provide a novel expression for the likelihood to be used for single-allele scRNA-seq data, which allows us to take cell-to-cell variation in cell size and capture efficiency correctly into account. We show that numerical challenges can make maximum likelihood estimation (MLE) unreliable. To overcome this limitation, we introduce likelihood-free approaches, including a modified method of moments (MME) and two simulation-based inference methods. We demonstrate the reliability and flexibility of the simulation-based inference methods through a series of benchmarks on synthetic and real data. We show that these methods also provide confidence intervals and could be easily generalized to nonsingle-allele situations, which makes them more widely applicable. We obtain the best results using simulation-based inference based on Bayesian neural networks (Gal and Ghahramani 2016, Jørgensen *et al.* 2022). Our analysis suggests the importance of properly taking into account cell size and capture efficiency variation and can be used to guide the design of scRNA-seq experiments suitable for reliable estimates of gene expression parameters. While, as expected, more cells and more sequencing depth will yield better results, we find that about 1000–2000 cells are sufficient to estimate the burst kinetics accurately.

Recent studies have used the maximum likelihood estimation method (Larsson *et al.* 2019) or Bayesian method (Kim and Marioni 2013) using a Beta-Poisson model without any normalization. As we show in this article, this approach can result in biased and distorted distributions of estimates for burst kinetic parameters, including the burst size. Also, we show that burst kinetics parameters become unidentifiable for lowly expressed genes and that this property could result in misleading results. While maximum likelihood estimation has good theoretical guarantees, computational challenges in evaluating the likelihood and also challenges in optimization can make this method less favourable. Indeed, recent studies have likewise highlighted the challenges with maximum likelihood estimation and the nonidentifiability for similar models of stochastic gene expression (Ham *et al.* 2021, Fu *et al.* 2022).

There are few available allele-specific scRNA-seq datasets, but UMI-based nonallele-specific scRNA-seq data are highly abundant. We have therefore modified the MME method and our simulation-based methods to infer the kinetic parameters directly from nonallele-specific (e.g. UMI) count matrices. Although we assume that the two gene copies have identical kinetic parameters and transcribe independently in this study, we note that these assumptions can easily be relaxed for simulation-based methods. Indeed, some recent studies have suggested evidence for allelic imbalance and dependence in burst kinetics across the gene alleles in existing scRNA-seq data (Choi *et al.* 2019, Mu *et al.* 2021). We applied our methods to two mouse brain scRNA-seq datasets. Our results indicate that gene regulation across stem cells and the ageing of the brain tends to be associated with the regulation of burst frequency and, to some degree, burst size. A recent study has proposed that epigenetic regulation of burst frequency in fitness genes upon stress could underlie the evolution of cancer (Loukas *et al.* 2023).

We note here that we are neglecting other possible sources of extrinsic variability, such as fluctuations in the kinetic rates due to fluctuations of other molecules in the cells (Ham *et al.* 2021). However, we have shown here that many gene expression correlations between alleles can be explained by accounting for variations in cell size and capture efficiency. In fission yeast, we have previously shown that it is possible to capture most of the extrinsic variability observed in gene expression by accounting for cell size variation (Sun *et al.* 2020). Other studies have included the effect of different cell cycle stages, replication and gene copy numbers (Fu *et al.* 2022). Sun and Zhang (2020) used allele-specific expressions in diploid cells and intrinsic and extrinsic noise decomposition to study the genetic factors affecting gene expression noise. We note that more detailed mechanistic models of RNA-sequencing protocols can help to explain more of the technical noise and biases in the data (Dyer *et al.* 2019, Fischer *et al.* 2019, Davies *et al.* 2021, Gorin and Pachter 2022, Luo *et al.* 2023).

Inferring kinetic parameters of stochastic gene expression from scRNA-seq data is challenging. First and foremost, the data are sparse and have missing values. This characteristic of the data presents an obstacle to any attempt to estimate the parameters accurately. In addition, the extrinsic variables, such as cell size and capture efficiency, are usually not known [for an exception, where cell size has been measured along with scRNA-seq, see Saint *et al.* (2019)]. Furthermore, measurements or theoretical considerations that constrain the kinetic parameters’ range are not readily available. Statistical analysis, such as the one presented in this article, would thus benefit from additional measurements or other constraints that would provide tighter priors. While many researchers have already studied the inference of kinetic parameters from high-throughput data, such as scRNA-seq data, several aspects are hence, by far, not fully explored. An important area of future research is using multi-omic single-cell data. The data are quickly becoming available and could thus inform our understanding of global gene expression variability (Lee *et al.* 2020, Argelaguet *et al.* 2021). Some research is already starting in this important area based on both statistical data integration (Argelaguet *et al.* 2021, Rautenstrauch *et al.* 2022, Rodosthenous *et al.* 2021) and model-based inference (La Manno *et al.* 2018, Bergen *et al.* 2020, Gorin and Pachter 2022). Ultimately, by harnessing gene-gene correlations, such multi-omic single-cell datasets could be used to infer genetic networks (Stumpf 2021, Qiu *et al.* 2022).

In summary, we proposed a simple and accurate method to take the variation of cell size and capture efficiency into account when performing the inference of burst kinetics from scRNA-seq data. We provide implementations of our likelihood-free approaches that are robust and flexible and apply them to synthetic and real data. Our analysis shows how state-of-the-art inference tools can help us to extract valuable information missed by standard approaches.

## Supplementary Material {#sec14}

Click here for additional data file.

## Acknowledgements {#ack1}

The authors acknowledge Ioannis Loukas and Paola Scaffidi for early discussions on the challenges in inferring burst kinetics from scRNA-seq data. They thank Zekai Li and Dimitris Volteras for providing detailed comments on the manuscript.

## Contributor Information {#_ci93_}

Wenhao Tang, Department of Mathematics, Imperial College London, London SW7 2BX, United Kingdom.

Andreas Christ Sølvsten Jørgensen, Department of Mathematics, Imperial College London, London SW7 2BX, United Kingdom; I-X Centre for AI in Science, Imperial College London, White City Campus, London W12 0BZ, United Kingdom.

Samuel Marguerat, MRC London Institute of Medical Sciences (LMS), London W12 0NN, United Kingdom; Institute of Clinical Sciences (ICS), Faculty of Medicine, Imperial College London, London W12 0NN, United Kingdom.

Philipp Thomas, Department of Mathematics, Imperial College London, London SW7 2BX, United Kingdom.

Vahid Shahrezaei, Department of Mathematics, Imperial College London, London SW7 2BX, United Kingdom.

## Supplementary data {#sec15}

Supplementary data are available at *Bioinformatics* online.

## Conflict of interest {#sec16}

None declared.

## Funding {#sec17}

This work was supported by the Oli Hilsdon Foundation through The Brain Tumour Charity [GN-000595] in connection with the program ‘Mapping the spatio-temporal heterogeneity of glioblastoma invasion’; a UKRI Future Leaders Fellowship [MR/T018429/1 to P.T.]; and the Engineering and Physical Sciences Research Council [EP/N014529/1 to V.S.]. Finally, A.C.S.J. was supported by the Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship, a Schmidt Futures programme.

## Data availability {#sec18}

Regard to real experimental data used in this study, scRNA-seq allele specific data can be downloaded from ; scRNA-seq data from Mizrak study can be downloaded from GEO: [GSE109447](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109447); scRNA-seq data from Ximerakis study can be downloaded from GEO: [GSE129788](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129788).

## References {#ref1}

## Associated Data {#_ad93_}

### Supplementary Materials {#_adsm93_}

Click here for additional data file.

### Data Availability Statement {#_adda93_}

Regard to real experimental data used in this study, scRNA-seq allele specific data can be downloaded from ; scRNA-seq data from Mizrak study can be downloaded from GEO: [GSE109447](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE109447); scRNA-seq data from Ximerakis study can be downloaded from GEO: [GSE129788](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129788).

---

[← 3 Results](03-3-results.md) · [Up: contents](index.md)
