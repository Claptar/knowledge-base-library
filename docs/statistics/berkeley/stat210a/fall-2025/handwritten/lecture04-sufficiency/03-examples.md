---
title: Examples
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture04-sufficiency.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture04-sufficiency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture04-sufficiency.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture04-sufficiency.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Examples

### Ex. Normal location family

$$X_1, \dots, X_n \overset{\text{iid}}{\sim} N(\theta, 1) = \frac{1}{\sqrt{2\pi}} e^{-(x-\theta)^2 / 2}$$

$$p_\theta(x) = (2\pi)^{-n/2} \prod_{i=1}^n e^{-(x_i-\theta)^2 / 2}$$

$$= e^{\theta \sum x_i - n\theta^2 / 2} \cdot \frac{e^{-\sum x_i^2 / 2}}{(2\pi)^{n/2}} \quad (\text{collect factors with no dep. on } \theta)$$

$$\Rightarrow \sum X_i \quad \text{is sufficient}$$

### Ex. Poisson family

$$X_1, \dots, X_n \overset{\text{iid}}{\sim} \text{Pois}(\theta) = \frac{\theta^x e^{-\theta}}{x!} \quad \text{for } x = 0, 1, 2, \dots$$

$$p_\theta(x) = \prod_{i=1}^n \frac{\theta^{x_i} e^{-\theta}}{x_i!} = \theta^{\sum x_i} e^{-n\theta} \cdot \frac{1}{\prod x_i!}$$

$$\Rightarrow \sum X_i \quad \text{is sufficient}$$

These two examples have something important in common! (next lecture)

### Ex. Uniform location family

$$X_1, \dots, X_n \overset{\text{iid}}{\sim} U[\theta, \theta + 1] = \mathbf{1}\{\theta \le x \le \theta + 1\}$$

$$p_\theta(x) = \prod_{i=1}^n \mathbf{1}\{\theta \le x_i \le \theta + 1\}$$

$$= \mathbf{1}\{\theta \le X_{(1)}\} \, \mathbf{1}\{X_{(n)} \le \theta + 1\}$$

$$\Rightarrow (X_{(1)}, X_{(n)}) \quad \text{is sufficient.}$$

---

## Interpretations of Sufficiency

$X$ is informative about $\theta$ only because its distribution depends on $\theta$.

We can think of the data as being generated in two stages:

---

[← Factorization Theorem](02-factorization-theorem.md) · [Up: contents](index.md)
