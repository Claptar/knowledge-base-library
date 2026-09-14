---
title: Differential identities {.anchored anchor-id="differential-identities"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/exponential-families.html
source_file: sources/berkeley-stat210a/fall-2025/reader/exponential-families.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Differential identities {.anchored anchor-id="differential-identities"}

**Source:** [`reader/exponential-families.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/exponential-families.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Exponentiating <a href="#eq-log-partition" class="quarto-xref">Equation 2</a>, we obtain the equation

<span id="eq-partition"><span class="math display">\\$$ e^{A(\\eta)} = \\int\_\\cX e^{\\eta'T(x)}h(x)\\td\\mu(x) \\tag{3}\\$$</span></span>

We can derive many interesting identities by differentiating this function, and related functions, with respect to <span class="math inline">\$\\eta\$</span>. We will always evaluate derivatives by differentiating under the integral sign. This is not always a correct operation, but by Theorem 2.4 in Keener, it is correct on the interior of the natural parameter space <span class="math inline">\$\\Xi\_1\$</span>. We refer the reader to Keener for details.

### Mean of <span class="math inline">\$T(X)\$</span> {.anchored anchor-id="mean-of-tx"}

Partially differentiating <a href="#eq-partition" class="quarto-xref">Equation 3</a> once with respect to a generic coordinate <span class="math inline">\$\\eta\_j\$</span>, for <span class="math inline">\$j =1, \\ldots, s\$</span>, we obtain

<span class="math display">\\$$ \\begin{aligned} \\frac{\\partial}{\\partial \\eta\_j} e^{A(\\eta)} &= \\int\_\\cX \\frac{\\partial}{\\partial \\eta\_j} e^{\\eta'T(x)}h(x)\\td\\mu(x)\\\\\[7pt$$ e^{A(\\eta)} \\frac{\\partial A}{\\partial \\eta\_j}(\\eta) &= \\int\_\\cX T\_j(x) e^{\\eta'T(x)}h(x)\\td\\mu(x)\\\\$$7pt$$ \\frac{\\partial A}{\\partial \\eta\_j}(\\eta) &= \\int\_\\cX T\_j(x) e^{\\eta'T(x) - A(\\eta)}h(x)\\td\\mu(x)\\\\$$7pt$$ &= \\EE\_\\eta \\left$$\\,T\_j(X)\\,\\right$$\\\\ \\end{aligned} \\\]</span>

Arranging these partial derivatives into a vector, we obtain

<span class="math display">\\$$ \\nabla A(\\eta) = \\EE\_\\eta\\left\[\\,T(X)\\,\\right$$, \\\]</span>

which gives us a very convenient method for evaluating the expectation of the sufficient statistic.

### Variance of <span class="math inline">\$T(X)\$</span> {.anchored anchor-id="variance-of-tx"}

Pushing our luck further, we can take a second partial derivative:

<span class="math display">\\$$ \\begin{aligned} \\frac{\\partial^2}{\\partial \\eta\_j\\partial \\eta\_k} e^{A(\\eta)} &= \\int\_\\cX \\frac{\\partial^2}{\\partial \\eta\_j\\partial \\eta\_k} e^{\\eta'T(x)}h(x)\\td\\mu(x)\\\\\[7pt$$ e^{A(\\eta)}\\left(\\frac{\\partial^2 A}{\\partial \\eta\_j\\partial \\eta\_k} + \\frac{\\partial A}{\\partial \\eta\_j} \\frac{\\partial A}{\\partial \\eta\_k} \\right)&= \\int\_\\cX T\_j(x) T\_k(x)e^{\\eta'T(x)}h(x)\\td\\mu(x)\\\\$$7pt$$ \\frac{\\partial^2 A}{\\partial \\eta\_j\\partial \\eta\_k} + \\EE\_\\eta$$T\_j(X)$$\\EE\_\\eta$$T\_k(X)$$ &= \\EE\_\\eta \\left$$\\,T\_j(X) T\_k(X)\\,\\right$$\\\\ \\frac{\\partial^2 A}{\\partial \\eta\_j\\partial \\eta\_k} &= \\text{Cov}\_\\eta\\left(T\_j(X), T\_k(X)\\right). \\end{aligned} \\\]</span>

Again, collecting these second partials into a Hessian matrix gives us

<span class="math display">\\$$ \\nabla^2 A(\\eta) = \\text{Var}\_\\eta(T(X)), \\$$</span>

where the right-hand side denotes the <span class="math inline">\$s\\times s\$</span> variance-covariance matrix of the random vector <span class="math inline">\$T(X)\$</span>.

**Example (Poisson, continued):** As we showed above, in the Poisson exponential family the sufficient statistic is <span class="math inline">\$T(X)=X\$</span>, the natural parameter is <span class="math inline">\$\\eta = \\log\\lambda\$</span>, and the log-partition function is <span class="math inline">\$A(\\eta) = e^\\eta \\;(=\\lambda)\$</span>.

**Note:** This calculation would not have worked correctly if we had instead said <span class="math inline">\$A(\\eta) = \\lambda\$</span>, and differentiated that expression with respect to <span class="math inline">\$\\lambda\$</span>. We would then get <span class="math inline">\$\\EE\_\\eta$$X$$ = 1\$</span> and <span class="math inline">\$\\text{Var}\_\\eta(X) = 0\$</span>, which are clearly incorrect.

### Moment-generating function and cumulant-generating function {.anchored anchor-id="moment-generating-function-and-cumulant-generating-function"}

The moment generating function (MGF) of a <span class="math inline">\$d\$</span>-dimensional random vector <span class="math inline">\$X\\sim P\$</span> is defined as <span class="math inline">\$M^X(u) = \\EE$$e^{u'X}$$\$</span>, for <span class="math inline">\$u\\in \\RR^d\$</span>. If the MGF is well-defined in a neighborhood of <span class="math inline">\$u=0\$</span>, then we can use it to calculated moments of <span class="math inline">\$X\$</span> by evaluating its derivatives at 0.

We can show this using manipulations very similar to the ones we saw above. To evaluate the first moment of <span class="math inline">\$X\_j\$</span>, we can differentiate once with respect to <span class="math inline">\$u\_j\$</span>, since

<span class="math display">\\$$ \\frac{\\partial}{\\partial u\_j} M^X(u) = \\int\_\\cX \\frac{\\partial}{\\partial u\_j} e^{u'x}\\td P(x) = \\int\_\\cX x\_j e^{u'x}\\td P(x) = \\int\_\\cX x\_j e^{u'x} \\td P(x). \\$$</span>

Here we have again assumed that we can differentiate under the integral sign; this is a technical condition that we would check if we were being more careful.

Evaluating the derivative at <span class="math inline">\$u=0\$</span>, we obtain <span class="math inline">\$\\frac{\\partial}{\\partial u\_j} M^X(0) = \\int\_\\cX x\_j \\td P(x) = \\EE$$X\_j$$\$</span>. Moreover, we can repeat this trick as many times as we want, leading to a formula for mixed partial derivatives of any order:

<span id="eq-mgf"><span class="math display">\\$$ \\left.\\frac{\\partial^{m\_1 + \\cdots + m\_d}}{\\partial u\_1^{m\_1}\\cdots\\partial u\_d^{m\_d}} M^X(u)\\right\|\_{u=0} = \\left.\\int\_{\\cX} x\_1^{m\_1}\\cdots x\_d^{m\_d} e^{u'x}\\td P(x)\\right\|\_{u=0} = \\EE\\left\[\\,X\_1^{m\_1} \\cdots X\_d^{m\_d}\\,\\right$$. \\tag{4}\\\]</span></span>

The MGF is therefore very useful for evaluating moments of <span class="math inline">\$X\$</span>. It is also useful for finding distributions of sums of independent random variables, because <span class="math inline">\$M^{X + Y}(u) = M^X(u)M^Y(u),\$</span> if <span class="math inline">\$X\$</span> and <span class="math inline">\$Y\$</span> are independent. If two random variables have the same MGF then they have the same distribution.

In an exponential family, the MGF of <span class="math inline">\$T(X)\$</span>, under sampling from <span class="math inline">\$P\_\\eta\$</span>, is simple to evaluate:

<span class="math display">\\$$ \\begin{aligned} M^{T(X)}\_\\eta(u) &= \\EE\_\\eta\\left\[\\,e^{u'T(X)}\\,\\right$$\\\\$$5pt$$ &= \\int\_\\cX e^{u'T(x)}e^{\\eta'T(x) - A(\\eta)}h(x)\\td\\mu(x) \\\\$$5pt$$ &= e^{-A(\\eta)}\\int\_\\cX e^{(u+\\eta)'T(x)} h(x)\\td\\mu(x)\\\\$$5pt$$ &= e^{A(\\eta+u)-A(\\eta)} \\end{aligned} \\\]</span>

**Example (Poisson, continued):** The MGF for <span class="math inline">\$X \\sim \\text{Pois}(\\lambda)\$</span>, with <span class="math inline">\$\\eta = \\log\\lambda\$</span>, is

<span class="math display">\\$$ M^{X}\_\\eta(u) = \\exp\\{e^{\\eta + u} - e^{\\eta}\\} = \\exp\\{\\lambda (e^u - 1)\\} \\$$</span>

To see how the MGF is useful, suppose we have <span class="math inline">\$X\_i \\sim \\text{Pois}(\\lambda\_i)\$</span>, independently for <span class="math inline">\$i = 1,2,\\ldots,n\$</span>, and we want to know the distribution of <span class="math inline">\$X\_+ = \\sum\_i X\_i\$</span>. Then we can multiply the MGF’s for <span class="math inline">\$X\_1,\\ldots,X\_n\$</span> together to obtain the MGF for <span class="math inline">\$X\_+\$</span>:

<span class="math display">\\$$ M^{X\_+}(u) = \\prod\_i M\_{\\eta\_i}^{X\_i}(u) = \\exp\\left\\{\\sum\_i \\lambda\_i (e^u-1)\\right\\}. \\$$</span>

As a result, we have <span class="math inline">\$X\_+ \\sim \\text{Pois}(\\lambda\_+)\$</span>, for <span class="math inline">\$\\lambda\_+ = \\sum\_j \\lambda\_i\$</span>.

Likewise, the closely related *cumulant-generating function* (CGF) is defined as the log of the MGF:

<span class="math display">\\$$ K^{T(X)}\_\\eta(u) = \\log M^{T(X)}\_\\eta(u) = A(\\eta+u)-A(\\eta) \\$$</span>

Evaluating the CGF’s derivatives at <span class="math inline">\$u=0\$</span> gives us the distribution’s *cumulants* instead of its moments (the first two cumulants are the mean and variance). <span class="math inline">\$K\_\\eta^{T(X)}\$</span> and <span class="math inline">\$A\$</span> are closely related. In particular, note that

<span class="math display">\\$$ \\left.\\frac{\\partial}{\\partial \\eta\_j}K\_\\eta^{T}(u)\\right\|\_{u=0} = \\frac{\\partial}{\\partial \\eta\_j} A(\\eta), \\$$</span>

This relationship explains why we can also get cumulants for <span class="math inline">\$T(X)\$</span> under <span class="math inline">\$P\_\\eta\$</span> by differentiating <span class="math inline">\$A(\\eta)\$</span>. It also partly explains why <span class="math inline">\$A(\\eta)\$</span> is sometimes referred to as the CGF even though it is generally not the CGF for <span class="math inline">\$T(X)\$</span>.

---

[← Exponential family structure {.anchored anchor-id="exponential-family-structure"}](02-exponential-family-structure-anchored-anchor-id-exponential.md) · [Up: contents](index.md) · [Other parameterizations {.anchored anchor-id="other-parameterizations"} →](04-other-parameterizations-anchored-anchor-id-other-parameteriz.md)
