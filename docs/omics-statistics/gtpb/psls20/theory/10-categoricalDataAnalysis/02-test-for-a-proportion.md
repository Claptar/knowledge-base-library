---
title: Test for a proportion
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/10-categoricalDataAnalysis.Rmd
source_file: sources/gtpb-psls20/theory/10-categoricalDataAnalysis.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Test for a proportion

**Source:** [`theory/10-categoricalDataAnalysis.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/10-categoricalDataAnalysis.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

##Saksen-study

- Fairly closed population (few migration)
- Probability that an unborn child is male?

```r
boys <- 3175
n <- 6155
```

- On `r n` unborn children `r boys` boys are observed.
- Is there a difference in the probability on the gender of an unborn child?

---

- The data are derived from a binary random variable $X$

  - $X=1$ for a boy and
  - $X=0$ for a girl.

- Note: count problem: the outcome is a count (number of boys)

- Formally we have considered a population of unborn children where each individual is characterized by a 0 or 1.

---

## Bernoulli Probability Mass Distribution

- Binary data can be modelled using a Bernoulli distribution:
  \begin{eqnarray*}
X_i &\sim& B(\pi) \text{ with}\\
B(\pi)&=&\pi^{X_i}(1-\pi)^{(1-X_i)},
\end{eqnarray*}

- It has one model parameter $\pi$

    - Expected value of $X_i$: $\text{E}[X_i]=\pi,$
    - Proportion of unborn boys (children with $X=1$) in the population.
    - Hence $\pi$ is the probability that a random individual from the population is a boy (an observation with $X=1$).

- The variance of Bernoulli data is also related to $\pi$.
$$\text{Var}[X_i]=\pi (1-\pi).$$

---

Some Bernoulli probability mass functions

```r
par(mfrow=c(1,3),pty="s")
probs=c(0.25,.5,.75)
for (i in 1:length(probs))
{
plot(c(0,1),c(1-probs[i],probs[i]),ylim=c(0,1),type="h",xaxt="n",xlab="X",ylab="Probability",main= as.expression(substitute(pi == val,list(val=probs[i]))),lwd=3)
axis(1,at=c(0,1))
}
```

---

- In the Saksen study  6155 observaties were sampled at random from the population.
- We can estimate $\pi$  using the sample mean:
$$\hat \pi = \bar X = \frac{\sum\limits_{i=1}^n X_i}{n},$$

```r
pi=boys/n
pi
```

In our example $\bar x =$ `r boys` / `r n` = `r format(pi*100,digits=3)`%.

---

## Binomiale test

- Is the observed probability `r format(pi*100,digit=3)`% that an unborn child is male, sufficient evidence to conclude that there is a higher chance on a boy than on a girl?

- Statistical test for
  $$H_0: \pi=1/2 \text{ versus } H_1: \pi\neq 1/2,$$

- We need known the distribution of

    - $X$ and $\bar X$
    - or of the sum $S=n\bar X$.

---


- Suppose that $H_0:\pi=1/2$ is true (boys and girls have an equal frequency in the population)
- A random individual from the population has a probability of $$P(X=1)=\pi=1/2.$$ to be a boy

- Two children that are drawn independently :

    - Probability of $\pi=1/2$ on a boy for the first and second child (independent from each other)
    - Outcomes $(x_1, x_2)$ for both children have 4 possible combinations:
    $(0,0),(0,1),(1,0)\text{ en }(1,1).$
    - Each of them has a probability of $1/4 = 1/2 \times 1/2$.

- Random variable $S$ is the sum of the outcomes :

$(x_1,x_2)$|$s$|$P(S = s)$|
|:---:|:---:|:---:|
(0,0)|0|1/4|
(0,1), (1,0)|1|1/2|
(1,1)|2|1/4|

---

###General: $n$ independent samples

- Probability for $\pi$ on success ($X=1$)
- Total number of successes $S$ (sum of all values of 1) can take $n+1$ possible values
  $$S=k\text{, met }k=0,\ldots,n$$
- Distribution of $S$?
\begin{equation}
P(S=k) = \left (
\begin{array}{c}
n \\
k \\
\end{array}
\right ) \pi^k (1-\pi)^{n-k}
\end{equation}
- $1-\pi$: probability on 0 for individual observation and
-  binomial coefficient
\begin{equation*}
\left (
\begin{array}{c}
n \\
k \\
\end{array}
\right ) = \frac{n \times (n-1) \times ...\times (n-k+1) }{ k!} = \frac{ n!}{ k!(n-k)! }
\end{equation*}

- In R you can calculate the probabilities on each $S=k$ with the function `dbinom(k,n,p)`


---

### Binomial Distribution

S is a:

-  *Binomial distributed random  variable* with *Binomial probability mass function*

- Parameters

    - $n$ (total number of draws from the population, is equivalent to maximal value of the outcome)
    - $\pi$ (probability on `success` for each draw).

- Calculate probability on $k$ successes on $n$ independent draws each with a succes probability of $\pi$.
- For binary data X.
- e.g.: wild type vs mutant of a gene, infected or not infected with HIV, ...
- Use: Compare proportions or risks on a particular event between groups.

---

### Some Binomial probability mass functions.

```r
par(mfrow=c(2,2))
probs=c(0.25,.5,.75)
for (i in 1:length(probs))
{
plot(0:10,dbinom(0:10,prob=probs[i],size=10),ylim=c(0,1),type="h",xlab="X",ylab="Kans (Dichtheid)",main= as.expression(substitute(pi == val,list(val=paste(probs[i],", nobs=10")))),lwd=3)
}
plot(2925:3225,dbinom(2925:3225,prob=.5,size=n),type="h",xlab="X",ylab="Kans (Dichtheid)",main= as.expression(substitute(pi == val,list(val=paste0("0.5, nobs=",n)))))
```

---

Test statistic $$H_0:\pi=1/2\text{ vs }H_1:\pi\neq 1/2$$


- $\bar X-1/2$ or, equivalent,
- $\Delta=n(\bar X-\pi_0)=S-s_0$.
- Distribution of the latter test statistic can be derived immediately from the Binomial distribution:
  - We observe $s=$ `r boys` and thus $\delta=s-s_0=$ `r boys` $-$ `r n` $\times 0.5=$ `r boys-n/2`.
  - When boys and girls are equally likely, i.e. under $H_0:\pi=1/2$, we will get following two-sided p-value:
    $$p=\text{P}_0\left[S-s_0\geq \vert \delta\vert \right] + \text{P}_0\left[S-s_0\leq - \vert \delta\vert \right].$$

- Note, that we can rewrite it in terms of S.
$$p=\text{P}_0\left[S\geq s_0+ \vert \delta\vert \right] + \text{P}_0\left[S \leq s_0 - \vert \delta\vert \right].$$

---

- For the Saksen study we calculate:

\begin{eqnarray*}
\text{P}_0\left[S\geq s_0+ \vert \delta\vert \right] &=& P(S \geq 6155 \times 0.5 + \vert 3175 - 6155 \times 0.5\vert ) \\&=& P(S \geq 3175)\\
&= &P(S= 3175) + P(S=3176) + ... + P(S=6155)\\
& =& 0.0067\\\\
\text{P}_0\left[S \leq s_0 - \vert \delta\vert \right] &=& P(S \leq  6155 \times 0.5 - \vert 3175- 6155 \times 0.5\vert) \\&=& P(S \leq 2980)\\ &= &P(S=0) + ... + P(S=2980) \\
&=&0.0067
\end{eqnarray*}

- The Binomial distribution is symmetric for$\pi=1/2$:
$$\text{P}_0\left[S\geq s_0+ \vert \delta\vert \right] = \text{P}_0\left[S \leq s_0 - \vert \delta\vert \right]$$
- This is no longer the case when $\pi$ deviate from 0.5.

---


```r
pi0 <- 0.5; s0 <- pi0 *n
delta <- abs(boys- s0)
delta

sUp <- s0 + delta
sDown <- s0 -delta
c(sDown,sUp)

pUp <- 1-pbinom(sUp-1,n,pi0)
pDown <- pbinom(sDown,n,pi0)
p <- pUp+pDown
c(pUp,pDown, p)
```

---


- If $\pi= 1/2$, the probability to observe at least  $\delta=$ `r delta` boys more or less than the mean under $H_0: s_0=$ `r s0` in a random sample under H_0 is only `r format(p*100,digits=3)`% is: **$p$-value of binomial test.**
- Very unlikely to observe such a large number of boys in a random sample when boys and girls have the same  frequency in the population (under $H_0$).
- Hence the hypothesis that the frequency of boys and girls is the same is not supported by the data.

---

```r
plot(s0+seq(-150.5,150.5,1),dbinom(s0+seq(-150.5,150.5,1),prob=.5,size=n),type="h",xlab="X",ylab="Probability",main= as.expression(substitute(pi == val,list(val=paste0("0.5, nobs=",n)))),ylim=c(-.0009,0.011))
abline(v=s0,lwd=2,col=4)
abline(v=boys,lwd=2,col=2)
abline(v=sDown,lwd=1,col=2,lty=2)
text(c(sDown,s0,boys,boys),c(rep(0.011,3),0.01),labels=c(expression(paste(s[0]-delta)),expression(s[0]),expression(s==s[0]+delta),as.expression(substitute(s==val,list(val=boys)))),pos=4,col=c(2,4,2))
text(sDown-50,-.0005,label="p-value",col=2,pos=4)
text(sUp,-.0005,label="p-value",col=2,pos=4)
arrows(s0+1500.5,-.0009,sUp,-.0009,col=2,lwd=2,angle=20,length=.1)
arrows(s0-1500.5,-.0009,sDown,-.0009,col=2,lwd=2,angle=20,length=.1)
```

---

The test can immediately be conducted using the `binomial.test` function in R.

```r
binom.test(x=boys,n=n,p=pi0)
```

On the 5% significance-level we conclude that there is on average a higher probability on a unborn male child than an unborn female child.

---

### Confidence interval on a proportion

- Estimator of the proportion of boys in the population  is the sample mean $\hat \pi=\bar x=$ `r format(pi,digits=3)`
- The standard error is
$$SE_{\bar x}=\sqrt{\frac{\text{Var}[X]}{n}}=\sqrt{\frac{\pi(1-\pi)}{n}}$$
- We can estimate this based on the sample: $SE_{\bar x}=\sqrt{\frac{\hat\pi(1-\hat\pi)}{n}}=$ `r format(sqrt(pi*(1-pi)/n),digits=2)`.
- 95% CI via CLT: $\hat\pi \pm 1.96 SE_{\hat\pi}.$

```r
se=sqrt(pi*(1-pi)/n)
pi+c(-1,1)*qnorm(0.975)*se
```

---

### CI on proportion in small sample?

```r
CI <- binom.test(x=boys,n=n,p=pi0)$conf.int
CI
```

---


### Conclusion

- Note that the test for a proportion is equivalent to a one-sample t-test for binary data.

- For the Saksen population we conclude at the 5% significance level that the gender of unborn children is more likely to be male than female ($p=$ `r round(binom.test(x=boys,n=n,p=pi0)$p.value,3)`).
The probability that an unborn child is male equals `r format(pi*100,digits=3)`% (95% CI [`r paste(format(CI*100,digits=3),collapse=",")`]%).

---

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Test for association between two qualitative variables →](03-test-for-association-between-two-qualitative-variables.md)
