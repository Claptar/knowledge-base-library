---
title: Probability spaces and random variables
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/probability.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/probability.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Probability spaces and random variables

**Source:** [`reader/probability.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/probability.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

In a typical statistics problem we may have multiple random variables, some continuous and some discrete, some random variables may be functions of others, and we want to have good notation for the probability that "something happens," like $\PP(X^2 < (Y+Z)/ W)$, or the expectation of a random variable, like $\EE[(XY-ZW)^2]$. What does this kind of expression have to do with the measures and integrals we have been discussing so far?

If we defined a probability measure $P$ as the joint distribution of $(X, Y, Z, W)$ then we could evaluate $P$ on the corresponding subset of the sample space, e.g. $P(\{x,y,z,w :\; x^2 < (y+z)/w\})$. Or we could write an appropriate integral like $\int (xy-zw)^2\,dP(x,y,z,w)$. But it is convenient not to have to make things so explicit. To this end, we can introduce the idea of an *abstract outcome* $\omega$ in an *outcome space* $\Omega$, which informally represents "all of the information required to evaluate every random variable in the problem." Then a *random variable* is simply any function of $\omega$, and we can think of $\PP$ as a measure on $\Omega$ and $\EE$ as an integral with respect to $\PP$. Then our usual way of writing probabilities and expectations become shorthand for the corresponding measure and integral over $\Omega$; e.g. $$\PP(X^2 < (Y+Z)/W) = \PP\left(\{\omega \in \Omega:\; X(\omega)^2 < (Y(\omega) + Z(\omega))/W(\omega)\}\right),$$ and $$\EE((XY-ZW)^2) = \int_\Omega (X(\omega)Y(\omega) - Z(\omega)W(\omega))^2 \,d\PP(\omega),$$ and it is understood that we will never bother to make explicit what kind of object $\omega$ is. A subset of $\Omega$ to which $\PP$ assigns a probability is called an *event* and any function of $\omega$ is a *random variable*. If $\PP(A) = 1$, we say $A$ occurs *almost surely*.

To do actual calculations of probabilities and expectations we use the distributions of the random variables involved in that particular calculation. The distribution of a random variable $X(\omega)$ is given by the *push-forward* measure defined as $Q = \PP \circ X^{-1}$. That is, if $X$ has realizations in the sample space $\cX$, and $B$ is a (measurable) subset of $\cX$, then $$Q(B) = \PP(X^{-1}(B)) = \PP(\{\omega \in \Omega:\; X(\omega) \in B \}).$$

---

[← Densities](05-densities.md) · [Up: contents](index.md) · [Conditional probability →](07-conditional-probability.md)
