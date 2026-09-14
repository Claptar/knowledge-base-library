---
title: Causal attributable risk models
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Causal attributable risk models

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We consider again a data structure consisting of baseline covariates W , point treatment A, and outcome Y : O = (W, A, Y ). Under the consistency assumption, there exist full data X = (W, {Ya : a ∈A}) that allow us to view this as a missing data problem by thinking of the observed data as O = (W, A, Y ) = (W, A, YA) ∼ PFX0 ,g0 where FX0 is the distribution of the full data and g0 is the conditional distribution of the treatment mechanism given the full data: g0(a|X) ≡ P (A = a|X). Under the randomization assumption, treatment assignment is independent of the full data X given the baseline covariates W , i.e. g0(a|X) = g0(a|W ) .

The class of causal attributable risk models arises when one is interested in comparing the observed marginal distribution of Y to the marginal distribution of the counterfactuals Ya0 for different treatments a0. If desired, this comparison can be stratified based on a subset V of the baseline covariates W . These models may be of interest, for example, when one wishes to estimate the effect of different interventions on the marginal distribution of Y .

The two distributions of interest can be compared through a number of different summary measures that then yield natural parameters of interest. If we wish to compare the two distributions on an additive scale, a natural parameter of interest is E[Ya0 − Y |V ]. If Y is binary, a comparison on a multiplicative scale may be preferred. In this case, one natural parameter of interest is the relative risk

26


If we wish to model the relative risk as a function of a0 and the covariates of interest V , we need to ensure that our model does not allow these two probabilities to lie outside the interval [0, 1]. If, for example, we were to use the model


we would have that


which could easily fall outside the range [0, 1]. A commonly used approach is to model the log odds rather than the probabilities themselves. In the example above, one might use the model


which always constrains P [Ya0 = 1|V ] to lie in the interval [0, 1]. Such models,however, have the disadvantage that they are not robust with respect to the estimation of the nuisance parameter log P <u>[Y =1|V ]</u> 1−P [Y =1|V ]<sup>.</sup>

A class of models that not only respects the constraints on the probabilities of interest, but also achieves greater robustness focuses on modelling the switch relative risk given by


where I(·) is the indicator function. Such models do not rely on estimating E[Y |V ] consistently. In fact, even if one simply plugs in 0.5 for E[Y |V ], the switch relative risk is still estimated consistently.

Another approach to comparing the observed marginal distribution of Y to the marginal distribution of the counterfactuals Ya0 is to use quantile-quantile functions. If X1 ∼ F1 and X2 ∼ F2, then the quantilequantile function F2<sup>−1</sup> F1(·) maps X1 to a random variables that is distributed as F2. This approach leads to the class of structural nested models. Note that the quantile-quantile function as defined above does not work for discrete random variables. In this case, one may use the function F2<sup>−1</sup> [∆F1(X1) + (1 − ∆)F1(X1<sup>−)],</sup> where ∆ ∼ U (0, 1).

We will now focus on additive models and write E[Ya0 − Y |V ] = m(a0, V |β0), where m(·) is a function that is known up to β0. Our parameter of interest thus becomes β0. In order to estimate β0, we identify η0(V ) ≡ E0[Y |V ] as an additional nuisance paramter and write


Suppose η0(V ) were known. Then the class of IPTW estimating functions would be given by all


such that h is any function of A,V . The class of double robust estimating functions is obtained by subtracting the projection of Dh,IP T W<sup>∗(O|g, η0, β)ontothenuisancetangentspaceundertherandomization</sup> assumption, TRA. Since TRA = {s(A, W ) : E[s(A, W )|W ] = 0}, the projection of Dh,IP T W<sup>∗(O|g, η0, β)</sup> onto TRA can be obtained by first projecting onto the larger space of functions {s(A, W ) : s}, yielding E[Dh,IP T W<sup>∗(O|g, η0, β)|A, W],andthencompletingtheprojectionontoTRAbysubtractingtheconditional</sup> mean of E[Dh,IP T W<sup>∗(O|g, η0, β)|A, W]givenW.LettingQ0(A, W) = E0[Y |A, W],wehavethattheclassof</sup> double robust estimating functions is given by all


such that h is any function of A,V . If the nuisance parameter η0(V ) needs to be estimated, Dh,IP T W<sup>∗(O|g, η0, β)</sup> and Dh,DR<sup>∗(O|g, Q, η0, β)arenotorthogonaltoη0(V ).WethuswouldliketofindTNUISundertheassump-</sup> tion that η(V ) is unknown in order to orthogonalize these estimating functions with respect to TNUIS. If we achieve this, our estimator βn of β will no longer depend on η(V ) in first order. Furthermore, in some cases, an estimating function that has been orthogonalized to a nuisance parameter remains unbiased even if that nuisance parameter is mis-specified. In order to find TNUIS, we need the following definition and lemma:

<u>Definition:</u> An estimator βn of β is asymptotically linear with influence function IC(O|β) if


i.e. if βn − β can be written as an empirical mean of a function of the data plus a term that tends to zero in probability even when multiplied by<sup>√</sup> <u>n.</u>

<u>Lemma 1.3</u> (van der Laan & Robins): Under certain regularity conditions, TNUIS<sup>⊥canbeidentifiedwith</sup> the set of all influence functions corresponding to the class of asymptotically linear estimators βn of β:


Thus we can identify TNUIS<sup>⊥byfindingthesetofallinfluencefunctionsoftheestimatorsobtainedby</sup> solving the estimating equation corresponding to Dh,DR<sup>∗(O|g, Q, η, β).HavingidentifiedT ⊥</sup> NUIS<sup>inthisway,</sup> we find the projections of Dh,IP T W<sup>∗(O|g, η, β)andD</sup> h,DR<sup>∗(O|g, Q, η, β)ontoT ⊥</sup> NUIS<sup>as</sup>

28


We wish to check whether these estimating functions remain unbiased even if the specified η1(V ) is wrong. In the case of the IPTW estimating function, suppose that g is specified correctly. Then


Thus the IPTW estimating function will remain unbiased even if η is mis-specified as long as g is estimated consistently.

In the case of the DR estimating function, suppose first that g is specified correctly. Then


Now suppose that Q is specified correctly. Then


We conclude that the DR estimator obtained as the solution of the estimating equation


29

retains its double robust quality even if η is mis-specified.

**Marginal Structural Models for Time-Dependent Treatments: Doubly Robust Estimators** 11/1/04-11/3/04


**Observed Data.**


where A<sup>¯</sup> ≡ A<sup>¯</sup> (K) = (A(0), ..., A(K)) and L<sup>¯</sup> ≡ L<sup>¯</sup> (K + 1) = (L(0), ..., L(K + 1)). **Full Data.**


where A is the set of possible treatments and L<sup>¯</sup> a¯ is the counterfactual outcome process under treatment a¯. **Parameter of Interest.** We assume a **marginal structural model** (MSM)


where m() is a known function and V ⊆ L(0).

β0 is the parameter of interest.

**Assumptions. Temporal Ordering** We assume the time ordering that L(0) precedes A(0) precedes L(1), etc. We also assume that La¯(j) = La¯(j−1)(j) for j = 0, ..., K. **CA** O = ( A,<sup>¯</sup> L<sup>¯</sup> A¯<sup>)</sup> **SRA** P (A(j)|A<sup>¯</sup> (j − 1), X) = P (A(j)|A<sup>¯</sup> (j − 1), L<sup>¯</sup> ¯A(j−1)<sup>(j)),forj= 0, ..., K.</sup> **ETA** P (A = ¯a|X) > 0 for all a¯ ∈A.

**Factoring** P (O) **.** P (O) can be factored as


By SRA, we have


g0 is called the **treatment assignment mechanism** (TAM). Recall that G-computation ignores the treatment assignment mechanism and uses the first factor of P (O), which will be denoted Q0 (see the Sept 8 notes). The distribution of O is thus determined by Q0 and the treatment assignment mechanism g0.

---

[← Lecture of October 25, 2004, Oliver Bembom](33-lecture-of-october-25-2004-oliver-bembom.md) · [Up: contents](index.md) · [Recap of Point-Treatment Marginal Structural Models →](35-recap-of-point-treatment-marginal-structural-models.md)
