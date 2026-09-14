---
title: Introduction
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_02_GLM_SVM.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_02_GLM_SVM.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`notes/Lecture_02_GLM_SVM.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_02_GLM_SVM.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Jingshen Wang

September 8, 2021

Consider an input space _X_ which is a subset of R<sup>_d_</sup> , and the output space _Y_ = _{_ 0 _,_ 1 _}_ , and let


be the target function. Given a set of functions _H_ contains mapping from _X_ to _Y_ , the binary classification task is formulated as follows. The learner receives a training sample _S_ = _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>ofsize</sup><sup>_n_i.i.dfrom</sup><sup>_X_</sup> according to some unknown distribution _F_ ( _·_ ), with _Yi_ = _f_ ( _Xi_ ) and _Xi ∈_ R<sup>_d_</sup> , _Yi ∈{_ 0 _,_ 1 _}_ . The supervised problem then aim to identify a function _h ∈H_ , a binary classifier, with small generalization error (or risk):


Different functions _H_ can be selected for this task. In this section, we shall disuses several methods that work with different class of functions _H_ .

Formalized by the Occam’s razor principle<sup>1</sup> , mappings with smaller complexity provide transparent interpretation, better learning guarantees. A natural choice for _H_ of relatively low complexity is that of linear classifiers or hyperplanes, which can be defined as follows


A classifier of the form _x →_ **1** ( _x_<sup>_′_</sup> _β >_ 0) thus puts label “1” for all points falling on one side of the hyperplane _x_<sup>_′_</sup> _β_ = 0 and “0” for all others. Such a problem is referred to as a linear classification problem. Without loss of generality, we include the intercept as the first component in each covariate _Xi_ through out the lecture notes.

---

[Up: contents](index.md) · [1 Logistic Regression →](02-1-logistic-regression.md)
