---
title: Question 2
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions-qu02-s08-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 2

**Source:** `solutions/02-solutions-qu02-s08-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Each Mac book has a lifetime that is exponentially distributed with parameter _λ_ . The lifetime of Mac books are independent of each other. Suppose you have two Mac books, which you begin using at the same time. Define _T_ 1 as the time of the first ~~laptop~~ failure and _T_ 2 as the time of the second ~~laptop~~ failure.

a. Compute _fT_ 1( _t_ 1).

## **Solution**

Let _M_ 1 be the life time of mac book 1 and _M_ 2 the lifetime of mac book 2, where _M_ 1 and _M_ 2 are iid exponential random variables with CDF _FM_ ( _m_ ) = 1 _− e_<sup>_−λm_</sup> _. T_ 1, the time of the first mac book failure, is the minimum of _M_ 1 and _M_ 2 _._ To derive the distribution of _T_ 1 _,_ we first find the CDF _FT_ 1( _t_ ), and then differentiate to find the PDF _fT_ 1( _t_ ) _._


Differentiating _FT_ 1( _t_ ) with respect to _t_ yields:


4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 2 Solutions | Spring 2008)

- b. Let _X_ = _T_ 2 _− T_ 1. Compute _fX|T_ 1( _x|t_ 1).

**Solution**

Conditioned on the time of the first mac book failure, the time until the other mac book fails is an exponential random variable by the memoryless property. The memoryless property tells us that regardless of the elapsed life time of the mac book, the time until failure has the same exponential CDF. Consequently,


- c. Is _X_ independent of _T_ 1? Give a mathematical justification for your answer. **Solution**

Since we have shown in 2(c) that _fX|T_ 1( _x | t_ ) does not depend on _t_ , _X_ and _T_ 1 are independent.

- d. Compute _fT_ 2( _t_ 2) and **E** [ _T_ 2].

## **Solution**

The time of the second laptop failure _T_ 2 is equal to _T_ 1 + _X._ Since _X_ and _T_ 1 were shown to be independent in 2(b), we convolve the densities found in 2(a) and 2(b) to determine _fT_ 2( _t_ ) _._


An equivalent method for solving this problem is to note that _T_ 2 is the maximum of _M_ 1 and _M_ 2 _,_ and deriving the distribution of _T_ 2 in our standard CDF to PDF method:


Differentiating _FT_ 2( _t_ ) with respect to _t_ yields:


which is equivalent to our solution by convolution above. Finally, from the above density we obtain that **E** [ _T_ 2] = _λ_ <u>2</u> _−_ 21 _λ_ = 23 _λ_ , which matches our earlier solution.

5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 2 Solutions | Spring 2008)

- e. Now suppose you have 100 Mac books, and let _Y_ be the time of the first laptop failure. Find the best answer for **P** ( _Y <_ 0 _._ 01)

**Solution**

_Y_ is equal to the minimum of 100 independent exponential random variables. Following the derivation in (a), we determine by analogy:


Integrating over _y_ from 0 to .01, we find **P** ( _Y < ._ 01) = 1 _− e_<sup>_−λ_</sup> _._

Your friend, Charlie, loves Mac books so much he buys _S_ new Mac books every day! On any given day _S_ is equally likely to be 4 or 8, and all days are independent from each other. Let _S_ 100 be the number of Mac books Charlie buys over the next 100 days.

- f. (6 pts) Find the best approximation for **P** ( _S_ 100 _≤_ 608). Express your final answer in terms of _·_

- Φ( ), the CDF of the standard normal.

**Solution**

Using the De Moivre - Laplace Approximation to the Binomial, and noting that the step size between values that S can take on is 4,

---

[← Question 1](01-question-1.md) · [Up: contents](index.md) · [Question 3 →](03-question-3.md)
