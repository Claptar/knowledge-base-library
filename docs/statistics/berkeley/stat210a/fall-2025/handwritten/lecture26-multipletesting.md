---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture26-multipletesting.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture26-multipletesting.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture26-multipletesting.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture26-multipletesting.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Multiple Testing
2) Familywise error rate control
3) Stepdown multiple testing
4) Simultaneous intervals / deduced inference
5) False Discovery Rate control
6) Benjamini-Hochberg Procedure

---

## Multiple Testing

In many testing problems, we want to test many hypotheses at a time, e.g.

- Test $H_{0j}: \beta_j = 0$ for $j=1,\dots,d$ in linear regression

- Test whether each of 2M single nucleotide polymorphisms (SNPs) is associated with a given phenotype (e.g., diabetes / schizophrenia)

- Test whether each of 2000 web site tweaks affects user engagement

**Setup**: $X \sim P_\theta \in \mathcal{P} \qquad H_{0i}: \theta \in \Theta_{0i}, \quad i=1,\dots,m$
(Commonly, $H_{0i}: \theta_i = 0$)

**Goal**: Return accept/reject decision for each $i$.

Let $\mathcal{R}(X) = \{i : H_{0i} \text{ rejected}\} \subseteq \{1, \dots, m\}$
$\mathcal{H}_0(\theta) = \{i : H_{0i} \text{ true}\}$
$R(X) = |\mathcal{R}(X)|, \quad m_0 = |\mathcal{H}_0|$

---

## Familywise Error Rate

**Problem**: Even if all $H_{0i}$ true, might have
$$\mathbb{P}(\text{any } H_{0i} \text{ rejected}) \gg \alpha$$

**Ex** $X_i \stackrel{\text{ind.}}{\sim} \mathcal{N}(\theta_i, 1) \quad i=1,\dots,m. \quad H_{0i}: \theta_i = 0$
$$\mathbb{P}_\theta(\text{any } H_{0i} \text{ rejected}) = 1 - (1-\alpha)^{m_0} \to 1$$

Is this a problem? Yes, if all attention will be focused on the (false) rejections and none on the (correct) non-rejections.

Classical solution is to control the **familywise error rate** (FWER):
$$\begin{aligned}
\text{FWER}_\theta &= \mathbb{P}_\theta(\text{any false rejections}) \\
&= \mathbb{P}_\theta(\mathcal{R} \cap \mathcal{H}_0 \neq \emptyset)
\end{aligned}$$

Want $\sup_{\theta \in \Theta} \text{FWER}_\theta \le \alpha$

Typically achieved by "correcting" marginal $p$-values $p_1(X), \dots, p_m(X)$ $\quad \left(p_i \stackrel{H_{0i}}{\ge} \mathcal{U}[0,1]\right)$
e.g., $p_i(X) = 2(1 - \Phi(|X_i|))$ for Gaussian

---

## Bonferroni Correction

Assume $p_1, \dots, p_m$ are $p$-values for $H_{0,1}, \dots, H_{0m}$ with $p_i \ge \mathcal{U}[0,1]$ under $H_{0i}$

For general dependence, can guarantee control by rejecting $H_{0i}$ iff $p_i \le \alpha / m$:

$$\begin{aligned}
\mathbb{P}_\theta(\text{any false rejections}) &= \mathbb{P}_\theta\left(\bigcup_{i \in \mathcal{H}_0} \{H_{0i} \text{ rejected}\}\right) \\
&\le \sum_{i \in \mathcal{H}_0} \mathbb{P}_\theta(H_{0i} \text{ rejected}) \\
&\le m_0 \cdot \alpha/m \le \alpha
\end{aligned}$$

If $p$-values independent, can improve to $\tilde{\alpha}_m = 1 - (1-\alpha)^{1/m}$ (Šidák correction)

Then $\mathbb{P}_\theta(\text{no false rejections})$
\$\$\begin{aligned}
&= \prod_{i \in \mathcal{H}_0} \mathbb{P}_\theta(p_i > \tilde{\alpha}_m)

---

[Up: contents](../index.md)
