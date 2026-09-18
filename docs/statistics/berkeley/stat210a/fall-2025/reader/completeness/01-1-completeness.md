---
title: 1 Completeness
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html
source_file: sources/berkeley-stat210a/fall-2025/reader/completeness.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/completeness.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Completeness

1.  [Course Reader](../introduction/index.md)
2.  [Completeness, Ancillarity, and Basu’s Theorem](index.md)

## Completeness, Ancillarity, and Basu’s Theorem {#completeness-ancillarity-and-basus-theorem .title}

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
\DeclareMathOperator*{\maxz}{maximize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
\newcommand{\ep}{\varepsilon}
$$

### 1 Completeness {.anchored number="1" anchor-id="completeness"}

As we have seen, for a given statistical problem we may have many different sufficient statistics, some of which reduce the data more than others. We usually want to look for one that is *minimal sufficient*, meaning that it strips away as much irrelevant information as possible and only retains the information that is relevant to estimating the parameter.

In some cases the minimal sufficient statistic has an additional property called *completeness*. The definition of completeness is initially counterintuitive, but it has a number of useful implications we will explore throughout the semester.

#### 1.1 Definition of completeness {.anchored number="1.1" anchor-id="definition-of-completeness"}

A statistic $T(X)$ is complete for a family of distributions $\cP = \{P_\theta: \theta \in \Theta\}$ if no nontrivial function of $T$ can have expectation zero for every distribution in the family:

$$
\EE_\theta \,f(T(X)) = 0 \quad \forall \theta \in \Theta \implies f(T) \eqPas 0
$$

Note

The name for complete statistics comes from a prior notion that $\cP^T = \{P_\theta^T:\; \theta \in \Theta\}$ is \`\`complete’’ as a model if its linear span includes all possible distributions on $T(X)$; see Homework 3.

An equivalent formulations would is that if $\EE_\theta f(T(X)) = c \forall \theta$, for any constant $c$, then $f(T) \eqPas c$.

If $X$ itself is complete, then the definition immediately implies that there can be at most one unbiased estimator for any estimand: if $\EE_\theta \delta_1(X) = \EE_\theta \delta_2(X) = g(\theta)$ for all $\theta \in \Theta$, then $f(X) = \delta_1(X) - \delta_2(X) = 0$ almost surely. More generally, if $T(X)$ is a complete statistic then there can be at most one unbiased estimator that runs through $T$. We will return to this fact when we discuss unbiased estimation.

We will be especially interested in statistics that are both complete and sufficient. If $T(X)$ is complete and sufficient we call it a *complete sufficient statistic*.

Warning

A complete statistic need not be sufficient: the constant “statistic” $T(X) \equiv 0$ is complete in any model. In general, to show that $T(X)$ is complete sufficient we must establish both properties.

#### 1.2 Examples {.anchored number="1.2" anchor-id="examples"}

**Example 1 (Laplace location family)**: Let $X_1,\ldots,X_n \simiid \text{Lap}(\theta)$ for $\theta \in \RR$ and $n\geq 2$, and recall that the vector of order statistics $S(X) = (X_{(1)},\ldots,X_{(n)})$ is a minimal sufficient statistic. Is $S(X)$ complete?

Expand to see answer

**No, $S(X)$ is not complete.**

One simple way to see this is that $X_{(n)}-X_{(1)}$ has the same distribution for every $\theta$, because we can write $X_i = \theta + Z_i$ for $Z_1,\ldots,Z_n \simiid \text{Lap}(0)$ and then $X_{(n)}-X_{(1)} = Z_{(n)}-Z_{(1)}$.

Another evocative counterexample is that both the sample median $\text{Med}(X)$ and sample mean $\overline{X}$ can be calculated using $S(X)$ alone, and both are unbiased estimators for $\theta$ (since the distribution is symmetric for $\theta=0$ and $\text{Med}(X) = \theta + \text{Med}(Z)$). Hence $f(S) = \text{Med}(X) - \overline{X}$ has expectation zero, but is not almost surely equal to zero because the median and mean are a.s. unequal for $n>2$.

**Example 1 (Uniform scale family)**: Let $X_1, \ldots, X_n \simiid U[0, \theta]$, for $\theta > 0$. We showed previously that the maximum $T(X) = X_{(n)}$ is minimal sufficient. Is it complete?

Expand to see answer

**Yes, $T(X)$ is complete.**

As we showed previously, the density of $T(X)$ for $t > 0$ is

$$
p_\theta(t) =  \frac{nt^{n-1}}{\theta^n}\,\cdot \;1\{t \leq \theta\}.
$$

Suppose we could find $f(t)$ such that

$$
0 = \EE_\theta f(T) = \frac{n}{\theta^n}\int_0^\theta f(t) t^{n-1} \,dt, \quad \text{ for all } \theta > 0.
$$

 Dividing the last expression by $n/\theta^n$ and then differentiating with respect to $\theta$, we obtain

$$
0 = f(\theta) \theta^{n-1}, \quad \text{ for all } \theta > 0,
$$

 hence $f \equiv 0$.

#### 1.3 Full-rank exponential families {.anchored number="1.3" anchor-id="full-rank-exponential-families"}

In the general case where $T(X)$ can take on infinitely many values, it can be hard to show completeness because the space of possible counterexample functions $f$ is infinite-dimensional. But there is an important class of examples where we can quickly verify complete sufficiency, as we see next.

**Definition:** Let $\cP = \{P_\eta:\; \eta \in \Xi\}$ be an $s$-parameter exponential family with densities

$$
p_\eta(x) = e^{\eta'T(x) - A(\eta)} h(x),
$$

 with respect to some carrier measure $\mu$. Assume further that the sufficient statistic $T(X)$ satisfies no affine constraint: that is, there is no $\alpha \in \RR$ and nonzero $\beta \in \RR^s$ with $\beta'T(x) \eqPas \alpha$.

If $\Xi$ contains an open set we say $\cP$ is *full-rank*; otherwise we say it is *curved*.

Note

If $T(X)$ does satisfy a linear constraint, that means $\cP$ can be defined equivalently as an $r$-parameter exponential family for some $r < s$. It may be full-rank or curved depending on the parameter space in a lower-dimensional parameterization.

**Theorem (Complete sufficiency in full-rank exponential families):** If $\cP$ is a full-rank $s$-parameter exponential family, then $T(X)$ is complete sufficient.

The proof is somewhat technical and uses the uniqueness of moment-generating functions.

Expand for proof

$T(X)$ is sufficient by the factorization theorem, so it remains only to prove completeness.

Assume without loss of generality that $0$ is in the interior of $\Xi$; otherwise we can reparameterize. Assume also that $\cP$ is in canonical form, i.e. $T(X) = X$ and $p_\eta(x) = e^{\eta'x - A(\eta)}$. We can always reduce to this case by making a sufficiency reduction and taking $P_0^T$ as the carrier measure, and showing $T(X)$ is complete after a sufficiency reduction is equivalent to showing it is complete in the original model.

If $X$ is not complete then there is some nontrivial $f(x)$ for which $\EE_\eta f(X) = 0$ for all $\eta\in\Xi$. Decompose $f(x) = f^+(x) - f^-(x)$ where $f^+(x) = \max\{0,f(x)\}$ and $f^{-}(x) = \max\{0,-f(x)\}$.

If $\EE_\eta f(X) = \int (f^+-f^-)p_\eta \,d\mu = 0$ for all $\eta\in\Xi$, then we have

$$
\int e^{\eta'x} f^+(x) \,d\mu(x) = \int e^{\eta'x} f^-(x) \,d\mu(x), \quad \text{ for all } \eta \in \Xi.
\tag{1}
$$

Assume wlog that $\int f^+(x)\,d\mu(x) = \int f^-(x)\,d\mu(x) = 1$ (otherwise normalize $f$). Then we can define the random variables $Y^+$ and $Y^-$ with probability densities $f^+(x)$ and $f^-(x)$ respectively, and Equation 1 implies that $Y^+$ and $Y^-$ have equal MGFs in a neighborhood of $0$. Hence they have the same distribution and their densities must be a.s. equal to each other. But $f^+(x)=f^-(x)$ only when both are zero, so $f(x) \eqmuas 0$ and we have derived a contradiction.

The next figure shows three cases for exponential families with the same sufficient statistic. The set $\Xi_1$ indicates the full natural parameter space for a generic 2-parameter exponential family, and (A), (B), and (C) denote parameter spaces for three different subfamilies. The subfamily described by the shaded circle (A) is a full-rank exponential family, because it contains an open set. The subfamily described by the curve (B) is a typical example of a curved family, because it does not contain an open set. The subfamily described by the line segment (C) can be re-parameterized as a full-rank $1$-parameter exponential family.

![](https://raw.githubusercontent.com/berkeley-stat210a/fall-2025/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.png)

This figure shows three cases:

#### 1.4 Complete sufficient statistics are minimal {.anchored number="1.4" anchor-id="complete-sufficient-statistics-are-minimal"}

A second convenient property of completeness is that complete sufficient statistics are always minimal sufficient.

**Theorem:** If $T(X)$ is complete sufficient for the family $\mathcal{P}$, then $T(X)$ is minimal sufficient for $\cP$.

The way that we usually use completeness in proofs is to show that two quantities are almost surely equal by showing that they have the same expectation. The next proof is an example.

*Proof:* Let $S(X)$ represent any minimal sufficient statistic, and define the conditional expectation of $T$ given $S$:

$$
\overline{T}(S(X)) = \EE[T(X) \mid S(X)].
$$

 Note that this conditional expectation does not depend on the parameter $\theta$, because $S(X)$ is sufficient, so $\overline{T}$ is a valid statistic. If we can show that $\overline{T} \eqas T(X)$, that means we can calculate $T(X)$ from $S(X)$, so $T(X)$ is also minimal sufficient.

Because $S(X)$ is minimal sufficient, we can write it as $f(T(X))$ for some function $f$, and use $f$ to define a function $g$ giving the difference between $T$ and $\overline{T}$:

$$
g(t) = t - \overline{T}(f(t)).
$$

 The expectation of $g(T)$ is always zero, because

$$
\begin{aligned}
\EE_\theta\; g(T(X)) &= \EE_\theta\; T(X) - \EE_\theta\; \overline{T}(S(X)) [5pt]
&= \EE_\theta\; T(X) - \EE_\theta\left[\EE[T(X) \mid S(X)]\right]\\
&= 0.
\end{aligned}
$$

 As a result, $g(T) \eqas 0$ and hence $T \eqas \overline{T}$, as desired.

---

[Up: contents](index.md) · [2 Ancillarity →](02-2-ancillarity.md)
