---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework7.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework7.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework7.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework7.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

In some sense, the Jeffreys prior in scale families plays the same role that the flat prior plays in location families. In this problem, since we chose a scale-invariant loss based on relative error, the problem is equally hard everywhere in the parameter space, so the problem exhibits a kind of scale symmetry that is analogous to the translational symmetry that we see when we have a location family and a translationally invariant loss.

**Problem 2** (Monotone likelihood ratio and location families).

A one-parameter family $\mathcal{P}= \{P_\theta:\;\theta\in\Theta\}$, with $\Theta\subseteq \mathbb{R}$, has *monotone likelihood ratios* in a statistic $T(X)$ if $$\frac{p_{\theta_1}(x)}{p_{\theta_0}(x)} \text{ is a non-decreasing function of } T(X), \text{ for all } \theta_0\leq \theta_1.$$

1.  Assume $X\sim p_\theta(x) = p_0(x-\theta)$, a location family with $p_0$ continuous and strictly positive. Show that the family has MLR in $x$ if and only if $\log p_0$ is concave.

    **Note:** For full credit, you should not assume that $p_0$ is differentiable.

    **Hint 1:** It may help to recall that $f(x)$ is convex if and only if $$R(x_1,x_2) = \frac{f(x_1) - f(x_2)}{x_1-x_2}$$ is non-decreasing in $x_1$ and $x_2$.

    **Hint 2:** It may also help to recall that a continuous function $f$ is convex if and only if it is *midpoint convex* meaning $$f\left(\frac{x_1+x_2}{2}\right) \leq \frac{f(x_1) + f(x_2)}{2}, \quad \text{ for all } x_1,x_2.$$

2.  Consider testing in the Cauchy location family: $$p_{\theta}(x) = \frac{1}{\pi (1+(x-\theta)^2)}.$$ Let $\theta_0, \theta_1$ be any two real numbers with $\theta_1> \theta_0$ and consider the LRT for testing $H_0:\; \theta = \theta_0$ vs $H_1:\; \theta = \theta_1$ at some level $\alpha \in (0,1)$. Show that for some $\alpha^*(\theta_0,\theta_1)$, the rejection region for any $\alpha < \alpha^*$ is a bounded interval, and the rejection region for any $\alpha > \alpha^*$ is a union of two half intervals. Find $\alpha^*$.

    **Hint:** recall that $\frac{d}{dx}\arctan(x) = \frac{1}{1+x^2}$.

3.  In the Cauchy location family, prove that, for any $\alpha \in (0,1)$, there exists no UMP level-$\alpha$ test of $H_0:\;\theta = 0$ vs. $H_1:\; \theta > 0$.

4.  Consider testing $H_0:\theta = 0$ vs. $H_1:\; \theta = 6$ in the Cauchy location family at level $\alpha = 0.01$. Numerically calculate the rejection region and the power for the LRT, and also for the one-tailed test that rejects for large values of $X$.

5.  In words, can you explain why the optimal LRT rejection regions for the Cauchy distribution take this odd form? Think about how you would explain to a scientific collaborator why you are proposing such an odd test, beyond “it fell out of an optimization problem.”

---

[← Homework7 Part 01 —](01-homework7-part-01.md) · [Up: contents](index.md) · [Moral →](03-moral.md)
