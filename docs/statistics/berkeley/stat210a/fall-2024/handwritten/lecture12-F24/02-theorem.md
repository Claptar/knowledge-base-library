---
title: Theorem
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture12-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture12-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Theorem

If $r_\Lambda = \sup_\theta R(\theta; \delta_\Lambda)$ with Bayes estimator $\delta_\Lambda$ then:

(a) $\delta_\Lambda$ is minimax

(b) If $\delta_\Lambda$ is unique Bayes (up to $\overset{\text{a.s.}}{=}$) for $\Lambda$, it is unique minimax

(c) $\Lambda$ is least fav.

**Proof**

a) Any other $\tilde{\delta}$:

$$\begin{aligned}
\sup_\theta R(\theta; \tilde{\delta}) &\ge \int R(\theta; \tilde{\delta}) \, d\Lambda(\theta) \\
&\ge \int R(\theta; \delta_\Lambda) \, d\Lambda(\theta) \qquad (*) \\
&= r_\Lambda \\
&= \sup_\theta R(\theta; \delta_\Lambda) \quad \text{by assumption}
\end{aligned}$$

$\Rightarrow r_\Lambda$ is minimax risk, $\delta_\Lambda$ is minimax.

b) Replace "$\ge$" with "$>$" in $2^{\text{nd}}$ ineq. $(*)$

c) Any other prior $\tilde{\Lambda}$:

$$\begin{aligned}
r_{\tilde{\Lambda}} &= \inf_\delta \int R(\theta; \delta) \, d\tilde{\Lambda}(\theta) \\
&\le \int R(\theta; \delta_\Lambda) \, d\tilde{\Lambda}(\theta) \\
&\le \sup_\theta R(\theta; \delta_\Lambda) = r_\Lambda \qquad \blacksquare
\end{aligned}$$

---

The above theorem gives a checkable condition:
does avg risk = sup risk?

mistake on final: saying $r_\Lambda$ is const. doesn't prove anything

True if:
1) $R(\theta; \delta_\Lambda)$ is constant
2) $\Lambda(\{\theta: R(\theta; \delta_\Lambda) = \max_\zeta R(\zeta; \delta_\Lambda)\}) = 1$

```
 R(θ; δ_Λ)
    ^
    |      +-----------------------+
    |     /                         \
    |----+                           +----
    |    |                           |
    +----+---------------------------+-----> θ
         |                           |
         |                           |
    λ(θ) |                           |
    ^    |                           |
    |    |  _.-'-._                  |
    |    .-'       `'-._             |
    |   /               `'-._        |
    |  /                     `'-._   |
    +-+---------------------------+--+-----> θ
      |<-------- supp(Λ) -------->|
```

---

---

[← Minimax Estimation](01-minimax-estimation.md) · [Up: contents](index.md) · [Example (Binomial) →](03-example-binomial.md)
