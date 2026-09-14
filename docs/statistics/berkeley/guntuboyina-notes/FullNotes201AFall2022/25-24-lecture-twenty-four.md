---
title: 24 Lecture Twenty Four
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 24 Lecture Twenty Four

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **24.1 Central Limit Theorem (CLT)**

The following is the simplest version of the CLT.

**Theorem 24.1** (Central Limit Theorem) **.** _Suppose Xi, i_ = 1 _,_ 2 _, . . . are i.i.d with_ E( _Xi_ ) = _µ and var_ ( _Xi_ ) = _σ_<sup>2</sup> _< ∞. Then, with X_<sup>¯</sup> _n_ = ( _X_ 1 + _· · ·_ + _Xn_ ) _/n,_


_converges in distribution to N_ (0 _,_ 1) _. Convergence in distribution here means that_


Informally, the CLT says that for i.i.d observations _X_ 1 _, . . . , Xn_ with finite mean _µ_ and variance _σ_<sup>2</sup> , the quantity<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X_<sup>¯</sup> _n − µ_ ) _/σ_ is approximately (or asymptotically) _N_ (0 _,_ 1). Informally, the CLT also implies that

1.<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X_<sup>¯</sup> _n − µ_ ) is approximately _N_ (0 _, σ_<sup>2</sup> ).

2. _X_<sup>¯</sup> _n_ is approximately _N_ ( _µ, σ_<sup>2</sup> _/n_ ).

3. _Sn_ = _X_ 1 + _· · ·_ + _Xn_ is approximately _N_ ( _nµ, nσ_<sup>2</sup> ).

4. _Sn − nµ_ is approximately _N_ (0 _, nσ_<sup>2</sup> ).


It may be helpful here to note that


121

and also


The most remarkable feature of the CLT is that it holds regardless of the distribution of _Xi_ (as long as they are i.i.d from a distribution _F_ that has a finite mean and variance). Therefore the CLT is, in this sense, distribution-free. To illustrate the fact that the distribution of _Xi_ can be arbitrary, let us consider the following examples.

1. **Bernoulli** : Suppose _Xi_ are i.i.d Bernoulli random variables with probability of success given by _p_ . Then E _Xi_ = _p_ and _var_ ( _Xi_ ) = _p_ (1 _− p_ ) so that the CLT implies that _√n_ <u>(</u> _X_<sup>¯</sup> _n − p_ ) _/_ ~~�~~ _p_ (1 _− p_ ) is approximately _N_ (0 _,_ 1). This is actually called De Moivre’s theorem which was proved in 1733 before the general CLT. The general CLT stated above was proved by Laplace in 1810.

The CLT also implies here that _Sn_ is approximately _N_ ( _np, np_ (1 _− p_ )). We know that _Sn_ is exactly distributed according to the _Bin_ ( _n, p_ ) distribution. We therefore have the following result: When _p_ is fixed and _n_ is large, the Binomial distribution _Bin_ ( _n, p_ ) is approximately same as the normal distribution with mean _np_ and variance _np_ (1 _− p_ ).

2. **Poisson** : Suppose _Xi_ are i.i.d _Poi_ ( _λ_ ) random variables. Then E _Xi_ = _λ_ = _var_ ( _Xi_ ) so that the CLT says that _Sn_ = _X_ 1 + _· · ·_ + _Xn_ is approximately Normal with mean _nλ_ and variance _nλ_ . It is not hard to show here that _Sn_ is exactly distributed as a _Poi_ ( _nλ_ ) random variable (proved later). We deduce therefore that when _n_ is large and _λ_ is held fixed, _Poi_ ( _nλ_ ) is approximately same as the Normal distribution with mean _nλ_ and variance _nλ_ .

3. **Gamma** : Suppose _Xi_ are i.i.d random variables having the _Gamma_ ( _α, λ_ ) distribution. Check then that E _Xi_ = _α/λ_ and _var_ ( _Xi_ ) = _α/λ_<sup>2</sup> . We deduce then, from the CLT, that _Sn_ = _X_ 1+ _· · ·_ + _Xn_ is approximately normally distributed with mean _nα/λ_ and variance _nα/λ_<sup>2</sup> . We derived previously that _Sn_ is exactly distributed as _Gamma_ ( _nα, λ_ ). Thus when _n_ is large and _α_ and _λ_ are held fixed, the _Gamma_ ( _nα, λ_ ) is approximately closely by the _N_ ( _nα/λ, nα/λ_<sup>2</sup> ) distribution according to the CLT.

4. **Chi-squared** . Suppose _Xi_ are i.i.d chi-squared random variables with 1 degree of freedom i.e., _Xi_ = _Zi_<sup>2fori.i.dstandardnormalrandomvariables</sup><sup>_Z_1</sup><sup>_, Z_2</sup><sup>_, . . ._.</sup> It is easy to check then that _Xi_ is a _Gamma_ (1 _/_ 2 _,_ 1 _/_ 2) random variable. This gives that _X_ 1 + _· · ·_ + _Xn_ is exactly _Gamma_ ( _n/_ 2 _,_ 1 _/_ 2). This exact distribution of _X_ 1 + _· · ·_ + _Xn_ is also called the chi-squared distribution with _n_ degrees of freedom (denoted by _χ_<sup>2</sup> _n_<sup>).The</sup> CLT therefore implies that the _χ_<sup>2</sup> _n_<sup>distributioniscloselyapproximatedby</sup><sup>_N_(</sup><sup>_n,_2</sup><sup>_n_).</sup>

5. **Cauchy** . Suppose _Xi_ are i.i.d standard Cauchy random variables. Then _Xi_ ’s do not have finite mean and variance. Thus the CLT does not apply here. In fact, it can be proved here that ( _X_ 1 + _· · ·_ + _Xn_ ) _/n_ has the Cauchy distribution for every _n_ . A sketch of this proof is given later in this lecture.

### **24.2 CLT Proof strategy**

To prove the CLT, the natural idea is to write down some sort of formula for


and then see what happens to the formula as _n →∞_ . The problem with this approach is that the formula is a bit tricky to write (it depends on whether the random variables

122

are discrete or continuous, for example). Even if we assume that the random variables are discrete, the formula is a bit messy. For example, suppose that _X_ 1 _, X_ 2 _, . . ._ are i.i.d discrete random variables taking the values 0 _,_ 1 _,_ 2 _, . . ._ . Then


where _pj_ := P _{X_ 1 = _j}_ . Understanding the behaviour of this as _n_ gets large is a bit tricky.

For this reason, while dealing with sums of independent random variables, people usually work with certain transforms of distributions.

### **24.3 Transforms**

There are three commonly used transforms: _z_ -transform (also known as Probability Generating Function) for random variables taking values in _{_ 0 _,_ 1 _,_ 2 _, . . . }_ , Laplace transform (also known as Moment Generating Function), and the Fourier transform (also known as the Characteristic Function).

#### **24.3.1** _z_ **-Transform (Probability Generating Function)**

Suppose _X_ is a discrete random variable taking the values 0 _,_ 1 _,_ 2 _, . . ._ . The _z_ -transform of _X_ is defined as


Here is a simple example.

**Example 24.2.** _Suppose X takes the values_ 8 _,_ 13 _,_ 20 _,_ 29 _,_ 35 _with probabilities_ 0 _._ 3 _,_ 0 _._ 2 _,_ 0 _._ 15 _,_ 0 _._ 3 _,_ 0 _._ 05 _. Then the z-transform of X is given by_


In general _GX_ ( _z_ ) will be a complicated power series with many terms. In some cases however, the series corresponding to _GX_ ( _z_ ) can be summed explicitly to yield a simpler formula for _GX_ ( _z_ ) as in the next example.

**Example 24.3.** _Suppose X has the Poisson distribution with mean λ. Then_


Note that _GX_ ( _z_ ) uniquely determines the distribution of _X_ because


123

for every _k_ = 0 _,_ 1 _,_ 2 _, . . ._ .

The _z_ -transform (and all other transforms) have the important property that the transform for the sum of _n_ i.i.d random variables is simply the transform of the individual random variable raised to power _n_ . This is because:


The utility of this result for dealing with sums of i.i.d random variables can be found in the following two examples.

**Example 24.4.** _Suppose X_ 1 _, . . . , X_ 100 _are i.i.d with common distribution giving probabilities_ 0 _._ 3 _,_ 0 _._ 2 _,_ 0 _._ 15 _,_ 0 _._ 3 _,_ 0 _._ 05 _to the values_ 8 _,_ 13 _,_ 20 _,_ 29 _,_ 35 _with probabilities. What is the distribution of X_ 1 + _· · ·_ + _X_ 100 _?_

_X_ 1 + _· · ·_ + _X_ 100 _will be a discrete random variable taking many possible values. Specifying its distribution via the probability mass function will be tedious. But it is very easy to write down its z-transform as_


**Example 24.5.** _The following is a fundamental fact. The sum of n independent random variables X_ 1 _, . . . , Xn with Xi ∼ Poi_ ( _λi_ ) _for i_ = 1 _, . . . , n equals Poi_ ( _λ_ 1 + _· · ·_ + _λn_ ) _. This can be very easily proved using z-transforms (and the fact that the z-transform of Poi_ ( _λ_ ) _equals_ exp( _λ_ ( _z −_ 1)) _) because_


_Thus the z-transform of X_ 1 + _· · ·_ + _Xn coincides with that of Poi_ ( _λ_ 1 + _· · ·_ + _λn_ ) _which implies that X_ 1 + _· · ·_ + _Xn has the Poi_ ( _λ_ 1 + _· · ·_ + _λn_ ) _distribution._

While the _z_ -transform makes dealing with independent sums convenient, it is not a general tool as it is only defined for discrete random variables taking the values 0 _,_ 1 _,_ 2 _, . . ._ . This is the reason for considering Laplace and Fourier transforms.

#### **24.3.2 Laplace Transform (Moment Generating Function)**

The Laplace transform of a random variable _X_ is defined as the function:


for all _t ∈_ ( _−∞, ∞_ ) for which E( _e_<sup>_tX_</sup> ) _< ∞_ . Note that _MX_ (0) = 1.

**Example 24.6** (MGF of Standard Gaussian) **.** _If X ∼ N_ (0 _,_ 1) _, then its MGF can be easily computed as follows:_


_Thus MX_ ( _t_ ) = _e_<sup>_t_2</sup><sup>_/_2</sup> _for all t ∈_ R _._

124

The Laplace transform is defined for every random variable _X_ (although for some random variables _MX_ ( _t_ ) can be + _∞_ for many values of _t_ ) unlike the _z_ -transform which is only defined for random variables taking values in _{_ 0 _,_ 1 _,_ 2 _, . . . }_ . Just like the _z_ -transform, the Laplace transform also factorizes for independent random variables. Indeed, if _X_ 1 _, . . . , Xn_ are independent, then


This is a consequence of the fact that


the last equality being a consequence of independence.

The Laplace transform is known as the Moment Generating Function because it allows one to easily read off the moments of the random variable. For _k ≥_ 1, the number E( _X_<sup>_k_</sup> ) is called the _k_<sup>_th_</sup> moment of _X_ . Knowledge of _MX_ ( _t_ ) allows one to easily read off the moments of _X_ because the power series expansion of _MX_ ( _t_ ) is


Therefore the _k_<sup>_th_</sup> moment of _X_ is simply the coefficient of _t_<sup>_k_</sup> in the power series of expansion of _MX_ ( _t_ ) multiplied by _k_ !. Alternatively, one can derive the moments E( _X_<sup>_k_</sup> ) as derivatives of the MGF at 0 because


so that

_MX_<sup>(</sup><sup>_k_)(0) = E(</sup><sup>_Xk_)</sup><sup>_._</sup>

In words, E( _X_<sup>_k_</sup> ) equals the _k_<sup>_th_</sup> derivative of _MX_ at 0. Therefore


and so on.

As an application, we can deduce the moments of the standard normal distribution from the fact that its Laplace Transform equals _e_<sup>_t_2</sup><sup>_/_2</sup> . Indeed, because


it immediately follows that the _k_<sup>_th_</sup> moment of _N_ (0 _,_ 1) equals 0 when _k_ is odd and equals


The Central Limit Theorem can be established using Laplace transforms in the following way.

_Proof of the CLT with Laplace Transforms._ We have i.i.d random variables _X_ 1 _, X_ 2 _, . . ._ which have mean _µ_ and finite variance _σ_<sup>2</sup> . Let _Yn_ :=<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X_<sup>¯</sup> _n − µ_ ) _/σ_ . We need to show that _Yn_ converges in distribution to _N_ (0 _,_ 1). We shall show that the Laplace transform of _Yn_ converges of the Laplace transform of _N_ (0 _,_ 1) which is _e_<sup>_t_2</sup><sup>_/_2</sup> :


125

Note that


As a result,


where _M_ ( _·_ ) is the Laplace transform of ( _X_ 1 _− µ_ ) _/σ_ . We now use Taylor’s theorem to expand _M_ ( _tn_<sup>_−_1</sup><sup>_/_2</sup> ) up to a quadratic polynomial around 0. Recall that Taylor’s theorem says that for a function _f_ and two points _x_ and _p_ in the domain of _f_ , we can write


where _ξ_ is some point that lies between _x_ and _p_ . Using Taylor’s theorem with _r_ = 1, _x_ = _tn_<sup>_−_1</sup><sup>_/_2</sup> and _p_ = 0, we obtain


for some _sn_ that lies between 0 and _tn_<sup>_−_1</sup><sup>_/_2</sup> . This implies therefore that _sn →_ 0 as _n →∞_ . Note now that _M_ (0) = 1 and _M_<sup>_′_</sup> (0) = E(( _X_ 1 _− µ_ ) _/σ_ ) = 0. We therefore deduce that


Note also that


We therefore invoke the following fact:

to deduce that


This completes the proof of the CLT assuming the fact (120). It remains to prove (120). There exist many proofs for this. Here is one. Write


Let _ℓ_ ( _x_ ) := log(1 + _x_ ). Taylor’s theorem for _ℓ_ for _r_ = 2 and _p_ = 0 gives

for some _ξ_ that lies between 0 and _x_ . Taking _x_ = _an/n_ , we get


for some _ξn_ that lies between 0 and _an/n_ (and hence _ξn →_ 0 as _n →∞_ ). As a result,


as _n →∞_ . This proves (120).

126

The above proof of the CLT has two deficiencies:

1. It tacitly assumes that the moment generating function of _X_ 1 _, . . . , Xn_ exists for all _t_ . This is much stronger than the existence of the variance of _Xi_ (which is all the CLT needs). Indeed if _MX_ ( _t_ ) exists for all _t_ in any open interval containing zero, then moments of all orders (not just the variance) exist.

- _Xn−µ_

- 2. We have proved that the Laplace transform of<sup>_√_</sup> _<u>n</u> σ_ converges to that of _N_ (0 _,_ 1). It is not clear though as to how this implies that


for _−∞≤ a < b ≤∞_ .

To fix these two deficiencies, one works with the Fourier transform for proving the CLT.

#### **24.3.3 Fourier Transform (Characteristic Function)**

The Fourier transform of a random variable _X_ is defined as the function:


for all _t ∈_ ( _−∞, ∞_ ). Here _i_ =<sup>_√_</sup> _−_ 1. The Fourier transform is defined for every random variable and it is finite for all _t ∈_ ( _−∞, ∞_ ). This is because cos( _tX_ ) and sin( _tX_ ) are always bounded by 1 so the expectation will obviously be finite. For example, suppose _X_ has the Cauchy distribution with density:


Then it is easy to check that the Laplace transform _MX_ ( _t_ ) will equal + _∞_ for all _t̸_ = 0. On the other hand, the Fourier transform of _X_ is


It turns out that the above integral equals _e_<sup>_−|t|_</sup> so that


You should find a proof of the above online. Just like the other two transforms, the Fourier transform factorizes for independent random variables. Indeed, if _X_ 1 _, . . . , Xn_ are independent, then


This is a consequence of the fact that


the last equality being a consequence of independence.

127

**Example 24.7.** _The following is a standard fact. If X_ 1 _, X_ 2 _, . . . , Xn are i.i.d random variables having the Cauchy distribution. Then their mean X_<sup>¯</sup> _n_ := ( _X_ 1 + _· · ·_ + _Xn_ ) _/n also has the Cauchy distribution. This can be proved using Fourier transforms as follows. The Fourier transform of X_<sup>¯</sup> _n equals_


_Because the Fourier transform of the Cauchy distribution equals e_<sup>_−|t|_</sup> _, we get_

_φX_ ¯ _n_<sup>(</sup><sup>_t_) = (exp (</sup><sup>_−|t|/n_))</sup><sup>_n_= exp(</sup><sup>_−|t|_)</sup><sup>_._</sup>

_Thus the Fourier transform of X_<sup>¯</sup> _n also equals e_<sup>_−|t|_</sup> _which implies that X_<sup>¯</sup> _n also has the Cauchy distribution._

In the next class, we shall study the proof of the CLT using the Fourier transform.

---

[← 23 Lecture Twenty Three](24-23-lecture-twenty-three.md) · [Up: contents](index.md) · [25 Lecture Twenty Five →](26-25-lecture-twenty-five.md)
