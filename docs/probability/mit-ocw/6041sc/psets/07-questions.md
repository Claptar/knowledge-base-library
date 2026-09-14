---
title: 07 questions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/psets/07-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 07 questions

**Source:** `psets/07-questions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Problem Set 7 Due November 8, 2010

1. Consider a sequence of mutually independent, identically distributed, probabilistic trials. Any particular trial results in either a success (with probability p) or a failure.

   - (a) Obtain a simple expression for the probability that the ith success occurs before the jth failure. You may leave your answer in the form of a summation.

   - (b) Determine the expected value and variance of the number of successes which occur before the jth failure.

   - (c) Let L17 be described by a Pascal PMF of order 17. Find the numerical values of a and b in the following equation. Explain your work.


2. Fred is giving out samples of dog food. He makes calls door to door, but he leaves a sample (one can) only on those calls for which the door is answered and a dog is in residence. On any call the probability of the door being answered is 3/4, and the probability that any household has a dog is 2/3. Assume that the events “Door answered” and “A dog lives here” are independent and also that the outcomes of all calls are independent.

   - (a) Determine the probability that Fred gives away his first sample on his third call.

   - (b) Given that he has given away exactly four samples on his first eight calls, determine the conditional probability that Fred will give away his fifth sample on his eleventh call.

   - (c) Determine the probability that he gives away his second sample on his fifth call.

   - (d) Given that he did not give away his second sample on his second call, determine the condi­ tional probability that he will leave his second sample on his fifth call.

   - (e) We will say that Fred “needs a new supply” immediately after the call on which he gives away his last can. If he starts out with two cans, determine the probability that he completes at least five calls before he needs a new supply.

   - (f) If he starts out with exactly m cans, determine the expected value and variance of Dm, the number of homes with dogs which he passes up (because of no answer) before he needs a new supply.

3. Let T1 and T2 be exponential random variables with parameter λ, and let S be an exponential random variable with parameter µ. We assume that all three of these random variables are inde­ pendent. Derive an expression for the expected value of min{T1 + T2, S}. Hint: See Problem 6.19 in the text.

4. A single dot is placed on a very long length of yarn at the textile mill. The yarn is then cut into lengths requested by different customers. The lengths are independent of each other, but all distributed according to the PDF fL(ℓ). Let R be be the length of yarn purchased by that customer whose purchase included the dot. Determine the expected value of R in the following cases:

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)


5. Consider a Poisson process of rate λ. Let random variable N be the number of arrivals in (0, t] and M be the number of arrivals in (0, t + s], where t, s ≥ 0.

   - (a) Find the conditional PMF of M given N , pM |N (m|n), for m ≥ n.

   - (b) Find the joint PMF of N and M , pN,M (n, m).

   - (c) Find the conditional PMF of N given M , pN |M (n|m), for n ≤ m, using your answer to part (b).

   - (d) Rederive your answer to part (c) without using part (b). As a hint, consider what kind of distribution the k<sup>th</sup> arrival time has if we are given the event {M = m}, where k ≤ m.

   - (e) Find E[NM ].

6. The interarrival times for cars passing a checkpoint are independent random variables with PDF


where the interarrival times are measured in minutes. The successive experimental values of the durations of these interarrival times are recorded on small computer cards. The recording operation occupies a negligible time period following each arrival. Each card has space for three entries. As soon as a card is filled, it is replaced by the next card.

   - (a) Determine the mean and the third moment of the interarrival times.

   - (b) Given that no car has arrived in the last four minutes, determine the PMF for random variable K, the number of cars to arrive in the next six minutes.

   - (c) Determine the PDF and the expected value for the total time required to use up the first dozen computer cards.

   - (d) Consider the following two experiments:

      - i. Pick a card at random from a group of completed cards and note the total time, Y , the card was in service. Find E[Y ] and var(Y ).

      - ii. Come to the corner at a random time. When the card in use at the time of your arrival is completed, note the total time it was in service (the time from the start of its service to its completion). Call this time W . Determine E[W ] and var(W ).

- G1<sup>†</sup> . Consider a Poisson process with rate λ, and let N (Gi) denote the number of arrivals of the process during an interval Gi = (ti, ti + ci]. Suppose we have n such intervals, i = 1, 2, · · · , n, mutually disjoint. Denote the union of these intervals by G, and their total length by c = c1 + c2 + · · · + cn. Given ki ≥ 0 and with k = k1 + k2 + · · · + kn, determine


†Required for 6.431; optional for 6.041

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
