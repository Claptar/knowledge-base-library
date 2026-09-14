---
title: Permutation tests
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-nuisance.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-nuisance.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Permutation tests

**Source:** [`reader/testing-nuisance.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-nuisance.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Even when we can't get a UMPU test, conditional testing can be very useful.

**Example (Two-sample permutation test):** We observe two independent samples of real-valued random variables $X_1, \ldots, X_n \simiid P$, and $Y_1, \ldots, Y_m \simiid Q$, and we want to test whether the distributions are the same or different; i.e., we test $H_0: P=Q$ vs $H_1: P \neq Q$.

We cannot write this model as an exponential family, but we can condition on a statistic that is sufficient under the null hypothesis. If $P=Q$, then we have
$$
X_1, \ldots, X_n, Y_1, \ldots, Y_m \simiid P
$$
Define the vector $Z = (Z_1, \ldots, Z_{n+m}) = (X_1, \ldots, X_n, Y_1, \ldots, Y_m)$ which concatenates the two samples. Under $H_0$, the vector of **pooled order statistics** $U(Z) = (Z_{(1)}, Z_{(2)}, \ldots, Z_{(n+m)})$ is complete sufficient for $Z=(X,Y)$, and the conditional distribution of $Z$ is uniform on all permutations of $U$; that is, if $\mathcal{S}_{n+m}$ is the group of all permutations on $n+m$ items, then
$$
Z \mid U(Z) = u \stackrel{H_0}{\sim} \text{Unif}\{\pi u:\; \pi \in \mathcal{S}_{n+m}\}.
$$
Because $U$ is sufficient for the null model, $H_0$ is a *simple null* in the conditional model. But the alternative in the conditional model is highly composite: For example, if $Q$ is stochastically larger than $P$, then the last $m$ observations in $Z$ (the $Y$ values) should be systematically larger than the first $n$ (the $X$ values); or, if $Q$ has more variability, then the sample variance of the last $m$ observations should be systematically larger than that of the first $n$, and so on.

Because there are so many ways that $P$ and $Q$ could differ from each other, there is no generically optimal test statistic for us to use. But the good news is that we can perform a valid conditional test using *any* statistic $T(X,Y)$, by conditioning on $U(X,Y)$ (we will slightly abuse notation by using $(X,Y)$ and $Z$ interchangeably as arguments to $T$ and $U$).

In principle, if we had unlimited computational resources (or a way of analytically simplifying the problem) we could simply reject when $T(X)$ is above its conditional $\alpha$ quantile; or equivalently, we reject for small values of the corresponding $p$-value
$$
p(x,y \mid u) = \PP_{H_0}(T(X,Y) \geq T(x,y) \mid U(X,Y) = u) = \frac{1}{(n+m)!}\sum_{\pi \in \mathcal{S}_{n+m}} 1\{T(\pi u) \geq T(x,y)\}.
$$
In practice, enumerating all $(n+m)!$ permutations is unnecessary, so we sample permutations to perform a **Monte Carlo test**: for $\pi_1,\ldots,\pi_B \simiid \text{Unif}(\mathcal{S}_{n+m})$, define the Monte Carlo $p$-value
$$
p = \frac{1}{B+1} \left(1 + \sum_{b=1}^B 1\left\{T(\pi_b u) \geq T(x,y)\right\}\right).
$$
This test is exact: if we let $\pi_0$ denote the permutation for which $\pi_0u = (x,y)$, then under $H_0$, $\pi_0,\pi_1,\ldots,\pi_B$ are i.i.d. draws from $\mathcal{S}_{n+m}$, so $(x,y)=\pi_0 u$ has exactly the same chance to give the largest test statistic as every other permutation has.

Note that usually permutation tests are defined by randomly permutating $(x,y)$, rather than randomly permuting $u$; this is equivalent, since $\tilde\pi_b = \pi_b \circ \pi_0^{-1}$ are also i.i.d. draws from $\mathcal{S}_{n+m}$.

::: callout
It is worth noting that the concept of a Monte Carlo test can be applied to any situation where we prefer to sample $B$ values from the null distribution rather than directly calculate an exact quantile. There are very interesting extensions to Markov Chain Monte Carlo, that allow us to perform *exact* tests even when we cannot sample
:::

Crucially, $U(Z)$ is *not* sufficient for $Z$ under the *full* model where $P$ and $Q$ vary arbitrarily. Suppose we instead conditioned on the order statistics of each sample separately:
$$
V(X,Y) = (X_{(1)},\ldots,X_{(n)},Y_{(1)},\ldots,Y_{(m)}).
$$
Then, the distribution of $(X,Y)$ given $V$ would be fully known under the null or the alternative: we would have conditioned away the distinction between the null and the alternative, rendering the entire model a singleton. This is *not* what we want to do: whereas conditioning on $U$ and collapsing the null hypothesis to a singleton is convenient, conditioning on $V$ and collapsing the entire model to a singleton renders the data useless.

---

[← Multiparameter exponential families](03-multiparameter-exponential-families.md) · [Up: contents](index.md)
