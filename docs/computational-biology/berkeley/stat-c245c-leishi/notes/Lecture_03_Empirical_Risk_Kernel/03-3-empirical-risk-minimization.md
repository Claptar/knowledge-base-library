---
title: 3 Empirical Risk Minimization
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_03_Empirical_Risk_Kernel.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_03_Empirical_Risk_Kernel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Empirical Risk Minimization

**Source:** [`notes/Lecture_03_Empirical_Risk_Kernel.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_03_Empirical_Risk_Kernel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Recall in the SVM with soft constraint problem, we work with


7

Whenever _C̸_ = 0, the optimization problem will always try to minimize _ξi_ as much as possible. Then the equation must hold as an equality and we have


Therefore, the slack variable _ξi_ has a closed form expression:


When we plug this closed form into the objective of the SVM primal problem, we obtain the following unconstrained version as loss function:


The hinge loss is intuitive to understand: the classifier _h_ learnt by SVM is parametrized by w, and we make decisions based on


Whenever the classifier makes a mistake, we have _Yi ·_ ( _a_ + w<sup>_′_</sup> _Xi_ ) _<_ 0–generating a loss. Therefore, we define a hinge loss for the classifier _h_ w as


Then the SVM primal problem can be understood from a penalized “regression” perspective (suppose we ignore the intercept _b_ for simplicity<sup>3</sup> )


In your lab, you should have worked with GLM Lasso (or some general penalty) when we label the outcome as _Yi ∈{−_ 1 _,_ 1 _}_ (try this one on your own, the optimization problem we worked out in GLM section is for _Yi ∈{_ 0 _,_ 1 _}_ ):


> 3This works as once we have solved SVM for some w _∗_ , then optimal value for _b∗_ can be calculated immediately.

8

where the classifier _hb_ does the following:


Figure 2: Common Classification Loss Functions on the x-axis: _f_ ( _Xi_ ) _Yi_

Now, the logistic regression and SVM look oddly similar. Both say that if we misclassify more pairs ( _Xi, Yi_ ), the loss function (either _l_ `logit` or _l_ `svm` ) is large; the penalty is trying to make the classifier _h_ simple (remember the Occam’s razor principle?). In other words, we are trying to find a classifier that (1) makes less mistakes, and (2) as simple as possible. This principle applies in many famous estimators (ridge regression, Lasso, Elastic Net, etc.).

Let’s now look into the difference between the SVM and the logistic losses in Figure 2. The exponential loss is of the form (this is a very sensitive/aggressive loss)


Which loss do you like better? Why? Think about it

from a statistical _inference_ point of view.

We end this section by defining the general empirical risk minimization problem with a loss function _l_ and some penalty function _p_ :


where the loss function _l_ ( _·, ·_ ) is a function that penalize the difference between _Yi_ and _h_ w( _Xi_ ), and the penalty function _p_ ( _·_ ) penalizes the classifier’s complexity.

9

---

[← 2 SVM-continued](02-2-svm-continued.md) · [Up: contents](index.md) · [References →](04-references.md)
