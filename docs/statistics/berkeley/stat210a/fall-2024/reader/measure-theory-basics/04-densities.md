---
title: Densities
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/measure-theory-basics.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/measure-theory-basics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Densities

**Source:** [`reader/measure-theory-basics.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/measure-theory-basics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We have just seen in the last two examples that there is a special relationship between the Lebesgue measure $\lambda$ on $\RR$ and the Gaussian measure $P_Z$, allowing us to evaluate integrals with respect to $P$ by turning them into integrals with respect to $\lambda$, namely $\int f(x)\td P_Z(x) = \int f(x)\phi(x) \td\lambda(x)$.

This is a happy fact, since mathematicians have gone to a lot of trouble figuring out how to calculate integrals with respect to the usual (Lebesgue) measure. Most of the expectations we want to calculate in statistics are integrals with respect to some joint probability measure over random variables, and we certainly wouldn't want to have to reinvent the wheel of integration every time we want to do calculations with respect to a new random variable.

Note that we can't turn integrals for every random variable into Lebesgue integrals. If $Y$ follows a binomial distribution, for example, we can just as well define $P_Y(A) = \PP(Y \in A)$, but there is no counterpart to $\phi$ that would let us turn $P_Y$ integrals into Lebesgue integrals in the same way.

Formally, consider a measurable space $(\cX, \cF)$, with two measures $P$ and $\mu$. We say $P$ is *absolutely continuous* *with respect to* $\mu$ if $P(A) = 0$ whenever $\mu(A) = 0$. In notation, we write $P \ll \mu$.

If $P \ll \mu$ then, [under mild conditions](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem), we can always define a *density function* $p:\cX \mapsto [0,\infty)$ such that

$$
P(A) = \int 1_A(x) p(x)\td\mu(x), \quad \text{ for all } A \in \cF,
$$

and by extension $\int f(x)\td P(x) = \int f(x) p(x) \td\mu(x)$.

The function $p$ is called the *density function* or *Radon-Nikodym derivative* of $P$ with respect to $\mu$. It is sometimes written using the suggestive notation $\frac{\td P}{\td\mu}(x)$. Whenever we have a density function we can turn integrals with respect to $P$ into integrals with respect to $\mu$ simply by multiplying the integrand by $p$.

If we do not specify what $\mu$ is, it is assumed to be the Lebesgue measure; that is, if we say $P$ is *absolutely continuous* with no further elaboration, we mean $P \ll \lambda$.

If $P$ is a probability measure, we call $p(x)$ its *probability density function (with respect to* $\mu$). If $\mu$ is a counting measure, we call $p(x)$ its *probability mass function*. These are abbreviated pdf and pmf, respectively.

---

[← Integrals](03-integrals.md) · [Up: contents](index.md) · [Probability spaces and random variables →](05-probability-spaces-and-random-variables.md)
