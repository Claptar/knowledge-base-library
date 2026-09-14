---
title: 6 Examples
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 6 Examples

**Source:** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

**Example: i.i.d. sample**

Assume <span class="math inline">\$X\_1, \\ldots, X\_n \\simiid p\_\\theta^{(1)}(x)\$</span>, for <span class="math inline">\$\\theta \\in \\Theta \\subseteq \\RR^d\$</span>.

Assume additionally that <span class="math inline">\$p\_\\theta^{(1)}\$</span> is “regular:” it has common support, and finite derivative w.r.t. <span class="math inline">\$\\theta\$</span>.

Then the full data density is <span class="math inline">\$p\_\\theta(x) = \\prod\_i p\_\\theta^{(1)}(x\_i)\$</span>.

Define the single-sample log-likelihood <span class="math inline">\$\\ell\_1(\\theta;x\_i) = \\log p\_\\theta^{(1)}(x\_i)\$</span>; then we have <span class="math inline">\$\\ell(\\theta;x) = \\sum\_i \\ell\_1(\\theta;x\_i)\$</span>.

Then the Fisher information for the full sample is <span class="math display">\\$$J(\\theta) = \\Var\_\\theta(\\nabla \\ell(\\theta; X)) = \\sum\_{i=1}^n \\Var\_\\theta(\\nabla \\ell\_1(\\theta; X\_i)) = n J\_1(\\theta),\\$$</span> where <span class="math inline">\$J\_1(\\theta) = \\Var\_\\theta(\\nabla\\ell(\\theta; X\_1))\$</span> is the Fisher information for a single sample.

As a result, we see that the Information bound scales like <span class="math inline">\$n^{-1}\$</span> for regular families; in other words, the standard deviation of an estimator should scale roughly like <span class="math inline">\$1/\\sqrt{n}\$</span>.

**Example: exponential family**

Suppose we have an exponential family of the form <span class="math display">\\$$ p\_\\eta(x) = e^{\\eta'T(x) - A(\\eta)} h(x).\\$$</span>

The log-likelihood is <span class="math inline">\$\\ell(\\eta;X) = \\eta'T(X) - A(\\eta) + \\log h(X)\$</span>, and its gradient (the score) is <span class="math display">\\$$\\nabla \\ell(\\eta;X) = T(X) - \\nabla A(\\eta) = T(X) - \\EE\_\\eta T(X).\\$$</span> Since <span class="math inline">\$\\EE\_\\eta T(X)\$</span> is nonrandom, the variance is <span class="math display">\\$$ J(\\eta) = \\Var\_\\eta (T(X)) = \\nabla^2 A(\\eta).\\$$</span>

We could alternatively derive the Fisher information from taking a second derivative with respect to <span class="math inline">\$\\eta\$</span>, giving <span class="math display">\\$$ \\nabla^2\\ell(\\eta;X) = -\\nabla^2 A(\\eta),\\$$</span> which is deterministically equal to <span class="math inline">\$-\\Var\_\\eta(T(X))\$</span>, so we have confirmed the identity <span class="math inline">\$J(\\eta) = -\\EE\_\\eta$$\\nabla^2 \\ell(\\eta;X)$$\$</span>.

**Example: Curved exponential family**

Next, consider a curved version of the previous family, parameterized by <span class="math inline">\$\\theta \\in \\RR\$</span>: <span class="math display">\\$$p\_\\theta(x) = e^{\\eta(\\theta)'T(x) - B(\\theta)}h(x),\\quad \\text{ with } B(\\theta) = A(\\eta(\\theta))\\$$</span> Again, the log-likelihood is <span class="math display">\\$$\\ell(\\theta;X) = \\eta(\\theta)'T(x) - B(\\theta) + \\log h(x),\\$$</span> and its first derivative is <span class="math display">\\$$\\begin{aligned} \\dot{\\ell}(\\theta;X) &= \\dot{\\eta}(\\theta)'T(X) - \\dot{\\eta}(\\theta)'\\nabla\_\\eta A(\\eta(\\theta))\\\\ &= \\dot{\\eta}(\\theta) '\\left(T(X) - \\nabla\_\\eta A(\\eta(\\theta))\\right)\\\\ &= \\dot{\\eta}(\\theta)'(T(X) - \\EE\_\\theta T(X)).\\end{aligned}\\$$</span>

As a result, the Fisher information is <span class="math display">\\$$J(\\theta) = \\Var\_\\theta(\\dot{\\eta}(\\theta)'T(X)) = \\dot{\\eta}(\\theta)'\\Var\_\\theta(T(X))\\dot{\\eta}(\\theta).\\$$</span> Note in this model <span class="math inline">\$\\dot{\\eta}'T(X)\$</span> is a “local complete sufficient statistic” for the model near <span class="math inline">\$\\theta\$</span>.

---

[← 5 Cramér-Rao Lower Bound](06-5-cramér-rao-lower-bound.md) · [Up: contents](index.md) · [7 Efficiency →](08-7-efficiency.md)
