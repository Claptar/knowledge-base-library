---
title: "Fleming et al. 2023 — Unsupervised removal of systematic background noise from droplet-based single-cell experiments using CellBender"
paper: "summary"
source: "https://doi.org/10.1038/s41592-023-01943-7"
licence: "CC BY-NC-ND preprint, closed journal version -- not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Fleming, S. J., Chaffin, M. D., Arduini, A., Akkad, A.-D., Banks, E., Marioni, J. C., Philippakis, A. A., Ellinor, P. T., & Babadi, M. (2023). Unsupervised removal of systematic background noise from droplet-based single-cell experiments using CellBender. Nature Methods, 20, 1323-1335. https://doi.org/10.1038/s41592-023-01943-7 ([original](https://doi.org/10.1038/s41592-023-01943-7)). Rights: CC BY-NC-ND preprint, closed journal version -- not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Unsupervised removal of systematic background noise from droplet-based single-cell experiments using CellBender

## What this covers
CellBender "remove-background": an unsupervised deep generative model that strips systematic
background noise out of droplet-based single-cell and single-nucleus omics data (scRNA-seq,
snRNA-seq, CITE-seq), for the single-cell genomics data-processing and quality-control literature.

## The question
Droplet-based assays never match the ideal of one cell, one droplet, zero noise elsewhere.
Cell-free droplets carry nonzero counts, and cell-containing droplets pick up off-target
transcripts from other cells, because of ambient RNA released by lysed or degraded cells (worse in
nuclear preps) and molecule/barcode "swapping" during PCR amplification and library prep. This
noise distorts marker-gene specificity, inflates batch effects, and can create spurious
differential expression, especially in single-nucleus data and in antibody-capture (CITE-seq) data
where background can dominate signal. Existing correction tools either need prior knowledge of
expected cell-type profiles or marker genes (SoupX) or model only part of the contamination process
(DecontX). The authors wanted a method needing no such priors, applicable to any droplet-based
molecular feature (RNA, protein, guide), that makes the sensitivity/specificity trade-off of
denoising an explicit, tunable choice.

## The approach
The model treats each droplet's observed counts as the sum of true cell-endogenous counts and noise
counts. Endogenous counts are negative-binomial draws whose rate depends on a per-cell
gene-expression profile; a neural network learns a flexible low-dimensional latent "cell state"
space shared across all cells instead of fixing that profile in advance, so weak droplets borrow
statistical strength from similar droplets elsewhere. Noise counts are Poisson, split into an
ambient component (a learned gene profile drawn from the cell-free "soup," scaled by
droplet-specific capture efficiency and size) and a barcode-swapping component tied to the
dataset-wide average expression. The whole model, including a per-droplet cell/empty indicator, is
fit end to end by stochastic variational inference with amortized (encoder) neural networks in
Pyro, with no marker genes, cell-type labels or expected ambient profile supplied as input. A
deliberate design choice separates this from autoencoder-style denoising: the learned
low-dimensional space serves only as a *prior* over cell states and is never decoded back into
output counts, so denoised counts can never exceed raw observed counts and collapse to the raw data
as inferred noise goes to zero. Converting the noise posterior into an integer denoised count
matrix is treated as a separate estimation problem, controlled by a user-set "nominal false
positive rate" (nFPR) that makes explicit how much real signal the user accepts losing for
specificity; the preferred estimator reduces this choice to a multiple-choice knapsack problem
solved fast and exactly under a log-concavity assumption.

## What it found
On simulated data with known ground truth, accuracy sits close to the theoretically optimal
denoising limit achievable with perfect knowledge of every latent variable, measured by ROC curves
over noise counts. On a public PBMC scRNA-seq dataset it sharply increases marker specificity:
genes such as S100A8, S100A9 and LYZ, previously found at low levels across most clusters, become
concentrated in the expected monocyte/neutrophil/pDC populations, with fold-changes for expected
markers roughly doubling while a uniformly-expressed control gene (PTPRC) is essentially untouched.
On a published human heart snRNA-seq atlas of nearly 600,000 nuclei, the model attributes much of
the background to abundant cardiomyocyte transcripts (TTN, RYR2) leaking into other cell types and
removes it, sharpening cell-type-specific expression of fibroblast and mural markers (DCN, LAMA2,
CTNNA3). In a human-mouse mixed-species benchmark, it removes most cross-species off-target counts
— median per-droplet off-target count drops from 225 in raw data to about 19 at default settings —
and head-to-head ROC comparisons show it removes more genuine background at matched sensitivity
than DecontX (92.3% of true noise removed versus 80.9% for DecontX at the same true-positive rate,
in one comparison). On a rat heart snRNA-seq dataset, it calls substantially more legitimate cells
than CellRanger, dropkick and EmptyDrops, and the extra cells it uniquely identifies show coherent
marker expression, with over a quarter passing standard post hoc quality filters. Applied to
CITE-seq antibody-capture data, denoising increases correlation between RNA and protein
measurements of the same target and sharpens expected anti-correlated patterns, for example between
the CD45RA and CD45RO splice isoforms across T-cell subsets.

## Limits and context
The model needs to be reasonably well specified for the noise actually present in a dataset, and
very low signal-to-noise separation between empty and cell-containing droplets can leave the
deconvolution problem ill-posed; the authors recommend checking convergence against prior
experimental expectations rather than trusting the fit blindly. Identifying empty versus non-empty
droplets is not a substitute for standard downstream cell-quality filtering (for example by
mitochondrial fraction or gene complexity) — such filters were deliberately left out to keep the
tool broadly applicable, and the authors recommend running them afterward. They argue against
relying on the two conventional Bayesian point estimators (the MAP estimate and the posterior mean)
to turn the noise posterior into an integer count matrix, showing both carry systematic biases
unsuited to controlling sensitivity against specificity, which motivates their nFPR-tunable
estimators instead. They also note background noise is only one contributor to batch effects;
variation in capture efficiency, sequencing depth and protocol differences remain separate sources
this method does not address. Directions flagged as open rather than resolved include modeling
noise at the level of individual sequencing reads rather than aggregated UMI counts, and evaluating
the approach on further single-cell modalities, including Perturb-seq guide assignment.

## Citation
Fleming, S. J., Chaffin, M. D., Arduini, A., Akkad, A.-D., Banks, E., Marioni, J. C., Philippakis,
A. A., Ellinor, P. T., & Babadi, M. (2023). Unsupervised removal of systematic background noise from
droplet-based single-cell experiments using CellBender. *Nature Methods*, 20, 1323-1335.
https://doi.org/10.1038/s41592-023-01943-7
