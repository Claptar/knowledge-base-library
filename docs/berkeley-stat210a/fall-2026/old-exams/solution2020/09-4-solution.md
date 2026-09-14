---
title: 4. Solution
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2020.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2020.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Solution

**Source:** [`old-exams/solution2020.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2020.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (a) Let _z_ = ( _g_ 0( _X_ 1) _, . . . , g_ 0( _Xn_ )) _∈_ R<sup>_n_</sup> , which is a fixed nonzero vector, and define the unit vector _q_ 1 = _z/∥z∥_ . Under _H_ 0, _Yi − f_ 0( _Xi_ ) = _εi_ , so the test statistic is


and the variance estimator is


where _Qr ∈_ R<sup>_n×_(</sup><sup>_n−_1)</sup> is chosen so _QrQ_<sup>_′_</sup> _r_<sup>=</sup><sup>_In−q_1</sup><sup>_q_</sup> 1<sup>_′_,an(</sup><sup>_n−_1)-</sup> dimensional projection matrix. Furthermore, _Q_<sup>_′_</sup> _r_<sup>_q_1=0so</sup><sup>_Q′_</sup> _r_<sup>_ε_and</sup> _q_ 1<sup>_′ε_areindependent,with</sup><sup>_q_</sup> 1<sup>_′ε ∼N_(0</sup><sup>_, σ_2)and</sup><sup>_∥Q_</sup> _r_<sup>_′ε∥_2</sup><sup>_∼σ_2</sup><sup>_χ_2</sup> _n−_ 1<sup>,under</sup> the null, so we should take _d_ = _n −_ 1 and


- (b) If we condition on _X_ 1 _, . . . , Xn_ , we are back in the same situation as in part (a), and we have just derived that _T_ is conditionally _tn−_ 1 distributed, given _X_ 1 _, . . . , Xn_ . If the conditional distribution of _T_ given _X_ doesn’t depend on _X_ , then _T_ is independent of _X_ .

- (c) Because [ _−_ 1 _,_ 1] is a compact parameter space, to apply our theorem from class we only need to establish that the model is identifiable, and


The log-likelihood and its derivative for a single pair ( _Xi, Yi_ ) is


Because _|gτ_ ( _Xi_ ) _| ≤_ 1, the first derivative is bounded by


18

where the last step uses the fact that


for any _x_ and _τ_ 1 _, τ_ 2 _∈_ [ _−_ 1 _,_ 1]. As a result, for any _τ_ 0 _∈_ [ _−_ 1 _,_ 1], we have


which is certainly finite.

As for identifiability, consider _τ_ 2 _> τ_ 1 and note


where _τ_ ˜( _x_ ) _∈_ [ _τ_ 1 _, τ_ 2] is defined implicity by the mean value theorem. Then


since _gτ_ ˜( _Xi_ )( _Xi_ ) _>_ 0 almost surely (we will accept more informal arguments along the same lines).

- (d) We have assumed consistency, and that _τ_ is in the interior of the parameter space. The other conditions can be checked using similar methods as in the previous part, but you did not need to check them. Continuing our calculation from part (c), the second derivative of _ℓ_ 1 is


and its expectation is


As a result, the asymptotic distribution of the MLE is


19

- (e) No, we can’t (necessarily) estimate _τ_ consistently anymore. The problem is that the intercept breaks our proof of identifiability. Indeed, let _fτ_ ( _x_ ) _≡ τ_ , which satisfies all of the conditions in the preamble since _gτ_ ( _x_ ) _≡_ 1 and _hτ_ ( _x_ ) _≡_ 0; then _τ_ is unidentifiable in the model so there is no way we can hope to estimate it using the MLE or any other method.

To get more specific in terms of the MLE, the likelihood function _ℓn_ ( _α − τ, τ_ ; _Xi, Yi_ ) is constant for _τ ∈_ [ _−_ 1 _,_ +1] and any ( _α, τ_ ) with _α_ + _τ_ = _Y n_ is a valid MLE, so clearly the second coordinate can’t be converging to the correct value of _τ_ for any sequence of MLEs.

20

---

[← 3. Solution](08-3-solution.md) · [Up: contents](index.md)
