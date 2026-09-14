---
title: 02 exam quiz02 s08
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/02-exam-quiz02-s08.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 02 exam quiz02 s08

**Source:** `exams/02-exam-quiz02-s08.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

�v��� � � {

**Question 1:** Multiple choice questions. **CLEARLY** circle the best answer for each question below. Each question is worth 4 points each, with no partial credit given.

- a. (4 pts) Let _X_ 1, _X_ 2, and _X_ 3 be independent random variables with the continuous uniform distribution over [0 _,_ 1]. Then **P** ( _X_ 1 _< X_ 2 _< X_ 3) =

(i) 1 _/_ 6 (ii) 1 _/_ 3 (iii) 1 _/_ 2 (iv) 1 _/_ 4

b. (4 pts) Let _X_ and _Y_ be two continuous random variables. Then

(i) **E** [ _XY_ ] = **E** [ _X_ ] **E** [ _Y_ ]

(ii) **E** [ _X_<sup>2</sup> + _Y_<sup>2</sup> ] = **E** [ _X_<sup>2</sup> ] + **E** [ _Y_<sup>2</sup> ] (iii) _fX_ + _Y_ ( _x_ + _y_ ) = _fX_ ( _x_ ) _fY_ ( _y_ )

(iv) var( _X_ + _Y_ ) = var( _X_ ) + var( _Y_ )

- c. (4 pts) Suppose _X_ is uniformly distributed over [0 _,_ 4] and _Y_ is uniformly distributed over [0 _,_ 1]. Assume _X_ and _Y_ are independent. Let _Z_ = _X_ + _Y_ . Then

   - (i) _fZ_ (4 _._ 5) = 0

(ii) _fZ_ (4 _._ 5) = 1 _/_ 8 (iii) _fZ_ (4 _._ 5) = 1 _/_ 4 (iv) _fZ_ (4 _._ 5) = 1 _/_ 2

- d. (4 pts) For the random variables defined in part (c), **P** (max( _X, Y_ ) _>_ 3) is equal to

(i) 0 (ii) 9 _/_ 4 (iii) 3 _/_ 4 (iv) 1 _/_ 4

- e. (4 pts) Consider the following variant of the hat problem from lecture: _N_ people put their hats in a closet at the start of a party, where each hat is uniquely identified. At the end of the party each person randomly selects a hat from the closet. Suppose _N_ is a Poisson random variable with parameter _λ_ . If _X_ is the number of people who pick their own hats, then **E** [X] is equal to

   - (i) _λ_

   - (ii) 1 _/λ_<sup>2</sup>

   - (iii) 1 _/λ_ (iv) 1

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �v��� � � {

- f. (4 pts) Suppose _X_ and _Y_ are Poisson random variables with parameters _λ_ 1 and _λ_ 2 respectively, where _X_ and _Y_ are independent. Define _W_ = _X_ + _Y_ , then

   - (i) _W_ is Poisson with parameter min( _λ_ 1 _, λ_ 2)

   - (ii) _W_ is Poisson with parameter _λ_ 1 + _λ_ 2

(iii) _W_ may not be Poisson but has mean equal to min( _λ_ 1 _, λ_ 2)

   - (iv) _W_ may not be Poisson but has mean equal to _λ_ 1 + _λ_ 2

- g. (4 pts) Let _X_ be a random variable whose transform is given by _MX_ ( _s_ ) = (0 _._ 4 + 0 _._ 6 _e_<sup>_s_</sup> )<sup>50</sup> . Then

(i) **P** ( _X_ = 0) = **P** ( _X_ = 50) (ii) **P** ( _X_ = 51) _>_ 0 (iii) **P** ( _X_ = 0) = (0 _._ 4)<sup>50</sup> (iv) **P** ( _X_ = 50) = 0 _._ 6

- h. (4 pts) Let _Xi, i_ = 1 _,_ 2 _, . . ._ be independent random variables all distributed according to the pdf _fX_ ( _x_ ) = _x/_ 8 for 0 _≤ x ≤_ 4. Let _S_ = 100<sup><u>1</u>�</sup> _i_<sup>100</sup> =1 _Xi_ . Then **P** ( _S >_ 3) is approximately equal to

(i) 1 _−_ Φ(5) (iii)(ii) Φ(5)1 _−_ Φ <u>�</u> _~~√~~_ 52 � (iv) Φ � _~~√~~_ 52 �

i. (4 pts) Let _Xi, i_ = 1 _,_ 2 _, . . ._ be independent random variables all distributed according to the pdf _fX_ ( _x_ ) = 1 _,_ 0 _≤ x ≤_ 1. Define _Yn_ = _X_ 1 _X_ 2 _X_ 3 _. . . Xn_ , for some integer _n_ . Then var( _Yn_ ) is equal to _n_ (i) 12 1 1 (ii) 3 _n −_ 4 _n_ 1 (iii) 12 _n_ 1 (iv) 12

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �v��� � � {

**Question 2:** Each Mac book has a lifetime that is exponentially distributed with parameter _λ_ . The lifetime of Mac books are independent of each other. Suppose you have two Mac books, which you begin using at the same time. Define _T_ 1 as the time of the first ~~laptop~~ failure and _T_ 2 as the time of the second ~~laptop~~ failure.

- a. (4 pts) Compute _fT_ 1( _t_ 1)

- b. (5 pts) Let _X_ = _T_ 2 _− T_ 1. Compute _fX|T_ 1( _x|t_ 1)

- c. (5 pts) Is _X_ independent of _T_ 1? Give a mathematical justification for your answer.

- d. (8 pts) Compute _fT_ 2( _t_ 2) and **E** [ _T_ 2]

- e. (5 pts) Now suppose you have 100 Mac books, and let _Y_ be the time of the first laptop failure. Find the best answer for **P** ( _Y <_ 0 _._ 01)

Your friend, Charlie, loves Mac books so much he buys _S_ new Mac books every day! On any given day _S_ is equally likely to be 4 or 8, and all days are independent from each other. Let _S_ 100 be the number of Mac books Charlie buys over the next 100 days.

- f. (6 pts) Find the best approximation for **P** ( _S_ 100 _≤_ 608). Express your final answer in terms of _·_

- Φ( ), the CDF of the standard normal.

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

�v��� � � {

**Question 3:** Saif is a well intentioned though slightly indecisive fellow. Every morning he flips a coin to decide where to go. If the coin is heads he drives to the mall, if it comes up tails he volunteers at the local shelter. Saif’s coin is not necessarily fair, rather it possesses a probability of heads equal to _q_ . We do not know _q_ , but we do know it is well-modeled by a random variable _Q_ where the density of _Q_ is


Assume conditioned on _Q_ each coin flip is independent. Note parts a, b, c, and _{d, e}_ may be answered independent of each other.

a. (4 pts) What’s the probability that Saif goes to the local shelter if he flips the coin once?

In an attempt to promote virtuous behavior, Saif’s father offers to pay him $4 every day he volunteers at the local shelter. Define _X_ as Saif’s payout if he flips the coin every morning for the next 30 days.

b. (6 pts) Find var( _X_ )

Let event _B_ be that Saif goes to the local shelter at least once in _k_ days.

- c. (6 pts) Find the conditional density of _Q_ given _B_ , _fQ B|_ ( _q_ )

While shopping at the mall, Saif gets a call from his sister Mais. They agree to meet at the Coco Cabana Court yard at exactly 1:30PM. Unfortunately Mais arrives _Z_ minutes late, where _Z_ is a continuous uniform random variable from zero to 10 minutes. Saif is furious that Mais has kept him waiting, and demands Mais pay him _R_ dollars where _R_ = exp( _Z_ + 2).

- d. (6 pts) Find Saif’s expected payout, **E** [ _R_ ]

- e. (6 pts) Find the density of Saif’s payout, _fR_ ( _r_ )

4

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
