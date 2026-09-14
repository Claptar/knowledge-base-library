---
title: 27 Lecture 27
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 27 Lecture 27

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall spend today’s lecture on uniform Bayes risk lower bounds in multi-hypotheses testing problems. It turns out (as will be seen in the next lecture) that the minimax risk in general decision theoretic problems can always be bounded from below by this testing risk and this is quite useful for establishing rate minimaxity.

## **27.1 The Multi-Hypothesis Testing Problem**

Suppose we observe data _X_ taking values in a space _X_ (as usual, _X_ can be a vector, matrix, function etc.). We have the following _N_ hypotheses for the distribution of _X_ :


Here _P_ 1 _, . . . , PN_ are probability measures on _X_ . We need to choose one of these hypotheses based on the observation _X_ . A test _T_ is any function from _X_ to _{_ 1 _, . . . , N }_ . Given a test _T_ , its type _i_ error is defined

145

by _Pi{T̸_ = _i}_ for _i_ = 1 _, . . . , n_ . We shall evaluate tests by the average of their type _i_ errors for _i_ = 1 _, . . . , N_ . Specifically, let


One can treat this problem in the general decision-theoretic framework by taking Θ = _A_ = _{_ 1 _, . . . , N }_ and _L_ ( _θ, a_ ) = _I{θ̸_ = _a}_ . In this case, _R_ ( _T_ ) will simply be the average risk of the test _T_ averaged with respect to the discrete uniform prior on Θ.

It is easy to see (shown below) that the test _T_<sup>_∗_</sup> which minimizes _R_ ( _T_ ) is given by the maximum likelihood test. To see this, let _pi_ denote the density of _Pi_ with respect to a common dominating measure _µ_ . We can then write


It is easy to see then that for every test _T_ and _x ∈X_ , we have


with equality being achieved for the maximum likelihood test defined by _T_<sup>_∗_</sup> ( _x_ ) := argmax1 _≤i≤N pi_ ( _x_ ). This proves that _T_<sup>_∗_</sup> minimizes _R_ ( _T_ ) and also that


It is usually difficult to compute _B_ ( _P_ 1 _, . . . , PN_ ) exactly. We shall focus on obtaining lower bounds for _B_ ( _P_ 1 _, . . . , PN_ ). As will be seen later, these lower bounds will yield lower bounds on the minimax risk in general decision theoretic problems.

In order to motivate lower bounds for _B_ := _B_ ( _P_ 1 _, . . . , PN_ ), let us first provide an intuitive meaning for _B_ . Because _B_ is the smallest possible average error (Bayes risk) in the testing problem, it should be clear that it measures, in some sense, the degree of separation between the probability measures _P_ 1 _, . . . , PN_ . Indeed, if _P_ 1 _, . . . , PN_ are far from each other, the testing problem should be easier and _B_ will be small. On the other hand, if _P_ 1 _, . . . , PN_ are close to each other, the testing problem will be harder and _B_ will be large. Note also that we always have


so that


Also, it is easy to see that the _B_ ( _P_ 1 _, . . . , PN_ ) takes the maximum possible value 1 _−_ (1 _/N_ ) when _P_ 1 = _· · ·_ = _PN_ . This makes sense because when _P_ 1 = _· · ·_ = _PN_ , identifying _i_ based on _X ∼ Pi_ is impossible and hence the testing Bayes risk _B_ ( _P_ 1 _, . . . , PN_ ) takes its maximum possible value.

On the other hand, _B_ ( _P_ 1 _, . . . , PN_ ) takes its minimum value of 0 when _P_ 1 _, . . . , PN_ are mutually singular (so that max _i pi_ = _p_ 1 + _. . . pN_ almost surely w.r.t _µ_ ). In this case, one can perfectly identify _i_ based on _X ∼ Pi_ so that the testing Bayes risk is at its lowest possible value.

The intuition that _B_ ( _P_ 1 _, . . . , PN_ ) measures the degree of separation between _P_ 1 _, . . . , PN_ suggests that we can bound it via other natural quantities for measuring the degree of separation or spread of _P_ 1 _, . . . , PN_ . For real numbers _a_ 1 _. . . . , aN_ , the most natural way of measuring their spread is their variance:


146

We can try to extend this idea to probability measures by defining


_D_ here refers to a notion of discrepancy/divergence between probability measures (analogous to the squared Euclidean distance between real numbers). Various choices for _D_ are possible but the most common one is the Kullback-Leibler divergence. Given two probability measures _P_ and _Q_ having densities _p_ and _q_ respectively with respect to a common dominating measure _µ_ , the Kullback-Leibler divergence between them is defined as


Based on the above discussion, it should be clear that there should be some connection between _B_ ( _P_ 1 _, . . . , PN_ ) and _I_ ( _P_ 1 _, . . . , PN_ ) (because both are measuring the spread or degree of separation between _P_ 1 _, . . . , PN_ ). The following lemma describes a simple relation between the two. This is often used in the statistics literature to prove Minimax Lower Bounds where it is referred to as Fano’s Inequality or Fano’s lemma. In fact, this is a weaker form of Fano’s inequality; there is a stronger version which we shall describe later today.

**Lemma 27.1.** _The following inequality holds for every N ≥_ 1 _and probability measures P_ 1 _, . . . , PN :_


_Proof of Lemma 27.1._ This elegant proof is due to Kemperman [13, Page 135].

Using the formula (245) for _B_ ( _P_ 1 _, . . . , PN_ ) and the definition of _I_ ( _P_ 1 _, . . . , PN_ ), it is clear that (247) is equivalent to


It is easy to see that this is further equivalent to (multiplying both sides above by _N_ log _N_ and using � (<sup>�</sup> _i_<sup>_pi_)</sup><sup>_dµ_=</sup><sup>_N_),</sup>

which is identical to


To prove this, it is obviously enough to prove the following fact involving nonnegative real numbers. For every set of nonnegative real numbers _a_ 1 _, . . . , aN_ , the following inequality holds:


To prove this inequality, note first that we can assume, without loss of generality,<sup>�</sup><sup>_N_</sup> _i_ =1<sup>_ai_=1(sothat</sup> _a_ 1 _, . . . , aN_ becomes a probability vector) and that _a_ 1 = max _i ai_ . Inequality (248) is then equivalent to


and this be rearranged as


147

The above inequality is true because (note that 2 _N ≥_ 2( _N −_ 1))


This completes the proof of (248) which gives (247).

## **27.2 Mutual Information**

The quantity _I_ ( _P_ 1 _, . . . , PN_ ) (defined in (246)) is known as _Mutual Information_ . Mutual Information is a term coming from information theory. It is usually defined for a pair of random variables _Y_ and _Z_ . Formally, the mutual information _I_ ( _Y, Z_ ) between _Y_ and _Z_ is defined as the Kullback-Leibler divergence between the joint distribution of _Y_ and _Z_ and the product of the marginal distributions of _Y_ and _Z_ . Specifically,


Consider now two random variables Θ and _X_ such that Θ is uniformly distributed on _{_ 1 _, . . . , N }_ and the conditional distribution of _X_ given Θ = _i_ is _Pi_ . Then it is easy to see that


Thus _I_ ( _P_ 1 _, . . . , PN_ ) defined as in (246) is just the mutual information between Θ and _X_ . For this reason, _I_ ( _P_ 1 _, . . . , PN_ ) is referred to as the mutual information term. Fano’s inequality therefore gives a bound for the Bayes risk in terms of Mutual Information.

The following fact about _I_ ( _P_ 1 _, . . . , PN_ ) will be useful in the sequel.

**Lemma 27.2.** _For every N ≥_ 1 _and probability measures P_ 1 _, . . . , PN , we have_


_where the infimum is taken over all probability measures Q._

_Proof._ The proof is simple and based on the following identity:


which is a consequence of:


Here _p_ ¯ = ( _p_ 1 + _· · ·_ + _pN_ ) _/N_ is the density of _P_<sup>¯</sup> with respect to _µ_ and _q_ is the density of _Q_ with respect to _µ_ .

## **27.3 Application to Sparse Normal Mean Estimation**

Fix _n ≥_ 1 and let _Pi_ be the _Nn_ ( _τei, In_ ) distribution for _i_ = 1 _, . . . , n_ . Here _τ_ is a positive real number that depends on _n_ and _ei_ is the vector with 1 in the _i_<sup>_th_</sup> position and 0 elsewhere. We are interested in _B_ := _B_ ( _P_ 1 _, . . . , Pn_ ) and how it depends on _n_ and _τ_ . Fano’s inequality (specifically inequality (247)) gives


148

To get an explicit bound from here, we need upper bounds for _I_ . Here Lemma 27.2 is very useful because it states that


for every probability measure _Q_ . A natural choice for _Q_ which enables explicit computation is _Q_ = _Nn_ (0 _, In_ ). We then obtain (using the fact that _D_ ( _Nn_ ( _µ_ 1 _,_ Σ) _∥Nn_ ( _µ_ 2 _,_ Σ)) = ( _µ_ 1 _− µ_ 2)<sup>_T_</sup> Σ<sup>_−_1</sup> ( _µ_ 1 _− µ_ 2) _/_ 2)

This allows us to deduce that


This gives interesting corollaries such as:


However, inequality (251) is not strong enough to yield anything nontrivial when _τ_ is close to _λn_ :=<sup>_√_</sup> 2 log _n_ . For example, when _τn_ := _λn −_ log( _λn_ ), then (251) does not give anything useful. However, by a direct calculation (as shown below), it can be shown that


This shows an important weakness of using Fano’s inequality to obtain lower bounds for _B_ . To prove (252), first note that


From this, we can obtain

Thus if _z_ 1 _, . . . , zn_ are independent standard normal random variables, then


To further bound this from below, we need to bound E max _i e_<sup>_τzi_</sup> from above which we do in the following way (recall _λn_ =<sup>_√_</sup> 2 log _n_ ):


Note that the last inequality above (the Mill’s ratio bound) requires that _τ < λ_ . We thus get


For _τ_ = _λ −_ log( _λ_ ), we have _λ − τ →∞_ as _n →∞_ and then, from the above, we immediately obtain (252).

149

## **27.4 Fano’s Lemma via the Data Processing Inequality**

The Data Processing Inequality is a standard fact about the Kullback-Leibler divergence. It states the following. Suppose _P_ and _Q_ are two probability measures on a space _X_ . Let Γ : _X →Y_ be any function. Let _P_ Γ<sup>_−_1</sup> denote the image of the probability measure _P_ under the map Γ i.e.,


Similarly define _Q_ Γ<sup>_−_1</sup> . The Data Processing Inequality then states that


This is true for every pair of probability measures _P_ and _Q_ and every function Γ. We will not give a proof of this fact here (this is standard and can be found in many places). We shall outline a simple proof of Fano’s inequality in Lemma 27.1 (actually we shall derive a stronger version of Fano’s inequality than in (247)) via the Data Processing Inequality.

Consider the setting of Fano’s inequality where we have _N_ probability measures _P_ 1 _, . . . , PN_ on a space _X_ having densities _p_ 1 _, . . . , pN_ respectively with respect to _µ_ . Consider two random variables Θ and _X_ such that Θ is uniformly distributed on _{_ 1 _, . . . , N }_ and the conditional distribution of _X_ given Θ = _i_ is _Pi_ . Let P be the joint distribution of Θ and _X_ . Also let Q be the joint distribution that is the product of the marginal distributions of Θ and _X_ . We have seen (in (249)) that


Now fix a test _T_ i.e., _T_ is a function from _X_ to _{_ 1 _, . . . , N }_ . We will then apply the Data Processing Inequality to the map Γ : _{_ 1 _, . . . , N } × X →{_ 0 _,_ 1 _}_ defined by


The Data Processing Inequality will then give


It is now easy to see that


and


We have therefore proved that for every test _T_ ,


Because this is true for every test _T_ , we can take _T_ = _T_<sup>_∗_</sup> (the maximum likelihood test which minimizes _R_ ( _T_ ) over all _T_ ) so that _R_ ( _T_<sup>_∗_</sup> ) = _B_ = _B_ ( _P_ 1 _, . . . , PN_ ). This will then give


150

This inequality can be treated as a stronger version of Fano’s inequality. It is easy to prove that (253) implies (247). To see this, just note that the right hand side of (253) equals:


because inf _x∈_ (0 _,_ 1) ( _x_ log _x_ + (1 _− x_ ) log(1 _− x_ )) = _−_ log 2 and log( _N/_ ( _N −_ 1)) _≥_ 0.

An important advantage of this proof of Fano’s inequality (via the Data Processing Inequality) is that it generalizes to _f_ -divergences. _f_ -divergences are a general class of divergences between probability measures that include the Kullback-Leibler divergence as a special case. They are defined in the following way. Let _f_ : (0 _, ∞_ ) _→_ R be a convex function with _f_ (1) = 0. It is then easy to show that the following limits exist (even though they may be + _∞_ . Suppose _P_ and _Q_ are two probability measures on a space _X_ having densities _p_ and _q_ with respect to a common dominating measure _µ_ . The _f_ -divergence between _P_ and _Q_ is denoted by _Df_ ( _P ∥Q_ ) and is defined in the following way:


Different choices of _f_ lead to different specific divergences. For example, KL divergence corresponds to _f_ ( _x_ ) = _x_ log _x_ , total variation distance corresponds to _f_ ( _x_ ) = _|x−_ 1 _|/_ 2, squared Hellinger distance corresponds to _f_ ( _x_ ) = 1 _−_<sup>_√_</sup> _<u>x</u>_ or _f_ ( _x_ ) = (<sup>_√_</sup> _<u>x −</u>_ 1)<sup>2</sup> _/_ 2, chi-squared divergence corresponds to _f_ ( _x_ ) = _x_<sup>2</sup> _−_ 1 and so on.

It turns out that the data processing inequality is satisfied for every _f_ -divergence. Using this, it is possible to prove the following generalization of Fano’s inequality for every _f_ -divergence:


With specific choices for _f_ , this leads to more explicit lower bounds for _B_ . For example, for _f_ ( _x_ ) = _x_<sup>2</sup> _−_ 1, one obtains


where _χ_<sup>2</sup> ( _P ∥Q_ ) = _Df_ ( _P ∥Q_ ) for _f_ ( _x_ ) = _x_<sup>2</sup> _−_ 1. See Gushchin [10] or Guntuboyina [9] and Chen et al. [4] for more details.

---

[← 26 Lecture 26](27-26-lecture-26.md) · [Up: contents](index.md) · [28 Lecture 28 →](29-28-lecture-28.md)
