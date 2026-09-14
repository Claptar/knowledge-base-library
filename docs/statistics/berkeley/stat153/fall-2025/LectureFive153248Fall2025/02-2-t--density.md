---
title: 2 t -density
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 t -density

**Source:** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The formula for the density corresponding to the _t_ -distribution _tp_ ( _µ,_ Σ _, ν_ ) is (see ( `https: //en.wikipedia.org/wiki/Multivariate_t-distribution` ):


Here:

1. _p_ denotes dimension of the vector _x_ (this is a _p_ -variate joint density)

2. _µ_ is a _p ×_ 1 vector called the location

3. Σ is a _p × p_ matrix called the scale matrix

4. _ν >_ 0 denotes the degrees of freedom.

Here is some more information about the _t_ -density (3):

1. **Connection to the Multivariate Normal Density** : The most important term in the formula (3) is ( _x − µ_ )<sup>_T_</sup> Σ<sup>_−_1</sup> ( _x − µ_ ). This exact term also appears in the multivariate normal density. If _X ∼ N_ ( _µ,_ Σ), then the density of _X_ is given by:


This suggests that the _t_ -density is closely related to the multivariate normal density. Here is the connection. Suppose _X ∼ Np_ ( _µ,_ Σ) and _V ∼ χν_<sup>2(thisisthechi-squared</sup> distribution with _ν_ degrees of freedom) are independent. Then


Thus, in the notation _tp_ ( _µ,_ Σ _, ν_ ), _ν_ denotes degrees of freedom, _p_ denotes dimension, _µ_ and Σ denote the mean vector and covariance matrix of the corresponding normal random vector _X_ . For completeness, we include a proof of (4) in Section 4.

2. **Individual Components as well as Linear Combinations of Components of** _T_ **are also** _t_ **-distributed** : Suppose _T ∼ tp_ ( _µ,_ Σ _, ν_ ) and the components of _T_ are _T_ 1 _, . . . , Tp_ . Then each individual component _Tj_ is also _t_ -distributed. Also every linear combination _a_ 0 + _a_ 1 _T_ 1 + _a_ 2 _T_ 2 + _· · ·_ + _apTp_ is also _t_ -distributed. To see this, first write


where _a_ is the _p ×_ 1 vector with components _a_ 1 _, . . . , ap_ . Using the formula (4), we can write


Because _a_ 0 + _a_<sup>_T_</sup> _X ∼ N_ ( _a_ 0 + _a_<sup>_T_</sup> _µ, a_<sup>_T_</sup> Σ _a_ ), the same fact (4) applied to this case gives:

_a_ 0 + _a_<sup>_T_</sup> _T ∼ t_ 1( _a_ 0 + _a_<sup>_T_</sup> _µ, a_<sup>_T_</sup> Σ _a, ν_ ) _._

2

In particular, this implies that for each _j_ = 1 _, . . . , p_ ,


where _µj_ is the _j_ th component of _µ_ and Σ( _j, j_ ) is the ( _j, j_ )th entry of Σ.

3. **When** _ν_ **is large,** _t_ **is very close to normal** : This can intuitively be seen by noting that when _ν_ is large, the term ( _x − µ_ )<sup>_T_</sup> Σ<sup>_−_1</sup> ( _x − µ_ ) _/ν_ is small so that


where we used the observation that 1 + _z ≈ e_<sup>_z_</sup> when _z_ is small. Thus the _t_ -density (3) for large _ν_ becomes approximately:


because<sup>_ν_</sup><sup><u>+</u></sup> _ν_<sup>_<u>p</u>_</sup> _≈_ 1 when _ν_ is large. This gets us the normal density:


In our regression case, the degrees of freedom is _n − m −_ 1 where _n_ is the number of observations, and _m_ is the number of covariates. Thus **if** _n − m −_ 1 **is large** , then the posterior distribution (which is actually _t_ ) is approximately normal:

---

[← 1 Posterior t -density in Multiple Linear Regression](01-1-posterior-t--density-in-multiple-linear-regression.md) · [Up: contents](index.md) · [3 Back to Regression →](03-3-back-to-regression.md)
