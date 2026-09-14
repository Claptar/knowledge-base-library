---
title: 02 solutions quiz02 sol2
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions-quiz02-sol2.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 02 solutions quiz02 sol2

**Source:** `solutions/02-solutions-quiz02-sol2.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Fall</u> 2010)

# 6.041/6.431 Fall 2010 Quiz 2 Solutions

**Problem 1. (80 points)** In this problem:

(i) _X_ is a (continuous) uniform random variable on [0 _,_ 4].

(ii) _Y_ is an exponential random variable, independent from _X_ , with parameter _λ_ = 2.

1. **(10 points)** Find the mean and variance of _X −_ 3 _Y_ .


2. **(10 points)** Find the probability that _Y ≥ X_ . (Let _c_ be the answer to this question.) The PDFs for _X_ and _Y_ are:


Using the total probability theorem,


Page 1 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

<u>(Fall</u> 2010)

3. **(10 points)** Find the conditional joint PDF of _X_ and _Y_ , given that the event _Y ≥ X_ has occurred.

(You may express your answer in terms of the constant _c_ from the previous part.)

Let _A_ be the event that _Y ≥ X_ . Since _X_ and _Y_ are independent,


4. **(10 points)** Find the PDF of _Z_ = _X_ + _Y_ .

Since _X_ and _Y_ are independent, the convolution integral can be used to find _fZ_ ( _z_ ).


5. **(10 points)** Provide a fully labeled sketch of the conditional PDF of _Z_ given that _Y_ = 3. Given that _Y_ = 3, _Z_ = _X_ + 3 and the conditional PDF of _Z_ is a shifted version of the PDF of _X_ . The conditional PDF of Z and its sketch are:


6. **(10 points)** Find **E** [ _Z | Y_ = _y_ ] and **E** [ _Z | Y_ ].

The conditional PDF _fZ|Y_ = _y_ ( _z_ ) is a uniform distribution between _y_ and _y_ + 4. Therefore,


The above expression holds true for all possible values of _y_ , so


7. **(10 points)** Find the joint PDF _fZ,Y_ of _Z_ and _Y_ .

The joint PDF of _Z_ and _Y_ can be expressed as:


Page 2 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Fall</u> 2010)

8. **(10 points)** A random variable _W_ is defined as follows. We toss a fair coin (independent of _Y_ ). If the result is “heads”, we let _W_ = _Y_ ; if it is tails, we let _W_ = 2 + _Y_ . Find the probability of “heads” given that _W_ = 3.

Let _X_ be a Bernoulli random variable for the result of the fair coin where _X_ = 1 if the coin lands “heads”. Because the coin is fair, **P** ( _X_ = 1) = **P** ( _X_ = 0) = 1 _/_ 2. Furthermore, the conditional PDFs of _W_ given the value of _X_ are:


Using the appropriate variation of Bayes’ Rule:


**Problem 2. (30 points)** Let _X, X_ 1 _, X_ 2 _, . . ._ be independent normal random variables with mean 0 and variance 9. Let _N_ be a positive integer random variable with **E** [ _N_ ] = 2 and **E** [ _N_<sup>2</sup> ] = 5. We assume that the random variables _N, X, X_ 1 _, X_ 2 _, . . ._ are independent. Let _S_ =<sup>�</sup><sup>_N_</sup> _i_ =1<sup>_Xi_.</sup>

1. **(10 points)** If _δ_ is a small positive number, we have **P** (1 _≤|X| ≤_ 1+ _δ_ ) _≈ αδ_ , for some constant _α_ . Find the value of _α_ .

Therefore,


2. **(10 points)** Find the variance of _S_ . Using the Law of Total Variance,


Page 3 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Fall</u> 2010)

3. **(5 points)** Are _N_ and _S_ uncorrelated? Justify your answer.

The covariance of _S_ and _N_ is


since the **E** [ _X_ 1] is 0. Therefore, _S_ and _N_ are uncorrelated.

4. **(5 points)** Are _N_ and _S_ independent? Justify your answer.

_S_ and _N_ are not independent.

_Proof_ : We have var( _S | N_ ) = 9 _N_ and var( _S_ ) = 18, or, more generally, _fS|N_ ( _s | n_ ) = _N_ (0 _,_ 9 _n_ ) and _fS_ ( _s_ ) = _N_ (0 _,_ 18) since a sum of an independent normal random variables is also a normal random variable. Furthermore, since **E** [ _N_<sup>2</sup> ] = 5 = ( **E** [ _N_ ])<sup>2</sup> = 4, _N_ must take more than one value and is not simply a degenerate random variable equal to the number 2. In this case, _N_ can take at least one value (with non-zero probability) that satisfies var( _S | N_ ) = 9 _N_ = var( _S_ ) = 18 and hence _fS|N_ ( _s | n_ ) = _fS_ ( _s_ ). Therefore, _S_ and _N_ are not independent.

Page 4 of 4

MIT OpenCourseWare http://ocw.mit.edu

6.041 / 6.431 Probabilistic Systems Analysis and Applied Probability Fall 2010

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
