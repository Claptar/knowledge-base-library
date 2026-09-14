---
title: 9 Lecture Nine
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 9 Lecture Nine

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.1 Normal Approximation for the Binomial: CLT**

In the last class, we studied the normal approximation to the Binomial. We proved that


46

This approximation is not always good. It is only accurate when _f_ := _k/n_ is closed to _p_ . More precisely, we argued in the last class that the approximation is good provided


is small. Note the presence of _n_ in the numerator above. This means that, for the approximation to be accurate, _f_ needs to be much closer to _p_ when _n_ is large.

The normal approximation of the binomial is usually stated in the form of the **De MoivreLaplace Central Limit Theorem** as discussed below.

#### **9.1.1 De Moivre-Laplace Central Limit Theorem**

**Fact 9.1.** _Let X ∼ Bin_ ( _n, p_ ) _with fixed_ 0 _< p <_ 1 _. For every fixed pair of real numbers a and b with a < b, we have_


Here is a sketch of the proof of (37). First write


The key now is to observe that, in the range _k ∈_ � _np_ + _a_ ~~�~~ _np_ (1 _− p_ ) _, np_ + _b_ ~~�~~ _np_ (1 _− p_ )�, the normal approximation is accurate. To see this, first note that


As a result, _|f − p|_ is at most of order _n_<sup>_−_1</sup><sup>_/_2</sup> which implies that _n|f − p|_<sup>3</sup> will be of order _n_<sup>_−_1</sup><sup>_/_2</sup> and thus small (the denominator in (36) will behave like a constant as _p_ is fixed away from 0 and 1 and _f_ is close to _p_ ). As a result, we can use the approximation (35) to write


Using the formula

we get

so that

47

Let us now write

Thus


The left hand side above is a Riemann sum for � _ab_<sup>_φ_(</sup><sup>_z_)</sup><sup>_dz_anditapproachesthatintegralas</sup> _n →∞_ (note that _zk − zk−_ 1 _→_ 0 as _n →∞_ ). This proves (37).

The statement (37) is also true if _a_ = _−∞_ and/or _b_ = + _∞_ . This can be derived as a consequence of (37) for finite _a_ and _b_ . This argument is technical and omitted; if interested, see Corollary 3.2 of the book _Probability Theory_ by Yakov G. Sinai.

### **9.2 The Exponential Distribution**

The exponential distribution is given by the exponential density. The exponential density with rate parameter _λ >_ 0 (denoted by _Exp_ ( _λ_ )) is given by


It is arguably the simplest density for modeling random quantities that are constrained to be nonnegative. It is used to model things such as the time of the first phone call that a telephone operator receives starting from now. This can be justified by a discretization argument as follows.

Suppose we divide the time starting now into a large number of small intervals each of length _δ_ . In each time interval, assume that there can be at most one phone call and that the probability of a phone call is a small real number _p_ . Also assume independence of getting phone calls in distinct time intervals. In this setup, suppose _X_ is the random variable denoting the time of the first phone call. For a positive real number _x_ ,


is the probability that there is no phone call in the first _x/δ_ time intervals and that there is a phone call in the (1 + ( _x/δ_ ))<sup>_th_</sup> interval. Thus


The quantity _p_ is quite small so we can use the approximation 1 _− p ≈ e_<sup>_−p_</sup> . This gives


Now the quantity<sup>_<u>p</u>_</sup> _δ_<sup>istheaveragenumberofphonecallsinunittime(notethatthereare</sup> 1 _/δ_ intervals in unit time). This can therefore be termed as the “rate” of arrival of phone calls:


We can then write

P _{x ≤ X < x_ + _δ} ≈ δλ_ exp ( _−λx_ )

which is same as


48

for _x >_ 0.

Observe also that in the above setup, the distribution of the number of phone calls in any time interval of length _T_ is _Bin_ ( _T/δ, p_ ) (as the number of small time intervals each of length _δ_ in the original time interval of length _T_ equals _T/δ_ ). The quantity


which is small if _δ_ is small and _T_ and _λ_ are held fixed. The Poisson approximation holds and we can approximate the distribution of the number of phone calls in any time interval of length _T_ as _Poi_ ( _T_<sup>_<u>p</u>_</sup> _δ_<sup>) =</sup><sup>_Poi_(</sup><sup>_λT_).</sup>

Also, by the assumption of independence, the number of phone calls in _disjoint_ time intervals will be independent.

These two assumptions (Poisson distribution of arrivals in any time interval and independence of number of arrivals in disjoint time intervals) are characteristic of the Poisson process. We have therefore assumed that the phone call arrivals form a Poisson process. The waiting time for the first phone call then is Exponentially Distributed.

The exponential density has the memorylessness property (just like the Geometric distribution in the discrete case). To see this, first note that


which gives


The property


is called memorylessness.

The exponential density is the only density on (0 _, ∞_ ) that has the memorylessness property (proof left as exercise). In this sense, the Exponential distribution can be treated as the continuous analogue of the Geometric distribution. Note that a Geometric random variable would satisfy (38) when _a, b_ are integers but not when _a, b_ are arbitrary real numbers.

### **9.3 The Gamma Distribution**

It is customary to talk about the Gamma density after the exponential density. The Gamma density with shape parameter _α >_ 0 and rate parameter _λ >_ 0 is given by


To find the proportionality constant above, we need to evaluate

Now the function


49

is called the Gamma function in mathematics. So the constant of proportionality in (39) is given by


so that the Gamma density has the formula:


We shall refer to this as the _Gamma_ ( _α, λ_ ) density.

Note that the _Gamma_ ( _α, λ_ ) density reduces to the _Exp_ ( _λ_ ) density when _α_ = 1. Therefore, Gamma densities can be treated as a generalization of the Exponential density. In fact, the Gamma density can be seen as the continuous analogue of the negative binomial distribution because if _X_ 1 _, . . . , Xk_ are independent _Exp_ ( _λ_ ) random variables, then _X_ 1 + _· · ·_ + _Xn ∼ Gamma_ ( _k, λ_ ) (thus the Gamma distribution arises as the sum of i.i.d exponentials just as the Negative Binomial distribution arises as the sum of i.i.d Geometric random variables).

Here are some elementary properties of the Gamma function that will be useful to us later. The Gamma function does not have a closed form expression for arbitrary _α >_ 0. However when _α_ is a positive integer _k_ , it can be shown that


The above inequality is a consequence of the property


and the trivial fact that Γ(1) = 1. You can easily verify (41) by integration by parts.

Another easy fact about the Gamma function is that Γ(1 _/_ 2) =<sup>_√_</sup> _<u>π</u>_ (this is a consequence of the fact that � _e_<sup>_−x_2</sup><sup>_/_2</sup> _dx_ = _√_ 2 _π_ ).

When _α_ = _k_ is a positive integer, the Γ( _k, λ_ ) distribution arises as the distribution of the _k_<sup>_th_</sup> arrival in a Poisson process of rate _λ_ . To see, consider the same binomial setup (that we used for the modeling the arrivals of phone calls in the previous section). Then if _X_ denotes the waiting time for the _k_<sup>_th_</sup> phone call, then (for _x >_ 0)


is the probability that there are exactly _k −_ 1 phone calls in the first _x/δ_ small time intervals (of length _δ_ ) and an additional phone call in the ( _x/δ_ + 1)<sup>_th_</sup> interval. Thus


If _x_ and _k_ are fixed, then _x/δ_ is much larger than _k −_ 1 so we can approximate the right hand side above as (also as _p_ is small)


Now using 1 _− p ≈ e_<sup>_−p_</sup> and writing _λ_ = _p/δ_ ,


which means that _X_ has the _Gamma_ ( _k, λ_ ) density.

50

### **9.4 Variable Transformations**

It is often common to take functions or transformations of random variables. Consider a random variable _X_ and apply a function _u_ ( _·_ ) to _X_ to transform _X_ into another random variable _Y_ = _u_ ( _X_ ). How does one find the distribution of _Y_ = _u_ ( _X_ ) from the distribution of _X_ ?

If _X_ is a discrete random variable, then _Y_ = _u_ ( _X_ ) will also be discrete and then the pmf of _Y_ can be written directly in terms of the pmf of _X_ :


If _X_ is a continuous random variable with density _fX_ and _T_ ( _·_ ) is a smooth function, then it is fairly straightforward to write down the density of _Y_ = _T_ ( _X_ ) in terms of _fX_ . In the case when _T_ is invertible and _T_<sup>_−_1</sup> is differentiable, there is the following formula:


We shall look at the ideas behind this formula (as well how to solve this problem when _T_ is not invertible) in the next class. We will look at the following problem in the next class.

**Example 9.2.** _Suppose X ∼ U_ ( _−π/_ 2 _, π/_ 2) _. What is the density of Y_ = tan( _X_ ) _? We shall prove, in the next class, that Y has the_ **_Cauchy_** _density:_

---

[← 8 Lecture Eight](09-8-lecture-eight.md) · [Up: contents](index.md) · [10 Lecture Ten →](11-10-lecture-ten.md)
