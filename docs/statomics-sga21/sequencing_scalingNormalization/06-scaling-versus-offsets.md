---
title: Scaling versus offsets
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd
source_file: sources/statomics-sga21/sequencing_scalingNormalization.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Scaling versus offsets

**Source:** [`sequencing_scalingNormalization.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

In RNA-seq, we are working with count data. Count data has an inherent mean-variance structure, where the variance is positively associated with the mean.
For example, assume a random variable $Y_{i} \sim Poi(\mu)$, where $i \in \{1, \ldots, n\}$. We can visualize the mean-variance relationship by simulating different random variables $\mathbf{Y}_1, \mathbf{Y}_2, \mathbf{Y}_3$.
Say,

$$ Y_{1i} \sim Poi(\mu_1 = 5) $$
$$ Y_{2i} \sim Poi(\mu_2 = 50) $$
$$ Y_{3i} \sim Poi(\mu_3 = 500) $$

Below, we enforce the same mean for all three random variables, i.e. we create the set of random variables $\{ Y_{1i} \times 10, Y_{2i}, Y_{3i} / 10 \}$, and plot the density of each variable.
It is clear that the distributions are drastically different. This is because, although they all have the same mean, their variance is different, and indeed this is because of the mean-variance relationship that was impliclty used when simulating the data.

```r
library(ggplot2)
set.seed(50)
n <- 1e4
y1 <- rpois(n = n, lambda = 5)
y2 <- rpois(n = n, lambda = 50)
y3 <- rpois(n = n, lambda = 500)

df <- data.frame(y = c(y1 * 10, y2, y3 / 10),
                 gr = factor(rep(1:3, each = n)))

ggplot(df, aes(x=y)) +
  geom_density() +
  facet_wrap(. ~ gr) +
  geom_vline(xintercept = 50, col="red") +
  theme_bw()
```

**But didn't you say a higher mean was associated with a higher variance?**

The critical reader would rightly so be somewhat confused at this point. Indeed, above we wrote that *"the variance is positively associated with the mean"*, but the density plots are showing that $\mathbf{Y}_3$, which was simulated to have the highest mean, has the smallest variance. Based on the simulation, we have that $Var(\mathbf{Y}_3) = 500$. However, $Var(\mathbf{Y}_3 / 10) = \frac{1}{100} Var(\mathbf{Y}_3) = 5$. Thus, $\mathbf{Y}_3$ indeed will have a small variance upon rescaling.

One could also say that the **relative** certainty of the mean of a Poisson random variable increases with its mean. With relative certainty, we mean the coefficient of variation (CV). Indeed, the CV of a Poisson distribution decreases with the mean

$$ CV(\mathbf{Y}_3) \le CV(\mathbf{Y}_2) \le CV(\mathbf{Y}_1).  $$

We show this below using our simulated data.

```r
calcCV <- function(x) sd(x) / mean(x)
cv1 <- calcCV(y1) ; cv1
cv2 <- calcCV(y2) ; cv2
cv3 <- calcCV(y3) ; cv3

plot(x=c(mean(y1), mean(y2), mean(y3)),
     y=c(cv1, cv2, cv3),
     xlab="Mean",
     ylab="CV")
```


See also appendix B1 of [Ahlmann-Eltze \& Huber (2021)](https://www.biorxiv.org/content/10.1101/2021.06.24.449781v2) for more information and a more formal justification.

---

[← Poisson GLM with library size offset: no longer significantly DE on 5% level.](05-poisson-glm-with-library-size-offset-no-longer-significantly.md) · [Up: contents](index.md)
