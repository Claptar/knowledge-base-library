---
title: 1 Logistic Regression
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_02_GLM_SVM.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_02_GLM_SVM.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Logistic Regression

**Source:** [`notes/Lecture_02_GLM_SVM.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_02_GLM_SVM.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **1.1 Review of regression**

Regression is a method for studying the relationship between a response variable _Y_ and a covariate _X_ . One way to summarize the relationship between _X_ and _Y_ is through the regression function:


> 1According to Wikipedia: The Occam’s razor principle is the principle of parsimony or law of parsimony. It is also a problem-solving principle that “entities should not be multiplied beyond necessity”, sometimes inaccurately paraphrased as “the simplest explanation is usually the best one.”

1

Our goal is to estimate the regression function _r_ ( _x_ ) from the training sample _S_ = _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>.Aclassical</sup> parametric approach assumes _r_ ( _x_ ) to be linear:


Occasionally, we add the assumption that _εi|Xi ∼ N_ (0 _, σ_<sup>2</sup> ). The maximum likelihood estimator of _β_ coincides with the popular least squares estimator:


To this end, implicitly, we made three assumptions:

1. The pairs ( _Y_ 1 _, X_ 1) _, . . . ,_ ( _Yn, Xn_ ) are independent and identically distributed (why we make this assumption?)

2. Conditional on _X_ , the outcome _Y_ follows a normal distribution: _Y |_ **_X_** _∼ N_ ( _µ_ ( **_X_** ) _, σ_<sup>2</sup> _· I_ )

3. The conditional mean of _Y_ and _X_ is linked through a linear function: _µ_ ( **_X_** ) = **_X_** _β_

In the presence of discrete outcome (e.g., _Yi ∈{_ 0 _,_ 1 _,_ 2 _,_ 3 _}_ ), the last two assumptions are no longer appropriate. Generalized linear regression thus modify the last two assumptions to:

2. Conditional on _X_ , the outcome _Y_ follows certain discrete distribution

3. The conditional mean of _Y_ and _X_ is linked through a non-linear function _g_ ( _·_ ):


**Example 1** (Disease Occuring Rate) **.** _In the early stages of a disease epidemic, the rate at which new cases occur can often increase exponentially through time. Hence, suppose Yi is the number of cases observed on day Ti and µ_ ( _Ti_ ) _is the expected number of new cases on day Ti, we assume that_


_where δ represents the exponential growth rate and γ represents the day-1 cases count. We then take_ log _on both side, which yields_


_Since Yi is a count, assuming Yi|Ti ∼ Poisson_ � _µ_ ( _Ti_ )� _seems to be quite reasonable._

## **1.2 Logistic regression**

In the presence of binary outcome _Yi ∈{_ 0 _,_ 1 _}_ , we assume


2

As _µ_ ( _Xi_ ) is a number between zero and one, we assume that


Equivalently, we assume thta


The name “logistic regression” comes from the fact that _e_<sup>_x_</sup> _/_ (1 + _e_<sup>_x_</sup> ) is called “logistic function (or expit function).” A plot of the logistic function for a one-dimensional _x_ is shown in Figure 1.

Thus, the likelihood function for the training sample _{_ ( _Yi, Xi_ ) _}_<sup>_n_</sup> _i_ =1<sup>is</sup>


and the maximum likelihood estimator for _β_ is obtained by


Figure 1: Logistic function _e_<sup>_x_</sup> _/_ (1 + _e_<sup>_x_</sup> ) illustration.

To minimize the mis-classification error rate (is mis-classification error always desirable? especially in health science), we predict the label for a new data point _x ∈X_ as


Therefore, logistic regression gives us a linear classifier. The decision boundary separating two predicted class is the hyper-plane _x_<sup>_′_�</sup> _β_ = 0.

Logistic regression is one of the most commonly adopted tools for applied statistics. There are many reasons for this. First, logistic regression is easy-to-compute with Newton-Rapson and is being well-integrated into `R` . Second, the coefficient _β_ has clear interpretation. When _Xi_ contains the intercept and a univariate covariate (say gender) and the outcome indicate whether the individual has CAD, then _β_ 1 = 10 represents the odds of having CAD for male is 10 times higher than females. In addition, the larger the coefficient _β_ 1, the difference between female and male more strongly influences the disease status–because informally we can think of our prediction as being a very confidence one if _x_<sup>_′_�</sup> _β ≫_ 0 and vice versa.

3

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Support Vector Machines →](03-2-support-vector-machines.md)
