---
title: Background
source: https://doi.org/10.1186/s13059-020-1950-6/
source_file: sources/papers/yang-2020-decontx/yang-2020-decontx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `yang-2020-decontx.jats` from [papers/yang-2020-decontx](https://doi.org/10.1186/s13059-020-1950-6/) — papers · yang-2020-decontx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Background

Received 2019 Sep 30; Accepted 2020 Jan 29; Collection date 2020.

## Background {#Sec1}

Single-cell RNA sequencing (scRNA-seq) has emerged as a powerful technique to study complex biological systems at single-cell resolution [1]. Droplet-based scRNA-seq platforms have been widely adopted because of their ability to profile a large number of cells at relatively low cost [2]. These devices work by using droplets to partition cells into nanoliter reaction chambers along with beads harboring oligonucleotide primers with unique barcodes. Within each droplet, cells are lysed and the mRNAs will be tagged with the oligonucleortide primers to create barcoded cDNA after reverse transcription [3–5].

Despite their many advantages, droplet-based single-cell technologies can suffer from the presence of cross-contamination from ambient RNA in each droplet. Ambient RNA is the pool of mRNA molecules that have been released in the cell suspension, likely from cells that are stressed or have undergone apoptosis. Cross-contamination occurs when the ambient RNA gets incorporated into the droplets and is barcoded and amplified along with a cell’s native mRNA (Fig. 1a). Contamination from ambient RNA is evident when highly expressed cell type-specific genes are observed at low levels in other cell populations. Different proportions of contamination can be found in different droplets depending on the amount of ambient and native mRNA present. Two major goals of many scRNA-seq studies are to cluster cells into subpopulations and identify unique combinations of marker genes that define each cell population [6]. Ambient RNA can hinder these tasks by causing different cell populations to “blend” together and the expression of true marker genes to be detected across multiple cell populations. Beyond ambient RNA, other technical factors may cause contamination between cells such as evaporation in plate-based protocols [7, 8] or barcode swapping during sequencing [9].

![](https://doi.org/10.1186/s13059-020-1950-6/)

![](https://doi.org/10.1186/s13059-020-1950-6/)

Overview of decontamination with DecontX. **a** In droplet-based microfluidic devices, ambient RNA can be incorporated into droplets along with oligonucleotide-barcoded beads and cells. Both native mRNA from the cell and contaminating ambient RNA will be barcoded and counted within a droplet. **b** Left: DecontX assumes that each cell is a mixture of two multinomial distributions: (1) a distribution of native transcripts from the cell’s true population and (2) a distribution of contaminating transcripts from all other cell populations captured in the assay. Right: simulation of an example cell with 20% contamination. The 800 native transcripts are from the multinomial distribution for cell population 1 while the 200 contaminating transcripts are derived from a probability distribution that is a weighted combination of the 2 other populations. **c** DecontX will take an expression count matrix and cell cluster labels and estimate matrices of native expression and contamination from ambient RNA

Another common problem in scRNA-seq methods is when more than one cell is captured in a droplet, also known as a “doublet” or “multiplet.” In microfluidic systems, the occurrence of doublets is proportional to the concentration of cells in the suspension and capture rate of the device [10–13]. Several computational methods have been developed to detect doublets for scRNA-seq data. Scrublet [10] and DoubletFinder [11] simulate artificial doublets from the original data coordinates in a reduced-dimensional representation, then create doublet score for each barcode by calculating the similarity of its representation with artificial doublets. Other approaches such as demuxlet [12] and scds [13] model gene expression from the original data, then assign doublet to barcodes that have observed expression from genes that are likely to not occur simultaneously. While it is important to identify doublets in scRNA-seq, these approaches do not address the problem of contamination caused by ambient RNA or other experimental factors.

We developed a computational method called DecontX to estimate and remove ambient RNA for scRNA-seq data. We applied DecontX to three datasets to demonstrate its ability to accurately quantify and remove contamination within each cell from other populations and to improve downstream clustering. Applying DecontX to benchmark datasets containing the same cell lines sequenced across four different scRNA-seq methods, including two plate-based (CEL-seq2 and SORT-seq) and two droplet-based (10X Chromium and Drop-seq), generally showed that 10X Chromium had the lowest levels of contamination while CEL-seq2 had the highest. Highly contaminated cells also showed consistency with doublet predictions by Scrublet and demuxlet suggesting that this approach can also support doublet detection.

---

[Up: contents](index.md) · [Results →](02-results.md)
