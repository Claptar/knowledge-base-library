---
title: 3 Bayesian Inference
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwo153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwo153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Bayesian Inference

The first step is to select a prior for the unknown parameters $\beta_0, \beta_1, \sigma$. A reasonable prior reflecting ignorance is
$$
\beta_0, \beta_1, \log \sigma \overset{\text{i.i.d}}{\sim} \text{Unif}(-C, C)
$$
for a large number $C$ (the exact value of $C$ will not matter in the following calculations). Note that as $\sigma$ is always positive, we have made the uniform assumption on $\log \sigma$ (by the change of variable formula, the density of $\sigma$ would be given by $f_\sigma(x) = f_{\log \sigma}(\log x) \frac{1}{x} = \frac{I\{-C < \log x < C\}}{2Cx} = \frac{I\{e^{-C} < x < e^C\}}{2Cx}$).

The joint posterior for all the unknown parameters $\beta_0, \beta_1, \sigma$ is then given by (below we write the term "data" for $y_1, \dots, y_n$):
$$
f_{\beta_0, \beta_1, \sigma \mid \text{data}}(\beta_0, \beta_1, \sigma) \propto f_{y_1, \dots, y_n \mid \beta_0, \beta_1, \sigma}(y_1, \dots, y_n) f_{\beta_0, \beta_1, \sigma}(\beta_0, \beta_1, \sigma).
$$

The two terms on the right hand side above are the likelihood:
$$
f_{y_1, \dots, y_n \mid \beta_0, \beta_1, \sigma}(y_1, \dots, y_n) \propto \sigma^{-n} \exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2\right),
$$
and the prior:
$$
\begin{aligned}
f_{\beta_0, \beta_1, \sigma}(\beta_0, \beta_1, \sigma) &= f_{\beta_0}(\beta_0) f_{\beta_1}(\beta_1) f_\sigma(\sigma) \\
&\propto \frac{I\{-C < \beta_0 < C\}}{2C} \frac{I\{-C < \beta_1 < C\}}{2C} \frac{I\{e^{-C} < \sigma < e^C\}}{2C\sigma} \\
&\propto \frac{1}{\sigma} I\{-C < \beta_0, \beta_1, \log \sigma < C\}.
\end{aligned}
$$
We thus obtain
$$
f_{\beta_0, \beta_1, \sigma \mid \text{data}}(\beta_0, \beta_1, \sigma) \propto \sigma^{-n-1}\exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2\right) I\{-C < \beta_0, \beta_1, \log \sigma < C\}.
$$
The above is the joint posterior over $\beta_0, \beta_1, \sigma$. The posterior over only the main parameters $\beta_0, \beta_1$ can be obtained by integrating (or marginalizing) the parameter $\sigma$. We shall do this in the next lecture.

---

[← 2 Frequentist Inference](02-2-frequentist-inference.md) · [Up: contents](index.md)
