---
title: Methods
source: https://doi.org/10.1038/s41467-022-34857-7/
source_file: sources/papers/gorin-2022-interpretable-tractable/gorin-2022-interpretable-tractable.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `gorin-2022-interpretable-tractable.jats` from [papers/gorin-2022-interpretable-tractable](https://doi.org/10.1038/s41467-022-34857-7/) — papers · gorin-2022-interpretable-tractable, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Methods

The Supplementary Note contains comprehensive derivations and descriptions of analytical procedures. A complete list of major technical results is presented in Section 2. The Γ-OU and CIR models are fully motivated and solved in Section 3. Moments and autocorrelations are derived in Section 4. Limiting cases are derived in Section 5. Simulation details and validation of our exact results are presented in Section 6. Brief summaries of certain aspects of this work covered more fully in the supplement, and important miscellaneous information, are provided below.

## Notation {#Sec15}

A complete guide to our mathematical notation is presented in Section 2.2 in the Supplementary Note. The molecular species of interest are nascent transcripts ${{{{{{{{{\mathcal{N}}}}}}}}}}$ and mature transcripts ${{{{{{{{{\mathcal{M}}}}}}}}}}$. Their respective counts are denoted by random variables *X*_(*N*) and *X*_(*M*). The gene locus produces ${{{{{{{{{\mathcal{N}}}}}}}}}}$ with a time-dependent rate *K*(*t*) = *K*_(*t*), described by a stochastic process. Therefore, the probability density of the system is given by *P*(*X*_(*N*) = *x*_(*N*), *X*_(*M*) = *x*_(*M*), *K*_(*t*) ∈ [*K*, *K* + *dK*], *t*), i.e., the density associated with finding the system in a state with *x*_(*N*) molecules of ${{{{{{{{{\mathcal{N}}}}}}}}}}$, *x*_(*M*) molecules of ${{{{{{{{{\mathcal{M}}}}}}}}}}$, and a transcription rate of *K* at time *t*. Having introduced this rather formal notation, we use a shorthand that elides the random variables.

## Model definitions {#Sec16}

The Γ-OU and CIR models are mathematically defined via master equations, which describe how probability flows between different possible states. In particular,

$$\frac{dP({x}_{N},\,{x}_{M},\,K,\,t)}{dt}={{{{{{{{{\rm{CME}}}}}}}}}}+{{{{{{{{{\rm{FPE}}}}}}}}}},$$

$${{{{{{{{{{\rm{FPE}}}}}}}}}}}_{{{\Gamma }}{{{{{{{{{\rm{-OU}}}}}}}}}}}=-\frac{\partial }{\partial K}[(a\theta -\kappa K)P]+a\mathop{\sum }\limits_{n=2}^{\infty }{(-\theta )}^{n}\frac{{\partial }^{n}P}{\partial {K}^{n}},$$

$${{{{{{{{{{\rm{FPE}}}}}}}}}}}_{{{{{{{{{{\rm{CIR}}}}}}}}}}}=-\frac{\partial }{\partial K}[(a\theta -\kappa K)P]+\kappa \theta \frac{{\partial }^{2}(KP)}{\partial {K}^{2}}.$$

The CME term is identical for both models, and encodes transcription, splicing, and degradation reactions as in the constitutive model⁶⁷ (see Section 2 in the Supplementary Note). However, the Fokker-Planck equation (FPE) terms beyond first order, which encode transcription rate variation, are different.

## Analytically solving the Γ-OU and CIR models {#Sec17}

The Γ-OU model can be analytically solved using previous results for the *n*-step birth-death process coupled to a bursting gene. This approach exploits the fact that the source species of such a system has a Poisson intensity described by the Γ-OU process, and is fully outlined in Section 3.2 in the Supplementary Note. We set up a system with a bursting gene coupled to a 3-step birth-death process, characterized by the path graph $\varnothing \mathop{\to }\limits^{a}B\times {{{{{{{{{{\mathcal{T}}}}}}}}}}}_{0}\mathop{\to }\limits^{\kappa }{{{{{{{{{\mathcal{N}}}}}}}}}}\mathop{\to }\limits^{\beta }{{{{{{{{{\mathcal{M}}}}}}}}}}\mathop{\to }\limits^{\gamma }\varnothing$, where *B* ~ *Geom* with mean *θ*/*κ*.

The stochastic process describing the Poisson intensity of ${{{{{{{{{{\mathcal{T}}}}}}}}}}}_{0}$ is precisely the Γ-OU process⁸⁴. This implies that the joint distribution of the downstream species coincides with the system driven by Γ-OU transcription. The generating function of SDE-driven system can be computed using the solution of the bursty system, reported in Eq. (13), where *U*₀(*s*; *u*_(*N*), *u*_(*M*)) = *A*₀e^(−*κs*) + *A*₁e^(−*βs*) + *A*₂e^(−*γs*) can be computed by solving Eq. (14):

$${A}_{2}   ={u}_{M}\frac{\beta }{\beta -\gamma }\frac{\kappa }{\kappa -\gamma },\\ {A}_{1} =\frac{\kappa }{\kappa -\beta }\left({u}_{N}-{u}_{M}\frac{\beta }{\beta -\gamma }\right),\\ {A}_{0} =-{A}_{1}-{A}_{2}.$$

The CIR model is solved using a state space path integral representation of *P*(*x*_(*N*), *x*_(*M*), *K*, *t*) which combines a path integral representation of the CME⁵⁹ with a more conventional continuous state space path integral. The Γ-OU model can also be solved using this method, along with a plethora of other discrete-continuous hybrid models.

## Analytically computing moments and autocorrelation functions {#Sec18}

The master equation satisfied by *P*(*x*_(*N*), *x*_(*M*), *K*, *t*) can be recast as a partial differential equation (PDE) satisfied by *ϕ*(*u*_(*N*), *u*_(*M*), *s*, *t*) (see Section 3 in the Supplementary Note):

$$\frac{\partial \phi }{\partial t}=\,  {u}_{N}\frac{\partial \phi }{\partial s}+\beta ({u}_{M}-{u}_{N})\frac{\partial \phi }{\partial {u}_{N}}-\gamma {u}_{M}\frac{\partial \phi }{\partial {u}_{M}}\\     +a\theta s-\kappa s\frac{\partial \phi }{\partial s}+f(s),$$

$${f}_{{{\Gamma }}{{{{{{{{{\rm{-OU}}}}}}}}}}}(s)=\,a\mathop{\sum }\limits_{n=2}^{\infty }{\theta }^{n}{s}^{n},$$

$${f}_{{{{{{{{{{\rm{CIR}}}}}}}}}}}(s)=\,{s}^{2}\kappa \theta \frac{\partial \phi }{\partial s}.$$

By taking certain partial derivatives of the above PDEs, we can recover ODEs satisfied by moments and autocorrelation functions. These can then be straightforwardly solved to compute them.

## Obtaining RNA count distributions from analytical solutions {#Sec19}

The aforementioned analytical solutions to each model are in the form of generating functions. To numerically obtain predicted distributions, we first compute the generating function (Eq. (12)) by numerically solving ODEs and integrating the results (i.e., using Eqs. (13) and (14) or Eqs. (15) and (16)). Next, we take an inverse fast Fourier transform^(48,85). To avoid artifacts, the ODEs must be evaluated for a sufficiently fine grid of *g*_(*N*) and *g*_(*M*) on the complex unit sphere.

## Stochastic simulation {#Sec20}

Stochastic simulations can verify our analytical results and enable further facile extensions to SDE-driven systems that are otherwise analytically intractable. Because our models involve no feedback, we split this problem into two parts: first, we simulate the continuous stochastic dynamics of the transcription rate *K*(*t*), and then we simulate the discrete stochastic dynamics of the nascent and mature RNA using a variant of Gillespie’s direct method⁸⁶. This approach requires evaluating reaction waiting times for time-varying transcription rates. For the Γ-OU model, we computed these times exactly *via* the Lambert W function. For the CIR model, we used a trapezoidal approximation to the integral of the reaction flux.

To ensure that all regimes of interest are verified, we chose six parameter sets to test: four of these lie in the extreme limits shown in Fig. 2, and two lie in intermediate regimes. We performed 10⁴ simulations for each parameter set, with *β* = 1.2 and *γ* = 0.7. The trajectories were equilibrated until a putative steady-state time *T*_(*ss*). Afterward, the simulations were left to run until *T*_(*ss*) + *T*_(*R*) to enable the computation of autocorrelations. The parameters as well as values of *T*_(*ss*) and *T*_(*R*) are reported in Supplementary Table 5. The implementation details and simulation results are given in Section 6 in the Supplementary Note.

## Data processing {#Sec21}

We used four independent mouse datasets generated by the Allen Institute for Brain Science^(71,87). We pseudoaligned the raw reads to a combined intronic/exonic mm10 mouse genome reference using *kallisto∣bustools*, yielding spliced and unspliced count matrices^(72,88). We used the default *bustools* filter to remove low-quality cells. To obtain relatively homogeneous cell types, we did not recluster the data. Instead, we used pre-existing cell type annotations, removing all cells with fewer than 10⁴ total molecules.

## Filtering single-cell transcriptomic data {#Sec22}

The filtering procedure used data from a single mouse (see Section 8 in the Supplementary Note), and involved the following steps. We selected a series of moderate- to high-abundance glutamatergic cell subtypes (L2/3 IT, L5 IT, L6 IT, L5/6 NP, and L6 CT, taken from sample B08). Genes whose expression levels were too low (*μ*_(*N*), *μ*_(*M*) ≤ 0.01, or $\max ({X}_{N}),\max ({X}_{M})\le 3$) or too high ($\max ({X}_{N}),\max ({X}_{M})\ge 400$) were removed, leaving 3677 genes. Next, to find genes which are potentially well-described by the Γ-OU and CIR models, we fit the three computationally simpler overdispersed limiting models depicted in Fig. 2 using the *Monod* package⁷³. Within *Monod*, the *SciPy* implementation of L-BFGS-B was used to perform gradient descent⁸⁹ and obtain maximum likelihood estimates for the three-parameter reduced models. We selected genes most consistently assigned to each model (Fig. 4a) according to their Akaike weights⁹⁰. This step identified genes that appeared to be reproducibly described by each model class, and provided a tentative basis for out-of-sample predictions. Finally, we restricted our analysis to the best-fit 35 genes in each category, as quantified by the maximum rank of the chi-squared statistic observed across the five subtype datasets. This filtering step was applied to avoid contributions due to model misspecification or poor convergence, and focus on the genes that best agreed with the regimes of interest. The preliminary analysis produced 35 genes of interest for the Γ-OU-like and CIR-like categories and 10 genes for the mixture-like category.

## Fitting SDE–CME models to simulated and single-cell transcriptomic data {#Sec23}

The *SciPy* implementation of L-BFGS-B was used to perform gradient descent⁸⁹ and obtain maximum likelihood estimates for the four-parameter SDE–CME models. To control for potential failure to converge, we omitted all results with log-likelihood ratios with magnitude above 150 from visualization in Fig. 4. All fits to raw data are shown in Supplementary Figs. 8–37. Fits with large likelihood ratios typically corresponded to poor fits to one or both of the models, possibly due to numerical issues. The Python package *PyMC3* was used to sample the parameter posteriors, using the non-gradient-based Markov chain Monte Carlo sampler DEMetropolisZ⁹¹. Synthetic data inference used a uniform prior, four chains, 1000 burn-in iterations, and 12,000 sampling iterations. Biological data inference used a uniform prior, one chain, and 1000 iterations.

## Reporting summary {#Sec24}

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

---

[← Discussion](03-discussion.md) · [Up: contents](index.md) · [Supplementary information →](05-supplementary-information.md)
