---
title: 'Formal definition: $\mathcal{P}$, $\Theta0$, $\Theta1$'
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture16-pconf.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture16-pconf.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture16-pconf.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture16-pconf.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Formal definition: $\mathcal{P}$, $\Theta0$, $\Theta1$

### Outline

1) $p$-Values
2) Confidence regions
3) (Mis-)interpreting tests

---

## $p$-Values

Informal definition: Suppose $\phi(x)$ rejects for large values of $T(X)$.

$$
p(x) &= \text{``Null probability that $T(X)$ is as large or larger than what we observed''} \\
&= \text{``}\mathbb{P}_{H_0}(T(X) \ge T(x))\text{''} \\
&= \sup_{\theta \in \Theta_0} \mathbb{P}_\theta(T(X) \ge T(x))
$$

<!-- Drawing of a null distribution curve with the tail area past T(x) labeled as "p-value" and T(x) marked as "(observed)" -->

**Ex** $X \sim \text{Binom}(n, \theta) \quad H_0: \theta \le 0.5 \quad \text{vs} \quad H_1: \theta > 0.5$

One-sided test rejects for large $X$

$$
p(x) = \mathbb{P}_{0.5}(X \ge x) = \sup_{\theta \le 0.5} \mathbb{P}_\theta(X \ge x)
$$

**Ex** $X \sim N(\theta, 1) \quad H_0: \theta = 0 \quad \text{vs.} \quad H_1: \theta \ne 0$

Two-sided test rejects for large $T(X) = |X|$

$$
(\iff \phi(x) = \mathbf{1}\{|X| > z_{\alpha/2}\})
$$

The two-sided $p$-value is $p(x)$ where

$$
p(x) &= \mathbb{P}_0(|X| > |x|) \\
&= 2(1 - \Phi(|x|))
$$

---

## Formal definition: $\mathcal{P}$, $\Theta_0$, $\Theta_1$

Assume we have a test $\phi_\alpha$ for each significance level, $\sup_{\theta \in \Theta_0} \mathbb{E}_\theta \phi_\alpha(X) \le \alpha$

(Non-randomized case: $\phi_\alpha = \mathbf{1}\{x \in R_\alpha\}$)

Assume tests are monotone in $\alpha$:
if $\alpha_1 \le \alpha_2$ then $\phi_{\alpha_1}(x) \le \phi_{\alpha_2}(x)$
(non-randomized: $R_{\alpha_1} \subseteq R_{\alpha_2}$)

Then

$$
p(x) &= \sup\{\alpha: \phi_\alpha(x) < 1\} \\
(&= \sup\{\alpha: x \notin R_\alpha\})
$$

(can define randomized $p$-value but not worth it)

For $\theta \in \Theta_0$,

$$
\mathbb{P}_\theta(p(X) \le \alpha) &= \mathbb{P}_\theta(\sup\{\tilde{\alpha}: \phi_{\tilde{\alpha}}(X) < 1\} \le \alpha) \quad \left[\text{Note: } \inf_{\tilde{\alpha} > \alpha} \mathbb{P}_\theta(\phi_{\tilde{\alpha}}(X) = 1) \le \alpha\right] \\
&\le \lim_{\varepsilon \downarrow 0} \mathbb{P}_\theta(\phi_{\alpha+\varepsilon}(X) = 1) \\
&\le \lim_{\varepsilon \downarrow 0} \alpha + \varepsilon = \alpha
$$

$\implies$ $p$-value **stochastically dominates** $\mathcal{U}[0, 1]$

If $\phi_\alpha$ rejects for large $T(X)$, reduces to original definition.

---

Note the $p$-value is defined relative to
- the model & null hyp.,
- the data, AND
- the choice of test

**Ex** $X \sim \text{Exp}(\theta) \quad H_0: \theta = 1 \quad \text{vs} \quad H_1: \theta \ne 1$

We can use equal-tailed test
or UMPU test

For $X > 1$:
Equal-tailed: $p(x) = 2 \cdot \mathbb{P}_1(X \ge x) = 2e^{-x}$
UMPU: $p(x) = \alpha$ for which $c_2(\alpha) = x$

**Ex** $X \sim N_d(\theta, I_d) \quad H_0: \theta = 0 \quad \text{vs} \quad H_1: \theta \ne 0$

We can use
$$
T_1(X) = \|X\|^2 \quad (\chi^2 \text{ test})
$$
or
$$
T_2(X) = \|X\|_\infty = \max_i |X_i| \quad (\text{max test})
$$

Very different $p$-values / power if $d$ large
(choice reflects belief about whether $\theta$ is sparse)

---

## Confidence Sets

[Accept/reject decision only so interesting:
- usually we care how big $\theta$ is
- tiny $p$-value doesn't imply big $\theta$
(big $p$-value doesn't imply small $\theta$ either)]

**Def** $\mathcal{P} = \{\mathbb{P}_\theta : \theta \in \Theta\}$

$C(X)$ is a $1-\alpha$ confidence set for $g(\theta)$ if

$$
\mathbb{P}_\theta(C(X) \ni g(\theta)) \ge 1-\alpha, \quad \forall \theta \in \Theta
$$
*(where $C(X)$ is subject, $\ni$ is verb, $g(\theta)$ is object)*

We say $C(X)$ **covers** $g(\theta)$ if $C(X) \ni g(\theta)$
$\mathbb{P}_\theta(C(X) \ni g(\theta))$ is **coverage probability**
$\inf_\theta \mathbb{P}_\theta(C \ni g(\theta))$ is **conf. level**

**Notes**
- $C(X)$ is random, not $g(\theta)$
- Often misinterpreted as Bayesian guarantee
- Say ``$C(X)$ has a 95% chance of covering''
  NOT ``$g(\theta)$ has a 95% chance of being in $C$''
  NEVER ``95% chance $g(\theta) \in [0.5, 1.5]$'' (e.g.)

---

## Duality of Testing & Confidence Sets

Suppose we have a level-$\alpha$ test $\phi(x; a)$ of $H_0: g(\theta) = a$ vs. $H_1: g(\theta) \ne a$, $\forall a \in g(\Theta)$

We can use it to make a confidence set for $g(\theta)$:

Let
$$
C(X) &= \{a: \phi(X; a) < 1\} \\
&= \text{``all non-rejected values of $\theta$''}
$$

Then
$$
\mathbb{P}_\theta(C(X) \not\ni g(\theta)) = \mathbb{P}_\theta(\phi(X; g(\theta)) = 1) \le \alpha \quad \forall \theta
$$

Alternatively, suppose $C(X)$ is a $1-\alpha$ confidence set for $g(\theta)$.

We can use $C$ to construct a test $\phi(X)$ of
$$
H_0: g(\theta) = a \quad \text{vs.} \quad H_1: g(\theta) \ne a
$$

$$
\phi(X) = \mathbf{1}\{a \notin C(X)\}
$$

For $\theta$ s.t. $g(\theta) = a$:
$$
\mathbb{E}_\theta \phi(X) = \mathbb{P}_\theta(C(X) \not\ni g(\theta)) \le \alpha
$$

This is called **inverting the test**

---

## Confidence interval for median

Nonparametric model $X_1, \dots, X_n \overset{iid}{\sim} F$, $F$ any cdf
$g(F) = \text{median}(F) = F^{-1}(1/2)$ (assume well-defined)

Two-sided sign test:
$$
H_0: g(F) = \mu \iff F(\mu) = 1/2
$$
vs
$$
H_1: g(F) \ne \mu \iff F(\mu) \ne 1/2
$$

$$
S(X; \mu) = #\{X_i > \mu\} \sim \text{Binom}(n, 1 - F(\mu)) = 1/2 \text{ iff } H_0 \text{ true}
$$

Reject for $T(X; \mu) = |S(X; \mu) - n/2| > c_\alpha$ *(no dependence on $\mu$)*
e.g. $n = 100$, $c_\alpha = 5$, reject if $S(X) > 55$

$$
\mu \in C(X) &\iff |S(X; \mu) - n/2| \le c_\alpha \\
&\iff #\{X_i > \mu\} \in [n/2 - c_\alpha, \, n/2 + c_\alpha] \\
&\iff \mu \in \left[X_{(n/2 - c_\alpha)}, \, X_{(n/2 + c_\alpha)}\right]
$$

---

---

[Up: contents](index.md) · [Confidence Intervals / Bounds →](02-confidence-intervals-bounds.md)
