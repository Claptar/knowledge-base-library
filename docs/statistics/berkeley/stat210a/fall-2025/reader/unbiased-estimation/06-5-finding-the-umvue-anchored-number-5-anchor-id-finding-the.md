---
title: 5 Finding the UMVUE {.anchored number="5" anchor-id="finding-the-umvue"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5 Finding the UMVUE {.anchored number="5" anchor-id="finding-the-umvue"}

**Source:** [`reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We have two strategies for finding the UMVUE:

1.  Solve directly for an unbiased estimator based on <span class="math inline">\$T\$</span>
2.  Find any unbiased estimator at all, then Rao-Blackwellize it

We give examples of both strategies below:

**Example (Poisson):** Let <span class="math inline">\$X\_1, \\ldots, X\_n \\sim \\text{Pois}(\\theta)\$</span>, <span class="math inline">\$g(\\theta) = e^{-\\theta}\$</span> and consider unbiased estimation for <span class="math inline">\$g(\\theta) = \\theta^2\$</span>.

The complete sufficient statistic for the model is

<span class="math display">\\$$T(X) = \\sum X\_i \\sim \\text{Pois}(n\\theta),\\$$</span> and its probability mass function for <span class="math inline">\$t \\geq 0\$</span> is <span class="math display">\\$$ p\_\\theta(t) = \\frac{e^{-n\\theta} (n\\theta)^t}{t!} \\$$</span> **Strategy 1**

If there is some unbiased estimator <span class="math inline">\$\\delta(t)\$</span>, we can try to solve for it by setting its expectation equal to <span class="math inline">\$\\theta^2\$</span>: <span class="math display">\\$$ \\theta^2 = \\EE\_\\theta \\delta(T) = \\sum\_{t=0}^\\infty \\delta(t) \\frac{e^{-n\\theta} (n\\theta)^t}{t!}. \\$$</span> Rearranging factors, we obtain matching power series: <span class="math display">\\$$ \\sum\_{t=0}^\\infty \\delta(t) \\frac{n^t \\theta^t}{t!} = e^{n\\theta}\\theta^2 = \\sum\_{k=0}^\\infty \\frac{n^k\\theta^{k+2}}{k!}. \\$$</span> We will choose the coefficients on the left-hand side to match terms. First, change the index for the left-hand sum to <span class="math inline">\$t = k+2\$</span>: <span class="math display">\\$$ \\sum\_{t=0}^\\infty \\delta(t) \\frac{n^t \\theta^t}{t!} = e^{n\\theta}\\theta^2 = \\sum\_{t=2}^\\infty \\frac{n^{t-2}\\theta^{t}}{(t-2)!}. \\$$</span> To match the terms, we can set <span class="math inline">\$\\delta(0)=\\delta(1)=0\$</span>, and for <span class="math inline">\$t\\geq 2\$</span>, set <span class="math inline">\$\\delta(t)=\\frac{t!}{n^2(t-2)!}=\\frac{t(t-1)}{n^2}\$</span>. The same expression works for both, so we obtain the estimator <span class="math display">\\$$ \\delta(T) = \\frac{T(T-1)}{n^2} \\$$</span>

**Strategy 2:**

Alternatively, we can find an unbiased estimator and Rao-Blackwellize it. If <span class="math inline">\$n\\geq 2\$</span>, we can use the fact that

<span class="math display">\\$$ \\EE\_\\theta \[X\_1 X\_2$$ = \\EE\_\\theta $$X\_1$$ \\;\\cdot\\; \\EE\_\\theta $$X\_2$$ = \\theta^2 \\\]</span> to obtain an initial unbiased estimator <span class="math inline">\$\\delta\_0(X) = X\_1X\_2\$</span>, which we will Rao-Blackwellize.

Our calculation begins by recalling that, conditional on <span class="math inline">\$T\$</span>, we have <span class="math display">\\$$ (X\_1,\\ldots,X\_n) \\mid T=t \\sim \\text{Multinom}\\left(t, \\frac{1}{n}1\_n\\right), \\$$</span> so that, in particular, <span class="math inline">\$X\_1 \\mid T=t \\sim \\text{Binom}(t, \\frac{1}{n})\$</span>, which has mean <span class="math inline">\$t/n\$</span> and variance <span class="math inline">\$t\\frac{1}{n}\\cdot (1-\\frac{1}{n}) = \\frac{(n-1)t}{n^2}\$</span> Likewise, conditional on <span class="math inline">\$X\_1\$</span> and <span class="math inline">\$T\$</span>, we have <span class="math display">\\$$ (X\_2,\\ldots,X\_n) \\mid T=t, X\_1=x\_1 \\sim \\text{Multinom}\\left(t-x\_1, \\frac{1}{n-1}1\_{n-1}\\right), \\$$</span> where <span class="math inline">\$1\_n = (1,\\ldots,1) \\in \\RR^n\$</span>, so we likewise have <span class="math inline">\$X\_2 \\mid T=t, X\_1=x\_1 \\sim \\text{Binom}(t-x\_1, \\frac{1}{n-1})\$</span>.

Hence, we can write <span class="math display">\\$$ \\begin{aligned} \\EE\\left\[\\, X\_1 X\_2 \\mid T \\,\\right$$ &= \\EE\\left$$\\, X\_1 \\EE\[X\_2 \\mid T, X\_1$$ \\mid T\\,\\right\]\\\\$$5pt$$ &= \\EE\\left$$\\, X\_1 \\frac{T-X\_1}{n-1} \\mid T\\,\\right$$\\\\$$5pt$$ &= \\frac{1}{n-1}\\cdot\\EE$$X\_1 T - X\_1^2 \\mid T$$\\\\$$5pt$$ &= \\frac{1}{n-1}\\cdot\\left(T^2/n - \\left$$\\frac{T (n-1)}{n^2}+\\left(T/n\\right)^2\\right$$\\right)\\\\$$5pt$$ &= \\frac{T(T-1)}{n^2}, \\end{aligned} \\\]</span> giving us the same answer as above (as we knew it had to).

**Example:** <span class="math inline">\$X\_1, \\ldots, X\_n \\sim U$$0, \\theta$$\$</span>, <span class="math inline">\$\\theta &gt; 0\$</span>

The complete sufficient statistic for the model is <span class="math inline">\$T = X\_{(n)}\$</span>, and its pdf is <span class="math display">\\$$ p\_\\theta(t) = n t^{n-1} / \\theta^n \\cdot 1\\{0 &lt; t &lt; \\theta\\} \\$$</span>

**Strategy 1**

We can start by just checking how far off <span class="math inline">\$T\$</span> is from being an unbiased estimator, and see if we can correct it. From the density above we can recognize that <span class="math inline">\$T/\\theta\$</span> follows a <span class="math inline">\$\\text{Beta}(n,1)\$</span> distribution, which has mean <span class="math inline">\$\\frac{n}{n+1}\$</span> and variance <span class="math inline">\$\\frac{n}{(n+1)^2(n+2)}\$</span> (we could also compute these easily enough by integration).

As a result, we have <span class="math inline">\$\\EE\_\\theta$$T$$ = \\frac{n}{n+1} \\theta\$</span>, so <span class="math inline">\$\\frac{n+1}{n} T\$</span> is unbiased, and therefore UMVU.

**Strategy 2**

Alternatively, we could observe that <span class="math inline">\$2X\_1\$</span> is unbiased and try to Rao-Blackwellize it. To do this we need to find the conditional distribution of <span class="math inline">\$X\$</span> given that <span class="math inline">\$X\_{(n)}=t\$</span>. To warm up, let’s just condition on <span class="math inline">\$X\_{(n)} = t\$</span> *and* <span class="math inline">\$X\_n\$</span> is the maximum. This is equivalent to conditioning on <span class="math inline">\$X\_n = t\$</span> and <span class="math inline">\$X\_1,\\ldots,X\_{n-1} \\leq t\$</span>. In that case, <span class="math inline">\$X\_n\$</span> is deterministically <span class="math inline">\$t\$</span> and we have <span class="math display">\\$$ X\_1,\\ldots,X\_{n-1} \\mid \\max\_{i\\leq n} X\_i \\leq t, X\_n =t \\simiid \\text{Unif}\[0,t$$. \\\]</span> More generally, define <span class="math inline">\$I^\*(X)\$</span> to be the maximizing index. We’ve just calculated the distribution of <span class="math inline">\$T(X)\$</span> given <span class="math inline">\$I^\*(X)=n\$</span> and <span class="math inline">\$T(X)=t\$</span>. Since the data are exchangeable (or by Basu’s theorem) <span class="math inline">\$I^\*(X)\$</span> is also independent of <span class="math inline">\$T(X)\$</span>. So the conditional distribution of <span class="math inline">\$X\_1\$</span> is that its <span class="math inline">\$t\$</span> if <span class="math inline">\$I^\*(X)=1\$</span>, which happens with probability <span class="math inline">\$1/n\$</span>, and it’s <span class="math inline">\$\\text{Unif}$$0,t$$\$</span> otherwise. Wrapping up, we have

<span class="math display">\\$$ \\begin{aligned} \\EE\[X\_1 \\mid T=t$$ &= \\frac{1}{n}\\EE$$X\_1 \\mid T=t, I^\*=1$$ + \\frac{n-1}{n}\\EE$$X\_1 \\mid T=t, I^\* \\neq 1$$\\\\ &= \\frac{t}{n} + \\frac{t(n-1)}{2n}\\\\ &= \\frac{t(n+1)}{2n} \\end{aligned} \\\]</span> Hence <span class="math inline">\$\\EE$$2X\_1 \\mid T$$ = \\frac{n+1}{n} T\$</span>, giving the same estimator as we saw before.

**A better estimator**

Unfortunately, the estimator we just calculated twice is inadmissible.

For any estimator <span class="math inline">\$cT\$</span>, we can calculate its MSE as the squared bias plus the variance

<span class="math display">\\$$ \\begin{aligned} \\text{MSE}(\\theta; cT) &= (\\EE\_\\theta \[cT$$ - \\theta)^2 + \\Var\_\\theta(cT)\\\\ &= (c \\EE\_\\theta $$T$$ - \\theta)^2 + c^2\\Var\_\\theta(T)\\\\ &= \\theta^2\\left$$(c \\EE\_\\theta \[T/\\theta$$ - 1)^2 + c^2\\Var\_\\theta(T/\\theta)\\right\]\\\\ &= \\theta^2\\left$$\\left(\\frac{cn}{n+1}-1\\right)^2 + \\frac{c^2n}{(n+1)^2(n+2)}\\right$$. \\end{aligned} \\\]</span> The final expression is a quadratic in <span class="math inline">\$c\$</span>, which is minimized at <span class="math inline">\$c^\* = \\frac{n+2}{n+1}\$</span>. Thus, <span class="math inline">\$\\frac{n+2}{n+1}T\$</span> has a lower MSE than <span class="math inline">\$\\frac{n+1}{n}T\$</span> *for every value of <span class="math inline">\$\\theta\$</span>*. By scaling down our estimator a bit, we reduce its variance enough to compensate for the bias we have introduced.

Thus, we see that by introducing the unbiasedness constraint we have ruled out *all admissible estimators* and are left only with inadmissible ones, the best of which is <span class="math inline">\$\\frac{n+1}{n}T\$</span>.

---

[← 4 UMVU estimators {.anchored number="4" anchor-id="umvu-estimators"}](05-4-umvu-estimators-anchored-number-4-anchor-id-umvu-estimator.md) · [Up: contents](index.md) · [6 Doubts about unbiasedness {.anchored number="6" anchor-id="doubts-about-unbiasedness"} →](07-6-doubts-about-unbiasedness-anchored-number-6-anchor-id-doub.md)
