---
title: "Young & Behjati 2020 — SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data"
paper: "summary"
source: "https://doi.org/10.1093/gigascience/giaa151"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Young MD, Behjati S. SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data. GigaScience. 2020;9(12):giaa151. https://doi.org/10.1093/gigascience/giaa151 ([original](https://doi.org/10.1093/gigascience/giaa151)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data

**[Read the full text](full-text/index.md)**

## What this covers

A method paper in computational genomics: how to detect and remove "ambient RNA" contamination —
cell-free mRNA from the surrounding solution that gets sequenced alongside a cell's own transcripts
in droplet-based single-cell RNA-seq — and a tool, SoupX, that does it.

## The question

Droplet scRNA-seq (10X Chromium, Drop-seq, etc.) assumes each droplet's counts come from one
captured cell. In practice every droplet also picks up free-floating mRNA already present in the
cell suspension — lysed cells, secreted transcripts — so the observed counts are a mixture of
genuine cellular expression and this "soup." The authors set out to show that this contamination is
not a rare artefact but a pervasive, experiment-specific background, and that it can be large enough
to distort the biological conclusions drawn from the data: a cell can appear to express a gene it
never transcribed. The question was how to quantify and strip out that background without needing
specialised experimental controls, so that any existing dataset could be corrected before standard
downstream analysis.

## The approach

SoupX works in three steps. First, it estimates the ambient expression profile directly from
droplets with very few UMIs, which are assumed to contain no cell and so represent pure soup.
Second, it estimates a contamination fraction for each cell (or channel): the proportion of that
cell's UMIs attributable to the background rather than to its own transcription. This is the hard
step, and it rests on finding genes/cells where true expression can be assumed to be zero — for
example, haemoglobin genes in non-erythroid cells, or marker genes of one cluster in cells belonging
to other clusters — so that any counts for that gene in that cell must be contamination. Where such
a gene set isn't known in advance, SoupX offers an automated procedure that uses many cluster marker
genes to independently estimate the contamination fraction and takes the most consistent
(most frequent) value as the true one, reasoning that wrong estimates scatter while correct ones
agree. Third, given the background profile and the contamination fraction, it subtracts the
estimated background contribution gene-by-gene from each cell's observed counts (estimated via a
multinomial likelihood rather than simple subtraction, to cope with sparse counts), producing a
corrected count matrix that can be dropped into any standard downstream pipeline unchanged.

The method was validated using "species-mixing" experiments (human and mouse cells run together),
where any mouse transcript appearing in a human cell's droplet is unambiguous contamination,
providing ground truth against which to check the estimates.

## What it found

Contamination was present in every dataset examined. In the species-mixing controls, roughly 1% of
transcripts in a droplet were cross-species contamination at minimum, with the true total
contamination (including same-species background) around 6% in the PBMC dataset tested; applying
SoupX reduced cross-species (false) signal by a factor of 2 to an order of magnitude while leaving
correct-species expression essentially unchanged. The background profile closely tracked the
average expression profile across all cells in a channel (Pearson correlation 0.71-0.96 across
datasets, median 0.86), supporting the assumption that contamination is roughly a uniform sample of
the cell population rather than coming from one source. Contamination fraction was fairly constant
across cells within a channel but varied substantially between experiments, consistent with it
being a property of sample preparation rather than of individual cells.

Applying correction changed biological interpretation in concrete ways: in PBMC data it sharpened
marker gene specificity and revealed additional markers not detected in uncorrected data; in a
kidney tumour dataset it removed apparent collagen-gene expression from immune cell clusters that
would otherwise have suggested (incorrectly) that those cells were tissue-resident, and it increased
cross-sample mixing entropy, indicating that some of the apparent batch effect was actually
background contamination; in fetal liver data it resolved cells that appeared, before correction, to
co-express erythroid and non-erythroid markers in a way that looked like multiplets but was in fact
ambient contamination.

## Limits and context

The method assumes a single, roughly constant contamination fraction per cell or channel; it does
not model contamination that varies gene-by-gene within a cell in ways unrelated to overall
background abundance. The authors note that distinguishing contamination from genuine unexpected
expression still requires judgement — they give an example (GYPA expression in a macrophage
population) where SoupX's output supported treating the signal as genuine rather than contamination,
but this depended on the user interpreting the estimate, not on the algorithm deciding automatically.
Accurate correction is easiest when the user can supply biologically justified genes/cells known to
have zero true expression; the automated alternative is offered for when this isn't available but is
presented as a fallback, not the preferred route. The paper distinguishes SoupX from contemporaneous
alternatives it discusses (SoupOrCell, CellBender, DecontX), arguing those either require
mixed-genotype designs, carry a heavier computational cost and change the output format, or depend
more heavily on clustering accuracy — but it reports no head-to-head quantitative benchmark against
them in this paper.

## Citation

Young MD, Behjati S. "SoupX removes ambient RNA contamination from droplet-based single-cell RNA
sequencing data." *GigaScience*, 9(12):giaa151, 2020. https://doi.org/10.1093/gigascience/giaa151.
Open access (CC BY 4.0); code at https://github.com/constantAmateur/SoupX.
