---
title: Densities
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/probability.html
source_file: sources/berkeley-stat210a/fall-2025/reader/probability.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/probability.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/probability.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Densities

We have just seen in the last two examples that there is a special relationship between the Lebesgue measure $\lambda$ on $\RR$ and the Gaussian measure $P_Z$, allowing us to evaluate integrals with respect to $P_Z$ by turning them into integrals with respect to $\lambda$, namely $\int f(x)\,d P_Z(x) = \int f(x)\phi(x) \,d\lambda(x)$.

This is a happy fact: mathematicians have gone to a lot of trouble figuring out how to calculate Lebesgue integrals of various functions, and it’s nice not to have to reinvent the wheel!

Note that we can’t turn integrals for every random variable into Lebesgue integrals. If $Y$ follows a binomial distribution, for example, we can just as well define a probability measure $P_Y(A) = \PP(Y \in A)$, but there is no counterpart to $\phi$ that would let us turn $P_Y$ integrals into Lebesgue integrals in the same way.

Formally, consider a measurable space $(\cX, \cF)$, with two measures $P$ and $\mu$. We say $P$ is *absolutely continuous with respect to* $\mu$ if $P(A) = 0$ whenever $\mu(A) = 0$. In notation, we write $P \ll \mu$.

If $P \ll \mu$ then, [under mild conditions](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem), we can always define a *density function* $p:\cX \mapsto [0,\infty)$ such that

$$
P(A) = \int 1_A(x) p(x)\,d\mu(x), \quad \text{ for all } A \in \cF,
$$

and by extension $\int f(x)\,d P(x) = \int f(x) p(x) \,d\mu(x)$.

The function $p$ is called the *density function* or *Radon-Nikodym derivative* of $P$ with respect to $\mu$. It is sometimes written using the suggestive notation $\frac{\,d P}{\,d\mu}(x)$. Whenever we have a density function we can turn integrals with respect to $P$ into integrals with respect to $\mu$ simply by multiplying the density $p$ into the integrand.

If we do not specify what $\mu$ is, it is assumed to be the Lebesgue measure; that is, if we say $P$ is *absolutely continuous* without elaborating further, we mean $P \ll \lambda$.

If $P$ is a probability measure and $\mu$ is the Lebesgue measure, then $p(x)$ is a probability density function (pdf). If $\mu$ is a counting measure, we call $p(x)$ the probability mass function (pmf).

---

[← Integrals](04-integrals.md) · [Up: contents](index.md) · [Probability spaces and random variables →](06-probability-spaces-and-random-variables.md)
