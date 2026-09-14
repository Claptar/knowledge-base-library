---
title: 1 Minimax risk and estimator {number="1"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/minimax-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/minimax-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Minimax risk and estimator {number="1"}

**Source:** [`reader/minimax-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/minimax-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

## <span class="header-section-number">1.1</span> Definitions {.anchored number="1.1" anchor-id="definitions"}

Since introducing the basic problem in [Lecture 3](../estimation/index.md) of how to choose between estimators, we have studied two possible answers: First, to constrain our choice of estimator to be unbiased, which in the presence of a complete sufficient statistic narrows our choices to (at most) one good unbiased estimator for any estimand; and second, to summarize risk functions by their average-case risk, which leads us to Bayes estimators. In this lecture, we will consider another idea: to minimize the worst-case risk: <span class="math display">\\$$ \\minimize\_{\\delta} \\sup\_{\\theta\\in\\Theta} R(\\theta;\\delta) \\$$</span> The (possibly unattainable) infimum of all estimators’ sup-risks is called the **minimax risk** of the estimation problem <span class="math display">\\$$ r^\* = \\inf\_\\delta \\sup\_\\theta R(\\theta;\\delta), \\$$</span> and an estimator <span class="math inline">\$\\delta^\*\$</span> is called **minimax** if it achieves the minimax risk, i.e. if <span class="math display">\\$$ \\sup\_\\theta R(\\theta; \\delta^\*) = r^\*. \\$$</span> Whether or not a minimax estimator exists, or we want to use it, it can be informative to investigate a problem’s minimax risk as a measure of how difficult the problem is, and in particular how it changes with the sample size, problem dimension, or other problem parameters. Thus, it is useful to be able to bound <span class="math inline">\$r^\*\$</span> from above and below.

## <span class="header-section-number">1.2</span> Game theoretic interpretation {.anchored number="1.2" anchor-id="game-theoretic-interpretation"}

We can think of the minimax risk as the expected payoff in an adversarial zero-sum game between the analyst, who chooses the estimator to make the risk as small as possible, and “Nature,” who waits to see what estimator the analyst chooses and then assigns the parameter to make the risk as large as possible. If the analyst plays first and selects the estimator <span class="math inline">\$\\delta\$</span>, then Nature will always select the value of <span class="math inline">\$\\theta\$</span> that maximizes <span class="math inline">\$R(\\theta;\\delta)\$</span>; then <span class="math inline">\$r^\*\$</span> corresponds to the attained risk in this game, and <span class="math inline">\$\\delta^\*\$</span> to the analyst’s optimal move.

What if Nature played first? If the analyst could know <span class="math inline">\$\\theta\$</span> while choosing <span class="math inline">\$\\delta\$</span>, the problem would be too easy, but it becomes more interesting if we allow Nature to choose a *mixed strategy* of sampling <span class="math inline">\$\\theta \\sim \\Lambda\$</span>. Then, an analyst who could see the prior (but not the realized value of <span class="math inline">\$\\theta\$</span>) would play the Bayes estimator <span class="math inline">\$\\delta\_\\Lambda\$</span> and attain the Bayes risk.

Intuitively, the analyst is in a better position when playing second than when playing first, and indeed the Bayes risk for any <span class="math inline">\$\\Lambda\$</span> is a lower bound for the minimax risk: <span class="math display">\\$$ r\_\\Lambda \\;=\\; \\inf\_{\\delta} \\int\_\\Theta R(\\theta;\\delta)\\;d\\Lambda(\\theta) \\;\\leq\\; \\inf\_{\\delta} \\sup\_\\theta R(\\theta; \\delta) \\;=\\; r^\*, \\$$</span> since any estimator’s average-case risk is no larger than its worst-case risk.

To optimize this lower bound on <span class="math inline">\$r^\*\$</span>, we can try to find Nature’s Nash equilibrium strategy.

## <span class="header-section-number">1.3</span> Least Favorable Priors {.anchored number="1.3" anchor-id="least-favorable-priors"}

Since <span class="math inline">\$r\_\\Lambda\$</span> for any prior <span class="math inline">\$\\Lambda\$</span> lower-bounds the minimax risk, we have <span class="math inline">\$\\sup\_\\Lambda r\_\\Lambda \\leq r^\*\$</span>. If a prior <span class="math inline">\$\\Lambda^\*\$</span> attains this supremum, we call it **least favorable prior**. When the supremum is not attainable by any prior, we can still attain it in the limit by defining a sequence of priors <span class="math inline">\$\\Lambda\_1,\\Lambda\_2,\\ldots\$</span> with <span class="math inline">\$r\_{\\Lambda\_n}\\to \\sup\_\\Lambda r\_\\Lambda\$</span>; such a sequence is called a least favorable sequence of priors.

Since <span class="math inline">\$\\sup\_\\theta R(\\theta;\\delta)\$</span> for any estimator <span class="math inline">\$\\delta\$</span> is also an upper bound for <span class="math inline">\$r^\*\$</span>, one way to show that we have a least favorable prior and a minimax estimator is to show that the Bayes risk <span class="math inline">\$r\_\\Lambda\$</span> and the sup-risk of the Bayes estimator <span class="math inline">\$\\delta\_\\Lambda\$</span> give matching lower and upper bounds:

**Theorem:** Suppose that <span class="math inline">\$r\_\\Lambda\$</span> and <span class="math inline">\$\\delta\_\\Lambda\$</span> are the Bayes risk and Bayes estimator for a prior <span class="math inline">\$\\Lambda\$</span>, and assume that <span class="math inline">\$r\_\\Lambda = \\sup\_\\theta R(\\theta;\\delta\_\\Lambda)\$</span>. Then <span class="math inline">\$\\delta\_\\Lambda\$</span> is minimax, <span class="math inline">\$\\Lambda\$</span> is least favorable, and <span class="math inline">\$r\_\\Lambda = r^\*\$</span>.

Moreover, if <span class="math inline">\$\\delta\_\\Lambda\$</span> is the unique Bayes estimator for <span class="math inline">\$\\Lambda\$</span> (up to <span class="math inline">\$\\stackrel{\\text{a.s.}}{=}\$</span>) then it is the unique minimax estimator.

*Proof:* 1. For any other estimator <span class="math inline">\$\\delta\$</span>, we have <span class="math display">\\$$ \\begin{aligned} \\sup\_\\theta R(\\theta;\\delta) &\\geq \\int R(\\theta;\\delta)\\,d\\Lambda(\\theta)\\\\ &\\geq r\_\\Lambda\\\\ &= \\sup\_\\theta R(\\theta;\\delta\_\\Lambda), \\end{aligned} \\$$</span> so <span class="math inline">\$\\delta\_\\Lambda\$</span> is minimax. If <span class="math inline">\$\\delta\_\\Lambda\$</span> is the unique Bayes estimator, then the second inequality is strict, so <span class="math inline">\$\\delta\_\\Lambda\$</span> is the unique minimax estimator.

Moreover, we have <span class="math display">\\$$ r\_\\Lambda \\leq r^\* \\leq \\sup\_\\theta R(\\theta;\\delta\_\\Lambda) = r^\*, \\$$</span> so <span class="math inline">\$r\_\\Lambda=r^\*\$</span> and <span class="math inline">\$\\Lambda\$</span> is optimizing the lower bound.<span class="math inline">\$\\blacksquare\$</span>

This theorem shows that any Bayes estimator is minimax if its average-case risk is the same as its worst-case risk. The simplest way this could be true is if the risk function is constant.

More generally, it could be true if the prior puts all of its mass on parameter values that attain the worst-case risk, as in the following example:

**Example:** We observe <span class="math inline">\$X\\sim N(\\theta,1)\$</span> where <span class="math inline">\$\|\\theta\|\\geq 1\$</span>, and we want to estimate <span class="math inline">\$g(\\theta)=\\text{sgn}(\\theta)\$</span> under squared-error loss. Let <span class="math inline">\$\\Lambda\$</span> be the prior that puts mass <span class="math inline">\$1/2\$</span> on <span class="math inline">\$\\theta=1\$</span> and <span class="math inline">\$\\theta=-1\$</span>, and no mass anywhere else. The posterior probability that <span class="math inline">\$\\theta=1\$</span> is given by <span class="math display">\\$$ \\PP(\\theta=1\\mid X=x) = \\frac{\\phi(x-1)}{\\phi(x-1)+\\phi(x+1)}, \\$$</span> so the Bayes estimator is <span class="math display">\\$$ \\EE\_\\Lambda\[g(\\theta) \\mid X=x$$ = \\frac{\\phi(x-1) - \\phi(x+1)}{\\phi(x-1)+\\phi(x+1)} = \\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}} = \\tanh(x). \\\]</span> We can plot the risk function for this estimator below to verify that it attains its sup-risk at both <span class="math inline">\$\\theta=-1\$</span> and <span class="math inline">\$\\theta=1\$</span>, and therefore on the entire support of <span class="math inline">\$\\Lambda\$</span>:

<figure class="figure">
<p><img src="minimax-estimation_files/figure-html/unnamed-chunk-1-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

Thus, <span class="math inline">\$\\delta\_\\Lambda(X)=\\tanh(X)\$</span> is also minimax for this problem.

**Note:** A common mistake students make is to come up with a prior <span class="math inline">\$\\Lambda\$</span>, then calculate <span class="math inline">\$r\_\\Lambda\$</span> and observe that it does not depend on <span class="math inline">\$\\theta\$</span>. We can apply our theorem if <span class="math inline">\$R(\\theta;\\delta\_\\Lambda)\$</span> is constant, but we haven’t shown anything if we just show that <span class="math inline">\$r\_\\Lambda\$</span> is constant. <span class="math inline">\$r\_\\Lambda\$</span> for *any* prior will not depend on <span class="math inline">\$\\theta\$</span>, for the simple reason that we have integrated it out.

**Example (Binomial):** As a more prosaic example, consider estimating <span class="math inline">\$\\theta\$</span> with squared error loss, in the model <span class="math inline">\$X\\sim \\text{Binom}(n,\\theta)\$</span>. Since we know that the Bayes estimator for the <span class="math inline">\$\\text{Beta}(\\alpha,\\beta)\$</span> prior is <span class="math inline">\$\\frac{X+\\alpha}{n+\\alpha+\\beta}\$</span>, we can see whether one of the Bayes estimators in this class has a constant risk function. If one does, it should be a symmetric prior, so we can try <span class="math inline">\$\\alpha=\\beta\$</span>, so let <span class="math inline">\$\\delta\_\\alpha=\\frac{X+\\alpha}{n+2\\alpha}\$</span>.

To calculate the MSE, we first calculate the mean and bias of <span class="math inline">\$\\delta\_\\alpha(X)\$</span> as <span class="math display">\\$$ \\EE\_\\theta \\left\[\\frac{X+\\alpha}{n+2\\alpha}\\right$$ = \\frac{n\\theta +\\alpha}{n+2\\alpha} \\;\\;\\Longrightarrow\\;\\; \\text{Bias}(\\theta;\\delta\_\\alpha) = \\frac{\\alpha (1-2\\theta)}{n+2\\alpha}, \\\]</span> and the variance as <span class="math display">\\$$ \\Var\_\\theta \\left(\\frac{X+\\alpha}{n+2\\alpha}\\right) = \\frac{\\Var\_\\theta(X)}{(n+2\\alpha)^{2}} = \\frac{n\\theta(1-\\theta)}{(n+2\\alpha)^{2}}. \\$$</span>

Thus, the MSE is <span class="math display">\\$$ \\begin{aligned} \\text{MSE}(\\theta;\\delta\_\\alpha) &= \\frac{\\alpha^2(1-2\\theta)^2+ n\\theta(1-\\theta)}{(n+2\\alpha)^{2}} \\\\\[7pt$$ &= \\frac{\\alpha^2+(n-4\\alpha^2)\\theta(1-\\theta)}{(n+2\\alpha)^{2}}. \\end{aligned} \\\]</span> Setting <span class="math inline">\$\\alpha^\* = \\sqrt{n}/2\$</span> eliminates the dependence on <span class="math inline">\$\\theta\$</span>, giving constant MSE of <span class="math display">\\$$ R(\\theta;\\delta\_{\\alpha^\*})=\\left(\\frac{\\alpha^\*}{n+2\\alpha^\*}\\right)^2 = \\frac{n}{4(n+\\sqrt{n})^2} \\$$</span> Since <span class="math inline">\$\\delta\_{\\alpha^\*}\$</span> is the unique Bayes estimator for <span class="math inline">\$\\Lambda^\*=\\text{Beta}(\\alpha^\*,\\alpha^\*)\$</span>, we can conclude that it is the unique minimax estimator, and <span class="math inline">\$\\Lambda^\*\$</span> is least favorable with <span class="math inline">\$r^\*=r\_{\\Lambda^\*}=\\frac{n}{4(n+\\sqrt{n})^2}\$</span>.

In particular, for <span class="math inline">\$n=16\$</span>, we have <span class="math inline">\$\\alpha^\*=2\$</span> and <span class="math inline">\$\\delta\_{\\alpha^\*}(X) = \\frac{X+2}{X+4}\$</span>, as claimed in [Lecture 3](../estimation/index.md).

Note that while we can consider <span class="math inline">\$\\Lambda^\*\$</span> as a kind of “objective prior” in that it is chosen without reference to anyone’s subjective opinion, it is very different from the Jeffreys prior <span class="math inline">\$\\text{Beta}\\left(\\frac{1}{2},\\frac{1}{2}\\right)\$</span>, which puts greatest weight on <span class="math inline">\$\\theta\$</span> near <span class="math inline">\$0\$</span> and <span class="math inline">\$1\$</span> (where the Fisher information is greatest). By contrast, <span class="math inline">\$\\Lambda^\*\$</span> places greatest weight near <span class="math inline">\$\\theta=\\frac{1}{2}\$</span>, where the problem of estimating <span class="math inline">\$\\theta\$</span> is the most difficult (at least, as measured by squared error in the probability parameter).

<figure class="figure">
<p><img src="minimax-estimation_files/figure-html/unnamed-chunk-2-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

Unfortunately, this is quite a bad estimator throughout most of the parameter space, at least for large <span class="math inline">\$n\$</span>. Consider comparing the minimax estimator to the UMVU estimator <span class="math inline">\$\\delta\_0 = X/n\$</span>, whose MSE is <span class="math inline">\$\\frac{\\Var\_\\theta(X)}{n^2}=\\frac{\\theta(1-\\theta)}{n}\$</span>: <span class="math display">\\$$ \\frac{\\text{MSE}(\\theta;\\delta\_{0})}{\\text{MSE}(\\theta;\\delta\_{\\alpha^\*})} = \\frac{\\theta(1-\\theta)/n}{n/4(n+\\sqrt{n})^2} = 4\\theta(1-\\theta)\\cdot (1+n^{-1/2})^2. \\$$</span> This ratio is maximized at <span class="math inline">\$\\theta=\\frac{1}{2}\$</span>, where the UMVU estimator is indeed suboptimal by a factor of <span class="math inline">\$(1+n^{-1/2})^2\\approx 1+2n^{-1/2}\$</span> — so the advantage increasingly minuscule as <span class="math inline">\$n\$</span> gets large. But elsewhere in the parameter space, the UMVU is dramatically better: at <span class="math inline">\$\\theta = 0.01\$</span>, the ratio is about <span class="math inline">\$0.04\$</span> so the UMVU estimator is beating the minimax estimator by a factor of <span class="math inline">\$\\approx 25\$</span>, at least for large <span class="math inline">\$n\$</span>. The issue here is that the minimax estimator is overwhelmingly focusing on doing well in the center of the parameter space, where it is hardest to estimate <span class="math inline">\$\\theta\$</span>, at least as measured by MSE, and paying a severe price in easier regions of the parameter space.

<figure class="figure">
<p><img src="minimax-estimation_files/figure-html/unnamed-chunk-3-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

## <span class="header-section-number">1.4</span> Least Favorable Sequence {.anchored number="1.4" anchor-id="least-favorable-sequence"}

Sometimes there is no least favorable prior, because <span class="math inline">\$\\sup\_\\Lambda r\_\\Lambda\$</span> is not attainable, but a sequence <span class="math inline">\$\\Lambda\_1,\\Lambda\_2,\\ldots\$</span> is least favorable in the sense defined above, that <span class="math inline">\$\\lim\_n r\_{\\Lambda\_n} = \\sup\_\\Lambda r\_\\Lambda\$</span>.

**Theorem:** Suppose <span class="math inline">\$\\delta\$</span> is an estimator and <span class="math inline">\$\\Lambda\_1,\\Lambda\_2,\\ldots\$</span> is a sequence of priors such that <span class="math display">\\$$ \\sup\_\\theta R(\\theta;\\delta) = \\lim\_{n\\to\\infty} r\_{\\Lambda\_n}. \\$$</span> Then <span class="math inline">\$\\delta\$</span> is minimax, the sequence is least favorable, and <span class="math inline">\$r^\* = \\lim\_n r\_{\\Lambda\_n}\$</span>.

*Proof:* Our proof follows the same structure as our previous theorem. For another estimator <span class="math inline">\$\\tilde\\delta\$</span>, and any <span class="math inline">\$n\$</span>, <span class="math display">\\$$ \\begin{aligned} \\sup\_\\theta R(\\theta;\\tilde\\delta) &\\geq \\int R(\\theta; \\tilde\\delta)\\,d\\Lambda\_n(\\theta)\\\\ &\\geq r\_{\\Lambda\_n} \\end{aligned} \\$$</span> As a result, we have <span class="math display">\\$$ \\sup\_\\theta R(\\theta;\\tilde\\delta) \\geq \\lim\_{n\\to\\infty} r\_{\\Lambda\_n} = \\sup\_\\theta R(\\theta;\\delta), \\$$</span> and <span class="math inline">\$\\delta\$</span> is minimax. Moreover, <span class="math display">\\$$ \\lim\_{n\\to\\infty} r\_{\\Lambda\_n} \\leq r^\* \\leq \\sup\_\\theta R(\\theta;\\delta) = \\lim\_{n\\to\\infty} r\_{\\Lambda\_n}, \\$$</span> so the sequence is least favorable and <span class="math inline">\$\\lim\_{n\\to\\infty} r\_{\\Lambda\_n}=r^\*\$</span>. <span class="math inline">\$\\blacksquare\$</span>

## <span class="header-section-number">1.5</span> Bounding the minimax risk {.anchored number="1.5" anchor-id="bounding-the-minimax-risk"}

Outside of simple examples, it’s often difficult to find minimax estimators in finite samples, but minimax bounds are very commonly used in statistical theory to characterize the hardness of a problem.

### <span class="header-section-number">1.5.1</span> Application 1: near-optimal estimators. {.anchored number="1.5.1" anchor-id="application-1-near-optimal-estimators."}

As one application, we might exhibit an estimator that has other nice properties such as ease of calculation, unbiasedness, an appealing functional form, or a natural inductive bias that we expect to make it perform well in certain settings of interest. It is also nice if we can show that the estimator is not far from minimax optimal.

We can do this by calculating our estimator’s sup-risk and comparing it to the Bayes risk of any Bayes estimator. If (say) the former is only <span class="math inline">\$10\\%\$</span> greater than the latter, then we can say our estimator is within <span class="math inline">\$10\\%\$</span> of minimax optimality.

### <span class="header-section-number">1.5.2</span> Application 2: Problem Hardness. {.anchored number="1.5.2" anchor-id="application-2-problem-hardness."}

Another common application of minimaxity is to quantify the difficulty of a problem in some asymptotic regime; i.e. the hardness of a sequence of problems indexed by an asymptotic parameter <span class="math inline">\$n\$</span> (commonly the sample size). If we can find an upper bound by calculating or bounding the sup-risk of an estimator <span class="math inline">\$\\delta\_n\$</span>, and also a lower bound by calculating or bounding the Bayes risk for a prior <span class="math inline">\$\\Lambda\_n\$</span>, then we can sandwich the minimax risk <span class="math inline">\$r\_n^\*\$</span> as <span class="math display">\\$$ r\_{\\Lambda\_n} \\leq r\_n^\* \\leq \\sup\_\\theta R\_n(\\theta; \\delta\_n). \\$$</span> If the upper and lower bounds shrink (or grow) at the same rate in <span class="math inline">\$n\$</span>, then <span class="math inline">\$r\_n^\*\$</span> must also shrink (or grow) at that rate. This rate is called the problem’s **minimax rate**.

A caveat for this approach is that calculating a problem’s minimax risk may inappropriately focus attention on a small corner of the parameter space where the problem is especially hard. It’s possible that it matters more what is happening elsewhere.

Caveat: A problem might be easy throughout most of parameter space but very hard in some bizarre corner we never encounter in practice.

---

[← Minimax Estimation {#minimax-estimation .title}](01-minimax-estimation-minimax-estimation-title.md) · [Up: contents](index.md)
