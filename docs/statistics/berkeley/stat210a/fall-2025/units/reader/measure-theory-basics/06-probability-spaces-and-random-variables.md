---
title: Probability spaces and random variables
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/measure-theory-basics.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/measure-theory-basics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Probability spaces and random variables

**Source:** [`units/reader/measure-theory-basics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/measure-theory-basics.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

A typical statistics problem involves many, random variables of various types (e.g. some discrete and some continuous random variables), some of which may be functions of others. The overall joint distribution is defined implicitly by specifying the variables’ relationships to one another, or giving some sequence of rules for how they are all generated. We will want to ask about probabilities of events that involve functions of multiple random variables, e.g. a natural question to ask in a simple variance estimation problem with i.i.d. random variables <span class="math inline">\$X\_1,\\ldots,X\_n\$</span> might be “what is the probability that <span class="math inline">\$\\left\|\\frac{1}{n-1}\\sum\_{i=1}^n \\left(X\_i - \\overline X\\right)^2 - \\sigma^2\\right\| &lt; \\delta\$</span> ?”

The notation in the previous section doesn’t allow us to ask questions like this without, e.g., massaging the above event into the set of <span class="math inline">\$(X\_1,\\ldots,X\_n)\$</span> vectors for which the event would hold. This would become even more difficult in more complicated setups.

Instead of trying to work directly with the measure corresponding to the joint distribution of all of the random variables involved, it can be convenient to instead think of the variables as all being functions of some abstract “outcome” <span class="math inline">\$\\omega\$</span> that encompasses all of the randomness in the problem. We introduce an abstract probability space <span class="math inline">\$(\\Omega, \\cF, \\PP)\$</span> where

- <span class="math inline">\$\\omega \\in \\Omega\$</span> is called an *outcome*,

- <span class="math inline">\$A \\in \\cF\$</span> is called an *event*,

- <span class="math inline">\$\\PP(A)\$</span> is called the *probability of* <span class="math inline">\$A\$</span>.

Then a *random variable* is any (nice enough) function <span class="math inline">\$X:\\; \\Omega \\to \\cX\$</span>. We say <span class="math inline">\$X\$</span> has *distribution* <span class="math inline">\$P\$</span>, and write <span class="math inline">\$X \\sim P\$</span>, if

<span class="math display">\\$$ \\PP(X \\in B) = \\PP(\\{\\omega:\\; X(\\omega) \\in B\\}) = P(B). \\$$</span>We say the real-valued random variable <span class="math inline">\$X\$</span> is *continuous* if its distribution is absolutely continuous (with respect to the Lebesgue meaure). If <span class="math inline">\$X\$</span> is a random variable, then <span class="math inline">\$f(X)\$</span> is also a random variable for any (nice enough) function <span class="math inline">\$f\$</span>.

Likewise, the *expectation* of a random variable is defined as an integral with respect to <span class="math inline">\$\\PP\$</span>:

<span class="math display">\\$$ \\EE\[X$$ = \\int X(\\omega) \\td\\PP(\\omega), \\quad \\text{ and } \\quad \\EE$$f(X,Y)$$ = \\int f(X(\\omega), Y(\\omega)) \\td\\PP(\\omega). \\\]</span>

Usually, to do real calculations we will eventually boil <span class="math inline">\$\\PP\$</span> or <span class="math inline">\$\\EE\$</span> into a composition of integrals and/or sums.

---

[← Densities](05-densities.md) · [Up: contents](index.md) · [Conditional probability →](07-conditional-probability.md)
