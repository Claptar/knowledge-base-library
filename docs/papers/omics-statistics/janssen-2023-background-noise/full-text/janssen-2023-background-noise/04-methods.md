---
title: Methods
source: https://doi.org/10.1186/s13059-023-02978-x/
source_file: sources/papers/janssen-2023-background-noise/janssen-2023-background-noise.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `janssen-2023-background-noise.jats` from [papers/janssen-2023-background-noise](https://doi.org/10.1186/s13059-023-02978-x/) — papers · janssen-2023-background-noise, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Methods

## Mice {#Sec14}

Three mouse strains were ordered from Jackson Laboratory at 6–8 weeks of age: C57BL/6J (000664), CAST/EiJ (000928), and 129S1/SvlmJ (002448). All animals were subjected to intracardiac perfusion of PBS to remove blood. Kidneys were dissected, divided into 1/4s, and subjected to the tissue dissociation protocol, stored in RNAlater, or snap-frozen in liquid nitrogen.

## Tissue dissociation for single cell isolation {#Sec15}

The single cell suspensions were prepared following an established protocol [24] with minor modifications. In detail, one of each kidney sagittal quarter from three perfused mice of different strains C57BL/6, CAST/EiJ and 129S1/SvImJ were harvested into cold RPMI (Thermo Fisher Scientific, 11875093) with 2% heat-inactivated Fetal Bovine Serum (Gibco, Thermo Fisher Scientific, 16140-071; FBS) and 1% penicillin/streptomycin (Gibco, Thermo Fisher Scientific, 15140122). Each piece of the tissue was then minced for 2 min with a razor blade in 0.5 ml 1x liberase TH dissociation medium (10x concentrated solution from Millipore Sigma, 05401135001, reconstituted in DMEM/F12(Gibco, Thermo Fisher Scientific, 11320-033 in a petri dish on ice. The chopped tissue pieces were then pooled into one 1.5 ml Eppendorf tube and incubated in a thermomixer at 37${}^{\circ }$C for 1 hour at 600rpm with gentle pipetting for trituration every 10 min. The digestion mix was then transferred to a 15 ml conical tube and mixed with 10 ml 10% FBS RPMI. After centrifugation in a swinging bucket rotor at 500g for 5 min at 4 °C and supernatant removal, the pellet was resuspended in 1ml red blood cell lysing buffer (Sigma Aldrich, R7757). The suspension was spun down at 500g for 5 min at 4 °C followed by supernatant removal. The pellet cleared of the red blood cell ring was then resuspended in 250 $\upmu$l Accumax (Stemcell Technologies, 7921) and incubated at 37 °C for 3 mins. The reaction was stopped by mixing with 5 ml 10% FBS RPMI and spinning down at 500g for 5 min at 4 °C followed by supernatant removal. The cell pellet was then resuspended in PBS with 0.4% BSA (Sigma, B8667) and passed through a 30 $\upmu$m filter (Sysmex, 04-004-2326). The cell suspension was then assessed for viability and concentration using the K2 Cellometer (Nexcelom Bioscience) with the AOPIcell stain (Nexcelom Bioscience, CS2-0106-5ML).

## Nuclei isolation from RNAlater preserved frozen tissue {#Sec16}

The single nuclei suspensions were prepared following an established protocol [25] with minor modifications. In detail, the RNAlater reserved frozen tissue of 3 mice kidney quarters were thawed and transferred to one petri dish preloaded with 1 ml TST buffer containing 10 mM Tris, 146 mM NaCl, 1 mM CaCl2, 21 mM MgCl2, 0.03% Tween-20 (Roche, 11332465001), and 0.01% BSA (Sigma, B8667). It was minced with a razor blade for 10 min on ice. The homogenized tissue was then passed through a 40 $\upmu$m cell strainer (VWR, 21008-949) into a 50 ml conical tube. One ml TST buffer was used to rinse the petri dish and collect the remaining tissue into the same tube. It was then mixed with 3 ml of ST buffer containing 10 mM Tris, 146 mM NaCl, 1 mM CaCl2, and 21 mM MgCl2 and spun down at 500g for 5 min at 4 °C followed by supernatant removal. In the second experiment this washing step was repeated 2 more times. The pellet was resuspended in 100 $\upmu$l ST buffer and passed through a 35 $\upmu$m filter. The nuclei concentration was measured using the K2 Cellometer (Nexcelom Bioscience) with the AO nuclei stain (Nexcelom Bioscience, CS1-0108-5ML).

## Single-cell and single-nucleus RNA-seq {#Sec17}

The cells or nuclei were loaded onto a 10× Chromium Next GEM G chip (10x Genomics, 1000120) aiming for recovery of 10,000 cells or nuclei. The RNA-seq libraries were prepared using the Chromium Next GEM Single Cell 3’ Reagent kit v3.1 (10× Genomics, 1000121) following vendor protocols. The libraries were pooled and sequenced on NovaSeq S1 100c flow cells (Illumina) with 28 bases for read1, 55 bases for read2 and 8 bases for index1 and aiming for 20,000 reads per cell.

## Processing and annotation of scRNA-seq and snRNA-seq data {#Sec18}

The scRNA-seq and snRNA-seq data were processed using Cell Ranger 3.0.2 using as reference genome and annotation mm10 version 2020A for the scRNA-seq data and and a pre-mRNA version of mm10 2.1.0 as reference for snRNA-seq. In order to identify cell containing droplets we processed the raw UMI matrices with the DropletUtils package [5]. The function barcodeRanks was used to identify the inflection point on the total UMI curve and the union of barcodes with a total UMI count above the inflection point and Cell Ranger cell call were defined as cells.

For cell type assignment we used 3 scRNA-seq and 4 snRNA-seq experiments from Denisenko et al. [14] as a reference. Cells labeled as “Unknown” (*n*=46), “Neut” (*n*=17) and “Tub” (*n*=1) were removed. The reference was log-normalized and split into seven count matrices based on chemistry, preservation and dissociation protocol. Subsequently, a multi-reference classifier was trained using the function *trainSingleR* with default parameters of the R package SingleR version 1.8.1 [20]. After this processing, we could use the data to classify our log-normalized data using the *classifySingleR* function without fine-tuning (fine.tune = F). Hereby, each cell is compared to all seven references and the label from the highest-scoring reference is assigned. Some cell type labels were merged into broader categories after classification: cells annotated as “CD\_IC,” “CD\_IC\_A,” or “CD\_IC\_B” were relabeled as “CD\_IC,” cells annotated as “T,” “NK,” “B,” or “MPH” were relabeled as “Immune.” Cells that were unassigned after pruning of assignments based on classification scores were removed for subsequent analyses.

## Demultiplexing of mouse strains {#Sec19}

A list of genetic variants between mouse strains was downloaded in VCF format from the Mouse Genomes Project [13], accessed on 21 October 2020. This reference VCF file was filtered for samples CAST\_EiJ, C57BL\_6NJ and 129S1\_SvImJ and chromosomes 1–19. Genotyping of single barcodes was performed with cellsnp-lite [26], filtering for positions in the reference VCF with a coverage of at least 20 UMIs and a minor allele frequency of at least 0.1 in the data (–minCOUNT 20, –minMAF 0.1). Vireo [22] was used to demultiplex and label cells based on their genotypes. Only cells that could be unambiguously assigned to CAST\_EiJ (CAST), C57BL\_6NJ (BL6) or 129S1\_SvImJ (SvImJ) were kept, cells labeled as doublet or unassigned were removed.

## Genotype-based estimation of background noise {#Sec20}

Based on the coverage filtered VCF-file (see above), we identified homozygous SNPs that distinguish the three strains and removed SNPs that had predominantly coverage in only one of the strains (1st percentile of allele frequency).

In most parts of the analysis, we focused on the comparison between the mouse subspecies, *M. m. domesticus* and *M. m. castaneus*. To this end, we subseted reads (UMI-counts) that overlap with SNPs that distinguish the two mouse subspecies.

To estimate background noise levels based on allele counts of genetic variants, an approach described in Heaton et al.[15] was adapted to estimate the total amount of background noise for each cells. First, the abundance of endogenous and foreign allele counts (i.e., cross-genotype background noise) was quantified per cell. Because of the filter for homozygous variants, there are two possible genotypes for each locus, denoted as 0 for the endogenous allele, i.e., the expected allele based on the strain assignment of the cell, and 1 for the foreign allele. The probability for observable background noise at each locus *l* in cell *c* is given by

$$\begin{aligned} p=\rho _{c}*\frac{A_{l,1}}{A_{l,0}+A_{l,1}} \end{aligned}$$

where $\rho _{c}$ is the total background noise fraction in a cell and the experiment wide (over cells and empty droplets) foreign allele fraction is calculated from the foreign allele counts $A_{l,1}$ and the endogenous allele counts $A_{l,0}$. The foreign allele fraction is then used to account for intra-genotype background noise (contamination within endogenous allele counts).

The observed allele counts $A_c$ per cell are modeled as draws from a binomial distribution with the likelihood function:

$$\begin{aligned} P(A_c|\rho _{c}) = \prod _{l \in L}{A_{l,c,0}+A_{l,c,1}\atopwithdelims (){A_{l,c,1}}}p^{A_{l,1}}(1-p)^{A_{l,0}} \end{aligned}$$

A maximum likelihood estimate of $\rho _c$ was obtained using one dimensional optimization in the interval [0,1].

The 95% confidence interval of each $\rho _c$ estimate was calculated as the profile likelihood using the function *uniroot* of the R package stats [27].

## Comparison of endogenous, contamination, and empty droplet profiles {#Sec21}

Empty droplets were defined based on the UMI curve of the barcodes ranked by UMI counts, thus selecting barcodes from a plateau with $\sim 500-1000$ UMIs (Additional file 1: Fig. S5). For the following analysis, the presence of *M. m. domesticus* alleles in *M. m. domesticus* cells (i.e., endogenous), in *M. m. castaneus* cells (i.e., contamination) and empty droplets was compared. After this filtering, we summarized counts per gene and across barcodes of the same category to generate pseudobulk profiles.

In order to estimate cell type composition in the empty and contamination profiles, we used the deconvolution method implemented in SCDC[16], the endogenous single cell allele counts from the respective replicate were used as reference (*qcthreshold =* 0.6). In addition, cell type filtering (frequency>0.75%) was applied. Endogenous, contamination and empty pseudobulk profiles from each replicate were deconvoluted using their respective single cell/single nucleus reference.

To compare the correlation between the different profiles, pseudobulk counts were downsampled to the same total size.

## Detection of barcode swapping events {#Sec22}

Information about the number of reads per molecule and the combination of cell barcode (CB), UMI and gene were extracted from the molecule info file in the Cellranger output. We assume that a combination of CB and UMI corresponds to a single original molecule. Thus we define a PCR chimera as a non-unique CB-UMI combination in which multiple genes were associated with the same CB and UMI. Since we can only detect PCR chimera, if we detect at least 2 reads for a CB-UMI combination, we also restrict the total molecule count to CB-UMI combinations with at least 2 reads for the calculation of the chimera fraction.

For the comparison of reads/UMI the identified chimera were intersected with identified cross-genotype contamination. To this end, the the analysis was restricted to *M. m. castaneus* cells and CB-UMI-gene combinations which can be associated with an informative SNP. The number of reads/UMI was summarized per CB-UMI-gene combination for chimera (as defined above), unique CB-UMI-gene combinations with coverage for an endogenous allele (endo) and unique CB-UMI-gene combinations with coverage for a foreign allele (cont).

## Evaluation of marker gene expression {#Sec23}

A list of marker genes for Proximal tubule cells (PT), Principal cells (CD\_PC), Intercalated cells (CD\_IC), and Endothelial cells (Endo) was downloaded from the public database PanglaoDB [17], accessed on 13 May 2022.

Log2 fold changes contrasting PT cells against all other cells were calculated with Seurat using the function *FindMarkers* after normalization with *NormalizeData*. The expression fraction *e* of PT markers was calculated as the fraction of cells for which at least 1 count of that gene was detected. To contrast expression fraction in PT cells against non-PT, the negative log-ratio was calculated as $-log((e_{PT}+1)/(e_{non-PT}+1))$.

## Computational background noise estimation and correction methods {#Sec24}

*CellBender* [4] makes use of a deep generative model to include various potential sources of background noise. Cell states are encoded in a lower-dimensional space and an integer matrix of noise counts is inferred, which is subsequently subtracted from the input count matrix to generate a corrected matrix.

The *remove-background* module of CellBender v0.2.0 was run on the raw feature barcode matrix as input, with a default *fpr* value of 0.01. For the comparison of different parameter settings, *fpr* values of 0.05 and 0.1 were also included in the analysis. For the parameter *expected-cells* the number of cells after cell calling and filtering in each replicate was provided. The parameter *total-droplets-included* was set to 25,000.

*SoupX *[11] estimates the experiment-wide amount of background noise based on the expression of strong marker genes that are expected to be expressed exclusively in one cell type. These genes can either be provided by the user or identified from the data. A profile of background noise is inferred from empty droplets. This profile is subsequently removed from each cell after aggregation into clusters to generate a corrected count matrix.

Cluster labels for SoupX were generated by Louvain clustering on 30 principal components and a resolution of 1 as implemented by *FindClusters* in Seurat after normalization and feature selection of 5000 genes. Providing the CellRanger output and cluster labels as input, data were imported into SoupX version 1.6.1 and the background noise profile was inferred with *load10X*. The contamination fraction was estimated using *autoEstCont* and background noise was removed using *adjustCounts* with default parameters.

For the comparison of parameter settings, different resolution values (0.5, 1, 2) for Louvain clustering were tested, alongside with manually specifying the contamination fraction (0.1, 0.2).

*DecontX *[8] is a Bayesian method that estimates and removes background noise by modeling the expression in each cell as a mixture of multinomial distributions, one native distribution cell’s population and one contamination distribution from all other cell populations. The main inputs are a filtered count matrix only containing barcodes that were called as cells and a vector of cluster labels. The contamination distribution is inferred as a weighted combination of multiple cell populations. Alternatively, it is also possible to obtain an empirical estimation of the contamination distribution from empty droplets in cases where the background noise is expected to differ from the profile of filtered cells.

The function *decontX* from the R package celda version 1.12.0 was run on the filtered, unnormalized count matrix and clusters were inferred with the implemented default method based on UMAP dimensionality reduction and dbscan [28] clustering. For the “DecontX\_default” results the parameter “background” was set to NULL, i.e., estimating background noise based on cell populations in the filtered data only. “DecontX\_background” results were obtained by providing an unfiltered count matrix including all detected barcodes as “background” to empirically estimate the contamination distribution. Besides the default clustering method implemented in DecontX, cluster labels obtained from Louvain clustering (resolution 0.5, 1, and 2) were also provided to test different parameter settings.

## Evaluation metrics {#Sec25}

### Estimation accuracy {#Sec26}

The genotype-based estimates $\rho _c$ for *M. m. castaneus* cells served as ground truth to evaluate the estimation accuracy of different methods. For each method cell-wise background noise fractions $a_c$ were calculated from the corrected count matrix *X* and the uncorrected (“raw”) count matrix *R* as

$$\begin{aligned} a_c = 1-{\frac{\sum _gx_{c,g}}{\sum _gr_{c,g}}} \end{aligned}$$

for cells *c* and genes *g*.

**RMSLE** The Root Mean Squared Logarithmic Error (RMSLE) is a lower bound metric that we use to quantify the difference between estimated background noise fractions per cell $a_c$ from different computational background correction methods and the genotype-based estimates $\rho _c$, obtained from genotype based estimation. It is calculated as:

$$\begin{aligned} RMSLE = \sqrt {\frac{1}{n}\sum _{c=1}^{n}(log(a_c+1)-log(\rho _c+1))^2} \end{aligned}$$

**Kendall’s **

$\tau$ To evaluate how well cell-to-cell variation of the background noise fraction is captured by the estimated values $a_c$, the Kendall rank correlation coefficient $\tau$ to the genotype-based estimates $\rho _c$ was computed using the implementation in the R package stats [27] as $\tau = cor(a_c,\rho _c, method = ``kendall'')$.

### Marker gene detection {#Sec29}

The same set of 10 PT marker genes from PanglaoDB as in the “Evaluation of marker gene expression” section was used to evaluate the improvement on marker gene detection on corrected count matrices.

**Log2 fold change** for each gene between the average expression in PT cells and average expression in other cells were obtained using the *NormalizeData* and *FindMarkers* functions in Seurat version 4.1.1.

***Expression fraction*** Entries in each corrected count matrix were first rounded to the nearest integer. The expression fraction of each gene in a cell population was calculated as the fraction of cells for which at least 1 count of that gene was detected. For evaluation of PT marker genes, unspecific detection is defined as the expression fraction in non-PT cells.

### Cell type identification {#Sec30}

**Prediction score** Each corrected count matrix was log-normalized and reference-based classification in SingleR [20] was performed with a pre-trained model (see “Processing and annotation of scRNA-seq and snRNA-seq data” section) on data from Denisenko et al. [14]. SingleR provides *delta* values as a measure for classification confidence, which depicts the difference of the assignment score for the assigned label and the median score across all labels. The *delta* values for each cell were retrieved using the function *getDeltaFromMedian* relative to the cells highest-scoring reference. A prediction score per cell type was calculated by averaging *delta* values across individual cells and a global prediction score per replicate was calculated by averaging across cell type prediction scores.

**Average silhouette** The silhouette width is an internal cluster evaluation metric to contrast similarity within a cluster with similarity to the nearest cluster. The cell type annotations from reference-based classification were used as cluster labels here. Count matrices were filtered to select for *M. m. castaneus* cells and cell types with more than 10 cells. Distance matrices were computed on the first 30 principal components using euclidean distance as distance measure. Using the cell type labels and distance matrix as input, the average silhouette width per cell type was computed with the R package cluster version 2.1.4. An *Average silhouette* per replicate was calculated as the mean of cell type silhouette widths.

**Purity** Purity is an external cluster evaluation metric to evaluate how well a clustering recovers known classes. Here, *Purity* was used to assess to what extent unsupervised cluster labels correspond to cell types. Count matrices were filtered to select for *M. m. castaneus* cells and cell types with more than 10 cells and Louvain clustering as implemented in *FindClusters* of Seurat version 4.1.1 on the first 30 principal components and with a resolution parameter of 1 was used to get a cluster label for each cell. Providing cell type annotations as true labels alongside the cluster labels, *Purity* was computed with the R package ClusterR version 1.2.6 [29].

***k-NN overlap*** To evaluate the lower-dimensional structure in the data beyond clusters and cell-types *k*-NN overlap was used as described in Ahlmann-Eltze and Huber [30]. A ground truth reference *k*-NN graph was constructed on a ’genotype-cleaned’ count matrix, only counting molecules that carry a subspecies-endogenous allele. Raw and corrected count matrices were filtered to contain the same genes as in the reference and a query *k*-NN graph was computed on the first 30 principal components. The *k*-NN overlap summarizes the overlap of the 50 nearest neighbors of each cell in the query with the reference *k*-NN graph.

---

[← Discussion](03-discussion.md) · [Up: contents](index.md) · [Supplementary information →](05-supplementary-information.md)
