---
title: 'Post hoc analysis: Multiple comparisons of means'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd
source_file: sources/gtpb-psls20/theory/07-Anova.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Post hoc analysis: Multiple comparisons of means

**Source:** [`theory/07-Anova.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

## Naive method

In the first part we developed the $F$-test to assess

$$  H_0: \mu_1=\cdots = \mu_g \text{ versus } H_1: H_1: \exists\ j,k \in \{1,\ldots,g\} : \mu_j\neq\mu_k$$


- If we reject $H_0$ we conclude that at least two means are different
- The method does not allow to identify which means are different.

A first naive method is to split $H_0$  in partial hypotheses
$$H_{0jk}: \mu_j=\mu_k \text{ versus } H_{1jk}: \mu_j \neq \mu_k$$

- Falsify partial null hypotheses with two-sample $t$-testen

- Comparison of group $j$ with group $k$ with two-sample $t$-test under the equality of means:
$$T_{jk} = \frac{\bar{Y}_j-\bar{Y}_k}{S_p\sqrt{\frac{1}{n_j}+\frac{1}{n_k}}} \sim t_{n-2}$$

With

- $S_p^2$ the pooled variance estimator,
$$S_p^2 = \frac{(n_j-1)S_j^2 + (n_k-1)S_k^2}{n_j+n_k-2}$$

- with $S_j^2$ and $S_k^2$ the sample variances of group $j$ en $k$, respectively.

In ANOVA context we assume that the variance of **all** $g$ groups is equal, i.e. the residual variance $\sigma^2$.

- Use of $S_p^2$ is not efficient because it does not make use of all data

- We can gain efficiency by using MSE
$$\text{MSE}= \sum_{j=1}^g \frac{(n_j-1)S_j^2}{n-g}$$

- The $t$-tests are thus best based on
$$T_{jk} = \frac{\bar{Y}_j-\bar{Y}_k}{\text{MSE}\sqrt{\frac{1}{n_j}+\frac{1}{n_k}}} \sim t_{n-g}.$$

---

```r
with(prostacyclin,pairwise.t.test(prostac,dose,"none"))
```

When we perform $m$-tests on the $\alpha$ significance level we cannot correctly control the type I error.

## We show with simulation that naive method does not work

1. We simulate from an ANOVA model with $g=3$ groups.
2. The means in the ANOVA model are equal to each other, so that $$H_0: \mu_1=\mu_2=\mu_3$$.
3. For each simulated dataset we conduct $m=3$ pairwise two-sample $t$-test
4. As soon as one of the $p$-values is below significance level $\alpha=5\%$, we reject $H_0: \mu_1=\mu_2=\mu_3$ because two means are different according to the  $t$-tests.
5. We rapport the relative frequency of rejection of the global null hypothesis, i.e. the probability on a type I error  $H_0: \mu_1=\mu_2=\mu_3$.


```r
g<-3 # number of treatments (g=3)
ni<-12 # number of observations in each group
n<-g*ni # total number of observation
alpha<-0.05 # significance level of individual test
N=10000 # number of simulations
set.seed(302) #seed to reproduce results exactly
trt=factor(rep(1:g,ni)) #factor
cnt<-0 #counter for erroneous rejections
for(i in 1:N) {
#if (i%%1000==0) cat(i,"/",N,"\n")
y <- rnorm(n)
tests<-pairwise.t.test(y,trt,"none")
reject<-min(tests$p.value,na.rm=T)<alpha
if(reject) cnt<-cnt+1
}
cnt/N
```

---

- Probability on the type I error equals `r round(cnt/N,3)*100`%
- It is more then twice $\alpha=5$%.
- If we repeat the simulation with g = 5 groups (i.e. 10 pairwise t-tests) we find a type I error of 28.0% instead of the desired 5%.

- The simulation study illustrates the  **multiplicity** problem

  - Classical p-values can only be compared with the significance level $\alpha$, if the conclusion is based on a single p-value.
  - Here the final decision is based on $m=g\times(g-1)/2$ $p$-values.

- We first discuss on the extension of the concept of type I errors and then introduce some solutions

## Family-wise error rate

- When $m>1$ tests are used to make one decision it is necessary to correct for the risk on false positive results (type I errors).
- Most procedures for multiple testing assume that *all $m$ null hypotheses are true*.

- So one tries to control the *risk on at least 1 false positive* on the **family wise error rate (FWER) $\alpha_F$**, typical $\alpha_F=0.05$.

## Bonferroni correction

When we conduct $m$ independent test each on the significance level $\alpha$, then
\begin{eqnarray*}
\alpha_F&=&\text{P}[\text{at least 1 Type I fout}]\\
&=&1-(1-\alpha)^m \leq m\alpha
\end{eqnarray*}

- If we assess 5 tests on the 5% significance level then  the FWER $\approx 25\%$. {10pt}
- By conducting them at the 1% significance level the FWER $\approx 5\%$.

- The Bonferroni correction controls the FWER on $\alpha_F$ by setting $$\alpha=\alpha_F/m$$ for each of the $m$ pairwise comparisons

An alternative approach is to report

  1. *adjusted p-values* that can be compared to the FWER $\alpha_F$ level: $$\tilde{p}=min(m\times p,1)$$
  2. and $(1-\alpha_F/m)100\%$ confidence intervals.

### prostacyclin example

```r
with(prostacyclin,pairwise.t.test(prostac,dose, data = prostacyclin, p.adjust.method="bonferroni"))
```

- The conclusions remain similar, except that the FWER is now controlled at $\alpha_F=5\%$ and that the $\tilde{p}$-values are larger with a factor 3.

The same analysis can be conducted in the `multcomp` R package that is developed for multiple testing in linear models.
```r
library(multcomp)
```

```r
model1.mcp<-glht(model1,linfct=mcp(dose="Tukey"))
summary(model1.mcp,test=adjusted("bonferroni"))
```

Note, that the user has to define custum functions to obtain Bonferonni adjusted confidence intervals.

- Bonferonni confidence intervals are not implemented because better methods exist for multiple testing.

- The function below is added here merely for completeness, but we will generally use the default method for multiple testing in multcomp.

```r
calpha_bon_t<-function(object,level)
 abs(
   qt(
     (1-level)/2/nrow(object$linfct),
     object$df
     )
    )
```

```r
confint(model1.mcp,calpha=calpha_bon_t)
```

### Evaluate Bonferroni method via simulation

```r
g<-3 # number of treatments (g=3)
ni<-12 # number of observations in each group
n<-g*ni # totaal number observation
alpha<-0.05 # significance level of individual test
N=10000 # number of simulaties
set.seed(302) #seed to reproduce results exactly
trt=factor(rep(1:g,ni)) #factor
cnt<-0 #counter for erroneous rejections
for(i in 1:N) {
#if (i%%1000==0) cat(i,"/",N,"\n")
y <- rnorm(n)
tests<-pairwise.t.test(y,trt,"bonferroni")
reject<-min(tests$p.value,na.rm=T)<alpha
if(reject) cnt<-cnt+1
}
cnt/N
```


- We find an FWER of `r round(cnt/N*100,1)`%, which is slightly conservative.
- For simulations of $g=5$ group the FWER is $4.1\%$ (more conservative).

- By using Bonferroni the probability on at least one false positive result is lower than $< \alpha_F$.
- Power loss because the real FWER is smaller than 5%

## Tukey Method

- Less conservatieve
- Implementation approximates the null distribution of posthoc tests via simulations
- Results can change slightly if the posthoc analysis is repeated
- Details on the method falls outside the scope of the short course
- Is the default method in the multcomp package:

    - adjusted p-values
    - adjusted confidence intervals

### Captopril example

```r
model1.mcp<-glht(model1,linfct=mcp(dose="Tukey"))
summary(model1.mcp)
```


```r
confint(model1.mcp)
```


```r
plot(confint(model1.mcp))
```

###Evaluate Tukey method

```r
g<-3 # number of treatments (g=3)
ni<-12 # number of observations in each group
n<-g*ni # totaal number observation
alpha<-0.05 # significance level of individual test
N <- 10000 # number of simulations
set.seed(302) #seed to reproduce results exactly
trt <- factor(rep(1:g,ni)) #factor
cnt<-0 #counter for erroneous rejections
for(i in 1:N) {
#if (i%%1000==0) cat(i,"/",N,"\n")
y <- rnorm(n)
m<-lm(y~trt)
m.mcp<-glht(m,linfct=mcp(trt="Tukey"))
tests<-summary(m.mcp)$test
reject<-min(as.numeric(tests$pvalues),na.rm=T)<alpha
if(reject) cnt<-cnt+1
}
cnt/N
```

---

[← Sum of squares and Anova](03-sum-of-squares-and-anova.md) · [Up: contents](index.md) · [Conclusions: Prostacyclin example →](05-conclusions-prostacyclin-example.md)
