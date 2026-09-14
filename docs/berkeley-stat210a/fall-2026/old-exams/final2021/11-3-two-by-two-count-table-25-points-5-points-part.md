---
title: 3. Two-by-two count table (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2021.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/final2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Two-by-two count table (25 points, 5 points / part).

**Source:** [`old-exams/final2021.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

- For _θ >_ 0, the Poisson density for _X ∼_ Pois( _θ_ ) is<sup>_<u>θx</u>_</sup> _x_<sup>_<u>e</u>_</sup> !<sup>_−θ_</sup> on _x_ = 0 _,_ 1 _, . . ._ . The mean and variance are both _θ_ .

- For _π_ 1 _, . . . , πd ≥_ 0 with<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_πi_=1,themultinomialdensityfor</sup><sup>_X∼_</sup> Multinom( _n, π_ ) is


   - on _x ∈{_ 0 _, . . . , n}_<sup>_d_</sup> with<sup>�</sup> _i_<sup>_xi_=</sup><sup>_n_.</sup>

- Suppose _Xi ∼_ Pois( _θi_ ) with _θi >_ 0, independently for _i_ = 1 _, . . . , d_ , and let _X_ + =<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_Xi_and</sup><sup>_θ_+= �</sup> _i_<sup>_d_</sup> =1<sup>_θi_.Then, conditional on</sup><sup>_X_+=</sup><sup>_n_,</sup>


Assume that _Xij ∼_ Pois( _λij_ ), independently for _i, j ∈{_ 0 _,_ 1 _}_ . We will consider the model with _λij_ = _λ_ 0 _ρ_<sup>_i_+</sup><sup>_j_</sup> , for _λ_ 0 _, ρ >_ 0. Except when otherwise specified, assume both parameters are unknown.

- (a) Give a complete sufficient statistic for the model and show it is complete.

- (b) Assume (for this part **only** ) that _λ_ 0 is known, but _ρ_ is unknown. Suggest a UMP test of _H_ 0 : _ρ_ = _ρ_ 0 vs. _H_ 1 : _ρ > ρ_ 0. You do not need to give an explicit cutoff for your test but give an explicit formula for the test statistic, explain how you would find the cutoff, and explain why your test is UMP.

- (c) Assuming again that both parameters are unknown, suggest a UMPU test of _H_ 0 : _ρ_ = 1 against _H_ 1 : _ρ >_ 1. You do not need to give an explicit cutoff for your test but explain how you would calculate it. If the data are _X_ 00 = _X_ 01 = 0 and _X_ 10 = _X_ 11 = 1, calculate the (conservative, nonrandomized) _p_ -value for your test.

- (d) For the same data set, _X_ 00 = _X_ 01 = 0 and _X_ 10 = _X_ 11 = 1, find the maximum likelihood estimators for _λ_ 0 and _ρ_ . Give your answers as explicit numbers.

- (e) (*) Now suppose we consider a relaxed model _λij_ = _f_ ( _i_ + _j_ ), for any strictly positive real-valued function _f_ on _{_ 0 _,_ 1 _,_ 2 _}_ . This includes our previous parametric model as a special case since we could have _f_ ( _i_ + _j_ ) = _λ_ 0 _ρ_<sup>_i_+</sup><sup>_j_</sup> . Does

11

there exist a UMPU test of the null hypothesis that our previous model was correctly specified, against the alternative that it was misspecified but the relaxed model is correct? Explain why or why not. (If you say yes you only need to give enough details to establish that such a test exists).

12

---

[← Problem 2 answers continued (3)](10-problem-2-answers-continued-3.md) · [Up: contents](index.md) · [Problem 3 answers continued (1) →](12-problem-3-answers-continued-1.md)
