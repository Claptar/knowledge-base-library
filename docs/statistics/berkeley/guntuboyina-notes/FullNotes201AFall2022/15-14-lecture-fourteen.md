---
title: 14 Lecture Fourteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 14 Lecture Fourteen

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **14.1 Recap: Last Class**

In the last class, we looked at conditional densities for continuous random variables. Given two continuous random variables _X_ and _Y_ having a joint density _fX,Y_ ( _x, y_ ), the conditional density of _X_ given _Y_ = _y_ is defined as


This definition makes sense when _fY_ ( _y_ ) _>_ 0. Also when _fY_ ( _y_ ) _>_ 0, the above is a valid density in _x_ i.e., _fX|Y_ = _y_ ( _x_ ) _≥_ 0 for all _x_ and


Using the conditional density, the conditional probabilities involving _X_ given _Y_ = _y_ are calculated as:


### **14.2 Law of Total Probability (LTP) and Bayes Rule for Continuous Variables**

Conditional densities are used all over the place in probability and statistics. They are particulary useful while making probability assignments in Bayesian analyses. Here it is convenient to denote the two random variables by Θ and _X_ (as opposed to _X_ and _Y_ ). Θ typically denotes an unobserved parameter while _X_ denotes observed data. A Bayesian analysis starts by making an assignment for the probability distribution of Θ and _X_ . Directly modeling the joint density is usually difficult. One therefore models the marginal distribution

71

of Θ (this is called the prior distribution) and the conditional distribution of _X_ given Θ = _θ_ (this is called the likelihood):


From these, the joint density can be written as


This completely specifies the joint probability distribution of Θ and _X_ . Unspecified quantities such as the marginal distribution of _X_ and the conditional distribution of Θ given _X_ = _x_ are then calculated by using the rules of probability.

For calculating the marginal distribution of _X_ , we use the law of total probability:


For calculating the conditional distribution of Θ given _X_ = _x_ , we use the Bayes rule:


In the statistical context, we shall refer to _f_ Θ _|X_ = _x_ ( _·_ ) as the posterior density of Θ and _fX_ ( _·_ ) as the Evidence.

Here are a simple application of these formulae. More interesting examples will be studied later.

**Example 14.1.** _Suppose_ Θ _∼ N_ ( _µ, τ_<sup>2</sup> ) _and X|_ Θ = _θ ∼ N_ ( _θ, σ_<sup>2</sup> ) _. Then_


_I will sketch the proof of the above results below. The intuition behind the posterior distribution is as follows. For a normal density with mean m and variance v_<sup>2</sup> _, the inverse of the variance_ 1 _/v_<sup>2</sup> _is called the precision. Skinnier normal distributions have high precision and vice versa._

_The formula for the posterior distribution given above implies that the precision of the conditional distribution of_ Θ _given X_ = _x equals the sum of the precisions of the distribution of_ Θ _and the distribution of X respectively which means that the posterior is skinnier compared to the prior and the likelihood normal distributions. Also the mean of the posterior distribution equals a weighted linear combination of the prior mean and the data with the weights being proportional to the precisions._

_To derive the first part of_ (71) _, we use the LTP:_


_Now_


72

_The term in the exponent above can be simplified as_


_where I skipped a few steps to get to the last equality (complete the square and simplify the resulting expressions)._

_As a result_


_Consequently,_


_which gives_


_For the posterior distribution in_ (71) _, we use the Bayes rule (and the above derived expressions for fX|_ Θ= _θ_ ( _x_ ) _f_ Θ( _θ_ ) _and fX_ ( _x_ ) _):_


_which immediately implies:_


### **14.3 LTP and Bayes Rule for general random variables**

The LTP describes how to compute the distribution of _X_ based on knowledge of the conditional distribution of _X_ given Θ = _θ_ as well as the marginal distribution of Θ. The Bayes rule describes how to compute the conditional distribution of Θ given _X_ = _x_ based on the same knowledge of the conditional distribution of _X_ given Θ = _θ_ as well as the marginal distribution of Θ.

We have so far looked at the LTP and Bayes rule when _X_ and Θ are both discrete or when they are both continuous. Now we shall also consider the cases when one of them is discrete and the other is continuous.

73

**14.3.1** _X_ **and** Θ **are both discrete**

The LTP is


and the Bayes rule is


**14.3.2** _X_ **and** Θ **are both continuous**

Here LTP is


and Bayes rule is


#### **14.3.3** _X_ **is discrete while** Θ **is continuous**

LTP is


and Bayes rule is


**14.3.4** _X_ **is continuous while** Θ **is discrete**

LTP is


and Bayes rule is


These formulae are useful when the conditional distribution of _X_ given Θ = _θ_ as well as the marginal distribution of Θ are given as part of the model specification and the goal is to determine the marginal distribution of _X_ as well as the conditional distribution of Θ given _X_ = _x_ .

The following is an example of the LTP and Bayes Rule when Θ is continuous and _X_ is discrete.

74

**Example 14.2.** _Suppose that_ Θ _has the Beta_ ( _α, β_ ) _distribution on_ (0 _,_ 1) _and let X|_ Θ = _θ has the binomial distribution with parameters n and θ. What then is the marginal distribution of X as well as the conditional distribution of_ Θ _given X_ = _x?_

_Note that this is a situation where X is discrete (taking values in_ 0 _,_ 1 _, . . . , n) and_ Θ _is continuous (taking values in the interval_ (0 _,_ 1) _). To compute the marginal distribution of X, we use the appropriate LTP to write (for x_ = 0 _,_ 1 _, . . . , n)_


_Let us now calculate the posterior distribution of_ Θ _given X_ = _x. Using the Bayes rule, we obtain_


_Thus_

---

[← 13 Lecture Thirteen](14-13-lecture-thirteen.md) · [Up: contents](index.md) · [15 Lecture Fifteen →](16-15-lecture-fifteen.md)
