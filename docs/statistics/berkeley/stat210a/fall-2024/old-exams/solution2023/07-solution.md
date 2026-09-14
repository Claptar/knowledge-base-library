---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The estimator is unbiased because E _θ|Xi|_ = _θ_ , since it is exponentially distributed. So _T/n_ , which is an average of _n_ random variables each having expectation _θ_ , also has expectation _θ_ and is therefore unbiased. Its variance is _θ_<sup>2</sup> _/n_ , again because it is an average of _n_ independent random variables each with variance _θ_<sup>2</sup> . This matches the Cram´er-Rao Lower Bound based on the variance calculated above.

- (e) Now, suppose that we are concerned the variance might be gradually shrinking. Specifically, we are concerned that the _i_ th random variable has parameter _θi_ = _θ_ 0(1 _− δ_ )<sup>_i_</sup> . That is, we consider an alternative model with an additional parameter _δ ∈_ [0 _,_ 1), where


Assume (for this part **only** ) that the value of _θ_ 0 is known.

Suppose that we want to test our original model (which has _δ_ = 0) against the alternative that _δ >_ 0. Suggest a score test, giving an explicit expression for the score statistic and a cutoff based on its asymptotic distribution. You do **not** need to justify why the score statistic (calculated in the usual way and appropriately normalized) is asymptotically Gaussian in this non-i.i.d. model; you can just assume that it is.

---

[← Solution](06-solution.md) · [Up: contents](index.md) · [Solution →](08-solution.md)
