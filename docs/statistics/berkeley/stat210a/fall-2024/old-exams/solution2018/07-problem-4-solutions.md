---
title: Problem 4 solutions
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2018.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2018.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 4 solutions

**Source:** [`old-exams/solution2018.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2018.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(a) The part of the log-likelihood that depends on _θ_ is


Evaluating at _θ_ = 0, we get that the score is _S_ ( _X_ ) =<sup>�</sup> _i_<sup>sign(</sup><sup>_Xi_).</sup> Slightly modifying the statistic in a way that doesn’t change the test, we can take


We reject if _T_ ( _X_ ) is above the upper- _α_ quantile of this binomial distribution.

- (b) Generically, we have


where


For any symmetric _f_ , it is clear that _π_ 0 _,f_ = 1 _/_ 2, so the null distribution of _T_ ( _X_ ) does not depend on _f_ and the test has exact level _α_ as in part (a).

- (c) The integral _πθ,f_ is evidently increasing in _θ_ for any function _f_ with _π_ 0 _,f_ = 1 _/_ 2, and the binomial random variable _T_ ( _X_ ) is stochastically increasing in _πθ,f_ , so the rejection probability is increasing as well, and equals exactly _α_ and _θ_ = 0 for any _f_ . As a result, the test rejects with probability no greater than _α_ if _θ ≤_ 0 and with probability no less than _α_ if _θ >_ 0.

15

---

[← Problem 3 solutions](06-problem-3-solutions.md) · [Up: contents](index.md)
