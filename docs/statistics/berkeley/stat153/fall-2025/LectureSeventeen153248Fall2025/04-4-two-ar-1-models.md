---
title: 4 Two AR(1) Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeventeen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Two AR(1) Models

**Source:** [`LectureSeventeen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We therefore have two different versions of AR(1) corresponding to each of the likelihoods (6) and (7).

The first version is:


The second version assumes


6

Note that this, along with _y_ 2 = _ϕ_ 0 + _ϕ_ 1 _y_ 1 + _ϵ_ 2 implies that


By induction, one can show that


So the second version of the AR(1) model can be simply written as:


i.i.d where _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Note that this equation automatically satisfies: _yt_ = _ϕ_ 0 + _ϕ_ 1 _yt−_ 1 + _ϵt_ and also that _ϵt_ is independent of _yt−_ 1 _, yt−_ 2 _, . . ._ .

It is important to note that the second model (8) only makes sense when _|ϕ_ 1 _| <_ 1. So this second definition is not valid unless _|ϕ_ 1 _| <_ 1. When _|ϕ_ 1 _|_ = 1, one cannot make sense of the right hand side of (8) (this is becase<sup>�</sup><sup>_∞_</sup> _j_ =0<sup>_ϕ_</sup> 1<sup>_jϵt−j_failstoconvergewhen</sup><sup>_|ϕ_1</sup><sup>_| ≥_1).</sup>

We shall see in the next lecture that (8) is an example of a stationary model. We will explore in depth the notion of stationarity.

---

[← 3 Likelihood for AR(1)](03-3-likelihood-for-ar-1.md) · [Up: contents](index.md) · [References →](05-references.md)
