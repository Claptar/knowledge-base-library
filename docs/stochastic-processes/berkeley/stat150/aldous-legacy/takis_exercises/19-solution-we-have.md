---
title: Solution. We have
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution. We have

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

First consider the case a > 0. We have that, for all values of p,


So


If p ≥ q then |p − q| = p − q and simple algebra gives P (Ta < ∞) = 1. If p < q then |p − q| = q − p and simple algebra gives P (Ta < ∞) = (q/p)<sup>a</sup> . Next consider the case a < 0. By interchanging the roles of p and q we have


If p ≥ q then |q − p| = p − q and simple algebra gives P (Ta < ∞) = (p/q)<sup>a</sup> . If p > q then |q − p| = q − p and simple algebra gives P (Ta < ∞) = 1.

74.

Show that for a symmetric simple random walk any state is visited infinitely many times with probability 1.

Solution.

75.

Derive the expectation of the running maximum Mn for a SSRW starting from 0:


Conclude that EMn/E|Sn| → 1, as n →∞.

Solution. This follows from the formula


We have EMn =<sup>�∞</sup> x=1<sup>P(Mn≥x),E|Sn| = �∞</sup> x=1<sup>P(|Sn| ≥x),so:</sup>


The last sum equals 1 − P (Sn = 0) = 1 − �n/n2�2<sup>−n</sup> .

62

76.

Using the ballot theorem, show that, for a SSRW starting from 0,


where Sn<sup>+= max(Sn, 0).</sup>

Solution. The ballot theorem says


Hence


77.

For a simple random walk with p < q show that EM∞ = p q−p<sup>.</sup>

Solution. We have


78.

Consider a SSRW, starting from some positive integer x, and let T0 be the first n such that Sn = 0. Let M = max{Sn : 0 ≤ n ≤ T0}. Show that M has the same distribution as the integer part of (i.e. the largest integer not exceeding) x/U , where U is a uniform random variable between 0 and 1.

Solution. Let Ta be the first time that the random walk reaches level a ≥ x. Then


On the other hand, if [y] denotes the largest integer not exceeding the real number y, we have, for all a ≥ x,


Hence P ([x/U ] ≥ a) = P (M ≥ a), for all x ≥ a (while both probabilities are 1 for x < a). Hence M has the same distribution as [x/U ].

79.

Show that (Xn, n ∈ Z+) is Markov if and only if for all intervals I = [M, N ] ⊆ Z+ (Xn, n ∈ I) (the process inside) is independent of (Xn, n̸ ∈ I) (the process outside), conditional on the pair (XM , XN ) (the process on the boundary).

63

80.

A deck of cards has 3 Red and 3 Blue cards. At each stage, a card is selected at random. If it is Red, it is removed from the deck. If it is Blue then the card is not removed and we move to the next stage. Find the average number of steps till the process ends.

Solution. The problem can be solved by writing first step equations for the Markov chain representing the number of red cards remaining: The transition probabilities are:


Let ψ(i) be the average number of steps till the process ends if the initial state is i. Then


Alternatively, observe that, to go from state i to i − 1, we basically toss a coin with probability of success equal to p(i, i − 1). Hence the expected number of tosses till success is 1/p(i, i − 1). Adding these up we have the answer:

---

[← Solution.](18-solution.md) · [Up: contents](index.md) · [Takis exercises Part 20 — →](20-takis-exercises-part-20.md)
