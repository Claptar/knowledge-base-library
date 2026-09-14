---
title: 'Modeling count data: Generalized linear models'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Modeling count data: Generalized linear models

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Just like we have modeled protein abundances in the proteomics module of this course in order to assess differential protein abundance, we can model gene expression counts to identify genes with differences in average expression between groups of samples.

## Why we can('t) use linear models to model count data

 - If we're using a linear model to model a response $Y_i$, with $i \in \{1, \ldots, n\}$ in function of a single covariate $X_i$, the linear model can be defined as follows:

$$
\left\{
\begin{array}{ccc}
Y_i & = & \beta_0 + \beta_1 X_i + \epsilon_i \\
Y_i | X_i & \sim & N(\beta_0 + \beta_1 X_i, \sigma^2 \mathbf{I}).
\end{array}
\right.
$$

 - Or, equivalently, we've seen we can write it in matrix form as
  $$
  \left\{
  \begin{array}{ccc}
  Y_i & = & \mathbf{X}^T_i \beta + \epsilon_i \\
  Y_i | \mathbf{X}_i & \sim & N(\mathbf{X}^T_i \beta, \sigma^2 \mathbf{I}),
  \end{array}
  \right.
  $$
where $\mathbf{X}$ now represents our $n \times p$ design matrix, with row $i$ corresponding to observation $i$.

 ---

 - The variance-covariance matrix of $\mathbf{Y}$ is assumed a diagonal matrix with $\sigma^2$ on the diagonal elements and zero everywhere else. This means that the data points are uncorrelated, and that every observation has the same variance $\sigma^2$, also referred to as homoscedasticity.
 - The latter doesn't hold for count data, due to the mean-variance relationship. This makes linear models, in its basic form, unsuitable to model count data.
 - In addition, count data are non-negative, while there are no such constraints in the standard linear model to make sure that our estimates will be non-negative. Indeed, $\hat{Y}_i = \mathbf{X}^T_i \hat{\beta} \in ] -\infty, \infty[$.

## Generalized linear models

 - As the name suggests, generalized linear models (GLMs) extend linear models. In GLMs, we extend two things with respect to the linear model:
    - The **conditional distribution of the response variable $Y_i | X_i$** can be assumed to follow any distribution that belongs to the **exponential family** of distributions, which includes the Gaussian but also other commonly known distributions, such as the Binomial, Gamma and Poisson distribution.
    - The linear model assumed a linear relationship between $Y_i$ and $X_i$, since we assumed that $E(Y_i | X_i) = \mathbf{X}^T_i \beta$. In GLMs, we will allow a **link function** $g()$ that links the conditional mean to the covariates. Hence, in GLMs we have that $g(E(Y_i | X_i)) = \mathbf{X}^T_i \beta$. Note that each family has got a canonical link function, which is the identity link function $g(\mu) = \mu$ for Gaussian, the log link function $g(\mu) = \log \mu$ for Poisson, or the logit link function $g(\mu) = \log(\frac{\mu}{1-\mu})$ for Binomial.

### A Poisson GLM

 - We can define a Poisson GLM as follows
  $$
  \left\{
  \begin{array}{ccc}
  Y_i & \sim & Poi(\mu_i) \\
  \log \mu_i & = & \eta_i \\
  \eta_i & = & \mathbf{X}^T_i \beta \\
  \end{array}
  \right.
  $$
where $Y_i$ is the response variable, with mean $\mu_i$, $\eta_i$ is the linear predictor, $\mathbf{X}$ is the $n \times p$ model matrix and $\beta$ is the $p \times 1$ matrix of regression coefficients, where $n$ is the number of data points and $p$ the total number of parameters to be estimated.
  - It is insightful to compare this model to a linear model where $Y_i$ is log-transformed. Indeed, in the linear model case, we would be modeling $E(\log Y_i )$, while in the GLM we are modeling $\log E(Y_i)$.
  - This shows that in the GLM setting we are modeling a transformed version of the expected value, and after retransforming we can interpret the fit in terms of the mean of our response variable. In the transformed linear model, however, we are working with the expected value of a transformed version of our response variable, and we will not be able to interpret the fit in terms of the mean, because $E( \log Y_i) \ne \log E(Y_i)$. In this specific case, we would have to resort to interpreting changes in terms of a geometric mean.
  - Also note that $\mathbf{X}^T_i \beta \in ]-\infty, \infty[$, while $Y_i$ must be non-negative $[0, \infty[$. The link function helps with this, since the exponential function transforms any real number to a non-negative number, i.e., $\exp(\mathbf{X}^T_i \beta) \in [0, \infty[$.


### Parameter estimation using maximum likelihood

 - In maximum likelihood, we attempt to **maximize the likelihood function of the data**, under the posited assumptions. The likelihood function is typically parametrized by a limited number of parameters, hence we can find the values of the parameters that maximize the likelihood function.
 - We do this by finding the point on the likelihood function where its first derivative equals zero, as this must be a maximum of the function. For non-convex likelihood functions, this may be a local maximum, but for GLMs the likelihood function is convex and therefore the obtained maximum must be the global maximum.

#### Maximum likelihood for a linear model

For linear models, we can derive an equivalent estimator for $\beta$ using maximum likelihood estimation as we had derived in our recap lecture using least squares estimation. We can define a linear model as

$$
Y_i \sim N(\mu_i, \sigma^2\mathbf{I}) \\
\mu_i = \mathbf{X}_i \mathbf{\beta}
$$

The likelihood function of the data is the product of the likelihoods of each datum. Since we are assuming a Gaussian distribution, we use the Gaussian probability density function:

$$
L(\mathbf{Y}; \beta, \sigma) = \prod_{i=1}^n \frac{1}{\sqrt{2 \pi \sigma^2}} \exp \left\{ - \frac{(Y_i - \mathbf{X}_i \beta)^2}{2 \sigma^2} \right\}
$$

Log-likelihood function

$$
\ell(\mathbf{Y}; \beta, \sigma) = \sum_{i=1}^n \left\{ -\frac{1}{2} \log(2\pi \sigma^2) - \frac{1}{2\sigma^2} (Y_i - \mathbf{X}_i \beta)^2 \right\}
$$

Score function is the derivative of the log-likelihood

$$
S(\mathbf{\beta}) = \frac{\partial \ell(\mathbf{Y}; \beta, \sigma)}{\partial \beta} = \sum_{i=1}^n \frac{1}{\sigma^2} \mathbf{X}_i (Y_i - \mathbf{X}_i \beta)
$$

 Set to zero and solve

$$
\mathbf{X}^T\mathbf{Y} - \mathbf{X}^T \mathbf{X} \mathbf{\beta} = \mathbf{0} \\
\rightarrow \widehat{\mathbf{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T\mathbf{Y}
$$

which gives us exactly the same estimator as we had derived using least squares!

#### Maximum likelihood for a generalized linear model

Now that we know how to use maximum likelihood for parameter estimation, we can also apply it to estimate the parameters of a generalized linear model. Let's try it for the Poisson GLM we have just introduced:

$$
\left\{
\begin{array}{ccc}
Y_i & \sim & Poi(\mu_i) \\
\log \mu_i & = & \eta_i \\
\eta_i & = & \mathbf{X}^T_i \beta \\
\end{array}
\right.
$$


Likelihood function of the Poisson distribution

$$
L(Y_i ; \mu) = \prod_{i=1}^n \frac{e^{-\mu} \mu^{Y_i}}{Y_i!}
$$

Log-likelihood function

$$
\ell(Y_i ; \mu) = \sum_{i=1}^n - \mu + Y_i \log(\mu) - \log (Y_i!)
$$

Note that the score function is the derivative of the log-likelihood with respect to our parameter of interest, $\beta$. So let's first rewrite our log-likelihood as a function of our parameter of interest. We know from the model that $\mu_i = \exp(\mathbf{X}_i \mathbf{\beta})$.

$$
\ell(Y_i ; \beta) = \sum_{i=1}^n - \exp(\mathbf{X}_i \mathbf{\beta}) + Y_i (\mathbf{X}_i \mathbf{\beta}) - \log (Y_i!)
$$

The score function then equals

$$
S(\mathbf{\beta}) = \frac{\partial \ell(\mathbf{Y}; \beta)}{\partial \beta} = \sum_{i=1}^n -\mathbf{X}_i^T \exp(\mathbf{X}_i \mathbf{\beta}) + \mathbf{X}_i^TY_i = -\mathbf{X}^T \exp(\mathbf{X} \mathbf{\beta}) + \mathbf{X}^T \mathbf{Y}
$$

Set to zero and solve

$$
\mathbf{X}^T \mathbf{Y} = \mathbf{X}^T \exp(\mathbf{X} \mathbf{\beta})
$$

However, since this is a non-linear equation in $\beta$, we cannot find a closed-form solution! You may see this more clearly when writing out in non-matrix form

$$
\sum_i \sum_p x_{ip} \exp(x_{ip} \beta_p) = \sum_i \sum_p x_{ip} Y_i.
$$

 ---

 - The above derivations show that estimating the parameters of a GLM is much harder as compared to a linear model.
 - The **iterative reweighted least squares (IRLS)** algorithm is usually adopted for fitting GLMs using maximum likelihood. As the name suggests, it is an iterative algorithm, where each data point is reweighted in each iteration according to the assumed mean-variance relationship, which is a function of its estimated mean of the previous iteration. Indeed, observations with high variance will be downweighted and vice versa. IRLS uses the derivative of the score function (i.e., the second derivative of the log-likelihood function) to move into the direction where the first derivative is zero.

```r

---

[← All defaults](03-all-defaults.md) · [Up: contents](index.md) · [All defaults →](05-all-defaults.md)
