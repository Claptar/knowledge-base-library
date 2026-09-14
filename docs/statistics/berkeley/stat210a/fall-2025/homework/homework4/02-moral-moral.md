---
title: 'Moral: {#moral}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework4.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework4.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral}

**Source:** [`homework/homework4.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework4.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Without any restrictions on the family $\mathcal{P}$, we can’t do much better than estimating population quantities with sample quantities (when the sample quantities are unbiased). In the case of the mean, for examples, $\overline X$ is always availableas an unbiased estimator of $\mathbb{E}X$, but if we impose additional assumptions on the family then we might be able to do better.

**Problem 2** (Unbiased estimation in replicated studies).

One focal issue in the ongoing scientific replication crisis is the “file drawer problem,” i.e. the tendency of researchers to report findings (or of journals to publish them) only if they have a $p$-value less than 0.05. Replication studies typically represent cleaner estimates of the results under study, since they are reported regardless of whether they are statistically significant. This is one of the reasons that replication studies often find much smaller effect size estimates than the original studies: if the original study had gotten a good estimate of the (small) true effect, we wouldn’t have heard about it.

We can introduce a toy model for a replicated study where the original study is $X_1 \sim N(\mu, 1)$ and the replication study is $X_2 \sim N(\mu, 1)$, but we only observe the study pair given that $X_1 > c$ for some significance cutoff $c \in \mathbb{R}$, e.g. $c=1.96$. In other words, the distribution for a study pair conditional on our observing it is $$\begin{align*}
p_\mu(x_1,x_2) &= \mathbb{P}_\mu(X_1=x_1,X_2=x_2 \mid X_1 > c)\\
  &= \frac{\phi(x_1-\mu)1\{x_1 > c\}}{1-\Phi(c-\mu)} \phi(x_2-\mu),
\end{align*}$$ where $\phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ is the standard normal pdf and $\Phi(x) =  \int_{-\infty}^x \phi(u)\,d  u$ is the standard normal cdf. We will consider the problem of estimating $\mu$ after observing a study pair.

Arguably, we should only care about the *conditional* bias or risk of an estimator, given that we actually get to see the data, since the conditional distribution more accurately describes the set of published results. Thus, all questions below about bias, admissibility, UMVU, etc.  should be answered in terms of the conditional distribution given that $X_1>c$ (i.e., with densities $p_{\mu}(x_1,x_2)$ above), *not* in terms of the marginal distribution (whose densities would be $\phi(x_1-\mu)\phi(x_2-\mu)$.) For example, in part (a) it would not be true to say that $\overline X$ is marginally biased, but I want you to show it is conditionally biased given that it is observed.

1.  Show that $\overline X = (X_1 + X_2)/2$ is an upwardly biased estimator of $\mu$ (we can call this the *naive* estimator since it ignores the selection bias).

2.  Show that $X_2$ is unbiased for $\mu$, but it is inadmissible under any strictly convex loss function (we can call this the *data splitting* estimator since we ignore $X_1$, which was used for selection, and use the fresh data $X_2$.)

3.  Show that the UMVU estimator for $\mu$ is $$\delta(\overline{X}) = \overline{X} -
    \frac{1}{\sqrt{2}}\;\zeta\left(\sqrt{2}(c-\overline{X})\right),$$ where $$\zeta(x) = \mathbb{E}_{Z \sim N(0,1)}[Z \mid Z > x] = \frac{\int_x^\infty u\phi(u)\,d  u}{1-\Phi(x)}.$$ **Hint:** It may help to note that $X_1+X_2$ is marginally independent of $X_1 - X_2$ (but note they are **not** conditionally independent given $X_1 > c$.)

4.  Show that $$\lim_{\overline{X} \to \infty} \delta(\overline{X}) - \overline{X} = 0.$$ In other words, if $\overline{X} \gg c$, then $\delta(\overline{X}) \approx \overline{X}$, the naive estimator. Can you give any intuition for why this limit makes sense?

5.  **Optional:** (Not graded, no extra points) Show that $$\lim_{\overline{X} \to -\infty} \delta(\overline{X}) - \left(X_2 + (X_1-c)\right) = 0,$$ and furthermore that for any $\varepsilon> 0$, we have $$\lim_{\overline{X} \to -\infty} \mathbb{P}(X_1 - c > \varepsilon\mid \overline{X}, X_1 > c) \to 0.$$ In other words, if $\overline{X} \ll c$, we have $\delta(\overline{X}) \approx X_2 + (X_1-c) \approx X_2$, the data splitting estimator. Can you give any intuition for why this limit makes sense?

    **Hint:** It may be helpful to use the tail inequality $$\left(\frac{1}{x} - \frac{1}{x^3}\right)\phi(x) \leq 1-\Phi(x) \leq \frac{1}{x} \phi(x),$$ for $x>0$.

---

[← Homework4 Part 01 —](01-homework4-part-01.md) · [Up: contents](index.md) · [Moral: {#moral-1} →](03-moral-moral-1.md)
