---
title: Takis exercises Part 06 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 06 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Smith is in jail and has 3 dollars; he can get out on bail if he has 8 dollars. A guard agrees to make a series of bets with him. If Smith bets A dollars, he wins A dollars with probability 0.4 and loses A dollars with probability 0.6. Find the probability that he wins 8 dollars before losing all of his money if (a) he bets 1 dollar each time (timid strategy). (b) he bets, each time, as much as possible but not more than necessary to bring his fortune up to 8 dollars (bold strategy). (c) Which strategy gives Smith the better chance of getting out of jail?

Solution. (a) The Markov chain (Xn, n = 0, 1, . . .) representing the evolution of Smith’s money has diagram


Let ϕ(i) be the probability that the chain reaches state 8 before reaching state 0, starting from state i. In other words, if Sj is the first n ≥ 0 such that Xn = j,


Using first-step analysis (viz. the Markov property at time n = 1), we have


We solve this system of linear equations and find


9

E.g., the probability that the chain reaches state 8 before reaching state 0, starting from state 3 is the third component of this vector and is equal to 0.0964. Note that ϕ(i) is increasing in i, which was expected.

(b) Now the chain is


and the equations are:


We solve and find


(c) By comparing the third components of the vector ϕ we find that the bold strategy gives Smith a better chance to get out jail.

11.

A Markov chain with state space {1, 2, 3} has transition probability matrix


Show that state 3 is absorbing and, starting from state 1, find the expected time until absorption occurs.

Solution. Let ψ(i) be the expected time to reach state 3 starting from state i, where i ∈{1, 2, 3}. We have


We solve and find


12.

A fair coin is tossed repeatedly and independently. Find the expected number of tosses till the pattern HTH appears.

10

Solution. Call HTH our target. Consider a chain that starts from a state called nothing ∅ and is eventually absorbed at HTH. If we first toss H then we move to state H because this is the first letter of our target. If we toss a T then we move back to ∅ having expended 1 unit of time. Being in state H we either move to a new state HT if we bring T and we are 1 step closer to the target or, if we bring H, we move back to H: we have expended 1 unit of time, but the new H can be the beginning of a target. When in state HT we either move to HTH and we are done or, if T occurs then we move to ∅. The transition diagram is


<!-- Start of picture text -->
1/2 1<br>H HT HTH<br>1/2 1/2 1/2<br>1/2 1/2<br><!-- End of picture text -->

Rename the states ∅, H, HT, HTH as 0, 1, 2, 3, respectively. Let ψ(i) be the expected number of steps to reach HTH starting from i. We have


We solve and find ψ(0) = 10.

13.

Consider a Markov chain with states S = {0, . . . , N } and transition probabilities pi,i+1 = p, pi,i−1 = q, for 1 ≤ i ≤ N − 1, where p + q = 1, 0 < p < 1; assume p0,1 = 1, pN,N −1 = 1.

1. Draw the graph (= transition diagram).

2. Is the Markov chain irreducible?

3. Is it aperiodic?

4. What is the period of the chain?

5. Find the stationary distribution.

Solution. 1. The transition diagram is:


<!-- Start of picture text -->
p p p p<br>q 0 1 2 i−1 i N−1 N<br>p<br>q q q q<br><!-- End of picture text -->

2. Yes, it is possible to go from any state to any other state.

3. Yes, because p0,0 > 0.

4. One.

5. We write balance equations by equating fluxes:


11

as long as 1 ≤ i ≤ N . Hence


Since

we find

which gives


as long as p̸ = q. Hence, if p̸ = q,


If p = q = 1/2, then


and so


Thus, in this case, π(i) is the uniform distribution on the set of states.

14.

A. Assume that an experiment has m equally probable outcomes. Show that the expected number of independent trials before the first occurrence of k consecutive occurrences of one of these outcomes is


Hint: Form an absorbing Markov chain with states 1, 2, . . . , k with state i representing the length of the current run. The expected time until a run of k is 1 more than the expected time until absorption for the chain started in state 1.

B. It has been found that, in the decimal expansion of π = 3.14159 . . ., starting with the 24,658,601st digit, there is a run of nine 7’s. What would your result say about the expected number of digits necessary to find such a run if the digits are produced randomly?

Solution. A. Let the outcomes be a, b, c, . . . (m of them in total). Suppose that a is the desirable outcome. We set up a chain as follows. Its states are


12

Or, more simply, 0, 1, 2, . . . , m. State k means that you are currently at the end of a run of k a’s. If you see an extra a (with probability 1/m) you go to state k + 1. Otherwise, you go to ∅. Let ψ(k) be the expected number of steps till state m is reached, starting from state k:


We want to find ψ(0). We have


Solving these, we find


B. So to get 10 consecutive sixes by rolling a die, you need more than 12 million rolls on the average (12, 093, 235 rolls to be exact).

C. They are not random. If they were, we expect to have to pick (10<sup>9</sup> − 1)/9 digits before we see nine consecutive sevens. That’s about 100 million digits. The actual position (24 million digits) is one fourth of the expected one.

15.

A rat runs through the maze shown below. At each step it leaves the room it is in by choosing at random one of the doors out of the room.


<!-- Start of picture text -->
1<br>2 3 4<br>5 6<br><!-- End of picture text -->

(a) Give the transition matrix P for this Markov chain. (b) Show that it is irreducible but not aperiodic. (c) Find the stationary distribution (d) Now suppose that a piece of mature cheddar is placed on a deadly trap in Room 5. The mouse starts in Room 1. Find the expected number of steps before reaching Room 5 for the first time, starting in Room 1. (e) Find the expected time to return to room 1.

---

[← Takis exercises Part 05 —](05-takis-exercises-part-05.md) · [Up: contents](index.md) · [Solution →](07-solution.md)
