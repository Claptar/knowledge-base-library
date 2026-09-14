---
title: Score fisher Part 06 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Score fisher Part 06 —

**Source:** [`reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

**Example: Exponential family**

It is also illuminating to calculated these quantities for exponential families. Assume we have <span class="math display">\\$$ p\_\\eta(x) = e^{\\eta'T(x) - A(\\eta)} h(x). \\$$</span>

Then the log-likelihood is <span class="math inline">\$\\ell(\\eta;X) = \\eta'T(X) - A(\\eta) + \\log h(X)\$</span>, and the score is <span class="math display">\\$$ \\nabla \\ell(\\eta;X) = T(X) - \\nabla A(\\eta). \\$$</span> Recalling that <span class="math inline">\$\\nabla A(\\eta) = \\EE\_\\eta T(X)\$</span>, we obtain <span class="math display">\\$$ S\_\\eta(X) = T(X) - \\EE\_\\eta T(X). \\$$</span> So we indeed see that, up to a constant shift (which is needed for its mean to be zero), the score in an exponential family (at least in the natural parameterization) is none other than the sufficient statistic <span class="math inline">\$T(X)\$</span>.

Since <span class="math inline">\$\\EE\_\\eta T(X)\$</span> is nonrandom, the variance is <span class="math display">\\$$ J(\\eta) = \\Var\_\\eta (T(X)) = \\nabla^2 A(\\eta). \\$$</span>

We could alternatively derive the Fisher information by taking a second derivative of the log-likelihood with respect to <span class="math inline">\$\\eta\$</span>, giving <span class="math display">\\$$ \\nabla^2\\ell(\\eta;X) = -\\nabla^2 A(\\eta), \\$$</span> which is deterministically equal to <span class="math inline">\$-\\Var\_\\eta(T(X))\$</span>, so we have confirmed the identity <span class="math inline">\$J(\\eta) = -\\EE\_\\eta$$\\nabla^2 \\ell(\\eta;X)$$\$</span>.

**Example: Curved exponential family**

Next, consider a curved version of the previous family, parameterized by <span class="math inline">\$\\theta \\in \\RR\$</span>: <span class="math display">\\$$ p\_\\theta(x) = e^{\\eta(\\theta)'T(x) - A(\\eta(\\theta))}h(x), \\$$</span> So, <span class="math inline">\$\\eta(\\theta)\$</span> is tracing out a one-dimensional curve through the ambient <span class="math inline">\$s\$</span>-dimensional parameter space.

Now, the log-likelihood is <span class="math display">\\$$\\ell(\\theta;X) = \\eta(\\theta)'T(x) - A(\\eta(\\theta)) + \\log h(x),\\$$</span> and we can obtain its first derivative by applying the chain rule: <span class="math display">\\$$ \\dot{\\ell}(\\theta;X) = \\dot{\\eta}(\\theta)'(T(X) - \\nabla\_\\eta A(\\eta(\\theta))), \\$$</span> leading to <span class="math display">\\$$ S\_\\theta(X) = \\dot{\\eta}(\\theta)'(T(X) - \\EE\_\\theta T(X)) = \\dot{\\eta}(\\theta)'S\_{\\eta(\\theta)}(X), \\$$</span> where (slightly abusing notation) <span class="math inline">\$S\_{\\eta}(X)\$</span> is the score in the ambient exponential family. Note here <span class="math inline">\$\\dot\\eta(\\theta)\$</span> is an <span class="math inline">\$s\$</span>-vector. Its direction tells us which projection of <span class="math inline">\$T(X)\$</span> is informative for distinguishing parameter values in a local neighborhood of <span class="math inline">\$\\theta\$</span>, and its magnitude tells us how rapidly we are traversing the parameter space.

Likewise the Fisher information is <span class="math display">\\$$ J(\\theta) = \\dot{\\eta}(\\theta)'J(\\eta(\\theta))\\dot{\\eta}(\\theta). \\$$</span> It is noteworthy that choosing a “faster” parameterization of the same subfamily will make the Fisher information larger. This is not because the data become any more or less informative about a statistical model when we change the parameterization. Again, we can think of it more as a “unit conversion” issue: the farther <span class="math inline">\$P\_{\\eta(\\theta)}\$</span> is from (say) <span class="math inline">\$P\_{\\eta(\\theta\\pm 0.1)}\$</span>, the better chance we have of estimating <span class="math inline">\$\\theta\$</span> up to a precision of <span class="math inline">\$0.1\$</span>.

**Example: Curved Gaussian location family**

As a concrete example of the above, suppose <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid N\_d(\\mu(\\theta), I\_d)\$</span>, for <span class="math inline">\$\\theta \\in \\RR\$</span> and <span class="math inline">\$\\mu(\\theta) \\in \\RR^d\$</span>: that is, <span class="math inline">\$\\mu(\\theta)\$</span> is tracing out a curve in the parameter space of the ambient <span class="math inline">\$d\$</span>-dimensional Gaussian location model.

In the ambient family, the score is <span class="math display">\\$$ S\_\\mu^{(\\mu)}(X) = \\sum\_i X\_i - n\\mu = n(\\overline{X}-\\mu), \\$$</span> and the Fisher information is <span class="math inline">\$J^{(\\mu)}(\\mu) = nI\_d\$</span>. Thus, in the curved subfamily, we have <span class="math display">\\$$ S\_{\\theta}(X) = n\\dot\\mu(\\theta)'(\\overline{X}-\\mu(\\theta)), \\$$</span> and <span class="math inline">\$J(\\theta) = n\\\|\\dot\\mu(\\theta)\\\|^2\$</span>, i.e. the sample size times the parameterization speed. The

---

[← Score fisher Part 05 —](05-score-fisher-part-05.md) · [Up: contents](index.md)
