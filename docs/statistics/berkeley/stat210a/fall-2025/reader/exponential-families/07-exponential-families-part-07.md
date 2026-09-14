---
title: Exponential families Part 07 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/exponential-families.html
source_file: sources/berkeley-stat210a/fall-2025/reader/exponential-families.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Exponential families Part 07 —

**Source:** [`reader/exponential-families.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/exponential-families.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

One of the most important properties of exponential families is that a large sample can be summarized by a low-dimensional statistic. Suppose we observe a vector of observations <span class="math inline">\$X = (X\_1,\\ldots,X\_n)\$</span> representing an independent and identically distributed (i.i.d.) sample from an exponential family. Let <span class="math inline">\$p\_\\eta^{(1)\$</span> denote the density for a single observation:

<span class="math display">\\$$ X\_1\\ldots,X\_n \\simiid p\_\\eta^{(1)}(x) = e^{\\eta'T(x) - A(\\eta)}h(x). \\$$</span>

Then the random vector <span class="math inline">\$X = (X\_1,\\ldots,X\_n)\$</span> follows another closely related exponential family:

<span class="math display">\\$$ \\begin{aligned} p\_\\eta(x) &= \\prod\_{i=1}^n e^{\\eta'T(x\_i) - A(\\eta)}h(x\_i)\\\\\[7pt$$ &= \\exp\\left\\{\\eta'\\sum\_{i=1}^n T(x\_i) - nA(\\eta)\\right\\} \\prod\_{i=1}^n h(x\_i). \\end{aligned} \\\]</span>

This new density <span class="math inline">\$p\_\\eta\$</span>, which governs the distribution of the entire sample, is an exponential family with the same natural parameter as before, sufficient statistic <span class="math inline">\$\\sum\_i T(X\_i)\$</span>, carrier density <span class="math inline">\$\\prod\_i h(x\_i)\$</span>, and log-partition function <span class="math inline">\$nA(\\eta)\$</span>.

For reasons that will become clearer in the next lecture, it is very significant that the sufficient statistic does not increase in dimension as the sample size grows. This means that the <span class="math inline">\$s\$</span>-dimensional vector <span class="math inline">\$\\sum\_i T(X\_i)\$</span> is for all intents and purposes a complete summary of the entire sample, no matter how large <span class="math inline">\$n\$</span> is.

---

[← Exponential families Part 06 —](06-exponential-families-part-06.md) · [Up: contents](index.md)
