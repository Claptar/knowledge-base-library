---
title: Solution
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(a) The transition matrix P for this Markov chain is as follows:


13

(b) The chain is irreducible, because it is possible to go from any state to any other state. However, it is not aperiodic, because for any n even p<sup>(</sup> 6<sup>n</sup> ,1<sup>)willbezeroandfor</sup> any n odd p<sup>(</sup> 6<sup>n</sup> ,5<sup>)willalsobezero(why?).ThismeansthatthereisnopowerofPthat</sup> would have all its entries strictly positive.

(c) The stationary distribution is


You should carry out the calculations and check that this is correct.

(d) We find from π that the mean recurrence time (i.e. the expected time to return) for the room 1 is 1/π(1)=12.

(e) Let

ψ(i) = E(number of steps to reach state 5 | X0 = i).

We have

ψ(5) = 0 ψ(6) = 1 + (1/2)ψ(5) + (1/2)ψ(4) ψ(4) = 1 + (1/2)ψ(6) + (1/2)ψ(3) ψ(3) = 1 + (1/4)ψ(1) + (1/4)ψ(2) + (1/4)ψ(4) + (1/4)ψ(5) ψ(1) = 1 + ψ(3) ψ(2) = 1 + ψ(3).

We solve and find ψ(1) = 7.

16.

Show that if P is the transition matrix of an irreducible chain with finitely many states, then Q := (1/2)(I + P) is the transition matrix of an irreducible and aperiodic chain. (Note that I stands for the identity matrix, i.e. the matrix which has 1 everywhere on its diagonal and 0 everywhere else.)

Show that P and (1/2)(I + P) have the same stationary distributions. Discuss, physically, how the two chains are related.

Solution. Let pij be the entries of P. Then the entries qij of Q are


The graph of the new chain has more arrows than the original one. Hence it is also irreducible. But the new chain also has self-loops for each i because qii > 0 for all i. Hence it is aperiodic.

Let π be a stationary distribution for P. Then


We must show that


But


The physical meaning of the new chain is that it represents a slowing down of the original one. Indeed, all outgoing probabilities have been halved, while the probability of staying at the same state has been increased. The chain performs the same transitions as the original one but stays longer at each state.

17.

Two players, A and B, play the game of matching pennies: at each time n, each player has a penny and must secretly turn the penny to heads or tails. The players then reveal their choices simultaneously. If the pennies match (both heads or both tails), Player A wins the penny. If the pennies do not match (one heads and one tails), Player B wins the penny. Suppose the players have between them a total of 5 pennies. If at any time one player has all of the pennies, to keep the game going, he gives one back to the other player and the game will continue. (a) Show that this game can be formulated as a Markov chain. (b) Is the chain regular (irreducible + aperiodic?) (c) If Player A starts with 3 pennies and Player B with 2, what is the probability that A will lose his pennies first?

Solution (a) The problem is easy: The probability that two pennies match is 1/2. The probability they do not match is 1/2. Let x be the number of pennies that A has. Then with probability 1/2 he will next have x + 1 pennies or with probability 1/2 he will next have x − 1 pennies. The exception is when x = 0, in which case, he gets, for free, a penny from B and he next has 1 penny. Also, if x = 5 he gives a penny to B and he next has 4 pennies. Thus:


(b) The chain is clearly irreducible. But the period is 2. Hence it is not regular. (c) To do this, modify the chain and make it stop once one of the players loses his pennies. After all, we are NOT interested in the behaviour of the chain after this time. The modification is an absorbing chain:


We then want to compute the absorbing probability ϕ01(3) where

ϕ01(i) = Pi(hit 0 before 1).

15

Write ϕ(i) = ϕ01(i), for brevity, and apply first-step analysis:


Six equations with six unknowns. Solve and find: ϕ(3) = 2/5. Alternatively, observe, from Thales’ theorem,<sup>6</sup> that ϕ must be a straight line:


From ϕ(0) = 1, ϕ(5) = 0, we find a = −1/5, b = 1, i.e.


which agrees with the above.

18.

A process moves on the integers 1, 2, 3, 4, and 5. It starts at 1 and, on each successive step, moves to an integer greater than its present position, moving with equal probability to each of the remaining larger integers. State five is an absorbing state. Find the expected number of steps to reach state five.

Solution. A Markov chain is defined and its transition probability matrix is as follows:


We apply first step analysis for the function


Thales’ theorem says (proved around the 6year 600 BCE) says that if the lines L, L<sup>′</sup> are parallel then<sup>DE</sup> BC<sup>=AE</sup> AC<sup>=AD</sup> AB<sup>.</sup>


16

where S5 = inf{n ≥ 0 : Xn = 5}. One of the equations is ψ(5) = 0 (obviously). Another is ψ(1) = 1 +<sup>1</sup> 4<sup>ψ(2) +1</sup> 4<sup>ψ(3) +1</sup> 4<sup>ψ(3) +1</sup> 4<sup>ψ(5).</sup>

It’s up to you to write the remaining equations and solve to find

---

[← Takis exercises Part 06 —](06-takis-exercises-part-06.md) · [Up: contents](index.md) · [Takis exercises Part 08 — →](08-takis-exercises-part-08.md)
