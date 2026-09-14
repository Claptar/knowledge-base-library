---
title: '2 Detour: usual linear regression'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeventeen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Detour: usual linear regression

**Source:** [`LectureSeventeen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The model (2) looks just like a usual regression model:


1

except we are using _ϕ_ instead of _β_ for the coefficients, and the index is now _t_ as opposed to _i_ . Let the data be denoted by ( _xi, yi_ ) _, i_ = 1 _, . . . , m_ ( _m_ is the number of data points).

i.i.d Under the assumption _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ), the likelihood for (3) is:


Let us take a closer look as to how the likelihood (4) is actually derived. We shall examine closely the assumptions that are made in deriving (4). Our main interest is to see whether the same assumptions are still true for AutoRegression.

The data is ( _xi, yi_ ) _, i_ = 1 _, . . . , m_ ( _m_ is the number of data points). The likelihood is the probability density function of the data treated as a function of the parameters _θ_ = ( _β_ 0 _, β_ 1 _, σ_ ) ( _σ_ is the standard deviation of the errors):


Given that the model (3) writes each _yi_ in terms of _xi_ , it makes sense to first condition on _x_ 1 _, . . . , xm_ :

Likelihood for model (3) = _fy_ 1 _,...,ym|x_ 1 _,...,xm,θ_ ( _y_ 1 _, . . . , ym_ ) _fx_ 1 _,...,xm|θ_ ( _x_ 1 _, . . . , xm_ ) _._

Now we write _yi_ = _β_ 0 + _β_ 1 _xi_ + _ϵi_ for each _i_ to get

Likelihood for model (3)


To proceed further, we assume that _ϵ_ 1 _, . . . , ϵn_ are independent of _x_ 1 _, . . . , xn_ (given the parameters). This allows us to remove the conditioning on _x_ 1 _, . . . , xn_ in the first term above, leading to:

Likelihood for model (3)

= _fϵ_ 1 _,...,ϵm|θ_ ( _y_ 1 _− β_ 0 _− β_ 1 _x_ 1 _, . . . , ym − β_ 0 _− β_ 1 _xm_ ) _fx_ 1 _,...,xm|θ_ ( _x_ 1 _, . . . , xm_ ) _._ i.i.d We now use the assumption that _ϵ_ 1 _, . . . , ϵn ∼ N_ (0 _, σ_<sup>2</sup> ) to write:

Likelihood for model (3)


How do we deal with the last term _fx_ 1 _,...,xm|θ_ ( _x_ 1 _, . . . , xm_ )? We simply assume that this term does not depend on _θ_ so it only becomes a constant (in terms of _θ_ ) multiplicative factor in the likelihood that can be omitted leading to:


which coincides with (4).

To summarize, we used the following assumptions to derive the likelihood (4):

2

1. The model equation (3)

2. Independence of the errors _ϵ_ 1 _, . . . , ϵm_ with the covariates _x_ 1 _, . . . , xm_

- i.i.d

- 3. _ϵi ∼ N_ (0 _, σ_<sup>2</sup> )

4. The density of _x_ 1 _, . . . , xm_ does not depend on _θ_ = ( _β_ 0 _, β_ 1 _, σ_ ).

Using the likelihood, frequentist inference first computes the Maximum Likelihood Estimates by maximizing the likelihood or the log-likelihood. This gives:


where _X_ is the _m ×_ 2 matrix with the first column consisting of all ones, and the second column consists of _x_ 1 _, . . . , xm_ . Then the goal is to derive the distribution of the MLEs _β_<sup>ˆ</sup> and _σ_ ˆMLE (given the parameters _θ_ ). For this, one again needs to use the above assumptions.

Bayesian inference proceeds by combining the prior _β_ 0 _, β_ 1 _,_ log _σ_<sup>i.i.d</sup> _∼_ unif( _−C, C_ ) with the likelihood to compute the posterior. We have seen previously that the posterior is given by:


A posterior for _σ_ can also be derived (we did this in Homework one). One important point about Bayesian inference is that once the likelihood is written, we no longer care about the assumptions that were needed for writing the likelihood. Once the likelihood is written, the subsequent inference (via the posterior distribution) only uses the likelihood. In contrast, frequentist inference uses the assumptions twice: first to write the likelihood in order to compute the MLEs, and then to derive the distribution of the MLEs.

---

[← 1 Parameter Estimation in AutoRegressive Models](01-1-parameter-estimation-in-autoregressive-models.md) · [Up: contents](index.md) · [3 Likelihood for AR(1) →](03-3-likelihood-for-ar-1.md)
