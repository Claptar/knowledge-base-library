---
title: "Ahlmann-Eltze & Huber 2021 — Transformation and Preprocessing of Single-Cell RNA-Seq Data"
paper: "summary"
source: "https://doi.org/10.1101/2021.06.24.449781"
licence: "CC BY-ND 4.0 — no adaptation permitted, not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Ahlmann-Eltze, C. and Huber, W. (2021). Transformation and Preprocessing of Single-Cell RNA-Seq Data. bioRxiv preprint, posted June 25, 2021. ([original](https://doi.org/10.1101/2021.06.24.449781)). Rights: CC BY-ND 4.0 — no adaptation permitted, not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Transformation and Preprocessing of Single-Cell RNA-Seq Data

## What this covers

Compares methods for pre-processing single-cell RNA-seq count tables — specifically, the
transformations applied so that a gene's variance no longer depends on its mean — a methods paper
in computational genomics and single-cell transcriptomics.

## The question

Single-cell RNA-seq counts are heteroskedastic: counts for highly expressed genes vary far more in
absolute terms than counts for lowly expressed ones, typically following something close to a
Gamma-Poisson (negative binomial) mean-variance relation. Most generic statistical and machine
learning methods — clustering, PCA, differential expression — implicitly assume roughly constant
variance, so an analyst normally transforms the counts first. Several such transformations are in
use, but it was unclear which to prefer, and the field held conflicting recommendations — notably
a dispute between Lause, Berens & Kobak (2021) and Hafemeister & Satija (2020) over how to set the
overdispersion parameter in one popular method (sctransform). The authors set out to put the main
families of transformation on a shared theoretical footing and test them against each other.

## The approach

Three conceptually different strategies are compared, all referenced to a Gamma-Poisson model of
the counts with mean $\mu$ and overdispersion $\alpha$ (variance $= \mu + \alpha\mu^2$):

- **Delta-method variance-stabilizing transformations**, non-linear functions of the raw count
  derived so that the transformed variance is roughly constant across the dynamic range. They give
  a closed form based on the inverse hyperbolic cosine, and show that the widely used shifted
  logarithm $\log(y+c)$ approximates it well once the pseudocount $c$ is matched to the
  overdispersion (roughly $c = 1/(4\alpha)$), rather than the conventional fixed choice of $c=1$.
- **Model residuals**, following Hafemeister & Satija's sctransform: a per-gene Gamma-Poisson
  regression is fit against a cell-specific size factor, and the Pearson residuals from that fit
  are used as the transformed value. They also test randomized quantile residuals as a non-linear
  alternative to Pearson residuals.
- **Inferred latent expression state**, following Breda et al.'s Sanity: a Bayesian model that
  infers a posterior mean and standard deviation of each gene's true expression per cell, rather
  than stabilizing variance directly.

These were compared on simulated branching datasets (a linear interpolation manifold and a
random-walk manifold) using how well each transformation preserves each cell's true nearest
neighbours (recall of the 100 nearest neighbours), both alone and combined with PCA. They also
examined real data — droplets containing only a reference RNA solution, several immortalized cell
lines, and a published mouse lung atlas — to measure typical overdispersion and to see how each
transformation renders marker genes for known cell types.

## What it found

Measured overdispersion differed by context: around $\alpha \approx 0.006$–$0.015$ in technical
control droplets containing pure RNA solution, but higher, around $\alpha \approx 0.07$–$0.17$, in
ostensibly homogeneous immortalized cell line populations, reflecting genuine biological variation
(e.g., cell-cycle stage) rather than measurement noise. Whether the overdispersion is fixed or
estimated per gene, and whether the size-factor coefficient is fixed or estimated, had much less
impact on the resulting residuals than which overdispersion value was chosen in the first place.
In the nearest-neighbour benchmark, the shifted-log transformation combined with PCA performed
among the best, essentially matching the theoretically motivated acosh-based transformation,
provided a suitable pseudocount and number of principal components were used — the right number of
PCA dimensions varied by dataset. Pearson residuals stabilized variance across genes but, being a
linear transform per gene, left heteroskedasticity within a gene across cells, which showed up as
failure to flatten the expression distribution of marker genes across cell types and is a concern
for tasks that compare a gene across cells (clustering, differential expression, visualization).
Sanity's inferred latent state performed well on the nearest-neighbour benchmark and needs no
tunable parameter, but its runtime scaled quadratically with the number of cells, measured at
1,000-10,000 times slower than the other transformations.

## Limits and context

The paper directly contests Lause et al.'s (2021) conclusion that Pearson residuals outperform
alternative transformations: the authors argue this result depended on the particular benchmark
dataset and summary statistic used (an average F1 score sensitive to performance on one rare cell
type), and that on their own benchmark, using all genes rather than a highly-variable subset, a
square-root/shifted-log-type transformation did at least as well by other metrics such as overall
accuracy. They do not claim a single overdispersion value or transformation is universally correct
— which is appropriate depends on the biological question and the reference frame (technical
replicate versus biological replicate) adopted for estimating overdispersion. They are explicit
that the entire two-step workflow they evaluate — normalize, transform, then apply a generic
statistical method — has, in their view, "fundamental limitations," and argue that future gains
are more likely to come from models that integrate the measurement's sampling process directly
with the biological signal of interest than from further refinement of variance-stabilizing
transformations.

## Citation

Ahlmann-Eltze, C. and Huber, W. (2021). Transformation and Preprocessing of Single-Cell RNA-Seq
Data. bioRxiv preprint, posted June 25, 2021. https://doi.org/10.1101/2021.06.24.449781
