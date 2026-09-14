---
title: Blocking and Variance {#blocking-and-variance .title}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/20-blocking-and-variance/slides.html
source_file: sources/berkeley-stat158/spring-2026/20-blocking-and-variance/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Blocking and Variance {#blocking-and-variance .title}

**Source:** [`20-blocking-and-variance/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/20-blocking-and-variance/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Preliminaries

Let <span class="math inline">\$g\_1\$</span> be a random subset of <span class="math inline">\$\\{1, \\ldots, n\\}\$</span> of size <span class="math inline">\$n\_1\$</span> that gets the treatment. Let <span class="math inline">\$g\_0\$</span> be a random subset of <span class="math inline">\$\\{1, \\ldots, n\\}\$</span> with <span class="math inline">\$n\_0\$</span> elements disjoint from <span class="math inline">\$g\_1\$</span> that gets the control. <sup>1</sup>

We estimate the population means with the sample means

<span class="math display">\\$$ \\hat{\\bar{Y}}\_1 = \\frac{1}{n\_1} \\sum\_{i \\in g\_1} Y\_i(1) \\quad \\quad \\quad \\hat{\\bar{Y}}\_0 = \\frac{1}{n\_0} \\sum\_{i \\in g\_0} Y\_i(0) \\$$</span>

with variance and covariance

<span class="math display">\\$$ Var(\\hat{\\bar{Y}}\_1) = \\frac{n - n\_1}{n - 1} \\frac{\\sigma\_1^2}{n\_1} \\quad \\quad Var(\\hat{\\bar{Y}}\_0) = \\frac{n - n\_0}{n - 1} \\frac{\\sigma\_0^2}{n\_0} \\$$</span>

<span class="math display">\\$$ Cov(\\hat{\\bar{Y}}\_1, \\hat{\\bar{Y}}\_0) = -\\frac{1}{n - 1}Cov(Y\_i(1), Y\_i(0)) \\$$</span>

Intuition behind what Cov(Y\_i(1), Y\_i(0)) is measuring: it’s linked to out heterogenous the treatment effects are.

- if its very positive: units with high Y(1) also have high Y(0) and units with low Y(1) also have low Y(0). This is a setting where there are fairly constant treatment effects across units. Example: an educational intervention that adds roughly +5 points to everyone’s test score.
- if its near zero: treatment effects are very heterogenous. Example: some students benefit a lot from a tutoring program, others not at all.
- if its very negative: the ordering of units in terms of their potential outcomes is reversed. Example: a drug that helps some people but harms others, and the people it helps are the ones who would have had the worst outcomes under control.

The reason the covariance of the averages has the opposite sign of the covariance of the potential outcomes is because of the random assignment. Units with high Y(1) appearing in the treatment group means they cannot appear in the control group, which flips the sign.

<style type="text/css">
        span.MJX_Assistive_MathML {
          position:absolute!important;
          clip: rect(1px, 1px, 1px, 1px);
          padding: 1px 0 0 0!important;
          border: 0!important;
          height: 1px!important;
          width: 1px!important;
          overflow: hidden!important;
          display:block!important;
      }</style>

1.  From appendix of *Statistics* 4<sup>th</sup> Edition by Freedman, Pisani, and Purves (2008).

---

[Up: contents](index.md) · [Completely Randomized Design \$CR$$1$$\$ →](02-completely-randomized-design.md)
