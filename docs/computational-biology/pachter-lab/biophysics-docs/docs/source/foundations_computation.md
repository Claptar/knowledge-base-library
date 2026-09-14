---
title: Theory and Computation of Transcriptional Dynamics
source: https://github.com/pachterlab/biophysics/blob/ca6fe2ae824eb4cc3508ce951e1a7a868f50a043/docs/source/foundations_computation.rst
source_file: sources/pachter-biophysics-docs/docs/source/foundations_computation.rst
licence: BSD-2-Clause
route: pandoc-rst
fidelity: high
converted: '2026-09-14'
---

# Theory and Computation of Transcriptional Dynamics

**Source:** [`docs/source/foundations_computation.rst`](https://github.com/pachterlab/biophysics/blob/ca6fe2ae824eb4cc3508ce951e1a7a868f50a043/docs/source/foundations_computation.rst) · **Licence:** BSD-2-Clause · Converted 2026-09-14 from `.rst` (high)

Here we list a few reference papers on the theory and simulation of the chemical master equation as well as its application in stochastic modeling of gene expression.

[A general method for numerically simulating the stochastic time evolution of coupled chemical reactions](https://doi.org/10.1016/0021-9991(76)90041-3) - D. Gillespie, 1976.

In this article, Gillespie described the Stochastic Simulation Algorithm (Gillespie algorithm).

[The Poisson Representation. I. A New Technique for Chemical Master Equations](https://doi.org/10.1007/BF01014349) C. Gardiner, and S. Chaturvedi, 1977.

In this article, Gardiner and Chaturvedi introduced the Poisson representation which expresses the probability distribution as a convolution of Poisson distributions. This representation transforms chemical master equations into Fokker-Planck and stochastic differential equations and leads to a simple expression of chemical equilibrium states.

[Markovian Modeling of Gene-Product Synthesis](https://doi.org/10.1006/tpbi.1995.1027) - J. Peccoud, and B. Ycart, 1995.

2

This article studied the telegraph model of transcription. They studies properties of the systems and derived an analytical steady state solution.

The telegraph model

<img src="./figures/Peccoud_1995.png" class="align-center" width="300" alt="some text" />

[The chemical Langevin equation](https://doi.org/10.1063/1.481811) D. Gillespie, 2000.

In this article, Gillespie derived the chemical Langevin equation (CLE) from the chemical master equation (CME) based on the existence of a timescale with certain properties. In particular, the two properties are: 1) the timescale is small enough that the change in the state will be so slight and the propensity functions do not changes appreciably; 2) the timescale is large enough that the expected number of occurrences of each reaction channel will be much larger than 1.

[Approximate accelerated stochastic simulation of chemically reacting systems](https://doi.org/10.1063/1.1378322) - D. Gillespie, 2001.

In this article, Gillespie proposed the "τ-leap" method for Gillespie algorithm. It finds a time τ that is small enough that the change in the state and propensity function are negligible. Therefore, in this time interval, the propensity function will be essentially constant and the number of times a reaction channel fires will be a Poisson random variable.

[Summing up the noise in gene networks](https://doi.org/10.1038/nature02257) - J. Paulsson, 2004.

In this article, Paulsson used fluctuation-dissipation theorem to derive an equation for second order noise. The equation depends on kinetic orders of reactions and unified results from a few studies of gene expression noise.

[The finite state projection algorithm for the solution of the chemical master equation](https://doi.org/10.1063/1.2145882) - B. Munsky, and M. Khammash, 2006.

2

This article introduced the finite state projection (FSP) method to directly solves or approximates the solution of the chemical master equation. If there are only a finite number of reachable states, the exact soluiton can be computed using matrix exponentials. When there are infinite or extremely large number of reachable states, the state space is projected onto finite space, and the authors provided an estimation of accuracy of the truncated space approximation.

Fig 1. Conceptual figure for the finite state projection method.

<img src="./figures/Munsky_2006.jpeg" class="align-center" width="300" alt="some text" />

[Solving the chemical master equation for monomolecular reaction systems analytically](https://doi.org/10.1007/s00285-006-0034-x) - T. Jahnke, and W. Huisinga, 2007.

This article derives the exact solution formula for the chemical master equations of monomolecular reaction systems. It shows that the solutions can be expressed as a convolution of multinomial and product Poisson distributions, with time-dependent parameters evolving according to traditional reaction-rate equations.

[A stochastic model of gene regulation using the chemical master equation](https://doi.org/10.1007/978-0-8176-4558-8_7) - H. Booth et al., 2007.

This chapter describes a hybrid deterministic/stochastic simulation for chemical master equation in combination with chemical rate equations, which is applied to study genetic regulatory networks in prokaryotes: states of the gene represent the binding and unbinding of protein complexes to DNA are modeled using the master equation, while protein and substrate concentrations are represented by continuum variables modeled by differential equations.

[Analytical distributions for stochastic gene expression](https://github.com/pachterlab/biophysics/blob/ca6fe2ae824eb4cc3508ce951e1a7a868f50a043/docs/source/www.pnas.org/cgi/doi/10.1073/pnas.0803850105) - V. Shahrezaei, and P. Swain, 2008.

2

This article used time-scale difference of mRNA and protein decay to derive an approximation of protein distribution under the two-stage (constitutive) and three-stage (telegraph) model.

Fig 3. Predictions and simulations for a three-stage model of gene expression.

<img src="./figures/Swain_2008.png" class="align-center" width="300" alt="some text" />

[Consequences of mRNA transport on stochastic variability in protein levels](https://doi.org/10.1016/j.bpj.2012.07.015) - A. Singh, and P. Bokes, 2012.

2

This article derived the analytical solution of bursty model via probability generating function methods. They studied the effects of pre-mRNA export on mRNA and protein levels, and concluded that export step can reduce variability at mRNA level but not protein level.

Fig 1. Schematic of the gene expression model.

<img src="./figures/Singh_2012.jpeg" class="align-center" width="300" alt="some text" />

[Steady-state fluctuations of a genetic feedback loop: An exact solution](https://doi.org/10.1063/1.4736721) - R. Grima et al., 2012.

2

This article derived the exact steady-state solution of the chemical master equation for a gene regulatory feedback loop

The model for a gene regulatory feedback loop

<img src="./figures/Grima_2012.png" class="align-center" width="300" alt="some text" />

[Phenotypic switching in gene regulatory networks](https://doi.org/10.1073/pnas.140004911) - P. Thomas et al., 2014.

2

This article extended linear noise approximation (LNA) to conditional LNA.

Fig 2. Binary promoter switching.

<img src="./figures/Thomas_2014.png" class="align-center" width="300" alt="some text" />

[Chemical Langevin equation: A path-integral view of Gillespie's derivation](https://doi.org/10.1103/PhysRevE.101.032417) - J. Vastola, and W. Holmes, 2020.

This article describes an original path-integral description of the CME and show how Gillespie's two conditions leads to a path-integral equivalent to the CLE. We compare this approach to the path-integral equivalent of a large system size derivation and show that they are qualitatively different.

[bayNorm: Bayesian gene expression recovery, imputation and normalization for single-cell RNA-sequencing data](https://doi.org/10.1093/bioinformatics/btz726) - W. Tang et al., 2020.

2

This article introduced bayNorm, which uses Bayesian approach to model scRNA-seq gene expression. Negative binomial and binomial distribution are used to model biological variance and technical variance. Based on the model, bayNorm eanbles global scaling normalization, imputation and count recovery of scRNA-seq data.

Fig 1. A binomial model of mRNA capture.

<img src="./figures/Tang_2020.jpeg" class="align-center" width="300" alt="some text" />

[Modelling capture efficiency of single-cell RNA-sequencing data improves inference of transcriptome-wide burst kinetics](https://doi.org/10.1093/bioinformatics/btad395) - W. Tang et al., 2023.

2

This article describes a model for scRNA-seq data. They assume a telegraph model with a transcription rate proportional to the cell size for gene expression and a binomial distribution for capture. They also compare four different inference methods for kinetic parameters: MLE, methods of moments estimation (MME), an Approximate Bayesian Computation (ABC) rejection sampling algorithm, and using direct likelihood-free inference based on a neural network (NN) implementation.

Fig 1. Model of stochastic gene expression.

<img src="./figures/Tang_2023.jpeg" class="align-center" width="300" alt="some text" />

---

[Up: contents](../../index.md)
