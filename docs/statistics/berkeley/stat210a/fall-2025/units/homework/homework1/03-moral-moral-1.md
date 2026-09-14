---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework1.tex
source_file: sources/berkeley-stat210a/fall-2025/units/homework/homework1.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`units/homework/homework1.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework1.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Intuition may fail us when we condition on a measure-zero event, and in cases like this the meaning can be ambiguous and give different answers. Conditioning on a random variable, on the other hand, tends to give less ambiguous answers (there are still some ambiguities, similar to those we encounter in defining densities, but they don’t really matter).

**Problem 3** (Non-uniqueness of densities).

It can be good to keep in mind that, in general, densities are not unique. For example, depending on what textbook you look in you might find the standard exponential distribution $\text{Exp}(1)$ defined as the distribution with probability density function ${e^{-x}\cdot 1\{x > 0\}}$ or as the distribution with probability density function $e^{-x}\cdot 1\{x \geq 0\}$. Which one is the real exponential distribution?

The answer is that both are: the two densities are different functions but they result in exactly the same probability distribution because changing the integrand at a single point never affects a (Lebesgue or Riemann) integral. If we wanted to be perverse for some reason we could even define the density as something like $e^{-x}\cdot 1\{x > 0\} \cdot 1\{x \notin \mathbb{Q}\}$, and we’d still end up with exactly the same probability measure. So, while there is only one $\text{Exp}(1)$ distribution, there are many densities that equivalently describe its relationship to the Lebesgue measure.

However, you will show in this problem that any two density functions do have to be equal *almost everywhere*, meaning the set of points where they differ has to have measure $0$.

1.  Consider two densities $p_1$ and $p_2$ with respect to some common measure $\mu$ on a sample space $\mathcal{X}$. Suppose $p_1$ and $p_2$ both result in the same probability measure $P$ defined by $P(A) = \int 1_A(x)p_i(x)\,d \mu(x)$.

    Define the set $A = \{x:\; p_1(x) \neq p_2(x)\}$, and show that $\mu(A) = 0$.

    **Hint:** consider sets like $$A_{n} = \left\{x:\; p_1(x) - p_2(x) \in \left[\frac{1}{n+1}, \;\frac{1}{n}\right)\right\}$$ for $n=1,2,\ldots$. Don’t worry about whether the sets $A_n$ are measurable (they are).

2.  If $\mathcal{X}$ is countable, show that any probability measure $P$ on the sample space $\mathcal{X}$ has a unique density with respect to the counting measure $\#$ on $\mathcal{X}$.

3.  Let $P$ be a probability measure on $\mathbb{R}$, which has a density with respect to the Lebesgue measure. Show that $P$ has at most one continuous density $p$.

**Problem 4** (Densities for continuous-discrete mixtures). Suppose $\mu_1$ and $\mu_2$ are both measures on $\mathcal{X}$, and $a_1,a_2 \geq 0$. You may use without proof that the sum $\nu = a_1\mu_1 + a_2\mu_2$ is also a measure, and that we have $$\int f(x)\,d \nu(x) = a_1\int f(x)\,d \mu_1(x) + a_2\int f(x)\,d \mu_2(x),$$ provided the two integrals on the right are well-defined and finite.

1.  For $\mathcal{X}= [0,\infty)$, define the measure $\mu(A) = \lambda(A) + \#(A)$, where $\lambda$ represents the Lebesgue measure and $\#$ still represents the counting measure on the set of integers $\mathbb{Z}$. For fixed $\theta \in \mathbb{R}$, define the random variable $$X = \max(0,Z) \text{ where } Z \sim N(\theta, 1),$$ Let $P_\theta$ represent the probability distribution of $X$. Show that $P_\theta$ has no density with respect to $\lambda$ or $\#$. Find a density of $P_\theta$ with respect to $\mu$.

2.  Find a density for $P_\theta$ with respect to $P_0$, or show that none exists.

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
