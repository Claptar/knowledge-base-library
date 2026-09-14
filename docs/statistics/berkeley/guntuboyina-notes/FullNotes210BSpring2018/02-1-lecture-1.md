---
title: 1 Lecture 1
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Lecture 1

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The first topic of the class will be _Empirical Process Theory_ . I will give a high-level overview of what we plan to cover in the empirical processes part of the class.

## **1.1 Some Aspects of Empirical Process Theory**

Empirical process theory usually deals with two fundamental questions.

### **1.1.1 Uniform Laws of Large Numbers**

The first question concerns uniform strong laws of large numbers. Suppose _X_ 1 _, X_ 2 _, . . ._ are independent and identically distributed random objects taking values in a set _X_ . Let _F_ denote a class of real-valued functions on _X_ . What can one say about the random variable:


Specifically,

1. Does the random variable (5) concentrate around its expectation?

2. Can one provide _finite-sample_ (i.e., bounds that hold for every _n_ ) bounds for (5) in terms of the class of functions _F_ and the common distribution _P_ of _X_ 1 _, X_ 2 _, . . ._ ?

3. Can one provide conditions on _F_ such that (5) converges to zero in probability or almost surely (if this is true, we say that the uniform strong law of large numbers holds)?

Empirical process theory provides answers to these questions. Why are these questions relevant to theoretical statistics? The two examples that we shall study in detail are given below.

**Example 1.1** (Classification) **.** _Consider a pair of random objects X and Y having some joint distribution where X takes values in a space X and Y takes only the two values: −_ 1 _or_ +1 _. A classifier is a function g_ : _X →{−_ 1 _,_ +1 _}. The error of the classifier is given by_


5

_The goal of classification is to construct a classifier with small error based on n i.i.d observations_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _having the same distribution as_ ( _X, Y_ ) _._

_For a classifier g, its empirical error (i.e., its error on the observed sample) is given by_


_A natural strategy for classification is to select a class of classifiers C and then to choose the classifier in C which has the smallest empirical error on the observed sample i.e.,_


_How good a classifier is g_ ˆ _n i.e., how small is its error:_


_Two questions are relevant about L_ (ˆ _gn_ ) _:_

_1. Is L_ (ˆ _gn_ ) _comparable to_ inf _g∈C L_ ( _g_ ) _? i.e., is the error of g_ ˆ _n comparable to the best achievable error in the class C?_

_2. is L_ (ˆ _gn_ ) _comparable to Ln_ (ˆ _gn_ ) _? i.e., is the error of g_ ˆ _n comparable its “in-sample” empirical error?_

_It is quite easy to relate these two questions to the size of_ sup _g∈C |Ln_ ( _g_ ) _−L_ ( _g_ ) _|. Indeed, if g_<sup>_∗_</sup> := argmin _g∈C L_ ( _g_ ) _, then_


_Also_


_Thus the key quantity to answering the above questions is_


_It is now easy to see that the above quantity is a special case of_ (5) _when F is taken to be the class of all functions I{g_ ( _x_ ) _̸_ = _y} as g varies over C. Also the Xis in_ (5) _need to be replaced by_ ( _Xi, Yi_ ) _._

_Sometimes, the two inequalities above can sometimes be quite loose. Later, we shall see more sharper inequalities which utilize a technique known as “localization”._

**Example 1.2** (Consistency and Rates of convergence of M-estimators) **.** _Many problems in statistics are concerned with estimators of the form_


_for i.i.d observations X_ 1 _, . . . , Xn taking values in a space X . Here_ Θ _denotes the parameter space and, for each θ ∈_ Θ _, mθ denotes a real-valued function (known as a loss or criterion function) on X . Such an estimator θ_<sup>ˆ</sup> _is called an M -estimator as it is obtained by maximizing an objective function. The most standard examples of M -estimators are:_

_1._ **_Maximum Likelihood Estimators_** _: These correspond to mθ_ ( _x_ ) := log _pθ_ ( _x_ ) _for a class of densities {pθ, θ ∈_ Θ _} on X ._

6

_2._ **_Location Estimators_** _:_

   - _(a)_ **_Mean_** _: corresponds to mθ_ ( _x_ ) := ( _x − θ_ )<sup>2</sup> _._

   - _(b)_ **_Median_** _: corresponds to mθ_ ( _x_ ) := _|x − θ|._

   - _(c)_ **_Mode_** _: may correspond to mθ_ ( _x_ ) := _I{|x − θ| ≤_ 1 _}._

_The target quantity for the estimator θ_<sup>ˆ</sup> _n is_


_The main question of interest while studying M -estimators concerns the accuracy of θ_<sup>ˆ</sup> _n for estimating θ_ 0 _. In the asymptotic framework (n →∞), the two key questions are:_

_1. Is θ_<sup>ˆ</sup> _n consistent for estimating θ_ 0 _i.e., does d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) _converge to zero almost surely or in probability as n →∞? Here d_ ( _·, ·_ ) _is a metric on_ Θ _(for example, the usual Euclidean metric when_ Θ _is a subset of_ R<sup>_k_</sup> _for some k)._

_2. What is the rate of convergence of d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) _? For example, is it Op_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> ) _? or Op_ ( _n_<sup>_−_1</sup><sup>_/_3</sup> ) _?._

_To answer these questions, it is obvious that one must investigate the closeness of_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_mθ_(</sup><sup>_Xi_)</sup><sup>_/n to_E</sup><sup>_mθ_(</sup><sup>_X_1)</sup> _in some sort of uniform sense over θ which leads to investigation of_ (5) _for appropriate subclasses F of {mθ, θ ∈_ Θ _}._

_Indeed, the standard argument involves first writing_


_where_


_One then bounds the right hand side of_ (3) _by_


_Empirical process results provide bounds for the above probability (some assumptions on the relation between M and the metric d will be needed)._

_Note that one can further bound the above probability by replacing the left hand side by_


_but this can sometimes be too loose._

The strategy for controlling (5) is as follows (we will mostly focus on the case when _F_ is a uniformly bounded class of functions):

1. The key observation is that the random variable (5) “concentrates” around its mean (or expectation).

2. Because of concentration, it is enough to control the mean of (5). The mean will be bounded by a quantity called “Rademacher Complexity” of _F_ via a technique called “symmetrization”.

7

3. The Rademacher complexity involves the expected supremum over a “sub-Gaussian process”. This is further controlled via a technique known as “chaining”. In the process, we shall also encounter a quantity known as the “Vapnik-Chervonenkis dimension”.

The best reference for these topics is the book Boucheron et al. [3]. The viewpoint that we shall take is the nonasymptotic viewpoint where bounds are proved which hold for every _n_ . The more classical viewpoint is the asymptotic one where statements are made that hold as _n →∞_ . In the asymptotic viewpoint, it is said that the class _F_ is “Glivenko-Cantelli” provided (5) converges almost surely as _n →∞_ . Using our nonasymptotic bounds, it will be possible to put appropriate conditions on _F_ under which _F_ becomes a Glivenko-Cantelli class.

---

[← Contents](01-contents.md) · [Up: contents](index.md) · [2 Lecture 2 →](03-2-lecture-2.md)
