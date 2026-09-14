---
title: Hierarchical bayes Part 03 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hierarchical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Hierarchical bayes Part 03 —

**Source:** [`units/reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Hierarchical models are very flexible, but often create big computational headaches:

<span class="math display">\\$$ \\pi(\\theta\|x) = \\frac{p(x\|\\theta)\\pi(\\theta)}{\\int p(x\|\\theta)\\pi(\\theta)d\\theta} \\$$</span>

Numerator is usually nice, denominator often intractable.

Computational strategy: Set up a Markov chain with stationary distribution <span class="math inline">\$\\pi(\\theta\|x)\$</span>, run it to get approximate samples from <span class="math inline">\$\\pi(\\theta\|x)\$</span>.

### <span class="header-section-number">2.1</span> Definition of Markov Chain {.anchored number="2.1" anchor-id="definition-of-markov-chain"}

A stationary Markov chain with transition kernel <span class="math inline">\$Q(y\|x)\$</span> and initial distribution <span class="math inline">\$\\pi\_0(x)\$</span> is a sequence of r.v.’s <span class="math inline">\$X\_0, X\_1, \\ldots\$</span> where <span class="math inline">\$X\_0 \\sim \\pi\_0\$</span> and:

<span class="math display">\\$$ P(X\_{t+1} \\in A \| X\_t, \\ldots, X\_0) = P(X\_{t+1} \\in A \| X\_t) = \\int\_A Q(y\|X\_t) dy \\$$</span>

Marginal distribution of <span class="math inline">\$X\_t\$</span>:

<span class="math display">\\$$ \\pi\_t(y) = P(X\_t \\in A) = \\int Q(y\|x)\\pi\_{t-1}(x) dx \\$$</span>

This is a directed graphical model: <span class="math inline">\$X\_0 \\to X\_1 \\to X\_2 \\to \\cdots\$</span>

If <span class="math inline">\$\\pi(y) = \\int Q(y\|x)\\pi(x) dx\$</span>, we say <span class="math inline">\$\\pi\$</span> is a stationary distribution for <span class="math inline">\$Q\$</span>.

A sufficient condition is detailed balance:

<span class="math display">\\$$ \\pi(x)Q(y\|x) = \\pi(y)Q(x\|y) \\$$</span>

<span class="math display">\\$$ \\int\_y Q(y\|x)\\pi(x) dx = \\int\_y \\pi(y)Q(x\|y) dy = \\pi(y) \\$$</span>

A Markov chain with detailed balance is called reversible: <span class="math inline">\$X\_{t-1} \| X\_t \\sim X\_{t+1} \| X\_t\$</span> if <span class="math inline">\$\\pi\_t = \\pi\$</span>.

### <span class="header-section-number">2.2</span> Theory {.anchored number="2.2" anchor-id="theory"}

If a Markov chain with stationary distribution <span class="math inline">\$\\pi\$</span> is:

1.  Irreducible: <span class="math inline">\$\\forall x,y, \\exists n: P(X\_n = y \| X\_0 = x) &gt; 0\$</span>
2.  Aperiodic: <span class="math inline">\$\\forall x, \\gcd\\{n &gt; 0: P(X\_n = x \| X\_0 = x) &gt; 0\\} = 1\$</span>

Then <span class="math inline">\$\\pi\_t \\to \\pi\$</span> in TV distance, regardless of <span class="math inline">\$\\pi\_0\$</span> (chain “forgets” <span class="math inline">\$\\pi\_0\$</span>).

Strategy: Find <span class="math inline">\$Q\$</span> with stationary distribution <span class="math inline">\$\\pi(\\theta\|x)\$</span>, start at any <span class="math inline">\$X\_0\$</span>, run chain for a long time, then <span class="math inline">\$X\_t\$</span> is approximately a sample from posterior for large <span class="math inline">\$t\$</span>.

---

[← 1 Hierarchical Bayes {.anchored number="1" anchor-id="hierarchical-bayes"}](02-1-hierarchical-bayes-anchored-number-1-anchor-id-hierarchica.md) · [Up: contents](index.md) · [3 Gibbs Sampler {.anchored number="3" anchor-id="gibbs-sampler"} →](04-3-gibbs-sampler-anchored-number-3-anchor-id-gibbs-sampler.md)
