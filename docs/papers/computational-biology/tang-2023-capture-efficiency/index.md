---
title: "Tang et al. 2023 — Modelling capture efficiency of single-cell RNA-sequencing data improves inference of transcriptome-wide burst kinetics"
paper: "summary"
source: "https://doi.org/10.1093/bioinformatics/btad395"
licence: "CC BY 4.0"
written: "2026-10-02"
---

> **Paper.** Tang W, Jørgensen ACS, Marguerat S, Thomas P, Shahrezaei V. Modelling capture efficiency of single-cell RNA-sequencing data improves inference of transcriptome-wide burst kinetics. Bioinformatics. 2023;39(7):btad395. ([original](https://doi.org/10.1093/bioinformatics/btad395)), licensed CC BY 4.0. Below is a short summary in our own words; the [full text](full-text/index.md) is reproduced under the paper's licence.

# Modelling capture efficiency of single-cell RNA-sequencing data improves inference of transcriptome-wide burst kinetics

**[Read the full text](full-text/index.md)**

## What this covers

How to infer the kinetics of transcriptional bursting — how often a gene's promoter switches on and
how much mRNA it makes per burst — from single-cell RNA-seq (scRNA-seq) data, in a way that
accounts for the fact that scRNA-seq only captures a small, variable fraction of the transcripts
actually present in each cell. Speaks to stochastic gene expression modelling and to the statistics
of scRNA-seq data analysis.

## The question

Genes are transcribed in stochastic bursts rather than at a constant rate, and the "telegraph
model" (a promoter switching between an inactive and active state) is the standard description of
this. scRNA-seq lets this burstiness be estimated genome-wide instead of gene-by-gene, but the
technology captures only a fraction of the mRNA molecules in a cell, and that capture efficiency
varies from cell to cell. Existing methods for inferring burst kinetics from scRNA-seq either
ignored this technical variability (applying maximum likelihood or method-of-moments directly to
raw counts) or required experimental controls, such as spike-ins, that are rarely available. The
authors set out to ask what happens to inferred burst kinetics once this capture-efficiency
variability, and the related biological variability in cell size, are properly modelled instead of
ignored.

## The approach

The authors extend the telegraph model so that the actual transcript count in a cell is Poisson
given the cell's size and the burst parameters, with the burst "on" probability drawn from a Beta
distribution (a Beta-Poisson distribution at steady state). The observed, sequenced count is then
modelled as a further binomial downsampling of the true count, governed by a cell-specific capture
efficiency — the same binomial-capture idea the authors had used previously (Tang et al. 2020,
bayNorm) to explain apparent "dropouts" without invoking zero-inflation. This combination gives an
observed-count distribution that is again Beta-Poisson, but with an effective synthesis rate scaled
by both cell size and capture efficiency.

Against this model, they implement and compare four inference strategies: a bare maximum-likelihood
and a bare method-of-moments estimator applied directly to raw counts (the existing approach,
following Larsson et al. 2019), a modified version of each that approximately corrects for cell size
and capture efficiency, an Approximate Bayesian Computation (ABC) rejection scheme, and a
likelihood-free neural-network (NN) inference method built on a Bayesian deep-learning approach the
group had previously used for agent-based models (Jørgensen et al. 2022). The simulation-based
methods (ABC and NN) work by binomially downsampling simulated gene expression using an assumed
distribution of capture efficiencies, so they never need to evaluate the awkward modified likelihood
directly. All methods are benchmarked on synthetic data generated with known ground-truth
parameters, and then applied to real allele-specific and non-allele-specific scRNA-seq datasets.

## What it found

With capture efficiency fixed at 1.0 (unrealistic, but a sanity check), all methods recovered the
ground truth accurately. With a realistic, cell-to-cell-variable capture efficiency (mean around
0.06, typical of droplet protocols), the uncorrected maximum-likelihood and method-of-moments
estimators — which implicitly assume 100% capture — developed a systematic bias in the burst-off
rate and synthesis rate, and returned no estimate at all for roughly 65% of simulated genes. The
capture-corrected maximum-likelihood estimator avoided the bias but ran into numerical problems. The
two simulation-based methods, ABC and the neural network, gave accurate and precise estimates
throughout, with the neural network best at low cell numbers; about 1,000–2,000 cells sufficed for
reliable inference. Burst kinetics were found to be identifiable only for genes expressed highly
enough: for lowly-expressed genes, simpler Poisson or negative-binomial models fit the downsampled
data better by AIC than the true generating Beta-Poisson model. Applied to real allele-specific data
(Larsson et al. 2019), accounting for realistic capture shifted inferred burst sizes systematically
upward and widened the spread of burst frequencies versus assuming full capture, while still
reproducing the known association between TATA-box promoters and larger burst size. The model's
assumption that cell size and capture efficiency are the dominant extrinsic noise sources was
supported by its reproducing the observed expression correlation between the two alleles of a gene,
without needing correlated regulation between them. In mouse brain scRNA-seq datasets, stem-cell
marker genes showed higher burst frequency (not burst size) in stem cells than in differentiated
cells, and the same frequency-dominated pattern underlay the drop in ribosomal gene expression with
ageing.

## Limits and context

The inference assumes cell size and capture efficiency are the only relevant extrinsic noise
sources, setting aside other possible contributors such as fluctuations in kinetic rates driven by
other molecules, cell-cycle stage, or gene copy number — though the allele-correlation analysis is
offered as support for this choice. The theoretically well-motivated capture-corrected
maximum-likelihood method proved numerically unreliable in practice, which is why the paper favours
the likelihood-free ABC and neural-network alternatives. Burst kinetics remain unidentifiable for
lowly-expressed genes regardless of method, since the data does not contain enough information to
distinguish a bursty from a non-bursty source. The non-allele-specific method assumes both gene
copies share identical kinetics and transcribe independently, which the authors flag as a
simplification recent work suggests may not always hold. They point to multi-omic single-cell data
and more detailed mechanistic models of the sequencing protocol as directions that could resolve
more of the remaining technical noise.

## Citation

Tang W, Jørgensen ACS, Marguerat S, Thomas P, Shahrezaei V. Modelling capture efficiency of
single-cell RNA-sequencing data improves inference of transcriptome-wide burst kinetics.
Bioinformatics. 2023;39(7):btad395. https://doi.org/10.1093/bioinformatics/btad395. Open access
under CC BY 4.0. Code: https://github.com/WT215/nnRNA (neural network) and
https://github.com/WT215/Julia_ABC (ABC).
