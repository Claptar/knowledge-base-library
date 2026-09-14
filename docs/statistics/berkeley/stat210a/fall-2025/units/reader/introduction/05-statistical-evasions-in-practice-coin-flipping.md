---
title: 'Statistical evasions in practice: coin flipping'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/introduction.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/introduction.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Statistical evasions in practice: coin flipping

**Source:** [`units/reader/introduction.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/introduction.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

#### Are coins really fair? {.anchored anchor-id="are-coins-really-fair"}

Although physical randomizers like coins and dice seem to be the firmest ground on which we can build a theory of probability, recent work has made the surprising finding that most human flippers have a somewhat greater than 50% chance of seeing their coin land on the same side as it started, due to the physics of rotating objects. This was first hypothesized in a theoretical article by Diaconis, Holmes, and Montgomery in 2007, and confirmed in a large experiment by Bartos et al. (2023), in which 48 human coin flippers collectively flipped <span class="math inline">\$n=350,757\$</span> coins — finding, indeed, that <span class="math inline">\$178,079\$</span> (<span class="math inline">\$50.77\\%\$</span>) of the coins landed on the same side as they started.

In fact, Bartos et al. collected a lot more data than this: each of the 48 flippers recorded the full sequence of all of their coin flips, including which type of coin they were using (coins minted in 46 different countries were used). All flippers even had to submit video of themselves flipping the coins. But the analysis in the next section will use only the summary statistic <span class="math inline">\$X = 178,079\$</span>, which records the number of flips that landed same-side-up.

#### Frequentist analysis in the binomial model {.anchored anchor-id="frequentist-analysis-in-the-binomial-model"}

The data set is simple to analyze if we make two seemingly innocuous simplifying assumptions: first, that the flips were statistically independent, and second, that every flip had an equal probability, which we will call <span class="math inline">\$\\theta\$</span>, of landing on the same side it started on. In that case, we can conclude (deductively) that the probability that <span class="math inline">\$x\$</span> out of the <span class="math inline">\$n\$</span> flips land on the same side is exactly <span class="math inline">\$\\binom{n}{x} \\theta^x(1-\\theta)^{n-x}\$</span>, for the realizable values <span class="math inline">\$x=0,\\ldots,n\$</span>.

If we accept these assumptions, we arrive at a one-parameter **statistical model** for the entire data set, called the **binomial model**. We abbreviate this by writing <span class="math inline">\$X \\sim \\text{Binom}(n,\\theta)\$</span>. If DHM’s prediction was right and a same-side bias exists, then we should have <span class="math inline">\$\\theta &gt; 0.5\$</span>; if they are wrong and the starting side makes no difference, we should have <span class="math inline">\$\\theta = 0.5\$</span>.

Following the frequentist paradigm, we can estimate the parameter <span class="math inline">\$\\theta\$</span> via the **estimator** <span class="math inline">\$\\hat\\theta = X/n\$</span>, in this case <span class="math inline">\$0.5077\$</span>. One thing we will prove in this class is that <span class="math inline">\$X/n\$</span> is the best estimator of <span class="math inline">\$\\theta\$</span>, among all **unbiased** estimators, meaning all estimators for which <span class="math inline">\$\\EE\_\\theta \\hat\\theta = \\theta\$</span>, for all possible values of the parameter <span class="math inline">\$\\theta \\in $$0,1$$\$</span>. This is an example of inductive behavior: if we use the estimator <span class="math inline">\$X/n\$</span> to estimate <span class="math inline">\$\\theta\$</span>, we will get the answer right on average, and our estimate will be as precise (on average) as it could possibly be, for any unbiased estimator. We can also say how variable our estimator is: its standard error (the term of art we use for the standard deviation of an estimator) is <span class="math inline">\$\\sqrt{\\theta(1-\\theta)}/n\$</span>. Substituting our estimator <span class="math inline">\$\\hat\\theta\$</span> for the true value <span class="math inline">\$\\theta\$</span>, we estimate that <span class="math inline">\$\\hat\\theta\$</span> is typically off by about <span class="math inline">\$0.00084\$</span>, so we have good reason to believe our estimate <span class="math inline">\$\\hat\\theta = 0.5077\$</span> is about that close to the true value of <span class="math inline">\$\\theta\$</span>. But we can’t necessarily say that it was close in this experiment; we could have gotten unlucky.

Can we confidently conclude, *inductively*, that there is a same-side bias (<span class="math inline">\$\\theta &gt; 0.5\$</span>)? Naturally, even if DHM were wrong and there were no same-side bias (<span class="math inline">\$\\theta = 0.5\$</span>), we would expect <span class="math inline">\$X/n\$</span> to deviate somewhat from <span class="math inline">\$0.5\$</span> in any given experiment, just by random chance. Could it be that that is what happened in this experiment?

Frequentist analysis evades this question and substitutes another question in its place. Using the `R` function `binom.test`, we can test the null hypothesis that <span class="math inline">\$\\theta = 0.5\$</span> and calculate a <span class="math inline">\$95\\%\$</span> confidence interval for <span class="math inline">\$\\theta\$</span>:

``` {.sourceCode .r .code-with-copy}
binom.test(x = 178079, n = 350757, p = 0.5, alternative = "greater")
```


        Exact binomial test

    data:  178079 and 350757
    number of successes = 178079, number of trials = 350757, p-value <
    2.2e-16
    alternative hypothesis: true probability of success is greater than 0.5
    95 percent confidence interval:
     0.5063091 1.0000000
    sample estimates:
    probability of success
                 0.5076991

The <span class="math inline">\$p\$</span>-value tells us the likelihood that we could observe as many same-side flips as we did, if <span class="math inline">\$\\theta\$</span> really were <span class="math inline">\$0.5\$</span>. In this experiment the <span class="math inline">\$p\$</span>-value is so small (<span class="math inline">\$p &lt; 2.2\\times 10^{-16}\$</span>) that `R` doesn’t bother to tell us its exact value. The probability involved in calculating the <span class="math inline">\$p\$</span>-value follows from our binomial assumptions, but most reasonable people would probably accept this as sufficient evidence to reject the null hypothesis; that is, to reach the inductive conclusion that <span class="math inline">\$\\theta\$</span> is not really <span class="math inline">\$0.5\$</span>.

This is a risky conclusion! Even if we were so conservative as to reject the null hypothesis only when <span class="math inline">\$p &lt; 10^{-10}\$</span>, say, there would still be some chance of our making a mistake in any given experiment. But we have quantified how likely this is, and we can decide whether it is high enough to trouble us.

Beyond just knowing that a same-side bias exists, it is interesting to have some sense of how large it is. Using very similar logic to the hypothesis test, the `binom.test` function also returns a <span class="math inline">\$95\\%\$</span> **confidence interval** <span class="math inline">\$$$50.6\\%, 50.9\\%$$\$</span> for the parameter <span class="math inline">\$\\theta\$</span>. We will explore how to construct confidence intervals later in the semester, but for now it is sufficient to know that the interval is defined so that it has at least a <span class="math inline">\$95\\%\$</span> chance of covering (i.e., including) <span class="math inline">\$\\theta\$</span> in any given experiment, no matter what value <span class="math inline">\$\\theta\$</span> takes. This is another example of inductive behavior: in producing a confidence interval, we take a risk that our inductive conclusion, in this case “<span class="math inline">\$\\theta\$</span> lies between <span class="math inline">\$0.0506\$</span> and <span class="math inline">\$0.0509\$</span>,” will be wrong. But we are behaving in such a way that we can quantify and limit this risk.

#### Bayesian analysis {.anchored anchor-id="bayesian-analysis"}

Another route we could take, if we have a more Bayesian bent, is to introduce another assumption about the distribution that <span class="math inline">\$\\theta\$</span> has; for example, that <span class="math inline">\$\\theta \\sim \\text{Unif}$$0,1$$\$</span>. This is a stronger assumption than we made before: in what sense does <span class="math inline">\$\\theta\$</span> have this distribution? Compared with the other assumptions, it is very difficult to test: there is only one draw from the distribution of <span class="math inline">\$\\theta\$</span>, and it is observed only indirectly through the coin flips. However, it turns out in this case not to matter much what prior we picked, in the sense that many other prior distributions would result in almost the same posterior distribution.

If we make this assumption about the distribution of <span class="math inline">\$\\theta\$</span>, then we can directly calculate the conditional distribution after observing <span class="math inline">\$X = 178,079\$</span>. The posterior distribution for <span class="math inline">\$\\theta\$</span> can be calculated analytically, giving probability density <span class="math display">\\$$ \\theta \\mid X = x \\sim \\frac{(n + 1)!}{x!(n-x)!} \\theta^x (1-\\theta)^{n-x}, \\quad \\text{ for } \\theta \\in \[0,1$$. \\\]</span> This distribution is called the **Beta distribution** with parameters <span class="math inline">\$\\alpha = x+1\$</span> and <span class="math inline">\$\\beta = n-x+1\$</span>. Note that this expression is a probability density for the parameter <span class="math inline">\$\\theta\$</span>, not a distribution for the data <span class="math inline">\$X\$</span>. Once we know the distribution of <span class="math inline">\$\\theta\$</span> we can make claims about it: for example, after seeing the data, there is only a <span class="math inline">\$3.8 \\times 10^{-20}\$</span> chance that <span class="math inline">\$\\theta \\leq 0.5\$</span>. We can also calculate a <span class="math inline">\$95\\%\$</span> Bayesian **credible interval**, which includes <span class="math inline">\$95\\%\$</span> of the posterior probability mass. In this case, the interval is <span class="math inline">\$$$50.6\\%, 50.9\\%$$\$</span>, coinciding with the frequentist confidence interval to several decimal points. The credible interval is making a stronger claim than the confidence interval: it is saying, *in this experiment*, there is a <span class="math inline">\$95\\%\$</span> chance that <span class="math inline">\$\\theta\$</span> falls in the range we calculated.

#### Questioning the binomial model {.anchored anchor-id="questioning-the-binomial-model"}

Bartos et al. stated in their paper that the binomial model is not quite correct: some human flippers had more same-side bias than others. We can modify the binomial model to allow for a different same-side probability <span class="math inline">\$\\theta\_i\$</span> for flipper <span class="math inline">\$i\$</span> over their <span class="math inline">\$n\_i\$</span> coin flips (with <span class="math inline">\$\\sum\_i n\_i = n\$</span>). If we retain the independence assumption, this leads to a more complex model where <span class="math inline">\$X\_i \\sim \\text{Binom}(n\_i,\\theta\_i)\$</span> independently for each <span class="math inline">\$i = 1, \\ldots, 48\$</span>.

There was also evidence that the flippers were improving over time. If we want to accommodate this information we can expand the model yet again, to allow <span class="math inline">\$X\_{i,t} \\sim \\text{Bernoulli}(\\theta\_{i,t})\$</span> independently for <span class="math inline">\$i = 1,\\ldots,48\$</span> and <span class="math inline">\$t = 1,\\ldots, n\_i\$</span>. We might add the constraint that for each <span class="math inline">\$i\$</span>, we have <span class="math inline">\$\\theta\_{i,1} \\geq \\theta\_{i,2} \\geq \\cdots \\geq \\theta\_{i,n\_i}\$</span>. With <span class="math inline">\$n = 350,757\$</span> parameters, one for every data point, this is effectively a nonparametric model. We will return to these models in future lectures.

#### Questions we’ll return to {.anchored anchor-id="questions-well-return-to"}

This example is complex enough to give us a glimpse of some of the questions we’ll be interested in throughout the semester:

1.  **Bayesian vs frequentist frameworks:** What are the pros and cons of each? Where does the prior come from, and how important is our choice of prior for the analysis?

2.  **Sufficiency:** The first binomial analysis summarized the data as just the number <span class="math inline">\$X\$</span> of total same-side flips, even though we have a lot more data than that (for one thing, we know the full sequence of flips for each flipper). As we’ll see, under the binomial model we lose nothing by summarizing the full data set by <span class="math inline">\$X\$</span> alone and forgetting everything else about it. What is it about the structure of the binomial model that makes this a complete summary?

3.  **Estimation:** What is a good way to estimate the parameters in each of these models? In the second model with a different <span class="math inline">\$\\theta\_i\$</span> for each flipper, how can / should our estimate for one flipper be informed by the data from the other <span class="math inline">\$47\$</span> flippers? In the third model, if we want to introduce a parametric functional form for the way <span class="math inline">\$\\theta\_{i,t}\$</span> changes with time, what would be a good model and how should we estimate it?

4.  **Testing:** In the basic binomial model, if we want to conclude with as much confidence as we can that there is some same-side bias, we might want to test the hypothesis <span class="math inline">\$H\_0:\\;\\theta \\leq 0.5\$</span> vs <span class="math inline">\$H\_1: \\;\\theta &gt; 0.5\$</span>. As it turns out, there is a unique best way to do this: reject when <span class="math inline">\$X\$</span> is large. In the second model, we might want to test whether we really need different <span class="math inline">\$\\theta\_i\$</span> values for the different flippers, by testing <span class="math inline">\$H\_0:\\; \\theta\_1=\\theta\_2=\\cdots=\\theta\_{48}\$</span> against <span class="math inline">\$H\_1:\\; \\text{not all } \\theta\_i \\text{ are equal}\$</span>. That is, we test the null that the first model was adequate. This is a more complex testing problem for two reasons: our null hypothesis has a nuisance parameter, which may affect the null distribution of any test statistic; and our <span class="math inline">\$48\$</span>-dimensional alternative distribution can vary from the <span class="math inline">\$1\$</span>-dimensional null model in many, many different directions. As we’ll see, it can matter a lot which alternative directions are prioritized by the test we select.

5.  **Asymptotics:** In analyzing this data set we will never actually calculate anything like <span class="math inline">\$350,757!\$</span> even though that quantity appears in the equations. In practice we replace the binomial model with an appropriate Normal model, in this case <span class="math inline">\$X \\sim \\cN(n\\theta, n\\theta(1-\\theta))\$</span>, and do the calculations with respect to that model. The normal approximation here is an obvious consequence of the central limit theorem, but we can make similar approximations in a lot of other problems where it is not so obvious *a priori* that this would be possible.

---

[← The problem of induction](04-the-problem-of-induction.md) · [Up: contents](index.md)
