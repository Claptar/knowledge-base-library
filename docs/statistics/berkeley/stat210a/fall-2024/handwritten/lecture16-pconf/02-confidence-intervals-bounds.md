---
title: Confidence Intervals / Bounds
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture16-pconf.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture16-pconf.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture16-pconf.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture16-pconf.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Confidence Intervals / Bounds

If $C(X) = [C_1(X), C_2(X)]$ we say $C(X)$ is a **confidence interval** (**CI**)

$C(X) = [C_1(X), \infty)$: **lower conf. bd.** (**LCB**)

$C(X) = (-\infty, C_2(X)]$: **upper conf bd.** (**UCB**)

We usually get LCB / UCB by inverting a one-sided test in appropriate direction
Called **uniformly most accurate** (**UMA**) if test UMP

Get CI by inverting a two-sided test
Called **UMAU** if test is UMPU

---

**Ex** $X \sim \text{Exp}(\theta) = \frac{1}{\theta} e^{-x/\theta} \qquad x > 0, \, \theta > 0$

CDF $\mathbb{P}_\theta(X \le x) = 1 - e^{-x/\theta}$

**LCB:** Invert test for $H_0: \theta \le \theta_0$

Solve $\alpha = \mathbb{P}_{\theta_0}(X > c(\theta_0)) = e^{-c(\theta_0)/\theta_0}$
$c(\theta_0) = \theta_0 \log(1/\alpha) \ (> 0)$
$X \le c(\theta_0) \implies \theta_0 \ge \frac{X}{-\log \alpha}$
$C(X) = \left[\frac{X}{-\log \alpha}, \, \infty\right)$

**UCB:** Similar, $C(X) = \left(-\infty, \, \frac{X}{-\log(1-\alpha)}\right]$

**Equal-tailed CI:**
Invert equal-tailed test of $H_0: \theta = \theta_0$

$$
\phi_\alpha^{\text{ET}}(X) = \phi_{\alpha/2}^{\ge \theta_0}(X) + \phi_{\alpha/2}^{\le \theta_0}(X)
$$
*(where $\phi_\alpha^{\text{ET}}$ is equal-tailed for $H_0: \theta = \theta_0$, $\phi_{\alpha/2}^{\ge \theta_0}$ is for $H_0: \theta \ge \theta_0$, and $\phi_{\alpha/2}^{\le \theta_0}$ is for $H_0: \theta \le \theta_0$)*

$$
\begin{aligned}
\implies C(X) &= \left[\frac{X}{-\log^{\alpha/2}}, \, \infty\right) \cap \left(-\infty, \, \frac{X}{-\log(1-\alpha/2)}\right] \\
&= \left[\frac{X}{-\log^{\alpha/2}}, \, \frac{X}{-\log(1-\alpha/2)}\right]
\end{aligned}
$$

Similar for UMPU 2-sided test

---

## (Mis-)Interpreting Hypothesis Tests

Hypothesis tests ubiquitous in science

Common misinterpretations:

1) $p < 0.05 \implies$ therefore ``there is an effect''
   or ``the effect size = the estimate''

2) $p > 0.05 \implies$ therefore ``there is no effect''

3) $p = 10^{-6} \implies$ therefore ``the effect is huge''

4) $p = 10^{-6} \implies$ therefore ``the data are signif.''
   and everything about our model is correct in most naive interp.

5) Effect CI for men is $[0.2, \, 3.2]$,
   for women is $[-0.2, \, 2.8]$ therefore
   ``there is an effect for men and not for women.''

Dichotomous test doesn't eliminate uncertainty
(CIs usually less misleading to novices)

---

## How to interpret testing

Learning about the world from data is not easy or automatic!

Hypothesis tests let us ask specific questions about specific data sets under specific modeling assumptions, using specific testing method.
All of these choices bear on the interpretation.

Top-tier medical journals let people publish claims, reporting $p$-values without saying what model was used or what test was employed.
**Pretty bad when you think about it!**

Hyp. tests can be a good companion to critical thinking, **never** a substitute.
``All models are wrong, some are useful'' but need experience and theory to understand when assumptions do or don't cause real trouble.

---

## Conceptual Objections

**Q1:** Why should I test $H_0: \theta = 0$? No $\theta$ is ever exactly 0.

**A1:**
a) Test $H_0: |\theta| \le \delta$ if you want.
If $\text{s.e.}(\hat{\theta}) \gg \delta$, not much difference.

b) Most two-sided tests justify directional inference:
``If $T > c_\alpha$ declare $\theta > 0$, if $T < c_\alpha$ declare $\theta < 0$'' with $\mathbb{P}(\text{false claim}) \le \alpha$

c) Harder to answer in non-parametric problems, e.g. $H_0: P = Q$ vs $H_1: P \ne Q$ for perm. test, but alternative frameworks like Bayes force very strong assumptions on us.

**Q2:** People only like frequentist results like $p$-values, CIs because they mistake them for Bayesian results.
95% chance $C(X) \ni \theta$ is misinterpreted as a claim about $p(\theta \mid X)$.

**A2:** True, but subjective Bayesian results often misinterpreted as ``the posterior dist. of $\theta$'' when really should be ``**my** posterior opinion about $\theta$''.

---

[← Formal definition: $\mathcal{P}$, $\Theta0$, $\Theta1$](01-formal-definition.md) · [Up: contents](index.md)
