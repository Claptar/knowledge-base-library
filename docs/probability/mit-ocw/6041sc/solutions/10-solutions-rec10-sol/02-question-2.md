---
title: Question 2
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/10-solutions-rec10-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 2

**Source:** `solutions/10-solutions-rec10-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Heather and Taylor play a game using independent tosses of an unfair coin. A head comes up on any toss with probability p, where 0 < p < 1. The coin is tossed repeatedly until either the second time head comes up, in which case Heather wins; or the second time tail comes up, in which case Taylor wins. Note that a full game involves 2 or 3 tosses.

- 2.1. Consider a probabilistic model for the game in which the outcomes are the sequences of heads and tails in a full game. Provide a list of the outcomes and their probabilities of occurring. Because of the independence of the coin tosses, the outcomes and their probabilities are as follows:


- 2.2. What is the probability that Heather wins the game?

The event of Heather winning is {HH, HTH, THH}. Adding the probabilities of the out­ comes in this event gives p<sup>2</sup> + p<sup>2</sup> (1 − p) + p<sup>2</sup> (1 − p) = p<sup>2</sup> (3 − 2p).

Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- 2.3. What is the conditional probability that Heather wins the game given that head comes up on the first toss?


- 2.4. What is the conditional probability that head comes up on the first toss given that Heather wins the game?

---

[← Question 1](01-question-1.md) · [Up: contents](index.md) · [Question 3 →](03-question-3.md)
