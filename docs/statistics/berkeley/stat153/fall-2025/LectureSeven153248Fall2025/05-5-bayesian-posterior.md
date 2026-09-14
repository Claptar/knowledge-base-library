---
title: 5 Bayesian Posterior
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Bayesian Posterior

**Source:** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For Bayesian inference, we need to select the prior on _β, σ_ and _f_ . For _β_ and _σ_ , we shall use, as usual:


For _f_ , we shall use:


because, as seen in Section 3, we know we can restrict _f_ to [0 _,_ 1 _/_ 2].

This will let us write the joint posterior of all the parameters _β, σ, f_ , and then we integrate out _β_ and _σ_ to deduce the posterior of _f_ . This calculation is exactly the same as in the last lecture when we studied the change of slope model; the only difference being that _c_ there is now replaced by _f_ (also the indicator _I{_ 1 _< c < n}_ should be replaced by _I{_ 0 _≤ f ≤_ 1 _/_ 2 _}_ ). The posterior for _f_ will be given by:


Thus psoterior will be evaluated numerically over a grid of values of _f_ in the range [0 _,_ 0 _._ 5]. The term _|Xf_<sup>_TXf|−_1</sup><sup>_/_2becomesinfinitewhen</sup><sup>_|X_</sup> _f_<sup>_TXf|_=0i.e.,when</sup><sup>_Xf_doesnothavefull</sup> column rank. This will be the case when _f_ = 0 or _f_ = 1 _/_ 2. We will exclude these edge cases while computing this posterior:


3

---

[← 4 Least Squares Estimation of β, f, σ](04-4-least-squares-estimation-of-β-f-σ.md) · [Up: contents](index.md) · [6 Efficient Computation of RSS ( f ) →](06-6-efficient-computation-of-rss-f.md)
