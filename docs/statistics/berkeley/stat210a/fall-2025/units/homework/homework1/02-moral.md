---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework1.tex
source_file: sources/berkeley-stat210a/fall-2025/units/homework/homework1.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`units/homework/homework1.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework1.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

One motivation for measure theory is to find a way to exclude counterexamples like this. The pathological sets we’re constructing here do not make it into the Borel $\sigma$-field.

**Problem 2** (A conditional probability paradox).

Let $X,Y \overset{\text{i.i.d.}}{\sim}N(0,1)$. This problem is meant to show that by carelessly conditioning on probability-zero events we can get ourselves into trouble. It is directly inspired by a calculation I personally flubbed in graduate school.

1.  Defining $S = X + Y$ and $D = X - Y$, show $S$ and $D$ are independent and conclude that $$\mathbb{E}[X^2 + Y^2 \mid D] = D^2/2 + 1$$

2.  Now define the polar parameterization $(R,\Theta)$ with $R = \sqrt{X^2 + Y^2}$ and $\Theta \in [0,2\pi)$ such that $X  = R\cos \Theta$ and $Y = R\sin \Theta$. Show that $R$ is independent of $\Theta$ and conclude that $$\mathbb{E}[X^2 + Y^2 \mid \Theta] = 2$$

3.  Use (a) and then (b) to find the expectation of $X^2 + Y^2$ conditional on the event $X = Y$. Can you come up with an intuitive explanation for how we could have arrived at two different answers?

---

[← Homework1 Part 01 —](01-homework1-part-01.md) · [Up: contents](index.md) · [Moral →](03-moral.md)
