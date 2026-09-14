---
title: 2 Random forest
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_06_Ensemble_methods.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_06_Ensemble_methods.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Random forest

**Source:** [`notes/Lecture_06_Ensemble_methods.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_06_Ensemble_methods.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One of the most famous and useful bagged algorithms is the Random Forest! A Random Forest is essentially nothing else but bagged decision trees, with a slightly modified splitting criteria. The algorithm works as follows:

1. Draw bootstrap samples from _D_ with replacement, denoted as _D_ 1<sup>_∗, . . . , D_</sup> _B_<sup>_∗_;</sup>

2. On each bootstrap sample, further randomly subsample _k ≤ d_ attributes (without replacement) and only consider these for your split – this further increases the variance of the trees, but reduces the correlation between different trees. Then, build a classifier _fb_<sup>_∗_(</sup><sup>_x_)(canbetree,oranyofyourfavourite</sup> methods);

3. Then final random forested classifier is then


The Random Forest is one of the best, most popular and easiest to use out-of-the-box classifier. There are two reasons for this: (1) The RF only has two hyper-parameters, _B_ and _k_ . It is extremely insensitive to both of these. A good choice for _k_ is _k_ = _√d_ (where _d_ denotes the number of attribute). Ideally, if we can afford the computational cost, we would choose _B_ as large as possible. (2) Decision trees do not require a lot of preprocessing. For example, the features can be of different scale, magnitude, or slope. This can be highly advantageous in scenarios with heterogeneous data, for example the medical settings where features could be things like blood pressure, age, gender, ..., each of which is recorded in completely different units.

While random forests are naturally less interpretable than individual decision trees, where we can trace a decision via a rule sets, it is possible (and common) to compute the so-called “variable importance” of the attributes that means, we can infer how important a feature is for the overall prediction. For classification tree, the variable importance is typically calculated based on Gini-index.

---

[← 1 Bagging](02-1-bagging.md) · [Up: contents](index.md) · [3 Boosting →](04-3-boosting.md)
