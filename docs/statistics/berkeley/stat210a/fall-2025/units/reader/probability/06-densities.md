---
title: Densities
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/probability.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Densities

**Source:** [`units/reader/probability.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We have just seen in the last two examples that there is a special relationship between the Lebesgue measure <span class="math inline">\$\\lambda\$</span> on <span class="math inline">\$\\RR\$</span> and the Gaussian measure <span class="math inline">\$P\_Z\$</span>, allowing us to evaluate integrals with respect to <span class="math inline">\$P\_Z\$</span> by turning them into integrals with respect to <span class="math inline">\$\\lambda\$</span>, namely <span class="math inline">\$\\int f(x)\\,d P\_Z(x) = \\int f(x)\\phi(x) \\,d\\lambda(x)\$</span>.

This is a happy fact: mathematicians have gone to a lot of trouble figuring out how to calculate Lebesgue integrals of various functions, and it’s nice not to have to reinvent the wheel!

Note that we can’t turn integrals for every random variable into Lebesgue integrals. If <span class="math inline">\$Y\$</span> follows a binomial distribution, for example, we can just as well define a probability measure <span class="math inline">\$P\_Y(A) = \\PP(Y \\in A)\$</span>, but there is no counterpart to <span class="math inline">\$\\phi\$</span> that would let us turn <span class="math inline">\$P\_Y\$</span> integrals into Lebesgue integrals in the same way.

Formally, consider a measurable space <span class="math inline">\$(\\cX, \\cF)\$</span>, with two measures <span class="math inline">\$P\$</span> and <span class="math inline">\$\\mu\$</span>. We say <span class="math inline">\$P\$</span> is *absolutely continuous with respect to* <span class="math inline">\$\\mu\$</span> if <span class="math inline">\$P(A) = 0\$</span> whenever <span class="math inline">\$\\mu(A) = 0\$</span>. In notation, we write <span class="math inline">\$P \\ll \\mu\$</span>.

If <span class="math inline">\$P \\ll \\mu\$</span> then, [under mild conditions](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem), we can always define a *density function* <span class="math inline">\$p:\\cX \\mapsto $$0,\\infty)\$</span> such that

<span class="math display">\\\[ P(A) = \\int 1\_A(x) p(x)\\,d\\mu(x), \\quad \\text{ for all } A \\in \\cF, \\$$</span>

and by extension <span class="math inline">\$\\int f(x)\\,d P(x) = \\int f(x) p(x) \\,d\\mu(x)\$</span>.

The function <span class="math inline">\$p\$</span> is called the *density function* or *Radon-Nikodym derivative* of <span class="math inline">\$P\$</span> with respect to <span class="math inline">\$\\mu\$</span>. It is sometimes written using the suggestive notation <span class="math inline">\$\\frac{\\,d P}{\\,d\\mu}(x)\$</span>. Whenever we have a density function we can turn integrals with respect to <span class="math inline">\$P\$</span> into integrals with respect to <span class="math inline">\$\\mu\$</span> simply by multiplying the density <span class="math inline">\$p\$</span> into the integrand.

If we do not specify what <span class="math inline">\$\\mu\$</span> is, it is assumed to be the Lebesgue measure; that is, if we say <span class="math inline">\$P\$</span> is *absolutely continuous* with no further elaboration, we mean <span class="math inline">\$P \\ll \\lambda\$</span>.

If <span class="math inline">\$P\$</span> is a probability measure and <span class="math inline">\$\\mu\$</span> is the Lebesgue measure, then <span class="math inline">\$p(x)\$</span> is a probability density function (pdf). If <span class="math inline">\$\\mu\$</span> is a counting measure, we call <span class="math inline">\$p(x)\$</span> the probability mass function (pmf).

---

[← Integrals](05-integrals.md) · [Up: contents](index.md) · [Probability spaces and random variables →](07-probability-spaces-and-random-variables.md)
