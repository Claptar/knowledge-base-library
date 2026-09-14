---
title: 8 Lecture Eight
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Lecture Eight

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **8.1 The Normal Distribution as an Approximation to the Binomial Distribution**

The normal distribution shows up as an approximation to the Binomial Distribution and, in fact, this was the way the normal density was first discovered by De Moivre. We shall go over this today. Fix _n ≥_ 1 and _p ∈_ (0 _,_ 1). Suppose _X ∼_ Bin( _n, p_ ). Then


In what sense do the above probabilities resemble the normal density? To understand this, the first step is to approximate the factorials using the Stirling Approximation. A brief overview of Stirling’s approximation is discussed next.

#### **8.1.1 Stirling Approximation**

The Stirling Approximation is an approximation for _n_ ! that is quite accurate even for small values of _n_ . It states that


The Stirling Approximation is quite accurate even for small _n_ (even for _n_ = 1) as can be checked by evaluating the right hand side and comparing it to _n_ !. The accuracy of approximation can be gauged from the bound:


Here is a heuristic justification for the Stirling Approximation using the Laplace Method for approximating integrals. We start with the basic formula


which can be proved by induction over _n_ . Rewrite the integral as


The change of variable _x_ = _ny_ gives


The function _y �→_ log _y − y_ attains its maximum value of _−_ 1 at _y_ = 1. Because of the presence of _n_ in the exponent, the integral will be dominated by the points _y_ which are close to 1 (at least for large _n_ ). We shall therefore use the second order Taylor expansion:


42

in the exponent to get


which is exactly the Stirling Approximation.

#### **8.1.2 Entropy Approximation of** _Bin_ ( _n, p_ )

Let us now get back to the problem of approximating the binomial probabilities (32). A reference for these calculations is Sinai [2, Chapter 3] (available for free through the Berkeley Library website). Using the Stirling approximation


for each of the factorials in (32), we get


Note that _f_ = _k/n_ denotes the fraction of heads whose probability we are calculating. Using the notation


we have


The quantity _D_ ( _f ∥p_ ) is known variously as either the **Relative Entropy** of ( _f,_ 1 _− f_ ) with respect to ( _p,_ 1 _−p_ ) or as the **Kullback-Leibler divergence** between ( _f,_ 1 _−f_ ) and ( _p,_ 1 _−p_ ). We shall refer to (33) as the **Entropy Approximation to** _Bin_ ( _n, p_ ). The relative entropy _D_ ( _f ∥p_ ) has the following two important properties:

1. **Nonnegativity** : _D_ ( _f ∥p_ ) is always nonnegative. This is basically a consequence of the elementary inequality log _x ≤ x −_ 1 because


2. **Zero if and only if** _f_ = _p_ : This basically follows from the above argument and the fact that log _x_ = _x −_ 1 if and only if _x_ = 1.

43

The quantity _D_ ( _f ∥p_ ) is often seen as a measure of discrepancy or distance or divergence between the two discrete probability distributions ( _f,_ 1 _− f_ ) and ( _p,_ 1 _− p_ ).

The entropy approximation (33) can be rewritten in the following way. The proportion _f_ represents the empirical proportion of heads while _p_ represents the theoretical (or true) proportion of heads. Thus


which shows clearly how the probability decays the further ( _f,_ 1 _− f_ ) moves from ( _p,_ 1 _− p_ ) as measured by the Kullback-Leibler divergence. The subject “Large Deviations Theory” in Probability extends such probability facts to more complicated scenarios.

#### **8.1.3 Normal Approximation of** _Bin_ ( _n, p_ )

To obtain the normal approximation for the Binomial, we approximate


by its Taylor expansion around _f_ = _p_ :


for some _g_ between _f_ and _p_ . One can directly verify (by calculating derivatives of _G_ ) that


As a result


Plugging this in the formula for P _{Bin_ ( _n, p_ ) = _k}_ , we obtain


If the third term above is close to one, then we can drop it which will lead to the normal approximation for P _{Bin_ ( _n, p_ ) = _k}_ . In order to do so, we need


to be small. Because _|_ 2 _g −_ 1 _| ≤_ 1 (as _g_ lies between 0 and 1) and _g ≥_ min( _f, p_ ) and 1 _− g ≥_ min(1 _− p,_ 1 _− f_ ), we can write


If _p_ is away from 0 and 1 and _n|f − p|_<sup>3</sup> is small, then the above quantity will be small when _n_ is large. In this situation, we can ignore the remainder term to obtain the approximation:


44

Also in the case when _p_ is away from 0 and 1 and when _n|f − p|_<sup>3</sup> is small, we have _f/p_ is close to 1 for large _n_ . We can thus replace _f_ by _p_ in the multiplicative term to obtain


The above is the normal density with mean _np_ and variance _np_ (1 _− p_ ) evaluated at _k_ . We thus have


where _φ_ ( _x_ ; _µ, σ_<sup>2</sup> ) denotes the normal density with mean _µ_ and variance _σ_<sup>2</sup> evaluated at _x_ .

(35) is the normal approximation for P _{Bin_ ( _n, p_ ) = _k}_ . Note that this requires _p_ to be away from 0 and 1 and _n|_ ( _k/n_ ) _− p|_<sup>3</sup> to small. If these conditions are violated, the normal approximation will not be accurate. The Entropy Approximation, on the other hand, is accurate for a much larger range of _k_ (it is accurate as long as the Stirling Approximation is accurate for _n − k_ and _k_ and the Stirling approximation is quite accurate even for small integers).

For a concrete example, consider the following two situations:

1. Suppose _n_ = 3000 _, k_ = 2500 _, p_ = 0 _._ 5. Here _f_ = _k/n_ = 5 _/_ 6 which is quite far from _p_ . For example, _n|f − p|_<sup>3</sup> is quite large. One can then verify on the computer that:

   - P _{Bin_ ( _n, p_ ) = _k} ≈_ 1 _._ 7 _×_ 10<sup>_−_318</sup> and _φ_ ( _k_ ; _np, np_ (1 _− p_ )) _≈_ 4 _._ 3 _×_ 10<sup>_−_292</sup>

Thus the normal approximation is off by many orders of magnitude. On the other hand, the entropy approximation gives


which is quite close to P _{Bin_ ( _n, p_ ) = _k}_ .

2. Suppose _n_ = 3000 _, k_ = 1525 _, p_ = 0 _._ 5. Here _f_ = 0 _._ 5083 which is quite close to _p_ . Also _n ∗|f − p|_<sup>3</sup> = 0 _._ 00173 is quite small. Then

P _{Bin_ ( _n, p_ ) = _k} ≈_ 0 _._ 0096037 and _φ_ ( _k_ ; _np, np_ (1 _− p_ )) _≈_ 0 _._ 0096033 so the normal approximation is very accurate. The entropy approximation here is:


In both these situations, the entropy approximation is accurate while the normal approximation works well only in the second situation.

#### **8.1.4 Implication for the chi-squared test**

The Normal Approximation to the Binomial is the key ingredient in the popular Chi-Squared test for goodness of fit. Because the normal approximation is not always valid, the chisquared test comes with certain warnings recommending against its use in some exceptional cases (such as situations in which some of the cells have low counts). Use of the chi-squared test in such situations leads to paradoxical conclusions. This is very nicely illustrated in the following simple example (taken from Jaynes [1, Section 9.12]).

45

**Example 8.1.** _Suppose that a coin toss can give three different results: H (heads), T (tails) and edge (when the coin just stands on its edge). Suppose that a person A assigns probabilities_ 0 _._ 499 _,_ 0 _._ 499 _,_ 0 _._ 002 _to these three outcomes and another person B assigns probabilities_ 1 _/_ 3 _,_ 1 _/_ 3 _,_ 1 _/_ 3 _to these outcomes. Suppose now that we perform an experiment with this coin by tossing it n_ = 29 _times and this led to_ 14 _heads,_ 14 _tails and_ 1 _edge._

_We are now interested in measuring the fit between each of the two models (of person A and B) and the observed data. If we use the chi-squared criterion:_


_for measuring goodness of fit, we would obtain_


_as the goodness of fit for A and_


_as the goodness of fit for B. This clearly runs against intuition as clearly A’s model seems closer to the observed data compared to B. The reason for this strangeness is that the underlying normal approximation is not working._

_The right approach is simply to calculate probabilities of the observed data for each of the two models. Specifically,_


_and_


_So A’s model assigns much higher probability (about 483 times higher) to the observed data compared to B’s model. This certainly matches our intuition. Note that if we don’t know the specific order of the 29 outcomes, we can multiply the above probabilities by the multinomial coefficient_


_but this factor will not change anything as both the above probabilities will be multiplied by this same factor._

_The moral of this example is to always calculate binomial/multinomial probabilities directly (or use the Entropy Approximation if an approximation is necessary). The normal approximation probabilities should be calculated only when one is sure that the normal approximation is accurate._

---

[← 7 Lecture Seven](08-7-lecture-seven.md) · [Up: contents](index.md) · [9 Lecture Nine →](10-9-lecture-nine.md)
