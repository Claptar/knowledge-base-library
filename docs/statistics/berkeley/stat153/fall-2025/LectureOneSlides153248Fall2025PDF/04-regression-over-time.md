---
title: Regression over time
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureOneSlides153248Fall2025PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Regression over time

**Source:** [`LectureOneSlides153248Fall2025PDF.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The first time series technique we will study is regression over the time variable _t_

Simple linear regression of the time series _yt t_ on the time variable  will fit a line to the observed time series data

Multiple linear regression of  on  and other _t yt_ functions of  (such as powers, sinusoids etc) _t_ will fit more general functions to the data


Linear regression of  on 1, _t yt_


: Linear regression of  on 1, cos( _πt_ /6), sin( _πt_ /6) _yt_


~ 1, cos( _πt_ /6), sin( _πt_ /6), cos( _πt_ /3), sin( _πt_ /3) _yt_


cos( _πt_ /6), sin( _πt_ /6), cos( _πt_ /3), sin( _πt_ /3), cos( _πt_ /2), sin( _πt_ /2)


_yt_ ∼ sinusoids + quadratic

###### **Topic One: Multiple Linear Regression**

- These models clearly give (sometimes reasonable) solutions to the prediction problem

- • The first topic in this course is multiple linear regression

- • We will go over the usual frequentist inference but also discuss in detail Bayesian inference for linear regression

---

[← Questions](03-questions.md) · [Up: contents](index.md) · [Topic Two: Nonlinear Regression →](05-topic-two-nonlinear-regression.md)
