---
title: 'Source #2: "Objective" or "vague" prior'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture10-bayesinterp.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture10-bayesinterp.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture10-bayesinterp.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture10-bayesinterp.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Source #2: "Objective" or "vague" prior

Using default prior removes subjectivity
(But then what does the posterior mean?)

**Flat prior** $\lambda(\theta) \propto_{\theta} 1$ on $\Theta$
"Indifference" (in $\theta$ parameterization)
Often improper ($\Lambda(\Theta) = \infty$) but usually ok

**Ex:** $\theta \sim \text{flat prior on } \mathbb{R}$
$X \mid \theta \sim \mathcal{N}(\theta, \sigma^2)$
$$
\lambda(\theta \mid X) &\propto_{\theta} p_{\theta}(X) \\
&= \frac{1}{\sqrt{2\pi}} e^{-(X-\theta)^2 / 2\sigma^2} \\
&\propto_{\theta} \mathcal{N}(X, \sigma^2)
$$

**Jeffreys prior** $\lambda(\theta) \propto_{\theta} |J(\theta)|^{1/2}$
Higher density where $P_{\theta}$ "changing faster"
Invariant to parameterization

$(\text{Hw } 5)$
$$
\Lambda([\theta, \theta + \varepsilon]) &\approx \varepsilon \lambda(\theta) \propto \varepsilon \sqrt{J(\theta)} \\
&\approx \sqrt{D_{\text{KL}}(P_{\theta} \parallel P_{\theta+\varepsilon})}
$$

**Ex.** $X \mid \theta \sim \text{Binom}(n, \theta)$
$$
\lambda(\theta) \propto_{\theta} J(\theta)^{1/2} = \left(\frac{n}{\theta(1-\theta)}\right)^{1/2} \propto_{\theta} \text{Beta}\left(\frac{1}{2}, \frac{1}{2}\right)
$$
$\lambda(\theta) \to \infty$ as $\theta \to 0$ or $1$:
$$
\underset{7n \cdot 10^{-3}}{D_{\text{KL}}(0.001 \parallel 0.01)} \gg \underset{2n \cdot 10^{-4}}{D_{\text{KL}}(0.49 \parallel 0.5)} \quad (35\times)
$$

```
   λ(θ)
     \                     /
      \                   /
       \_________________/
     +-------------------+---
     0                   1   θ
```

---

## Intersubjective Agreement

Data may effectively rule out most $\theta$ values
$\rightsquigarrow$ Makes posterior uncontroversial

**Ex.** $X \sim \text{Binom}(10^4, \theta)$, observe $X = 3000$
$$
\text{SD}_{\theta}(X/n) = \sqrt{\frac{\theta(1-\theta)}{n}} \le 0.005
$$
$\Rightarrow \text{Lik}(\theta; X) \approx 0$ outside $C = [0.29, 0.31]$

All "reasonable" priors may be $\approx$ flat on $C$
$$
\Rightarrow \lambda(\theta \mid X) &\approx_{\theta} \text{Lik}(\theta; X) \\
&\approx_{\theta} \exp\left\{ -\frac{J(0.3)}{2} (\theta - 0.3)^2 \right\} \\
&\propto_{\theta} \mathcal{N}(0.3, J(0.3)^{-1})
$$

Data "swamps" everyone's prior

---

## Gaussian sequence model

$X \mid \theta \sim \mathcal{N}_d(\mu, I_d) \qquad \mu \in \mathbb{R}^d$

Jeffreys prior is flat: $\lambda(\mu) \propto_{\mu} 1$
$$
\lambda(\mu \mid X) = \mathcal{N}_d(X, I_d) \implies \mathbb{E}[\mu \mid X] = X \quad \text{Same as UMVU}
$$

What about $\rho^2 = \|\mu\|^2$? Recall
$$
\mu \sim \mathcal{N}_d(X, I_d) \implies \mathbb{E}\left[\|\mu\|^2 \mid X\right] = \|X\|^2 + d
$$

Note $\delta_{\text{umvu}}(X) = \|X\|^2 - d \implies \delta_{\lambda}(X) = \delta_{\text{umvu}}(X) + 2d$
$$
\text{MSE}(\theta; \delta_{\lambda}) &= \text{Var}_{\theta}(\delta_{\lambda}) + \text{Bias}_{\theta}(\delta_{\lambda})^2 \\
&= \text{Var}_{\theta}(\delta_{\text{umvu}}) + 4d^2
$$

**What went wrong?** Examine Jeffreys prior:
$$
\mathbb{P}(\rho^2 \le t) = \text{Vol}(\text{Ball of radius } \sqrt{t}) = \text{const}(d) \cdot t^{d/2}
$$
$\Rightarrow \lambda(\rho^2) \propto_{\rho^2} (\rho^2)^{\frac{d}{2}-1} = \rho^{d-2}$

Grows rapidly! Prior "expects" $\rho^2$ to be huge

---

## Source #3: Prior or concurrent experience

May have many "copies" of same problem
Assume corresp. $\theta$ values drawn from a population
$\rightsquigarrow$ Hierarchical Bayes / empirical Bayes

Can be hard to choose right reference class

**Ex.** Estimate same-side bias for $m = 48$ coin flippers
Flipper $i$ has $n_i$ trials, "true" same-side prob $\theta_i$

Hierarchical model: flippers $i = 1, \dots, m$
"hyperparameters" $\alpha, \beta \sim \lambda \leftarrow \text{"hyperprior"}$
$\theta_i \mid \alpha, \beta \overset{\text{iid}}{\sim} \text{Beta}(\alpha, \beta)$
$X_i \mid \alpha, \beta, \theta \overset{\text{ind.}}{\sim} \text{Binom}(n_i, \theta_i)$

$$
\mathbb{E}[\theta_i \mid X, \alpha, \beta] = \frac{X_i + \alpha}{n_i + \alpha + \beta}
$$

$$
\mathbb{E}[\theta_i \mid X] &= \mathbb{E}\left[\mathbb{E}[\theta_i \mid X, \alpha, \beta] \mid X\right] \\
&= \iint \frac{X_i + \alpha}{n_i + \alpha + \beta} \, \lambda(\alpha, \beta \mid X) \, d\alpha \, d\beta
$$

If $m$ large, $\alpha, \beta$ may be "almost known"
$\rightsquigarrow$ choice of $\lambda$ doesn't matter much

---

## Flexibility of Bayes

Any $\Lambda, \mathcal{P}, L, g(\theta)$: $\delta_{\Lambda}$ defined straightforwardly
$$
\delta_{\Lambda}(X) = \arg\min_d \int L(\theta, d) \, \lambda(\theta \mid X) \, d\theta
$$

Problem reduced to (possibly hard) computation
Posterior is "one stop shop" for all answers

**No need for:**
- special family structure (exp. fam. / complete s.s.)
- special estimator (u-estimable)
- convex or nice $L$

$\Rightarrow$ Highly expressive modeling & estimation

**Caveat:** Limited by ability to do computations
(Topic of next lecture)

### Source #4: Convenience Priors

Choosing conjugate or other "nice" priors
$\rightsquigarrow$ much faster computations esp. in high-dim.
(But what does the posterior mean?)

---

[← Outline](01-outline.md) · [Up: contents](index.md)
