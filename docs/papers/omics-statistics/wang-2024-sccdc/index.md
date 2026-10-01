---
title: "Wang et al. 2024 — scCDC: a computational method for gene-specific contamination detection and correction in single-cell and single-nucleus RNA-seq data"
paper: "summary"
source: "https://doi.org/10.1186/s13059-024-03284-w"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Wang, W., Cen, Y., Lu, Z., Xu, Y., Sun, T., Xiao, Y., Liu, W., Li, J.J., & Wang, C. (2024). scCDC: a computational method for gene-specific contamination detection and correction in single-cell and single-nucleus RNA-seq data. Genome Biology, 25, 136. https://doi.org/10.1186/s13059-024-03284-w ([original](https://doi.org/10.1186/s13059-024-03284-w)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# scCDC: a computational method for gene-specific contamination detection and correction in single-cell and single-nucleus RNA-seq data

**[Read the full text](full-text/index.md)**

## What this covers

A computational method, scCDC, for finding and correcting ambient-RNA contamination gene by gene
in droplet-based single-cell and single-nucleus RNA-seq data, for the field of scRNA-seq quality
control and preprocessing.

## The question

In droplet-based scRNA-seq and snRNA-seq, RNA leaked from lysed or ruptured cells floats free in
the suspension ("ambient RNA") and gets co-encapsulated with unrelated cells, inflating their
apparent expression of genes that are not really theirs. Existing correction tools (DecontX, SoupX,
CellBender, scAR) all estimate a global contamination profile and subtract it from every gene in
every cell. The authors ran into the problem directly while generating snRNA-seq data from mouse
mammary glands: markers expected to be restricted to one cell type — milk-protein genes such as
*Wap* and *Csn2* in differentiated alveolar cells, adipocyte genes such as *Acaca* and *Ghr* — were
turning up at low levels in almost every cell type. Applying the four existing tools revealed two
opposite failure modes: DecontX, CellBender, and SoupX's automated mode left the heavily
contaminated markers barely corrected, while SoupX's manual mode and scAR stripped real signal from
housekeeping and lowly expressed genes that were not contamination sources. No prior evaluation had asked whether correction strength should match how contaminated a given
gene actually is, and three of the four tools also require empty-droplet barcodes, routinely
discarded before data are shared publicly.

## The approach

Examining empty droplets across several datasets, the authors found ambient RNA is not spread
evenly across the transcriptome but dominated by a small set of "super-contaminating" genes (milk-
protein genes in lactating mammary gland, insulin genes in pancreas). This motivated a gene-specific
strategy: identify which particular genes cause contamination, and correct only those.

scCDC runs in two stages on data already clustered into cell types. Detection: for each gene in
each cluster, it compares the observed entropy of the gene's count distribution to an expected
entropy predicted from a curve fitted across genes assumed non-contaminating. Ambient RNA counts
are abundant but low-variance, so contamination suppresses observed entropy below expectation; this
gap is the "entropy divergence." A gene whose divergence is significant in more than a tunable
fraction of clusters (default 50%, the "restriction factor") is a "global contamination-causing
gene" (GCG). Correction: for each GCG, clusters where it is not really expressed are pooled as a
baseline, and a Youden-index threshold sets how many counts to subtract where it is genuinely
expressed. A "contamination ratio" — its share of total UMI counts in the non-expressing clusters —
quantifies how contaminated it is. Working from the cell-containing droplets themselves, scCDC
needs no empty-droplet data, unlike SoupX, CellBender and scAR.

## What it found

On simulated PBMC data with three artificially contaminated genes, scCDC correctly flagged all
three, with contamination-ratio estimates tracking the true contamination level. Across the
authors' own mammary gland datasets and thirteen public scRNA-seq/snRNA-seq datasets, scCDC
identified GCGs (72 and 106 in the lactating and virgin mammary gland datasets) that were mostly
known cell-type markers, matched the top contaminants found directly in empty droplets, and were
confirmed as highly expressed by bulk RNA-seq; it also recovered previously reported contaminants
elsewhere, including *Ins1*/*Ins2* in pancreas, *LYZ* in a PBMC dataset, and cross-species reads in
the mixed human/mouse "barnyard" benchmark.

Comparing correction across eight datasets with empty-droplet data retained, DecontX, SoupX's
automated mode, and CellBender under-corrected the most heavily contaminated GCGs, while SoupX's
manual mode and scAR stripped counts from many of 66 tested housekeeping genes in more than 95% of
cells. scCDC corrected the GCGs without touching those housekeeping genes, a pattern that held in
real data, in a pancreas dataset with spike-in-based ground truth, and in synthetic data spanning
low, medium and high contamination. DecontX's under-correction tended to appear once a GCG's
contamination ratio exceeded roughly $3.16\times10^{-4}$; the authors recommend running scCDC
followed by DecontX together when a dataset mixes highly and lowly contaminating genes, since scCDC
can fail to flag some lowly contaminating ones. Downstream, correcting with scCDC let a
gene-co-expression network method recover lactation marker genes (*Wap*, *Csn2*, *Csn3*, *Glycam1*)
as a coherent alveolar-cell module, and recovered pancreatic islet markers (*Gcg*, *Sst*) as central
genes of their respective modules — associations invisible before correction.

## Limits and context

scCDC requires cells to already be clustered into types, a dependency it shares with DecontX but
not with SoupX, CellBender or scAR; the paper treats this as an open issue, noting only that known
cell-type identification did not appear much degraded by contamination in the datasets tested. The
method can miss lowly contaminating genes and leaves them uncorrected, which is why the authors
recommend scCDC plus DecontX in combination rather than claiming scCDC alone suffices. They argue
against relying on the widely used mixed-species "barnyard" dataset as a sole decontamination
benchmark, since its contamination level was the lowest of the fifteen datasets examined. None of
the five compared methods, including scCDC, fully zeroed out contaminating counts where a GCG should
not be expressed; a small residual remained in every case. DecontX's convergence behaviour may need
further tuning, the authors note, calling this speculation rather than a tested finding, and flag
single-cell proteomics as an untested future application.

## Citation

Wang, W., Cen, Y., Lu, Z., Xu, Y., Sun, T., Xiao, Y., Liu, W., Li, J.J., & Wang, C. (2024). scCDC: a
computational method for gene-specific contamination detection and correction in single-cell and
single-nucleus RNA-seq data. *Genome Biology*, 25, 136. https://doi.org/10.1186/s13059-024-03284-w

Open access (CC BY 4.0), available at the DOI above and via PubMed Central (PMC11112958).
