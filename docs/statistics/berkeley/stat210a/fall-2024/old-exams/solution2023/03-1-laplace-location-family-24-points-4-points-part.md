---
title: 1. Laplace Location Family (24 points, 4 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Laplace Location Family (24 points, 4 points / part).

**Source:** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

- The exponential distribution with scale parameter _θ >_ 0 is called Exp( _θ_ ) and has density


The mean is _θ_ and the variance is _θ_<sup>2</sup> .

- The Gamma distribution with scale parameter _θ >_ 0 and shape parameter _k >_ 0 is called Gamma( _k, θ_ ) and has density


- A sum of _k_ independent Exp( _θ_ ) random variables is Gamma( _k, θ_ ).

- If _Z ∼_ Gamma( _k, θ_ ) then _aZ ∼_ Gamma( _k, aθ_ ), for any _a >_ 0.

Suppose that we observe an i.i.d. sample from the _Laplace scale family_ with parameter _θ >_ 0:


Note the density is supported on the entire real line. This is not the same as the Laplace location family that we have used as a running example in class.

- (a) Show that _|Xi| ∼_ Exp( _θ_ ) for _i_ = 1 _, . . . , n_ .

---

[← Final Examination: QUESTION BOOKLET](02-final-examination-question-booklet.md) · [Up: contents](index.md) · [Solution →](04-solution.md)
