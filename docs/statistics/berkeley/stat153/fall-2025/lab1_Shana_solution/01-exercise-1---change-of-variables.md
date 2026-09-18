---
title: Exercise 1 - Change of Variables
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/lab1_Shana_solution.pdf
source_file: sources/berkeley-stat153/fall-2025/lab1_Shana_solution.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`lab1_Shana_solution.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/lab1_Shana_solution.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Exercise 1 - Change of Variables

September 8, 2025

Let $n > 0$. Consider the unnormalized function on $(0, \infty)$

$$g_n(s) = s^{-n-1} \exp\left(-\frac{1}{2s^2}\right).$$

Show that

$$\int_0^\infty s^{-n-1} \exp\left(-\frac{1}{2s^2}\right) ds = 2^{\frac{n}{2}-1} \Gamma\left(\frac{n}{2}\right).$$

*Hint:* Use change of variables $u = \frac{1}{2s^2}$

*Proof.* Let $n > 0$ and consider

$$I = \int_0^\infty s^{-n-1} \exp\left(-\frac{1}{2s^2}\right) ds.$$

Use the change of variables $u = \frac{1}{2s^2}$ so that

$$s = (2u)^{-1/2}, \quad ds = -(2u)^{-3/2} du.$$

Then

$$s^{-(n+1)} ds = ((2u)^{-1/2})^{-(n+1)} (-(2u)^{-3/2} du) = -(2u)^{(n-2)/2} du.$$

As $s : 0 \to \infty$, we have $u : \infty \to 0$, hence

$$\begin{aligned}
I &= \int_\infty^0 e^{-u} (-(2u)^{(n-2)/2}) du = \int_0^\infty e^{-u} (2u)^{\frac{n}{2}-1} du \\
&= 2^{\frac{n}{2}-1} \int_0^\infty u^{\frac{n}{2}-1} e^{-u} du = 2^{\frac{n}{2}-1} \Gamma\left(\frac{n}{2}\right).
\end{aligned}$$

Recall the $\text{Gamma}(\alpha, \beta)$ density (shape–rate parameterization)

$$f(u) = \frac{\beta^\alpha}{\Gamma(\alpha)} u^{\alpha-1} e^{-\beta u}, \quad u > 0, \ \alpha > 0, \ \beta > 0.$$

Thus the integrand $u^{\frac{n}{2}-1}e^{-u}$ is the (unnormalized) Gamma kernel with $\alpha = \frac{n}{2}$ and $\beta = 1$, so

$$\int_0^\infty u^{\frac{n}{2}-1} e^{-u} du = \Gamma\left(\frac{n}{2}\right).$$

Therefore,

$$\boxed{\int_0^\infty s^{-n-1} \exp\left(-\frac{1}{2s^2}\right) ds = 2^{\frac{n}{2}-1} \Gamma\left(\frac{n}{2}\right).}$$

---

[Up: contents](index.md) · [Exercise 2 - MLE →](02-exercise-2---mle.md)
