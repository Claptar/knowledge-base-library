---
title: Use in Industry and Research
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html
source_file: sources/berkeley-stat158/spring-2026/27-sequential-analysis/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Use in Industry and Research

**Source:** [`27-sequential-analysis/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Uses of Modern Sequential Testing

Platforms like [Statsig](https://www.statsig.com/) implement the SPRT and it is quite easy to use.

## AI Deployment Monitoring

<figure>

</figure>

<figure>

</figure>

- Monitor model quality after deployment
- Detect regressions in real time, no fixed <span class="math inline">\$n\$</span>

## Early Stopping for Clinical Trials

- Stop early for efficacy or futility
- FDA recommends ***group sequential designs*** [FDA Guidance](https://www.fda.gov/media/78495/download)
- We discuss Group Sequential Designs in future slides

## From Testing to Confidence Sequences

- We’ve been talking about hypothesis testing
- Can we use confidence intervals?

## Gaussian Example

You have a dataset <span class="math inline">\$X\_1, X\_2, \\ldots, X\_n \\sim N(\\mu, 1)\$</span>. You calculate <span class="math display">\\$$ \\dot C\_n(X\_1, \\ldots, X\_n) = \\hat \\mu \\pm \\frac{1.96}{\\sqrt{n}} = \[1.5, 5$$ \\\]</span> Can you reject the null <span class="math inline">\$\\mu = 0\$</span>?

What if you observe a sequence of data <span class="math inline">\$X\_1, X\_2, \\ldots \\sim N(\\mu, 1)\$</span>. You construct <span class="math inline">\$\\dot C\_1, \\dot C\_2, \\ldots \\dot C\_{67}\$</span>. <span class="math display">\\$$ 0 \\in \\dot C\_i, \\forall i &lt; 67 \\quad \\text{ but } 0 \\not \\in \\dot C\_{67}. \\$$</span> Can you stop at 67 and reject the null that <span class="math inline">\$\\mu = 0\$</span>.

---

[← calculate beta](05-calculate-beta.md) · [Up: contents](index.md) · [Confidence Sequences →](07-confidence-sequences.md)
