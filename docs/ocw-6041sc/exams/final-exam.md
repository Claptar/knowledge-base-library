---
title: Final exam
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/final-exam.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Final exam

**Source:** `exams/final-exam.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Final Exam | Fall 2010)

**Problem 1. (32 points)** Consider a Markov chain _{Xn_ ; _n_ = 0 _,_ 1 _, . . .}_ , specified by the following transition diagram.


<!-- Start of picture text -->
0.5 0.9<br>0.6<br>0.3<br>0.4<br>1 2 3<br>0.1<br>0.2<br><!-- End of picture text -->

1. **(4 points)** Given that the chain starts with _X_ 0 = 1, find the probability that _X_ 2 = 2.

2. **(4 points)** Find the steady-state probabilities _π_ 1, _π_ 2, _π_ 3 of the different states.

_In case you did not do part (b) correctly, in_ **all** _subsequent parts of this problem you can just use the symbols πi: you do not need to plug in actual numbers._

3. **(4 points)** Let _Yn_ = _Xn − Xn−_ 1. Thus, _Yn_ = 1 indicates that the _n_ th transition was to the right, _Yn_ = 0 indicates it was a self-transition, and _Yn_ = _−_ 1 indicates it was a transition to the left. Find lim **P** ( _Yn_ = 1). _n→∞_

4. **(4 points)** Is the sequence _Yn_ a Markov chain? Justify your answer.

5. **(4 points)** Given that the _n_ th transition was a transition to the right ( _Yn_ = 1), find the probability that the previous state was state 1. (You can assume that _n_ is large.)

6. **(4 points)** Suppose that _X_ 0 = 1. Let _T_ be defined as the first _positive time_ at which the state is again equal to 1. Show how to find **E** [ _T_ ]. (It is enough to write down whatever equation(s) needs to be solved; you do not have to actually solve it/them or to produce a numerical answer.)

7. **(4 points)** Does the sequence _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ converge in probability? If yes, to what? If not, just say “no” without explanation.

8. **(4 points)** Let _Zn_ = max _{X_ 1 _, . . . , Xn}_ . Does the sequence _Z_ 1 _, Z_ 2 _, Z_ 3 _, . . ._ converge in probabil­ ity? If yes, to what? If not, just say “no” without explanation.

**Problem 2. (68 points)** Alice shows up at an Athena * cluster at time zero and spends her time exclusively in typing emails. The times that her emails are sent are a Poisson process with rate _λA_ per hour.

1. **(3 points)** What is the probability that Alice sent exactly three emails during the time interval [1 _,_ 2]?

2. Let _Y_ 1 and _Y_ 2 be the times at which Alice’s first and second emails were sent.

   - (a) **(3 points)** Find **E** [ _Y_ 2 _| Y_ 1].

   - (b) **(3 points)** Find the PDF of _Y_ 12.

   - (c) **(3 points)** Find the joint PDF of _Y_ 1 and _Y_ 2.

1

*Athena is MIT's UNIX-based computing environment. OCW does not provide access to it.

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Final Exam | Fall 2010)

3. You show up at time 1 and you are told that Alice has sent exactly one email so far. (Only give answers here, no need to justify them.)

   - (a) **(3 points)** What is the conditional expectation of _Y_ 2 given this information?

   - (b) **(3 points)** What is the conditional expectation of _Y_ 1 given this information?

4. Bob just finished exercising (without email access) and sits next to Alice at time 1. He starts typing emails at time 1, and fires them according to an independent Poisson process with rate _λB_ .

   - (a) **(5 points)** What is the PMF of the total number of emails sent by the two of them together during the interval [0 _,_ 2]?

   - (b) **(5 points)** What is the expected value of the total typing time associated with the email that Alice is typing at the time that Bob shows up? (Here, “total typing time” includes the time that Alice spent on that email both before and after Bob’s arrival.)

   - (c) **(5 points)** What is the expected value of the time until each one of them has sent at least one email? (Note that we count time starting from time 0, and we take into account any emails possibly sent out by Alice during the interval [0 _,_ 1].)

   - (d) **(5 points)** Given that a total of 10 emails were sent during the interval [0 _,_ 2], what is the probability that exactly 4 of them were sent by Alice?

5. **(5 points)** Suppose that _λA_ = 4. Use Chebyshev’s inequality to find an upper bound on the probability that Alice sent at least 5 emails during the time interval [0 _,_ 1]. Does the Markov inequality provide a better bound?

6. **(5 points)** You do not know _λA_ but you watch Alice for an hour and see that she sent exactly 5 emails. Derive the maximum likelihood estimate of _λA_ based on this information.

7. **(5 points)** We have reasons to believe that _λA_ is a large number. Let _N_ be the number of emails sent during the interval [0 _,_ 1]. Justify why the CLT can be applied to _N_ , and give a precise statement of the CLT in this case.

8. **(5 points)** Under the same assumption as in last part, that _λA_ is large, you can now pretend that _N_ is a normal random variable. Suppose that you observe the value of _N_ . Give an (approx­ imately) 95% confidence interval for _λA_ . State precisely what approximations you are making. _Possibly useful facts:_ The cumulative normal distribution satisfies Φ(1 _._ 645) = 0 _._ 95 and Φ(1 _._ 96) = 0 _._ 975.

9. You are now told that _λA_ is actually the realized value of an exponential random variable Λ, with parameter 2:

      - _f_ Λ( _λ_ ) = 2 _e_<sup>_−_2</sup><sup>_λ_</sup> _, λ ≥_ 0 _._

   - (a) **(5 points)** Find **E** [ _N_<sup>2</sup> ].

   - (b) **(5 points)** Find the linear least squares estimator of Λ given _N_ .

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Final Exam | Fall 2010)

**Problem 1. (32 points)** Consider a Markov chain _{Xn_ ; _n_ = 0 _,_ 1 _, . . .}_ , specified by the following transition diagram.


<!-- Start of picture text -->
0.5 0.9<br>0.6<br>0.3<br>0.4<br>1 2 3<br>0.1<br>0.2<br><!-- End of picture text -->

1. **(4 points)** Given that the chain starts with _X_ 0 = 1, find the probability that _X_ 2 = 2.

2. **(4 points)** Find the steady-state probabilities _π_ 1, _π_ 2, _π_ 3 of the different states.

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

_In case you did not do part (b) correctly, in_ **all** _subsequent parts of this problem you can just use the symbols πi: you do not need to plug in actual numbers._

3. **(4 points)** Let _Yn_ = _Xn − Xn−_ 1. Thus, _Yn_ = 1 indicates that the _n_ th transition was to the right, _Yn_ = 0 indicates it was a self-transition, and _Yn_ = _−_ 1 indicates it was a transition to the left. Find lim **P** ( _Yn_ = 1). _n→∞_

4. **(4 points)** Is the sequence _Yn_ a Markov chain? Justify your answer.

4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

5. **(4 points)** Given that the _n_ th transition was a transition to the right ( _Yn_ = 1), find the probability that the previous state was state 1. (You can assume that _n_ is large.)

6. **(4 points)** Suppose that _X_ 0 = 1. Let _T_ be defined as the first _positive time_ at which the state is again equal to 1. Show how to find **E** [ _T_ ]. (It is enough to write down whatever equation(s) needs to be solved; you do not have to actually solve it/them or to produce a numerical answer.)

5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

7. **(4 points)** Does the sequence _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ converge in probability? If yes, to what? If not, just say “no” without explanation.

8. **(4 points)** Let _Zn_ = max _{X_ 1 _, . . . , Xn}_ . Does the sequence _Z_ 1 _, Z_ 2 _, Z_ 3 _, . . ._ converge in probabil­ ity? If yes, to what? If not, just say “no” without explanation.

6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

*

**Problem 2. (68 points)** Alice shows up at an Athena * cluster at time zero and spends her time exclusively in typing emails. The times that her emails are sent are a Poisson process with rate _λA_ per hour.

1. **(3 points)** What is the probability that Alice sent exactly three emails during the time interval [1 _,_ 2]?

2. Let _Y_ 1 and _Y_ 2 be the times at which Alice’s first and second emails were sent.

   - (a) **(3 points)** Find **E** [ _Y_ 2 _| Y_ 1].

7

*Athena is MIT's UNIX-based computing environment. OCW does not provide access to it.

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Final Exam | Fall 2010)

- (b) **(3 points)** Find the PDF of _Y_ 12.

- (c) **(3 points)** Find the joint PDF of _Y_ 1 and _Y_ 2.

8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

3. You show up at time 1 and you are told that Alice has sent exactly one email so far. (Only give answers here, no need to justify them.)

   - (a) **(3 points)** What is the conditional expectation of _Y_ 2 given this information?

   - (b) **(3 points)** What is the conditional expectation of _Y_ 1 given this information?

9

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Final Exam | Fall 2010)

4. Bob just finished exercising (without email access) and sits next to Alice at time 1. He starts typing emails at time 1, and fires them according to an independent Poisson process with rate _λB_ .

   - (a) **(5 points)** What is the PMF of the total number of emails sent by the two of them together during the interval [0 _,_ 2]?

10

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

- (b) **(5 points)** What is the expected value of the total typing time associated with the email that Alice is typing at the time that Bob shows up? (Here, “total typing time” includes the time that Alice spent on that email both before and after Bob’s arrival.)

11

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

- (c) **(5 points)** What is the expected value of the time until each one of them has sent at least one email? (Note that we count time starting from time 0, and we take into account any emails possibly sent out by Alice during the interval [0 _,_ 1].)

12

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

- (d) **(5 points)** Given that a total of 10 emails were sent during the interval [0 _,_ 2], what is the probability that exactly 4 of them were sent by Alice?

13

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

5. **(5 points)** Suppose that _λA_ = 4. Use Chebyshev’s inequality to find an upper bound on the probability that Alice sent at least 5 emails during the time interval [0 _,_ 1]. Does the Markov inequality provide a better bound?

6. **(5 points)** You do not know _λA_ but you watch Alice for an hour and see that she sent exactly 5 emails. Derive the maximum likelihood estimate of _λA_ based on this information.

14

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Final Exam | Fall 2010)

7. **(5 points)** We have reasons to believe that _λA_ is a large number. Let _N_ be the number of emails sent during the interval [0 _,_ 1]. Justify why the CLT can be applied to _N_ , and give a precise statement of the CLT in this case.

15

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Final Exam | Fall 2010)

8. **(5 points)** Under the same assumption as in last part, that _λA_ is large, you can now pretend that _N_ is a normal random variable. Suppose that you observe the value of _N_ . Give an (approx­ imately) 95% confidence interval for _λA_ . State precisely what approximations you are making. _Possibly useful facts:_ The cumulative normal distribution satisfies Φ(1 _._ 645) = 0 _._ 95 and Φ(1 _._ 96) = 0 _._ 975.

16

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Final Exam | Fall 2010)

9. You are now told that _λA_ is actually the realized value of an exponential random variable Λ, with parameter 2:

_f_ Λ( _λ_ ) = 2 _e_<sup>_−_2</sup><sup>_λ_</sup> _, λ ≥_ 0 _._

- (a) **(5 points)** Find **E** [ _N_<sup>2</sup> ].

17

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Final Exam | Fall 2010)

- (b) **(5 points)** Find the linear least squares estimator of Λ given _N_ .

18

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
