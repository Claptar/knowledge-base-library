---
title: Introduction
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/final-f09-exam.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `exams/final-f09-exam.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Final Exam | Fall 2009)</u>

**Problem 2.** (20 points) A pair of jointly continuous random variables, _X_ and _Y_ , have a joint probability density function given by


<!-- Start of picture text -->
y<br>1<br>1 / 2<br>0 1 / 2 1 x<br><!-- End of picture text -->

Figure 1: The shaded region is the domain in which _fX,Y_ ( _x, y_ ) = _c_ .

- (a) (5 points) Find _c_ .

- (b) (5 points) Find the marginal PDFs of _X_ and _Y_ , i.e., _fX_ ( _x_ ) and _fY_ ( _y_ ).

- (c) (5 points) Find **E** [ _X | Y_ = 1 _/_ 4] and Var[ _X | Y_ = 1 _/_ 4], that is, the conditional mean and conditional variance of _X_ given that _Y_ = 1 _/_ 4.

- (d) (5 points) Find the conditional PDF for _X_ given that _Y_ = 3 _/_ 4, i.e., _fX|Y_ ( _x |_ 3 _/_ 4).

**Problem 3.** (25 points)

Consider a Markov chain _Xn_ whose one-step transition probabilities are shown in the figure.


<!-- Start of picture text -->
1<br>4<br>1 1 1<br>3 6<br>1<br>1<br>1 1<br>3 4 3 4<br>1 1<br>3 2 3<br><!-- End of picture text -->

(a) (5 points) What are the recurrent states?

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Final Exam | Fall 2009)</u>

- (b) (5 points) Find **P** ( _X_ 2 = 4 _| X_ 0 = 2).

- (c) (5 points) Suppose that you are given the values of _rij_ ( _n_ ) = **P** ( _Xn_ = _j | X_ 0 = _i_ ). Give a formula for _r_ 11( _n_ + 1) in terms of the _rij_ ( _n_ ).

- (d) (5 points) Find the steady-state probabilities _πj_ = lim _n→∞_ **P** ( _Xn_ = _j | X_ 0 = _i_ ), or explain why they do not exist.

- (e) (5 points) What is the probability of eventually visiting state 4, given that the initial state is _X_ 0 = 1?

**Problem 4.** (30 points)

Al, Bonnie, and Clyde run laps around a track, with the duration of each lap (in hours) being exponentially distributed with parameters _λA_ = 21, _λB_ = 23, and _λC_ = 24, respectively. Assume that all lap durations are independent. At the completion of each lap, a runner drinks either one or two cups of water, with probabilities 1 _/_ 3 and 2 _/_ 3, respectively, independent of everything else, including how much water was consumed after previous laps. (The time spent drinking is negligible, assumed zero.)

- (a) (5 points) Write down the PMF of the total number of completed laps over the first hour.

- (b) (5 points) What is the expected number of cups of water to be consumed by the three runners, in total, over the first hour.

- (c) (5 points) Al has amazing endurance and completed 72 laps. Find a good approximation for the probability that he drank at least 130 cups. (You do not have to use 1 _/_ 2-corrections.)

- (d) (5 points) What is the probability that Al finishes his first lap before any of the others?

- (e) (5 points) Suppose that the runners have been running for a very long time when you arrive at the track. What is the distribution of the duration of Al’s current lap? (This includes the duration of that lap both before and after the time of your arrival.)

- (f) (5 points) Suppose that the runners have been running for 1/4 hours. What is the distribution of the time Al spends on his second lap, given that he is on his second lap?

**Problem 5.** (25 points)

A pulse of light has energy _X_ that is a second-order Erlang random variable with parameter _λ_ , i.e., its PDF is


This pulse illuminates an ideal photon-counting detector whose output _N_ is a Poisson-distributed random variable with mean _x_ when _X_ = _x_ , i.e., its conditional PMF is


- (a) (5 points) Find **E** [ _N_ ] and Var[ _N_ ], the unconditional mean and variance of _N_

- (b) (5 points) Find _pN_ ( _n_ ), the unconditional PMF of _N_ .

- (c) (5 points) Find _X_<sup>ˆ</sup> lin( _N_ ), the linear least-squares estimator of _X_ based on an observation of _N_ .

- (d) (5 points) Find _X_<sup>ˆ</sup> MAP( _N_ ), the MAP estimator of _X_ based on an observation of _N_ .

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Final Exam | Fall 2009)</u>

(e) (5 points) Instead of the prior distribution in Eq. (1), we are now told that


Given the observation _N_ = 3, and in order to minimize the probability of error, which one of the two hypotheses _X_ = 2 and _X_ = 3 should be chosen?

**Useful integral and facts:**


The second-order Erlang random variable satisfies:


Each question is repeated in the following pages. Please write your answer on the appropriate page.

3

---

[Up: contents](index.md) · [Final f09 exam Part 02 — →](02-final-f09-exam-part-02.md)
