---
title: (2) Moment generating function
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation/recitation2.pdf
source_file: sources/berkeley-stat210a/fall-2025/recitation/recitation2.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`recitation/recitation2.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation/recitation2.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# (2) Moment generating function

$X$: a random variable

Suppose $\mathbb{E}[e^{uX}] < +\infty$ for $-r < u < r$.

We define the moment generating function of $X$ as
$$M_X(u) = \mathbb{E}[e^{uX}] \quad \text{for } -r < u < r.$$

**Example)** $X \sim N(\mu, \sigma^2)$

Recall that the pdf of $X$ is
$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right], \quad x \in \mathbb{R}$$

$$\begin{aligned}
\implies M_X(u) = \mathbb{E}[e^{ux}] &= \int_{-\infty}^\infty \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-\frac{(x-\mu)^2}{2\sigma^2} + ux\right] dx \\
&= \int_{-\infty}^\infty \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-\frac{1}{2\sigma^2}(x-\mu-u\sigma^2)^2 + u\mu + \frac{u^2}{2}\sigma^2\right] dx \\
&= \exp\left\{u\mu + \frac{u^2}{2}\sigma^2\right\}
\end{aligned}$$

* For every $m \in \mathbb{N}$,
$$\mathbb{E}[X^m] = M_X^{(m)}(0)$$

* $M_X(u) = \sum_{k=0}^\infty \frac{1}{k!} \mathbb{E}[X^k] u^k \quad \text{for } -r < u < r$   (called "moment")

* $X, Y$: random variables

  If $\exists \, \varepsilon > 0$ s.t. $M_X(u) = M_Y(u)$ for $-\varepsilon < u < \varepsilon$,
  then $X$ and $Y$ have the same distribution.

**Example)** $X \sim N(0, \sigma^2)$
$$\begin{aligned}
M_X(u) &= \exp\left\{\frac{u^2}{2}\sigma^2\right\} = \sum_{k=0}^\infty \frac{1}{k!} \left(\frac{u^2}{2}\sigma^2\right)^k \quad \left(\exp(t) = \sum_{k=0}^\infty \frac{1}{k!} t^k\right) \\
&= \sum_{k=0}^\infty \frac{\sigma^{2k}}{2^k \cdot k!} \times u^{2k} \quad \text{for } u \in \mathbb{R}
\end{aligned}$$

$$\implies \mathbb{E}[X^k] = \begin{cases} 0 & \text{if } k \text{ odd} \\ \frac{k!}{2^{\frac{k}{2}} (\frac{k}{2})!} \times \sigma^k & \text{if } k \text{ even} \end{cases}$$

---

---

← (1) Probability generating function · [Up: contents](index.md) · [(3) Change of variables for pdf →](03-3-change-of-variables-for-pdf.md)
