---
title: Is my die fair?
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/25-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Is my die fair?

**Source:** `lectures/25-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Hypothesis _H_ 0: **P** ( _X_ = _i_ ) = _pi_ = 1 _/_ 6, _i_ = 1 _, . . . ,_ 6

- Observed occurrences of _i_ : _Ni_

- Choose form of rejection region; chi-square test:


- Choose _ξ_ so that:


         - Need the distribution of _T_ : (CLT + derived distribution problem)

         - for large _n_ , _T_ has approximately a chi-square distribution

         - available in tables

      - **Do I have the correct pdf?**

- Partition the range into bins

- _npi_ : expected incidence of bin _i_ (from the pdf)

- _Ni_ : observed incidence of bin _i_

   - Use chi-square test (as in die problem)

- Kolmogorov-Smirnov test: form **empirical CDF** , _F_<sup>ˆ</sup> _X_ , from data


(http://www.itl.nist.gov/div898/handbook/)

---

[← Composite hypotheses](05-composite-hypotheses.md) · [Up: contents](index.md) · [What else is there? →](07-what-else-is-there.md)
