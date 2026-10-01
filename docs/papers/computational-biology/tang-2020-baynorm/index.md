---
title: "Tang et al. 2020 — bayNorm: Bayesian gene expression recovery, imputation and normalization for single-cell RNA-sequencing data"
paper: "summary"
source: "https://doi.org/10.1093/bioinformatics/btz726"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Tang, W., Bertaux, F., Thomas, P., Stefanelli, C., Saint, M., Marguerat, S., & Shahrezaei, V. (2020). bayNorm: Bayesian gene expression recovery, imputation and normalization for single-cell RNA-sequencing data. Bioinformatics, 36(4), 1174–1181. https://doi.org/10.1093/bioinformatics/btz726 ([original](https://doi.org/10.1093/bioinformatics/btz726)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# bayNorm: Bayesian gene expression recovery, imputation and normalization for single-cell RNA-sequencing data

**[Read the full text](full-text/index.md)**

## What this covers

How to turn raw single-cell RNA-sequencing (scRNA-seq) counts, which are dominated by technical
dropout and capture noise, into estimates of the true number of transcripts per gene per cell —
a problem at the intersection of computational biology and Bayesian statistics.

## The question

scRNA-seq only captures a small, cell-varying fraction of the RNA actually present in a cell, so
raw count matrices are sparse, noisy, and subject to batch-to-batch shifts in that capture
fraction. Existing methods treated normalization (removing cell-size/capture differences),
imputation (filling in dropouts) and batch correction as three separate problems, and several
relied on explicit zero-inflation models to explain dropouts. The authors wanted a single,
minimally-assumption approach that recovers true counts, handles dropouts, and corrects batch
effects together, and that could also be tested for whether dropout really needs a special
zero-inflation mechanism at all.

## The approach

bayNorm treats observed counts as a *Binomial* sample of the true transcript count for each gene
in each cell, with a cell-specific "capture efficiency" probability $\beta_j$ standing in for the
usual scaling factor. The true (unobserved) count is given a Negative Binomial prior, with
gene-specific mean and dispersion parameters estimated empirically by pooling expression values
across cells (an empirical Bayes approach), either across all cells ("global" priors) or within
defined cell groups/batches ("local" priors). Combining the Binomial likelihood with the Negative
Binomial prior gives, via Bayes' rule, a closed-form posterior distribution of the true count for
every gene/cell pair; the paper derives this posterior (itself a shifted Negative Binomial) and its
mean and variance analytically. The output is either point estimates (mean or MAP) of true counts,
or samples drawn from the full posterior, both usable in downstream analyses such as differential
expression (DE) testing and clustering. Choosing global versus local priors, and estimating the
mean capture efficiency $\bar\beta$, are the method's key tuning decisions.

## What it found

Simulated data generated from the binomial-capture assumption reproduced the mean-variance and
mean-dropout relationships, and the per-gene and per-cell dropout-rate distributions, of several
real UMI-based scRNA-seq datasets more closely than the existing Gamma-Poisson-based Splatter
simulator — support for treating dropout as a consequence of binomial sampling rather than
requiring a separate zero-inflation mechanism. A simple constant rescaling made the same binomial
model fit non-UMI data reasonably well too. Against datasets with matched single-molecule FISH
(smFISH) ground truth, bayNorm recovered mean expression as well as competing methods but matched
the FISH-measured noise (coefficient of variation) and dispersion (Gini coefficient) more closely
than scaling normalization or other recent imputation methods (scImpute, MAGIC, SAVER, DCA). In
differential expression benchmarks (using MAST, benchmarked against matched bulk RNA-seq DE gene
lists), bayNorm with local (group-specific) priors matched or exceeded other methods' sensitivity
(AUC), while with global priors it produced almost no spurious DE genes between groups selected
only by differing capture efficiency — demonstrating that it is specifically controlling for the
capture-efficiency bias rather than just performing well on average. Using within-individual local
priors across batches, bayNorm reduced batch-driven false-positive DE rates (tested on data with
three individuals x three batches each) while preserving true biological differences between
individuals, outperforming the global-prior and within-batch-prior alternatives on that trade-off.
Global priors preserved unsupervised cell-type clustering (by t-SNE/Jaccard index against scaling
normalization) about as well as scaling-based normalization. The method was also shown not to be
very sensitive to a 2-fold misestimate of mean capture efficiency.

## Limits and context

The prior assumes no correlation between genes, so bayNorm's gene-specific priors were shown to
underestimate gene-gene correlation on data with matched smFISH measurements (in the opposite
direction to SAVER's pooling-across-genes approach, which tended to overestimate it). Accurate
estimation of cell-specific capture efficiency remains central to the method and is not always
easy to obtain, since calibration approaches such as smFISH are uncommon and spike-in-based
estimates have known shortcomings; the paper found that neither spike-ins nor housekeeping-gene
estimates improved recovery of per-cell dropout statistics in its tests. Local-prior estimation
loses robustness when a comparison group has very few cells. The authors note that clustering
could potentially be improved further by iterating the prior estimation together with clustering,
as in the BISCUIT method, and suggest combining bayNorm's framework with deep-learning-based
approaches as future work rather than presenting that combination here.

## Citation

Tang, W., Bertaux, F., Thomas, P., Stefanelli, C., Saint, M., Marguerat, S., & Shahrezaei, V.
(2020). bayNorm: Bayesian gene expression recovery, imputation and normalization for single-cell
RNA-sequencing data. *Bioinformatics*, 36(4), 1174–1181. https://doi.org/10.1093/bioinformatics/btz726
