---
title: 1. One Poisson, two Poissons (30 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2020.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/final2020.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. One Poisson, two Poissons (30 points, 5 points / part).

**Source:** [`old-exams/final2020.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2020.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts / notation for this problem:

- For _θ >_ 0, the Poisson density for _X ∼_ Pois( _θ_ ) is<sup>_<u>θx</u>_</sup> _x_<sup>_<u>e</u>_</sup> !<sup>_−θ_</sup> on _x_ = 0 _,_ 1 _, . . ._ . The mean and variance are both _θ_ .

- Let _P_ ( _n_ ) denote the set of integers 0 _≤ i ≤ n_ with the same parity (odd/even) as _n_ , i.e. for which _n − i_ is even:


so for example _P_ (10) = _{_ 0 _,_ 2 _,_ 4 _,_ 6 _,_ 8 _,_ 10 _}_ while _P_ (9) = _{_ 1 _,_ 3 _,_ 5 _,_ 7 _,_ 9 _}_ .

Suppose we observe two independent random variables, with

_X ∼_ Pois( _θ_ ) _,_ and _Y ∼_ Pois( _θ_<sup>2</sup> ) _,_

where _θ >_ 0 is an unknown parameter.

- (a) Show that the model is an exponential family and find its complete sufficient statistic.

- (b) Give an explicit expression for the UMVU estimator of _θ_ . Evaluate it when _X_ = _Y_ = 2 (give your answer as a fraction, or a decimal with at least 3 significant digits).

- (c) Now suppose that you observe an i.i.d. sample of _n_ pairs ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) where each pair has the same distribution specified above. That is, _Xi ∼_ Pois( _θ_ ) and _Yi ∼_ Pois( _θ_<sup>2</sup> ), independently. Give an explicit expression for the MLE _θ_<sup>ˆ</sup> _n_ as a function of the data.

If<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_= �</sup><sup>_n_</sup> _i_ =1<sup>_Yi_=2</sup><sup>_n_,findtheMLEfor</sup><sup>_θ_(giveyouranswerasa</sup> fraction, or a decimal with at least 3 significant digits).

- (d) Find the asymptotic distribution of _θ_<sup>ˆ</sup> _n_ as _n →∞_ . (Don’t worry about checking any regularity conditions for this part).

- (e) A simpler estimator for _θ_ is


where _X n_ = _n_<sup>_−_1 �</sup><sup>_n_</sup> _i_ =1<sup>_Xi_and</sup> _Y n_ = _n_<sup>_−_1 �</sup><sup>_n_</sup> _i_ =1<sup>_Yi_.</sup>

Find the asymptotic distribution of this estimator. Justify why it has the distribution you say and give its asymptotic relative efficiency.

2

- (f) Now suppose we want to test our model against the alternative hypothesis that ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) are still i.i.d. pairs of independent Poisson random variables, but their means do not have the relationship we posited. In other words, in the expanded model


Test _H_ 0 : _λ_ = _θ_<sup>2</sup> against the alternative _H_ 1 : _λ̸_ = _θ_<sup>2</sup> , for large _n_ . Suggest an asymptotic test from class or homework: give an explicit expression for the test statistic and an explicit rejection cutoff in terms of a quantile of a known distribution. (If you choose a well-known test that is appropriate for this kind of setting then you do **not** need to justify why your test has the correct null distribution in this case).

( **Hint:** there are at least three choices of asymptotic tests from class or homework; it might pay off to take a moment to consider which is easiest to carry out here).

3

---

[← Prof. Will Fithian](02-prof-will-fithian.md) · [Up: contents](index.md) · [2. A problem of limited means (20 points, 5 points / part). →](04-2-a-problem-of-limited-means-20-points-5-points-part.md)
