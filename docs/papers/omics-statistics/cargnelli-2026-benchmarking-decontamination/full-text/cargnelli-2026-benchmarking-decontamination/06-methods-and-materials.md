---
title: Methods and materials
source: https://doi.org/10.64898/2026.01.13.699237/
source_file: sources/papers/cargnelli-2026-benchmarking-decontamination/cargnelli-2026-benchmarking-decontamination.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `cargnelli-2026-benchmarking-decontamination.pdf` from [papers/cargnelli-2026-benchmarking-decontamination](https://doi.org/10.64898/2026.01.13.699237/) — papers · cargnelli-2026-benchmarking-decontamination, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Methods and materials

## Decontamination methods

A total of seven different ambient RNA decontamination methods were included in the benchmark;
CellBender$^6$ (version 0.3.2), scAR$^{18}$ (version 0.7.0), CellClear$^{10}$ (version 0.0.3), scCDC$^{11}$ (version
1.4), FastCAR$^9$ (version 0.1.0), SoupX$^7$ (version 1.6.2), and DecontX$^3$ (version 1.6.0). All methods
were run with default parameters as described in their documentation, except for simulated and
negative control datasets.

The methods have different input requirements. Most methods (DecontX, SoupX, FastCAR, and
CellClear) by default use both a filtered and an unfiltered count matrix. For droplet-based datasets,
the filtered matrix used emptyDrops to detect putative cell-containing droplets. For non-dropletsbased datasets, the threshold on the number of counts for separating empty droplets from putative
cell-containing droplets was manually set. By default, scAR uses only a filtered count matrix, but it
has the option to run on unfiltered count matrices. This mode was not included in the benchmark as
the run time was unfeasible. By default, CellBender uses only an unfiltered count matrix and
automatically detects putative cells. SoupX and DecontX have the option to run using only a filtered
count matrix, this mode of operation was included in the benchmark. In addition to count matrices,
two methods (scCDC, and SoupX) require clustering information, which was obtained through the
standard Seurat v5 pipeline$^{19}$ manually specifying the number of dimensions and clustering
resolution (Supplemental Table S6). Subsequently, barcodes with high mitochondrial content were
removed.

## Datasets

Seven datasets covering 64 samples and 135.561 cells were used for benchmarking the ambient
RNA removal methods (Supplemental Table S1). These datasets span four different dataset
categories: species-mixing, strain-mixing, negative control and synthetic. There are three
species-mixing datasets, varying in their level of ambient RNA and complexity. The low complexity
species-mixing dataset is a one-to-one mixture of fresh frozen human 293T and mouse 3T3 cells.
Count matrices were downloaded from 10X Genomics$^{20}$. The medium complexity (GSE147203)
samples are mixtures of human islets of Langerhans spiked in with a mix of human Jurkat cells and
murine 32D cells$^{21}$. The high complexity (GSE207393) samples are human islets of Langerhans
xenografted into murine kidneys$^{22}$. For both the medium and high complexity samples, raw data was
aligned to a composite human-mouse genome$^{23}$ and quantified using STARsolo$^{24}$. After quality
control, we defined the species of origin by calculating the fraction of UMIs mapped to genes from
each species, and retained only cells with at least 75% mapped to one species. In these samples,
the ground truth for ambient RNA was defined as all UMIs assigned to genes from minor species,
and endogenous RNA was defined as all UMIs assigned to genes from major species.

For the strain-mixing dataset (GSE218853)$^{25}$, which are mixtures of kidney cells from three inbred
mice strains from two subspecies (*M. m. domesticus:* C57BL/6 and 129S1/SvImJ and *M. m.
castenus*: CAST/EiJ), preprocessed count matrices were downloaded. In these samples, the ground
truth for ambient and endogenous RNA was determined as the original authors, with the exception
that only genotype-specific single nucleotide polymorphisms (SNPs) with at least 2 counts were
included.

The negative control dataset, a smart-seq2 dataset (E-MTAB-5061) from human islets of
Langerhans$^{13}$, were aligned to the human genome (2020-A human GRCh38) and quantified using
STARsolo$^{24}$. Only three samples (HP1506401, HP1507101, and HP1508501T2D) were able to run
through all decontamination runs and therefore selected for further analysis. For these samples, the
ground truth for endogenous RNA were defined as all UMIs, as the samples are expected not to
contain ambient RNA.

Synthetic datasets were simulated by first fitting gene-wise negative binomial distributions to
single-cell RNA-seq data on MCF12A, HCC1500 and HS578T cells$^{26}$. For each real cell to be
simulated, we define a total number of UMIs and randomly sampled: a cell type using a specified
mixing probability and an ambient fraction for each cell using a normal distribution with a specified
average and standard deviation (Supplemental Table S1). Based on the total number of UMIs and
ambient fraction, we calculate the number of non-ambient UMIs and sample from the cell
type-specific negative binomial distribution. The remaining ambient UMIs were sampled from the two
other cell type-specific negative binomial distributions proportionally to the mixing fraction. For each
empty cell to be simulated, we define a total number of UMIs and sample from all cell type-specific
negative binomial distributions proportionally to the mixing fraction.

## Characterizing ambient RNA

The strain- and species-mixing datasets were used to characterize ambient RNA. For strain-mixing,
only features with at least two counts across genotype-specific SNPs were included, as ambient
RNA contamination can only be reliably estimated for those. For the medium complexity
species-mixing dataset, only the spike-in cells of the opposite species, compared to the source of
islets of Langerhans, were included. The major cell types were disregarded, as the spike-ins are low
abundant, why there is little-to-no spike-in to islet cell contamination.

For every cell, the fraction of ambient RNA was calculated and associated with regression analyses
with cellular parameters, including the number of UMIs, number of features, the fraction of UMIs
derived from exons, or from protein-coding, ribosomal, mitochondrial genes. For every feature, we
calculated the fraction of ambient RNA and associated it with overall expression levels, expression
frequency in cells or empty (less than 50 UMIs) droplets, as well as the fraction of UMIs derived from
exons.

## Evaluating ambient RNA removal and endogenous RNA preserved

Decontamination was evaluated by their ability to remove ambient RNA, preserve endogenous
signals, and how they affect biological interpretation. An ambient removal score (ARS) and
endogenous retain score (ERS) were evaluated by comparing the input to the corrected by each
method, calculating their relative differences.

$$ARS_i = \min\left(1,\ -\frac{\left|\sum_j A_{ij}^{(m)} - \sum_j X_{ij}\right|}{\sum_j X_{ij}}\right)$$

$$ERS_i = \max\left(0,\ 1 - \frac{\left|\sum_j E_{ij}^{(m)} - \sum_j X_{ij}\right|}{\sum_j X_{ij}}\right)$$

$X_{ij}$: input ambient (in ARS) or endogenous (in ERS) UMI counts

$E_{ij}^{(m)}$: endogenous counts after correction by method $m$

$A_{ij}^{(m)}$: ambient counts after correction by method $m$

$j$: cell index

$i$: gene index

For the negative control samples and synthetic datasets simulated without ambient RNA, only
endogenous retain was calculated, as these datasets do not contain any ambient contamination.

## Evaluating biological interpretation

The impact of ambient RNA removal on biological interpretation was evaluated across several tasks
and metrics.

For label transfer, we used Azimuth$^{15}$ and evaluated only islets of Langerhans and kidney-derived
cells across datasets, as we had reference atlases available. For species-mixing experiments, we
estimated the observed transcriptome with ambient RNA contamination by adding UMIs for genes
across species based on orthologs. The label transfer was evaluated by several metrics: the fraction
of highly confident (>0.9) mapping and annotation scores, the highest adjusted Rand index between
unsupervised clustering (resolutions between 0.05 and 1.0 in steps of 0.05) and transferred labels,
the label purity of neighborhoods identified by Milo$^{27}$, the average silhouette width of labels in
across the first 20 principal components, as well as the root mean square error (RMSE) of each cell
assigned to a label compared the average of all cells assigned to that label for features expressed in
at least 10% of the cells in that label.

For sample integration, all datasets were evaluated, except the low complexity species-mixing
dataset, as it is only one sample. For each dataset, we integrated the samples using Harmony$^{28}$.
The integration was evaluated by several metrics: the highest adjusted Rand index between
unsupervised clustering (resolutions between 0.05 and 1.0 in steps of 0.05) and sample labels, the
local inverse Simpson index (LISI)$^{14}$, principal component regression and average silhouette width
for sample labels in the first 20 principal components, the Gini coefficient of marker gene
expression, as well as the Moran I's and entropy of their expression using nearest neighbors.

For within-sample quality, all datasets were evaluated using several metrics: For species- and
strain-mixing datasets, the purity of neighborhoods identified by Milo$^{27}$ in terms of species of origin,
as well as the purity of marker genes of neighborhoods, as well as the LISI of species of origin using
the first 20 principal components. For all datasets, the Gini coefficient of marker gene expression, as
well as the Moran I's and entropy of their expression using nearest neighbors.

## Ranking methods

To rank methods for each evaluated task (ambient removal, endogenous retain, sample quality, label
transfer and batch integration), we averaged across metrics for each dataset and method pair, if
more than one metric was used to evaluate the task. Subsequently, the values were min-max scaled
across methods for each dataset and task pair and averaged across all datasets within each task.
The rank for each task was obtained by ordering the average task scores from highest to lowest. An
overall weighted score was obtained by calculating the weighted sum of task score, weighting
endogenous retain and ambient removal by a factor of 2, as these tasks are the core functionality of
the methods. The overall rank was obtained by ordering the weighted overall scores from highest to
lowest. Furthermore, we calculated a score for biological interpretation by taking the median of task
scores across the sample quality, label transfer and batch integration tasks. Finally, we calculated an
overcorrection score by min-max scaling only control samples based on the difference to the ground
truth across all tasks, except ambient removal and averaging across tasks and samples for each
method.

## Code availability

The code used to generate the results presented in this study will be made openly available on
GitHub at https://github.com/madsen-lab/AmbientRemovalBenchmark. The repository contains all
scripts and documentation required to reproduce the analyses.

## Data availability

This study solely used publicly available datasets, all listed in the 'Methods and Materials' section
and on the GitHub repository listed in the 'Code availability' section.

## Acknowledgements

This work was supported by grants from the Novo Nordisk Foundation (NNF21SA0072102 and
NNF21OC0068929), as well as the Danish National Research Foundation (DNRF grant No. 141) to
the Center for Functional Genomics and Tissue Plasticity (ATLAS). Computation for this project was
performed using the UCloud interactive HPC system, which is managed by the eScience Center at
the University of Southern Denmark. We thank all the members of the MadLab group for comments
and fruitful discussions that improved the manuscript.

## Conflicts of interest

The authors declare no competing interests.

---

[← References](05-references.md) · [Up: contents](index.md) · [Figures →](07-figures.md)
