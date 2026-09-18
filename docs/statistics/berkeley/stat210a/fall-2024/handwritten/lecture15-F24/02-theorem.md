---
title: Theorem
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture15-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture15-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture15-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture15-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Theorem

Assume $X_i \overset{\text{iid}}{\sim} e^{\theta T(x) - A(\eta)} h(x)$

$$H_0: \theta \in [\theta_1, \theta_2] \quad\text{vs}\quad H_1: \theta < \theta_1 \text{ or } \theta > \theta_2$$
$$\text{(possibly } \theta_1 = \theta_2\text{)}$$

Then
a) The unbiased test **based on** (rejecting for extreme values of) $\sum T(X_i)$ with sig. $\text{level} = \alpha$ is UMP among all unbiased tests (UMPU)

b) If $\theta_1 < \theta_2$ the UMPU test can be found by solving for $c_i, \gamma_i$ s.t.
$$\mathbb{E}_{\theta_1}\phi = \mathbb{E}_{\theta_2}\phi = \alpha$$

c) If $\theta_1 = \theta_2 = \theta_0$ the UMPU test can be found by solving for $c_i, \gamma_i$ s.t.
$$\mathbb{E}_{\theta_0}\phi(X) = \alpha \quad\text{and}$$
$$\frac{d\beta_\phi}{d\theta}(\theta_0) = \mathbb{E}_{\theta_0}\left[(\sum T(X_i))(\phi(X) - \alpha)\right] = 0$$

(Proof in Keener)

---

$$\frac{d^2}{d\eta^2} \int e^{\eta T(x) - A(\eta)} \phi(x) d\mu(x)$$

$$= \frac{d}{d\eta} \int (T - A'(\eta)) p_\eta \, \phi \, d\mu$$

$$= \int \left[(T - A'(\eta))^2 - A''(\eta)\right] p_\eta \phi d\mu$$

$$\max \quad \int \phi \, p_2 \, d\mu - \lambda_0 \int \phi \, p_0 \, d\mu - \lambda_1 \int (T - \mathbb{E}_0 T) \phi \, p_0 \, d\mu$$

$$\int \phi \left( p_2 - \lambda_0 p_0 - \lambda_1(T - \mathbb{E}_0 T) p_0 \right) d\mu$$

$$= \int \phi \left( \frac{p_2}{p_0} - \lambda_0 - \lambda_1(T - \mathbb{E}_0 T) \right) d\mu$$

$$=$$

---

[← One-sided tests in general](01-one-sided-tests-in-general.md) · [Up: contents](index.md)
