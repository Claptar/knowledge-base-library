---
title: Theorem (Consistency of MLE for compact $\Theta$)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture22-mle-consistency.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture22-mle-consistency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture22-mle-consistency.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture22-mle-consistency.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Theorem (Consistency of MLE for compact $\Theta$)

$$X_1, \ldots, X_n \overset{\text{iid}}{\sim} P_{\theta_0}, \quad \mathcal{P} \text{ has densities } p_\theta, \quad \theta \in \Theta$$

Assume
- $\log p_\theta(x)$ cts in $\theta$, all $x \in \mathcal{X}$
- $\Theta$ compact
- $\mathbb{E}_{\theta_0} \left[\sup_{\theta \in \Theta} |W_1(\theta)|\right] < \infty \qquad \mathbb{E}_{\theta_0} \sup_{\theta} |l(\theta; X_i) - l(\theta_0; X_i)|$
- Model identifiable

Then $\hat{\theta}_n \overset{P}{\to} \theta_0$ if $\hat{\theta}_n \in \operatorname{argmax} l_n(\theta; X)$

**Proof** $W_i \in C(\Theta)$ iid, mean $\mu(\theta) = -D_{\text{KL}}(\theta_0 \,\|\, \theta)$

$\mu(\theta_0) = 0$, $\mu(\theta) < 0 \quad \forall \theta \neq \theta_0 \quad (\theta_0 = \operatorname{argmin} \mu)$

By definition, $\hat{\theta}_n$ maximizes $\bar{W}_n$,

$\delta_n = \|\bar{W}_n - \mu\|_\infty \overset{P}{\to} 0$.

Fix $\varepsilon > 0$, want to show $\mathbb{P}(\|\hat{\theta} - \theta_0\| \ge \varepsilon) \to 0$

Let $\widetilde{\Theta}_\varepsilon = \Theta \setminus B_\varepsilon(\theta_0) = \{\theta \in \Theta : \|\theta - \theta_0\| \ge \varepsilon\}$ (compact)

Let $\mu_\varepsilon^* = \max_{\theta \in \widetilde{\Theta}_\varepsilon} \mu(\theta) < 0 = \mu(\theta_0)$

$W_\varepsilon^* = \max_{\theta \in \widetilde{\Theta}_\varepsilon} \bar{W}_n(\theta)$

---

$$\mathbb{P}_{\theta_0}(\|\hat{\theta} - \theta_0\| \ge \varepsilon) \le \mathbb{P}_{\theta_0}\left(W_\varepsilon^* \ge \bar{W}_n(\theta_0)\right)$$

$$\le \mu_\varepsilon^* + \delta_n \quad \ge -\delta_n$$

$$\le \mathbb{P}_{\theta_0}\left(2\delta_n \ge \underbrace{-\mu_\varepsilon^*}_{> 0}\right) \to 0$$

$$\tag*{$\blacksquare$}$$

**Note** We usually care about non-compact parameter spaces, need some extra assumption to get us there.

**Corollary** Same assumptions except now $\Theta = \mathbb{R}^d$, (non-compact) but there's some $R < \infty$ large enough so

$$\mathbb{P}_{\theta_0}(\|\hat{\theta}_n - \theta_0\| > R) \to 0$$

Then $\hat{\theta}_n \overset{P}{\to} \theta_0$.

**Proof** Let $\widetilde{\Theta} = \{\theta : \|\theta - \theta_0\| \le R\}$, $\widetilde{\theta}_n = \underset{\theta \in \widetilde{\Theta}}{\operatorname{argmax}} \, p_\theta(X)$

Then $\widetilde{\theta}_n \overset{P}{\to} \theta_0$ by assumption

$\mathbb{P}(\hat{\theta}_n \neq \widetilde{\theta}_n) = \mathbb{P}_{\theta_0}(\hat{\theta}_n \notin \widetilde{\Theta}) \to 0$

so $\hat{\theta}_n - \widetilde{\theta}_n \overset{P}{\to} 0 \implies \hat{\theta}_n = \widetilde{\theta}_n + (\hat{\theta}_n - \widetilde{\theta}_n) \overset{P}{\to} \theta_0$ $\tag*{$\blacksquare$}$

So the only thing we actually need to worry about is if $\hat{\theta}_n$ is extremely far away from $\theta_0$ with non-negligible prob.

---

---

[← Consistency of MLE](03-consistency-of-mle.md) · [Up: contents](index.md) · [Theorem (Asymptotic distribution of MLE) →](05-theorem-asymptotic-distribution-of-mle.md)
