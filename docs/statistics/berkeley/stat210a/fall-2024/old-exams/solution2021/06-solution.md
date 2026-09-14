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

Consider the model with _Y_<sup>(1)</sup> _, . . . , Y_<sup>(</sup><sup>_m_)i.i.d.</sup> _∼ Nn_ ( _µ,_ Σ), with arbitrary _µ ∈_ R<sup>_n_</sup> and positive definite Σ. In the submodel where Σ is known, Σ<sup>_−_1</sup> _Y_ is complete sufficient (applying part (a) with _X_ = _In_ ) and Σ<sup>�</sup> is ancillary, so by Basu’s theorem Σ<sup>_−_1</sup> _Y_ , and therefore also _Y_ , is independent of Σ<sup>�</sup> . The two statistics are therefore independent for any _µ_ and Σ, so in particular they are independent if _µ_ = _Xβ_ for any Σ.

**Common mistake:** _Y_ is not complete sufficient in the model with _µ_ = _Xβ_ , for _d < n_ .

- (d) Show that Σ<sup>�</sup> is an unbiased estimator of Σ.

**Solution:**

3


Then, because E [¯ _εε_ ¯<sup>_′_</sup> ] = Var(¯ _ε_ ) = _m_<sup>_−_1</sup> Σ, we have


(e) Now assume _n_ = _d_ . Is Σ<sup>�</sup> UMVU? Why or why not?

---

[← Solution](05-solution.md) · [Up: contents](index.md) · [Solution →](07-solution.md)
