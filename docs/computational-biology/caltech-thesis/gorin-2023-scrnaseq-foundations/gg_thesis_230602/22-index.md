---
title: INDEX
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# INDEX

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A

Akaike information criterion (AIC), 24 Akaike weight, 24, 79, 87, 90

B

Bayes factor (BF), 23, 90

C Chemical master equation (CME), 25, 28 Complementary DNA (cDNA), 40 Constitutive transcription General, 35 One-stage, 7 Two-stage, 44

F

Fisher information matrix (FIM), 61 Fokker-Planck equation (FPE), 25, 30

### G

Generating function (GF), 16 Gillespie algorithm or stochastic simulation algorithm (SSA), 31, 63

J

Jaccard distance, 24

### K

k-nearest neighbor ( _𝑘_ -NN), 220 Kullback-Leibler divergence (KLD), 24

L

Likelihood ratio (LR), 23, 90, 93

### M

Markov property, 15 Model scales, 25 Moment-generating function (MGF), 17

225

226

### O

Ordinary differential equation (ODE), 25, 34

P Partial differential equation (PDE), 33 Poisson representation, 27, 35 Principal component analysis (PCA), 71, 104 Probability density function (PDF), 17, 19 Probability mass function (PMF), 17, 22 Probability-generating function (PGF), 16

R Reverse transcriptase (RTase), 41 RNA velocity Method, 69 Qualitative category of transient processes, 205 Quantity, 71

### S

Single-nucleus RNA sequencing (snRNA-seq), 92, 102 Squared coefficient of variation (CV<sup>2</sup> ), 102, 107 Stochastic differential equation (SDE), 25, 29 Survival function (generalized), 37

### U

Uniform Manifold Approximation and Projection (UMAP), 75, 104 Unique molecular identifier (UMI), 41

### V

Variational autoencoder (VAE), 125

227

1Note that we do not explicitly allow competing reaction pathways for species with non-Markovian efflux. The precise justification for this is somewhat subtle. In the Markovian case, setting up multiple reaction channels and choosing between them based on a categorical distribution over reactions is equivalent to simply seeing which reaction fires first. But in the non-Markovian case, these things are distinct: obviously, a reaction with deterministic waiting time _𝜏_ 1 _< 𝜏_ 2 will always fire before a reaction with waiting time _𝜏_ 2. This is, however, no obstacle: we can simply prepend a virtual Markovian species that is rapidly converted into species that follow one of the two waiting time distributions, and use a common generating function argument for all three species to obtain the sum of these species.

2To encode the dynamics of non-catalytic, non-Markovian processes, we exploit the isomorphism between characteristics and survival functions. This is most relevant for discrete systems, but Equation 4.30 suggests the correct way to connect this framework to continuous systems: Markovian interconversion is essentially an exponentially weighted moving average; deterministically-timed interconversion is a simple delay (a degenerate single-point “moving average”); generic non-Markovian interconversion maps to a generic moving average kernel. However, at this point, this framing is largely a mathematical curiosity.

> 3This nomenclature is somewhat at odds with the usual usage in [81, 277, 298]. Here, we use it to mean this particular noise model, in the spirit of, but with a narrow meaning than [124]. Elsewhere throughout the thesis, we somewhat loosely use it to indicate biological variability attributable to cell-to-cell differences, as in [136]. The nomenclature has evolved somewhat in the constituent reports, and by, e.g., [113], we converged on the following arbitrary but intuitive convention: in a distribution induced by a purely biological process, “intrinsic” noise is the Poisson component of variance or CV<sup>2</sup> , “extrinsic” noise is everything else.

> 4Here, a particularly imaginative reader of [112] and [115] will exclaim: “Hold on, if this entire formalization just amounts to fitting Equation 4.33, why do we need joint nascent and mature RNA data at all?” They will be correct: this even works for _𝑛_ = 1. The key idea is that distributions of stochastic systems exhibit exponential convergence to their steady state, so near-equilibrium states will be more “condensed” and far-from-equilibrium states will be more “dispersed,” because they are less stable, hence fewer cells will be sampled from them. Having multivariate data provides the advantage of disambiguating the dynamics when multiple attractors exist, e.g., the trajectories above and below the equilibrium line showcased in [168], which encode this exponential convergence to the high- and low-expression attractors, and would be difficult to impossible to distinguish based on a single modality.

5Here, an extraordinarily careful and attentive reader of [113] may raise a very natural question. The CIR model is derived under the assumption the regulator is present at high concentrations and largely resides near the mean. Why should we consider this limit, which is typically near zero and exhibits jump behavior? The justification is fourfold. First, there may be other systems that lead to CIR driving behavior without the approximation we have made, perhaps relating to membrane transport rather than production and degradation of regulators. Second, although the limit is nonphysical, the _convergence_ is relatively rapid, so there are large portions of parameter

228

space where the limiting behavior is an approximately valid description of the dynamics without violating the assumptions too harshly. Interestingly, the convergence to the extrinsic noise model is considerably slower. Third, it motivates the consideration of relatively “exotic” drivers that are otherwise ignored throughout this thesis: elsewhere, we assume all jump processes are compound Poisson. Fourth, the the continuous CIR process is equivalent to discrete autocatalysis, per Section A.8.3.2, so there may be an analogous fully discrete multi-stage process that follows the same statistics; however, we have not investigated this direction further.

> 6A careful reader of [107] may raise the concern: if we observe high expression of short nascent transcripts, does this mean these transcripts are present at _even higher_ abundance in the cell, potentially in the thousands or tens of thousands of copies? The answer is unclear, and will require dedicated study of specific genes. This is likely a combination of effects: real high biological expression, limitations in the choice of reference, limitations of the constant- _𝐶𝑁_ assumption, obscure technical artifacts like priming of spliced-out introns.

> 7More strictly, the _zero-inflated_ negative binomial (ZINB) distribution is most popular for _scVI_ . However, its meaning is unclear; the distribution appears to be an obsolete [274] holdover from pre-single-cell and single-molecule sequencing technology analyses. I am aware of one publication that attempts to provide a basis for this model [149], but it conflates a technical effect (dropout) with a biological one (promoter state switching) without any apparent justification. Ultimately, the problem with using a ZINB model to describe technical variation is that there is no mechanistic motivation for a process that leads to the loss of all of a gene’s molecules, nor an explanation for why it should choose _that_ gene without depleting others. That said, the ZINB distribution can be immediately obtained in the slow limit of an _𝑁_ = 2 model with a bursty and an inactive state.

> 8Here, a subtlety emerges. I do not believe that, e.g., landscapes or gradients are a helpful way to conceptualize _discrete molecule counts_ , because forcing a discrete object into a Procrustean bed of continuous models appears to be questionable modeling practice. That said, they may be effective for the underlying _continuous parameters_ . For example, the model I simulate from in Section 6.2 is precisely a (non-Markovian) graph traversal that represents transitions between cell types, and the time-varying H operator introduced in Chapter 4 indicates some generic transient process, which may, in turn, be reasonably well-approximated by a simple function. This function could be axiomatic (i.e., “a cell type is a point mass with respect to a set of parameter distributions”) or reflect a specific biophysical process. The key idea is that we have to operate on a slightly higher level of abstraction if we want to use these models, because the layers of single-molecule biological and technical stochasticity are inherent and non-negotiable. Considerable further work remains to determine whether this approach is promising, whether it leads to intractable problems, or whether it amounts to kicking the can down the road without providing any useful scientific insights.

> 9We can, of course, define dedicated bound states that are only accessible through molecule interactions, but this makes no difference to the mathematical challenges.

10This point is explored in substantial detail in [108].

> 11A naïve reading of this result might suggest that we have spent a considerable amount of theoretical effort to recapitulate something that is already fairly accepted practice. This reading is grossly incorrect, and the fact that the terms happen to match in this simplest of cases should only

229

encourage us to be more vigilant and thorough about developing and disclosing explicit mechanistic models, as they can provide insights about the basis for the success of procedures which are, at first glance, _ad hoc_ . Further, the result _does not_ fully agree with the standard description: for example, the interpretation of the Poisson variance term as purely technical does not hold under this model.

---

[← QUALITATIVE DISCUSSION OF SEQUENCING PROCEDURES AND THEIR CAVEATS](21-qualitative-discussion-of-sequencing-procedures-and-their-ca.md) · [Up: contents](index.md)
