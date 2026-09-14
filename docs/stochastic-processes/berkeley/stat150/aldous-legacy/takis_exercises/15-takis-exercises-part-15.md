---
title: Takis exercises Part 15 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 15 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A fair coin is tossed repeatedly and independently. Find the expected number of tosses required until the patter HTHH appears.

Solution. It’s easy to see that the Markov chain described by the following transition diagram captures exactly what we are looking for.


Rename the states ∅, H, HT, HTH, HTHH as 0, 1, 2, 3, 4, respectively, and let ψi be the average number of steps required for the state 4 to be reached if the starting state

54

is i. Writing first-step (backwards) equations we have


Also, obviously, ψ4 = 0. Solving, we find


So the answer is: “it takes, on the average, 18 coin tosses to see the pattern HTHH for the first time”.

61.

Show that the stationary distribution for the Ehrenfest chain is Binomial.

Solution. The Ehrenfest chain has state space


and transition probabilities


From the transition diagram we immediately deduce that detailed balance equations must hold, so, if π denotes the stationary distribution,


or


iterating of which gives


which is immediately recognisable as Binomial distribution.

62.

A Markov chain has transition probability matrix


Draw the transition diagram. Are there any absorbing states? Which are the communicating classes? Can you find a stationary distribution?

55

What are the periods of the states? Are there any inessential states? Which states are recurrent? Which states are transient? Which states are positive recurrent?

Solution.


- There are no absorbing states because there is no state i for which pi,i = 1.

- All states communicate with one another. Therefore there is only one communicating class, {1, 2, 3, 4}, the whole state space. (We refer to this by saying that the chain is irreducible.)

- Yes, of course we can. We can ALWAYS find a stationary distribution if the state

- space is FINITE. It can be found by solving the system of equations (known as balance equations)


which, in explicit form, yield


Solving these, along with the normalisation condition π(1) + π(2) + π(3) + π(4) = 1, we find


• Since the chain is irreducible the periods of all the states are the same. So let take a particular state, say state 4 and consider the set


We see that the first few elements of this set are


We immediately deduce that the greatest common divisor of the set is 1. Therefore the period of state 4 is 1. And so each state has period 1. (We refer to this by saying that the chain is aperiodic.)

- Since all states communicate with one another there are no inessential states.

- Since π(i) > 0 for all i, all states are recurrent.

- Since all states are recurrent there are no transient states.

- Since π(i) > 0 for all i, all states are positive recurrent.

56

63.

In tennis the winner of a game is the first player to win four points, unless the score is 4–3, in which case the game must continue until one player wins by two points. Suppose that the game has reached the point where one player is trying to get two points ahead to win and that the server will independently win the point with probability 0.6. What is the probability the server will win the game if the score is tied 3-3? if she is ahead by one point? Behind by one point?

Solution. Say that a score x-y means that the server has x points and the other player y. If the current score is 3-3 the next score is either 4-3 or 3-4. In either case, the game must continue until one of the players is ahead by 2 points. So let us say that i represents the difference x − y. We model the situation by a Markov chain as follows:


Let ϕi be the probability that the server wins, i.e. that state 2 is reached before state −2. First-step equations yield:


In other words,


Of course,


Solving, we find


64.

Consider a simple random walk with p = 0.7, starting from zero. Find the probability that state 2 is reached before state −3. Compute the mean number of steps until the random walk reaches state 2 or state 3 for the first time.

Solution. Let ϕi be the probability that state 2 is reached before state −3, starting from state i. By writing first-step equations we have:


In other words,


57

We also have, of course,


By solving these equations we find:


Therefore


Next, let ti be the mean number of steps until the random walk reaches state 2 or state 3 for the first time, starting from state i. By writing first-step equations we have:


In other words,


We also have, of course,


By solving these equations we find:

Therefore


65.

A gambler has £9 and has the opportunity of playing a game in which the probability is 0.4 that he wins an amount equal to his stake, and probability 0.6 that he loses his stake. He is allowed to decide how much to stake at each game (in multiple of 10p). How should he choose the stakes to maximise his chances of increasing his capital to £10?

66.

Let ξ1, ξ2, . . . be i.i.d. r.v.’s with values in, say, Z and P (ξ1 = x) = p(x), x ∈ Z. Let A ⊆ Z such that P (ξ1 ∈ A) > 0. Let TA = inf{n ≥ 1 : ξn ∈ A}. Show that P (ξTA = x) = p(x)/<sup>�</sup> a∈A<sup>p(a),x ∈A.</sup>

Solution. Let x ∈ A.


58

67.

For a simple symmetric random walk starting from 0, compute ESn<sup>4</sup>

n<sup>.</sup>

Solution. We have that Sn = ξ1 + · · · + ξn, where ξ1, . . . , ξn are i.i.d. with P (ξ1 = 1) = P (ξ1 = −1) = 1/2. When we expand the fourth power of the sum we have


After taking expectation, we see that the expectation of each term in the last three rows is zero, because Eξi = 0 and because of independence. There are n terms in the first row and 3(n<sup>2</sup> − n) terms in the second one. Hence


68.

For a simple random walk, compute E(Sn − ESn)<sup>4</sup> and observe that this is less than Cn<sup>2</sup> for some constant C.

---

[← Takis exercises Part 14 —](14-takis-exercises-part-14.md) · [Up: contents](index.md) · [Solution. Write →](16-solution-write.md)
