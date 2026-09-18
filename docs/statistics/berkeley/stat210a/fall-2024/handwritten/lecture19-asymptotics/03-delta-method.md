---
title: Delta Method
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture19-asymptotics.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture19-asymptotics.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture19-asymptotics.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture19-asymptotics.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Delta Method

[Scaling factor doesn't need to be $\sqrt{n}$, but need $X_n - \mu \overset{P}{\to} 0$]

---

**Ex** $X_1, \dots, X_n \overset{\text{iid}}{\sim} (\mu, \sigma^2)$
$Y_1, \dots, Y_n \overset{\text{iid}}{\sim} (\nu, \tau^2) \qquad X, Y \text{ indep.}$

For large $n$, what is the distribution of $(\bar{X} + \bar{Y})^2$?

1) $\bar{X} \overset{P}{\to} \mu, \quad \bar{Y} \overset{P}{\to} \nu \qquad \text{as } n \to \infty$
$\implies (\bar{X} + \bar{Y})^2 \overset{P}{\to} (\mu + \nu)^2 \qquad \checkmark$

2) $\sqrt{n}(\bar{X} - \mu) \Rightarrow N(0, \sigma^2) \qquad \sqrt{n}(\bar{Y} - \nu) \Rightarrow N(0, \tau^2)$
Let $f(x, y) = (x + y)^2$
$\frac{\partial f}{\partial x}(x, y) = \frac{\partial f}{\partial y}(x, y) = 2(x + y)$

$$
\begin{aligned}
f(\bar{X}, \bar{Y}) &\approx N\left(f(\mu, \nu), \, \nabla f' \begin{pmatrix} \sigma^2 & 0 \\ 0 & \tau^2 \end{pmatrix} \nabla f \,/\, n\right) \\
&= N\left((\mu + \nu)^2, \, 4(\mu + \nu)^2 (\sigma^2 + \tau^2) \,/\, n\right)
\end{aligned}
$$

More accurate:
$$
\sqrt{n}\left((\bar{X} + \bar{Y})^2 - (\mu + \nu)^2\right) \Rightarrow N\left(0, \, 4(\mu + \nu)^2 (\sigma^2 + \tau^2)\right)
$$

3) What if $(\mu + \nu)^2 = 0$? Conclusion still holds:
$$
\sqrt{n}(\bar{X} + \bar{Y})^2 \overset{P}{\to} 0
$$
Note $\sqrt{n}\bar{X} + \sqrt{n}\bar{Y} \Rightarrow N(0, \sigma^2 + \tau^2) \qquad (\text{cts mapping})$
$\text{\textbf{not} Slutsky!!}$
So $n(\bar{X} + \bar{Y})^2 \Rightarrow (\sigma^2 + \tau^2)\chi_1^2 \qquad (\text{cts mapping})$
$\text{why not delta method?}$

---

In general, can do higher-order Taylor expansions for delta method if derivatives $= 0$:

$$
f(X_n) \approx \underbrace{f(\mu)}_{O(1)} + \underbrace{\dot{f}(\mu)(X_n - \mu)}_{O_p(n^{-1/2})} + \underbrace{\frac{\ddot{f}(\mu)}{2}(X_n - \mu)^2}_{O_p(n^{-1})} + \cdots
$$

If $\dot{f}(\mu) = 0$, use second-order term:
$$
\begin{aligned}
n(f(X_n) - f(\mu)) &\approx \frac{\ddot{f}(\mu)}{2} (\sqrt{n}(X_n - \mu))^2 \\
&\approx \frac{\ddot{f}(\mu)\sigma^2}{2} \chi_1^2
\end{aligned}
$$

---

[← Convergence](02-convergence.md) · [Up: contents](index.md)
