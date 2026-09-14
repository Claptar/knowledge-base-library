---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/solution2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now the log-likelihood is


and its derivative is


The score evaluated at _δ_ = 0 is then


and the Fisher information at _δ_ = 0 is


Thus, the normalized test statistic is

and since we are doing a one-sided test we reject if it is larger than _zα_ .

- (f) (*) Now, drop the assumption that _θ_ 0 is known, so that now both _θ_ 0 and _δ_ are unknown. Assume we want to test the same hypothesis, _H_ 0 : _δ_ = 0 against _H_ 1 : _δ >_ 0, with _θ_ 0 as a nuisance parameter. How can we modify the test from the previous part so that it has finite-sample control of the Type I error rate? You do not need to give an explicit cutoff, but you should give a sufficient explanation of how you would find it without knowing the value of _θ_ 0.

---

[← Solution](07-solution.md) · [Up: contents](index.md) · [Solution →](09-solution.md)
