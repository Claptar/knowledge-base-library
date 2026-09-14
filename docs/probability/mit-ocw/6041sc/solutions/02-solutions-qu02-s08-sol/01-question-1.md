---
title: Question 1
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions-qu02-s08-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 1

**Source:** `solutions/02-solutions-qu02-s08-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Multiple choice questions. **CLEARLY** circle the best answer for each question below. Each question is worth 4 points each, with no partial credit given.

- a. Let _X_ 1, _X_ 2, and _X_ 3 be independent random variables with the continuous uniform distribution over [0 _,_ 1]. Then **P** ( _X_ 1 _< X_ 2 _< X_ 3) =

   - (i) 1 _/_ 6

   - (ii) 1 _/_ 3

(iii) 1 _/_ 2

(iv) 1 _/_ 4

**Solution:** To understand the principle, first consider a simpler problem with _X_ 1 and _X_ 2 as given above. Note that **P** ( _X_ 1 _< X_ 2) + **P** ( _X_ 2 _< X_ 1) + **P** ( _X_ 1 = _X_ 2) = 1 since the corresponding events are disjoint and exaust all the possibilities. But **P** ( _X_ 1 _< X_ 2) = **P** ( _X_ 2 _< X_ 1) by symmetry. Furthermore, **P** ( _X_ 1 = _X_ 2) = 0 since the random variables are continuous. Therefore, **P** ( _X_ 1 _< X_ 2) = 1 _/_ 2.

Analogously, omitting the events with zero probability but making sure to exhaust all other possibilities, we have that **P** ( _X_ 1 _< X_ 2 _< X_ 3) + **P** ( _X_ 1 _< X_ 3 _< X_ 2) + **P** ( _X_ 2 _< X_ 1 _< X_ 3) + **P** ( _X_ 2 _< X_ 3 _< X_ 1) + **P** ( _X_ 3 _< X_ 1 _< X_ 2) + **P** ( _X_ 3 _< X_ 2 _< X_ 1) = 1. And, by symmetry, **P** ( _X_ 1 _< X_ 2 _< X_ 3) = **P** ( _X_ 1 _< X_ 3 _< X_ 2) = **P** ( _X_ 2 _< X_ 1 _< X_ 3) = **P** ( _X_ 2 _< X_ 3 _< X_ 1) = **P** ( _X_ 3 _< X_ 1 _< X_ 2) = **P** ( _X_ 3 _< X_ 2 _< X_ 1). Thus, **P** ( _X_ 1 _< X_ 2 _< X_ 3) = 1 _/_ 6.

b. Let _X_ and _Y_ be two continuous random variables. Then

(i) **E** [ _XY_ ] = **E** [ _X_ ] **E** [ _Y_ ]


(iii) _fX_ + _Y_ ( _x_ + _y_ ) = _fX_ ( _x_ ) _fY_ ( _y_ )

(iv) var( _X_ + _Y_ ) = var( _X_ ) + var( _Y_ )

**Solution:** Since _X_<sup>2</sup> and _Y_<sup>2</sup> are random variables, the result follows by the linearity of expecta­ tion.

- c. Suppose _X_ is uniformly distributed over [0 _,_ 4] and _Y_ is uniformly distributed over [0 _,_ 1]. Assume _X_ and _Y_ are independent. Let _Z_ = _X_ + _Y_ . Then


(ii) _fZ_ (4 _._ 5) = 1 _/_ 8 (iii) _fZ_ (4 _._ 5) = 1 _/_ 4

(iv) _fZ_ (4 _._ 5) = 1 _/_ 2

**Solution:** Since _X_ and _Y_ are independent, the result follows by convolution:


1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 2 Solutions | Spring 2008)

d. For the random variables defined in part (c), **P** (max( _X, Y_ ) _>_ 3) is equal to

(i) 0 (ii) 9 _/_ 4 (iii) 3 _/_ 4

(iv) 1 _/_ 4

**Solution:** Note that **P** (max( _X, Y_ ) _>_ 3) = 1 _−_ **P** (max( _X, Y_ ) _≤_ 3) = 1 _−_ **P** ( _{X ≤_ 3 _} ∩{Y ≤_ 3 _}_ ). But, _X_ and _Y_ are independent, so **P** ( _{X ≤_ 3 _} ∩{Y ≤_ 3 _}_ ) = **P** ( _X ≤_ 3) **P** ( _Y ≤_ 3). Finally, computing the probabilities, we have **P** ( _X ≤_ 3) = 3 _/_ 4 and **P** ( _X ≤_ 3) = 1. Thus, **P** (max( _X, Y_ ) _>_ 3) = 1 _−_ 3 _/_ 4 = 1 _/_ 4.

- e. Recall the hat problem from lecture: _N_ people put their hats in a closet at the start of a party, where each hat is uniquely identified. At the end of the party each person randomly selects a hat from the closet. Suppose _N_ is a Poisson random variable with parameter _λ_ . If _X_ is the number of people who pick their own hats, then **E** [X] is equal to

   - (i) _λ_

   - (ii) 1 _/λ_<sup>2</sup>

(iii) 1 _/λ_

(iv) 1

**Solution:** Let _X_ = _X_ 1 + _. . ._ + _XN_ where each _Xi_ is the indicator function such that _Xi_ = 1 if the _i_<sup>th</sup> person picks their own hat and _Xi_ = 0 otherwise. By the linearity of the expectation, **E** [ _X | N_ = _n_ ] = **E** [ _X_ 1 _| N_ = _n_ ] + _. . ._ + **E** [ _XN | N_ = _n_ ]. But **E** [ _Xi | N_ = _n_ ] = 1 _/n_ for all _i_ = 1 _, . . . , n_ . Thus, **E** [ _X | N_ = _n_ ] = _n_ **E** [ _Xi | N_ = _n_ ] = 1. Finally, **E** [ _X_ ] = **E** [ **E** [ _X | N_ = _n_ ]] = 1.

- f. Suppose _X_ and _Y_ are Poisson random variables with parameters _λ_ 1 and _λ_ 2 respectively, where _X_ and _Y_ are independent. Define _W_ = _X_ + _Y_ , then

   - (i) _W_ is Poisson with parameter min( _λ_ 1 _, λ_ 2)

   - (ii) _W_ is Poisson with parameter _λ_ 1 + _λ_ 2

   - (iii) _W_ may not be Poisson but has mean equal to min( _λ_ 1 _, λ_ 2)

   - (iv) _W_ may not be Poisson but has mean equal to _λ_ 1 + _λ_ 2

**Solution:** The quickest way to obtain the answer is through transforms: _MX_ ( _s_ ) = _e_<sup>_λ_1(</sup><sup>_es−_1)</sup> and _MY_ ( _s_ ) = _e_<sup>_λ_2(</sup><sup>_es−_1)</sup> . Since _X_ and _Y_ are independent, we have that _MW_ ( _s_ ) = _e_<sup>_λ_1(</sup><sup>_es−_1)</sup> _e_<sup>_λ_2(</sup><sup>_es−_1)</sup> = _e_<sup>(</sup><sup>_λ_1+</sup><sup>_λ_2)(</sup><sup>_es−_1)</sup> , which equals the transform of a Poisson random variable with mean _λ_ 1 + _λ_ 2.

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Quiz 2 Solutions | Spring 2008)

- g. Let _X_ be a random variable whose transform is given by _MX_ ( _s_ ) = (0 _._ 4 + 0 _._ 6 _e_<sup>_s_</sup> )<sup>50</sup> . Then

   - (i) **P** ( _X_ = 0) = **P** ( _X_ = 50)

(ii) **P** ( _X_ = 51) _>_ 0


(iv) **P** ( _X_ = 50) = 0 _._ 6

**Solution:** Note that _MX_ ( _s_ ) is the transform of a binomial random variable _X_ with _n_ = 50 trials and the probability of success _p_ = 0 _._ 6. Thus, **P** ( _X_ = 0) = 0 _._ 4<sup>50</sup> .

- h. Let _Xi, i_ = 1 _,_ 2 _, . . ._ be independent random variables all distributed according to the PDF _fX_ ( _x_ ) = _x/_ 8 for 0 _≤ x ≤_ 4. Let _S_ = 1001<sup>�</sup> _i_ 100=1 _Xi_ . Then **P** ( _S >_ 3) is approximately equal to

(i) 1 _−_ Φ(5)

(ii) Φ(5)


Therefore,


and


3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Quiz 2 Solutions | Spring 2008)

- i. Let _Xi, i_ = 1 _,_ 2 _, . . ._ be independent random variables all distributed according to the PDF _fX_ ( _x_ ) = 1 _,_ 0 _≤ x ≤_ 1. Define _Yn_ = _X_ 1 _X_ 2 _X_ 3 _. . . Xn_ , for some integer _n_ . Then var( _Yn_ ) is equal to


**Solution:** Since _X_ 1 _, . . . , Xn_ are independent, we have that **E** [ _Yn_ ] = **E** [ _X_ 1] _× . . . ×_ **E** [ _Xn_ ]. Sim­ ilarly, **E** [ _Yn_<sup>2</sup> ] = **E** [ _X_ 1<sup>2</sup> ] _× . . . ×_ **E** [ _Xn_<sup>2</sup> ]. Since **E** [ _Xi_ ] = 1 _/_ 2 and **E** [ _Xi_<sup>2</sup> ] = 1 _/_ 3 for _i_ = 1 _, . . . , n_ , it 1 1 follows that var( _Sn_ ) = **E** [ _Yn_ 2] _−_ ( **E** [ _Yn_ ])2 = 3<sup>_n_</sup> _−_ 4 _n_ .

---

[Up: contents](index.md) · [Question 2 →](02-question-2.md)
