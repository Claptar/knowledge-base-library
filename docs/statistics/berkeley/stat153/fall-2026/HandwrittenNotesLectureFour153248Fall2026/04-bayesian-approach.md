---
title: Bayesian Approach
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/HandwrittenNotesLectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Bayesian Approach

**Model:**
$$y_i = \boxed{\beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im}} + \boxed{\varepsilon_i}, \qquad i = 1, \dots, n$$
$$\varepsilon_i \sim N(0, \sigma^2)$$

$m + 1 + n$ variables

$$\to \beta_0, \dots, \beta_m \overset{\text{iid}}{\sim} \text{Unif}(-C, C)$$
$$\log \sigma \sim \text{Unif}(-C, C)$$

$$(\beta_0, \dots, \beta_m) \Big| \begin{matrix} \text{data} \\ y_1, \dots, y_n \end{matrix} \qquad \sigma \Big| \begin{matrix} \text{data} \\ = (y_1, \dots, y_n) \end{matrix}$$

---

$$f_{\beta | \text{data}}(\beta)$$

$$f_{\beta, \sigma | y_1, \dots, y_n}(\beta, \sigma)$$
$$\propto \underbrace{f_{y_1, \dots, y_n | \beta, \sigma}(y_1, \dots, y_n)}_{\text{Likelihood}} \underbrace{f_{\beta, \sigma}(\beta, \sigma)}_{\text{prior}}$$

$$\to = \sigma^{-n} \exp\left(-\frac{S(\beta)}{2\sigma^2}\right) \frac{I(-C < \beta_j < C)}{(2C)^{m+1}} \frac{I(-C < \log \sigma < C)}{2C \sigma}$$
$$\propto \sigma^{-n-1} \exp\left(-\frac{S(\beta)}{2\sigma^2}\right) I(\sigma > 0)$$

$\beta \mid \text{data}$
$$f_{\beta | \text{data}}(\beta) \propto \int_0^\infty \sigma^{-n-1} \exp\left(-\frac{S(\beta)}{2\sigma^2}\right) d\sigma$$
$$\propto \left( \frac{1}{S(\beta)} \right)^{n/2}$$

$$\left( \frac{S(\hat{\beta})}{S(\beta)} \right)^{n/2} \longrightarrow t\text{-distribution.}$$

---

[← Step 2: $\boxed{\text{Calculate the distribution.}}$](03-step-2.md) · [Up: contents](index.md)
