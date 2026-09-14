---
title: 08 questions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/psets/08-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 08 questions

**Source:** `psets/08-questions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Problem Set 8 Due November 15, 2010

1. Oscar goes for a run each morning. When he leaves his house for his run, he is equally likely to go out either the front or back door; and similarly, when he returns, he is equally likely to go to either the front or back door. Oscar owns only five pairs of running shoes which he takes off immediately after the run at whichever door he happens to be. If there are no shoes at the door from which he leaves to go running, he runs barefooted. We are interested in determining the long-term proportion of time that he runs barefooted.

   - (a) Set the scenario up as a Markov chain, specifying the states and transition probabilities.

   - (b) Determine the long-run proportion of time Oscar runs barefooted.

2. Consider a Markov chain X1, X2, . . . modeling a symmetric simple random walk with barriers, as shown below:


<!-- Start of picture text -->
1/2 1/2<br>1/2 1/2 1/2 1/2 1/2 1/2<br>− m − 1 0 1 m<br>1/2 1/2 1/2 1/2 1/2 1/2<br><!-- End of picture text -->

   - (a) Explain why |X1|, |X2|, |X3|, . . . also satisfies the Markov property and draw the associated chain.

   - (b) Suppose that we also wish to keep track of the largest deviation from the origin, i.e., define the largest deviation at time t as Yt = max{|X1|, |X2|, . . . , |Xt|}. Draw a Markov chain that keeps track of the largest deviation and explain why it satisfies the Markov property.

3. As flu season is upon us, we wish to have a Markov chain that models the spread of a flu virus. Assume a population of n individuals. At the beginning of each day, each individual is either infected or susceptible (capable of contracting the flu). Suppose that each pair (i, j), i = j, independently comes into contact with one another during the daytime with probability p. Whenever an infected individual comes into contact with a susceptible individual, he/she infects him/her. In addition, assume that overnight, any individual who has been infected for at least 24 hours will recover with probability 0 < q < 1 and return to being susceptible, independently of everything else (i.e., assume that a newly infected individual will spend at least one restless night battling the flu).

   - (a) Suppose that there are m infected individuals at daybreak. What is the distribution of the number of new infections by day end?

   - (b) Draw a Markov chain with as few states as possible to model the spread of the flu for n = 2. In epidemiology, this is called an SIS (Susceptible-Infected-Susceptible) model.

   - (c) Identify all recurrent states.

Due to the nature of the flu virus, individuals almost always develop immunity after contracting the virus. Consequently, we improve our model and assume that individuals become infected at most one time. Thus, we consider individuals as either infected, susceptible, or recovered.

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

   - (d) Draw a Markov chain to model the spread of the flu for n = 2. In epidemiology, this is called an SIR (Susceptible-Infected-Recovered) model.

   - (e) Identify all recurrent states.

4. Consider the Markov chain below. For all parts of this problem, the process is in state 3 imme­ diately before the first transition. Be sure to comment on any unusual results.


<!-- Start of picture text -->
1/2  4/10  3/4  1/4  1/2<br>1  2/10  1/4  1/4<br>S 1  S 2  S 3  S 4  S 5  S 6<br>1/2  1/10  1/2 1/2<br>3/10<br>S 7<br>1<br><!-- End of picture text -->

   - (a) Find the variance for J, the number of transitions up to and including the transition on which the process leaves state 3 for the last time.

   - (b) Find the expectation for K, the number of transitions up to and including the transition on which the process enters state 4 for the first time.

   - (c) Find πi for i = 1, 2, . . . , 7, the probability that the process is in state i after 10<sup>10</sup> transitions.

   - (d) Given that the process never enters state 4, find the πi’s as defined in part (c).

- G1<sup>†</sup> . Consider a Markov chain {Xk} on the state space {1, . . . , n}, and suppose that whenever the state is i, a reward g(i) is obtained. Let Rk be the total reward obtained over the time interval {0, 1, . . . , k}, that is, Rk = g(X0) + g(X1) + · · · + g(Xk). For every state i, let


and


respectively be the conditional mean and conditional variance of Rk, conditioned on the initial state being i.

- (a) Find a recursion that, given the values of mk(1), . . . , mk(n), allows the computation of mk+1(1), . . . , mk+1(n).

- (b) Find a recursion that, given the values of mk(1), . . . , mk(n) and vk(1), . . . , vk(n), allows the computation of vk+1(1), . . . , vk+1(n). Hint: Use the law of total variance.

†Required for 6.431; optional for 6.041

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
