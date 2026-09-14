---
title: 10 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 slides

**Source:** `recitations/10-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Recitation 10 October 12, 2010

- Question 1. The two parts of this question are about identities for a probabilistic model with sample space Ω, events A and B, and discrete random variable X. Any time conditioning on an event is indicated, the event has positive probability. An identity is true when it holds without any additional restrictions; it is false when there is any counterexample.

   - 1.1. Which one of the following statements is true?

      - (a) P(A ∩ B) may be larger than P(A).

      - (b) The variance of X may be larger than the variance of 2X.

      - (c) If A<sup>c</sup> ∩ B<sup>c</sup> = ∅, then P(A ∪ B) = 1.

      - (d) If A<sup>c</sup> ∩ B<sup>c</sup> = ∅, then P(A ∩ B) = P(A)P(B).

      - (e) If P(A) > 1/2 and P(B) > 1/2, then P(A ∪ B) = 1.

   - 1.2. Which one of the following statements is true?

      - (a) If E[X] = 0, then P(X > 0) = P(X < 0).

      - (b) P(A) = P(A | B) + P(A | B<sup>c</sup> )

      - (c) P(B | A) + P(B | A<sup>c</sup> ) = 1

      - (d) P(B | A) + P(B<sup>c</sup> | A<sup>c</sup> ) = 1

      - (e) P(B | A) + P(B<sup>c</sup> | A) = 1

- Question 2. Provide clear reasoning; partial credit is possible

Heather and Taylor play a game using independent tosses of an unfair coin. A head comes up on any toss with probability p, where 0 < p < 1. The coin is tossed repeatedly until either the second time head comes up, in which case Heather wins; or the second time tail comes up, in which case Taylor wins. Note that a full game involves 2 or 3 tosses.

- 2.1. Consider a probabilistic model for the game in which the outcomes are the sequences of heads and tails in a full game. Provide a list of the outcomes and their probabilities of occurring.

- 2.2. What is the probability that Heather wins the game?

- 2.3. What is the conditional probability that Heather wins the game given that head comes up on the first toss?

- 2.4. What is the conditional probability that head comes up on the first toss given that Heather wins the game?

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

- Question 3. Provide clear reasoning; partial credit is possible

A casino game using a fair 4-sided die (with labels 1, 2, 3, and 4) is offered in which a basic game has 1 or 2 die rolls:

- If the first roll is a 1, 2, or 3, the player wins the amount of the die roll, in dollars, and the game is over.

- If the first roll is a 4, the player wins $2 and the amount of a second (“bonus”) die roll in dollars.

Let X be the payoff in dollars of the basic game.

- 3.1. Find the PMF of X, pX(x).

- 3.2. Find E[X].

- 3.3. Find the conditional PMF of the result of the first die roll given that X = 3. (Use a reasonable notation that you define explicitly.)

- 3.4. Now consider an extended game that can have any number of bonus rolls. Specifically:

   - ∗ Any roll of a 1, 2, or 3 results in the player winning the amount of the die roll, in dollars, and the termination of the game.

   - ∗ Any roll of a 4 results in the player winning $2 and continuation of the game.

   - Let Y denote the payoff in dollars of the extended game. Find E[Y ].

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
