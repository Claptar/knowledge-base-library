---
title: 1 Bayes Risk and Bayes Estimator
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Bayes Risk and Bayes Estimator

**Source:** [`units/reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">1.1</span> Definitions {.anchored number="1.1" anchor-id="definitions"}

The Bayes risk is the average case risk:

<span class="math display">\\$$ r(\\pi, \\delta) = \\EE\_\\pi\[R(\\theta, \\delta)$$ = \\int R(\\theta, \\delta) \\,d\\pi(\\theta) \\\]</span>

where <span class="math inline">\$\\pi(\\theta)\$</span> is a probability measure (for now, we assume it’s proper; later we will allow it to be improper).

Note: <span class="math inline">\$\\pi\$</span> and <span class="math inline">\$\\delta\$</span> are functionally equivalent for average risk, which makes sense even if we don’t believe <span class="math inline">\$\\pi\$</span>.

<span class="math display">\\$$ r(\\pi, \\delta) = \\EE\_\\pi\[\\EE\_\\theta\[L(\\theta, \\delta(X))$$\] = \\EE$$L(\\theta, \\delta(X))$$ \\\]</span>

where <span class="math inline">\$(\\theta, X) \\sim p(\\theta, x) = p(x\|\\theta)\\pi(\\theta)\$</span>

An estimator <span class="math inline">\$\\delta\$</span> minimizing <span class="math inline">\$r\_\\text{Bayes}(\\delta)\$</span> is called a Bayes estimator. It depends on <span class="math inline">\$\\pi\$</span> and <span class="math inline">\$L\$</span>.

<span class="math display">\\$$ \\delta\_\\pi = \\argmin\_\\delta \\EE\[L(\\theta, \\delta(X))$$ \\\]</span>

### <span class="header-section-number">1.2</span> Prior and Posterior {.anchored number="1.2" anchor-id="prior-and-posterior"}

- The usual interpretation of <span class="math inline">\$\\pi\$</span> is the prior belief about <span class="math inline">\$\\theta\$</span> before seeing the data.
- The conditional distribution <span class="math inline">\$\\pi(\\theta\|X)\$</span> is called the posterior distribution (belief after seeing the data).

Densities: - Prior: <span class="math inline">\$\\pi(\\theta)\$</span> - Likelihood: <span class="math inline">\$p(x\|\\theta)\$</span> - Joint density: <span class="math inline">\$p(\\theta, x) = \\pi(\\theta)p(x\|\\theta)\$</span> - Marginal density: <span class="math inline">\$q(x) = \\int p(\\theta, x) \\,d\\theta\$</span> - Posterior density: <span class="math inline">\$\\pi(\\theta\|x) = \\frac{p(\\theta, x)}{q(x)}\$</span>

The Bayes estimator depends on the posterior:

<span class="math display">\\$$ \\delta\_\\pi(x) = \\argmin\_d \\EE\[L(\\theta, d)\|X=x$$ = \\argmin\_d \\int L(\\theta, d) \\pi(\\theta\|x) \\,d\\theta \\\]</span>

### <span class="header-section-number">1.3</span> Theorem: Characterization of Bayes Estimators {.anchored number="1.3" anchor-id="theorem-characterization-of-bayes-estimators"}

Suppose <span class="math inline">\$X \\sim p\_\\theta(x)\$</span> and <span class="math inline">\$\\delta\_\\pi(x) = \\delta(x)\$</span> for some function <span class="math inline">\$\\delta\$</span>. Then <span class="math inline">\$\\delta\$</span> is Bayes with respect to <span class="math inline">\$\\pi\$</span> if and only if <span class="math inline">\$\\delta(x) \\in \\argmin\_d \\EE$$L(\\theta, d)\|X=x$$\$</span> for almost every <span class="math inline">\$x\$</span>.

Proof: 1. Let <span class="math inline">\$\\delta'\$</span> be any other estimator. 2. <span class="math inline">\$r(\\pi, \\delta') = \\int \\EE$$L(\\theta, \\delta'(X))\|X=x$$ q(x) \\,dx\$</span> 3. <span class="math inline">\$r(\\pi, \\delta) = \\int \\EE$$L(\\theta, \\delta(X))\|X=x$$ q(x) \\,dx\$</span> 4. Define <span class="math inline">\$E\_x(d) = \\EE$$L(\\theta, d)\|X=x$$\$</span> 5. If <span class="math inline">\$\\delta(x) \\in \\argmin\_d E\_x(d)\$</span>, then <span class="math inline">\$E\_x(\\delta(x)) \\leq E\_x(\\delta'(x))\$</span> for all <span class="math inline">\$x\$</span> 6. This implies <span class="math inline">\$r(\\pi, \\delta) \\leq r(\\pi, \\delta')\$</span>

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Special Cases and Examples →](03-2-special-cases-and-examples.md)
