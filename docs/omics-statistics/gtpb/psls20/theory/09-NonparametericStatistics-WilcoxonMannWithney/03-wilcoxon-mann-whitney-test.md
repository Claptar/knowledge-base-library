---
title: Wilcoxon-Mann-Whitney Test
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd
source_file: sources/gtpb-psls20/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Wilcoxon-Mann-Whitney Test

**Source:** [`theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Simultaneously developed by Wilcoxon, and,  Mann and Whitney:  **Wilcoxon-Mann-Whitney**, **Wilcoxon rank sum test**  or **Mann-Whitney U test**

## hypotheses

Under $H_0$ the distributions of the two groups are equal
$$H_0: f_1=f_2$$


Under the alternative $H_1$ the distributions differ in location $$H_1: \mu_1\neq \mu_2$$

$H_1$ assumes **location-shift**, we will relax this assumption later on.

## Test statistic

Classic T-test: difference in sample means $\bar{Y}_1-\bar{Y}_2$.

Here: Difference in sample means based on rank transformed data

Ranks based on the pooled sample (upon joining the observations from the two groups): $R_{ij}=R(Y_{ij})$ is de rank of observation $Y_{ij}$ in the pooled sample.

$$
  T = \frac{1}{n_1}\sum_{i=1}^{n_1} R(Y_{i1}) - \frac{1}{n_2}\sum_{i=1}^{n_2} R(Y_{i2}) .
$$

- Under $H_0$ we expect the average rank of the first group to be close to that of the second group so $T$ is close to zero.

- Under $H_1$ we expect the mean ranks to differ so that $T$ deviates from zero.

- It is sufficient to only calculate
  $$S_1=\sum_{i=1}^{n_1} R(Y_{i1})$$.

- $S_1$ is the sum of the ranks of the first group: *rank sum test*.

- This holds because
$$
  S_1+S_2 = \text{sum of all ranks} = 1+2+\cdots + n=\frac{1}{2}n(n+1).
$$


- $S_1$ (or $S_2$) is a good test statistic

- Use permutations to determine the exact permutation distribution. (Permute the ranks between the groups)

- For a given $n$ and no *ties* the rank transformed data is always
  $$1, 2, \ldots, n$$
- For given $n_1$ en $n_2$ the permutation distribution is always the same!
- With current computing power this is not so important any more.

---

## Standardized statistic

Often the standardized test statistic is used
$$
  T = \frac{S_1-\text{E}_{0}\left[S_1\right]}{\sqrt{\text{Var}_{0}\left[S_1\right]}},
$$

- with $\text{E}_{0}\left[S_1\right]$ and $\text{Var}_{0}\left[S_1\right]$ the expect mean and variance of S1 under $H_0$.

- Under $H_0$
 $$
   \text{E}_{0}\left[S_1\right]= \frac{1}{2}n_1(n+1) \;\;\;\;\text{ en }\;\;\;\; \text{Var}_{0}\left[S_1\right]=\frac{1}{12}n_1n_2(n+1).
 $$

- Under $H_0$ and when $\min(n_1,n_2)\rightarrow \infty$
 $$
    T = \frac{S_1-\text{E}_{0}\left[S_1\right]}{\sqrt{\text{Var}_{0}\left[S_1\right]}} \rightarrow N(0,1).
 $$

Asymptotically the standardised statistic follows a standard normal distribution!

---

## Cholesterol example

We illustrate the result for the cholesterol example using the R function `wilcox.test`.
```r
wilcox.test(cholest~group,data=chol)
```

- We reject $H_0$ ($p=$ `r format(wilcox.test(cholest~group,data=chol)$p.value,digits=2)` $<0.05$)

- The output shows $W=$ `r wilcox.test(cholest~group,data=chol)$statistic`?

- Lets calculate
```r
S1 <- sum(rank(chol$cholest)[chol$group==1])
S1
S2 <- sum(rank(chol$cholest)[chol$group==2])
S2
```

- Where does $W=$ `r wilcox.test(cholest~group,data=chol)$statistic` comes from?

---

## Mann and Whitney test

Mann and Whitney test in absence of ties:
$$
 U_1 = \sum_{i=1}^{n_1}\sum_{k=1}^{n_2} \text{I}\left\{Y_{i1}\geq Y_{k2}\right\}.
$$

- with $\text{I}\left\{.\right\}$ an indicator that equals 1  if the expression is true and is zero otherwise.

- U counts how many times an observation of the first group is larger or equal to an observation from the second group.

```r
y1=subset(chol,group==1)$cholest
y2=subset(chol,group==2)$cholest
u1Hlp=sapply(y1,function(y1i,y2) {y1i>=y2},y2=y2)
colnames(u1Hlp)=y1;rownames(u1Hlp)=y2
```

```r
u1Hlp
U1=sum(u1Hlp); U1
```

It can be shown that $U_1 = S_1 - \frac{1}{2}n_1(n_1+1).$

```r
S1-nGroups[1]*(nGroups[1]+1)/2
```

1. $U_1$ en $S_1$ contain the same information
2. $U_1$ is also a rank statistic, and
3. Exact test based on $U_1$ and $S_1$ are equivalent.

---

## Probabilistic index

- $U_1$ has a better interpretation feature
- Let $Y_j$ a random observation from group $j$ ($j=1,2$). Then
\begin{eqnarray*}
  \frac{1}{n_1n_2}\text{E}\left[U_1\right]
     &=& \text{P}\left[Y_1 \geq Y_2\right].
\end{eqnarray*}

So we can estimate the probability by calculating the mean of all indicator variable values $\text{I}\left\{Y_{i1}\geq Y_{k2}\right\}$. Note, that we did $n_1 \times n_2$ comparisons

```r
mean(u1Hlp)
U1/(nGroups[1]*nGroups[2])
```

- Probability $\text{P}\left[Y_1 \geq Y_2\right]$ is referred to as the *probabilistic index*.
- It is the probability that a random observation of the first group is larger or equal than a random observation of the second group
- If $H_0$ holds $\text{P}\left[Y_1 \geq Y_2\right]=\frac{1}{2}$.

- R function `wilcox.test` does not return the Wilcoxon rank sum statistic. It returns the Mann-Whitney statistic $U_1$.
- Lets revisit the result
```r
wTest<-wilcox.test(cholest~group,data=chol)
wTest
U1
probInd=wTest$statistic/prod(nGroups)
probInd
```

Because $p=$ `r format(wTest$p.value,digits=3)` $<0.05$ we conclude at the $5\%$ significance level that the mean cholesterol level of hart patients is larger then that of healthy subjects.

  - Note that we have assumed that the location-shift model is valid in this conclusion.
  - We also know that higher cholesterol level are more likely for hart patients then for healthy subjects and this probability is
$U1/(n_1\times n_2)=$ `r probInd*100`%.
  - We should assess the location shift assumption. But this is not possible with only 5 observations.

Without the location-shift assumption the conclusion in terms of the probabilistic index remains valid!

  - So when we do not assume location shift we test for

$$H_0: F_1=F_2 \text{ vs } H_1: P[Y_1 \geq Y_2] \neq 0.5.$$


## Conclusion

There is a significant difference in the distribution of the cholesterol concentration of hart patients two days upon a stroke and that of healthy subject (($p=$ `r format(wTest$p.value,digits=3)`). It is more likely to observe higher cholesterol levels for hart patients then for healthy subjects. The point estimator for this probability is `r probInd*100`%.


---

---

[← Rank Tests](02-rank-tests.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) {-} →](04-home-https-gtpb-github-io-psls20.md)
