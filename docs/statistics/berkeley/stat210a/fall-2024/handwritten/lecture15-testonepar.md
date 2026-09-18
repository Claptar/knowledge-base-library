---
title: Testing with one real parameter
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture15-testonepar.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture15-testonepar.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture15-testonepar.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture15-testonepar.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Testing with one real parameter

### Outline

1) One-sided tests in general
2) Two-sided tests
3) UMP unbiased tests

---

## One-sided tests in general

$\mathcal{P} = \{P_\theta : \theta \in \Theta \subseteq \mathbb{R}\}$, $\theta_0 \in \Theta$

$H_0 : \theta \le \theta_0$ vs $H_1 : \theta > \theta_0$ called **one-sided hypothesis**

Often, no UMP test exists.

LRT may vary for different $\theta_1$ values

If $n$ large, could prioritize $\theta_1 = \theta_0 + \varepsilon$, $\varepsilon \downarrow 0$

$$\log LR(X) = \log \frac{p_{\theta_0 + \varepsilon}(X)}{p_{\theta_0}(X)} \approx \varepsilon \cdot \dot{\ell}(\theta_0; X)$$

$\implies$ Use **score at $\theta_0$** $\dot{\ell}(\theta_0; X)$ as test stat.

$$\phi(X) = \mathbf{1}\{\dot{\ell}(\theta_0; X) \ge c_\alpha\}$$

Need to check $\beta_\phi(\theta) \le \alpha$ for $\theta \le \theta_0$.

---

**Ex. Laplace:** $X_1, \dots, X_n \overset{iid}{\sim} \frac{1}{2} e^{-|x - \theta|}$

Test $H_0 : \theta \le \theta_0$ vs. \$H_1 : \theta >

---

[Up: contents](../index.md)
