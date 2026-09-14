---
title: 'Topic Four: Variance Modeling'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureOneSlides153248Fall2026PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Topic Four: Variance Modeling

**Source:** [`LectureOneSlides153248Fall2026PDF.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Daily closing prices _Pt_ of S&P 500 (2000-01-01 to 2024-01-01)


## **Stock Returns** _rt_

Note _rt_ ≈100 ×<sup>_Pt_−</sup><sup>_Pt_−1</sup> _rt_ = 100 × (log _Pt_ −log _Pt_ −1) _Pt_ −1


###### • Financial analysts also study the volatility of stock price returns

- For estimating volatility, it is common to use the model: and then to model _rt_ ∼ _N_ (0, _σt_<sup>2)</sup> _σt_

- (which is a proxy for volatility) as a function of _t_

- • These are examples of variance models as opposed to the mean (regression) models we saw so far


For the S&P returns data, below is an estimate of log _σt_

---

[← Topic Two: Nonlinear Regression](05-topic-two-nonlinear-regression.md) · [Up: contents](index.md) · [Spectral Analysis →](07-spectral-analysis.md)
