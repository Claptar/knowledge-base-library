---
title: Methods
source: https://doi.org/10.1186/s13059-024-03284-w/
source_file: sources/papers/wang-2024-sccdc/wang-2024-sccdc.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `wang-2024-sccdc.jats` from [papers/wang-2024-sccdc](https://doi.org/10.1186/s13059-024-03284-w/) — papers · wang-2024-sccdc, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Methods

### Calculation of cell-cluster-specific gene entropy divergences in scCDC {#Sec13}

For gene $g$ in cell cluster $c$, the *entropy* is defined as

$$E_{g,c} = - \sum\limits_{n \in V}p_{n,g,c}\text{log}_{2}{(p_{n,g,c})},$$

where $V$ is the set of unique values in $v_{g,c}$, a vector of gene $g$’s counts in the cells in cluster $c$; $p_{n,g,c}$ is the frequency of the count value $n$ in $v_{g,c}$, defined as

$$p_{n,g,c} = \frac{#\mspace{6mu}\text{of occurrences of value}\mspace{6mu} n\text{in}\mspace{6mu} v_{g,c}}{\text{length of}\mspace{6mu} v_{g,c}}.$$

For cell cluster $c$, the following procedure is used to calculate the cell-cluster-specific *expected entropy-expression curve*, inspired by the ROGUE score in [50].

1.  Calculate each gene g’s mean expression in cell cluster c as

$$M_{g,c} = \text{log}\left( {\text{(average of},v_{g,c},{) + 1}} \right)\text{,}$$

And calculate $E_{g,c}$ defined above.

1.  For $b = 1,\cdots,10$, in the $b$-th subsampling run, do the following.

    1.  Randomly sample 80% of genes.

    2.  Use the R function smooth.spline() to fit a curve between the sampled genes’ entropy values (*y*; response variable) and mean expression values (*x*; explanatory variable), using the following R code:$$\text{smooth}.\text{spline}(\text{M}_{\text{c}}^{\text{b}},\text{E}_{\text{c}}^{\text{b}},\mspace{6mu}\text{spar}\mspace{310mu} = \mspace{310mu} 1),$$

        where $M_{c}^{b}$ is a vector containing the randomly sampled genes’ $M_{g,c}$ values, and $E_{c}^{b}$ is a vector containing the randomly sampled genes’ $E_{g,c}$ values. Denote the fitted curve by function ${\hat{f}}^{b}$ that maps a gene’s mean expression to entropy.

    3.  For each sampled gene $g$, calculate the residual $r_{g,c}^{b} = {\hat{f}}^{b}\left( M_{g,c} \right) - E_{g,c}$, i.e., the difference between the gene’s fitted entropy from step ii and the actual entropy. Pool all residuals into a vector $r_{c}^{b}$. Assuming all residuals follow a normal distribution, define gene $g$ as an outlier if its residual falls into the top 1% tail of the fitted normal distribution, i.e., using R code, if

        $$1 - \mspace{6mu}\text{pnorm}(\text{r}_{(\text{g},\text{c})}^{\text{b}},\mspace{6mu}\text{mean}\mspace{310mu} = \mspace{310mu}\text{mean}{(\text{r}_\text{c}^{\text{b}})},\mspace{6mu}\text{sd}\mspace{310mu} = \mspace{310mu}\text{sd}{(\text{r}_\text{c}^{\text{b}})}) \leq 0.01$$

    4.  Remove the outlier genes detected in step iii and refit the curve as in step ii.

    5.  Detect outlier genes as in step iii based on the refitted curve in step iv.

    6.  Remove the outlier genes detected in step v and refit the curve as in step ii.

    7.  Output the curve from step vi.

1.  Calculate the expected entropy-expression curve by averaging the 10 curves from the subsampling runs. Specifically, for each gene $g$ , its expected entropy is the average of the 10 fitted entropy values.

Finally, the *entropy divergence* of $g$ in cell cluster $c$ is defined as

$${\Delta E}_{g,c} = {\hat{E}}_{g,c} - E_{g,c^{,}}$$

where ${\hat{E}}_{g,c}$ is the expected entropy of gene $g$ in cell cluster $c$, calculated based on gene $g$’s average expression and the expected entropy-expression curve in cell cluster $c$. Since we expect that gene $g$’s ambient RNAs would deflate its entropy $E_{g,c}$, a large and positive ${\Delta E}_{g,c}$ would indicate severe contamination of gene $g$ in cell cluster $c$.

### GCG identification in scCDC {#Sec14}

Small cell clusters (with fewer than 100 cells) are not considered in this GCG identification step. Figure 2B illustrates the GCG identification procedures described below.

1\. Among the considered cell clusters, in every cluster $c$, the genes with “significantly” large entropy divergences would be identified as the *candidate GCGs* of cluster $c$. Specifically, we fit a normal distribution of all genes’ entropy divergences ${\Delta E}_{g,c}$’s, denoted by the vector ${\Delta E}_{c}$. Then we calculate a pseudo-*p*-value of gene $g$, denoted by $pp_{g}$, as

$pp_{g} = 1 -$ pnorm(${\Delta E}_{g,c}$, mean = mean(${\Delta E}_{c}$), sd = sd(${\Delta E}_{c}$)), and set a 0.05 threshold on the adjusted pseudo-*p*-values based on the Benjamini–Hochberg procedure. That is, any gene $g$ whose post-adjustment $pp_{g} \leq 0.05$ would be called a candidate GCG in cluster $c$, if gene $g$ is expressed in at least 80% of the cells in cluster $c$.

2\. Across the considered cell clusters, the genes found as candidate GCGs in at least 50% (referred to as the *restriction factor*, which can be user-specified; the selection of an appropriate restriction factor is discussed in the Method Appendix) of the clusters and have non-zero counts in at least 20% cells in each cell cluster would be found as the *GCGs*. In other words, the GCGs are the genes that are stably found as candidate GCGs in many clusters.

### Estimation of a GCG’s contaminative count distribution in scCDC {#Sec15}

Each GCG’s contaminative count distribution is estimated by the GCG’s counts in the cells that are not expected to express the GCG endogenously (i.e., *eGCG − cells*; illustrated in Fig. 2B). To identify a GCG’s eGCG − cells, we take the following procedure. First, we filtered out cell clusters of less than 50 cells and identified the cluster in which the GCG has the lowest mean expression, calling this cluster an eGCG − cluster. Second, we use the GCG’s expression level as the only feature in a binary classification setting: distinguishing the eGCG − cluster from another cluster, so we can compute the area under the ROC curve (AUROC) to indicate the similarity of the other cluster to the eGCG − cluster (the larger the AUROC, the higher the similarity); the AUROC computation is done using the “pROC” (v1.17.0.1) package [51]. All clusters with AUROC values of less than 0.9 (a tuning parameter; see Table 2) are pooled with the eGCG − cluster and defined as the *eGCG − cells*. A GCG’s *eGCG* + *cells* are defined as the remaining cells, which are expected to have the GCG endogenously expressed.

Tuning parameters in the functions of scCDC

| Function | Parameter | Description | Default |
|----|----|----|----|
| Contamination detection | restrict\_factor | The minimum proportion of cell clusters in which a GCG is found as a candidate GCG | 0.5 |
|  | min.cells | The minimum cell number of the cell clusters used for finding candidate GCGs | 100 |
| Contamination correction | auc\_thres | The threshold of the AUROC used to define eGCG − clusters | 0.9 |
|  | min.cell | The threshold to filter the cell populations with an insufficient number of cells | 50 |

### Contamination ratio of a GCG by scCDC {#Sec16}

The contamination ratio $(C)$ of gene $g$ is calculated by the total UMI count of gene $g$ in eGCG − cells divided by the total UMI count of all genes in eGCG − cells:

$$R_{g} = \frac{\sum_{j \in N_{g}}X_{g,j}}{\sum_{g' \in G}\sum_{j \in N_{g}}X_{g',j}}$$

where $X_{g,j}$ represents the observed UMI count of gene $g$ in cell $j$, $N_{g}$ represents the eGCG − cells of gene $g$, and $G$ represents all genes in the data.

### Correction of a GCG’s contaminative counts by scCDC {#Sec17}

Given a GCG, scCDC uses the Youden index-based method to find a threshold $c$ so that the GCG’s contaminative counts in all cells would be corrected by subtracting $c$. To find $c$, we generate the ROC curve for classifying the eGCG − cells (class 0) and the least eGCG + cells (the eGCG + cell cluster in which the GCG has the lowest AUROC value against the GCG − cluster with the lowest expression of GCG). Based on the ROC curve, we calculate the Youden Index $(J)$ [52] of a given threshold $c$:

$$J_{c} = \mathit{Se}_{c} + \mathit{Sp}_{c} - 1,$$

where $\mathit{Se}_{c}$ is the sensitivity at the threshold $c$, and $\mathit{Sp}_{c}$ is the specificity at the threshold $c$. Then we find the threshold $c$ by maximizing $J_{c}$. Given the threshold $c$, we correct the GCG’s count in every cell by subtracting $c$, with a truncation at zero so that the GCG would not have negative counts.

In summary, scCDC has four tuning parameters listed in Table 2.

### Count correction by SoupX, DecontX, CellBender and scAR {#Sec18}

SoupX (v1.5.2), DecontX in Celda (v1.10.0), CellBender (v0.3.0), and scAR (v0.4.3) were employed for count correction.

For SoupX, both the raw feature matrix and filtered feature matrix generated by Cellranger (v6.0.1) are used to create the Soup Channel object, followed by the standard correction workflow in the tutorial [5]. The “automated” and “manual” modes are applied, respectively. The identified GCGs are provided as the “non-expressed genes,” whose RNAs in specified cells are treated as ambient, in the “manual” mode.

For DecontX, the correction is applied to the filtered feature matrix. The default procedure, referred to as the “default” mode, is performed. Alternatively, the pre-clustering information obtained from Seurat [53] is provided manually in the “pre-clustered” mode.

For CellBender, the correction uses the raw feature matrix with the remove-background function, following the tutorial ().

For scAR, both the raw feature matrix and filtered feature matrix are used based on the tutorial (). The filtering scale is applied to the filtered feature matrix for each of the datasets, as listed in Additional file 7: Table S6.

### Generation of simulated single-cell datasets {#Sec19}

To generate the simulated PBMC single-cell dataset, we first obtained a real PBMC dataset “pbmcsca.SeuratData” from the SeuratData R package (). We then sub-selected the dataset generated by the 10 × Chromium (v2) technology under the experiment “pbmc2,” using the “meta. data” information from “pbmcsca.SeuratData.” Next, we filtered out the ERCC spike-in’s, the mitochondrial genes, and the gene *MALAT1*, and we select five cell types (B cells, CD14 + monocytes, natural killer cells, CD4 + T cells, and cytotoxic T cells). Using the filtered and sub-selected real dataset from above, we applied the simulator scDesign2 [34, 54] to fit one multivariate probabilistic model to each of the five cell types.

The resulting gene expression matrix is stored as the file sce\_10x\_pbmc2\_hca\_corrected.rds.

The sce\_10x\_pbmc2\_hca\_corrected.rds file and the code for reproducing it are available at . In particular, the rds file is under Code summary.zip/Fig. 7 and supplementary S3 to S10/imputation\_comparison\_0614/Data\_gen/data/; the code is under Code summary.zip/Data simulation/. The rds file can be generated by sequentially executing the seven steps in the code directory.

To generate the simulated pancreas data with discrete cell types, we first obtained a real pancreas dataset based on the procedures in the “General single-cell and single-nuclei data processing” section. We selected four major cell types (Alpha, Beta, Gamma, and Delta cells) and sequentially filtered out non-Beta cells whose both *Ins1* and *Ins2*’s count expression is below 1, non-Alpha cells whose *Gcg*’s count expression is below 1, and non-Delta cells whose *Sst*’s count expression is below 1 to obtain a dataset with unambiguous cell clusters. Using this filtered real dataset, we then applied the scDesign2 [34, 54] to fit one multivariate probabilistic model to each of the four cell types.

To generate the simulated pancreas data that follow a continuous trajectory, we first obtained a real pancreas dataset from scDesign3’s [38] Zenodo repository (). The data file is PANCREAS\_sce.rds, a preprocessed and filtered dataset of pancreatic endocrinogenesis from scVelo [55]. It contains the top 1000 highly variable genes and four cell types that form a single trajectory, as well as the Slingshot [56] inferred cell pseudotime values, which are further normalized into the interval [0, 1]. We then applied scDesign3 [35] to fit one multivariate probabilistic model for all the cells using the pseudotime values as the cell covariates. Finally, we generated the simulated dataset using the scDesign3 fitted model with cell pseudotime values uniformly distributed in [0, 1].

### Artificial contamination of simulated single-cell datasets {#Sec20}

To simulate a contaminated PBMC dataset, we blended the simulated uncontaminated count matrix with artificial contaminative counts of three marker genes of CD14 + monocytes, *S100A9*, *S100A8*, and *LYZ*. In Additional file 1: Fig. S4A, the artificial contaminative counts of each gene were generated following a NB distribution, whose mean was the gene’s average original count and whose size was 10. Alternatively in Additional file 1: Fig. S4A, B, the three genes’ artificial contaminative counts were generated from a NB distribution with a fixed mean (0.5, 1, 1.5, 2, 2.5, or 3, indicating the contamination level) and a size of 1, 10, 50, or 100. Then for each of the three genes, we added to each of its original counts an artificial contaminative count, which was randomly picked from the generated ones.

We also generated a contaminated pancreas dataset by generating artificial contaminative counts of top 500 contaminating genes, which had the largest total counts in the empty droplets of the real pancreas dataset [6]. Specifically, we used the average count of *Ins2* in non-Beta cells, in which *Ins2* should not be expressed, as the baseline contamination level. Then for each of the 500 contaminating genes, we calculate its contamination level by multiplying the baseline contaminative level with the ratio of (the gene’s total count in the empty droplets)/(*Ins2*’s total count in the empty droplets). Finally, corresponding to the low, medium, or high contamination, each contaminating gene’s contaminative counts were sampled from a NB distribution, whose mean was 0.3, 1, or 3 times the gene’s contamination level and whose size was 10.

An additional contaminated pancreas trajectory dataset is generated by randomly blending the original raw count matrix with an artificial contaminative count matrix composed of four marker genes of Beta cells, *Ins1*, *Ins2*, *Iapp*, and *Nnat*. The contaminative count matrix is generated following NB distributions using the mean of the average count of the original raw count matrix and a size of 30. Then a contaminative count is randomly selected from the matrix and added to each original raw count.

### Single-nuclei RNA-seq of mammary glands {#Sec21}

Eight-week-old female C57BL/6N mice were timed mated. Abdominal and thoracic mammary tissues from nulliparous mice (virgin) and mice at lactation day 5 (L5) were harvested and lymph nodes in abdominal mammary tissues were removed. Mammary tissues were snap-frozen in liquid nitrogen followed by nuclei extraction and single-nuclei RNA sequencing (snRNA-seq) on a 10X Genomics platform in Lianchuan Biology Technology Co.

### General single-cell and single-nuclei data processing {#Sec22}

Cellranger (v6.0.1) was used to map raw reads to mouse or human reference genomes and obtain raw and filtered count matrixes of genes. Seurat (v4.0.3) was used for data filtration, principal component analysis (PCA), dimension reduction, clustering, marker gene identification, and data visualization. Specifically, for each dataset, cells with insufficient genes, molecules, and high mitochondria gene percentage were first filtered. The data were then normalized, and top variable genes were identified. Scaling, dimension reduction, and clustering were then performed. The specific parameters for filtering, dimension reduction, and clustering used in each dataset are provided in Additional file 7: Table S6.

When benchmarking for pre-clustering, the top 1000 variable genes identified by SeuratVST [53], scPNMF (v1.0) [57], and Scater (v1.20.1) [58] were used for dimension reduction, respectively.

Visualization of clusters and identification of marker genes was done in Seurat. Weighted gene co-expression network analysis (WGCNA) was done using the scWGCNA (v1.0.0) package [37].

## Supplementary Information {#Sec25}

Supplementary Material 1. Supplementary figures and Methods Appendix. This file contains the supplemental figures in the manuscript. In addition, a Methods Appendix is provided to assist users to understand the default setting of scCDC.

Supplementary Material 2: Supplementary Table 1. Summary of analyzed scRNA-seq and snRNA-seq datasets in this study.

Supplementary Material 3: Supplementary Table 2. Summary of scCDC correction results in the analyzed datasets.

Supplementary Material 4: Supplementary Table 3. Summary of under- and over-correction by different methods in the analyzed sn- and scRNAseq datasets.

Supplementary Material 5: Supplementary Table 4. Identified GCGs and clustering ARI after iterative runs in simulated, mammary gland and PBMC datasets.

Supplementary Material 6: Supplementary Table 5. Gene network modules identified by WGCNA before and after scCDC correction in pancreas and mammary gland datasets.

Supplementary Material 7: Supplementary Table 6. Summary of parameters used in the analysis of different datasets.

Supplementary Material 8. Review history.

## Acknowledgements {#ack1}

The authors would like to thank the suggestions from Prof. Kuan Yoow Chan and the support from the animal facility of ZJU-UoE Institute of Zhejiang University.

### Review history {#FPar1}

The review history is available as Additional File 8.

### Peer review information {#FPar2}

Anahita Bishop and Veronique van den Berghe were the primary editors of this article and managed its editorial process and peer review in collaboration with the rest of the editorial team.

## Authors’ contributions {#notes1}

W.C. conceived and designed the project. W.W., C.Y., and L.Z. developed the scCDC pipeline and performed data analysis. W.C., W.W., C.Y., and L.Z. wrote the manuscript. W.C. and L.J.J. supervised the project and edited the manuscript. Xu Y. conducted the snRNA-seq experiment in the mammary gland and analyzed the data. S.T. generated the simulated dataset. Xiao Y. and L.W. edited the manuscript.

## Funding {#notes2}

This work was funded by the National Key R&D Program of China (2021YFA1101100) and the National Natural Science Foundation of China (32370872, 31970776).

---

[← Discussion](03-discussion.md) · [Up: contents](index.md) · [Availability of data and materials →](05-availability-of-data-and-materials.md)
