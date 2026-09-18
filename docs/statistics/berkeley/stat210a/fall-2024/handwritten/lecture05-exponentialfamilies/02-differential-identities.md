---
title: Differential Identities
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture05-exponentialfamilies.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture05-exponentialfamilies.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture05-exponentialfamilies.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture05-exponentialfamilies.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Differential Identities

Write
$$e^{A(\eta)} = \int e^{\eta' T(x)} h(x) \, d\mu(x) \qquad (*)$$

We can derive lots of useful identities by differentiating $(*)$ on both sides, pulling derivative inside $\int$ [not always allowed]

**Keener Thm 2.4** For $f: \mathcal{X} \to \mathbb{R}$ let
$$\Xi_f = \left\{ \eta \in \mathbb{R}^s : \int |f| e^{\eta' T} h \, d\mu < \infty \right\}$$
Then $g(\eta) = \int f e^{\eta' T} h \, d\mu$ has cts partial derivatives of all orders for $\eta \in \Xi_f^\circ$, & we can get them by differentiating under the $\int$ sign.

$\Rightarrow$ on $\Xi_1^\circ$, $A(\eta)$ has all partial derivatives

### Differentiate once:

$$\frac{\partial}{\partial \eta_j} e^{A(\eta)} = \frac{\partial}{\partial \eta_j} \int e^{\eta' T(x)} h(x) \, d\mu(x)$$

$$e^{A(\eta)} \frac{\partial A}{\partial \eta_j}(\eta) = \int T_j(x) e^{\eta' T(x) - A(\eta)} h(x) \, d\mu(x)$$

$$\Rightarrow \frac{\partial A}{\partial \eta_j}(\eta) = \mathbb{E}_\eta [T_j(X)]$$

$$\nabla A(\eta) = \mathbb{E}_\eta [T(X)]$$

---

### Diff twice:

$$\frac{\partial^2}{\partial \eta_j \partial \eta_k} e^{A(\eta)} = \frac{\partial^2}{\partial \eta_j \partial \eta_k} \int e^{\eta' T} h \, d\mu$$

$$e^{A(\eta)} \left( \frac{\partial^2 A}{\partial \eta_j \partial \eta_k} + \underbrace{\frac{\partial A}{\partial \eta_j}}_{\mathbb{E}[T_j]} \underbrace{\frac{\partial A}{\partial \eta_k}}_{\mathbb{E}[T_k]} \right) = \underbrace{\int T_j T_k \, e^{\eta' T - A(\eta)} h \, d\mu}_{\mathbb{E}[T_j T_k]}$$

$$\frac{\partial^2 A}{\partial \eta_j \partial \eta_k}(\eta) = \text{Cov}_\eta(T_j, T_k)$$

$$\nabla^2 A(\eta) = \text{Var}_\eta(T(X)) \in \mathbb{R}^{s \times s}$$

### Example: Poisson: $T(X) = X$, $A(\eta) = e^\eta$ ($=\lambda$)

$$\mathbb{E}_\eta [X] = \frac{d}{d\eta} e^\eta = e^\eta = \lambda$$

$$\text{Var}_\eta(X) = \frac{d^2}{d\eta^2} e^\eta = e^\eta = \lambda$$

**NB:** We would get wrong answer by differentiating wrt $\lambda$

---

## Moment-generating function

We can get $k^{\text{th}}$ order moments of $T(X)$ by
1) Differentiating $(*)$ $k$ times, then
2) Dividing by $e^{A(\eta)}$

That is because $M_\eta^T(u) = e^{A(\eta+u) - A(\eta)}$ is the **moment-generating function** (mgf) of $T(X)$ when $X \sim P_\eta$

$$M_\eta^{T(X)}(u) = \mathbb{E}_\eta \left[ e^{u' T(X)} \right]$$
$$= \int e^{u' T} e^{\eta' T - A(\eta)} h \, d\mu$$
$$= e^{A(\eta+u) - A(\eta)} \underbrace{\int e^{(\eta+u)' T - A(\eta+u)} h \, d\mu}_{= 1}$$

Useful for
* finding moments
* finding dist. of sums of indep. RVs

### Cumulant-generating function

$$K_\eta^T(u) = \log M_\eta^T(u) = A(\eta+u) - A(\eta) \quad (A \text{ is sometimes called cgf})$$

---

## Other Parameterizations

Sometimes it is more convenient to use a different parameterization:
$$p_\theta(x) = e^{\eta(\theta)' T(x) - B(\theta)} h(x)$$
$$B(\theta) = A(\eta(\theta))$$

Many, many examples, sometimes requires massaging to see that they are exp. fam.s:

### Ex: Normal $X \sim N(\mu, \sigma^2) \quad \mu \in \mathbb{R} \quad \sigma^2 > 0$

$$\text{Let } \theta = (\mu, \sigma^2)$$
$$p_\theta(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-(\mu-x)^2 / 2\sigma^2}$$
$$= \exp \left\{ \frac{\mu}{\sigma^2} x - \frac{1}{2\sigma^2} x^2 - \frac{\mu^2}{2\sigma^2} - \frac{1}{2} \log (2\pi\sigma^2) \right\}$$

$$\eta(\theta) = \begin{pmatrix} \mu/\sigma^2 \\ -1/2\sigma^2 \end{pmatrix} \qquad T(x) = \begin{pmatrix} x \\ x^2 \end{pmatrix} \qquad h(x) = 1$$

$$B(\theta) = \frac{\mu^2}{2\sigma^2} + \frac{1}{2} \log (2\pi\sigma^2)$$

### Natural parameterization

$$p_\eta(x) = e^{\eta' \binom{x}{x^2} - A(\eta)}$$
$$A(\eta) = \frac{-\eta_1^2}{4\eta_2} + \frac{1}{2} \log(-\pi/\eta_2)$$

---

## More examples

### Binomial $X \sim \text{Binom}(n, \theta)$

$$p_\theta(x) = \theta^x (1-\theta)^{n-x} \binom{n}{x} \qquad x = 0, \dots, n$$
$$= \left(\frac{\theta}{1-\theta}\right)^x (1-\theta)^n \binom{n}{x}$$
$$= \exp \left\{ \log\left(\frac{\theta}{1-\theta}\right) \cdot x + n \log(1-\theta) \right\} \binom{n}{x}$$

$$\eta(\theta) = \log\left(\frac{\theta}{1-\theta}\right) \quad \text{"log odds ratio"}$$

### Beta $X \sim \text{Beta}(\alpha, \beta)$

$$p_{\alpha,\beta}(x) = x^{\alpha-1} (1-x)^{\beta-1} / B(\alpha, \beta) \leftarrow \text{Beta function}$$
$$= \exp \{ \alpha \log x + \beta \log(1-x) - \log B(\alpha, \beta) \} \frac{1}{x(1-x)}$$

$$\eta = \begin{pmatrix} \alpha \\ \beta \end{pmatrix} \qquad T(x) = \begin{pmatrix} \log x \\ \log(1-x) \end{pmatrix} \qquad h(x) = \frac{1}{x(1-x)}$$

Practically everything else on Wikipedia too:
Beta, Gamma, Multinom., Dirichlet, Pareto, Wishart...

---

## Interpretation: Exponential tilting

Can think of $p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$ as an **exponential tilt** of the carrier $h(x)$

1) Start with carrier $h(x)$
2) Multiply by $e^{\eta' T(x)}$
3) Re-normalize by $e^{-A(\eta)}$

$T(x) = (T_1(x), \dots, T_s(x))$ gives linear space of directions in which we can tilt $h(x)$

$\Xi_1 = \text{all tilts after which normalization is possible}$

$\Rightarrow$ Decomposition into $\eta, T, h, A$ very non-unique

1) Only $\text{span}(T_1, \dots, T_s)$ matters
2) Could absorb $h$ into $\mu$ ($d\nu(x) = h \, d\mu(x)$)
   (wlog $h(x) \equiv 1$ if we want)
3) Can add constant to $T(x)$
   $\vdots$ many others

---

## Distribution of $T(X)$

$$\text{Suppose } X \sim p_\eta(x) = e^{\eta' T(x) - A(\eta)} \quad \begin{array}{l} \text{wrt } \mu \\ (\text{wlog } h \equiv 1) \end{array}$$

$$\text{Then } T(X) \sim q_\eta(t) = e^{\eta' t - A(\eta)} \quad \text{wrt } \nu,$$
where $\nu$ is the measure $\mu$ "pushed forward" through $T: \mathcal{X} \to \mathbb{R}^s$
$$\nu(B) \triangleq \mu(\{x : T(x) \in B\})$$

$$\mathbb{P}_\eta(T(X) \in B) = \int \mathbf{1}_B(T(x)) e^{\eta' T(x) - A(\eta)} \, d\mu(x)$$
$$= \int \mathbf{1}_B(t) e^{\eta' t - A(\eta)} \, d\nu(t)$$

Simplest in discrete case: (drop $h \equiv 1$ assumption)

$$\mathbb{P}_\eta(T(X) = t) = \sum_{x : T(x) = t} e^{\eta' T(x) - A(\eta)} h(x) \mu(\{x\})$$
$$= e^{\eta' t - A(\eta)} \underbrace{\sum_{x : T(x) = t} h(x) \mu(\{x\})}_{\nu(\{t\})}$$

---

## Canonical Form

The structure is most evident when:

* $T(x) = x$ (wlog: sufficiency reduction)
* $h(x) \equiv 1$ (wlog: absorb $h$ into $\mu$)
* $\theta = \eta$ (wlog: parameterize by $\eta$)

Then, we say the family is in **canonical form**:
$$p_\eta(x) = e^{\eta' x - A(\eta)}$$

---

## Minimal form

Form of $p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$ **minimal** if $\eta \in \Xi$ and $T(x)$ satisfy no linear constraints:
no $a \neq 0$, $b \in \mathbb{R}$ s.t. $\eta' a = b$ for all $\eta \in \Xi$
or $T(x)' a = b$ $P$-a.s.

Otherwise we can represent $\mathcal{P}$ as an $r$-dim. ex. fam. for some $r < s$

If $p_\eta$ minimal, then $T(X)$ is minimal suff.
$$\text{Need to show } \ell(\cdot; x) = \ell(\cdot; y) + c_{xy} \underset{(\Leftarrow \text{holds by suff.})}{\Rightarrow} T(x) = T(y)$$

$$\ell(\eta; x) - \ell(\eta; y) = \eta' \underbrace{(T(x) - T(y))}_a$$

Can find $\eta, \zeta \in \Xi$ s.t. $\eta' a \neq \zeta' a$ unless $a = 0$

$$\Rightarrow T(x) = T(y)$$

**Important**: Converse is not true: reducing dimension of $T(X)$ may or may not be a data reduction (See multinomial problem in hw)

---

## Diagram

$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$$

Three subfamilies $\{P_\eta : \eta \in \Xi \subseteq \Xi_1\}$

$s=2$

```
  \eta_2 ^
        |              .---------. \Xi_1
        |             /           \
        |            /  (A)        \  (B)
        |           /  Minimal      \  Minimal
        |          /   ///////       |
        |         (   /////////      \
        |          \   ///////        )
        |           \                /
        |            \  (C)         /
        |             \  |  ^ \gamma|
        |          \   \ | /       /
        |     \gamma_\perp \|/        /
        |              / \       /
        |             /   \     /
        |            /  Not minimal
        |           / \eta = \eta_0 + \theta \gamma, \theta \in \Theta \subseteq \mathbb{R}
        |          /  \gamma_\perp' \eta = \gamma_\perp' \eta_0 \ \forall \eta
        |         '-----------------'
        +----------------------------------------> \eta_1
```

Can make (C) minimal for $s=1$
$$e^{\eta' T(x) - A(\eta)} h(x) = e^{\theta \underbrace{(\gamma' T(x))}_{\text{new } T(x)} - A(\eta_0 + \theta \gamma)} h(x)$$

---

[← Exponential Families](01-exponential-families.md) · [Up: contents](index.md)
