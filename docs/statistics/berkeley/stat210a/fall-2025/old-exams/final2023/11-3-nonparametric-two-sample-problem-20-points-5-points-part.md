---
title: 3. Nonparametric two-sample problem (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2023.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/final2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Nonparametric two-sample problem (20 points, 5 points / part).

**Source:** [`old-exams/final2023.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts you may assume are true for this problem:

- i.i.d.

- _•_ In the _one-sample_ model with _X_ 1 _, . . . , Xn ∼ P_ , with the _Xi_ observations taking values in R and no further assumptions on the distribution _P_ , the order statistics


are complete sufficient.

- If _Zn ⇒ Z_ and _Wn ⇒ W_ , and _Zn_ is independent of _Wn_ for every _n_ , then ( _Zn, Wn_ ) _⇒_ ( _Z, W_ ) where _Z_ is independent of _W_ .

Assume we have a non-parametric two-sample problem of the form


independently, where all _Xi_ and _Yi_ take values in R. You may assume, without proving, that ( _S_ ( _X_ ) _, S_ ( _Y_ )) is complete sufficient for the full model.

- (a) Define the estimand _g_ ( _P, Q_ ) = P _X∼P,Y ∼Q_ ( _X > Y_ ), i.e. the probability that an observation from _P_ is larger than an independent observation from _Q_ . Find the UMVU estimator for _g_ ( _P, Q_ ) and explain why it is UMVU.

- (b) Define _µ_ = E _P X_ , _ν_ = E _QY_ , _σ_<sup>2</sup> = Var _P_ ( _X_ ), and _τ_<sup>2</sup> = Var _Q_ ( _Y_ ). Show that _T_ ( _X, Y_ ) = ( _X/Y_ )<sup>2</sup> is a consistent estimator for _θ_ = ( _µ/ν_ )<sup>2</sup> as _n →∞_ , assuming _ν >_ 0 and _σ_<sup>2</sup> _, τ_<sup>2</sup> _∈_ (0 _, ∞_ ).

- (c) Give the asymptotic distribution of _T_ ( _X, Y_ ) as _n →∞_ , appropriately normalized so that the error has a nondegenerate distribution, and justify your answer. Your answer should be given as a distribution whose parameters are explicit functions of _µ, ν, τ_<sup>2</sup> _, σ_<sup>2</sup> _,_ and _θ_ .

- (d) (*) If _µ_ = _ν_ = 0, give the asymptotic distribution of _T_ ( _X, Y_ ) as _n →∞_ , normalized appropriately if necessary. Justify your answer.

11

---

[← Problem 2 answers continued (3)](10-problem-2-answers-continued-3.md) · [Up: contents](index.md) · [Problem 3 answers continued (1) →](12-problem-3-answers-continued-1.md)
