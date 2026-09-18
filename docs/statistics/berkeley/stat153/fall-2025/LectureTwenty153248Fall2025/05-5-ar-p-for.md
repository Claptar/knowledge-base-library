---
title: 5 AR(p) for $p \ge 1$
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 AR(p) for $p \ge 1$

Now consider the $\text{AR}(p)$ difference equationl In backshift notation, this is
$$\phi(B)y_t = \phi_0 + \epsilon_t \quad \text{where } \phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p.$$

We shall call $\phi(z) := 1 - \phi_1 z - \phi_2 z^2 - \dots - \phi_p z^p$ the AR polynomial.

We "solve" the $\text{AR}(p)$ by writing:
$$y_t = \frac{1}{\phi(B)} \epsilon_t = \frac{1}{1 - \phi_1 B - \dots - \phi_p B^p} \epsilon_t$$

The next step is to make sense of $1/(1 - \phi_1 B - \dots - \phi_p B^p)$. It is natural here to factorize the polynomial $1 - \phi_1 B - \dots - \phi_p B^p$ into monomials, and then use (9). So we write
$$\phi(z) = 1 - \phi_1 z - \dots - \phi_p z^p = (1 - a_1 z) \dots (1 - a_p z). \tag{10}$$
so that
$$\phi(B) = (1 - a_1 B) \dots (1 - a_p B).$$

The numbers $a_1, \dots, a_p$ appearing in (10) are simply the reciprocals of the roots of $\phi(z)$ i.e., the roots of $\phi(z)$ are given by $1/a_1, \dots, 1/a_p$. Note here that some of the $a_j$'s can be complex because the polynomial $1 - \phi_1 z - \dots - \phi_p z^p$ can have complex roots (even though all its coefficients are real).

We then get
$$y_t = \frac{1}{(1 - a_1 B) \dots (1 - a_p B)} (\phi_0 + \epsilon_t) = \prod_{k=1}^p \frac{1}{1 - a_k B} (\phi_0 + \epsilon_t).$$

For each $1/(1 - a_j B)$, we use the formula (9) to get:
$$y_t = \prod_{k=1}^p \left( \sum_{j=0}^\infty a_k^j B^j \right) (\phi_0 + \epsilon_t). \tag{11}$$

Multiplying out the product $\prod_{k=1}^p \left( \sum_{j=0}^\infty a_k^j B^j \right)$, we get
$$y_t = \prod_k \left( \sum_{j=0}^\infty a_k^j B^j \right) (\phi_0 + \epsilon_t)$$
$$= \left( \sum_{j_1=0}^\infty a_1^{j_1} B^{j_1} \right) \dots \left( \sum_{j_p=0}^\infty a_p^{j_p} B^{j_p} \right) (\phi_0 + \epsilon_t)$$
$$= \left( \sum_{j_1=0}^\infty \dots \sum_{j_p=0}^\infty a_1^{j_1} \dots a_p^{j_p} B^{j_1 + \dots + j_p} \right) (\phi_0 + \epsilon_t)$$
$$= \phi_0 \sum_{j_1=0}^\infty \dots \sum_{j_p=0}^\infty a_1^{j_1} \dots a_p^{j_p} + \sum_{j_1=0}^\infty \dots \sum_{j_p=0}^\infty a_1^{j_1} \dots a_p^{j_p} \epsilon_{t - j_1 - \dots - j_p}. \tag{12}$$

The above expression involves powers of $a_1, \dots, a_p$. For these powers to not explode, we need
$$|a_i| < 1 \quad \text{for each } i = 1, \dots, p. \tag{13}$$
Note that $a_i$ can be complex so $|a_i|$ represents the modulus of $a_j$. When $|a_i| < 1$, the powers $|a_i|^j$ decay rapidly in $j$ which makes the infinite sums above well-defined.

The formula above writes $y_t$ in terms of $\epsilon_t, \epsilon_{t-1}, \dots$. By collecting terms where $j_1 + \dots + j_p = j$ for each $j = 0, 1, \dots$, we can write this solution as
$$y_t = \mu + \sum_{j=0}^\infty \psi_j \epsilon_{t-j} \tag{14}$$
for some $\mu, \psi_1, \psi_2, \dots$. It can be checked that this is a stationary time series (note it is also causal as $y_t$ only depends on $\epsilon_t, \epsilon_{t-1}, \dots$).

The key condition here is (13). This is the analogue of the $\text{AR}(1)$ condition $|\phi_1| < 1$ for $\text{AR}(p)$ when $p \ge 1$. Because the roots of the AR polynomial $\phi(z) = 1 - \phi_1 z - \dots - \phi_p z^p$ are $1/a_1, \dots, 1/a_p$, the condition (13) is equivalent to assuming that all roots of the AR polynomial are strictly larger than 1 in modulus.

This analysis can be made rigorous to show the following:

1. When all roots of the AR polynomial are strictly larger than 1 in modulus, then there exists a unique causal stationary process $\{y_t\}$ which satisfies the $\text{AR}(p)$ equation: $y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t$. This causal stationary solution is of the form (14) where the coefficients $\psi_1, \psi_2, \dots$ are derived from (12).

2. When even one root of the AR polynomial has modulus $\le 1$, then there cannot exist a causal stationary solution to the AR equation.

3. `AutoReg` fits the model
$$y_1 = \text{fixed at observed value and } y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t$$
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. When the condition (13) is true, this model has similar behavior to (14) in the same way as the similarity between (3) and (7) for $p = 1$.

For assessing causal-stationarity of the fitted model, the output summary of `AutoReg` gives the values of the moduli of the roots of the fitted AR polynomial.

---

[← 4 Causal Stationary AR(1) formula using Backshift](04-4-causal-stationary-ar-1-formula-using-backshift.md) · [Up: contents](index.md) · [6 Determination of the order $p$ of AR($p$) →](06-6-determination-of-the-order-of-ar.md)
