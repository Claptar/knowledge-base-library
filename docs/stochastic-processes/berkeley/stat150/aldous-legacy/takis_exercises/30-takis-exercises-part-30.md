---
title: Takis exercises Part 30 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 30 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There are N coloured items. There are c possible colours. Pick an items at random and change its colour to one of the other c − 1 colours at random. Keep doing this. What is the Markov chain describing this experiment? Find its stationary distribution. (Hint: When c = 2 it is the Ehrenfest chain.)

Solution. The Markov chain has states


where xi is the number of items having colour i. Of course, x1 + · · · + xc = N . If we let ei be the vector with 1 in the i-th position and 0 everywhere else, then we see that from state x only a transition to a state of the form x − ei + ej is possible if xi > 0. The transition probability is


because xi/N is the probability that you pick an item with colour i, and 1/(c − 1) is the probability that its new colour will be j. To find the stationary distribution π(x) we just try to see if detailed balance equations hold. If they do then we are happy and know that we have found it. If they don’t, well, we don’t give up and try to see how to satisfy the (full) balance equations. Recall:

• Full balance equations: π(x) =<sup>�</sup> y<sup>π(y)p(y, x),forallx.</sup> If the chain is finite (and here it is), we can always find a probability distribution π that satisfies the full balance equations.

• Detailed balance equations: π(x)p(x, y) = π(y)p(y, x), for all x, y.

71

Even if the chain is finite, it is NOT always the case that detailed balance hold. If they do, then we should feel lucky!

Since, for c = 2 (the Ehrenfest chain) the stationary distribution is the binomial distribution, we may GUESS that the stationary distribution here is multinomial:


Now


If y, x are not related by y = x − ei + ej for some distinct colours i, j, then p(x, y) = p(y, x) = 0, and so the equations hold trivially. Suppose then that y = x − ei + ej for some distinct colours i, j, then p(x, y) = p(y, x) = 0, and so the equations hold trivially. Suppose then that y = x − ei + ej for some distinct colours i, j. We have

---

[← Takis exercises Part 29 —](29-takis-exercises-part-29.md) · [Up: contents](index.md) · [and →](31-and.md)
