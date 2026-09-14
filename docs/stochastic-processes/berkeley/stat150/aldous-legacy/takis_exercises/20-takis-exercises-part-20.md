---
title: Takis exercises Part 20 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 20 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There are two decks of cards. Deck 1 contains 50 Red cards, 30 Blue cards, and 20 Jokers. Deck 2 contains 10, 80, 10, respectively. At each stage we select a card from a deck. If we select a Red card then, we select a card of the other deck at the next stage. If we select a Blue card then we select a card from the same deck at the next stage. If, at any stage, a Joker is selected, then the game ends. Cards are always replaced in the decks. Set up a Markov chain and find, if we first pick up a card at random from a deck at random, how many steps it takes on the average for the game to end.

Solution. The obvious Markov chain has three states: 1 (you take a card from Deck 1), 2 (you take a card from Deck 2), and J (you selected a Joker). We have:


Let ψ(i) be the average number of steps for the game to end. when we start from deck i Then


Solve for ψ(1), ψ(2). Since the initial deck is selected at random, the answer is (ψ(1)+ ψ(1))/2.

64

---

[← Solution. We have](19-solution-we-have.md) · [Up: contents](index.md) · [Takis exercises Part 21 — →](21-takis-exercises-part-21.md)
