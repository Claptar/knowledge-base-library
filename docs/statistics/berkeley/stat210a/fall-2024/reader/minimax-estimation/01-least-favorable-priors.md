---
title: Least Favorable Priors
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Least Favorable Priors

## Definition of Minimax Risk

The last idea for choosing an estimator: worst-case risk.

Minimize $\sup_\theta R(\theta, \delta)$

The minimum achievable sup risk is called the minimax risk of the estimation problem:

$$r = \inf_\delta \sup_\theta R(\theta, \delta)$$

An estimator $\delta$ is called minimax if it achieves the minimax risk, i.e.,

$$\sup_\theta R(\theta, \delta) = r$$

## Game Theory Interpretation

1. Analyst chooses estimator $\delta$
2. Nature chooses parameter $\theta$ to maximize risk

Note: Nature chooses $\theta$ adversarially, not $X$.

Compare to Bayes where Nature chooses prior from a known distribution (Nature plays a specific mixed strategy).

We will look for Nature's Nash equilibrium strategy.

Minimax is closely related to Bayes.

Key observation: average case risk ≤ worst case risk

For proper prior $\pi$, the Bayes risk is:

$$r(\pi) = \int_\Theta R(\theta, \delta_\pi) d\pi(\theta)$$

$$\leq \int_\Theta \sup_\theta R(\theta, \delta) d\pi(\theta) = \sup_\theta R(\theta, \delta)$$

If $\delta_\pi$ is Bayes, then $r(\pi) = \inf_\delta \int_\Theta R(\theta, \delta) d\pi(\theta)$

Bayes risk of any Bayes estimator lower bounds $r$.

Least favorable prior $\pi$ gives best lower bound: $r(\pi) = \sup_\pi r(\pi)$

Sup risk of any estimator upper bounds $r$:

$$\sup_\theta R(\theta, \delta) \geq r \geq \sup_\pi r(\pi)$$

Can exhibit minimax est. & LF prior by finding $\pi$ and $\delta$ that collapse these inequalities.

## Theorem

If $R(\delta_\pi) = \sup_\theta R(\theta, \delta_\pi)$ with Bayes estimator $\delta_\pi$, then:

a) $\delta_\pi$ is minimax
b) If $\delta_\pi$ is unique Bayes (up to $\pi$-a.e.), it is unique minimax
c) $\pi$ is least favorable

Proof:

a) Any other $\delta$:
   $$\sup_\theta R(\theta, \delta) \geq \int R(\theta, \delta) d\pi(\theta) \geq$$
   $$\int R(\theta, \delta_\pi) d\pi(\theta) = r(\pi) = \sup_\theta R(\theta, \delta_\pi)$$
   $r$ is minimax risk, $\delta_\pi$ is minimax

b) Replace $\geq$ with $=$ in 2nd inequality ⟹ $\delta = \delta_\pi$ $\pi$-a.e.

c) Any other prior $\pi'$:
   $$\inf_\delta r(\pi') \leq \int R(\theta, \delta_\pi) d\pi'(\theta)$$
   $$\leq \sup_\theta R(\theta, \delta_\pi) = r(\pi)$$

The above theorem gives a checkable condition: does avg risk = sup risk?

Note: If $R(\theta, \delta_\pi)$ is constant, it doesn't prove anything.

1. $R(\theta, \delta_\pi)$ is constant
2. Also $R(\theta, \delta_\pi) = \sup_\theta R(\theta, \delta_\pi) = r(\pi)$

## Example: Binomial

$X \sim \text{Binom}(n, \theta)$, estimate $\theta$ with squared error

Try Beta($\alpha, \beta$), hope to get one with constant risk

$$\delta_\pi(X) = \frac{X + \alpha}{n + \alpha + \beta}$$

$$R(\theta, \delta_\pi) = \mathbb{E}[\theta^2] - \mathbb{E}[\delta_\pi(X)^2] + \text{Var}(\delta_\pi(X))$$

$$= \theta - \frac{(\alpha + \beta + n + 1)(\alpha + n\theta)^2}{(\alpha + \beta + n)^2(n + \alpha + \beta + 1)} + \frac{(\alpha + n\theta)(\beta + n(1-\theta))}{(\alpha + \beta + n)^2(n + \alpha + \beta + 1)}$$

Set $\alpha + \beta = n + 2$, $\alpha + \beta = \frac{n}{2}$

$$\beta = \frac{n+2}{2}, \alpha = \frac{n+2}{2}$$

Beta($\frac{n+2}{2}, \frac{n+2}{2}$) is LF, $\delta_\pi$ is minimax

We got lucky.

Question: Why so much prior weight on $\theta \approx \frac{1}{2}$?

---

[Up: contents](index.md) · [Least Favorable Sequence →](02-least-favorable-sequence.md)
