---
title: Conditional probability
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/measure-theory-basics.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/measure-theory-basics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/measure-theory-basics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/measure-theory-basics.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Conditional probability

While it is beyond the scope of this course, measure theory also allows us to patch the definition of conditional probability and conditional expectation. Given two events $A$ and $B$, if $\PP(B) > 0$, we can unproblematically define the conditional probability of $A$ given $B$ as $\PP(A \mid B) = \PP(A \cap B) / \PP(B)$, but this definition obviously fails when $\PP(B) = 0$.

Generally speaking, we cannot necessarily define $\PP(A \mid B)$ for measure zero events $B$ (Homework 0 includes a problem illustrating the inherent ambiguity of this definition). But, for example, if $X$ and $Y$ are both continuous random variables with some dependence between them we would like to be able to discuss, e.g., the distribution or expectation of $Y$ given that $X$ takes on some specific value $x$. We can do this by defining the conditional expectation $\EE(Y \mid X)$ as a *random variable* $g(X)$, which has the property $\EE[(Y - g(X)) 1_A(X)] = 0$ for all (nice) subsets $A$. By evaluating this function $g$ at $x$ we can answer the question we asked earlier. However, note this explanation is informal and brushes many important points under the rug; for a more complete explanation, take Stat 205A.

Having defined the conditional expectation, we can also ask about the conditional distribution of $Y$ by evaluating the conditional expectation on new random variables defined with indicator functions: $\PP(Y \in A \mid X) = \EE[1_A(Y) \mid X]$ .

## More definitions {.anchored anchor-id="more-definitions"}

Finally, this section includes some scattered definitions to remind you of a few more useful definitions which you likely have already seen in your previous probability courses.

If $\PP(A) = 1$, we say $A$ occurs *almost surely*.

The variance of a random variable $X$ is $\textrm{Var}(X) = \EE[X^2] - \EE [X]$

See Keener Ch. 1 for more on probability.

---

[← Probability spaces and random variables](05-probability-spaces-and-random-variables.md) · [Up: contents](index.md)
