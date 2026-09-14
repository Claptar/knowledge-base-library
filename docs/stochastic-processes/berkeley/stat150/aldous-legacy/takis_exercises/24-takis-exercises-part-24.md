---
title: Takis exercises Part 24 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 24 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A Markov chain takes values 1, 2, 3, 4, 5. From i it can move to any j > i with equal probability. State 5 is absorbing. Starting from 1, how many steps in the average will it take till it reaches 5?

Solution. 2.08

86.

There are N individuals, some infected by a disease (say the disease of curiosity) and

65

some not. At each stage, exactly one uninfected individual is placed in contact with the infected ones. An infected individual infects with probability p. So an uninfected individual becomes infected if he or she gets infected by at least one of the infected individuals. Assume that, to start with, there is only one infected person. Build a Markov chain with states 1, 2, . . . , N and argue that p(k, k + 1) = 1 − (1 − p)<sup>k</sup> . Show that, on the average, it will take N + q(1− q<sup>N</sup> )/(1− q) for everyone to become infected.

Solution. When there are k infected individuals and one uninfected is brought in contact with them, the chance that the latter is not infected is (1 − p)<sup>k</sup> . So


Of course, p(N, N ) = 1. The average number of steps to go from k to k + 1 is 1/p(k, k + 1). Hence, starting with 1 infected individual it takes


for everyone to become infected.

87.

Assume, in addition, that exactly one infected individual is selected for treatment and he or she becomes well with probability α > 0, and this occurs independently of everything else. (i) What is the state space and the transition probabilities? (ii) How many absorbing states are there? (iii) What kind of question would you like to ask here and how would you answer it?

Solution. (i) Since p(1, 0) is equal to α which is positive, we now need to include 0 among the states. So the state space is


The transition probabilities now become


where q = 1 − p. (ii) There is only one absorbing state: the state 0. (iii) The question here is: How long will it take for the chain to be absorbed at 0? Letting g(k) be the mean time to absorption starting from k, we have


There is a unique solution.

88.

Prove that for an irreducible Markov chain with N states it is possible to go from any state to any other state in at most N − 1 steps.

Solution. For any two distinct states i, j there is a path that takes you from i to j. Cut out any loops from this path and you still have a path that takes you from i to j. But this path has distinct states and distinct arrows. There are at most N − 1 such arrows.

66

---

[← Takis exercises Part 23 —](23-takis-exercises-part-23.md) · [Up: contents](index.md) · [Takis exercises Part 25 — →](25-takis-exercises-part-25.md)
