---
title: "26. Hypergeometric Probabilities"
course: "MIT 6.041SC"
chapter: 26
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 26. Hypergeometric Probabilities

## What this covers

This chapter answers a single counting question: an urn holds $n$ balls, $m$ of which are red and
the rest black; we draw $k$ balls without replacement; what is the probability that exactly $i$ of
the drawn balls are red? It assumes the reader already has the counting rule for combinations —
$\binom{r}{j}$, the number of ways to choose $j$ objects out of $r$ — and the equally-likely-outcomes
model of probability: when a sample space is a finite set of equally likely outcomes, the
probability of an event is the fraction of the sample space it occupies.

## The urn model

Picture the $n$ balls in a box, split by a line into two groups: $m$ red balls on one side and
$n-m$ black balls on the other — "red" and "black" just name "the kind being counted" and
"everything else." From this box a subset of $k$ balls is drawn: order doesn't matter, and a ball
is not returned once drawn. Write $p_r$ for the probability that exactly $i$ of the $k$ drawn balls
are red, so that $k-i$ are black.

## The sample space

Since a draw is an unordered subset of $k$ balls chosen from $n$, the natural sample space is the
set of all such subsets:
$$\Omega = \{\text{all } k\text{-subsets of the } n \text{ balls}\}, \qquad |\Omega| = \binom{n}{k}.$$
Every $k$-subset is equally likely, so the probability of any event is the count of subsets
belonging to it, divided by $\binom{n}{k}$.

## Counting the subsets with exactly $i$ red balls

Let $c$ be the number of $k$-subsets containing exactly $i$ red balls. Building one such subset is
a two-stage choice, and the stages don't interact: first pick which $i$ of the $m$ red balls are in
the subset, then separately pick which $k-i$ of the $n-m$ black balls are in it. If $a$ counts the
first stage and $b$ the second, the counting principle gives $c = a \cdot b$, and each stage is
itself a combination count:
$$a = \binom{m}{i}, \qquad b = \binom{n-m}{k-i}, \qquad c = \binom{m}{i}\binom{n-m}{k-i}.$$

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A box of n balls split into m red and n minus m black, with a drawn sample of k balls straddling both groups.">
  <rect x="30" y="50" width="280" height="120" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="110" y1="50" x2="110" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <text x="70" y="42" text-anchor="middle" font-size="12" fill="currentColor">m red</text>
  <text x="210" y="42" text-anchor="middle" font-size="12" fill="currentColor">n &#8722; m black</text>
  <ellipse cx="140" cy="110" rx="70" ry="48" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="90" y="114" text-anchor="middle" font-size="12" fill="currentColor">i red</text>
  <text x="190" y="114" text-anchor="middle" font-size="12" fill="currentColor">k &#8722; i black</text>
  <text x="170" y="198" text-anchor="middle" font-size="12" fill="currentColor">drawn sample of size k</text>
</svg>
<figcaption>The box of n balls split into m red and n − m black; the dashed ellipse is one draw of
k balls, taking i from the red side and k − i from the black side.</figcaption>
</figure>

## The hypergeometric probability

Dividing the count of favorable subsets by the size of the sample space gives
$$p_r = P(\text{exactly } i \text{ red}) = \frac{\binom{m}{i}\binom{n-m}{k-i}}{\binom{n}{k}}.$$
This is the hypergeometric probability — as a function of $i$, the hypergeometric distribution: the
law governing the number of "special" items (here, red balls) in a fixed-size sample drawn without
replacement from a finite population containing a fixed number of them.

## Worked example: aces in a seven-card hand

Take a standard deck, $n = 52$ cards, of which $m = 4$ are aces, so $n - m = 48$ are not. Deal
$k = 7$ cards and ask for the probability that exactly $i = 3$ of them are aces. Casting the deck
into the urn picture — aces playing the role of red balls, the rest of the deck playing the role of
black balls, dealing a hand playing the role of drawing $k$ balls — lets the formula carry over
unchanged; only the substitution changes:
$$p_r = \frac{\binom{4}{3}\binom{48}{4}}{\binom{52}{7}} = \frac{4 \times 194580}{133784560} \approx 0.0058.$$

## Sources

- Everything above is from the single supplied document for this chapter: a model-reconstructed
  transcript of an MIT 6.041SC recitation, "Hypergeometric Probabilities"
  (`docs/probability/mit-ocw/6041sc/other/edit2-take2-no13-ch1-hypergeometicprobabilities-slides.md`
  in the library repository), converted from a slide PDF that had no usable text layer. The source
  file itself flags that the prose is a paraphrase and every equation is unverified, reconstructed
  by a model reading the scanned pages — treat the formulas here as a pointer into the original
  slides, not as independently checked.
- No separate slide deck, lecture transcript, written notes, or problem set were supplied alongside
  it for this chapter; it is a single stray recording, as reflected in the short length here.
- The final decimal in the worked example ($\approx 0.0058$) completes the substitution the source
  sets up but stops short of evaluating; it is arithmetic on the source's own numbers, not an
  added example.

---

[← 25. Classical Hypothesis Testing](25-classical-hypothesis-testing.md) · [Contents](index.md)
