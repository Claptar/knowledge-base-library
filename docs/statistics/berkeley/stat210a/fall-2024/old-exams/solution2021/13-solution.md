---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2021.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2021.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that our restriction to _θ ≥_ 0 was not statistically essential: the loglikelihood would still be uniformly bounded and convex, and the parameter space compact, if we took the parameter space [ _a, b_ ] for any _−_ 1 _/C < a < b <_ 1. Hence consider an expansion of the parameter space to [ _−_ 1 _/_ 2 _C, b_ ] and let _θ_ ˆ<sup>_u_</sup> denote the MLE for that larger model. We have


Of course, _θ_<sup>ˆ</sup><sup>_u_</sup> and _θ_<sup>ˆ</sup> do not have the same distribution because _θ_<sup>ˆ</sup> cannot be negative. However, because the log-likelihood is convex, we must have _θ_<sup>ˆ</sup> = 0 and _θ_<sup>ˆ</sup><sup>_u_</sup> _<_ 0 if and only if _ℓ_<sup>˙</sup> _n_ (0; _X_ ) _<_ 0; otherwise, _θ_<sup>ˆ</sup> = _θ_<sup>ˆ</sup><sup>_u_</sup> _≥_ 0 because _θ_<sup>ˆ</sup><sup>_u_</sup> maximizes the log-likelihood over a larger parameter space. Thus, we have almost surely


By the continuous mapping theorem, we have ~~�~~ _nJ_ 1(0) _θ_<sup>ˆ</sup> _⇒_ max _{_ 0 _, Z}_ , where _Z ∼ N_ (0 _,_ 1).

8

---

[← Solution](12-solution.md) · [Up: contents](index.md) · [3. Two-by-two count table (25 points, 5 points / part). →](14-3-two-by-two-count-table-25-points-5-points-part.md)
