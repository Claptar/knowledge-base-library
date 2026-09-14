---
title: Probability spaces and random variables
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/probability.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Probability spaces and random variables

**Source:** [`units/reader/probability.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

In a typical statistics problem we may have multiple random variables, some continuous and some discrete, some random variables may be functions of others, and we want to have good notation for the probability that “something happens,” like <span class="math inline">\$\\PP(X^2 &lt; (Y+Z)/ W)\$</span>, or the expectation of a random variable, like <span class="math inline">\$\\EE$$(XY-ZW)^2$$\$</span>. What does this kind of expression have to do with the measures and integrals we have been discussing so far?

If we defined a probability measure <span class="math inline">\$P\$</span> as the joint distribution of <span class="math inline">\$(X, Y, Z, W)\$</span> then we could evaluate <span class="math inline">\$P\$</span> on the corresponding subset of the sample space, e.g. <span class="math inline">\$P(\\{x,y,z,w :\\; x^2 &lt; (y+z)/w\\})\$</span>. Or we could write an appropriate integral like <span class="math inline">\$\\int (xy-zw)^2\\,dP(x,y,z,w)\$</span>. But it is convenient not to have to make things so explicit. To this end, we can introduce the idea of an *abstract outcome* <span class="math inline">\$\\omega\$</span> in an *outcome space* <span class="math inline">\$\\Omega\$</span>, which informally represents “all of the information required to evaluate every random variable in the problem.” Then a *random variable* is simply any function of <span class="math inline">\$\\omega\$</span>, and we can think of <span class="math inline">\$\\PP\$</span> as a measure on <span class="math inline">\$\\Omega\$</span> and <span class="math inline">\$\\EE\$</span> as an integral with respect to <span class="math inline">\$\\PP\$</span>. Then our usual way of writing probabilities and expectations become shorthand for the corresponding measure and integral over <span class="math inline">\$\\Omega\$</span>; e.g. <span class="math display">\\$$\\PP(X^2 &lt; (Y+Z)/W) = \\PP\\left(\\{\\omega \\in \\Omega:\\; X(\\omega)^2 &lt; (Y(\\omega) + Z(\\omega))/W(\\omega)\\}\\right),\\$$</span> and <span class="math display">\\$$\\EE((XY-ZW)^2) = \\int\_\\Omega (X(\\omega)Y(\\omega) - Z(\\omega)W(\\omega))^2 \\,d\\PP(\\omega),\\$$</span> and it is understood that we will never bother to make explicit what kind of object <span class="math inline">\$\\omega\$</span> is. A subset of <span class="math inline">\$\\Omega\$</span> to which <span class="math inline">\$\\PP\$</span> assigns a probability is called an *event* and any function of <span class="math inline">\$\\omega\$</span> is a *random variable*. If <span class="math inline">\$\\PP(A) = 1\$</span>, we say <span class="math inline">\$A\$</span> occurs *almost surely*.

To do actual calculations of probabilities and expectations we use the distributions of the random variables involved in that particular calculation. The distribution of a random variable <span class="math inline">\$X(\\omega)\$</span> is given by the *push-forward* measure defined as <span class="math inline">\$Q = \\PP \\circ X^{-1}\$</span>. That is, if <span class="math inline">\$X\$</span> has realizations in the sample space <span class="math inline">\$\\cX\$</span>, and <span class="math inline">\$B\$</span> is a (measurable) subset of <span class="math inline">\$\\cX\$</span>, then <span class="math display">\\$$Q(B) = \\PP(X^{-1}(B)) = \\PP(\\{\\omega \\in \\Omega:\\; X(\\omega) \\in B \\}).\\$$</span>

---

[← Densities](06-densities.md) · [Up: contents](index.md) · [Conditional probability →](08-conditional-probability.md)
