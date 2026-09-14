---
title: 15 Lecture 15
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 15 Lecture 15

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we were studying the performance of estimators of the form:


under the model _Y_ = _θ_<sup>_∗_</sup> + _ϵ_ with _ϵ ∼ N_ (0 _, In_ ). Here _f_ : R<sup>_n_</sup> _→_ R is a convex function.

For this estimator, we remarked last time that the following inequality is true:


This inequality is due to Oymak and Hassibi [17]; it has a simple proof which is given below.

## **15.1 Proof of Inequality** (119)

Let _g_ ( _θ_ ) := _∥y − θ∥_<sup>2</sup> _/_ 2+ _λf_ ( _θ_ ) for _θ ∈_ R<sup>_n_</sup> . The statement that _θ_<sup>ˆ</sup> _λ,f_ minimizes _g_ is equivalent to the statement that 0 _∈ ∂g_ ( _θ_<sup>ˆ</sup> _λ,f_ ) (this is trivial because _θ_<sup>ˆ</sup> _λ,f_ minimizing _g_ is equivalent to _g_ ( _θ_ ) _≥ g_ ( _θ_<sup>ˆ</sup> _λ,f_ ) + �0 _, θ − θ_<sup>ˆ</sup> _λ,f_ �). It is now easy to check that

so that we have

or equivalently


We now use Lemma 15.1 below to deduce that for every _s ∈ ∂f_ ( _θ_<sup>_∗_</sup> ), we have


Writing _Y_ = _θ_<sup>_∗_</sup> + _ϵ_ , we obtain


76

The Cauchy-Schwarz inequality can be used on the right hand side above which will give:


This is true for every _s ∈ ∂f_ ( _θ_<sup>_∗_</sup> ) so we can take an infimum over all such _s_ and deduce


which completes the proof of inequality (119).

**Lemma 15.1.** _Let f_ : R<sup>_n_</sup> _→_ R _be a convex function. Then for every θ_ 1 _, θ_ 2 _∈_ R<sup>_n_</sup> _and s_ 1 _∈ ∂f_ ( _θ_ 1) _, s_ 2 _∈ ∂f_ ( _θ_ 2) _, we have_

_Proof._ By the definition of subgradients, we have


Adding these two inequalities results in (120).

## **15.2 Application of** (119) **to** _f_ ( _x_ ) = _∥x∥_ 1

In the last lecture, we applied (119) to the situation when _f_ ( _x_ ) = _∥x∥_ 1 = _|x_ 1 _|_ + _· · ·_ + _|xn|_ and argued that


where


We now proceed via (below _φ_ ( _x_ ) = (2 _π_ )<sup>_−_1</sup><sup>_/_2</sup> _e_<sup>_−x_2</sup><sup>_/_2</sup> is the standard Gaussian density)


We now apply integration by parts in the first integral above (with _u_ = _x_ and _dv_ = _xφ_ ( _x_ ) _dx_ ), evaluate the second integral in closed form and leave the third integral as is to obtain


77

to obtain


Using this in (121), we obtain


which implies, via inequality (119),


If we now make the choice


we obtain the risk bound


as _n →∞_ provided _k/n →_ 0. Thus the LASSO with the penality (124) achieves the risk 2 _k_ log( _n/k_ ).

Note that if the locations of the non-zero entries in _θ_<sup>_∗_</sup> are known, then the naive estimator which estimates the non-zero entries by _Yi_ and the zero entries by 0 with achieve risk equal to _k_ . This, in relation to (125), means that the LASSO with tuning (124) is paying a price of 2 log( _n/k_ ) for not knowing the non-zero locations. We shall later prove that every estimator will have to pay this price in a minimax sense. This is not too hard to see intuitively. For example, if _k_ = 1 and the magnitude of the non-zero signal is<sup>_√_</sup> _c_ log _n_ for some _c <_ 2, then the noise in the data will drown the signal so every estimator will most likely miss the signal and incur a loss of _c_ log _n_ . We shall make this precise later.

In order to use the choice (124) for the tuning parameter _λ_ , we need knowledge of _k_ . One can instead use


which does not depend on _k_ . With this choice, the bound (123) gives


which is only slightly worse compared to (125). If _k_ is of constant order, then there is not much difference between (125) and (127) but for _k_ = _n/_ (log _n_ ), there is a difference.

The bound (123) for the LASSO can actually be derived by a more direct method without relying on the inequality (119). This is because the estimator can be written in closed form via the soft thresholding operator. This is done next.

## **15.3 Soft Thresholding**

The estimator


78

can be written in closed form. Indeed observe first that if _θ_<sup>ˆ</sup> _λ_ = ( _θ_<sup>ˆ</sup> _λ_ (1) _, . . . , θ_<sup>ˆ</sup> _λ_ ( _n_ )), then


The function _Q_ ( _θi_ ) := ( _Yi − θi_ )<sup>2</sup> _/_ 2 + _λ|θi|_ is convex and


The derivative _Q_<sup>_′_</sup> ( _θi_ ) is therefore piecewise linear with positive slope except for an upward jump of 2 _λ_ at _θi_ = 0. Thus, _Q_<sup>_′_</sup> ( _θi_ ) has exactly one sign change from negative to positive at a single point which must therefore be the minimizing value of _Q_ ( _θi_ ). Depending on the value of _Yi_ , this crossing point is positive, zero or negative, and we can then check that


In other words,


Using this, we can directly study the risk of _θ_<sup>ˆ</sup> _λ_ as follows:


where


This quantity _rS_ ( _λ, µ_ ) is the risk of the soft thresholding estimator (at threshold _λ_ ) in the univariate problem with data _y ∼ N_ ( _µ,_ 1). We can explicitly write this as


The following are some basic properties of _rS_ ( _λ, µ_ ):

1. The function _µ �→ rS_ ( _λ, µ_ ) is increasing on [0 _, ∞_ ). This is intuitive and easy to check via the calculation:


which is positive when _µ >_ 0.

2. When _µ_ = 0, we have


We proved this in (122).

79

3. When _µ_ approaches _±∞_ , the risk _rS_ ( _λ, µ_ ) behaves like 1 + _λ_<sup>2</sup> :


I will leave this as an exercise to prove this. Intuitively, this is obvious since for large _µ_ , most likely soft _λ_ ( _y_ ) = _y − λ_ and E( _y − λ − µ_ )<sup>2</sup> = 1 + _λ_<sup>2</sup> . Combined with the fact that _µ �→ rS_ ( _λ, µ_ ) is increasing on [0 _, ∞_ ), we can deduce that


These facts imply that, compared to the naive estimator _y_ , the risk of the soft thresholding estimator is much smaller at _µ_ = 0 while its worst case risk is larger. Therefore, it makes sense to use it only when it is believed that _µ_ is zero or small.

Using the above observations, we can give an alternative proof of the risk bound (123) for LASSO. Indeed, we can write


Using the second and third facts above, we obtain


This proves (123) which, we have seen in the last subsection, allows us to deduce the rate results (125) and (127) under the choices (124) and (126) for the tuning parameter _λ_ respectively.

Note that in the above bound, we used


whenever _θi_<sup>_∗_</sup> _̸_<sup>=0.Ifmoreinformationisprovidedaboutthe</sup><sup>_θ∗_,thenthismightnotbeaverygoodbound.</sup> For example, it is common to also study the performance of LASSO under the assumption:


for some _Cn >_ 0. Under this assumption, potentiall all of the _θi_<sup>_∗_’scanbenon-zerosothatuseof(130)</sup> will give very poor bounds. Note that, even though under (131), all entries of _θ_<sup>_∗_</sup> can be non-zero, they have to satisfy the property that the _j_<sup>_th_</sup> largest entry in absolute value (to be denoted by _|θ_<sup>_∗_</sup> _|_ ( _j_ )) should be bounded by _Cn/j_ . This means that the entries of _θ_<sup>_∗_</sup> have to satisfy a certain decay. The assumption (131) can therefore be considered to be some form of _weak sparsity_ assumption on _θ_<sup>_∗_</sup> .

Let us now study the risk of _θ_<sup>ˆ</sup> _λ_ under the assumption (131). As mentioned earlier, we need some bound for _rS_ ( _λ, µ_ ) for _µ̸_ = 0 that is better than 1 + _λ_<sup>2</sup> . For this, we use inequality (128) to write


which gives


80

Combining this with (129), we deduce

_rS_ ( _λ, µ_ ) _≤ rS_ ( _λ,_ 0) + min( _µ_<sup>2</sup> _,_ 1 + _λ_<sup>2</sup> ) _._

This implies that the risk of LASSO is bounded by


We shall further bound this under the assumption (131). Because min( _a_<sup>2</sup> _, b_<sup>2</sup> ) _≤ ab_ for _a, b ≥_ 0, we obtain


The choice _λ_ =<sup>_√_</sup> 2 log _n_ will now lead to


This further gives


If, for example, _Cn_ ≲<sup>_√_</sup> _<u>n</u>_ <u>,</u> then the bound above becomes ~~�~~ (log _n_ ) _/n_ . We shall see later that this rate is minimax under the assumption (131).

---

[← 14 Lecture 14](15-14-lecture-14.md) · [Up: contents](index.md) · [16 Lecture 16 →](17-16-lecture-16.md)
