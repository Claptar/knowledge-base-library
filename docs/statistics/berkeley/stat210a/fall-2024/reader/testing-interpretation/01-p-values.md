---
title: p-Values
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# p-Values

**Source:** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Informal Definition

Suppose $\phi(x)$ rejects for $T(x) > c$. The p-value is:

$$p(x) = \mathbb{P}_0(T(X) \geq T(x)_{\text{observed}}) = \mathbb{P}_0(T(X) \geq t)$$

Example: $X \sim N(\theta, 1)$, $H_0: \theta = 0$ vs $H_1: \theta \neq 0$

Two-sided test rejects for large $|T(X)| = |X|$:

$$p(x) = \mathbb{P}_0(|X| \geq |x|) = 2(1 - \Phi(|x|))$$

The two-sided p-value is $p(X)$, where:

$$p(x) = \mathbb{P}_0(|X| \geq |x|) = 2\min\{\Phi(x), 1-\Phi(x)\}$$

### Formal Definition

Assume we have a test $\phi_\alpha$ for each significance level $\alpha$: $\mathbb{E}_0[\phi_\alpha(X)] \leq \alpha$

In the non-randomized case: $\phi_\alpha(x) = 1\{x \in R_\alpha\}$

Assume tests are monotone in $\alpha$: if $\alpha \leq \alpha'$, then $\phi_\alpha(x) \leq \phi_{\alpha'}(x)$

(In non-randomized case: $R_\alpha \subseteq R_{\alpha'}$)

Then:

$$p(x) = \inf\{\alpha \in [0,1]: \phi_\alpha(x) = 1\} = \inf\{\alpha: x \in R_\alpha\}$$

It's possible to define randomized p-value, but not worth it.

Note: $p(x) \leq \alpha \iff \phi_\alpha(x) = 1$

For $\theta = \theta_0$: $\mathbb{P}_0(p(X) \leq \alpha) = \mathbb{E}_0[\phi_\alpha(X)] \leq \alpha$

p-value stochastically dominates $U(0,1)$

If $\phi_\alpha$ rejects for large $T(X)$, reduces to original definition.

Note: The p-value depends on:
- The model
- Null hypothesis
- The data AND
- The choice of test

Example: $X \sim N(\theta, I_d)$, $H_0: \theta = 0$ vs $H_1: \theta \neq 0$

We can use $T(x) = \|x\|_2^2$ ($\chi^2$ test)
or $T(x) = \max_i |x_i|$ (max test)

Very different p-values, power if $d$ large
Choice reflects belief about whether $\theta$ is sparse

### Accept/Reject Decisions

Accept/reject decisions are not interesting
Usually, we care how big $\theta$ is
Tiny p-value doesn't imply big $\theta$
Big p-value doesn't imply small $\theta$ either

---

[Up: contents](index.md) · [Confidence Regions →](02-confidence-regions.md)
