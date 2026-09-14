---
title: Problem 1 Solutions
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2018.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2018.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 1 Solutions

**Source:** [`old-exams/solution2018.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2018.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (a) This model is a subfamily of the bivariate Gaussian location family with no restrictions on _µ_ . That family is full-rank with complete sufficient statistic _T_ ( _X_ ) =<sup>�</sup> _i_<sup>_Xi_andnaturalparameter</sup><sup>_µ_.</sup>

It is clear that


for example take _µ_ (1) _− µ_ (0) = �11� and _µ_ ( _−_ 1) _− µ_ (0) = � _−_ 11�; as a result � _i_<sup>_Xi_isminimalsufficient.</sup>

Furthermore, taking _f_ ( _t_ ) = ( _t_ 1 _/n_ )<sup>2</sup> _−_ ( _t_ 2 _/n_ ) _− n_<sup>_−_1</sup> , we have


But _f_ ( _T_ ( _X_ )) is clearly not almost surely zero, so _T_ ( _X_ ) is not complete.

(b) The part of the log-likelihood that depends on _θ_ is


The variance of<sup>�</sup> _i_<sup>_Xi,_1 + 2</sup><sup>_θ_�</sup> _i_<sup>_Xi,_2is</sup>


(c) The one-sided score test rejects for large values of


In generic “smooth” models this statistic has mean 0 and variance 1, and converges to _N_ (0 _,_ 1), under the null. In this particular model it is exactly _N_ (0 _,_ 1) in finite samples, because the _Xi,j_ values are independent Gaussian random variables. We reject if it is larger than _zα_ , which has probability exactly _α_ .

3

(d) Applying standard results we have


Further applying the delta method for the function _θ �→ θ_<sup>2</sup> , whose derivative is 2 _θ_ , we obtain


By contrast, we have<sup>_√_</sup> _<u>n</u>_ � _n_ <u>1</u> � _i_<sup>_Xi,_2</sup><sup>_−θ_2�</sup> _∼ N_ (0 _,_ 1) in finite samples as well as asymptotically, which is a higher variance no matter what _θ_ is. The asymptotic relative efficiency of the “obvious” estimator is therefore 1+11 _/_ 4 _θ_<sup>2.Notethisiscloseto1as</sup><sup>_θ→±∞_butas</sup><sup>_θ→_0it</sup> diverges to _∞_ .

- (e) Let _θ_ = 0 and let _n →∞_ . As we zoom into the origin, eventually the model is nearly a horizontal line through the origin. Because maximum likelihood estimation in a Gaussian location model is equivalent to Euclidean projection, we have _θ_<sup>ˆ</sup> _≈ X_<sup>¯</sup> 1 = _n_<sup><u>1</u></sup> � _i_<sup>_Xi,_1and</sup><sup>_θ_ˆ2</sup><sup>_≈_( ¯</sup><sup>_X_1)2=</sup> _n_<sup><u>1</u></sup><sup>_χ_</sup> 1<sup>2.</sup> If we did all this more carefully we would get


4

**2. Species abundance (20 points, 5 points / part).** Some useful facts for this problem:

   - Recall that the Poisson distribution _X ∼_ Pois( _λ_ ) has probability mass function


on _x_ = 0 _,_ 1 _,_ 2 _, . . ._ . _X_ has mean _λ_ and variance _λ_ .

- The multinomial distribution ( _X_ 1 _, . . . , Xd_ ) _∼_ Multinom( _n, π_ ) has probability mass function


- ind.

- _•_ Suppose _Xi ∼_ Pois( _λi_ ) for _i_ = 1 _, . . . , d_ , and let _X_ + =<sup>�</sup> _i_<sup>_Xi_and</sup> _λ_ + =<sup>�</sup> _i_<sup>_λi_.Thenconditionalon</sup><sup>_X_+=</sup><sup>_x_+,wehave</sup>


Consider an ecological sampling problem where we visit _m_ sites and for each of _s_ species, we count the total number of individuals at each site. Let _Nj_<sup>(</sup><sup>_i_)</sup> denote the number of individuals of species _j_ at site _i_ . Hence we observe a table of counts of the form

---

[← Final Examination: QUESTION BOOKLET](02-final-examination-question-booklet.md) · [Up: contents](index.md) · [Species →](04-species.md)
