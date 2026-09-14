---
title: 3 Boosting
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_06_Ensemble_methods.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_06_Ensemble_methods.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Boosting

**Source:** [`notes/Lecture_06_Ensemble_methods.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_06_Ensemble_methods.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There are two broad categories of boosting: Adaptive boosting and gradient boosting. Adaptive and gradient boosting rely on the same concept of boosting “weak learners” to “strong learners.” See Figure 2 for illustration. Boosting is an iterative process, where the training set is reweighted, at each iteration, based on

3


Figure 2: Illustration of weak and strong learners.

mistakes a weak leaner made (i.e., misclassifications); the two approaches, adaptive and gradient boosting, differ mainly regarding how the weights are updated and how the classifiers are combined. Since we have not discussed gradient-based optimization, in this lecture, we will focus on adaptive boosting. In particular, we will focus on AdaBoost.

Intuitively, we can outline the general boosting procedure as follows:

1. Initialize a weight vector with uniform weights–each data point plays an equal role in building the first classifier;

2. Train a weighted learner _f_ 1( _x_ ) based on the sample with equal weights, and calculate its training classification error, denoted as _ϵ_ 1 _∈_ [0 _,_ 1];

3. Increased the weights for misclassified data points (as the algorithm can improve its accuracy from furthering learning these data points), we define _w_ 1 = 2<sup><u>1</u>log</sup><sup><u>1</u></sup><sup>_−_</sup> _ϵ_ 1<sup>_<u>ϵ</u>_</sup><sup><u>1</u></sup> and


then normalize these weights so they sum up to one.

4. Train a weighted learner _f_ 2( _x_ ) based on the sample with equal weights, and calculate its weighted training classification error:


and we update the weights as


This step essentially tells us that we need to decrease the weights for the _i_ th data point whenever it is classified correctly.

5. Repeat the above steps until _ϵb >_ 1 _/_ 2. Then the adaboost classifier is of the from:


4


Figure 3: Illustration of AdaBoost.

---

[← 2 Random forest](03-2-random-forest.md) · [Up: contents](index.md) · [References →](05-references.md)
