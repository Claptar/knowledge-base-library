---
title: calculate estimated average number of bikers
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# calculate estimated average number of bikers

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

yhatA <- predict(m,
                newdata = dfA,
                type = "response")
yhatB <- predict(m,
                newdata = dfB,
                type = "response")

yhatA / yhatB # also equal to above.
```

 ---

 **Exercise**: try to derive the change in average number of bikers between (a) humidity of 0.1 above average, clear weather (`weathersit=1`), at hour 10 and (b) humidity of 0.1 below average, cloudy weather (`weathersit=2`), at hour 20, using all three methods.

## Statistical inference in GLMs

### Wald test and likelihood ratio test

 - In our interpretation above we have focussed on deriving changes in the average number of bikers between groups of interest. However, we have not yet tested whether these changes are statistically significant.
 - In genomics applications, statistical inference in GLMs is often adopted to test for differential expression between conditions for each gene (e.g., *is gene A differently expressed in healthy versus tumoral tissue?*), which amounts to testing the null hypothesis of whether a (linear combination of) coefficient(s) equals zero.
 - In this course, we will mainly work with two types of statistical tests for GLMs:
   - **Wald test**: The Wald test may be viewed as being anaologous to the $t$-test we are using in linear models. The Wald test relies on the following asymptotic result
   $$\hat{\beta} | \beta \sim N (\beta, Var(\hat{\beta}))$$.
   The Wald test statistic for testing a single parameter $\hat{\beta}$
   $$W = \frac{\hat{\beta}}{\hat{SE}(\hat{\beta})} \sim N(0,1) | H_0$$
   or, equivalently, letting $\mathbf{C}$ denote the $1 \times p$ contrast matrix denoting the contrast for the single parameter $\beta$ we would like to test, and $\hat{\Sigma}_{\hat{\beta}}$  the $p \times p$ variance-covariance matrix of the parameters,
   $$W = \mathbf{C}\hat{\beta} (\mathbf{C} \hat{\Sigma}_{\hat{\beta}} \mathbf{C}^T)^{-1} \hat{\beta}^T \mathbf{C}^T \sim \chi^2_1 | H_0.$$
   The null and alternative hypothesis can therefore in general be written as
   $$ H_0: \mathbf{C} \beta = 0$$
   $$ H_1: \mathbf{C} \beta \ne 0$$
   If $c \ge 1$ contrasts are tested, then the test statistic $W \sim \chi^2_c | H_0$, provided that the $c$ contrasts are linearly independent (i.e., the contrast matrix is full rank).
   - **Likelihood ratio test**: The likelihood ratio test (LRT) measures the discrepancy in log-likelihood between our current model (sometimes also referred to as full model) and a reduced model (sometimes also referred to as null or alternative model). The reduced model must be nested in (and therefore of lower dimension as compared to) the full model. While adding more covariates will always explain more variability in our response variable, the LRT tests whether this is actually significant.
   For example, in the example of gene differential expression between healthy versus tumoral tissue, the full model could be a GLM where the mean is modeled according to an intercept and a tissue indicator variable (healthy / tumoral), while the alternative model could be a GLM with just an intercept. Indeed, if the gene is similarly expressed between healthy and tumoral tissue, the log-likelihood of the alternative model will decrease only a little as compared to the full model.
   As the name suggests, the likelihood ratio test assesses whether the ratio of the log-likelihoods provides sufficient evidence for a worse fit of the alternative versus full model
   $$L = 2 \left\{ \ell(\hat{\beta}_{full}) -  \ell(\hat{\beta}_{alternative}) \right\}.$$
   Asymptotically, under the null hypothesis it can be shown that
   $$ L \sim \chi_c^2 | H_0, $$
   with $c$ the number of parameters dropped in the alternative model versus the full model. If we again let $\mathbf{C}$ denote the $c \times p$ contrast matrix denoting the contrast for the parameters being dropped, the null and alternative hypothesis are as in the Wald test setting:
   $$ H_0: \mathbf{C} \beta = 0$$
   $$ H_1: \mathbf{C} \beta \ne 0$$
   Finally, note that while, in this explanation, I have focussed on reducing a more complex model, but of course the LRT can also be adopted to check whether adding a covariate significantly improves the fit.
 - It is important to keep in mind that standard statistical inference theory in GLMs works **asymptotically in terms of the sample size**. Thus we need many data points in order for the theory to hold in practice. In order for the $p$-values to be correct, our parametric (distributional) assumptions as well as the independence assumption, must also hold.
 - In bulk RNA-seq, we are often working with a limited number of samples and so we typically do not expect asymptotic theory to hold yet. In single-cell RNA-seq, we often perform several preprocessing steps before calculating $p$-values for each gene and so we may be 'using the data multiple times'. Rather than attaching strong probabilistic interpretations to the $p$-values, we therefore advice to view the $p$-values simply as useful numerical summaries for ranking the genes for further inspection in genomics applications.

```r
include_graphics("./images_sequencing/likTests.png")
```

### Wald test and likelihood ratio test in `R`

Let's use a Wald test and a likelihood ratio test to test whether the average number of bikers differs between a working day or a weekend day, using a simple GLM with only that variable as a covariate.
This amounts to testing

$$H_0: \beta_{workingday} = 0$$
$$H_1: \beta_{workingday} \ne 0$$

```r
mSimple <- glm(bikers ~ workingday,
               family = "poisson",
               data = Bikeshare)
summSimple <- summary(mSimple)
summSimple$coefficients["workingday",]

---

[← set up data frames with relevant predictor variables' values.](11-set-up-data-frames-with-relevant-predictor-variables-values.md) · [Up: contents](index.md) · [Wald test manually →](13-wald-test-manually.md)
