---
title: 3 More challenging online streaming data analysis in healthcare with binary
  outcomes
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 More challenging online streaming data analysis in healthcare with binary outcomes

**Source:** [`notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In a real world scenario, it is hard to imagine that any digital platforms will allow daily update on the machine learning algorithms. At best, we would expect the system can be updated every week or every few weeks. We refer to this case as batch update. In this case, between batch updating time points, different patients would have different number of updates; see Figure 3 for an illustration. In other words, within a batch update time period, each patient has repeated and correlated measurements.

4


Figure 3: Illustration of online learning with electronic medical record data.

To establish notation, suppose we have different batch update time points _s_ 1 _, s_ 2 _, . . . , sb_ , we let _Yi_ = ( _yi_ 1 _, . . . , yini_ )<sup>_′_</sup> be the vector of outcome values and _Xi_ = � _xi_ 1 _, . . . , xini_ � _′ ∈_ R _ni×p_ matrix of covariates values for the _i_ th subject _i_ = 1 _, . . . , m_ . Suppose our outcome is a binary random variable _yit ∈{_ 0 _,_ 1 _}_ , and we further assume a marginal generalized linear model as


The conditional density of _yit|xit_ is


with


Then, under the working independence assumption, the score equation from a likelihood perspective has the form (Liang and Zeger, 1986):


where _Xi_ = ( _x_<sup>_′_</sup> _i_ 1<sup>_, . . . , x′_</sup> _ini_<sup>)</sup><sup>_′∈_R</sup><sup>_ni×p_and</sup><sup>_Yi_=(</sup><sup>_Yi_1</sup><sup>_, . . . , Yin_</sup> _i_<sup>)</sup><sup>_′∈_R</sup><sup>_ni×p_.Anestimatorthatsolvestheabove</sup> equation is easy-to-compute with existing software, and the estimator is _consistent_ as long as the model is correctly specified. Next question is how to carry out this estimator in an online fashion? Motivated by our previous construction, suppose our data are collected in different batches _D_ 1 _, . . . , Db_ and within each batch,

5

we may work with the weighted estimating equation:


Given this estimating equation, how can we dynamically revise the model to get an estimate of the coefficient _βb_ ?

6

---

[← 2 Online streaming data analysis with continuous outcomes](03-2-online-streaming-data-analysis-with-continuous-outcomes.md) · [Up: contents](index.md) · [References →](05-references.md)
