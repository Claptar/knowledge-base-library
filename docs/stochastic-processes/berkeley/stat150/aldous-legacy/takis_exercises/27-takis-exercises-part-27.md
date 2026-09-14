---
title: Takis exercises Part 27 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 27 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider the random walk on the graph


(i) Find its stationary distribution. (ii) Find the average number of steps to return to state 2, starting from 2. (iii) Repeat for 1. (iv) Find the average number of steps for it to go from i to N . (v) Find the average number of steps to go from i to either 1 or N . (vi) Find the average number of steps it takes to visit all states at least once.

Solution. Hint for (vi): The time to visit all states at least once is the time to hit the boundary plus the time to hit the other end of the boundary.

92.

When a bus arrives at the HW campus, the next bus arrives in 1, 2, . . . , 20 minutes with equal probability. You arrive at the bus stop without checking the schedule, at some fixed time. How long, on the average, should you wait till the next bus arrives? What is the standard deviation of this time?

Solution. This is based on one of the examples we discussed: Let Xn be the time elapsed from time n till the arrival of the next bus. Then Xn is a Markov chain with transition probabilities


67

where pk = (1/20)1(1 ≤ k ≤ 20). We find that the stationary distribution is


where c a constant determined by normalisation:


Hence


and so the average waiting time is


The standard deviation is


Note: To do the sums without too much work, use the formulae


93.

Build a Markov chain as follows: When in state k (k = 1, 2, 3, 4, 5, 6), roll a die k times, take the largest value and move to that state. (i) Compute the transition probabilities and write down the transition probability matrix. (ii) Is the chain aperiodic? (iii) Does it have a unique stationary distribution? (iv) Can you find which state will be visited more frequently on the average?

Solution. (i) Let Mk be the maximum of k independent rolls. Then


The transition probability from state k to state ℓ is


68

The transition probability matrix is


(ii) The chain is obviously aperiodic because it has at least one self-loop.

(iii) Yes it does because it is finite and irreducible.

(iv) Intuitively, this should be state 6.

94.

Simple queueing system: Someone arrives at a bank at time n with probability α. He or she waits in a queue (if any) which is served by one bank clerk in a FCFS fashion. When at the head of the queue, the person requires a service which is distributed like a random variable S with values in N: P (S = k) = pk, k = 1, 2, . . .. Different people require services which are independent random variables. Consider the quantity Wn which is the total waiting time at time n: if I take a look at the queue at time n then Wn represents the time I have to wait in line till I finish my service. (i) Show that Wn obeys the recursion


where the Sn are i.i.d. random variables distributed like S, independent of the ξn. The latter are also i.i.d. with P (ξn = 1) = α, P (ξn = 0) = 1 − α. Thus ξn = 1 indicates that there is an arrival at time n. (ii) Show that Wn is a Markov chain and compute its transition probabilities p(k, ℓ), k, ℓ = 0, 1, 2, . . ., in terms of the parameters α and pk. (iii) Suppose that p1 = 1 − β, p2 = β. Find conditions on α and β so that the stationary distribution exists. (iv) Give a physical interpretation of this condition. (v) Find the stationary distribution. (vi) Find the average waiting time in steady-state. (vii) If α = 4/5 (4 customers arrive every 5 units of time on the average–heavy traffic), what is the maximum value of β so that a stationary distribution exists? What is the average waiting time when β = 0.24?

Solution. (i) If, at time n the waiting time Wn is nonzero and nobody arrives then Wn+1 = Wn − 1, because, in 1 unit of time the waiting time decreases by 1 unit. If, at time n, somebody arrives and has service time Sn then, immediately the waiting time becomes Wn + Sn and so, in 1 unit of time this decreases by 1 so that Wn+1 = Wn + Sn − 1. Putting things together we arrive at the announced equation. Notice that the superscript + means maximum with 0, because, if Wn = 0 and nobody arrives, then Wn+1 = Wn = 0.

69

(ii) That the Wn form a Markov chain with values in Z+ follows from the previous exercise. To find the transition probabilities we argue as follows: Let p(k, ℓ) = P (Wn+1 = ℓ | Wn = k). First, observe that, for a given k, the ℓ cannot be less than k − 1. In fact, p(k, k − 1) = 1 − α (the probability that nobody arrives). Next, for ℓ to be equal to k we need that somebody arrives and brings work equal to 1 unit: p(k, k) = αp1. Finally, for general ℓ> k we need to have an arrival which brings work equal to ℓ − k + 1: p(k, ℓ) = αpℓ−k+1. (iii) Here we have


To compute the stationary distribution we write balance equations:

π(k)(1 − α) = π(k − 1)αβ, k ≥ 0.

Iterating this we get


We need to be able to normalise:


We can do this if and only if the geometric series converges. This happens if and only if


(iv) The condition can also be written as


The left side is the average service time (1 × (1 − β) + 2 × β). The right side is the average time between two successive arrivals. So the condition reads: Average service time < average time between two successive arrivals.

(v) From the normalisation condition, π(0) = (1 − α(1 + β))/(1 − α). This follows because

Hence


This is of the form π(0) = (1 − ρ)ρ<sup>k</sup> , where ρ = αβ/(1 − α), hence a geometric distribution.

(vi) The average waiting time in steady-state is


(vii) If α = 4/5 then β < (5/4) − 1 = 1/4. So the service time must be such that P (S = 2) = β < 1/4, and P (S = 1) = 1 − β > 3/4. When β = 0.24 we are OK since 0.2 < 0.25. In this case, the average waiting time is equal to 24, which is quite large compared to the maximum value of S.

70

95.

Let Sn be a simple symmetric random walk with S0 = 0. Show that |Sn| is Markov.

Solution. If we know the value of Sn, we know two things: its absolute value |Sn| and its sign. But to determine the value of |Sn+1|, knowledge of the sign is irrelevant, since, by symmetry |Sn+1| = |Sn| ± 1 with probability 1/2 if Sn̸ = 0, while |Sn+1| = 1 is Sn = 0. Hence P (|Sn+1| = j | Sn = i) depends only on |i|: if |i| > 0 it is 1/2 for j = i ± 1, and if |i| = 0 it is 1 for j = 1.

---

[← Takis exercises Part 26 —](26-takis-exercises-part-26.md) · [Up: contents](index.md) · [Takis exercises Part 28 — →](28-takis-exercises-part-28.md)
