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

In this case we are testing the null hypothesis _H_ 0 : _η_ 1 = 0 against the alternative hypothesis _H_ 1 : _η_ 1 _>_ 0. On the null, _T_ 1( _X_ ) = _X_ 00 + _X_ 10 + _X_ 01 + _X_ 11 is complete sufficient, so we should condition on it and reject for large values of _T_ 2( _X_ ).

For this particular data set, _T_ 1( _X_ ) = 2 so we observe a Multinom(2 _,_ 14 _/_ 4) distribution under the null, conditional on _T_ 1( _X_ ) = 2. Our test statistic is _T_ 2( _X_ ) = 3. The largest value we could have observed is 4, if _X_ 11 = 2, which would happen with probability (1 _/_ 4)<sup>2</sup> = 1 _/_ 16. The second largest value we could have observed is 3, which can happen two ways: if _X_ 01 = _X_ 11 = 1, or if _X_ 10 = _X_ 11 = 1; both of these events occur with probability 2 _·_ (1 _/_ 4)<sup>2</sup> = 1 _/_ 8. As a result, the _p_ -value is


- (d) For the same data set, _X_ 00 = _X_ 01 = 0 and _X_ 10 = _X_ 11 = 1, find the maximum likelihood estimators for _λ_ 0 and _ρ_ . Give your answers as explicit numbers.

**Solution:**

10

The MLE solves


Dividing the second equation by the first gives


and plugging into the first equation gives _λ_<sup>ˆ</sup> 0 = 1 _/_ 8.

- (e) (*) Now suppose we consider a relaxed model _λij_ = _f_ ( _i_ + _j_ ), for any strictly positive real-valued function _f_ on _{_ 0 _,_ 1 _,_ 2 _}_ . This includes our previous parametric model as a special case since we could have _f_ ( _i_ + _j_ ) = _λ_ 0 _ρ_<sup>_i_+</sup><sup>_j_</sup> . Does there exist a UMPU test of the null hypothesis that our previous model was correctly specified, against the alternative that it was misspecified but the relaxed model is correct? Explain why or why not. (If you say yes you only need to give enough details to establish that such a test exists).

---

[← Solution](16-solution.md) · [Up: contents](index.md) · [Solution →](18-solution.md)
