---
title: Takis exercises Part 02 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 02 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A certain calculating machine uses only the digits 0 and 1. It is supposed to transmit one of these digits through several stages. However, at every stage, there is a probability p that the digit that enters this stage will be changed when it leaves and a probability q = 1 − p that it won’t. Form a Markov chain to represent the process of transmission by taking as states the digits 0 and 1. What is the matrix of transition probabilities?

Now draw a tree and assign probabilities assuming that the process begins in state 0 and moves through two stages of transmission. What is the probability that the machine, after two stages, produces the digit 0 (i.e., the correct digit)?

Solution. Taking as states the digits 0 and 1 we identify the following Markov chain (by specifying states and transition probabilities):


where p + q = 1. Thus, the transition matrix is as follows:


It is clear that the probability that that the machine will produce 0 if it starts with 0 is p<sup>2</sup> + q<sup>2</sup> .

---

[← Takis exercises Part 01 —](01-takis-exercises-part-01.md) · [Up: contents](index.md) · [Takis exercises Part 03 — →](03-takis-exercises-part-03.md)
