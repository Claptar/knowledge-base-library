---
title: Empirical Bayes/Moderated $t$-test.
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd
source_file: sources/statomics-sga21/technicalDetailsProteomics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Empirical Bayes/Moderated $t$-test.

**Source:** [`technicalDetailsProteomics.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

A general class of moderated test statistics is given by

 $$\tilde{T}_p = \frac{\mathbf{L}_k \hat{ \boldsymbol{\beta_p}}}{\mathbf{L}_k^T(\mathbf{X}^T\mathbf{WX})^{-1}\mathbf{L}_k^T \tilde{s}_p^2}$$

 where $\tilde{s}_p$ is a moderated variance estimator.

Simple approach: set $\tilde{s}_p=s_p + s_0$: simply add a small positive constant to the denominator of the t-statistic

\textbf{empirical Bayes} theory provides formal framework for borrowing strength across genes or proteins,
e.g. popular bioconductor package \textbf{limma}
$$\tilde{s}_g=\sqrt{\frac{d_ps_p^2+d_0s_0^2}{d_g+d_0}},$$
and the moderated t-statistic is t-distributed with $d_0+d_g$ degrees of freedom under the null hypothesis $H_0: \mathbf{L}\boldsymbol{\beta}=0$.

- Note, that the degrees of freedom increase by borrowing strength across proteins.

---

## Intermezzo: Bayesian Methods

- Frequentists consider data as random and population parameters as fixed but unknown
- In Bayesian viewpoint a person has prior beliefs about the population parameters and the uncertainty on this prior beliefs are represented by a probability distribution placed on this parameter.

  - This distribution reflects the person's subjective prior opinion about plausible values of the parameter.
  - And is referred to as the prior $g(\boldsymbol{\theta})$.

- Bayesian thinking will update the prior information on the population parameters by confronting the model to data ($\mathbf{Y}$).

- By using Bayes Theorem this results in a posterior distribution on the model parameters.
$$
g(\boldsymbol{\theta}\vert\mathbf{Y})=\frac{f(Y\vert \boldsymbol{\theta})g(\boldsymbol{\theta})}{\int f(Y\vert \boldsymbol{\theta}) g(\boldsymbol{\theta}) d\boldsymbol{\theta}} \text{     }\left(\text{ posterior}=\frac{\text{prior} \times \text{ likelihood}}{\text{Marginal distribution}}\right)
$$

---

## Limma  approach

Developed for gene expression analysis with micro arrays.
Let g be the index for gene g.
$$
\begin{array}{cc}
&\beta_{gk}\vert \sigma^2_g,\beta_{gk}\neq 0 \sim N(0,v_{0k}\sigma_g^2)\\\\
\text{Prior}\\
&\frac{1}{\sigma^2_g}\sim s^2_0\frac{\chi^2_{d_0}}{d_0}\\\\\\\\
&\hat \beta_{gk} | \beta_{gk} , \sigma_g^2 \sim N( \beta_{gk} , v_{gk}\sigma_g^2)\\\\
\text{Data}\\
&s_g^2\sim \sigma^2_g\frac{\chi^2_{d_g}}{d_g}\\\\
\end{array}
$$

---

## Limma  approach

Under this assumption, it can be shown that

- Posterior Mean for the variance parameter: $$\tilde{s}^2_p = \text{E}\left[\sigma^2_p\vert s_p^2\right]=\frac{d_0 s_0^2+d_ps_p^2}{d_0+d_p}$$

- $$\tilde{T}_p=\frac{\mathbf{L}_k \hat{ \boldsymbol{\beta_p}}}{\mathbf{L}_k^T(\mathbf{X}^T\mathbf{WX})^{-1}\mathbf{L}_k^T \tilde{s}_p^2}$$

is t-distributed under $H_0: \mathbf{L}_j\boldsymbol{\beta} = 0$

$$\tilde{T}_p \vert H_0 \sim t(d_0 + d_p)$$

---

## Empirical Bayes
- A fully Bayesian
  - would define the prior distribution by carefully choosing the prior parameters based on prior knowledge on the process
  - would confront the prior to the data and performs inference using the posterior distribution of the model parameters.
- In an empirical Bayesian approach one estimates the prior parameters based on the data.
- In **Limma** moment estimators for $s_0$ and $d_0$ are derived using the information on the gene (protein) wise variances of all genes (proteins).
- In **Limma** one also does not work with the full posterior distribution for the variances, but with the maximum a-posterior estimate.

---

## Illustration

We borrow strength across proteins by

1. placing a scaled $\chi^2$ prior: $\chi^2(s_o,d_0)$ on the precisions ($1/\sigma^2_p$)
2. estimating the prior parameters $s_0$ and $df_0$
3. replacing the estimated protein-wise variances ($s_p^2$) with the maximum a-posteriori variance
$$\tilde{s}_p = \frac{d_p s^2_p + d_0 s_0^2}{d_p+d_0}$$


```r
sd <- sapply(
  rowData(pe[["proteinRobust"]])$msqrobModels,
  getSigma) %>%
  na.exclude
sdPost <- sapply(
  rowData(pe[["proteinRobust"]])$msqrobModels,
  getSigmaPosterior) %>%
  na.exclude

p1 <- qplot(sd,sdPost) +
  geom_abline()
p1
```

### How do we get to the posterior standard deviation?

```r
hlp <- limma::squeezeVar(
  var = sapply(rowData(pe[["proteinRobust"]])$msqrobModels, getVar),
  df = sapply(rowData(pe[["proteinRobust"]])$msqrobModels, getDF)
  )
```

#### Degrees of freedom of prior

```r
hlp$df.prior

model <- rowData(pe[["proteinRobust"]])$msqrobModels[[2]]
getDfPosterior(model) - getDF(model)
```

#### posterior variance

$$\tilde s_p=\sqrt{\frac{d_p\times s^2_p + d_0 s_0^2}{d_p+d_0}} $$

```r
hlp$var.prior

varPost <- (getVar(model) * getDF(model) + hlp$df.prior * hlp$var.prior)/(getDF(model)+hlp$df.prior)
sqrt(varPost)
getSigmaPosterior(model)
```

Hence, standard deviations are shrunken towards prior standard deviation!
Large standard deviations become smaller and smaller standard deviations become larger!

```r
p1 +
  geom_hline(yintercept = hlp$var.prior^.5)
```


### Illustration via Simulation

Suppose that the standard deviations for all proteins are the same and are equal to 1.
We simulate proteins with the same mean as the fitted mean in the experiment but with standard deviation of 1.

```r
nCoefs <- getCoef(rowData(pe[["proteinRobust"]])$msqrobModels[[2]]) %>% length
coefs <-
sapply(rowData(pe[["proteinRobust"]])$msqrobModels,
    function(x) getCoef(x)[1:nCoefs]
  ) %>%
  t %>%
  na.exclude


p <- nrow(coefs)
n <- ncol(pe[[1]])
f0_equalVar <- sapply(1:p,
  FUN=function(i, n, betas, sd, design) {
  rnorm(n, mean = design %*% betas[i,], sd = sd)},
  n = n,
  betas = coefs,
  sd = 1,
  design = X
  ) %>%
  t
colnames(f0_equalVar) <- colnames(pe[[1]])
sims <- readQFeatures(f0_equalVar %>% as.data.frame, ecol = 1:n, name = "sim_equalVar")
colData(sims) <- colData(pe)
sims <- msqrob(object = sims, i = "sim_equalVar", formula = ~ location*tissue + patient)

sd0 <- sapply(
  rowData(sims[["sim_equalVar"]])$msqrobModels,
  getSigma) %>%
  na.exclude
sdPost0 <- sapply(
  rowData(sims[["sim_equalVar"]])$msqrobModels,
  getSigmaPosterior) %>%
  na.exclude

qplot(sd0,sdPost0) +
  geom_abline() +
  ylim(range(sd0))
```

- We observe a large variability in the individual protein level standard deviation estimates.
- We simulated proteins with standard deviation of 1, but the protein estimates vary from `r paste(round(range(sd0),2),collapse=", ... , ")`.
- Large uncertainty on the estimation of variances in small samples
- The empirical Bayes method, however, recognises that all proteins are simulated with the same variance.
- Hence, it can borrow tremendous strength across proteins to stabilize the variance estimation
- Here, it shrinks all protein variance to the prior variance, which is indeed very close to 1, the value we have adopted in the simulation.

Note, that the prior degree of freedom also is set to infinity:
```r
getDF(rowData(sims[["sim_equalVar"]])$msqrobModels[[1]])
getDfPosterior(rowData(sims[["sim_equalVar"]])$msqrobModels[[1]])
```

which imposes shrinkage to the prior standard deviation!

The empirical Bayes method can thus indeed recognise the common variance that is shared across proteins!

---

[← Robust regression](03-robust-regression.md) · [Up: contents](index.md) · [P-values →](05-p-values.md)
