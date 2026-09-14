---
title: 02 solutions qu02 f09 sol Part 02 —
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions-qu02-f09-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 02 solutions qu02 f09 sol Part 02 —

**Source:** `solutions/02-solutions-qu02-f09-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## (Quiz 1 Solutions | Fall 2009)

Differentiating the CDF of Z yields the PDF


Alternatively, you can apply the PDF formula for a strictly monotonic function of a continuous random variable. Recall if _z_ = _g_ ( _x_ ) and _x_ = _h_ ( _z_ ), then


In this problem, _z_ = _e_<sup>2</sup><sup>_x_</sup> and _x_ =<sup><u>1</u></sup> 2<sup>ln</sup><sup>_z_.Notethat</sup><sup>_f_</sup> _Z_<sup>(</sup><sup>_z_)isnonzerofor</sup><sup>_z>_1.Since</sup><sup>_X_isan</sup> exponential random variable with _λ_ = 1, _fX_ ( _x_ ) = _e_<sup>_x_</sup> . Thus,


where the second equality holds since the expression inside the absolute value is always positive for _z ≥_ 1.

**Problem 3.** (10 points)

- (a) (5 points) The quantity **E** [ _X | Y_ ] is always:

   - (i) A number.

   - (ii) A discrete random variable.

   - (iii) A continuous random variable.

   - (iv) Not enough information to choose between (i)-(iii).

If _X_ and _Y_ are not independent, then **E** [ _X | Y_ ] is a function of _Y_ and is therefore a continuous random variable. However if _X_ and _Y_ are independent, then **E** [ _X | Y_ ] = **E** [ _X_ ] which is a number.

- (b) (5 points) The quantity **E** [ **E** [ _X | Y, N_ ] _| N_ ] is always:

   - (i) A number.

   - (ii) A discrete random variable.

   - (iii) A continuous random variable.

   - (iv) Not enough information to choose between (i)-(iii).

If _X_ , _Y_ and _N_ are not independent, then the inner expectation _G_ ( _Y, N_ ) = **E** [ _X | Y, N_ ] is a function of _Y_ and _N_ . Furthermore **E** [ _G_ ( _Y, N_ ) _| N_ ] is a function of _N_ , a discrete random variable. If _X_ , _Y_ and _N_ are independent, then the inner expectation **E** [ _X | Y, N_ ] = **E** [ _X_ ], which is a number. The expectation of a number given _N_ is still a number, which is a special case of a discrete random variable.

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 Solutions | Fall 2009)

**Problem 4.** (25 points)

(a) (i) (5 points)

Using the Law of Iterated Expectations, we have


(ii) (5 points) _X_ is a Bernoulli random variable with a mean _p_ = 21<sup>anditsvarianceisvar(</sup> _X_ ) = _p_ (1 _− p_ ) = 1 _/_ 4.

(b) (7 points)

We know that cov( _X, Q_ ) = **E** [ _XQ_ ] _−_ **E** [ _X_ ] **E** [ _Q_ ], so first let’s calculate **E** [ _XQ_ ]:


Therefore, we have


(c) (8 points) Using Bayes’ Rule, we have


Additionally, we know that


and that for Bernoulli random variables


Thus, the conditional PDF of _Q_ given _X_ = 1 is


**Problem 5.** (21 points)

(a) (7 points)


3

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [02 solutions qu02 f09 sol Part 03 — →](03-02-solutions-qu02-f09-sol-part-03.md)
