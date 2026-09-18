---
title: 1 p-Values
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 p-Values

Published

October 17, 2023

$$
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cP}{\mathcal{P}}
\newcommand{\cX}{\mathcal{X}}
\newcommand{\EE}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\td}{\,\textrm{d}}
\newcommand{\simiid}{\stackrel{\textrm{i.i.d.}}{\sim}}
\newcommand{\simind}{\stackrel{\textrm{ind.}}{\sim}}
\newcommand{\eqas}{\stackrel{\textrm{a.s.}}{=}}
\newcommand{\eqPas}{\stackrel{\cP\textrm{-a.s.}}{=}}
\newcommand{\eqmuas}{\stackrel{\mu\textrm{-a.s.}}{=}}
\newcommand{\eqD}{\stackrel{D}{=}}
\newcommand{\indep}{\perp\!\!\!\!\perp}
\DeclareMathOperator*{\minz}{minimize\;}
\DeclareMathOperator*{\maxz}{minimize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
$$

## 1 p-Values {.anchored number="1" anchor-id="p-values"}

### 1.1 Informal Definition {.anchored number="1.1" anchor-id="informal-definition"}

Suppose $\phi(x)$ rejects for $T(x) > c$. The p-value is:

$$
p(x) = \mathbb{P}_0(T(X) \geq T(x)_{\text{observed}}) = \mathbb{P}_0(T(X) \geq t)
$$

Example: $X \sim N(\theta, 1)$, $H_0: \theta = 0$ vs $H_1: \theta \neq 0$

Two-sided test rejects for large $|T(X)| = |X|$:

$$
p(x) = \mathbb{P}_0(|X| \geq |x|) = 2(1 - \Phi(|x|))
$$

The two-sided p-value is $p(X)$, where:

$$
p(x) = \mathbb{P}_0(|X| \geq |x|) = 2\min\{\Phi(x), 1-\Phi(x)\}
$$

### 1.2 Formal Definition {.anchored number="1.2" anchor-id="formal-definition"}

Assume we have a test $\phi_\alpha$ for each significance level $\alpha$: $\mathbb{E}_0[\phi_\alpha(X)] \leq \alpha$

In the non-randomized case: $\phi_\alpha(x) = 1\{x \in R_\alpha\}$

Assume tests are monotone in $\alpha$: if $\alpha \leq \alpha'$, then $\phi_\alpha(x) \leq \phi_{\alpha'}(x)$

(In non-randomized case: $R_\alpha \subseteq R_{\alpha'}$)

Then:

$$
p(x) = \inf\{\alpha \in [0,1]: \phi_\alpha(x) = 1\} = \inf\{\alpha: x \in R_\alpha\}
$$

It’s possible to define randomized p-value, but not worth it.

Note: $p(x) \leq \alpha \iff \phi_\alpha(x) = 1$

For $\theta = \theta_0$: $\mathbb{P}_0(p(X) \leq \alpha) = \mathbb{E}_0[\phi_\alpha(X)] \leq \alpha$

p-value stochastically dominates $U(0,1)$

If $\phi_\alpha$ rejects for large $T(X)$, reduces to original definition.

Note: The p-value depends on: - The model - Null hypothesis - The data AND - The choice of test

Example: $X \sim N(\theta, I_d)$, $H_0: \theta = 0$ vs $H_1: \theta \neq 0$

We can use $T(x) = \|x\|_2^2$ ($\chi^2$ test) or $T(x) = \max_i |x_i|$ (max test)

Very different p-values, power if $d$ large Choice reflects belief about whether $\theta$ is sparse

### 1.3 Accept/Reject Decisions {.anchored number="1.3" anchor-id="acceptreject-decisions"}

Accept/reject decisions are not interesting Usually, we care how big $\theta$ is Tiny p-value doesn’t imply big $\theta$ Big p-value doesn’t imply small $\theta$ either

---

[Up: contents](index.md) · [2 Confidence Regions →](02-2-confidence-regions.md)
