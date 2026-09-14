---
title: 4. Change point problem (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2021.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Change point problem (25 points, 5 points / part).

**Source:** [`old-exams/solution2021.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

_•_ The Beta distribution Beta( _α, β_ ) with parameters _α, β >_ 0 has density


with respect to the Lebesgue measure on (0 _,_ 1). Its mean and variance are


- The negative binomial distribution NB( _m, θ_ ) with parameters _m ∈{_ 1 _,_ 2 _, . . .}, θ ∈_ (0 _,_ 1) has probability mass function


Its mean and variance are


Assume we observe independent random variables _Xi ∼_ NB( _m, θi_ ) for _i_ = 1 _, . . . , n_ . Assume also that the _θi_ values are constant except at some integer _k ∈ {_ 1 _, . . . , n −_ 1 _}_ where they change. That is,


for _γ_ 0 _, γ_ 1 _∈_ (0 _,_ 1).

Until otherwise specified, assume _k_ is known. Throughout the problem, we will assume _m_ is known.

- (a) Calculate the maximum likelihood estimator for _γ_ 0 and find its asymptotic distribution if _k, n →∞_ . You do not need to check regularity conditions.

---

[← Solution](18-solution.md) · [Up: contents](index.md) · [Solution →](20-solution.md)
