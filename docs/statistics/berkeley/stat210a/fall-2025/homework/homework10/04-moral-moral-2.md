---
title: 'Moral: {#moral-2}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework10.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework10.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-2}

**Source:** [`homework/homework10.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework10.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

This is an example of a “deduced inference” whereby we arrive at simultaneous confidence regions for many (even infinitely many in this case) estimands at once, by assuming that an initial confidence region covers and then “deducing” all possible conclusions that follow from that assumption. So long as the initial confidence region covers, our deductions will all be simultaneously correct.

**Problem 4** (Probabilistic big-O notation).

Let $X_1,X_2,\ldots$ denote a sequence of random vectors (with $\|X_n\| <\infty$ almost surely for each $n$). We say the sequence is *bounded in probability* (or sometimes *tight*) if for every $\varepsilon>0$ there exists a constant $M_\varepsilon> 0$ for which $$\mathbb{P}(\|X_n\| > M_\varepsilon) < \varepsilon, \quad \forall n.$$

Informally, there is “no mass escaping to infinity” as $n$ grows. Like regular big-O notation, these symbols can help to make rigorous asymptotic proofs look clean and intuitive.

For a fixed sequence $a_n$, we say $X_n = o_p(a_n)$ if $X_n/a_n \overset{p}{\to}0$ as $n\to \infty$, and $X_n = O_p(a_n)$ if the sequence $(X_n/a_n)_{n\geq 1}$ is bounded in probability.

Prove the following facts for $X_n, Y_n \in \mathbb{R}^d$:

1.  If $X_n \Rightarrow X$ for any random vector $X$, then $X_n = O_p(1)$.

2.  If $X_n = o_p(a_n)$ then $X_n = O_p(a_n)$.

3.  If $X_n = O_p(a_n)$ and $Y_n = o_p(b_n)$, then $X_n'Y_n = o_p(a_n b_n)$. If $X_n = O_p(a_n)$ and $Y_n = O_p(b_n)$, then $X_n'Y_n = O_p(a_n b_n)$.

4.  If $X_n = O_p(1)$ and $g:\; \mathbb{R}^d \to \mathbb{R}^k$ is continuous then $g(X_n) = O_p(1)$.

5.  For $d=1$, if $X_n = O_p(a_n)$ with $a_n \to 0$ and $g:\; \mathbb{R}\to \mathbb{R}$ is continuously differentiable with $g(0) = \dot{g}(0) = 0$, then $g(X_n) = o_p(a_n)$. Show further that if $g$ is twice continuously differentiable then $g(X_n) = O_p(a_n^2)$. (**Hint:** Use the mean value theorem and apply a previous part of this problem.)

6.  For $d=1$, if $\text{Var}(X_n) = a_n^2 < \infty$ and $\mathbb{E}X_n = 0$ then $X_n = O_p(a_n)$. (**Hint:** Use Chebyshev’s inequality.)

7.  If $\text{Var}(X_n) = a_n^2 < \infty$, is it impossible to have $X_n = o_p(a_n)$? Prove or give a counterexample.

---

[← Moral: {#moral-1}](03-moral-moral-1.md) · [Up: contents](index.md) · [Moral: {#moral-3} →](05-moral-moral-3.md)
