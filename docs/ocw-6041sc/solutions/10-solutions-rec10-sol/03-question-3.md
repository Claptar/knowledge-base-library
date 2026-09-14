---
title: Question 3
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/10-solutions-rec10-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 3

**Source:** `solutions/10-solutions-rec10-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A casino game using a fair 4-sided die (with labels 1, 2, 3, and 4) is offered in which a basic game has 1 or 2 die rolls:

- If the first roll is a 1, 2, or 3, the player wins the amount of the die roll, in dollars, and the game is over.

- If the first roll is a 4, the player wins $2 and the amount of a second (“bonus”) die roll in dollars.

Let X be the payoff in dollars of the basic game.

- 3.1. Find the PMF of X, pX(x).

Define a probabilistic model in which the outcomes are the sequences of rolls in a full game. The outcomes, their probabilities, and the resulting values of X are as follows:

|ω|P({ω})|X(ω)|
|---|---|---|
|(1)|1/4|1|
|(2)|1/4|2|
|(3)<br>|1/4<br>|3|
|(4, 1)|1/16|3|
|(4, 2)<br>|1/16<br>|4|
|(4, 3)|1/16|5|
|(4, 4)|1/16|6|


Page 2 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

By gathering the probabilities of the possible values for X, we obtain


- 3.2. Find E[X].

It does not take too much arithmetic to compute E[X] using the PMF computed in the previous part. A more elegant solution is to use the total expectation theorem. Let A be the event that the first roll is a 4. Then


where E[X | A] = 4.5 because the conditional distribution is uniform on {3, 4, 5, 6}; and E[X | A<sup>c</sup> ] = 2 because the conditional distribution is uniform on {1, 2, 3}.

- 3.3. Find the conditional PMF of the result of the first die roll given that X = 3. (Use a reasonable notation that you define explicitly.)

Let Z be the result of the first die roll, and let B = {X = 3}. By definition of conditioning,


By using values tabulated above,


- 3.4. Now consider an extended game that can have any number of bonus rolls. Specifically:

   - Any roll of a 1, 2, or 3 results in the player winning the amount of the die roll, in dollars, and the termination of the game.

   - Any roll of a 4 results in the player winning $2 and continuation of the game.

Let Y denote the payoff in dollars of the extended game. Find E[Y ].

One could explicitly find the PMF of Y , but this is unnecessarily messy. Instead, let L be the payoff of the last roll and let W be the payoff of all of the earlier rolls. Then Y = W + L by construction, and E[Y ] = E[W ] + E[L].

The last roll is uniformly distributed on {1, 2, 3}, so E[L] = 2. The winnings on earlier rolls is 2(N − 1) where N is the number of rolls in the game. Since termination of the game can be seen as “success” on a Bernoulli trial with success probability of 3/4, N has the geometric distribution with parameter 3/4. Thus,


Combining the calculations,


(Many other methods of solution are possible.)

Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Question 2](02-question-2.md) · [Up: contents](index.md)
