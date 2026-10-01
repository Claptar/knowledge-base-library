---
title: "Yang et al. 2020 — Decontamination of ambient RNA in single-cell RNA-seq with DecontX"
paper: "summary"
source: "https://doi.org/10.1186/s13059-020-1950-6"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Yang S, Corbett SE, Koga Y, Wang Z, Johnson WE, Yajima M, Campbell JD. Decontamination of ambient RNA in single-cell RNA-seq with DecontX. Genome Biology. 2020;21:57. https://doi.org/10.1186/s13059-020-1950-6 ([original](https://doi.org/10.1186/s13059-020-1950-6)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# Decontamination of ambient RNA in single-cell RNA-seq with DecontX

**[Read the full text](full-text/index.md)**

## What this covers

A statistical method for a nuts-and-bolts problem in single-cell RNA sequencing: separating a
cell's genuine transcripts from contaminating "ambient RNA" that leaked in from other cells during
library preparation. It speaks to computational methods for droplet-based scRNA-seq quality control.

## The question

In droplet-based scRNA-seq (10X Chromium, Drop-seq, and similar platforms), cells are lysed inside
tiny droplets along with barcoded beads, but the cell suspension also contains free-floating mRNA
released by dying or stressed cells before encapsulation. This "ambient RNA" gets captured,
barcoded, and sequenced alongside a cell's own transcripts, so every droplet's count matrix is
really a mixture of native and foreign reads. The practical symptom is that a gene that is a sharp
marker for one cell type turns up, at low level, in cells that should never express it — which
blurs clustering and makes marker genes look less specific than they are. Existing computational
tools at the time addressed a related but distinct artifact, doublets (two cells captured in one
droplet), and did not tackle cross-contamination from ambient RNA at all. The authors wanted a way
to estimate, per cell, how much of its observed counts are contamination, and to strip that
contamination out before downstream analysis.

## The approach

DecontX models each cell's observed transcript counts as a mixture of two multinomial
distributions over genes: one is the "native" expression profile of the cell's own population, the
other is a "contamination" profile built from the expression profiles of all the other populations
in the dataset, weighted by how much each population contributes to the ambient pool. A per-cell
parameter (drawn from a shared beta distribution across the dataset) sets what fraction of that
cell's transcripts are native versus contaminating, and each individual transcript carries a hidden
label for which of the two distributions it came from. This construction is structurally close to
latent Dirichlet allocation, except that instead of K independent topic distributions, the
contamination distribution for each population is explicitly tied to the expression of every other
population. Fitting is done with variational inference rather than full MCMC sampling, which the
authors chose for speed and scalability to the tens of thousands of cells typical of modern
datasets. The method needs cell population labels as an input; the authors used existing cluster
assignments (flow-sorted labels, or genome-of-origin in the mixture experiment) where available,
and their own earlier clustering tool, Celda, to generate labels when none existed.

## What it found

On a public human-mouse cell mixture dataset, where the "true" contamination level can be checked
against reads that align uniquely to the wrong species' genome, DecontX's per-cell contamination
estimates correlated strongly with the known exogenous-transcript proportion ($R = 0.99$ in both
human and mouse cells, with low RMSE), and it removed most of the cross-species reads after
decontamination. Contamination levels varied widely cell to cell (roughly 0.4-45%) even though the
median was low (around 1-3%), supporting the case for per-cell rather than per-dataset correction.
On a 4,000-cell PBMC dataset, decontamination eliminated most aberrant expression of T cell and B
cell marker genes in the wrong cell population, improved cluster separation in t-SNE, and raised
the mean silhouette width from 0.04 to 0.07. Cells that DecontX flagged as highly contaminated
(over 70%) were consistently also flagged as doublets by an independent method (Scrublet),
suggesting DecontX estimates double as orthogonal evidence for doublet detection. Applied across
four scRNA-seq protocols on matched cell-line benchmark data, 10X Chromium showed the lowest median
contamination and CEL-seq2 the highest, with Drop-seq and SORT-seq in between; newer 10X chemistry
(V3) showed lower contamination than the older V2 chemistry across three tissue types, and PBMCs
showed more than twice the contamination of brain or heart cells.

## Limits and context

The authors note DecontX does not always fully remove aberrant marker expression: in the PBMC
dataset, 43% of NK cells retained some T cell marker signal, which they attribute partly to
possible true NKT cells in the mixture and partly to the method's deliberately conservative
behavior when two populations' expression profiles overlap substantially — it is built to avoid
stripping out genuine biological similarity between cell types, at the cost of leaving some
contamination uncorrected. The method depends on having cell population labels in advance, which
the authors treat as a limitation rather than an afterthought; a clustering tool can supply labels
when none exist, but results can be sensitive to how finely populations are split, and the paper
suggests that broader groupings (e.g., all T cell subtypes together) can help in some cases. The
paper does not benchmark against other contamination-specific methods, since it frames DecontX as
addressing a gap left by the available doublet-detection tools rather than competing with a direct
alternative.

## Citation

Yang S, Corbett SE, Koga Y, Wang Z, Johnson WE, Yajima M, Campbell JD. Decontamination of ambient
RNA in single-cell RNA-seq with DecontX. *Genome Biology*. 2020;21:57.
DOI: https://doi.org/10.1186/s13059-020-1950-6. Open access, CC BY 4.0;
available from Genome Biology and PubMed Central (PMC7059395).
