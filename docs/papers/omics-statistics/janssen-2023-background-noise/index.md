---
title: "Janssen et al. 2023 — The effect of background noise and its removal on the analysis of single-cell expression data"
paper: "summary"
source: "https://doi.org/10.1186/s13059-023-02978-x"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Janssen P, Kliesmete Z, Vieth B, Adiconis X, Simmons S, Marshall J, McCabe C, Heyn H, Levin JZ, Enard W, Hellmann I. The effect of background noise and its removal on the analysis of single-cell expression data. Genome Biology. 2023;24:140. https://doi.org/10.1186/s13059-023-02978-x ([original](https://doi.org/10.1186/s13059-023-02978-x)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# The effect of background noise and its removal on the analysis of single-cell expression data

**[Read the full text](full-text/index.md)**

## What this covers

A benchmarking study in single-cell genomics: how much of the signal in droplet-based scRNA-seq and
snRNA-seq data is "background noise" from sources other than the cell a barcode is supposed to
represent, where that noise comes from, and how well three widely used correction tools
(CellBender, DecontX, SoupX) remove it.

## The question

Reads tagged with a cell's barcode are not all transcripts from that cell: some come from cell-free
"ambient" RNA floating in the suspension, and some from chimeric molecules created by barcode
swapping during library preparation. This contamination blurs cell-type clusters, creates spurious
marker-gene combinations that look like new cell types, and can confound differential expression
between conditions. Several correction tools already existed, but they had been validated mainly on
a mix of human and mouse cell lines, or on marker genes assumed to be strictly on/off in one cell
type. In both cases the contaminating reads land on genes the real cell could never express, which
is an easy regime for a correction method and not representative of ordinary data, where background
mostly nudges expression levels rather than switching genes fully on or off. The authors wanted a
more realistic ground truth — a complex, multi-cell-type sample where contamination shares the same
genes as the real signal — to measure the extent and source of background noise and to judge how
well existing tools actually perform.

## The approach

The authors pooled kidney cells from three inbred mouse strains belonging to two subspecies (*Mus
musculus domesticus* and *M. m. castaneus*) into single 10x Genomics runs, producing three scRNA-seq
and two snRNA-seq replicates. Because the strains carry known homozygous SNPs, every read can be
assigned to its true genotype of origin, so any read in a *castaneus* cell carrying a *domesticus*
allele is unambiguous cross-genotype contamination — on the very same genes used for real
expression, across thirteen annotated kidney cell types. From the allele counts they derived a
per-cell maximum-likelihood estimate of total background-noise fraction (adapting a method from
Heaton et al.), and treated this genotype-based estimate as ground truth. They used it to compare
contamination profiles against profiles built from ambient RNA in empty droplets and from true
endogenous counts, to identify PCR-chimera events directly, and then to benchmark CellBender, DecontX
and SoupX on both their noise-level estimates and the downstream effects of applying each
correction — marker gene detection, cell classification, clustering, and local ("fine") structure via
k-nearest-neighbour overlap with a genotype-cleaned reference.

## What it found

Background noise made up on average 3–35% of UMI counts per cell, varying strongly between
replicates and cells and not tracking the overall success of the experiment: the snRNA-seq replicates
prepared from frozen tissue carried much more noise than scRNA-seq from the same samples (35% vs 11%,
and 17% vs 3%, in matched pairs). Noise was roughly constant in absolute amount per cell regardless
of cell size, so the noise *fraction* mainly reflected how much endogenous RNA a cell had — evidence
for ambient RNA rather than swapping as the dominant source. Contamination profiles correlated
strongly with empty-droplet profiles (Spearman's $\rho = 0.73$–$0.85$) and matched them in intronic
read content, while PCR chimeras, directly detected via repeated barcode–UMI combinations, accounted
for less than 10% of total background. Marker gene specificity degraded as background rose: a
proximal-tubule marker's log2-fold-change shrank and its detection rate in other cell types rose with
noisier replicates. Among the correction tools, CellBender gave the most accurate per-cell noise
estimates and the largest improvement in marker-gene detection (for example, cutting false-positive
detection of the marker gene *Slc34a1* in non-target cells to about 7%, versus 54% for SoupX and 9%
for DecontX using an empty-droplet background profile), though at a cost of far higher runtime (CPU
hours versus seconds to minutes for the others). Cell classification and clustering, by contrast,
proved fairly robust to background noise: correction relabelled only a small fraction of cells (up to
about 1.3% in the noisiest replicate) and improved broad cluster structure only modestly, sometimes
at the cost of distorting fine-grained neighbour structure, particularly with DecontX.

## Limits and context

The authors restrict their quantitative benchmarking of correction methods to four of the five
replicates, excluding one snRNA-seq replicate because its low cell-type diversity and cell count made
all three methods perform poorly and unreliably. They present the weak correlation between cell size
and absolute background counts as consistent with ambient RNA leaking in proportion to dropout rates
rather than as a fully settled mechanism, and they describe barcode swapping's contribution as
bounded above by their chimera-based estimate rather than precisely measured. Their practical
recommendation is correspondingly qualified: they advise using background removal routinely for
marker-gene analysis, but only when background levels are high for classification, clustering or
pseudotime analyses, since at low-to-moderate noise levels the correction's tightening of broad
structure can come at the expense of fine structure. The dataset and conclusions are drawn from one
tissue (mouse kidney) and are offered as a benchmark resource rather than a claim that the same noise
levels or method rankings generalize to all tissues or protocols.

## Citation

Janssen P, Kliesmete Z, Vieth B, Adiconis X, Simmons S, Marshall J, McCabe C, Heyn H, Levin JZ, Enard
W, Hellmann I. The effect of background noise and its removal on the analysis of single-cell
expression data. *Genome Biology*. 2023;24:140. https://doi.org/10.1186/s13059-023-02978-x. Open
access (CC BY 4.0) via Genome Biology / PubMed Central (PMC10278251).
