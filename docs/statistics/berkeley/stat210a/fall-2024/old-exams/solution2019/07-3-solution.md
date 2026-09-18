---
title: 3. Solution.
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2019.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2019.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3. Solution.

(a) (**Common mistake:** In applying the factorization theorem we need to treat $n$ as an unknown parameter: $n!/(n - N_{11} - N_{10} - N_{01})!$ is not just a function of the data.)

There are four possible outcomes for each reindeer, labeled 00 (undetected twice), 01 (undetected then detected), 10 (detected then undetected), and 11 (detected twice), which occur respectively with probability $p_{00} = (1 - \pi)^2$, $p_{01} = p_{10} = \pi(1 - \pi)$, and $p_{11} = \pi^2$. The counts $N_{00}, N_{01}, N_{10}, N_{11}$ record how many times each outcome happens, so
$$
\begin{aligned}
(N_{00}, N_{01}, N_{10}, N_{11}) &\sim \text{Multinom}(n, ((1 - \pi)^2, \pi(1 - \pi), \pi(1 - \pi), \pi^2)) \\
&= (1 - \pi)^{2N_{00}} \cdot (\pi(1 - \pi))^{N_{10}+N_{01}} \cdot \pi^{2N_{11}} \cdot \frac{n!}{N_{00}! N_{01}! N_{10}! N_{11}!}, \\
&= \left( \frac{\pi}{1 - \pi} \right)^{2N_{11}+N_{10}+N_{01}} \cdot \frac{n!}{(n - N_{11} - N_{01} - N_{10})!} \cdot \frac{1}{N_{01}! N_{10}! N_{11}!},
\end{aligned}
$$
where the first two factors are functions of $T = (N_{11}, N_{01} + N_{10})$ and the parameters $(n, \pi)$ but the last factor is only a function of the data. By the factorization theorem, then, $T$ is sufficient.

(b) If $T$ can be computed from the collection of all likelihood ratios (and if it is also sufficient, as we have just shown it is), then it is minimal sufficient. The likelihood ratio between $(n, \pi)$ and $(\tilde{n}, \tilde{\pi})$ is
$$
\left( \frac{\pi(1 - \tilde{\pi})}{\tilde{\pi}(1 - \pi)} \right)^{2N_{11}+N_{10}+N_{01}} \cdot \frac{n!}{\tilde{n}!} \cdot \frac{(\tilde{n} - N_{11} - N_{10} - N_{01})!}{(n - N_{11} - N_{10} - N_{01})!}
$$
By taking $n = \tilde{n} = N_{11} - N_{10} - N_{01}$ and varying $\pi/\tilde{\pi}$, we can learn $2N_{11} + N_{10} + N_{01}$; whereas by taking $\pi = \tilde{\pi} = 0.5$ and varying $n$ and $\tilde{n}$, we can learn $N_{11} + N_{11} + N_{10} + N_{01}$; knowing both of these is equivalent to knowing $T$.

(c) Note that $N_{ij}/n \to p_{ij}$ by LLN, since it is an average of $n$ i.i.d. $\text{Bern}(p_{ij})$ random variables which have finite expectation. Dividing by $n^2$ in the numerator and $n$ in the denominator and applying the continuous map-

---

ping theorem, we get
$$
\begin{aligned}
\frac{\hat{n}}{n} &= \frac{(N_{01}/n + N_{10}/n + 2N_{11}/n)^2}{4N_{11}/n} \\
&\overset{p}{\to} \frac{(2p_{01} + 2p_{11})^2}{4p_{11}} \quad \text{(continuous since } p_{11} > 0) \\
&= (2\pi(1 - \pi) + 2\pi^2)^2 / 4\pi^2 = 1.
\end{aligned}
$$

(d) By grouping together the outcomes 01 and 10 we can get a reduced multinomial
$$
(N_{00}, N_{10} + N_{01}, N_{11}) \sim \text{Multinom}(n, (p_{00}, 2p_{01}, p_{11})),
$$
which is also a sum of $n$ i.i.d. $\text{Multinom}(1, (p_{00}, 2p_{01}, p_{11}))$ random variables which have finite variance. Restricting attention to the two entries we actually observe and then applying the CLT gives
$$
\frac{1}{\sqrt{n}} \left( \begin{pmatrix} N_{10} + N_{01} \\ N_{11} \end{pmatrix} - \begin{pmatrix} 2np_{01} \\ np_{11} \end{pmatrix} \right) \Rightarrow N_2(0, \Sigma)
$$
where
$$
\Sigma = \begin{pmatrix} 2p_{01}(1 - 2p_{01}) & -2p_{01}p_{11} \\ -2p_{01}p_{11} & p_{11}(1 - p_{11}) \end{pmatrix} = \begin{pmatrix} 2\pi(1 - \pi)(1 - 2\pi(1 - \pi)) & -2\pi(1 - \pi)\pi^2 \\ -2\pi(1 - \pi)\pi^2 & \pi^2(1 - \pi^2) \end{pmatrix}
$$
We will apply delta method to the function $f(t_1, t_2) = (t_1 + 2t_2)^2 / 4t_2$:
$$
\nabla f(t_1, t_2) = \left( 1 + \frac{t_1}{2t_2}, \; 1 - \frac{t_1^2}{4t_2^2} \right).
$$
Applying the delta method to $f\left( \frac{N_{10} + N_{01}}{n}, \frac{N_{11}}{n} \right)$ gives
$$
\sqrt{n} \left( \frac{\hat{n}}{n} - 1 \right) = \sqrt{n} \left( f\left( \frac{N_{10} + N_{01}}{n}, \frac{N_{11}}{n} \right) - f(2p_{10}, p_{11}) \right) \Rightarrow N(0, \sigma^2),
$$
where $\sigma^2 = \nabla f(2p_{10}, p_{11})' \Sigma \nabla f(2p_{10}, p_{11})$. After a lot of algebra we can simplify $\sigma^2 = (1 - \pi)^2/\pi^2$, but we would award full credit for the unsimplified form as described above.

---

---

[← 3. "And if you ever saw it..." (24 points, 6 points / part).](06-3-and-if-you-ever-saw-it-24-points-6-points-part.md) · [Up: contents](index.md) · [4. Nonlinear regression (24 points, 6 points / part). →](08-4-nonlinear-regression-24-points-6-points-part.md)
