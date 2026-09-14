---
title: Introduction
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_06_Ensemble_methods.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_06_Ensemble_methods.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`notes/Lecture_06_Ensemble_methods.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_06_Ensemble_methods.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

PH 240C Supervised Learning (5): Bagging, random forest, and boosting

Jingshen Wang


Bagging (Breiman, 1984), random forest (Breiman, 2001), and boosting (Bartlett et al., 1998) can be broadly categorized as “ensemble learning”, which refers to the learning a weighted combination of base models of the form:


where _wb_ are tuning parameters (weights), _fb_ ( _x_ ) is a given classifier that predict the outcome based on attribute _x_ , and _M_ represents an index for a class of classifiers. Ensemble learning is sometimes called a committee method, since each base model _fb_ gets a weighted “vote.” The question now is how can we find these weights _wb_ and the classifiers _fb_ ( _·|·_ ). Bagging, random forest, and boosting refers to three different approaches to find the weights and those classifiers.


Figure 1: Illustration of Bagging (Breiman, 1984).

---

[Up: contents](index.md) · [1 Bagging →](02-1-bagging.md)
