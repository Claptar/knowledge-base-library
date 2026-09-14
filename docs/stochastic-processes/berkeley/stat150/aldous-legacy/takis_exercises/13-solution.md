---
title: Solution.
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution.

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
p<br>i− 1<br>p 2 p 3 p i<br>p0 0 1 1 1 2 1 3 i− 1 1 i<br><!-- End of picture text -->

- (i) Yes it is. It is possible to move from any state to any other state.

(ii) It is 1.

49

(iii) Same.

(iv) We write balance equations:


Solving this we find


The normalising condition gives


This can be satisfied if and only if


This is the condition for positive recurrence.

Note that, since p0 + · · · + pi−1 = P0(X1 ≤ i − 1), the condition can be written as


But


so the condition is equivalent to


(v)


53.

Consider a simple symmetric random walk Sn = ξ1 +· · ·+ξn, started from S0 = 0. Find the following probabilities: (i) P (S4 = k), for all possible values of k.

(ii) P (Sn ≥ 0 ∀n = 1, 2, 3, 4). (iii) P (Sn̸ = 0 ∀n = 1, 2, 3, 4). (iv) P (Sn ≤ 2 ∀n = 1, 2, 3, 4). (v) P (|Sn| ≤ 2 ∀n = 1, 2, 3, 4).

Solution. (i) We have


50

and so

P (S4 = −4) = P (S4 = 4) = 1/16, P (S4 = −2) = P (S4 = 2) = 4/16, P (S4 = 0) = 6/16.

(ii) Since the random walk is symmetric, all paths of the same length are equally likely. There are 6 paths compris4 ing the event {(Sn ≥ 0 ∀n = 1, 2, 3, 4} and so P ((Sn ≥ 3 0 ∀n = 1, 2, 3, 4) = 6/16. 2 (iii) There are just 2 paths comprising the event {Sn > 1 0 ∀n = 1, 2, 3, 4}. Hence P (Sn̸ = 0 ∀n = 1, 2, 3, 4) = 4/16. 0 (iv) There are 2 paths violating the condition {Sn ≤ 2 ∀n = −1 1, 2, 3, 4}. Hence P (Sn ≤ 2 ∀n = 1, 2, 3, 4) = (16 − 2)/16 = −2 14/16. −3 −4 (v) There are 4 paths violating the condition {|Sn| ≤ 2 ∀n = 1, 2, 3, 4}. Hence P (|Sn| ≤ 2 ∀n = 1, 2, 3, 4) = (16−4)/16 = 0 1 2 3 4 12/16.

54.

Consider a simple random walk Sn = ξ1 + · · · + ξn, started from S0 = 0, with P (ξ1 = 1) = p, P (ξ1 = −1) = q, p + q = 1. (i) Show that


(ii) Are you surprised by the fact that the answer does not depend on p? Solution. (i) If m > n then Sm = Sn + (Sm − Sn), so


But Sm − Sn = ξn+1 + · · · + ξm. Since ξn+1, . . . , ξm are independent of Sn, we have


Thus,

E(Sm − Sn | Sn) = Sn + (p − q)(m − n), if m > n.

If m ≤ n, then


Now notice that for all k = 1, . . . , n,


because the random variables ξ1, . . . , ξn are i.i.d. and Sn is a symmetric function of them (interchanging two does not change the sum). Hence for all m = 1, . . . , n,


This is true even for m = n. But, in this case, E(Sm | Sn) = E(Sn | Sn) = Sn, so that E(ξ1 | Sn) = Sn/n. Thus,


(ii) At first sight, yes, you should be surprised. But look (think) again...

55.

Consider a simple random walk Sn again, which does not necessarily start from 0, and define the processes the processes:


(i) Show that each of them is Markov and identify their state spaces.

(ii) Compute their transition probabilities.

Solution. (i) The first two are Markov because they are a subsequence of a Markov chain. The third is Markov because x �→ e<sup>x</sup> is a bijection from R into (0, ∞). The state space of the first two is Z. The state space of the third is the set S = {e<sup>k</sup> : k ∈ Z} = {. . . , e<sup>−2</sup> , e<sup>−1</sup> , 1, e, e<sup>2</sup> , e<sup>3</sup> , . . .}.

(ii) For the first one we have

P (Xn+1 = j|Xn = i) = P (S2n = j|S2n = i) = P (i+ξ2n+1+ξ2n = j) = P (ξ1+ξ2 = j−i).

Hence, given i, the only possible values of j are i − 2, i, i + 2. For all other values of j, the transition probability is zero. We have


The second process has the same transition probabilities.

For the third process we have


56.

Consider a simple random walk Sn again, and suppose it starts from 0. As usual, P (ξ1 = 1) = p, P (ξ1 = −1) = q = 1 − p. Compute Ee<sup>αSn</sup> for α ∈ R.

Solution. We have Sn = ξ1 + · · · + ξn. By independence


52

57.

- (i) Explain why P (limn→∞ Sn = ∞) = 1 is p > q and, similarly, P (limn→∞ Sn = −∞) = 1 if p < q.

(ii) What can you say about the asymptotic behaviour of Sn as n →∞ when p = q?

Solution. (i) The Strong Law of Large Numbers (SLLN) says that


because Eξ1 = p − q. If p > q, then SLLN implies that


But


Since the event on the left has probability 1, so does the event on the right, i.e.


If, on the other hand, p < q, then p − q < 0, and so SLLN implies that


But


Since the event on the left has probability 1, so does the event on the right, i.e.


(ii) If p = q, then p − q = 0, and the fact that Sn/n converges to 0 cannot be used to say something about the sequence Sn other than that the sequence Sn has no limit. So, we may conclude that


Stronger conclusions are possible, as we saw in the lectures.

58.

For a simple symmetric random walk let fn be the probability of first return to 0 at time n. Compute fn for n = 1, . . . , 6 first by applying the general formula and then by path counting (i.e. by considering the possible paths that contribute to the event). Solution. Obviously, fn = 0 if n is odd. Recall the formula


53

With k = 1, 2, 3, we have


To do path counting, we consider, e.g. the last case. The possible paths contributing to the event {T0<sup>′= 8}aretheonesinthefigurebelowaswellastheirreflections:</sup>


Each path consists of 8 segments, so it has probability 2<sup>−8</sup> . There are 5 paths, so f8 = 10/2<sup>8</sup> = 5/128.

---

[← Takis exercises Part 12 —](12-takis-exercises-part-12.md) · [Up: contents](index.md) · [Takis exercises Part 14 — →](14-takis-exercises-part-14.md)
