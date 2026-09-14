---
title: Some Discrete Distributions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/01-exam-quiz01-revi.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Some Discrete Distributions

**Source:** `exams/01-exam-quiz01-revi.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

||X<br>|_pX_ (_k_)<br>|**E**[_X_ ]|_var_(_X_ )|
|---|---|---|---|---|
|Bernoulli|�<br>1 success<br>0 failure|�<br>_p_<br>_k_ = 1<br>1 _−_ _p_ _k_ = 0<br> <br>|_p_|_p_(1 _−_ _p_)|
|Binomial|Number of successes<br>in n Bernoulli trials|��<br>_n_<br>_k_ <sup>_pk_</sup> <sup>(1 </sup><sup>_−_ </sup><sup>_p_)</sup><sup>_n−k_</sup><br>_k_ = 0_,_ 1_,_ _._ _._ _._ _,_ _n_<br>|np|np(1-p)|
|Geometric|Number of trials<br>until first success|(1 _−_ _p_)<sup>_k−_1</sup>_p_<br>_k_ = 1_,_ 2_,_ _._ _._ _._<br><br>|1<br>_p_|1_−p_<br>_p_<sup>2</sup>|
|Uniform|An integer in<br>|�<br>1<br>_b−a_+1 <sup>_k_ = </sup><sup>_a,_ </sup><sup>_._ </sup><sup>_._ </sup><sup>_._ </sup><sup>_,_ </sup><sup>_b_</sup>|_a_+_b_<br>|(_b−a_)(_b−a_+2)<br>|
||the interval [a,b]|0<br>otherwise|2|12|


26 / 26

Quiz I Review

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms .

---

[← Independence](23-independence.md) · [Up: contents](index.md)
