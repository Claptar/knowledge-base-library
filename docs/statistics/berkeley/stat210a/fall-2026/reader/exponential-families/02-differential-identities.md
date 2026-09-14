---
title: Differential identities
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/exponential-families.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/exponential-families.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Differential identities

**Source:** [`reader/exponential-families.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/exponential-families.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Exponentiating @eq-log-partition, we obtain the equation

$$
e^{A(\eta)} = \int_\cX e^{\eta'T(x)}h(x)\td\mu(x)
$$ {#eq-partition}

We can derive many interesting identities by differentiating this function, and related functions, with respect to $\eta$. We will always evaluate derivatives by differentiating under the integral sign. This is not always a correct operation, but by Theorem 2.4 in Keener, it is correct on the interior of the natural parameter space $\Xi_1$. We refer the reader to Keener for details.

### Mean of $T(X)$

Partially differentiating @eq-partition once with respect to a generic coordinate $\eta_j$, for $j =1, \ldots, s$, we obtain

$$
\begin{aligned}
\frac{\partial}{\partial \eta_j} e^{A(\eta)} &= \int_\cX \frac{\partial}{\partial \eta_j} e^{\eta'T(x)}h(x)\td\mu(x)\\[7pt]
e^{A(\eta)} \frac{\partial A}{\partial \eta_j}(\eta) &= \int_\cX T_j(x) e^{\eta'T(x)}h(x)\td\mu(x)\\[7pt]
\frac{\partial A}{\partial \eta_j}(\eta) &= \int_\cX T_j(x) e^{\eta'T(x) - A(\eta)}h(x)\td\mu(x)\\[7pt]
&= \EE_\eta \left[\,T_j(X)\,\right]\\
\end{aligned}
$$

Arranging these partial derivatives into a vector, we obtain

$$
\nabla A(\eta) = \EE_\eta\left[\,T(X)\,\right],
$$

which gives us a very convenient method for evaluating the expectation of the sufficient statistic.

### Variance of $T(X)$

Pushing our luck further, we can take a second partial derivative:

$$
\begin{aligned}
\frac{\partial^2}{\partial \eta_j\partial \eta_k} e^{A(\eta)} &= \int_\cX \frac{\partial^2}{\partial \eta_j\partial \eta_k} e^{\eta'T(x)}h(x)\td\mu(x)\\[7pt]
e^{A(\eta)}\left(\frac{\partial^2 A}{\partial \eta_j\partial \eta_k} + \frac{\partial A}{\partial \eta_j} \frac{\partial A}{\partial \eta_k} \right)&= \int_\cX T_j(x) T_k(x)e^{\eta'T(x)}h(x)\td\mu(x)\\[7pt]
\frac{\partial^2 A}{\partial \eta_j\partial \eta_k} + \EE_\eta[T_j(X)]\EE_\eta[T_k(X)] &= \EE_\eta \left[\,T_j(X) T_k(X)\,\right]\\
\frac{\partial^2 A}{\partial \eta_j\partial \eta_k} &= \text{Cov}_\eta\left(T_j(X), T_k(X)\right).
\end{aligned}
$$

Again, collecting these second partials into a Hessian matrix gives us

$$
\nabla^2 A(\eta) = \text{Var}_\eta(T(X)),
$$

where the right-hand side denotes the $s\times s$ variance-covariance matrix of the random vector $T(X)$.

**Example (Poisson, continued):** As we showed above, in the Poisson exponential family the sufficient statistic is $T(X)=X$, the natural parameter is $\eta = \log\lambda$, and the log-partition function is $A(\eta) = e^\eta \;(=\lambda)$.

**Note:** This calculation would not have worked correctly if we had instead said $A(\eta) = \lambda$, and differentiated that expression with respect to $\lambda$. We would then get $\EE_\eta[X] = 1$ and $\text{Var}_\eta(X) = 0$, which are clearly incorrect.

### Moment-generating function and cumulant-generating function

The moment generating function (MGF) of a $d$-dimensional random vector $X\sim P$ is defined as $M^X(u) = \EE[e^{u'X}]$, for $u\in \RR^d$. If the MGF is well-defined in a neighborhood of $u=0$, then we can use it to calculated moments of $X$ by evaluating its derivatives at 0.

We can show this using manipulations very similar to the ones we saw above. To evaluate the first moment of $X_j$, we can differentiate once with respect to $u_j$, since

$$
\frac{\partial}{\partial u_j} M^X(u) = \int_\cX \frac{\partial}{\partial u_j} e^{u'x}\td P(x) = \int_\cX x_j e^{u'x}\td P(x) = \int_\cX x_j e^{u'x} \td P(x).
$$

Here we have again assumed that we can differentiate under the integral sign; this is a technical condition that we would check if we were being more careful.

Evaluating the derivative at $u=0$, we obtain $\frac{\partial}{\partial u_j} M^X(0) = \int_\cX x_j \td P(x) = \EE[X_j]$. Moreover, we can repeat this trick as many times as we want, leading to a formula for mixed partial derivatives of any order:

$$
\left.\frac{\partial^{m_1 + \cdots + m_d}}{\partial u_1^{m_1}\cdots\partial u_d^{m_d}} M^X(u)\right|_{u=0} = \left.\int_{\cX} x_1^{m_1}\cdots x_d^{m_d} e^{u'x}\td P(x)\right|_{u=0} = \EE\left[\,X_1^{m_1} \cdots X_d^{m_d}\,\right].
$$ {#eq-mgf}

The MGF is therefore very useful for evaluating moments of $X$. It is also useful for finding distributions of sums of independent random variables, because $M^{X + Y}(u) = M^X(u)M^Y(u),$ if $X$ and $Y$ are independent. If two random variables have the same MGF then they have the same distribution.

In an exponential family, the MGF of $T(X)$, under sampling from $P_\eta$, is simple to evaluate:

$$
\begin{aligned}
M^{T(X)}_\eta(u) &= \EE_\eta\left[\,e^{u'T(X)}\,\right]\\[5pt]
&= \int_\cX e^{u'T(x)}e^{\eta'T(x) - A(\eta)}h(x)\td\mu(x) \\[5pt]
&= e^{-A(\eta)}\int_\cX e^{(u+\eta)'T(x)} h(x)\td\mu(x)\\[5pt]
&= e^{A(\eta+u)-A(\eta)}
\end{aligned}
$$

**Example (Poisson, continued):** The MGF for $X \sim \text{Pois}(\lambda)$, with $\eta = \log\lambda$, is

$$
M^{X}_\eta(u) = \exp\{e^{\eta + u} - e^{\eta}\} = \exp\{\lambda (e^u - 1)\}
$$

To see how the MGF is useful, suppose we have $X_i \sim \text{Pois}(\lambda_i)$, independently for $i = 1,2,\ldots,n$, and we want to know the distribution of $X_+ = \sum_i X_i$. Then we can multiply the MGF's for $X_1,\ldots,X_n$ together to obtain the MGF for $X_+$:

$$
M^{X_+}(u) = \prod_i M_{\eta_i}^{X_i}(u) = \exp\left\{\sum_i \lambda_i (e^u-1)\right\}.
$$

As a result, we have $X_+ \sim \text{Pois}(\lambda_+)$, for $\lambda_+ = \sum_j \lambda_i$.

Likewise, the closely related *cumulant-generating function* (CGF) is defined as the log of the MGF:

$$
K^{T(X)}_\eta(u) = \log M^{T(X)}_\eta(u) = A(\eta+u)-A(\eta)
$$

Evaluating the CGF's derivatives at $u=0$ gives us the distribution's *cumulants* instead of its moments (the first two cumulants are the mean and variance). $K_\eta^{T(X)}$ and $A$ are closely related. In particular, note that

$$
\left.\frac{\partial}{\partial \eta_j}K_\eta^{T}(u)\right|_{u=0} = \frac{\partial}{\partial \eta_j} A(\eta),
$$

This relationship explains why we can also get cumulants for $T(X)$ under $P_\eta$ by differentiating $A(\eta)$. It also partly explains why $A(\eta)$ is sometimes referred to as the CGF even though it is generally not the CGF for $T(X)$.

---

[← Exponential family structure](01-exponential-family-structure.md) · [Up: contents](index.md) · [Other parameterizations →](03-other-parameterizations.md)
