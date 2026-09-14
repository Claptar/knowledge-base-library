---
title: What is a probability?
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/probability.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/probability.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# What is a probability?

**Source:** [`reader/probability.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/probability.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

There is some philosophical controversy about what probability is. Roughly speaking, there are two common answers:

1.  **Frequentist answer:** Probability represents a relative frequency of an outcome when an experiment is repeated many times.

2.  **Bayesian answer:** Probability represents a degree of belief that something is true, or that something will happen.

People who give the first answer tend to be doubtful that we can meaningfully assign probabilities to everything. There is no sense in which the next presidential election is an experiment that we can repeat. Below is a list of outcomes that seem more and more difficult to assign probabilities to. Think about where you would stop agreeing that probability is a meaningful construct:

1.   **The probability that a (roughly) physically symmetrical die will roll 4 on the next toss:** most people, regardless of their metaphysical views about probability, would probably agree on $1/6$, whether it is because they can imagine the die being tossed many times, because they believe the die has an equal physical propensity to land on any given face, or because they think we should be subjectively indifferent between any of the six outcomes.

2.   **The probability that a radiation treatment will be successful for a given cancer patient:** we could probably give some answer based on the fraction of patients for whom the treatment is successful, but we have to be careful about what comparison group to use: we should probably only include patients whose cancer is at a similar stage and who are roughly the same age, but perhaps we should take into account other factors like the patient's family history, other aspects of their health profile, the cancer's genetic profile, etc. By the time we get done conditioning on everything that might matter, the patient may be the only person left in our comparison class.

3.   **The probability that the Democratic candidate will win the next presidential election:** every presidential election is a truly one-off event, and anyone whose opinion is worth listening to can probably list a few important aspects of this election that are more or less unprecedented.

4.   **The probability that a given subatomic particle has the mass predicted by a certain physical theory:** this is not the probability that *something will happen* but a probability that *something is true about the world*. Whether it is true or false, it has been so since the creation of the universe.

5.   **The probability that P = NP (as a statement about computational complexity theory):** whether or not this is true is a purely mathematical question, but it is one that may or may not be resolved in our lifetime.

6.   **The probability that the 20th digit of** $\sqrt{2}$ **is 5:** this is another mathematical question that you could probably work out for yourself in a few minutes with just a pencil and paper and no new data about the world, so it seems perverse to think of it as random. Still, if you were forced to place a bet and didn't have time to work it out you might assign a $10\%$ probability.

The two great statistical frameworks of frequentist and Bayesian statistics loosely correspond to the two views about probability above. Generally speaking, Bayesians get a lot of mileage out of being willing to assign probabilities to everything, while frequentists try to take a more conservative course where possible, allowing some quantities to simply be unknown.

A great deal of ink has been spilled about whether one approach is superior to another. Fifty years ago, it was more common for statisticians to be dogmatically committed to one or the other view, but nowadays the mainstream view is that both approaches have strengths and weaknesses, and which framework to use is a pragmatic choice that should be made on a case-by-case basis.

Fortunately, the philosophical and methodological disagreements between frequentists and Bayesians are not disagreements about the mathematical construct of probability, only questions about how and when these mathematical formalisms should be connected to real-world questions. There is very little controversy about how we should conceive of probability mathematically. This leads us to our third answer:

3.  **Mathematical answer:** a probability is a measure $P$ on a sample space $\cX$, which assigns total measure $1$ to the sample space.

<!-- function $P$ mapping (non-pathological[^1]) subsets of a sample space $\cX$ to a number in $[0,1]$, for which $P(\cX) = 1$ and which is **additive** over disjoint subsets, meaning -->

<!-- [^1]: A problem in the first homework will guide you step-by-step in constructing the kind of pathological set that makes the parenthetical caveat necessary when we are dealing with continuous spaces. -->

<!-- $$ -->
<!-- P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i), \quad \text{ if } A_i \cap A_j = \emptyset \text{ for all } i \neq j. -->
<!-- $$ -->

---

[Up: contents](index.md) · [Probability as a measure →](02-probability-as-a-measure.md)
