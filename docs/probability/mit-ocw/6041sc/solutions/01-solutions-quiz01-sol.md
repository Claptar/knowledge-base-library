---
title: 01 solutions quiz01 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/01-solutions-quiz01-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 01 solutions quiz01 sol

**Source:** `solutions/01-solutions-quiz01-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Quiz 1 Solutions | Fall 2010)

Quiz 1 Solutions: October 12, 2010

Problem 1.

1. (10 points) Let Ri be the amount of time Stephen spends at the ith red light. Ri is a Bernoulli random variable with p = 1/3. The PMF for Ri is:


The expectation and variance for Ri are:


Let TS be the total length of time of Stephen’s commute in minutes. Then,


TS is a shifted binomial with n = 5 trials and p = 1/3. The PMF for TS is then:

The expectation and variance for TS are:


2. (10 points) Let N be the number of red lights Stephen encountered on his commute. Given that TS ≤ 19, then N = 0 or N = 1. The unconditional probability of N = 0 is P(N = 0) = ( 23 )5. The unconditional probability of N = 1 is P(N = 1) = �15<sup>�</sup> ( 32 )4( 13 )1.

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Quiz 1 Solutions | Fall 2010)

To find the conditional expectation, the following conditional PDF is calculated:


Therefore,


3. (10 points) Given that the last red light encountered by Stephen was the fourth light, R4 = 1 and R5 = 0.

We are asked to compute var(N | {R4 = 1} ∩{R5 = 0}). Therefore,


4. (10 points) Under the given condition, the discrete uniform law can be used to compute the probability of interest. There are �53� ways that Stephen can encounter a total of three red lights. There are ��32 ways that two out of the first three lights were red. This leaves one additional red light out of the last two lights and there are �12� possible ways that this event can occur. Putting it all together,


5. (5 points) Let TJ be the total length of time of Jon’s commute in minutes. The PMF of Jon’s commute is:


6. (10 points) Let A be the event that Jon arrives at work in 20 minutes and let B be the event that exactly one person arrives in 20 minutes.


2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Quiz 1 Solutions | Fall 2010)

Jon arrives at work in 20 minutes (or TJ = 20) if he does not have to wait for the train at the station (or X = 0). The probability of this event occurring is:


Stephen arrives at work in 20 minutes if he encounters 2 red lights. The probability of this event is a binomial probability:

Thus,


7. (10 points) The probability of interest is P(TS ≤ TJ ). This can be calculated using the total probability theorem by conditioning on the length of Jon’s commute or Jon’s wait at the station. If Jon’s commute is 20 minutes (or X = 0), then Stephen can encounter up to 2 red lights to satisfy TS ≤ TJ . Similarly if Jon’s commute is 21 minutes (or X = 1), Stephen can encounter up to 3 red lights and so on.


An alternative approach follows. We first compute the joint PMF of the commute times of Stephen and Jon PTS ,TJ (k, ℓ). Because of independence, PTS ,TJ (k, ℓ) = PTS (k)PTJ (ℓ). Therefore,


8. (10 points) We express the conditional probability as such:


3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Quiz 1 Solutions | Fall 2010)

If Jon waited 3 minutes at the train, his commute was 23 minutes and Stephen’s commute takes at most as long as Jon’s commute since the longest possible commute for Stephen is 23 minutes. Therefore, the numerator in the previous expression is equal to P(X = 3) =<sup>1</sup> 4<sup>.The denominator</sup> was computed in the previous part.


Problem 2.

1. (10 points) Always True. We need to show that


We start with expressing P(A) as P(A ∩ B) + P(A ∩ B<sup>c</sup> ). Therefore,


which shows that A and B<sup>c</sup> are independent.

2. (10 points) Not Always True. Using the diagram below, let C = A ∩ B and let P(A) > P(C) and let P(B) > P(C). The conditional probability P(A ∩ B | C) = 1. Furthermore, P(A | C) = 1 and P(B | C) = 1. Since P(A ∩ B | C) = P(A | C)P(B | C), A and B are conditionally independent given a third event C. Given C<sup>c</sup> , A and B are disjoint which means that A and B are not independent.


The following is an alternative counterexample. Imagine having 3 coins with the following probabil­ ity of heads: p = 1/5, p = 1/3 and p = 2/3, respectively. Each coin has equal probability of being selected. Let C be the event that you select the coin with p = 1/5. Let C<sup>c</sup> be the event that you choose one of the other two coins. Let A be the event that the first coin toss results in heads. Let B be the event that the second coin toss results in heads. For a given coin, the tosses are independent such that:

P(B | A ∩ C) = P(B | C).

4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Quiz 1 Solutions | Fall 2010)

Given C<sup>c</sup> , A and B are not independent since we can have either the p = 1/3 coin or the p = 2/3 coin. Knowing A changes our beliefs of the result of the second coin toss.


However,


As shown, P(B | A ∩ C<sup>c</sup> ) = P(B | C<sup>c</sup> ).

3. (10 points) Always True. Using independence of X and Y , var(X + Y ) = var(X) + var(Y ). Since variance is always non-negative, var(X) + var(Y ) ≥ var(X).

5

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
