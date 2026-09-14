---
title: one before and one after sample for each
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# one before and one after sample for each

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

time <- factor(rep(c("before", "after"), 8), levels=c("before", "after"))

table(patient, disease, time)

## simulate data for one gene
n <- 16
y <- rpois(n = n, lambda = 50)

## fit a Poisson model
m <- glm(y ~ patient + disease*time,
         family = "poisson")
summary(m)
```

 ---

We find that one of the coefficients is `NA`! This is obviously not because we're dealing with `NA` values in the data as we've just simulated the response variable ourselves. What's going on?

One of the parameters, in this case the parameter distinguishing cancer from healthy patients **cannot be estimated as it is a linear combination of other parameters**. In our case, estimating the diseased effect would use information that is already used to estimate the patient-level intercepts. In other words, **once you know the patient, you immediately also know the disease status**, so estimating the diseased vs healthy effect on top of the patient effect provides no additional information if we have already estimated the patient-level effects. This concept is called aliasing, and is a common technical issue in 'omics experiments with complex experimental designs.

 ---

While to understand the origin of the aliasing it is crucial to understand the relationship between the variables in the experimental design, we can also investigate it in detail using the `alias` function, to give us an idea.

```r
alias(m)
```

We see that the effect `diseasecancer` is a linear combination of the patient-specific effects of the cancer patients. This makes sense!

 ---

For clarity, let's reproduce this using our design matrix.

```r
X <- model.matrix(~ patient + disease*time) # this is the design used in glm()

## these are indeed identical.
X[,"diseasecancer"]
X[,"patiente"] + X[,"patientf"] + X[,"patientg"] + X[,"patienth"]
```

Since one of our parameters is a linear combination of other parameters, it cannot be estimated simultaneously with the other parameters. In this case, we can actually drop the `disease` main effect from the model, since we know that it is already included in the `patient` effect.

 ---

We will have to carefully construct our design matrix in order to account for all important sources of variation while still allowing us to answer the research question of interest. The aliasing exploration above has made it clear we may drop the `disease` main effect, so let's start by constructing this design matrix.

```r
X <- model.matrix(~ patient + time + disease:time)

m2 <- glm(y ~ -1 + X,
         family = "poisson")
summary(m2)
alias(m2)
```

We are still confronted with aliasing as the model matrix contains an interaction effect `timebefore:diseasecancer` as well as `timeafter:diseasecancer`, while only the latter is relevant. Indeed, we know that we can derive the `timebefore:diseasecancer` effect by averaging the patient effects of the cancer patients.

 ---

```r
X <- X[,!colnames(X) %in% "timebefore:diseasecancer"]


## fit a Poisson model
m2 <- glm(y ~ -1 + X,
         family = "poisson")
summary(m2)
```

We see that all coefficients can now be estimated. The `timeafter` effect may be interpreted as the time effect for healthy patients, while the `timeafter:diseasecancer` effect may be interpreted as the difference in the time effect for cancer patients as compared to healthy patients, i.e., it is the relevant interaction effect we are interested in.

**Question**. Taking this further, suppose that we can safely assume that there is no interaction effect between disease status and time. How would you now test for differential expression between healthy and cancer patients at the first timepoint? Specify the experimental design and contrast used.

<details><summary> Answer. </summary><p>
Assuming no interaction, we can specify the design as follows:

```r
XMain <- model.matrix(~ patient + time)
head(XMain)
```

In order to set up the contrast testing for healthy versus diseased patients at the first timepoint, we need to take the average of the appropriate patient-level intercepts.
The average expression for healthy patients is
$$ \log \mu_{healthy} = \frac{1}{4} \left\{ \beta_0 + (\beta_0 + \beta_1) + (\beta_0 + \beta_2) + (\beta_0 + \beta_3) \right\}. $$
Similar, for the diseased patients it equals
$$ \log \mu_{diseased} = \frac{1}{4} \left\{ (\beta_0 + \beta_4) + (\beta_0 + \beta_5) + (\beta_0 + \beta_6) + (\beta_0 + \beta_7) \right\}. $$
And thus the relevant contrast
$$ \log \frac{\mu_{diseased}}{\mu_{healthy}} = \frac{1}{4} (\beta_4 + \beta_5 + \beta_6 + \beta_7 ) - \frac{1}{4} (\beta_1 + \beta_2 + \beta_3).$$
</p></details>

---

[← first four are healthy, next four are diseased](09-first-four-are-healthy-next-four-are-diseased.md) · [Up: contents](index.md) · [limma-voom as an alternative approach to modeling counts →](11-limma-voom-as-an-alternative-approach-to-modeling-counts.md)
