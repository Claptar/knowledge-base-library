---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2024.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2024.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2024.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2024.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Start by making the sufficiency reduction to _Tw ∼_ Binom( _Nw, α_ + _β_ ) and _Tb ∼_ Binom( _Nb, α_ ), independently. We want to maximize the concave loglikelihood subject to the constraint _β ≥_ 0.

The unconstrained solution sets the expectations of _Tw_ and _Tb_ equal to their realized values, giving _α_ ˆ = _Tb/Nb_ and _α_ ˆ + _β_<sup>ˆ</sup> = _Tw/Nw_ , so _β_<sup>ˆ</sup> = _Tw/Nw − Tb/Nb_ .

If the unconstrained solution satisfies the constraint, it is also the constrained solution. Otherwise the constrained solution is at the boundary _β_ = 0, corresponding to the one-parameter model where all edges have probability _α_ . That model has MLE _α_ ˆ = ( _Tb_ + _Tw_ ) _/_ ( _Nb_ + _Nw_ ) (and _β_<sup>ˆ</sup> = 0).

- (c) (*) Now (for this part only) assume _α ∈_ (0 _,_ 1) is known. Does there exist an admissible unbiased estimator for _β_ , for the squared error loss?

9

---

[← Solution](12-solution.md) · [Up: contents](index.md) · [Solution →](14-solution.md)
