---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework3.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework3.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework3.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework3.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

The structure of the families and subfamilies determines the properties of the sufficient statistic.

**Problem 2** (Gamma family).

The gamma family is a two-parameter family of distributions on $\mathbb{R}_+ = [0,\infty)$, with density $$p_{k,\theta}(x) = \frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k}$$ with respect to the Lebesgue measure on $\mathbb{R}_+$. $k>0$ and $\theta>0$ are respectively called the shape and scale parameters, and $\Gamma(k)$ is the gamma function, defined as $$\Gamma(k) = \int_0^\infty x^{k-1}e^{-x}\,d x.$$ The gamma distribution generalizes the exponential distribution $$\text{Exp}(\theta) = \theta^{-1}e^{-x/\theta} = \text{Gamma}(1,\theta)$$ and the chi-squared distribution $$\chi_d^2 = \frac{x^{d/2-1}e^{-x/2}}{\Gamma(d/2)2^{d/2}} = \text{Gamma}(d/2,2).$$

1.  Show that the Gamma is a 2-parameter exponential family by putting it into its canonical form. Find the natural parameter, sufficient statistic, carrier density, and log-partition function (**Note**: there are multiple valid ways of doing this).

2.  Find the mean and variance of $X \sim \Gamma(k,\theta)$.

3.  Find the moment generating function of $X\sim \Gamma(k,\theta)$: $$M_X(u) = \mathbb{E}_{k,\theta}[e^{uX}],$$ and use it to find the distribution of $X_+ = \sum_{i=1}^n X_i$ where $X_1,\ldots,X_n$ are mutually independent with $X_i \sim \text{Gamma}(k_i, \theta)$.

    You may use without proof the following uniqueness result about MGFs: If $Y$ and $Z$ are two random variables whose MGFs coincide in a neighborhood of 0 ($\exists \delta>0$ for which $M_Y(u) =M_Z(u) < \infty$ for all $u\in[-\delta,\delta]$), then $Y$ and $Z$ have the same distribution.

**Problem 3** (Interpretation of completeness).

The concept of *completeness* for a family of measures was introduced in \citet{lehmann1950completeness} as a precursor to their definition, in the same paper, of a complete statistic. The definition of a complete family did not stick, and lives on only in the (consequently confusingly named) idea of complete statistic (in particular it has nothing to do with the definition of a *complete measure* that you can find on Wikipedia).

If $\mathcal{P}= \{P_\theta:\; \theta \in \Theta\}$ is a family of measures on $\mathcal{X}$, we say that $\mathcal{P}$ is *complete* if $$\int f(x)\,d  P_\theta(x) = 0, \;\forall \theta \quad\Rightarrow\quad
P_\theta(\{x:\; f(x) \neq 0\}) = 0, \;\forall \theta.$$ This can be interpreted as an inner product $\langle f, P_\theta\rangle = \int f\,d  P_\theta$, where $f \perp P_\theta$ if $\langle f, P_\theta\rangle = 0$. Then, the family is **not** complete if there is some nonzero function $f$ that is orthogonal to every $P_\theta$. We will try to gain some intuition for this definition and, thereby, for the definition of a complete statistic.

For the following parts, let $\mathcal{P}= \{P_\theta:\; \theta \in \Theta\}$ be a family of probabilty measures on $\mathcal{X}$, assume $T(X)$ is a statistic, and let $\mathcal{T}= T(\mathcal{X})$ be the range of the statistic $T(X)$. Let $\mathcal{P}^T = \{P_\theta^T:\; \theta\in \Theta\}$ denote the induced model of push-forward probability measures on $\mathcal{T}$ denoting the possible distributions of $T(X)$: $$P_\theta^T(B) = P_\theta(T^{-1}(B)) = \mathbb{P}_\theta(T(X) \in B).$$

1.  Show that $T(X)$ is a complete statistic for the family $\mathcal{P}$ if and only if $\mathcal{P}^T$ is a complete family.

2.  Assume (for this part only) that $\mathcal{X}$ is a finite set, i.e. $\mathcal{X}= \{x_1,\ldots, x_n\}$ for some $n<\infty$, and assume without loss of generality that every $x\in\mathcal{X}$ has $P_\theta(\{x\}) > 0$ for at least one value of $\theta$ (otherwise we could truncate the sample space).

    Let $p_\theta(x) = \mathbb{P}_\theta(X = x) \geq 0$, and $v^\theta = (p_\theta(x_1),\ldots,p_\theta(x_n)) \in \mathbb{R}^n$. Show that $\mathcal{P}$ is complete if and only if $\text{Span}\{v^\theta:\;\theta\in\Theta\} = \mathbb{R}^n$.

3.  Let $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}\text{Pois}(\theta)$ for $\theta\in \Theta = \{\theta_1,\ldots, \theta_m\}$ with $2 \leq m < \infty$. Find a sufficient statistic that is minimal but not complete (prove both properties).

4.  **Optional:** (Not graded, no extra points) In the same scenario but with $\Theta = \pi\mathbb{Z}_+ = \{0, \pi, 2\pi, \ldots\}$, show that the same statistic is minimal but not complete.

    **Hint:** Recall the Taylor series $$\sin(\theta) = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots.$$

5.  **Optional:** (Not graded, no extra points) Let $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}\text{Pois}(\theta)$ for $\theta\in \Theta$, and assume that $\Theta$ has an accumulation point at 0, i.e. $\Theta$ includes an infinite sequence of positive values $\theta_1,\theta_2,\ldots\in \Theta$ such that $\lim_{m\to\infty} \theta_m = 0$. Find a complete sufficient statistic and prove it is complete sufficient.

    **Hint:** suppose $f$ is a counterexample function; what is $f(0)$? It may be helpful to recall that $\int f\,d  \mu$ is undefined unless either $\int \max(0,f(x))\,d  \mu(x)$ or $\int \max(0, -f(x))\,d  \mu(x)$ is finite; as a result $\int f\,d  \mu = 0 \Rightarrow \int|f|\,d  \mu < \infty$.

---

[← Homework3 Part 01 —](01-homework3-part-01.md) · [Up: contents](index.md) · [Moral 1 →](03-moral-1.md)
