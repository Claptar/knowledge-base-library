---
title: 19 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/19-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 19 solutions

**Source:** `solutions/19-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Recitation 19 Solutions: November 16, 2010

1. (a) The Markov chain is shown below.


<!-- Start of picture text -->
1  1<br>9  15<br>1/2<br>1/8  1/8<br>1/4  6-1  1/2<br>3/8  1/8<br>1/8  3/8<br>6-3  3/8  6-2<br>1/8<br><!-- End of picture text -->

By inspection, the states 6-1, 6-2, and 6-3 are all transient, since they each have paths leading to either state 9 or state 15, from which there is no return. Therefore she eventually leaves course 6 with probability 1 .

- (b) This is the absorption probability for the recurrent class consisting of the state course-15. Let us denote the probability of being absorbed by state 15 conditioned on being in state i as ai. Then


Solving this system of equations yields


We will keep the other ai’s around as well - they will be useful later:


Page 1 of 5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

- (c) This is the expected time until absorption for the transient state 6 − 1. Let µi be the expected time until absorption conditioned on being in state i. Then


Solving this system of equations yields


- (d) The student buys one ice cream cone every time she goes from 6-2 to 6-1 or from 6-3 to 6-1, and buys no more than 2 ice cream cones. Let us denote vi(j) as the conditional probability that given that she is in state i, that she transitions from 6 − 2 to 6 − 1 or from 6 − 3 to 6 − 1 j additional times. Then we are interested in the expected value of the random variable N , which denotes the number of cones bought before leaving course 6, and takes on the values 0, 1, or 2. So


We use the total probability theorem, conditioning on the next day, to yield the following set of equations:


Solving this system of equations yields:


We still need to find v6−1(1), and we do this by again conditioning on the following day and solving the following set of equations:


Page 2 of 5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Notice in the second and third equations that when she transitions into state 6-1, there should be no additional transitions from 6-2 to 6-1 or from 6-3 to 6-1 after the second day in order for there to be a total of one such transition. Solving this system of equations yields:


Finally, we can solve for the expected number of cones:


- (e) We want to find the expected time to absorption conditioned on the event that the student eventually ends up in state 15, which we will call A. So


where ak is the absorption probability of eventually ending up in state 15 conditioned on being in state k, which we found in part (b). So we may modify our chain with these new conditional probabilities and calculate the expected time to absorption on the new chain. Note that state 9 now disappears. Also, note that Pj,j|A = Pj,j, but Pi,j|A = Pi,j for i = j, which means that we may not simply renormalize the transition probabilities in a uniform fashion after conditioning on this event. Let us denote the new expected time to absorption, conditioned on being in state i as ˜µi. Our system of equations now becomes


Solving this system of equations yields


(f) The new Markov chain is shown below.

Page 3 of 5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


<!-- Start of picture text -->
1<br>9<br>1/2<br>1/6<br>1/4<br>6-1<br>3/8  1/6<br>1/6  3/4<br>6-3  3/8  6-2<br>1/4<br><!-- End of picture text -->

This is another expected time to absorption question on the new chain. Let us define µk to be the expected number of days it takes the student to go from state k to state 9 in this new Markov chain:


Solving this system of equations yields:


- (g) States 6-1, 6-2 and 6-3 are now transient. States 9 and 15 form a recurrent class. By symmetry, 9 and 15 have the same steady state probability of 1/2.


<!-- Start of picture text -->
1/2 1/2 1/2<br>9 15<br>1/2<br>1/2<br>1/8 1/8<br>1/4 6-1 1/2<br>3/8 3/8<br>1/8 1/8<br>3/8<br>6-3 6-2<br>1/8<br><!-- End of picture text -->

Image by MIT OpenCourseWare. States 6-1, 6-2 and 6-3 are now transient. States 9 and 15 form a recurrent class. By symmetry, 9 and 15 have the same steady state probability of 1/2.

Page 4 of 5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

(h) The corresponding Markov chain is the same as the one in part (a) except p9,6−1 = <u>18</u> , p9,9 = <u>7 1 7</u> 8 , p15,6−1 = 8 , p15,15 = 8 instead of p9,9 = 1, p15,15 = 1. We can consider state 6-1 as an absorbing state. Let µk be the expected number of transi­ tions until absorption if we start at state k


Let R be the number of days until she is 6-1 again. We find E[R] by using the total expectation theorem, conditioned on what happens on the first transition.


Notice that this chain consists of a single recurrent aperiodic class. Another approach to solving this problem uses the steady state probabilities of this chain, which are π6−1 = <u>61 11 9 79 105</u> 265 , π6−2 = 265 , π6−3 = 265 , π9 = 265 , π15 = 265 . The expected frequency of visits to 6-1 is π6−1, so the expected number of days between visits to 6-1 is π61 `−` 1<sup>. 1Since she is currently</sup> 6-1, the expected number of days until she is 6-1 again is π61 `−` 1 = <u>26561</u> .

> 1See problem 7.34 on page 399 of the text for a more detailed explanation of this correspondence between mean recurrence times and steady-state probabilities.

Page 5 of 5

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
