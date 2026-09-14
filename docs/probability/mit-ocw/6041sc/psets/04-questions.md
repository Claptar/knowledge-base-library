---
title: 04 questions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 04 questions

**Source:** `psets/04-questions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Fall</u> 2010)

**Problem Set 4**


1. Random variables _X_ and _Y_ have the joint PMF


   - (a) What is the value of the constant _c_ ?

   - (b) What is **P** ( _Y < X_ )?

   - (c) What is **P** ( _Y > X_ )?

   - (d) What is **P** ( _Y_ = _X_ )?

   - (e) What is **P** ( _Y_ = 3)?

   - (f) Find the marginal PMFs _pX_ ( _x_ ) and _pY_ ( _y_ ).

   - (g) Find the expectations **E** [ _X_ ], **E** [ _Y_ ] and **E** [ _XY_ ].

   - (h) Find the variances var( _X_ ), var( _Y_ ) and var( _X_ + _Y_ ).

   - (i) Let _A_ denote the event _X ≥ Y_ . Find **E** [ _X | A_ ] and var( _X | A_ ).

2. The newest invention of the 6.041/6.431 staff is a three-sided die with faces numbered 1, 2, and 3. The PMF for the result of any one roll of this die is


Consider a sequence of six independent rolls of this die, and let _Xi_ be the random variable corresponding to the _i_ th roll.

   - (a) What is the probability that exactly three of the rolls have result equal to 3?

   - (b) What is the probability that the first roll is 1, given that exactly two of the six rolls have result of 1?

   - (c) We are told that exactly three of the rolls resulted in 1 and exactly three resulted in 2. Given this information, what is the probability that the sequence of rolls is 121212?

   - (d) Conditioned on the event that at least one roll resulted in 3, find the conditional PMF of the number of 3’s.

3. Suppose that _X_ and _Y_ are independent, identically distributed, geometric random variables with parameter _p_ . Show that


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Fall</u> 2010)

   4. Consider 10 independent tosses of a biased coin with a probability of heads of _p_ .

      - (a) Let _A_ be the event that there are 6 heads in the first 8 tosses. Let _B_ be the event that the 9th toss results in heads. Show that events _A_ and _B_ are independent.

      - (b) Find the probability that there are 3 heads in the first 4 tosses and 2 heads in the last 3 tosses.

      - (c) Given that there were 4 heads in the first 7 tosses, find the probability that the 2nd head occurred during the 4th trial.

      - (d) Find the probability that there are 5 heads in the first 8 tosses and 3 heads in the last 5 tosses.

   5. Consider a sequence of independent tosses of a biased coin at times _t_ = 0 _,_ 1 _,_ 2 _, . . ._ . On each toss, the probability of a ’head’ is _p_ , and the probability of a ’tail’ is 1 _− p_ . A reward of one unit is given each time that a ’tail’ follows immediately after a ’head.’ Let _R_ be the total reward paid in times 1 _,_ 2 _, . . . , n_ . Find **E** [ _R_ ] and var( _R_ ).

- G1<sup>_†_</sup> . A simple example of a random variable is the _indicator_ of an event _A_ , which is denoted by _IA_ :


- (a) Prove that two events _A_ and _B_ are independent if and only if the associated indicator random variables, _IA_ and _IB_ are independent.

- (b) Show that if _X_ = _IA_ , then **E** [ _X_ ] = **P** ( _A_ ).

> _†_ Required for 6.431; optional for 6.041

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
