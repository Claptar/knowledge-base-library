---
title: Exponential family structure
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/exponential-families.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/exponential-families.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Exponential family structure

**Source:** [`reader/exponential-families.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/exponential-families.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Thus far we have discussed statistical models in the abstract without making any assumptions about them. Exponential families, the topic of this lecture, are models with a special structure that makes them especially easy to work with.

<!--# Rewrite this to give the more general structure first and then call out the parameterization later. Also, next time maybe do sufficient statistics before exponential families? -->

We say the model $\cP = \{P_\eta:\eta \in \Xi\}$ is an $s$*-parameter* *exponential family* if it is defined by a family of densities of the form:

$$
p_\eta(x) = e^{\eta'T(x) - A(\eta)}h(x),
$$ {#eq-expo-fam}

all with respect to a common *dominating measure* $\mu$, i.e. a measure $\mu$ such that $P_\eta \ll \mu$ for all $\eta\in \Xi$.

The different parts of the expression in @eq-expo-fam have distinct names referring to the role they play in defining the density:

$$
\begin{aligned}
T&:\; \cX \to \RR^s &\qquad &\text{ is called the {\it sufficient statistic}}\\
h&:\; \cX \to [0,\infty) &\qquad &\text{ is called the {\it carrier density} or {\it base density}}\\
\eta &\in \Xi \subseteq \RR^s &\qquad &\text{ is called the {\it natural parameter}}\\
A&:\; \Xi \to \RR &\qquad &\text{ is called the {\it log-partition function}}
\end{aligned}
$$

The function $A(\eta)$ is totally determined by $T$ and $h$, and plays the role of normalizing the density so that $P_\eta(\cX) = 1$:

$$
A(\eta) = \log\left( \int_\cX e^{\eta'T(x)}h(x)\td\mu(x)\right) \leq \infty
$$ {#eq-log-partition}

If $A(\eta) = \infty$ then there is no way to normalize $p_\eta$, so $\eta$ is not an allowed value for the natural parameter to take. The *natural parameter space*, which we denote $\Xi_1$, is the set of all $\eta$ values for which the family is normalizable:

$$
\Xi_1 = \{\eta:\; A(\eta) < \infty\} \subseteq \RR^s.
$$

We will show in Homework 1 that $A(\eta)$ is a convex function, so $\Xi_1$ is a convex set.

Note that, because $\mu$ is allowed to be an arbitrary measure, $h(x)$ also plays an inessential role since we could always absorb it into the base measure $\mu$. More precisely, suppose we define a new dominating measure $\nu$ whose density with respect to $\mu$ is $h$ (informally we can write $\td\nu = h\td\mu$). Then $P_\eta$, which had density $e^{\eta'T(x)}h(x)$ with respect to $\mu$, now has density $e^{\eta'T(x)}$ with respect to $\nu$.

As a result, if we were aiming for maximal parsimony we could assume without loss of generality that $h(x) = 1$, removing it from the definition @eq-expo-fam and replacing $\mu$ with our new, bespoke measure $\nu$. However, it is convenient to leave @eq-expo-fam as is if it allows us to take $\mu$ to be some simple default measure like a counting measure or Lebesgue measure. In that case, $p_\eta$ will be a standard pmf or pdf, so we can discuss it without going over the head of anyone who lacks a background in measure theory.

**Example (Poisson):** The Poisson distribution $\textrm{Pois}(\lambda)$ has probability mass function

$$
p_\lambda(x) = \frac{\lambda^x e^{-\lambda}}{x!}, \quad \textrm{ on } x = 0, 1, 2, \ldots.
$$

Formally this pmf is a density over the counting measure on the set of non-negative integers $\ZZ_+ = \{0,1,\ldots\}$.

Letting $\lambda$ range over $[0, \infty)$ yields an exponential family, but it is not immediately obvious from the form of the density. To see this, we need to massage $p_\lambda(x)$ a bit, by observing that

$$
p_\lambda(x) = \exp\{(\log \lambda) x - \lambda\}\frac{1}{x!}.
$$

Now we see that we can reparameterize the family by setting $\eta = \log\lambda$, leading to

$$
p_\eta(x) = \exp\{\eta x - e^\eta\} \frac{1}{x!}.
$$ At this point, we immediately recognize $p_\eta$ as an exponential family with sufficient statistic $T(x) = x$, and base density $h(x) = \frac{1}{x!}$, and log-partition function $A(\eta) = e^{\eta}$.

Note that this is not the only way to decompose the Poisson distribution as an exponential family. For example, we could just as well take $T(x) = x/2$; then we would have $\eta = 2\log\lambda$ and $A(\eta) = e^{\eta/2}$. Or, we could take $T(x) = x + 1$ and $A(\eta) = e^{\eta} + \eta$.

This is not just a property of the Poisson distribution; the decomposition is generally non-unique for exponential families. For any exponential family of the form @eq-expo-fam , if $U \in \RR^{s\times s}$ is invertible and $v \in \RR^s$ then we can write the same density as $e^{\zeta'S(x) - B(\zeta)}h(x)$, for new sufficient statistic $S(x) = U T(x) + v$, new natural parameter $\zeta = (U^{-1})'\eta$, and and new log-partition function $B(\zeta) = A(U'\zeta) + \zeta'U^{-1}v$. So "the" sufficient statistic of an exponential family is defined only up to invertible affine transformations.

---

[Up: contents](index.md) · [Differential identities →](02-differential-identities.md)
