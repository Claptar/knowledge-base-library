---
title: Final f09 exam Part 03 —
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/final-f09-exam.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Final f09 exam Part 03 —

**Source:** `exams/final-f09-exam.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Problem 4.** (30 points)

Al, Bonnie, and Clyde run laps around a track, with the duration of each lap (in hours) being exponentially distributed with parameters _λA_ = 21, _λB_ = 23, and _λC_ = 24, respectively. Assume that all lap durations are independent. At the completion of each lap, a runner drinks either one or two cups of water, with probabilities 1 _/_ 3 and 2 _/_ 3, respectively, independent of everything else, including how much water was consumed after previous laps. (The time spent drinking is negligible, assumed zero.)

- (a) (5 points) Write down the PMF of the total number of completed laps over the first hour.

- (b) (5 points) What is the expected number of cups of water to be consumed by the three runners, in total, over the first hour.

9

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Final Exam | Fall 2009)</u>

- (c) (5 points) Al has amazing endurance and completed 72 laps. Find a good approximation for the probability that he drank at least 130 cups. (You do not have to use 1 _/_ 2-corrections.)

- (d) (5 points) What is the probability that Al finishes his first lap before any of the others?

10

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Final Exam | Fall 2009)</u>

- (e) (5 points) Suppose that the runners have been running for a very long time when you arrive at the track. What is the distribution of the duration of Al’s current lap? (This includes the duration of that lap both before and after the time of your arrival.)

- (f) (5 points) Suppose that the runners have been running for 1/4 hours. What is the distribution of the time Al spends on his second lap, given that he is on his second lap?

11

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Final Exam | Fall 2009)</u>

## **Problem 5.** (25 points)

A pulse of light has energy _X_ that is a second-order Erlang random variable with parameter _λ_ , i.e., its PDF is


This pulse illuminates an ideal photon-counting detector whose output _N_ is a Poisson-distributed random variable with mean _x_ when _X_ = _x_ , i.e., its conditional PMF is


**Useful integral and facts:**


The second-order Erlang random variable satisfies:


(a) (5 points) Find **E** [ _N_ ] and Var[ _N_ ], the unconditional mean and variance of _N_

12

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Final Exam | Fall 2009)</u>

- (b) (5 points) Find _pN_ ( _n_ ), the unconditional PMF of _N_ .

- (c) (5 points) Find _X_<sup>ˆ</sup> lin( _N_ ), the linear least-squares estimator of _X_ based on an observation of _N_ .

13

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Final Exam | Fall 2009)</u>

- (d) (5 points) Find _X_<sup>ˆ</sup> MAP( _N_ ), the MAP estimator of _X_ based on an observation of _N_ .

- (e) (5 points) Instead of the prior distribution in Eq. (1), we are now told that


Given the observation _N_ = 3, and in order to minimize the probability of error, which one of the two hypotheses _X_ = 2 and _X_ = 3 should be chosen?

14

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Final f09 exam Part 02 —](02-final-f09-exam-part-02.md) · [Up: contents](index.md)
