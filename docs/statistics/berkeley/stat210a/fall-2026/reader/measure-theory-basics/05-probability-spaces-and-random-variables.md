---
title: Probability spaces and random variables
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/measure-theory-basics.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/measure-theory-basics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Probability spaces and random variables

**Source:** [`reader/measure-theory-basics.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/measure-theory-basics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

A typical statistics problem involves many, random variables of various types (e.g. some discrete and some continuous random variables), some of which may be functions of others. The overall joint distribution is defined implicitly by specifying the variables' relationships to one another, or giving some sequence of rules for how they are all generated. We will want to ask about probabilities of events that involve functions of multiple random variables, e.g. a natural question to ask in a simple variance estimation problem with i.i.d. random variables $X_1,\ldots,X_n$ might be "what is the probability that $\left|\frac{1}{n-1}\sum_{i=1}^n \left(X_i - \overline X\right)^2 - \sigma^2\right| < \delta$ ?"

The notation in the previous section doesn't allow us to ask questions like this without, e.g., massaging the above event into the set of $(X_1,\ldots,X_n)$ vectors for which the event would hold. This would become even more difficult in more complicated setups.

Instead of trying to work directly with the measure corresponding to the joint distribution of all of the random variables involved, it can be convenient to instead think of the variables as all being functions of some abstract "outcome" $\omega$ that encompasses all of the randomness in the problem. We introduce an abstract probability space $(\Omega, \cF, \PP)$ where

-   $\omega \in \Omega$ is called an *outcome*,

-   $A \in \cF$ is called an *event*,

-   $\PP(A)$ is called the *probability of* $A$.

Then a *random variable* is any (nice enough) function $X:\; \Omega \to \cX$. We say $X$ has *distribution* $P$, and write $X \sim P$, if

$$
\PP(X \in B) = \PP(\{\omega:\; X(\omega) \in B\}) = P(B).
$$We say the real-valued random variable $X$ is *continuous* if its distribution is absolutely continuous (with respect to the Lebesgue meaure). If $X$ is a random variable, then $f(X)$ is also a random variable for any (nice enough) function $f$.

Likewise, the *expectation* of a random variable is defined as an integral with respect to $\PP$:

$$
\EE[X] = \int X(\omega) \td\PP(\omega), \quad \text{ and } \quad \EE[f(X,Y)] = \int f(X(\omega), Y(\omega)) \td\PP(\omega).
$$

Usually, to do real calculations we will eventually boil $\PP$ or $\EE$ into a composition of integrals and/or sums.

---

[← Densities](04-densities.md) · [Up: contents](index.md) · [Conditional probability →](06-conditional-probability.md)
