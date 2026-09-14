---
title: Two sample T-test
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference-twosampleT.Rmd
source_file: sources/gtpb-psls20/theory/05-statisticalInference-twosampleT.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Two sample T-test

**Source:** [`theory/05-statisticalInference-twosampleT.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference-twosampleT.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

## Notation

Suppose that $Y_{ij}$ is the response for subjects $i=1,\ldots, n_j$ from population $j=1,2$.

Use of the term **treatment** or **group** instead of population

Here the treatment is $j=1$ microbial transplant vs $j=2$ placebo.

We assume

$$Y_{ij}\text{ i.i.d. } N(\mu_j,\sigma^2)\;\;\;i=1,\ldots,n_i\;j=1,2.$$

Note, that we assume equal variances **homoscedastic**

(Unequal variances are referred to as  **heteroscedastic**)

---

## Hypotheses

Test $$ H_0: \mu_1 = \mu_2 $$
against
$$  H_1: \mu_1 \neq \mu_2 .$$

$H_1$ is again the research hypothesis: the average relative abundance of *Staphylococcus spp.* is different upon microbial transplant then upon placebo treatment.

$H_0$ and $H_1$ can also be specified in terms of the effect size between the two treatments, $\mu_1-\mu_2$
$$H_0: \mu_1-\mu_2 = 0,$$
$$H_1: \mu_1-\mu_2 \neq 0.$$

We can estimate the effect size using the difference in sample means:
$$\hat \mu_1-\hat \mu_2=\bar Y_1 -\bar Y_2.$$

---

## Variance estimator

The experimental units are independent so the sample means are also independent and the variance on the difference is
$$\text{Var}_{\bar Y_1 -\bar Y_2}=\frac{\sigma^2}{n_1}+\frac{\sigma^2}{n_2}=\sigma^2 \left(\frac{1}{n_1}+\frac{1}{n_2}\right).$$

And the standard error becomes
$$\sigma_{\bar Y_1 -\bar Y_2}=\sigma\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}.$$

The variance can be estimated within each group using the sample variance:

$$S_1^2 = \frac{1}{n_1-1}\sum_{i=1}^{n_1} (Y_{i1}-\bar{Y}_1)^2.$$

$$S_2^2 = \frac{1}{n_2-1}\sum_{i=1}^{n_2} (Y_{i2}-\bar{Y}_2)^2.$$

But, if we assume equal variances $\sigma_1^2=\sigma_2^2=\sigma^2$ than we can estimate the variance more precise by using all observations in both groups. This variance estimator is also referred to as the *pooled variance estimator: $S^2_p$*.

So $S_1^2$ en $S_2^2$ are estimators of the same parameter $\sigma^2$.

And we can combine them into one estimator based on all $n_1+n_2$ observations:

$$  S_p^2 = \frac{n_1-1}{n_1+n_2-2} S_1^2 + \frac{n_2-1}{n_1+n_2-2} S_2^2 = \frac{1}{n_1+n_2-2}\sum_{j=1}^2\sum_{i=1}^{n_j} (Y_{ij} - \bar{Y}_j)^2.$$

$$ S_p^2= \sum\limits_{j=1}^2\sum\limits_{i=1}^{n_j} \frac{(Y_{ij}-\bar{Y}_{.j})^2}{n_1+n_2-2}$$


The pooled variance estimator uses the squared deviations of the observations from their group mean and has $n_1+n_2-2$ degrees of freedom.

---

## Test statistic
Two-sample $t$-teststatistiek:

$$T = \frac{\bar{Y}_1-\bar{Y}_2}{\sqrt{\frac{S_p^2}{n_1}+\frac{S_p^2}{n_2}}} =
  \frac{\bar{Y}_1 - \bar{Y}_2}{S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}.$$

The statistic T follows a t-distribution with $n_1+n_2-2$ under $H_0$ is all data are independent, normally distributed and have equal variances.

---

## Armpit example

We can implement the test in R:

```r
t.test(rel~trt,data=ap,var.equal=TRUE)
```

On the $5\%$ significance level we reject the null hypothesis in favor of the alternative hypothesis and conclude that the relative abundance of  *Staphylococcus spp.* is on average extreme significant larger is in transplantation group than in the placebo group.

If there is no effect of the transplant we have a probability of less then 9 in $100000$ to observe a test statistic in a random sample that is at least as extreme as what we observed in the armpit experiment.

This is extremely rare under $H_0$.

If $H_1$ is correct, we expect that the test statistic is larger in absolute value and expect small p-values. Hence we decide that there is a lot of evidence against $H_0$ in favour of $H_1$.

**Good statistical practice** is to report the $p$-value, but also  effect size along with its confidence interval. So that we can judge the statistical significance and the biological relevance.

### Conclusion

On average the relative abundance of *Staphylococcus spp.* in the microbiome of the armpit in the transplant group is extremely significantly different from that in the placebo group ($p<<0.001$). The relative abundance of *Staphylococcus spp.* is on average `r round(diff(t.test(rel~trt,data=ap,var.equal=TRUE)$estimate),1)`% larger in the transplant group than in the placebo group (95\% CI [`r paste(format(-t.test(rel~trt,data=ap,var.equal=TRUE)$conf.int[2:1],digits=2,nsmall=1),collapse=",")`]%).

---

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Assumptions →](03-assumptions.md)
