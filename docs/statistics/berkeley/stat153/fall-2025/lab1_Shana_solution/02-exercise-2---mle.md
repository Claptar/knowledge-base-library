---
title: Exercise 2 - MLE
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/lab1_Shana_solution.pdf
source_file: sources/berkeley-stat153/fall-2025/lab1_Shana_solution.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Exercise 2 - MLE

**Source:** [`lab1_Shana_solution.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/lab1_Shana_solution.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

i.i.d. Given data _y_ 1 _, . . . , yn_ , consider the model _yi ∼N_ ( _µ, σ_<sup>2</sup> ) for two unknown parameters _µ_ and _σ >_ 0.

Find the maximum likelihood estimators (MLEs) of _µ_ and _σ_ by maximizing the log-likelihood (use first-order derivatives).

**Requirement.** Show that the solution is the _unique interior maximizer_ by arguing concavity of the log-likelihood OR by showing a sign change of the derivative and checking boundary behavior.

_Proof._ **1) Likelihood and log-likelihood.** The likelihood is


Hence the log-likelihood is


**2) Maximize in** _µ_ **for fixed** _σ_ **.** Differentiate w.r.t. _µ_ :


Setting the first derivative to zero yields


Since _∂_<sup>2</sup> _ℓ/∂µ_<sup>2</sup> _<_ 0, _ℓ_ ( _µ, σ_ ) is strictly concave down in _µ_ (for fixed _σ_ ), so _µ_ � is the unique maximizer in _µ_ . Equivalently, maximizing _ℓ_ in _µ_ is the same as minimizing<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_yi −µ_)2,</sup> a strictly convex (concave up) quadratic in _µ_ with unique minimizer _y_ ¯.

**3) Maximize in** _σ_ **for** _µ_ = _y_ ¯ **.** Let _S_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_yi −y_¯)2.Theprofilelog-likelihoodis</sup>


Differentiate w.r.t. _σ_ :

Set to zero:


3

_Uniqueness and interiority._ As _σ →_ 0<sup>+</sup> , _ℓ_ (¯ _y, σ_ ) _→−∞_ and as _σ →∞_ , _ℓ_ (¯ _y, σ_ ) _→−∞_ . Moreover,


so the log-likelihood increases on (0 _,_ � _σ_ ) and decreases on ( _σ,_ � _∞_ ). Therefore _σ_ � is the _unique interior maximizer_ over _σ >_ 0.

**Conclusion.** The MLEs are


These form the unique interior maximizer of the log-likelihood over _µ ∈_ R _, σ >_ 0.

4

---

[← Exercise 1 - Change of Variables](01-exercise-1---change-of-variables.md) · [Up: contents](index.md)
