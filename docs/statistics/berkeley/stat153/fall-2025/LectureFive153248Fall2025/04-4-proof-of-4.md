---
title: 4 Proof of (4)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Proof of (4)

*Proof of (4).* Start with the formula:

$$
f_T(y) = \int_0^\infty f_{T \mid V=x}(y) f_V(x) dx.
$$

Observe that

$$
T \mid V = x \sim N\left(\mu, \frac{\nu}{x}\Sigma\right)
$$

so that

$$
\begin{aligned}
f_{T \mid V=x}(y) &= \frac{1}{(2\pi)^{p/2}\sqrt{\det(\frac{\nu}{x}\Sigma)}} \exp \left[ -\frac{1}{2}(y - \mu)^T \left(\frac{\nu}{x}\Sigma\right)^{-1} (y - \mu) \right] \\
&= \frac{x^{p/2}}{(2\pi)^{p/2}\nu^{p/2}\sqrt{\det(\Sigma)}} \exp \left( -\frac{x}{2\nu}(y - \mu)^T \Sigma^{-1}(y - \mu) \right)
\end{aligned}
$$

where we used $\det(\frac{\nu}{x}\Sigma) = (\nu/x)^p \det(\Sigma)$. As a result

$$
\begin{aligned}
f_T(y) &= \int_0^\infty f_{T \mid V=x}(y) f_V(x) dx \\
&\propto \int_0^\infty \frac{x^{p/2}}{(2\pi)^{p/2}\nu^{p/2}\sqrt{\det(\Sigma)}} \exp \left( -\frac{x}{2\nu}(y - \mu)^T \Sigma^{-1}(y - \mu) \right) x^{\frac{\nu}{2}-1} e^{-x/2} dx \\
&\propto \int_0^\infty x^{\frac{p+\nu}{2}-1} \exp \left( -\frac{x}{2} \left[ 1 + \frac{1}{\nu}(y - \mu)^T \Sigma^{-1}(y - \mu) \right] \right) dx.
\end{aligned}
$$

The change of variable

$$
t = x \left[ 1 + \frac{1}{\nu}(y - \mu)^T \Sigma^{-1}(y - \mu) \right]
$$

leads to

$$
\begin{aligned}
f_T(y) &\propto \frac{1}{\left[ 1 + \frac{1}{\nu}(y - \mu)^T \Sigma^{-1}(y - \mu) \right]^{\frac{\nu+p}{2}}} \int_0^\infty t^{\frac{\nu+p}{2}-1} e^{-t/2} dt \\
&\propto \frac{1}{\left[ 1 + \frac{1}{\nu}(y - \mu)^T \Sigma^{-1}(y - \mu) \right]^{\frac{\nu+p}{2}}}.
\end{aligned}
$$

which proves (4). $\square$

---

[← 3 Back to Regression](03-3-back-to-regression.md) · [Up: contents](index.md) · [5 Nonlinear Regression →](05-5-nonlinear-regression.md)
