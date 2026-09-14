---
title: Asymptotics Part 02 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/asymptotics.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/asymptotics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Asymptotics Part 02 —

**Source:** [`units/reader/asymptotics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/asymptotics.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

So far, everything we have seen in this class has dealt with the exact distributions of finite data sets. In many cases we have needed to exploit special properties of the model <span class="math inline">\$\\cP\$</span> (e.g., that it has a complete sufficient statistic, it is an exponential family, it is a multivariate Gaussian distribution, etc.) to make exact calculations easier. In generic models, however, the tools we have learned so far may fail us.

For generic models, exact calculations may be intractable or impossible. However, we may be able to approximate our problem with a simpler problem in which calculations are easy. Typically, we approximate by Gaussian by taking the limit as observations <span class="math inline">\$n \\to \\infty\$</span>. This is only interesting if the approximation is good for reasonable sample sizes, but fortunately it very often is.

### <span class="header-section-number">1.1</span> Example: Logistic regression {.anchored number="1.1" anchor-id="example-logistic-regression"}

To take a specific example, suppose that we modify the linear regression example from the last lecture to allow for a binary rather than a continuous response. We retain the feature vector <span class="math inline">\$x\_i \\in \\RR^d\$</span> and regression coefficients <span class="math inline">\$\\beta \\in \\RR^d\$</span>, but instead of observing outcome <span class="math inline">\$y\_i \\simind N(\\beta'x\_i, \\sigma^2)\$</span>, we now observe <span class="math inline">\$y\_i \\simind \\text{Bern}(\\mu(\\beta'x\_i))\$</span>, where

<span class="math display">\\$$ \\mu(\\eta) = \\frac{e^{\\eta}}{1+e^{\\eta}}. \\$$</span> Define the *mean response* <span class="math inline">\$\\mu\_i = \\mu(\\beta'x\_i)\$</span> and *linear predictor* <span class="math inline">\$\\eta\_i = \\log \\frac{\\mu\_i}{1-\\mu\_i} = \\beta'x\_i\$</span>.

Unlike the linear regression model, we cannot simply rotate the response vector into a canonical basis without destroying the structure of our model; the entries of the rotated response vector would be neither Bernoulli nor independent.

We might still hope to make progress by observing that we have an exponential family model, since <span class="math display">\\$$ \\begin{aligned} p\_\\beta(y \\mid X) &= \\prod\_{i=1}^n \\mu\_i^{y\_i}(1-\\mu\_i)^{1-y\_i}\\\\ &= \\prod\_{i=1}^n \\exp\\left\\{\\beta'x\_i y\_i + \\log(1-\\mu(\\beta'x\_i))\\right\\}\\\\ &= \\exp\\left\\{\\beta'X'y - A(\\beta;X)\\right\\}, \\end{aligned} \\$$</span> a <span class="math inline">\$d\$</span>-parameter exponential family on <span class="math inline">\$\\mathcal{Y} = \\{0,1\\}^n\$</span> with natural parameter <span class="math inline">\$\\beta\$</span>, complete sufficient statistic <span class="math inline">\$X'y\$</span>, and normalizing constant <span class="math inline">\$A(\\beta; X) = - \\sum\_i \\log (1+e^{\\beta'x\_i})\$</span>. Note <span class="math inline">\$A\$</span> depends only on <span class="math inline">\$\\beta\$</span> and the design matrix <span class="math inline">\$X\$</span>, which we typically treat as fixed (possibly after conditioning on it, if it is “really” random).

If we want to estimate <span class="math inline">\$\\beta\$</span>, we might hope for a UMVU estimator. Unfortunately, no unbiased estimator could possibly exist: any estimator <span class="math inline">\$\\hat\\beta\_j\$</span> would have some largest value that it can take on the finite sample space <span class="math inline">\$\\mathcal{Y}\$</span>, and its expectation can never be larger than that value, even though <span class="math inline">\$\\beta\_j\$</span> can range over the entire real line. We could also come up with a Bayes estimator, but we would have to specify a joint distribution over the parameter vector <span class="math inline">\$\\beta \\in \\RR^d\$</span>, which we might not wish to do.

Likewise, we might want to test a hypothesis like <span class="math inline">\$H\_0:\\;\\beta\_j = 0\$</span> vs <span class="math inline">\$H\_1:\\;\\beta\_j \\neq 0\$</span>. Again, we might think we are in good shape due to the exponential family form: all we have to do is condition on <span class="math inline">\$X\_{-j}'y\$</span> and then reject for conditionally large values of <span class="math inline">\$X\_j'y\$</span>. Unfortunately, however, this is also typically a nonstarter: if one of the features <span class="math inline">\$X\_k\$</span> takes continuous values, then the entire vector <span class="math inline">\$y\$</span> can be recovered from observing only <span class="math inline">\$X\_k'y = \\sum\_{i:y\_i=1} x\_{i,k}\$</span> if all <span class="math inline">\$2^n\$</span> such partial sums are distinct. In that case, the only unbiased test is the trivial constant test that ignores the response vector <span class="math inline">\$y\$</span> and rejects with probability <span class="math inline">\$\\alpha\$</span>.

Fortunately, if <span class="math inline">\$n\$</span> is “large” then we can apply general-purpose asymptotic methods to come up with very good estimators, tests, or confidence intervals in this problem. Define the *maximum likelihood estimator* <span class="math display">\\$$ \\begin{aligned} \\hat\\beta\_{\\text{MLE}} &= \\argmax\_{\\beta \\in \\RR^d} p\_\\beta(y \\mid X)\\\\ &= \\argmax\_{\\beta \\in \\RR^d} \\beta'X'y - A(\\beta; X), \\end{aligned} \\$$</span> which can be maximized efficiently because the log-likelihood is concave in <span class="math inline">\$\\beta\$</span>.

We’ll show in a future lecture that, under relatively mild conditions, we will have <span class="math display">\\$$ \\hat\\beta\_{\\text{MLE}} \\approx N\_d(\\beta, J(\\beta)^{-1}), \\$$</span> for the Fisher information matrix <span class="math display">\\$$ J(\\beta) = \\Var\_{\\beta}(\\nabla\\ell(\\beta; y, X)) = -\\EE\_\\beta \\nabla^2\\ell(\\beta; y, X) \\$$</span> That is, if <span class="math inline">\$n\$</span> is large then <span class="math inline">\$\\hat\\beta\_{\\text{MLE}}\$</span> approximately follows a Gaussian distribution that is not only approximately unbiased, but its variance-covariance matrix <span class="math inline">\$\\Sigma(\\beta) = J(\\beta)^{-1}\$</span> matches the Cramèr–Rao lower bound.

What is more, the observed value of minus the Hessian matrix gives a good approximation to its expectation, the Fisher information matrix at the true <span class="math inline">\$\\beta\$</span>: <span class="math display">\\$$ \\widehat{\\Sigma}(y,X) = (-\\nabla^2\\ell(\\hat\\beta\_{\\text{MLE}}; y, X))^{-1} \\approx \\Sigma(\\beta) = J(\\beta)^{-1} \\$$</span> For a single coefficient <span class="math inline">\$\\beta\_j\$</span> we can say <span class="math inline">\$\\hat\\beta\_j - \\beta\_j \\approx N(0, \\sigma^2\_{j}(\\beta))\$</span>, for <span class="math inline">\$\\sigma^2\_j(\\beta) = \\Sigma\_{jj}(\\beta))\$</span>, or <span class="math display">\\$$ Z\_j = \\frac{\\hat\\beta\_j - \\beta\_j}{\\hat\\sigma\_j} \\approx N(0,1), \\quad \\text{ for } \\hat\\sigma^2\_j = \\widehat\\Sigma\_{jj}, \\$$</span> leading to natural tests for hypotheses like <span class="math inline">\$H\_0:\\;\\beta\_j = 0\$</span> or the confidence interval <span class="math inline">\$\\hat\\beta\_j \\pm z\_{\\alpha/2} \\sqrt{\\hat\\Sigma\_{jj}}\$</span> for <span class="math inline">\$\\beta\_j\$</span>.

These results do not necessarily require <span class="math inline">\$n\$</span> to be huge; for example, we can simulate the distribution of <span class="math inline">\$\\hat\\beta\_1\$</span> in the logistic regression model <span class="math inline">\$\\eta\_i = \\beta\_0 + \\beta\_1 x\_i\$</span> with an intercept and a single (uniformly distributed) covariate. For <span class="math inline">\$\\beta\_0 = -2\$</span>, <span class="math inline">\$\\beta\_1 = 4\$</span>, and <span class="math inline">\$n = 100\$</span>, the normal approximation appears reasonably good, though it depends on the parameters.

``` {.sourceCode .r .code-with-copy}
set.seed(12345)
n <- 100
beta <- c(-2,4)

B <- 1E4
beta.hat <- matrix(NA, nrow=B, ncol=2)
sigma.hat <- matrix(NA, nrow=B, ncol=2)
for (b in 1:B) {
  x <- runif(n)
  eta <- beta[1] + x * beta[2]
  mu <- exp(eta) / (1+exp(eta))
  y <- 1*(runif(n) < mu)
  mod <- glm(y ~ x, family=binomial)
  ## Estimate is MLE
  beta.hat[b,] <- coef(mod)
  ## Std. error estimate is sqrt(-diag(Hessian) at MLE)
  sigma.hat[b,] <- coef(summary(mod))[,"Std. Error"]
}

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · ["True" Fisher information →](03-true-fisher-information.md)
