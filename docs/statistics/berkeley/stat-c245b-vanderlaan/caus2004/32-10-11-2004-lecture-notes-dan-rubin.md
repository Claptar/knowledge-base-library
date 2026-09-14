---
title: 10/11/2004 Lecture Notes, Dan Rubin
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10/11/2004 Lecture Notes, Dan Rubin

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This lecture concerns estimating function methods in marginal structural models for point treatment longitudinal studies. The data is O = (W, A, Y ), where W, A, Y represent covariates, treatment, and an outcome. Let X = (W, Y ), and let g(·|W ) denote the conditional distribution of A, given W . As usual, we make the consistency assumption, so assume there is an unobserved full data structure of counterfactuals X<sup>F ull</sup> = (W, (Ya : a ∈A)), for A a finite set of possible treatments. We also make the randomization assumption, which here states that g(a|X<sup>F ull</sup> ) = g(a|W ), and the experimental treatment assumption (ETA) that g(a|W ) > 0 for all a ∈A with probability one.

Suppose the parameter of interest is E[Ya|V ], where V ⊆ W . In general, this will be hard to estimate for high dimensional data without additional assumptions, which is why marginal structural models were introduced. A marginal structural model assumes that E[Ya|V ] = m(a, V |β), for a known function m, where β is an unknown k-dimensional Euclidean parameter. When we assume such a model, β becomes the parameter of interest.

23

In previous lectures, we studied how estimating functions can be used to estimate β when the full data is observed. In particular, the class of full data estimating functions was given by:


We next define the class of inverse probability of treatment weighted (IPTW) estimators as follows:


Note that unlike in the full data estimating functions, the IPTW estimating functions depend on a nuisance parameter (g), which must be estimated from the data. It is trivial to check that under the consistency, SRA and ETA assumptions (unlike G-computation methods, ETA is necessary here), E[Dh,IP T W (O|β, g)|X<sup>F ull</sup> ] = Dh(X<sup>F ull</sup> |β). So by first conditioning on X<sup>F ull</sup> , the IPTW estimating functions are indeed unbiased estimating functions for β.

Although the IPTW estimators are simple and easy to implement, we can improve upon them in terms of both efficiency and robustness, using estimating functions described below. Before giving these functions, we need a few definitions and facts. Consider the Hilbert space L<sup>2</sup> 0<sup>(O) ={h(O) :E[h(O) =0], E[h2(O)] <∞}</sup> endowed with the inner product (h1(O), h2(O)) = E[h1(O)h2(O)]. Let TRA denote the linear closure in this Hilbert space of all scores of one dimensional regular parametric submodels Pϵ of the data generating distribution, where the submodels only fluctuate the treatment mechanism g, and pass through the true data generating distribution at ϵ = 0. Such submodels can be represented as Pϵ(O) = P (Y |A, W )P (W )gϵ(A|W ), where −1 < ϵ < 1 and gϵ=0(A|W ) = g(A|W ). Consider the submodels gϵ(A|W ) = (1 + ϵs(A, W ))g(A|W ), where s(A, W ) ∈ L<sup>2</sup> 0<sup>(O)andE[s(A, W)|W] = 0.TakingthelogofPϵ(0)anddifferentiating,itiseasytosee</sup> that s(A, W ) is the score. From this, it can be shown that TRA = {s(A, W ) ∈ L<sup>2</sup> 0<sup>(O) : E[s(A, W)|W] = 0}.</sup> We now need a few further facts.

- (1) From Theorem 1.3 in Mark’s book with Jamie Robins, the class of all possible estimating is given by {Dh,IP T W (O|β, g) − Π(Dh,IP T W (O|β, g)|TRA)}, where Π represents the projection operator in Hilbert space.

(2) For any function f (O) ∈ L<sup>2</sup> 0<sup>(O),Π(f(O)|TRA) = E[f(O)|A, W] −E[f(O)|W].</sup>

To see part (2), note that clearly the proposed Π(f (O)|TRA) is in TRA, because:

(7) E[Π(f (O)|TRA)] = E[E[f (O)|A, W ]|W ] − E[E[f (O)|W ]|W ] = E[f (O)|W ] − E[f (O)|W ] = 0

And if s(A, W ) ∈ TRA then E[s(A, W )|W ] = 0, so:

(8)E[(f − E[f |A, W ] + E[f |W ])s(A, W )] = E[fs(A, W )] − E[E[f |A, W ]s(A, W )] + E[E[f |W ]s(A, W )] (9) = E[s(A, W )E[f |A, W ]] − E[s(A, W )E[f |A, W ]] + E[E[f |W ]E[s(A, W )|W ]] = 0

Hence, subtracting the IPTW estimating functions from their projections on TRA, we obtain the following class of all possible estimating functions. These depend on two nuisance parameters: the treatment mechanism g(a|W ) and E[Y − m(A, V |β)|A, W ]. These are called doubly robust estimating functions, because they are unbiased if either of the two nuisance parameters is correctly specified.


This lecture concerns estimating function methods in marginal structural models for point treatment longitudinal studies. The data is O = (W, A, Y ), where W, A, Y represent covariates, treatment, and an outcome. Let X = (W, Y ), and let g(·|W ) denote the conditional distribution of A given W . As usual, we make the consistency assumption, so assume there is an unobserved full data structure of counterfactuals X<sup>F ull</sup> = (W, (Ya : a ∈A)), for A a finite set of possible treatments, and that Y = YA. We also make the randomization assumption, which here states that g(a|X<sup>F ull</sup> ) = g(a|W ), and the experimental treatment

24

assumption (ETA) that g(a|W ) > 0 for all a ∈A.

Suppose the parameter of interest is E[Ya|V ], where V ⊆ W . In general, this will be hard to estimate for high dimensional data without additional assumptions, which is why marginal structural models were introduced. A marginal structural model assumes that E[Ya|V ] = m(a, V |β), for a known function m, where β is an unknown k-dimensional Euclidean parameter. When we assume such a model, β becomes the parameter of interest.

In previous lectures, we studied how estimating functions can be used to estimate β when the full data is observed. In particular, the class of full data estimating functions was given by:


We next define the class of inverse probability of treatment weighted (IPTW) estimators as follows:


Note that unlike in the full data estimating functions, the IPTW estimating functions depend on a nuisance parameter (g), which must be estimated from the data. It is trivial to check that under the consistency, SRA and ETA assumptions (unlike G-computation methods, ETA is necessary here), E[Dh,IP T W (O|β, g)|X<sup>F ull</sup> ] = Dh(X<sup>F ull</sup> |β). So by first conditioning on X<sup>F ull</sup> , the IPTW estimating functions are indeed unbiased estimating functions for β.

Although the IPTW estimators are simple and easy to implement, we can improve upon them in terms of both efficiency and robustness, using estimating functions described below. Before giving these functions, we need a few definitions and facts. Consider the Hilbert space L<sup>2</sup> 0<sup>(O) ={h(O) :E[h(O) =0], E[h2(O)] <∞}</sup> endowed with the inner product (h1(O), h2(O)) = E[h1(O)h2(O)]. Let TRA denote the linear closure in this Hilbert space of all scores of one dimensional regular parametric submodels Pϵ of the data generating distribution, where the submodels only fluctuate the treatment mechanism g, and pass through the true data generating distribution at ϵ = 0. Such submodels can be represented as Pϵ(O) = P (Y |A, W )P (W )gϵ(A|W ), where −1 < ϵ < 1 and gϵ=0(A|W ) = g(A|W ). Consider the submodels gϵ(A|W ) = (1 + ϵs(A, W ))g(A|W ), where s(A, W ) ∈ L<sup>2</sup> 0<sup>(O)andE[s(A, W)|W] = 0.TakingthelogofPϵ(0)anddifferentiating,itiseasytosee</sup> that s(A, W ) is the score. From this, it can be shown that TRA = {s(A, W ) ∈ L<sup>2</sup> 0<sup>(O) : E[s(A, W)|W] = 0}.</sup> We now need a few further facts.

- (1) From Theorem 1.3 in Mark’s book with Jamie Robins, the class of all possible estimating is given by {Dh,IP T W (O|β, g) − Π(Dh,IP T W (O|β, g)|TRA)}, where Π represents the projection operator in Hilbert space.

- (2) For any function f (O) ∈ L<sup>2</sup> 0<sup>(O),Π(f(O)|TRA) = E[f(O)|A, W] −E[f(O)|W].</sup>

To see part (2), note that clearly the proposed Π(f (O)|TRA) is in TRA, because:

E[Π(f (O)|TRA)] = E[E[f (O)|A, W ]|W ] − E[E[f (O)|W ]|W ] = E[f (O)|W ] − E[f (O)|W ] = 0 And if s(A, W ) ∈ TRA then E[s(A, W )|W ] = 0, so:

E[(f − E[f |A, W ] + E[f |W ])s(A, W )] = E[fs(A, W )] − E[E[f |A, W ]s(A, W )] + E[E[f |W ]s(A, W )] = E[s(A, W )E[f |A, W ]] − E[s(A, W )E[f |A, W ]] + E[E[f |W ]E[s(A, W )|W ]] = 0

Hence, subtracting the IPTW estimating functions from their projections on TRA, we obtain the following class of all possible estimating functions. These depend on two nuisance parameters: the treatment mechanism g(a|W ) and E[Y − m(A, V |β)|A, W ]. These are called doubly robust estimating functions, for reasons we will discuss below. Here, Q(A, W |β) = E[Y − m(A, V |β)|A, W ].


Now consider the model where g = g0 is known, as would be the case in a randomized trial. Intuitively, this constrained model allows for less submodels through the data generating distribution varying the nuisance parameter g, so the nuisance tangent space should be smaller than before. Hence, the orthocomplement of the nuisance tangent space (meaning the class of all estimating functions) should be larger than before. This is indeed the case. In this constrained model, the orthogonal complement of the nuisance tangent space at the data generating distribution P0 is:


For given h, it can be shown that the function Dh,IP T W (O|β, g0)+ ϕ(A, W ) in TNUIS<sup>⊥with the smallest vari-</sup> ance (and hence the best estimating function) has ϕ(A, W ) = Π(Dh,IP T W (O|β, g)|TRA). However, this choice of ϕ leads to the estimating function Dh,DR(O|β, g0, Q). So when g is known, minimizing the variance over (h, ϕ) leads to the same optimal estimating function as in the model where g is unknown, and the variance is minimized over the index h. In practice, a general recommendation is to take h(A, V ) = dβd<sup>m(A, V |β)g(A|V ).</sup>

We will now explain why the estimating function Dh,DR(O|β, g, Q) is called doubly robust. Note that the function depends on two nuisance parameters, g and Q, and each parameter is an unknown function. Here g is the treatment mechanism, while Q only depends on the full data distribution. If either of the two nuisance parameters is correctly specified, then the estimating function will be unbiased. Suppose statistician A models g and implements the IPTW estimator, statistician B models Q (so models E[Y |A, W ]) from which he/she implements the G-computation estimator, and statistician C implements the double robust estimator from the g and Q fits of statisticians A and B. If g and Q are correctly modelled, all three statisticians will have consistent estimators. If g is correctly modelled but Q is not, statisticians A and C will be consistent. If Q is correctly modelled but g is not, statisticians B and C will be consistent. Therefore, statistician C is said to implement a doubly robust estimator, because he/she is consistent whenever statisitician A or B is consistent. Note that when g is correctly modelled but Q is not, the doubly robust estimator still has smaller asymptotic variance than the IPTW estimator, so it can improve efficiency as well as robustness.

---

[← Estimating Function Approach](31-estimating-function-approach.md) · [Up: contents](index.md) · [Lecture of October 25, 2004, Oliver Bembom →](33-lecture-of-october-25-2004-oliver-bembom.md)
