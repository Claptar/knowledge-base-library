---
title: "Efron 2008 — Microarrays, Empirical Bayes and the Two-Groups Model"
paper: "summary"
source: "https://doi.org/10.1214/07-STS236"
licence: "© Institute of Mathematical Statistics — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Efron, B. (2008). Microarrays, Empirical Bayes and the Two-Groups Model. Statistical Science, 23(1), 1-22. ([original](https://doi.org/10.1214/07-STS236)). Rights: © Institute of Mathematical Statistics — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Microarrays, Empirical Bayes and the Two-Groups Model

## What this covers

A statistics paper on testing thousands of hypotheses at once — the situation created by
microarrays and similar high-throughput devices — built around the "two-groups model" that lets
Bayesian and frequentist ideas about false discovery rates meet in one framework.

## The question

Classical hypothesis testing, built by Neyman, Pearson and Fisher, was designed for a handful of
tests at a time, with controlling the overall Type-I error rate as the main goal. Efron asks what
happens to that theory when an experiment produces thousands of simultaneous tests — one per gene
on a microarray, one per voxel in a brain scan, one per school in an education dataset — each
reduced to its own test statistic ("z-value"). He argues that at this scale, Bayesian information
about the whole ensemble of tests forces itself on the analysis whether or not the statistician
wants it, and that the field's working tool, Benjamini and Hochberg's False Discovery Rate (FDR)
procedure, deserves a Bayesian account of why it works and where it can mislead. He also questions
an assumption the microarray literature had largely taken for granted: that an uninteresting case
should look like a draw from a standard normal distribution, and asks what goes wrong with FDR
methods when that is not actually true of the data.

## The approach

The organizing device is the "two-groups model": each of the $N$ cases is either null or non-null
with some prior probability, with its z-value drawn from one of two corresponding densities. Bayes'
rule then gives a *local false discovery rate*, $\mathrm{fdr}(z)$, the posterior probability that a
case with score $z$ is null — and Efron shows this sits underneath the Benjamini-Hochberg tail-area
rate, making that frequentist rule interpretable as an approximate Bayesian posterior probability.
Since the two densities are unknown, he turns to empirical Bayes: with thousands of similar parallel
cases, the mixture density of all the z-values can be estimated from the data itself, via a Poisson
generalized linear model fit to binned counts (the basis of his `locfdr` software). The paper's
central methodological move is the *empirical null*: rather than assume the null density is the
theoretical standard normal, estimate its mean and spread from the central bulk of the observed
z-histogram, under a "zero assumption" that values near zero are mostly null. The second half
surveys reasons the theoretical null can fail — correlation among test statistics, unmodeled
covariates, violated distributional assumptions — and extends the two-groups picture to related
problems: confidence intervals for cases flagged non-null, testing whether a predefined group of
cases (a biological pathway) is jointly enriched, and a "one-group" generalization where effect
sizes vary continuously instead of splitting cleanly into two classes.

## What it found

Across four real datasets — prostate cancer, school performance, proteomics and brain imaging — the
theoretical $N(0,1)$ null fits some (prostate) but badly misrepresents others (the BRCA and HIV
microarray studies), and using the wrong null changes conclusions sharply: for BRCA, the
Benjamini-Hochberg procedure at a 0.10 control level reports over 100 genes with the theoretical
null but essentially none with the empirical null, because the true central spread was overdispersed
relative to the textbook assumption. A simulation shows that even when every per-case assumption is
correct, correlation across thousands of z-values alone can make a nominal 10% false discovery
target behave very differently run to run — achieved false discovery proportions ranging from about
3% to 29% depending on an observable measure of the ensemble's spread, despite an average matching
the target. A power diagnostic on the prostate data shows only a small fraction of true non-null
genes would be expected to be flagged in any single run, underscoring that these studies are often
underpowered despite large $N$. Extending the machinery to gene-set enrichment and voxel-level
imaging works with mixed success: density estimation becomes harder in higher dimensions, and it
becomes unclear what null hypothesis even applies to a correlated or non-exchangeable group.

## Limits and context

Efron does not resolve several things the paper raises. He does not settle the disagreement between
Bayesian and frequentist camps over Benjamini-Yekutieli false-coverage-rate confidence intervals,
which he shows can be far wider and more poorly centered than the corresponding two-groups Bayesian
intervals in one simulated case, without declaring either approach simply wrong. He argues against
two reflexes: always trusting the theoretical null, a habit he traces to a long history of
one-case-at-a-time testing that does not transfer cleanly to large ensembles, and uncritically
trusting permutation-based nulls, which he shows can reproduce a wrong theoretical null just as
confidently as the parametric formula when the real problem is correlation rather than a per-case
failure. He is explicit that the empirical null costs real estimation variability relative to the
theoretical null — a cost he judges usually worth paying against the larger risk of a null that is
simply wrong. The paper leaves open how to build a theory of experimental design for large-scale
testing, and acknowledges his density-estimation approach becomes impractical in the higher
dimensions needed for rigorous gene-set testing. He presents the piece as one statistician's
viewpoint rather than a comprehensive review; published discussions of the paper, and his rejoinder,
engage further with points left open here.

## Citation

Efron, B. (2008). Microarrays, Empirical Bayes and the Two-Groups Model. *Statistical Science*,
23(1), 1-22. DOI: [10.1214/07-STS236](https://doi.org/10.1214/07-STS236). Published by the
Institute of Mathematical Statistics; available via Project Euclid.
