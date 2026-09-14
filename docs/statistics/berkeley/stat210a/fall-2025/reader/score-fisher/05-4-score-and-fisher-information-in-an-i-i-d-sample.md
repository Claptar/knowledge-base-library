---
title: 4 Score and Fisher information in an i.i.d. sample
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Score and Fisher information in an i.i.d. sample

**Source:** [`reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

The score and Fisher information are both additive over i.i.d. observations. Assume <span class="math inline">\$X\_1, \\ldots, X\_n\$</span> are sampled i.i.d. from a univariate density <span class="math inline">\$p\_\\theta^{(1)}(x)\$</span>, for <span class="math inline">\$\\theta \\in \\Theta \\subseteq \\RR^d\$</span>. Assume additionally that <span class="math inline">\$p\_\\theta^{(1)}\$</span> is “regular:” it has common support, and tame derivatives w.r.t. <span class="math inline">\$\\theta\$</span>.

The full data density is <span class="math inline">\$p\_\\theta(x) = \\prod\_{i=1}^n p\_\\theta^{(1)}(x\_i)\$</span>. Likewise, if we define the single-sample log-likelihood <span class="math display">\\$$ \\ell\_1(\\theta;X\_i) = \\log p\_\\theta^{(1)}(X\_i), \\$$</span> then the log-likelihood for the full sample is <span class="math inline">\$\\ell(\\theta;X) = \\sum\_{i=1}^n \\ell\_1(\\theta;X\_i)\$</span>. Hence, each sample gives us a random realization of the log-likelihood function on the parameter space, and we just add them up to obtain the log-likelihood function for the full sample.

If the score for a single observation is <span class="math inline">\$S\_\\theta^{(1)}(X\_i) = \\nabla \\ell(\\theta; X\_i)\$</span>, then the score for the full sample is <span class="math inline">\$S\_\\theta(X) = \\sum\_i S\_\\theta^{(i)}(X\_i)\$</span>, the sum of the single-observation scores. Because these are i.i.d., the variance of <span class="math inline">\$S\_\\theta(X)\$</span> for the full sample is just <span class="math inline">\$n\$</span> times the variance of <span class="math inline">\$S\_\\theta^{(1)}(X\_i)\$</span>, so we can write <span class="math inline">\$J(\\theta)=n J\_1(\\theta)\$</span>, where <span class="math inline">\$J\_1(\\theta)\$</span> is the Fisher information when <span class="math inline">\$n=1\$</span>.

As one consequence, we see that the CRLB scales like <span class="math inline">\$n^{-1}\$</span> for regular families; in other words, the standard deviation of an estimator should scale roughly like <span class="math inline">\$1/\\sqrt{n}\$</span>.

---

[← 3 Cramér-Rao Lower Bound](04-3-cramér-rao-lower-bound.md) · [Up: contents](index.md) · [5 Score and Fisher information in (curved) exponential families →](06-5-score-and-fisher-information-in-curved-exponential-familie.md)
