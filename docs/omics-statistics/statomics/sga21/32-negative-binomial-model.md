---
title: "32. Negative Binomial Model"
course: "StatOmics Sga21"
chapter: 32
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 32. Negative Binomial Model

## What this covers

This chapter picks up a single-gene RNA-seq count analysis at the point where the model for the
counts is a negative binomial generalized linear model rather than a Poisson one, so that the
variance of the counts is allowed to exceed their mean. It covers how the fitted coefficients
correspond to the comparisons ("contrasts") of scientific interest, how those contrasts are tested
with a Wald statistic, why the more familiar likelihood-ratio alternative is awkward to apply here,
how the fit is checked with deviance and Pearson residuals and a goodness-of-fit test, and how a
basic correction for differences in sequencing depth between samples is added to the model as an
offset. It assumes familiarity with generalized linear models, the log link, maximum-likelihood
fitting, and the mechanics of a Wald or likelihood-ratio test.

## The negative binomial GLM

A Poisson model for count data forces $\mathrm{Var}(Y) = \mathbb{E}[Y]$. The negative binomial
distribution relaxes this by adding a second, dispersion parameter $\theta$ (R calls it `size`),
so that for a count $Y$ with mean $\mu$,

$$ \mathrm{Var}(Y) = \mu + \frac{\mu^2}{\theta}. $$

The variance always exceeds the mean by an amount that grows with $\mu^2/\theta$; as $\theta \to
\infty$ this extra term vanishes and the negative binomial reduces to the Poisson. This is the
standard reason count data — RNA-seq gene counts among them — are modelled as negative binomial
rather than Poisson: it lets the model absorb variability beyond what a Poisson mean-equals-variance
assumption can account for.

Fitting the model keeps the log link of the Poisson GLM,

$$ \log \mu_i = x_i^\top \beta, $$

but now estimates $\beta$ and $\theta$ jointly by maximum likelihood. In R this is `glm.nb` from the
`MASS` package:

```r
library(MASS)
mNB <- glm.nb(y ~ treatment*time + patient)
```

Here `y` is the count vector for one gene across samples, and the design combines a `treatment`
factor, a `time` factor, their interaction, and `patient` — a blocking factor that absorbs
patient-to-patient variation in a design where several treatments are measured within the same
patients over time, rather than letting it contribute to residual variance.

## Reading the design and its coefficients

The formula `treatment*time + patient` produces one coefficient for the intercept, one for each
non-reference level of `treatment`, one for each non-reference level of `time`, one for each
non-reference level of `patient`, and one for each treatment-by-time interaction term. Which
coefficient is which can be read off directly from how the contrasts of interest are later built
out of them: the coefficient in position 2 is the effect of one treatment (call it "DPN") against
the reference treatment ("control") at the reference time point, position 3 is the same for the
second treatment ("OHT"), and positions 8 and 9 are the DPN-by-time and OHT-by-time interaction
terms — the extra shift in each treatment's effect at the later time point, on top of its effect at
the reference time. The coefficients in between correspond to the main effect of time and to the
patient blocking factor.

Because the link is log, every coefficient is a difference of log means, i.e. a log fold change: a
coefficient of $b$ means the corresponding comparison multiplies the mean count by $e^b$.

## Testing contrasts

The study asks seven specific questions of this one design: is DPN different from control at the
earlier time point, is it different at the later time point, the same two questions for OHT, and
whether each treatment's effect *changes* between time points (an interaction), including whether
OHT and DPN change differently from each other. Each of these is a **contrast** — a linear
combination $c = L^\top \beta$ of the fitted coefficients — and all seven are collected as the
columns of one matrix $L$, one row per coefficient:

```r
L <- matrix(0, nrow = length(coef(mNB)), ncol = 7)
rownames(L) <- names(coef(mNB))
colnames(L) <- c("DPNvsCON24", "DPNvsCON48",
                 "OHTvsCON24", "OHTvsCON48",
                 "DPNvsCONInt", "OHTvsCONInt",
                 "OHTvsDPNInt")
L[2, "DPNvsCON24"]      <- 1
L[c(2,8), "DPNvsCON48"] <- 1
L[3, "OHTvsCON24"]      <- 1
L[c(3,9), "OHTvsCON48"] <- 1
L[8, "DPNvsCONInt"]     <- 1
L[9, "OHTvsCONInt"]     <- 1
L[c(9,8), "OHTvsDPNInt"] <- c(1, -1)
```

The pattern is worth reading closely. "DPN vs control at the reference time" needs only coefficient
2, because that coefficient *is* the DPN-vs-control comparison at the reference time by
construction. "DPN vs control at the later time" needs coefficient 2 *and* coefficient 8, because
at the later time point the DPN-vs-control gap is the main effect plus the extra shift the
interaction term contributes. The two interaction contrasts are just the interaction coefficients
read off on their own, and the last contrast — whether OHT's change over time differs from DPN's —
is the difference of the two interaction coefficients, coefficient 9 minus coefficient 8.

### The Wald test

For a single contrast $c = L^\top\beta$, estimated by $\hat c = L^\top \hat\beta$ with estimated
variance $L^\top \widehat{\mathrm{Cov}}(\hat\beta)\, L$, the Wald statistic is

$$ W = \frac{\hat c^2}{L^\top \widehat{\mathrm{Cov}}(\hat\beta)\, L}, $$

which, under the null hypothesis $H_0: c = 0$ and the usual large-sample theory for
maximum-likelihood estimators, is approximately $\chi^2_1$-distributed. This is exactly what the
loop below computes, one column of $L$ at a time, from the fitted coefficient vector `beta` and the
estimated covariance matrix `vcov(mNB)`:

```r
beta <- matrix(coef(mNB), ncol = 1)
waldStats <- c()
for (ll in 1:ncol(L)) {
  curL <- L[, ll, drop = FALSE]
  curWald <- t(curL) %*% beta %*% solve(t(curL) %*% vcov(mNB) %*% curL) %*% t(beta) %*% curL
  waldStats[ll] <- curWald
}
pvalues <- 1 - pchisq(waldStats, df = 1)
```

Each entry of `waldStats` is $W$ for the corresponding contrast, and `pvalues` reads it off against
the upper tail of a $\chi^2_1$ — one Wald test, and one p-value, per contrast.

### Why a likelihood-ratio test is harder here

A likelihood-ratio test compares the log-likelihood of a full model to that of a reduced model with
some coefficient constrained to zero, and refers twice the difference to a $\chi^2$ distribution
with degrees of freedom equal to the number of constrained coefficients. That directly tests "is
*this* fitted coefficient zero" — not "is this particular linear combination of several
coefficients zero," which is what six of the seven contrasts above are. Getting a likelihood-ratio
test for a contrast like `DPNvsCON48` (coefficients 2 and 8 together) would require reparameterizing
the model so that the contrast itself becomes one of the estimated coefficients, after which
dropping that one coefficient and comparing the two model fits recovers the test. This is possible
in principle, but the reparameterization is not carried out here — it is flagged as out of scope for
the course, and the analysis proceeds with the Wald tests above.

## Checking the fit: residuals

### Deviance residuals

The (unit) deviance residual for observation $i$ is

$$ d_i = \mathrm{sign}(y_i - \hat\mu_i)\sqrt{2\left[\ell(y_i; y_i, \hat\theta) - \ell(y_i;
\hat\mu_i, \hat\theta)\right]}, $$

where $\ell(y;\mu,\theta)$ is the negative binomial log-likelihood of $y$ with mean $\mu$ and
dispersion $\theta$. It compares the log-likelihood the fitted model actually achieves at $y_i$ to
the log-likelihood of the *saturated* model that would fit $y_i$ exactly ($\mu = y_i$); summing the
squared deviance residuals gives the residual deviance $D = \sum_i d_i^2$. The code builds this by
hand from `dnbinom` and checks that it reproduces R's built-in residual:

```r
devResid <- sign(y - fitted(mNB)) *
  sqrt(2 * (dnbinom(x = y, mu = y, size = mNB$theta, log = TRUE) -
            dnbinom(x = y, mu = fitted(mNB), size = mNB$theta, log = TRUE)))
range(devResid - resid(mNB, type = "deviance"))
```

### Pearson residuals

The Pearson residual standardizes the raw residual by the model's own variance function instead of
by a log-likelihood difference:

$$ e_i^{P} = \frac{y_i - \hat\mu_i}{\sqrt{\widehat{\mathrm{Var}}(Y_i)}}, \qquad
\widehat{\mathrm{Var}}(Y_i) = \hat\mu_i + \frac{\hat\mu_i^2}{\hat\theta}. $$

The denominator is exactly the negative binomial variance function from the first section,
evaluated at the fitted mean and estimated dispersion — for a Poisson fit the second term would be
absent and this would reduce to $\sqrt{\hat\mu_i}$. Again the code recomputes it directly and
checks it against R's built-in version:

```r
pearsResid <- (y - fitted(mNB)) / sqrt(fitted(mNB) + 1/mNB$theta * fitted(mNB)^2)
range(pearsResid - resid(mNB, type = "pearson"))
```

### A goodness-of-fit test

Summing the squared Pearson residuals gives the Pearson $\chi^2$ statistic,

$$ X^2 = \sum_i (e_i^P)^2, $$

which, if the model is correctly specified, is approximately $\chi^2$-distributed with $n - p$
degrees of freedom ($n$ samples, $p$ estimated coefficients):

```r
X2 <- sum(pearsResid^2)
1 - pchisq(X2, df = length(y) - length(coef(mNB)))
```

A small value here says the residuals are more spread out than the fitted model's own sampling
distribution predicts — evidence against the fit; a large value gives no such evidence.

## Correcting for sequencing depth: an offset

Total counts differ across samples for a reason that has nothing to do with any one gene's biology:
some libraries are simply sequenced more deeply than others. The simplest correction is to compute
each sample's total read count across all genes,

```r
seqDepth <- colSums(assays(se)$counts)
```

and add $\log(\text{seqDepth})$ to the linear predictor as an **offset** — a term added to the
right-hand side of the model with its coefficient fixed at $1$ rather than estimated:

$$ \log \mu_j = \log(\text{seqDepth}_j) + x_j^\top \beta. $$

Because the link is log, this is equivalent to modelling $\mu_j / \text{seqDepth}_j$ — the gene's
expression relative to that sample's total sequencing output — with the same log-linear form, so
the offset re-expresses the comparisons in relative rather than raw terms:

```r
library(MASS)
mNBOffset <- glm.nb(y ~ treatment*time + patient + offset(log(seqDepth)))
```

The same seven contrasts in $L$ are then re-tested against this new fit, using the identical Wald
construction with the new coefficient vector and covariance matrix:

```r
betaOffset <- matrix(coef(mNBOffset), ncol = 1)
waldStatsOffset <- c()
for (ll in 1:ncol(L)) {
  curL <- L[, ll, drop = FALSE]
  curWald <- t(curL) %*% betaOffset %*% solve(t(curL) %*% vcov(mNBOffset) %*% curL) %*%
    t(betaOffset) %*% curL
  waldStatsOffset[ll] <- curWald
}
pvaluesOffset <- 1 - pchisq(waldStatsOffset, df = 1)
```

Comparing `pvaluesOffset` to the original `pvalues` contrast by contrast is the check the exercise
sets up: whether this basic normalization for sequencing depth changes which of the seven
comparisons look significant.

## Sources

- Notes: `docs/omics-statistics/statomics/sga21/sequencing_lab_oneGene/02-negative-binomial-model.md`,
  a converted excerpt of `sequencing_lab_oneGene.Rmd` (statomics SGA21, Koen Van den Berge, CC
  BY-NC-SA 4.0), covering the negative binomial fit, the Wald and likelihood-ratio discussion, both
  residual checks, the goodness-of-fit test, and the sequencing-depth offset re-analysis.
- No slides, transcript, or exercise set was supplied for this chapter.
- The source page links back to an "Introduction" page that is not part of the supplied material:
  it is where the count vector `y`, the `treatment`/`time`/`patient` covariates, and the
  SummarizedExperiment `se` are first set up, and where a preceding Poisson fit for the same gene is
  checked and set aside in favour of the negative binomial model used throughout this chapter.

---

[← 31. Sequencing Technology and Preprocessing](31-sequencing-technology-and-preprocessing.md) · [Contents](index.md) · [33. RNA-seq Differential Expression Pipeline →](33-rna-seq-differential-expression-pipeline.md)
