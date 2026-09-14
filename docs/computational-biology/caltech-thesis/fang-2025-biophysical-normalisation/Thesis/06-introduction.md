---
title: INTRODUCTION
source: https://thesis.library.caltech.edu/17389/
source_file: sources/fang-2025-biophysical-normalisation/Thesis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# INTRODUCTION

**Source:** `Thesis.pdf` from [fang-2025-biophysical-normalisation](https://thesis.library.caltech.edu/17389/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In his seminal 2001 essay on statistical modeling, Leo Breiman identified two distinct modeling cultures: data models, which posit a stochastic mechanism for data generation and emphasize interpretability, and algorithmic models, which prioritize predictive performance without necessarily modeling the underlying process (Breiman, 2001). At the time, data models dominated the statistical modeling field, and Breiman advocated for broader adoption of algorithmic approaches. A parallel to this can be seen in early studies of (single) gene expression at single-cell resolution, where the focus was on the development of models for the data, with the goal of providing mechanistic insight into transcriptional dynamics.

Two decades later, the landscape of single-cell biology has changed dramatically. Rapid expansion of single-cell genomic data, driven by advances in sequencing technologies, has led to a dominant reliance on algorithmic models . In this thesis, we advocate for greater use of data models, which provide a more principled and insightful framework for uncovering meaningful biological insights from single-cell data. Rather than replacing algorithmic approaches, data models offer essential complementary strengths, particularly in terms of interpretability and mechanistic understanding (Gorin and Lior Pachter, 2024).

In this introduction, we begin by reviewing early stochastic models of gene expression, developed from the data model perspective, which lay the theoretical foundation for interpreting single-cell sequencing data. We then introduce the development and limitations of single-cell RNA sequencing (scRNA-seq), and current practices for scRNA-seq analysis. Finally, we explain the two modeling cultures in contemporary scRNA-seq analysis and argue for more mechanistic models in this rapidly evolving field.

## **1.1 The study of stochastic gene expression**

Gene expression, encompassing transcription (RNA synthesis) and translation (protein synthesis), is a central pillar of molecular biology research. As it inherently consists of a series of biochemical reactions such as transcriptional activation, mRNA synthesis, splicing, and degradation, one approach to studying gene expression is to

2

quantitatively model gene expression processes as biochemical reaction networks (or chemical reaction networks). Two major frameworks exist for such modeling: 1) deterministic models, based on the law of mass action, describe reactions using continuous concentrations and ordinary differential equations (ODEs) and focus on the graphical and algebraic structures of reaction networks (Feinberg, 2019); 2) stochastic models, grounded in the chemical master equation (CME), explicitly account for randomness in molecular interactions and focus on the properties of probability distributions of the systems (Van Kampen, 2007; C. Gardiner, 2009).

Since gene expression often involves molecules with low copy numbers (e.g., DNA in transcription initiation), stochastic models are frequently necessary to accurately describe gene expression dynamics. Stochastic fluctuations in gene expression contribute substantially to cellular heterogeneity in genetically homogeneous populations (Ko, Nakauchi, and Takahashi, 1990; Elowitz et al., 2002). As a result, the distribution of gene expression outcomes becomes critical, and stochastic chemical reaction networks, along with the chemical master equation, have become the standard framework for gene expression models. It describes the time evolution of the probability distribution over the discrete states of a biochemical system with a transition rate matrix. Furthermore, as common biochemical reactions only depend on the current states in a time-independent manner, biochemical reaction networks are modeled as homogeneous continuous time discrete state Markov chains, which have a time-independent transition rate matrix, i.e., homogeneous, and the time derivative of the probability distribution only depends on the current probability distribution, i.e., Markovian. A detailed discussion on the stochastic model, along with their deterministic counterparts as the large-volume limit, will be presented in Chapter 2.

The biochemical reactions incorporated in the gene expression models are based on the mechanistic characterization of gene expression processes. Canonical messenger RNA (mRNA) maturation involves an ordered sequence of regulated steps: (1) transcription initiation and elongation, (2) co-transcriptional splicing, (3) nuclear export, (4) cytoplasmic translation, and (5) active degradation. Among these steps, transcription initiation has been the most widely characterized and typically serves as the primary regulatory node in gene expression models. The subsequent steps are predominantly modeled as single first-order reactions with constant rates.

Let us begin with the simplest case: a constitutive zero-order transcription combined with first-order mRNA degradation. In this scenario, the stationary distribution of

3

mRNA levels follows a Poisson distribution. This model, which we will refer to as the constitutive model throughout this thesis, serves as the basic model for gene expression. If we extend it to include models with constitutive production and firstorder degradation for mRNA which still lead to a Poisson distribution at steady states, then despite its apparent simplicity, some recent experimental evidence supports its applicability to cytoplasmic mRNA counts (Battich, Stoeger, and Pelkmans, 2015). Notably, in such cases, nuclear export—rather than transcription—behaves as a constitutive zero-order process.

Beyond the constitutive model, more sophisticated models have been inspired by experimental advances. Early electron micrograph results revealed there were active and inactive period of transcription (Miller and McKnight, 1979). Additional evidence came from studies of inducible gene expression. In 1990, Ko et al. performed single-cell quantification of a glucocorticoid-inducible reporter gene, revealing heterogeneous expression that led to the formulation of the telegraph model (Ko, Nakauchi, and Takahashi, 1990; Ko, 1991; Ko, 1992). This model introduces two fundamental states of DNA: “on” state where active promoter permits RNA polymerase binding and transcription initiation; “off” state where inactive promoter halts RNA synthesis. The promoter switches between these two states with defined activation and inactivation rates, and transcription occurs at a transcription initiation rate only in the on state. The stationary distribution of the chemical master equation of this telegraph model has been solved analytically using generating function methods (Peccoud and Ycart, 1995), with a Fano factor (variance-to-mean ratio) greater than one, in contrast to the Poissonian statistics (Fano factor = 1) expected from constitutive model. The telegraph model has also been extended to incorporate more promoter states (Ham et al., 2020), as well as to include other modalities such as protein expression (Shahrezaei and Swain, 2008; Bokes, 2022).

Building on the telegraph model, further critical insights into transcriptional dynamics have been gained through advanced imaging technologies that enable the direct observation of mRNA production at the single-molecule level. Using an MS2-GFP fusion protein to tag mRNA transcribed from inducible promoters, Golding et al. demonstrated that transcription occurs in bursts in living E. coli cells (Golding et al., 2005). This behavior reflects a limiting case of the telegraph model, characterized by long "off" periods followed by brief, intense "on" periods during which multiple mRNAs are produced in rapid succession, a regime we will refer to as the bursty model. In this regime, mRNA counts follow a geometric distribution, with each

4

burst corresponding to a stochastic event that generates a variable number of transcripts. A similar bursting regime has been observed in mammalian cells when fitting with the telegraph model, where the promoter activation rate is an order of magnitude lower than the inactivation rate, and the transcription initiation rate is two orders of magnitude higher than the inactivation rate (Raj et al., 2006). Under these conditions, the telegraph model can be accurately approximated by the bursty model, in which only the ratio of the transcription initiation rate to the inactivation rate is identifiable. This ratio defines the size of the burst, effectively reducing the number of model parameters by one and simplifying the description of the system. Therefore, in conjunction with the telegraph model, the bursty model has since been routinely employed in stochastic modeling of gene expression (Singh and Bokes, 2012), as it offers a reasonable approximation to the complex biological reality (Jiao et al., 2024).

However, these studies have primarily focused on a limited number of genes. A central question that remains is whether all genes follow the bursty model, or more broadly, how gene expression patterns are distributed across different models. To address this question, the bursty model has been applied to a broader set of genes beyond the scope of previous studies, providing a genome-wide portrait of transcriptional dynamics (Taniguchi et al., 2010; Suter et al., 2011; Dar et al., 2012). For example, it has been fit to fluorescence data driven by the HIV-1 LTR promoter integrated into more than 8,000 individual human genomic loci, and revealed that the bursty model rather than the constitutive model is the predominant mode of gene expression (Dar et al., 2012). However, _in vivo_ mRNA and/or protein data across the entire genome without relying on artificial integration of reporter constructs would be valuable for gaining a more comprehensive understanding of transcriptional kinetics.

The limited throughput and perturbation are related to the fluorescent imaging technologies predominantly used in earlier studies on stochastic gene expression. Excitingly, recent advances in single cell sequencing have enabled us to measure high-throughput _in vivo_ gene expression.

## **1.2 Single-cell RNA sequencing**

Single-cell RNA sequencing (scRNA-seq) enables the isolation and high-throughput sequencing of mRNA transcripts from individual cells, providing transcriptomewide resolution at the single-cell level. Compared to imaging-based approaches,

5

sequencing technologies are more amenable to high-throughput analysis, allowing researchers to measure gene expression across tens of thousands of genes in individual cells. Since the first study of single cell RNA sequencing (scRNA-seq) was published in 2009 (F. Tang et al., 2009), the field has rapidly evolved, with numerous methodological innovations expanding its applications (Hashimshony et al., 2012; Ramsköld, Luo, et al., 2012; Klein et al., 2015; Macosko et al., 2015; Zheng et al., 2017). Initially focused solely on transcriptomic profiling, scRNA-seq technologies now facilitate multimodal measurements, enabling simultaneous detection of RNA, chromatin accessibility (ATAC-seq), and proteins in the same cell (Mimitou et al., 2021).

Despite providing unprecedented single-cell resolution of gene expression, scRNAseq also presents significant challenges and limitations. First, these measurements are notoriously noisy, presenting new challenges for model fitting. This noise arises from factors such as low capture efficiency, dropout events, amplification bias, and variability in transcript detection. Many studies have sought to characterize the technical noise in scRNA-seq data (Brennecke et al., 2013; Grün, Kester, and Oudenaarden, 2014; Kim, Kolodziejczyk, et al., 2015); nevertheless, there remains ongoing debate about the most appropriate statistical models for handling unique molecular identifier (UMI) counts (Svensson, 2020; Sarkar and Stephens, 2021). These challenges underscore the necessity of incorporating a well-calibrated technical noise model to accurately infer transcription kinetics (Gorin and Lior Pachter, 2023). Currently, the most common measurement models for scRNA-seq are Poisson and Bernoulli sampling with cell-wise capture rates (Sarkar and Stephens, 2021; W. Tang et al., 2023; Gorin and Lior Pachter, 2022b).

Another key limitation of scRNA-seq is that these methods provide only static snapshots of gene expression, as they require cell lysis and therefore cannot directly capture temporal dynamics. Metabolic labeling of newly synthesized mRNA can provide partial insight into past transcriptional events; however, the measurement still represents the distribution at a single time point (Erhard et al., 2022). However, scRNA-seq data often capture cells at different stages along underlying biological processes, which motivates the development of trajectory inference methods.

## **1.3 Current practices for scRNA-seq analysis**

In summary, scRNA-seq and fluorescent imaging technologies represent two complementary approaches: scRNA-seq captures the expression of thousands of genes

6

at a single time point, while fluorescent imaging enables dynamic tracking of a limited number of genes over time. Perhaps not surprisingly, the analysis of scRNA-seq data marks a clear departure from the mechanistic strategies that have traditionally guided the study of gene expression. Contemporary approaches are largely rooted in the algorithmic model culture, frequently relying on heuristics. To see this, let us look at steps in common scRNA-seq analysis workflow.


Figure 1.1: Common scRNA-seq analysis workflow.

The direct output of scRNA-seq experiments is a collection of sequencing reads, which are processed to generate count matrices. Then count matrices undergo an analysis workflow (Figure 1.1). A standard workflow can be broadly divided into two phases. The first phase involves data preprocessing, including quality control

7

(e.g., cell filtering), normalization, variance stabilization, feature selection, and dimensionality reduction. The second phase focuses on downstream analysis, such as clustering, differential expression (DE) analysis, trajectory inference, and RNA velocity.

At the beginning of analysis, cells are filtered based on their total transcript counts. A knee plot is used to identify high-quality cells by ranking barcodes based on total UMI or gene counts. The plot typically shows a sharp bend, i.e., knee, separating barcodes likely to represent real cells (above the knee) from low-quality or empty droplets (below). This helps determine a threshold for filtering valid cells during quality control. Genes are also filtered by retaining those expressed in a minimum number of cells.

Normalization in scRNA-seq aims to correct for technical variability (e.g., differences in sequencing depth, capture efficiency). Typically, a global-scaling normalization method is used, which calculates a single normalization factor per cell (cell size factor) using the sum of total counts. Then raw counts are scaled by cell size factors.

In scRNA-seq data, genes often exhibit a strong mean–variance relationship, where genes with higher mean expression levels also display greater variance. This heteroskedasticity poses challenges for downstream analyses such as clustering and differential expression. A common approach to mitigate this issue is to apply a variancestabilizing transformation. One widely used method is the log-transformation, typically _𝑙𝑜𝑔_ (1 + _𝑥_ ), which effectively reduces the dependence of variance on the mean. Despite its simplicity, this transformation performs surprisingly well in practice (Ahlmann-Eltze and Huber, 2023).

Both highly variable gene (HVG) selection and dimensionality reduction address the high dimensionality of scRNA-seq data, which captures expression levels for tens of thousands of genes in each cell. Typically, genes with high dispersion (varianceto-mean ratio) are selected as HVGs. For dimensionality reduction, methods such as PCA, t-SNE, and UMAP are commonly used, although they can introduce great distortions of the data (Chari and Pachter, 2021).

Here, we provide only a brief summary of the preprocessing steps. There are reviews offering more comprehensive discussions on scRNA-seq analysis (Luecken and Theis, 2019), and articles providing thorough benchmark of certain steps in the workflow (Booeshaghi and Lior Pachter, 2021; Booeshaghi, Hallgrímsdóttir, et al.,

8

2022; Ahlmann-Eltze and Huber, 2023; Rich et al., 2024).

## **1.4 The two cultures in scRNA-seq analysis**

We can clearly see the pattern that the methods in standard workflow do not have underlying models but are defined by the algorithms.

The prominence of algorithmic models can be partially explained by both the strengths and limitations of scRNA-seq technology. Although it allows highthroughput profiling of thousands of genes across large numbers of individual cells, it is also plagued by significant technical noise, reducing its reliability as a direct quantitative readout. Furthermore, the high dimensionality of the data makes it difficult to construct mechanistic models that fully capture the complexities of gene regulation.

However, we argue that data models should not be ignored in analyzing scRNAseq data. A balanced approach to scRNA-seq analysis requires integrating the strengths of both algorithmic and data modeling cultures. Algorithmic models excel at extracting patterns from high-dimensional data and scaling to large datasets, enabling powerful exploratory analyses. However, they often lack interpretability and mechanistic grounding. In contrast, data models, particularly mechanistic models grounded in biophysical principles, offer interpretable parameters and insights into the underlying biological processes. By combining the predictive power of algorithmic approaches with the interpretability and rigor of mechanistic modeling, we can gain a deeper and more principled understanding of single-cell gene expression. Given the prevalence of algorithmic models, there is a strong case for renewed investment in mechanistic modeling.

Several studies have successfully integrated traditional gene expression models with scRNA-seq data. For example, the telegraph and bursty models have been applied to scRNA-seq data to infer transcriptional bursting kinetics in various biological contexts (Kim and Marioni, 2013; Ramsköld, Hendriks, et al., 2024; Larsson et al., 2019; Gorin and Lior Pachter, 2022b; Tara Chari, Gorin, and Lior Pachter, 2024b). These efforts reflect a mechanistic perspective that aims to explain the observed data by explicitly modeling the underlying biological processes.

However, a mechanistic approach to scRNA-seq analysis goes beyond applying bursting models, since scRNA-seq has been used in a variety of ways. What we advocate for is a data model culture that emphasizes the formulation of biophysically inspired models and rigorous inference.

9

## **1.5 Outline**

This thesis summarizes my work in advancing this approach. Chapter 2 provides a review of the chemical master equation for stochastic chemical reaction systems, along with a theoretical study of the large-volume limit for infinite time. Chapter 3 introduces an extrinsic noise model for normalization. Chapters 4 presents a process time model for trajectory inference. The thesis concludes with a discussion of future directions in Chapter 5.

10

_C h a p t e r 2_

---

[← TABLE OF CONTENTS](05-table-of-contents.md) · [Up: contents](index.md) · [STOCHASTIC CHEMICAL REACTION SYSTEMS AND APPROXIMATIONS →](07-stochastic-chemical-reaction-systems-and-approximations.md)
