---
title: 'Statistical evasions in practice: coin flipping'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/introduction.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/introduction.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Statistical evasions in practice: coin flipping

**Source:** [`reader/introduction.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/introduction.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

#### Are coins really fair?

Although physical randomizers like coins and dice seem to be the firmest ground on which we can build a theory of probability, recent work has made the surprising finding that most human flippers have a somewhat greater than 50% chance of seeing their coin land on the same side as it started, due to the physics of rotating objects. This was first hypothesized in a theoretical article by Diaconis, Holmes, and Montgomery in 2007, and confirmed in a large experiment by Bartos et al. (2023), in which 48 human coin flippers collectively flipped $n=350,757$ coins — finding, indeed, that $178,079$ ($50.77\%$) of the coins landed on the same side as they started.

In fact, Bartos et al. collected a lot more data than this: each of the 48 flippers recorded the full sequence of all of their coin flips, including which type of coin they were using (coins minted in 46 different countries were used). All flippers even had to submit video of themselves flipping the coins. But the analysis in the next section will use only the summary statistic $X = 178,079$, which records the number of flips that landed same-side-up.

#### Frequentist analysis in the binomial model

The data set is simple to analyze if we make two seemingly innocuous simplifying assumptions: first, that the flips were statistically independent, and second, that every flip had an equal probability, which we will call $\theta$, of landing on the same side it started on. In that case, we can conclude (deductively) that the probability that $x$ out of the $n$ flips land on the same side is exactly $\binom{n}{x} \theta^x(1-\theta)^{n-x}$, for the realizable values $x=0,\ldots,n$.

If we accept these assumptions, we arrive at a one-parameter **statistical model** for the entire data set, called the **binomial model**. We abbreviate this by writing $X \sim \text{Binom}(n,\theta)$. If DHM's prediction was right and a same-side bias exists, then we should have $\theta > 0.5$; if they are wrong and the starting side makes no difference, we should have $\theta = 0.5$.

Following the frequentist paradigm, we can estimate the parameter $\theta$ via the **estimator** $\hat\theta = X/n$, in this case $0.5077$. One thing we will prove in this class is that $X/n$ is the best estimator of $\theta$, among all **unbiased** estimators, meaning all estimators for which $\EE_\theta \hat\theta = \theta$, for all possible values of the parameter $\theta \in [0,1]$. This is an example of inductive behavior: if we use the estimator $X/n$ to estimate $\theta$, we will get the answer right on average, and our estimate will be as precise (on average) as it could possibly be, for any unbiased estimator. We can also say how variable our estimator is: its standard error (the term of art we use for the standard deviation of an estimator) is $\sqrt{\theta(1-\theta)}/n$. Substituting our estimator $\hat\theta$ for the true value $\theta$, we estimate that $\hat\theta$ is typically off by about $0.00084$, so we have good reason to believe our estimate $\hat\theta = 0.5077$ is about that close to the true value of $\theta$. But we can't necessarily say that it was close in this experiment; we could have gotten unlucky.

Can we confidently conclude, *inductively*, that there is a same-side bias ($\theta > 0.5$)? Naturally, even if DHM were wrong and there were no same-side bias ($\theta = 0.5$), we would expect $X/n$ to deviate somewhat from $0.5$ in any given experiment, just by random chance. Could it be that that is what happened in this experiment?

Frequentist analysis evades this question and substitutes another question in its place. Using the `R` function `binom.test`, we can test the null hypothesis that $\theta = 0.5$ and calculate a $95\%$ confidence interval for $\theta$:

```R
binom.test(x = 178079, n = 350757, p = 0.5, alternative = "greater")
```

The $p$-value tells us the likelihood that we could observe as many same-side flips as we did, if $\theta$ really were $0.5$. In this experiment the $p$-value is so small ($p < 2.2\times 10^{-16}$) that `R` doesn't bother to tell us its exact value. The probability involved in calculating the $p$-value follows from our binomial assumptions, but most reasonable people would probably accept this as sufficient evidence to reject the null hypothesis; that is, to reach the inductive conclusion that $\theta$ is not really $0.5$.

This is a risky conclusion! Even if we were so conservative as to reject the null hypothesis only when $p < 10^{-10}$, say, there would still be some chance of our making a mistake in any given experiment. But we have quantified how likely this is, and we can decide whether it is high enough to trouble us.

Beyond just knowing that a same-side bias exists, it is interesting to have some sense of how large it is. Using very similar logic to the hypothesis test, the `binom.test` function also returns a $95\%$ **confidence interval** $[50.6\%, 50.9\%]$ for the parameter $\theta$. We will explore how to construct confidence intervals later in the semester, but for now it is sufficient to know that the interval is defined so that it has at least a $95\%$ chance of covering (i.e., including) $\theta$ in any given experiment, no matter what value $\theta$ takes. This is another example of inductive behavior: in producing a confidence interval, we take a risk that our inductive conclusion, in this case "$\theta$ lies between $0.0506$ and $0.0509$," will be wrong. But we are behaving in such a way that we can quantify and limit this risk.

#### Bayesian analysis

Another route we could take, if we have a more Bayesian bent, is to introduce another assumption about the distribution that $\theta$ has; for example, that $\theta \sim \text{Unif}[0,1]$. This is a stronger assumption than we made before: in what sense does $\theta$ have this distribution? Compared with the other assumptions, it is very difficult to test: there is only one draw from the distribution of $\theta$, and it is observed only indirectly through the coin flips. However, it turns out in this case not to matter much what prior we picked, in the sense that many other prior distributions would result in almost the same posterior distribution.

If we make this assumption about the distribution of $\theta$, then we can directly calculate the conditional distribution after observing $X = 178,079$. The posterior distribution for $\theta$ can be calculated analytically, giving probability density $$
\theta \mid X = x \sim  \frac{(n + 1)!}{x!(n-x)!} \theta^x (1-\theta)^{n-x}, \quad \text{ for } \theta \in [0,1].
$$ This distribution is called the **Beta distribution** with parameters $\alpha = x+1$ and $\beta = n-x+1$. Note that this expression is a probability density for the parameter $\theta$, not a distribution for the data $X$. Once we know the distribution of $\theta$ we can make claims about it: for example, after seeing the data, there is only a $3.8 \times 10^{-20}$ chance that $\theta \leq 0.5$. We can also calculate a $95\%$ Bayesian **credible interval**, which includes $95\%$ of the posterior probability mass. In this case, the interval is $[50.6\%, 50.9\%]$, coinciding with the frequentist confidence interval to several decimal points. The credible interval is making a stronger claim than the confidence interval: it is saying, *in this experiment*, there is a $95\%$ chance that $\theta$ falls in the range we calculated.

#### Questioning the binomial model

Bartos et al. stated in their paper that the binomial model is not quite correct: some human flippers had more same-side bias than others. We can modify the binomial model to allow for a different same-side probability $\theta_i$ for flipper $i$ over their $n_i$ coin flips (with $\sum_i n_i = n$). If we retain the independence assumption, this leads to a more complex model where $X_i \sim \text{Binom}(n_i,\theta_i)$ independently for each $i = 1, \ldots, 48$.

There was also evidence that the flippers were improving over time. If we want to accommodate this information we can expand the model yet again, to allow $X_{i,t} \sim \text{Bernoulli}(\theta_{i,t})$ independently for $i = 1,\ldots,48$ and $t = 1,\ldots, n_i$. We might add the constraint that for each $i$, we have $\theta_{i,1} \geq \theta_{i,2} \geq \cdots \geq \theta_{i,n_i}$. With $n = 350,757$ parameters, one for every data point, this is effectively a nonparametric model. We will return to these models in future lectures.

#### Questions we'll return to

This example is complex enough to give us a glimpse of some of the questions we'll be interested in throughout the semester:

1.  **Bayesian vs frequentist frameworks:** What are the pros and cons of each? Where does the prior come from, and how important is our choice of prior for the analysis?

2.  **Sufficiency:** The first binomial analysis summarized the data as just the number $X$ of total same-side flips, even though we have a lot more data than that (for one thing, we know the full sequence of flips for each flipper). As we'll see, under the binomial model we lose nothing by summarizing the full data set by $X$ alone and forgetting everything else about it. What is it about the structure of the binomial model that makes this a complete summary?

3.  **Estimation:** What is a good way to estimate the parameters in each of these models? In the second model with a different $\theta_i$ for each flipper, how can / should our estimate for one flipper be informed by the data from the other $47$ flippers? In the third model, if we want to introduce a parametric functional form for the way $\theta_{i,t}$ changes with time, what would be a good model and how should we estimate it?

4.  **Testing:** In the basic binomial model, if we want to conclude with as much confidence as we can that there is some same-side bias, we might want to test the hypothesis $H_0:\;\theta \leq 0.5$ vs $H_1: \;\theta > 0.5$. As it turns out, there is a unique best way to do this: reject when $X$ is large. In the second model, we might want to test whether we really need different $\theta_i$ values for the different flippers, by testing $H_0:\; \theta_1=\theta_2=\cdots=\theta_{48}$ against $H_1:\; \text{not all } \theta_i \text{ are equal}$. That is, we test the null that the first model was adequate. This is a more complex testing problem for two reasons: our null hypothesis has a nuisance parameter, which may affect the null distribution of any test statistic; and our $48$-dimensional alternative distribution can vary from the $1$-dimensional null model in many, many different directions. As we'll see, it can matter a lot which alternative directions are prioritized by the test we select.

5.  **Asymptotics:** In analyzing this data set we will never actually calculate anything like $350,757!$ even though that quantity appears in the equations. In practice we replace the binomial model with an appropriate Normal model, in this case $X \sim \cN(n\theta, n\theta(1-\theta))$, and do the calculations with respect to that model. The normal approximation here is an obvious consequence of the central limit theorem, but we can make similar approximations in a lot of other problems where it is not so obvious *a priori* that this would be possible.

---

[← The problem of induction](03-the-problem-of-induction.md) · [Up: contents](index.md)
