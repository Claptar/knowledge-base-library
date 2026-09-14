---
title: try again
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# try again

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

W2 <- t(CIndep %*% beta) %*% solve(CIndep %*% Sigma %*% t(CIndep)) %*% CIndep %*% beta
W2
```


## Model deviance, residuals and goodness-of-fit

 - In linear models, we often use residuals $e_i = y_i - \hat{\mu}_i$ to check model assumptions (linearity, homoscedasticity). However, in a GLM setting, we know that the variance of our residuals will depend on the mean, i.e., $Var(\epsilon_i) = f(\mu_i)$. Using ordinary residuals such as $e_i$ therefore is no longer appropriate.
 - We have seen that the objective function that is used to fit a GLM is the log-likelihood of the data under the posited model. For example, the log likelihood of a Poisson GLM with response variable $\mathbf{Y}$, with elements $Y_i, i \in \{1, \ldots, n\}$ and model matrix $\mathbf{X}$ is
 $$ \ell(\mathbf{Y};  \beta) = \log \prod_{i=1}^n \left( \frac{\exp (\mathbf{X}_i^T \beta)^{Y_i} \exp( - \exp(\mathbf{X}_i^T \beta))}{Y_i!} \right) = \sum_{i=1}^n \log \left( \frac{\exp(\mathbf{X}_i^T \beta)^{Y_i} \exp( - \exp(\mathbf{X}_i^T \beta))}{Y_i!} \right) \\ = \sum_{i=1}^n Y_i (\mathbf{X}_i^T \beta) - \exp(\mathbf{X}_i^T \beta)  - \log Y_i!. $$
 The estimates $\hat{\beta}$ are then found by maximizing $\ell(\beta | \mathbf{Y}, \mathbf{X} )$ with respect to $\beta$. This is analogous to maximizing a Gaussian likelihood in the linear model setting.
 - A goodness-of-fit measure used in the GLM setting is the **residual deviance** $D$ (sometimes referred to simply as 'deviance'), that is twice the difference in log-likelihood between a 'saturated model' and the current model. Here, a saturated model, is a model where we fit one parameter per data point and therefore fit the data perfectly, in other words $\hat{\mu}_i = y_i$. This is,
 $$ D = 2 * \left\{ \ell(\mathbf{Y};  \beta | \hat{\mu}_i = y_i) - \ell(\mathbf{Y};  \beta | \hat{\mu}_i = \exp(\mathbf{X}_i^T \beta)) \right\}.$$
 - From the equation above it becomes clear that the residual deviance is actually a ratio in log-likelihoods and therefore a likelihood ratio test statistic!
 - A low residual deviance can thus be interpreted as a model that is fitting the data well, since your current model will be close in log-likelihood to the saturated model. The deviance is a very useful statistic that is also important in statistical inference and model selection, e.g., for testing if a smaller model fits significantly worse than a larger model.
 - Finally, a **deviance residual** $D_i$ can then be defined as the square root of the contribution of the $i$th datum to the residual deviance
 $$ D_i = sign(Y_i - \exp(\mathbf{X}_i^T \beta)) \sqrt{ 2* \left\{ \ell(Y_i;  \beta | \hat{\mu}_i = y_i) - \ell(Y_i;  \beta | \hat{\mu}_i = \exp(\mathbf{X}_i^T \beta)) \right\} } $$

 ---

 - Another type of residuals commonly used in a GLM setting are **Pearson residuals**. A Pearson residual is defined as
 $$ e_i = \frac{y_i - E(y_i)}{\sqrt{Var(y_i)}},$$
 and we can see that it has the form of a regular residual such as used in liner models (numerator), but normalized according to the variance of the observed response (denominator), to correct for the mean-variance relationship.

 ---

 - **Goodness-of-fit** (GOF) analyses serve to assess how well the model actually fits the observed data. One may view the fitting of a GLM as replacing a set of observed data points $\mathbf{y}$ by a set of fitted values $\hat{\mathbf{\mu}}$ derived from a model. In general $\hat{\mathbf{\mu}} \ne \mathbf{y}$ and the question arises as to how well $\hat{\mathbf{\mu}}$ approximates $\mathbf{y}$. This naturally raises the question of how much of a discrepancy we believe to be tolerable. Two important discrepancy measures are often used in a GLM setting.
 - Note that the **residual deviance** was a likelihood ratio test statistic between a saturated and our current model. This saturated model actually provides us with a baseline as to how well a model can fit the observed data (even if we know that the saturated model is uninformative for summarizing the data). This motivates a statistical test with
 $H_0$: The current model provides a similar fit as the saturated model.
 $H_1$: The current model fits significantly worse than a saturated model.
 - The residual deviance immediately tests this hypothesis using a likelihood ratio test and is therefore a useful goodness-of-fit measure.
 - Another measure of discrepancy is the generalized Pearson $\chi^2$ statistic
 $$ X^2 = \sum_{i=1}^n \frac{(y_i - \hat{\mu}_i)^2}{Var(y_i)} = \sum_{i=1}^n e_i^2,$$
 with $e_i$ the Pearson residual of observation $i$.
  - Asymptotic theory shows that both the residual deviance $D \sim \chi^2_{n-p} | H_0$ and $X^2 \sim \chi^2_{n-p} | H_0$, with $n$ the number of observations in our dataset (and, hence, the number of parameters fitted in our saturated model), and $p$ the number of parameters fitted in our current model.

 ---

 **Exercise**:

 - Verify the residual deviance that is reported in the summary of our model above.
 - Also check if you can recover the correct deviance and Pearson residuals by calculating them yourself. You can get the correct deviance residuals in `R` by `resid(m, type="deviance")` and `resid(m, type="pearson")`.
 - Does your model fit significantly worse than a saturated model?

## Overdispersion

 - Above we have always assumed that the Poisson distribution is valid for the dataset we have been using. However, we never checked for this.
 - As a matter of fact, it often happens that the variance=mean assumption is too stringent for count data. If the variance is larger than the mean, this is referred to as **overdispersion**. Though much less common, underdispersion happens when the variance is smaller than the mean.
 - We can use Pearson residuals to measure overdispersion using the following argument. The Poisson GLM implies that
 $$ Y_i | X, \hat{\beta} \sim Poi(\hat{\mu}_i),$$
 with $\hat{\mu}_i = \exp (\mathbf{X}_i^T \hat{\beta})$. This implies
 $$ Var(Y_i | X, \hat{\beta}) = \hat{\mu}_i.$$
 Since the variance is unaffected by addition we may also write
 $$ Var(Y_i - \hat{\mu}_i | X, \hat{\beta}) = \hat{\mu}_i.$$
 Which is also equal to
 $$ Var\left(\frac{Y_i - \hat{\mu}_i}{\sqrt{Var(Y_i)}} | X, \hat{\beta} \right) = \frac{\hat{\mu}_i}{Var(Y_i)}.$$
 Since we know from the Poisson distribution that $Var(Y_i) = \hat{\mu}_i$, we have that
 $$ Var \left(\frac{Y_i - \hat{\mu}_i}{\sqrt{\hat{\mu}_i}} | X, \hat{\beta} \right) = \frac{\hat{\mu}_i}{\hat{\mu}_i}.$$
 Note that the formulation within the variance at left-hand side of the equation is our definition of Pearson residuals $E_i$. Thus, if the Poisson assumption holds, we can write
 $$ Var(E_i | X, \hat{\beta}) = 1,$$
 which is something we can empirically test using our fitted model. Indeed, **if the variance of our Pearson residuals is much larger than $1$, we are dealing with overdispersion**. As a rough rule, I consider overdispersion to be present if this value is larger than $\sim 1.3$, but this is arbitrary and may depend on the situation (and statistician).

 ---

 - Below, we apply this to the `Bikeshare` dataset. We will notice that the overdispersion is huge! The p-values and standard errors provided by the model can therefore not be trusted!

```r
ePearson <- resid(m, type="pearson")
n <- nrow(Bikeshare)
p <- length(coef(m))
varPearson <- sum((ePearson^2)) / (n - p)
varPearson # HUGE!
```

### Remedies to overdispersion

- The presence of overdispersion tells us that the distributional assumption we have been making does not hold. Overdispersion is a common problem, and luckily we have a few available remedies, as in alternative distributions, although choosing between them may not always be trival.
  - The **negative binomial** (NB) distribution is a popular choice for modeling data that are overdispersed with respect to the Poisson distribution. The NB can be considered as a member of the exponential family and therefore fitted using standard GLM fitting engines. Just like the Poisson distribution, it is a distribution only appropriate for modeling count data. If
  $$ Y_i \sim NB(\mu_i, \phi), $$
  then $E(Y_i) = \mu_i$ and $Var(Y_i) = \mu_i + \phi \mu_i^2$, with $\phi \ge 0$ the **dispersion parameter**. Since $\phi \ge 0$ the variance of the negative binomial is always larger than that of the Poisson distribution, and in fact is now a quadratic (rather than linear) function of the mean. When $\phi = 0$, the NB reduces to the Poisson distribution.
  - The **quasi-Poisson** model is an alternative choice derived using the quasi-likelihood framework developed by [Wedderburn (1974)](https://www.jstor.org/stable/2334725?seq=1#metadata_info_tab_contents). However, only the first two moments (mean and variance) are specified, and all other moments are left unspecified. In particular if model $Y_i$ using a quasi-Poisson model, then $E(Y_i) = \mu_i$ and $Var(Y_i) = \phi \mu_i$, with $\phi \ge 0$ the **(quasi-)dispersion parameter**. Again, since $\phi \ge 0$ the variance of the quasi-Poisson is always larger than that of the Poisson distribution, however, the dispersion parameter here is on the linear scale, and so the mean-variance relationship is still linear as opposed to quadratic in the NB.

 ---

 Below, we fit a negative binomial and quasi-Poisson model in `R`.

```r
## negative binomial
library(MASS)
mNB <- glm.nb(bikers ~ weathersit + humc + I(humc^2) + I(humc^3) + hr,
         data = Bikeshare)
summary(mNB)
mean(resid(mNB, type = "pearson")^2) # no more overdispersion!

## quasi-Poisson
mQP <- glm(bikers ~ weathersit + humc + I(humc^2) + I(humc^3) + hr,
         data = Bikeshare,
         family="quasipoisson")

---

[← identify the linearly independent contrasts](20-identify-the-linearly-independent-contrasts.md) · [Up: contents](index.md) · [Sequencing countData Part 22 — →](22-sequencing-countdata-part-22.md)
