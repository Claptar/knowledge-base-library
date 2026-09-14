---
title: Densities {.anchored anchor-id="densities"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/measure-theory-basics.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/measure-theory-basics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Densities {.anchored anchor-id="densities"}

**Source:** [`units/reader/measure-theory-basics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/measure-theory-basics.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We have just seen in the last two examples that there is a special relationship between the Lebesgue measure <span class="math inline">\$\\lambda\$</span> on <span class="math inline">\$\\RR\$</span> and the Gaussian measure <span class="math inline">\$P\_Z\$</span>, allowing us to evaluate integrals with respect to <span class="math inline">\$P\$</span> by turning them into integrals with respect to <span class="math inline">\$\\lambda\$</span>, namely <span class="math inline">\$\\int f(x)\\td P\_Z(x) = \\int f(x)\\phi(x) \\td\\lambda(x)\$</span>.

This is a happy fact, since mathematicians have gone to a lot of trouble figuring out how to calculate integrals with respect to the usual (Lebesgue) measure. Most of the expectations we want to calculate in statistics are integrals with respect to some joint probability measure over random variables, and we certainly wouldn’t want to have to reinvent the wheel of integration every time we want to do calculations with respect to a new random variable.

Note that we can’t turn integrals for every random variable into Lebesgue integrals. If <span class="math inline">\$Y\$</span> follows a binomial distribution, for example, we can just as well define <span class="math inline">\$P\_Y(A) = \\PP(Y \\in A)\$</span>, but there is no counterpart to <span class="math inline">\$\\phi\$</span> that would let us turn <span class="math inline">\$P\_Y\$</span> integrals into Lebesgue integrals in the same way.

Formally, consider a measurable space <span class="math inline">\$(\\cX, \\cF)\$</span>, with two measures <span class="math inline">\$P\$</span> and <span class="math inline">\$\\mu\$</span>. We say <span class="math inline">\$P\$</span> is *absolutely continuous* *with respect to* <span class="math inline">\$\\mu\$</span> if <span class="math inline">\$P(A) = 0\$</span> whenever <span class="math inline">\$\\mu(A) = 0\$</span>. In notation, we write <span class="math inline">\$P \\ll \\mu\$</span>.

If <span class="math inline">\$P \\ll \\mu\$</span> then, [under mild conditions](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem), we can always define a *density function* <span class="math inline">\$p:\\cX \\mapsto $$0,\\infty)\$</span> such that

<span class="math display">\\\[ P(A) = \\int 1\_A(x) p(x)\\td\\mu(x), \\quad \\text{ for all } A \\in \\cF, \\$$</span>

and by extension <span class="math inline">\$\\int f(x)\\td P(x) = \\int f(x) p(x) \\td\\mu(x)\$</span>.

The function <span class="math inline">\$p\$</span> is called the *density function* or *Radon-Nikodym derivative* of <span class="math inline">\$P\$</span> with respect to <span class="math inline">\$\\mu\$</span>. It is sometimes written using the suggestive notation <span class="math inline">\$\\frac{\\td P}{\\td\\mu}(x)\$</span>. Whenever we have a density function we can turn integrals with respect to <span class="math inline">\$P\$</span> into integrals with respect to <span class="math inline">\$\\mu\$</span> simply by multiplying the integrand by <span class="math inline">\$p\$</span>.

If we do not specify what <span class="math inline">\$\\mu\$</span> is, it is assumed to be the Lebesgue measure; that is, if we say <span class="math inline">\$P\$</span> is *absolutely continuous* with no further elaboration, we mean <span class="math inline">\$P \\ll \\lambda\$</span>.

If <span class="math inline">\$P\$</span> is a probability measure, we call <span class="math inline">\$p(x)\$</span> its *probability density function (with respect to* <span class="math inline">\$\\mu\$</span>). If <span class="math inline">\$\\mu\$</span> is a counting measure, we call <span class="math inline">\$p(x)\$</span> its *probability mass function*. These are abbreviated pdf and pmf, respectively.

---

[← Integrals {.anchored anchor-id="integrals"}](04-integrals-anchored-anchor-id-integrals.md) · [Up: contents](index.md) · [Measure theory basics Part 06 — →](06-measure-theory-basics-part-06.md)
