---
title: "Felce 2026 — Biophysical Modeling for Gene Expression and Evolution"
paper: "summary"
source: "https://thesis.library.caltech.edu/17880/"
licence: "all rights reserved — not reproduced"
written: "2026-10-02"
---

> **Summary of a thesis.** Felce, Catherine (2026). "Biophysical Modeling for Gene Expression and Evolution". PhD thesis, California Institute of Technology. Defended December 10, 2025. ([original](https://thesis.library.caltech.edu/17880/)). Rights: all rights reserved — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Biophysical Modeling for Gene Expression and Evolution

## What this covers

A Caltech physics PhD thesis building biophysically motivated stochastic models for single-cell
genomics data, and separately developing exact mathematical analogies between physics and
evolutionary/ecological theory. It speaks to computational biology and theoretical evolutionary
biology, asking where mechanistic models of transcription, translation and chromatin dynamics can
replace heuristic analyses of single-cell data, and where correspondences between physical and
biological theory can sharpen evolutionary argument rather than just decorate it.

## The question

Single-cell gene-expression analysis has mostly relied on heuristics — differential expression,
dimension reduction, clustering — without reference to the molecular mechanisms of transcription,
translation and decay. As single-cell measurement expanded beyond mRNA to chromatin accessibility
(ATAC-seq) and surface protein (CITE-seq), the thesis asks whether these modalities can instead be
described jointly with RNA through stochastic chemical-master-equation models, and what such models
reveal about mechanism and data quality. A parallel question concerns evolution: comparative studies
of expression divergence between species have used bulk mRNA level as the evolving trait, which
obscures *which* biophysical process — burst size, burst frequency, decay rate — is actually under
selection. More broadly, the thesis asks whether analogies between physical theory (statistical
mechanics, Newtonian mechanics) and evolutionary/ecological theory (the Price equation, population
cycles) can be made exact rather than left as metaphor.

## The approach

Each central chapter builds a chemical master equation (CME) for molecular counts, solved via
generating-function methods, coupled either to real single-cell data or to a model of evolutionary
change. Chromatin accessibility at neighbouring ATAC-seq peaks is modeled as a 1-D Ising-like chain,
with one parameter tuning the preference of adjacent loci to share open/closed states, combined with
constitutive transcription to give a joint chromatin/RNA distribution. An existing nascent/mature-RNA
bursting model is extended with translation and protein decay, giving a joint CME for unspliced RNA,
spliced RNA and protein (with Meichen Fang). Per-gene biophysical parameters (burst size, splicing
rate, decay rate) estimated separately across six vertebrate species are treated as continuous traits
evolving along the species tree under competing multivariate Ornstein-Uhlenbeck models, each encoding
a different hypothesis about which quantity is under stabilizing selection. Finally, the
time-averaged continuous Price equation is shown identical to the virial theorem under a dictionary
mapping population size to momentum and trait value to position, then used to extend an ecological
maternal-effect model of population cycles to interacting, spatially separated subpopulations.

## What it found

In the chromatin chapter, an eight-parameter Ising-like model (independent on/off rates per site
plus a shared neighbour-correlation term) beat a six-parameter independent-sites model by BIC at
most tested six-peak loci across three 10x ATAC-seq datasets (26/30 PBMC, 7/7 mouse cortex, 14/14
human-mouse mixture), supporting real positive correlation between neighbouring sites. It also showed
that downstream transcript correlations can exceed the correlation of the parent DNA states, and that
registered and unregistered scATAC+scRNA data give comparable power to identify the correlation
parameter for a fixed budget, with scATAC-seq alone the most cost-efficient single modality.

In the RNA-protein chapter, simulations recovered all five parameters (burst size, splicing rate, RNA
decay, translation rate, protein decay) accurately for most of 46 simulated genes; because real
unspliced counts were too sparse, a reduced model fit to spliced RNA and protein alone remained
identifiable, with some loss of accuracy in splicing rate. Fit to two 10x CITE-seq PBMC datasets, it
reproduced observed joint mRNA-protein distributions for marker genes (CD14, CD45, IL7R).

In the phylogenetics chapter, fitting the competing models to parameters estimated across six
species' spleen data, the decay-rate-constrained model — selection on mRNA decay, with burst size
free to adapt and hold mean expression at its optimum — fit much better by AIC (2,124) than an
independent model (2,726) or a burst-size-constrained model (3,186). Selection strength on decay rate
also increased with expression level, matching dN/dS patterns for the same genes, suggesting mRNA
decay is the more constrained process and bursting the more flexible lever.

In the physics-analogy chapter, the Price-equation/virial-theorem identity supports reading the
covariance ("selection") term as a selection *rate*, and suggests selection corresponds to a rate of
change of fitness — a force — rather than being a constant force itself. Applied to the extended
maternal-effect model, it yields closed-form simple-harmonic-motion solutions for population cycles,
a "universality" result that combining such subpopulations can reproduce arbitrary periodic
dynamics, and, for spatially distributed competing subpopulations, a wave equation for trait
evolution in space.

## Limits and context

These are presented as first, deliberately minimal models rather than finished biological accounts.
The Ising-chromatin model does not explain the mechanistic origin of neighbour correlations and is
limited by ATAC-seq sparsity. The RNA-protein model treats surface protein as a direct,
instantaneous proxy for intracellular protein, and the full three-modality fit was unreliable on real
data because of noisy unspliced counts, hence the reduced two-modality fit used in practice. The
phylogenetic model assumes genome-wide-shared evolutionary rates and treats per-gene variability as
either following the shared model or white noise, resting on only six species and one tissue. The
physics analogies are flagged as formal correspondences, not shared causal mechanism — the
resemblance of the ecological oscillator to a mass on a spring is called "optical only" — and the
author favours the "statistical" interpretation of evolutionary theory over a "dynamical" one that
treats selection as a literal force. Throughout, the thesis argues against treating ad hoc heuristics
as adequate once single-cell, multi-modal data make mechanistic modeling possible.

## Citation

Felce, Catherine (2026). "Biophysical Modeling for Gene Expression and Evolution". PhD thesis,
California Institute of Technology. Defended December 10, 2025. Available at
https://thesis.library.caltech.edu/17880/.
