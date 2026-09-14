---
title: Consistency of MLE
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/maximum-likelihood.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/maximum-likelihood.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Consistency of MLE

**Source:** [`reader/maximum-likelihood.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/maximum-likelihood.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

$X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} f_{\theta_0}$, $\theta_n \in \arg\max_{\theta \in \Theta} \ell_n(\theta; X)$

Will be ok if $\theta_n$ comes close to maximizing $\ell_n$

Question: When does $\ell_n \to \ell$?

Assume model identifiable: $P_\theta = P_{\theta_0}$ for $\theta \neq \theta_0$

Recall KL Divergence:

$D(g\|f) = \mathbb{E}_g[\log \frac{g(X)}{f(X)}] = \int g(x) \log \frac{g(x)}{f(x)} dx$ (note switch)

$\log \frac{g}{f} \geq 1 - \frac{f}{g}$ (strict ineq unless const, i.e., unless $f=g$)

Let $W_i(\theta) = \ell_i(\theta; X_i) - \ell_i(\theta_0; X_i)$, $W(\theta) = \mathbb{E}_{\theta_0}[W_i(\theta)]$

Note: $\theta_0 = \arg\max_{\theta \in \Theta} W(\theta)$

$W(\theta_0) = 0$

$W(\theta) = -\mathbb{E}_{\theta_0}[\log \frac{f_{\theta_0}(X)}{f_\theta(X)}] = -D(f_{\theta_0}\|f_\theta) \leq 0$

$= 0$ iff $\theta = \theta_0$

But not enough:
1. MLE $\hat{\theta}_n$ depends on entire function $\ell_n$
2. Need uniform convergence in $\theta$

### Definition: Compact Convergence

For compact $K$, let $C(K) = \{f: K \to \mathbb{R} \text{ cts}\}$

For $f \in C(K)$, let $\|f\| = \sup_{x \in K} |f(x)|$

$f_n \to f$ in this norm if $\|f_n - f\| \to 0$

### Theorem: LLN for Random Functions

Assume $K$ compact, $W_i, W_2, \ldots \in C(K)$ iid
$\mathbb{E}[\|W_i\|] < \infty$, $\mathbb{E}[W_i(\theta)] = W(\theta)$

Then $\bar{W}_n \in C(K)$
and $\mathbb{P}(\|\bar{W}_n - W\| > \epsilon) \to 0$

i.e., $\ell_n \to \ell$ in $\|\cdot\|_\infty$ norm

### Theorem (Keener 9.4)

Let $G_n, G$ random functions in $K$ compact
1. $G_n \to g$ in $\|\cdot\|_\infty$, some fixed $g \in C(K)$. Then:
   a. If $t^* \in K$ fixed, then $G_n(t^*) \xrightarrow{p} g(t^*)$
   b. If $g$ maximized at unique value $t^*$
      and $G_n(t_n) = \max_t G_n(t)$, then $t_n \xrightarrow{p} t^*$
2. If $K \subset \mathbb{R}$, $g'(t) = 0$ has unique sol. $t^*$
   and $t_n$ solve $G_n'(t) = 0$, then $t_n \xrightarrow{p} t^*$

(Sketch of proof in purple)
If $G_n'(t_n) = 0$, get $G_n'(t^*) = g'(t^*) + (g'(t_n) - g'(t^*)) + (G_n'(t^*) - g'(t^*))$
$\to 0 + 0 + 0$
by assumptions + by cts mapping

Fix $\epsilon > 0$, let $B_\epsilon = \{t: \|t - t^*\| < \epsilon\}$
Let $K_\epsilon = K \setminus B_\epsilon(t^*)$, $K \setminus B_\epsilon$ compact
$\delta = g(t^*) - \max_{t \in K_\epsilon} g(t) > 0$

If $t_n \notin K_\epsilon$, then $G_n(t_n) > G_n(t^*) - \frac{\delta}{2} > g(t^*) - \delta = \max_{t \in K_\epsilon} g(t)$

$\mathbb{P}(t_n \notin K_\epsilon) \leq \mathbb{P}(\|G_n - g\|_\infty > \frac{\delta}{2}) \to 0$

Analogous to $\bar{X}_n \xrightarrow{p} \mu$

### Theorem: Consistency of MLE for Compact $\Theta$

$X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} f_{\theta_0}$, $\cP$ has densities $p_\theta$, $\theta \in \Theta$

Assume:
1. $p_\theta$ cts in $\theta$
2. $\Theta$ compact
3. $\mathbb{E}_{\theta_0}[\sup_\theta |f_\theta(X)|/f_{\theta_0}(X)] < \infty$
4. $\mathbb{E}_{\theta_0}[\sup_\theta |W_i(\theta)|] < \infty$
5. Model identifiable

Then $\hat{\theta}_n \xrightarrow{p} \theta_0$ if $\hat

---

[← Asymptotic Distribution of MLE](03-asymptotic-distribution-of-mle.md) · [Up: contents](index.md)
