---
title: Ex Generalized linear model with fixed $x$
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture23-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture23-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Ex Generalized linear model with fixed $x$

$x_1, \ldots, x_n \in \mathbb{R}^d$ fixed

$Y_i \overset{\text{ind.}}{\sim} p_{\eta_i}(y) = e^{\eta_i Y_i - A(\eta_i)} h(y_i)$

$\eta_i = \beta' x_i$ (canonical form)

Let $\mu_i(\beta) = \mathbb{E}_\beta Y_i$ ($= \mu(\eta_i(\beta))$)

(more general: $f(\mu_i) = \beta' x_i$ for link fcn $f$)

Most common examples:
- Logistic regression: $Y_i \overset{\text{ind.}}{\sim} \text{Bern}\left(\frac{e^{x_i'\beta}}{1 + e^{x_i'\beta}}\right)$
- Poisson log-linear model: $Y_i \overset{\text{ind.}}{\sim} \text{Pois}(e^{x_i'\beta})$

$$\ell_n(\beta; Y) = \sum_i (x_i'\beta) y_i - A(x_i'\beta) - \log h(y_i)$$

$$\nabla \ell_n(\beta; Y) = \sum_i y_i x_i - \dot{A}(x_i'\beta) \cdot x_i$$
$$= \sum_i (y_i - \mu_i(\beta)) x_i$$

$$-\nabla^2 \ell_n(\beta; Y) = \sum_i \ddot{A}(x_i'\beta) \cdot x_i x_i'$$
$$= \sum_i \operatorname{Var}_\beta(y_i) \cdot x_i x_i' \quad (\text{Not random})$$
$$= \operatorname{Var}_\beta(\nabla \ell_n(\beta; Y))$$

---

$$(-\nabla^2 \ell_n(\beta))^{-1/2} \nabla \ell_n(\beta) \sim (0, I_d) \quad \text{in finite samples}$$
$$\overset{*}{\Rightarrow} N_d(0, I_d)$$

$*$ Under regularity cond. on $X = \begin{pmatrix} - x_1' - \\ \vdots \\ - x_n' - \end{pmatrix}$

Taylor expansion of $\ell_n$ leads to

$$\hat{J}_n^{1/2}(\hat{\beta}_n - \beta) \Rightarrow N_d(0, I_d)$$

## Advantages of Wald test:

1) Easy to invert, simple conf. regions
2) Asymptotically correct

## Disadvantages:

1) Have to compute MLE
2) Depends on parameterization
3) Relies on two approximations:
   $\nabla \ell_n \approx \text{Normal}$ and $\ell_n \approx \text{quadratic}$
4) Need MLE to be consistent
5) Confidence interval / ellipsoid might go outside $\Theta$!

---

## Score Test

Test $H_0: \theta = \theta_0$ vs. $H_1: \theta \neq \theta_0$

We can bypass quadratic approximation entirely by using score as test stat

$$\frac{1}{\sqrt{n}} \nabla \ell_n(\theta_0; X) \xrightarrow{P_{\theta_0}} N_d(0, J_1(\theta_0))$$

(or $J_n(\theta_0)^{-1/2} \nabla \ell_n(\theta_0; X) \xrightarrow{P_{\theta_0}} N_d(0, I_d)$)

So, we can reject $H_0: \theta = \theta_0$ if

$$\|J_n(\theta_0)^{-1/2} \nabla \ell_n(\theta_0; X)\|_2^2 \ge \chi_d^2(\alpha)$$

$d = 1$: $\frac{\dot{\ell}_n(\theta_0)}{\sqrt{J_n(\theta_0)}} \Rightarrow N(0, 1)$, can do 1-sided tests

## Remarks

- No quadratic approx., no MLE
- No need to estimate Fisher info at $\theta_0$

Can be generalized to case with nuisance params.
Typically estimate via MLE on $\Theta_0$.

---

## Score test is invariant to reparameterization\*

Assume $d = 1$, $\theta = g(\zeta)$, $\dot{g}(\zeta) > 0 \; \forall \zeta$

$$q_\zeta(x) = p_{g(\zeta)}(x)$$

$$\dot{\ell}^{(\zeta)}(\zeta; x) = \frac{d}{d\zeta} \log p_{g(\zeta)}(x)$$
$$= \dot{\ell}^{(\theta)}(g(\zeta); x) \cdot \dot{g}(\zeta)$$

$$J^{(\zeta)}(\zeta) = J^{(\theta)}(g(\zeta)) \cdot \dot{g}(\zeta)^2$$

So $\frac{\dot{\ell}^{(\zeta)}(\zeta_0; X)}{\sqrt{J^{(\zeta)}(\zeta_0)}} \overset{\text{a.s.}}{=} \frac{\dot{\ell}^{(\theta)}(\theta_0; X)}{\sqrt{J^{(\theta)}(\theta_0)}}$

if $\theta_0 = g(\zeta_0)$

## **Ex** $s$-parameter exp. fam:

$$X_1, \ldots, X_n \overset{\text{iid}}{\sim} e^{\eta' T(x) - A(\eta)} h(x)$$

$$\nabla \ell(\eta; X) = \sum T(X_i) - n \mu(\eta)$$

$$\|J_n(\eta_0)^{-1/2} \left(\sum T(X_i) - n \mu(\eta_0)\right)\|^2 \Rightarrow \chi_d^2$$

$$\frac{\sum T(X_i) - n \mu(\eta_0)}{\sqrt{n \operatorname{Var}_{\eta_0}(T(X_i))}} \xrightarrow{P_{\eta_0}} N(0, 1)$$

---

## **Ex** $X_1, \ldots, X_n \overset{\text{iid}}{\sim} \text{Laplace}(\theta) = \frac{1}{2} e^{-|x - \theta|}$

Test $H_0: \theta \le 0$ vs $H_1: \theta > 0$ (Right-tailed)

$$\ell_n(\theta; X) = -\sum_{i=1}^n |X_i - \theta| - n \log(2)$$

$$\dot{\ell}_n(\theta; X) = \sum_{i=1}^n \operatorname{sgn}(X_i - \theta) \qquad \operatorname{sgn}(z) = \begin{cases} +1 & z > 0 \\ 0 & z = 0 \\ -1 & z < 0 \end{cases}$$

$$\dot{\ell}_n(0; X) = \sum_{i=1}^n \operatorname{sgn}(X_i)$$
$$= #\{i : X_i > 0\} - #\{i : X_i < 0\}$$
$$= 2 #\{i : X_i > 0\} - n$$

$Y \sim \text{Binom}(n, 1/2)$ **sign test**

**Note:** this test is $\approx$ the exact NP LRT for $H_0: \theta = 0$ vs $H_0: \theta = \varepsilon$, for $\varepsilon \downarrow 0$

**Intuition:** Maximize power for nearby alternatives, since we'll have power $\approx 1$ for $\theta \gg 1/\sqrt{n}$

More generally, one-sided score test is "almost" UMP for nearby alternatives.

$$\log \frac{p_{\theta_0 + \varepsilon}(x)}{p_{\theta_0}(x)} \approx \varepsilon \, \dot{\ell}_n(\theta_0; X) \quad \text{for small } \varepsilon > 0$$

---

---

[← Outline](01-outline.md) · [Up: contents](index.md) · [Ex Pearson's $\chi^2$ test (goodness of fit) →](03-ex-pearson-s-test-goodness-of-fit.md)
