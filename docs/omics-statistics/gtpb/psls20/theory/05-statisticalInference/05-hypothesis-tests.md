---
title: Hypothesis tests
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference.Rmd
source_file: sources/gtpb-psls20/theory/05-statisticalInference.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Hypothesis tests

**Source:** [`theory/05-statisticalInference.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

## Captopril Example:
Researchers want to assess if the drug captopril decreases the blood pressure for patients with hypertension.

- Is there no/an effect of administering captopril on the systolic blood pressure?

- It is not obvious to draw such conclusions based on a small sample

- It is uncertain if we can generalized the observations in the sample towards the population!

- Is the apparent beneficial effect systematic or random?

```r
captoprilTidy %>%
  filter(type%in%c("SBPa","SBPb")) %>%
  mutate(type=factor(type,levels=c("SBPb","SBPa")))%>%
  ggplot(aes(x=type,y=bp)) +
  geom_line(aes(group = id)) +
  geom_point()
```

```r
captopril$deltaSBP<-captopril$SBPa-captopril$SBPb
captopril%>%
  ggplot(aes(x="Systolic blood pressure",y=deltaSBP)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")+
  ylab("Difference (mm mercury)") +
  xlab("")
```


- The average blood pressure difference $\bar X$ is a natural basis to base our decision on.

$$\bar x\text{=`r round(mean(captopril$deltaSBP),2)` (s=`r round(sd(captopril$deltaSBP),2)`, SE=`r round(sd(captopril$deltaSBP)/sqrt(15),2)`)}$$

- It is not enough that $\bar{x}< 0$ to conclude that the systolic blood pressure is on average lower upon administrating captopril *at the level of the entire population*.

- To generalize the effect we observe in the sample to the population it has to be sufficiently large.

- But, how large?

---

### Hypothesis tests

- For this purpose statistical hypothesis tests have been developed
- They give a black/white answer
- It is almost impossible to read a scientific publication without results of statistical tests.
- According to the *falsification principle* of Popper we can never prove a hypothesis based on data.

    - Hence we will introduce two hypotheses: a null hypothesis $H_0$ and an alternative hypothesis $H_1$.

    - We will try to falsify the null hypothesis based on the statistical test.

#### Captopril

- Based on the sample we cannot prove that there is an effect of administering captopril ($H_1$ , alternative hypothesis).

- We therefore suppose that there is no effect of captopril.

    - We refer to this as the null hypothesis $H_0$.

    - Falsify ("try to reject") the $H_0$.

    - How likely is it to observe an effect that is at least as large as what we have seen in the sample in a random sample when  $H_0$ is true?

---


#### Permutation test


- Under $H_0$ the blood pressure measurements before and after administering captopril are two base line blood pressure measurements for a patient

- Under H$_0$ we can shuffle (permute) the blood pressure measurements for each patient.


```r
captoprilSamp<-captopril
perm<-sample(c(FALSE,TRUE),15,replace=TRUE)
captoprilSamp$SBPa[perm]<-captopril$SBPb[perm]
captoprilSamp$SBPb[perm]<-captopril$SBPa[perm]
captoprilSamp$deltaSBP <- captoprilSamp$SBPa-captoprilSamp$SBPb
captoprilSamp %>%
  gather(type,bp,-id) %>%
  filter(type%in%c("SBPa","SBPb")) %>%
  mutate(type=factor(type,levels=c("SBPb","SBPa")))%>%
  ggplot(aes(x=type,y=bp)) +
  geom_line(aes(group = id)) +
  geom_point()
```


```r
data.frame(deltaSBP=c(captopril$deltaSBP,captoprilSamp$deltaSBP),shuffled=rep(c(FALSE,TRUE),each=15)) %>%
  ggplot(aes(x=shuffled,y=deltaSBP)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")+
  stat_summary(fun.y=mean, geom="point", shape=19, size=3, color="red", fill="red") +
  ylab("Difference (mm mercury)")
```

And we permute again


```r
captoprilSamp<-captopril
perm<-sample(c(FALSE,TRUE),15,replace=TRUE)
captoprilSamp$SBPa[perm]<-captopril$SBPb[perm]
captoprilSamp$SBPb[perm]<-captopril$SBPa[perm]
captoprilSamp$deltaSBP <- captoprilSamp$SBPa-captoprilSamp$SBPb

captoprilSamp %>%
  gather(type,bp,-id) %>%
  filter(type%in%c("SBPa","SBPb")) %>%
  mutate(type=factor(type,levels=c("SBPb","SBPa")))%>%
  ggplot(aes(x=type,y=bp)) +
  geom_line(aes(group = id)) +
  geom_point()

data.frame(deltaSBP=c(captopril$deltaSBP,captoprilSamp$deltaSBP),shuffled=rep(c(FALSE,TRUE),each=15)) %>%
  ggplot(aes(x=shuffled,y=deltaSBP)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")+
  stat_summary(fun.y=mean, geom="point", shape=19, size=3, color="red", fill="red") +
  ylab("Difference (mm mercury)")
```


- We will do this 10000 times and we will keep track of the mean.
- We basically only have to swap the signs of the observed blood pressure differences $x$ when we shuffle.

```r
#generate a matrix with 15 rows and 10000 columns which consist of -1 and 1
permH<-sample(c(-1,1),150000,replace=TRUE)
dim(permH)<-c(15,10000)

#calculate the means for the permuted data
muPerm<-colMeans(permH*captopril$deltaSBP)
muPerm %>%
  as.data.frame %>%
  ggplot(aes(x=.)) +
  geom_histogram() +
  geom_vline(xintercept=mean(captopril$deltaSBP),col="blue")
```

- We observe that not one of the means that were obtained under $H_0$ (by permutation) were as extreme as the sample mean we observed in the captopril study.

- So the probability to observe a blood pressure drop that is larger then the one in the captopril study in a random sample generated under the null hypothesis is  smaller then 1 out of 10000.

So we have strong evidence that $H_0$ is incorrect and we thus we reject it and conclude $H_1$: There is an effect of administering captopril on the blood pressure of patients with hypertension.

---

### Pivot

- In practice we always use statistics that balance the effect size (average difference) to the noise (standard error)

- When we falsify the null hypothesis, we standardize the mean around $\mu_0=0$ the mean under $H_0$

$$t=\frac{\bar X-\mu_0}{se_{\bar X}}$$

- for the captopril example this becomes:
$$\frac{`r round(mean(captopril$deltaSBP),2)`-0}{`r round(sd(captopril$deltaSBP)/sqrt(15),2)`}=`r round(mean(captopril$deltaSBP)/(sd(captopril$deltaSBP)/sqrt(15)),2)`$$


We now determine the null distribution of test statistic t with permutation.

```r
deltaPerms<-permH*captopril$deltaSBP
tPerm<-colMeans(deltaPerms)/(apply(deltaPerms,2,sd)/sqrt(15))
tOrig<-mean(captopril$deltaSBP)/sd(captopril$deltaSBP)*sqrt(15)

tPermPlot<- tPerm %>%
  as.data.frame %>% ggplot(aes(x=.)) +
  geom_histogram(aes(y=..density.., fill=..count..)) +
  geom_vline(xintercept=tOrig,col="blue")
tPermPlot
```

- Again, none of the permutations gives a t-statistic as extreme as the one observed in the captopril study.

When there is no effect of captopril it is nearly impossible to obtain a test statistic as extreme as the one that was observed (  t=`r round(tOrig,2)`).

- The probability to observe a larger blood pressure drop then the one we observed in our sample in a random sample under $H_0$ is smaller 1/10000.

- We refer to this probability with the *p-value*.

- It measures the strength of the evidence against the null: the smaller the p-value the more evidence we have that the null is not true.

- The distribution has a nice bell shape.

---

### How do we decide?

When is the p-value sufficiently small to conclude that there is strong evidence against the null hypothesis?

- We typically work at a significance level of $\alpha=0.05$

- We state that we conducted the test at the 5% significance level

---

### Permutation tests are computationally demanding

- Can we assess how extreme the blood pressure drop was without permutation?

- We know that the blood pressure differences are approximately Normally distributed, so

$$t=\frac{\bar X - \mu}{se_{\bar X}}$$

follows a t-distribution (with 14 df for the captopril example).


- Under H$_0$ $\mu=0$ and $$t=\frac{\bar X-0}{se_{\bar X}}\sim f_{T,14}$$

```r
tPermPlot +
  stat_function(fun=dt,color="red",args=list(df=14))
```

- Note, the permutation null distribution indeed corresponds to a t-distribution with 14 degrees of freedom.

- So we can conduct the statistical test using statistical modelling of the data.

- We need to make assumptions for this, which we verify in the data exploration phase.


---


## Hypotheses

<details><summary>Click to see more formal details </summary><p>

Translate the research question to a null hypothesis ($H_0$) and an alternative hypothesis ($H_1$)

First the we need to translate the research question to a parameterized statistical model.

- From the experimental design it follows that  $$X_1,...,X_n \text{ i.i.d } f(X),$$ with $f(X)$ the density function of blood pressure differences.

- **Simplify**: assume that $f(X)$ is known except for an finite dimensional set of parameters $\mathbf{\theta}$ that still has to be estimated (parametric statistic model).
</p></details>

### Captopril example

<details><summary>Click to see more formal details </summary><p>
$X \sim N(\mu,\sigma^2)$ with $\mathbf{\theta}=(\mu,\sigma^2)$, the mean $\mu$ and variance $\sigma^2$.

The research question is now translated in terms of the average blood pressure drop: $\mu=E_f[X]$.

The **alternative hypothesis** is formulated in terms of a parameter of $f(X)$ and has to express what the researchers want to prove with the study.

- Here:
$$H_1: \mu<0.$$ On average the blood pressure of patients with hypertension decreases upon administering captopril.


The **null hypothesis** generally expresses a null condition, i.e. when notting exceptional happens.

- Researchers typically aim to prove via empirical research that observing the data under the null is highly unlikely so that they can reject the null hypothesis:
**Falsification principle**.

- The **null hypothesis is typically expressed with the same model parameter as the one used for $H_1$.**

- Here:
$$H_0 : \mu=0$$ i.e. on average the systolic blood pressure remains unchanged upon administering captopril.

</p></details>

---

## Test-statistic

<details><summary>Click to see more formal details </summary><p>

Once the population, the parameters, and, $H_0$ and $H_1$ are determined the concept of hypothesis testing is as follows:


Construct a test statistic so that it

1. measures evidence in the sample,
\vspace{10pt}
2. against the null hypothesis, and
\vspace{10pt}
3. in favour of the alternative hypothesis.

A test statistic thus has to be a function of the observations in the sample.

</p></details>

### Captopril example

<details><summary>Click to see more formal details </summary><p>

$$T=\frac{\bar{X}-\mu_0}{\text{SE}_{\bar X}}$$
With $\mu_0=0$ under $H_0$

Again

- If $H_0$ holds there is no effect of captopril on the blood pressure in the population and then we expect test statistic $T$ close to 0.

- If $H_1$ is true we expect $T<0$.

- In the captopril example we observe $t=(-18.93-0)/2.33=-8.12$.

- Is $t = -8.12$ large enough in absolute value to conclude that  $\mu < 0$ and with which confidence can we make this conclusion?

- We known that t follows a t-distribution with 14 d.f. under $H_0$

</p></details>

---

## p-value

The p-value is the probability to balance between $H_0$ and $H_1$.

The way how we calculate it is context dependent

- For the captopril example we have
  $$
    p = P\left[T \leq t \mid H_0\right] = \text{P}_0\left[T\leq t\right],
  $$
with the index "0" in $\text{P}_0\left[.\right]$ indicates that the probability is calculated under $H_0$.

It gives the probability to observe a test statistic $T$ lower or equal to the value observed in the current sample in a random sample under $H_0$
    - i.e. a test statistic $T$ in the random sample under $H_0$ with a value that is more extreme, more in the direction of $H_1$ then the one observed in the current sample.

### Captopril example

<details><summary>Click to see more formal details </summary><p>

- The $p$-value for the captopril example is calculated as follows
  $$p= \text{P}_0\left[T\leq -8.12\right]=F_t(-8.12;14) = 0.6\ 10^{-6}.$$

  with $F_t(;14)$ the cumulative distribution function of a t-distribution with 14 degrees of freedom:

$$F_t(x;14)=\int\limits_{-\infty}^{x} f_t(x;14).$$

and $f_t(.;14)$ the density function of the t-distribution.


- We calculate this probability in R with `pt(x,df)`

    - the value of the observed test statistic `x` en
    - the number of degrees of freedom of the t-distribution `df`.

- `pt(x,df)` calculates the probability to observe a value smaller or equal to x when we would draw a random sample from a t-distribution with df degrees of freedom.

```r
n <- length(captopril$deltaSBP)
stat<-(mean(captopril$deltaSBP)-0)/(sd(captopril$deltaSBP)/sqrt(n))
stat
pt(stat,n-1)
```

</p></details>

In practice we will not calculate the test ourself, but we will use the function t.test:

```r
t.test(captopril$deltaSBP, alternative = "less")
```

Note, that we need to specify the argument `alternative="less"` so that the p-value would be calculated in the left tail.

The function also gives a one-sided interval because we test in one direction.

---

### Definition of the p-value

The **p-value** (also referred to as the **observed significance level**) is the probability to observe a test statistic in a random sample under the null hypothesis that is as or more extreme then the test statistic observed in the current sample.

- The smaller the probability the more evidence against $H_0$.

- Note, that the p-value is **not** the probability that null hypothesis is true!

- The word "extreme" indicates on the direction in which the test statistic is more likely under the alternative hypothesis.

- In the example $H_1: \mu < 0$ and we thus expect very negative values for $t$ under $H_1$.

- From the definition small $p$-values indicate that observed test statistic is unlikely under the assumption that $H_0$ is correct.

- Thus a small value of $p$-value means that we have to **reject  $H_0$** in favour of $H_1$.

- The threshold that we use to compare the $p$-value with is referred to as the **significance level** and is denoted with $\alpha$.

- A statistical test conducted on the $\alpha$ significance level is also referred to as a **level-$\alpha$ test**.

A test result is *statistically significant* if $p<\alpha$

- $\alpha$ is commonly set at 5\%.

- The smaller the p-value the more `significant' the test result deviates from what can be expected under $H_0$.

- It summarizes the evidence against the null.

$$\begin{array}{cl}>0.10 & \text{ non significant (no evidence)}\\0.05-0.10 & \text{ marginal significant, weak evidence (do not use this yourself)}\\0.01-0.05 & \text{ significant}\\0.001-0.01 & \text{strongly significant}\\<0.001 & \text{ extremely significant}\end{array}$$

---

## Critical value

```r
par(mar=c(6,6,6,2))
grid <-seq(-10,10,.01)
tcrit <- qt(0.05,n-1)
reject <- c(grid[grid<tcrit],tcrit)
plot(grid,dt(grid,n-1),type="l",lwd=2,xlab="t-statistic",ylab="density",cex.lab=2,cex.axis=2,cex.main=2)
abline(v=mean(captopril$deltaSBP)/se,col=2,lwd=2,lty=2)
abline(v=qt(c(.05),n-1),col=2,lty=1,lwd=2)
text(c(-5,-5,5,5),c(.21,.19,.21,.19),label=c("rejection-","region","acception-","region"),col=c(2,2,4,4))
arrows(-100,.4,mean(captopril$deltaSBP)/se,.4,lwd=2,col=2,angle=20,length=.1)
text(-10,.35,label="p-value",srt=90,col=2)
arrows(-100,.2,tcrit,.2,lwd=2,col=2,angle=20,length=.1)
text(pos=4,mean(captopril$deltaSBP)/se,.02,label=paste("t=",round(mean(captopril$deltaSBP)/se,2)),col=2)
arrows(100,.2,tcrit,.2,lwd=2,col=4,angle=20,length=.1)
text(pos=4,tcrit,.02,label=paste("t-crit=",round(tcrit,2)),col=2)
polygon(c(reject,tcrit,-10),c(dt(reject,n-1),0,0),col=2,border=2)
text(-3.5,.05,label=expression(paste(alpha,"=0.05")),col=2)
arrows(-2,0.02,-3.5,.04,col=2,lwd=2,angle=20,length=.1)
```

---

## Decision Errors

The decision to accept or reject $H_0$ is made based on a single sample.
A wrong decision could have been made.

```r
library("kableExtra")
DecisionErrors=data.frame(Conclusion=c("Accept H0","Reject H0"),"H0"=c("OK","Type I ($\\alpha$)"),"H1"=c("Type II ($\\beta$)","OK"))
knitr::kable(DecisionErrors,,align="c")%>%
  kable_styling( position = "center") %>%
  add_header_above(c(" " = 1, "Reality" = 2))
```
 - Type I error, $\alpha$: wrongly reject the null hypothesis (false positive)
 \vspace{10pt}
 - Type II error, $\beta$: wrongly accept the null hypothesis

 - Decision is also stochastic! See first chapter of the course

### Captopril Example

- $H_0$: administering captopril has no effect on the systolic blood pressure

- $H_1$: administering captopril an average leads to a decrease in blood pressure

- **Type I error**: there is on average no blood pressure drop upon administering captopril, but we conclude that there is an effect of captopril.
- **Type II error**: there is on average a blood pressure drop upon administering captopril, but it is not picked up by the statistical test.

---

### Type I error is controlled

The type I error is controlled by the construction of the statistical test.

$$\text{P}\left[\text{type I error}\right]=\text{P}\left[\text{reject }H_0 \mid H_0\right] = \text{P}_0\left[T<t_{n-1;1-\alpha}\right]=\alpha $$


- The significance-level $\alpha$ is the probability to make a type I error.

- The statistical test ensures that the probability on a type I error is controlled at the significance level $\alpha$.

- The probability to correctly accept $H_0$ is $1-\alpha$.

- We can show that the p-value under $H_0$ is uniform distributed.

- So statistical hypothesis testing leads to a uniform decision strategy.

We will illustrate this in a simulation study

- n=15
- $\mu=0$ mmHg
- $\sigma =9$ mmHg
- number of simulations 1000

```r
nsim <- 10000
n <- 15
sigma <- 9
mu <- 0
mu0 <- 0
alpha=0.05

#simulate nsim samples of size n
deltaSim <- matrix(rnorm(n*nsim,mu,sigma),nrow=n,ncol=nsim)
pSim <- apply(deltaSim,2,function(x,mu,alternative) t.test(x,mu=mu,alternative=alternative)$p.value,mu=mu0,alternative="less")

mean(pSim<alpha)
pSim %>%
  as.data.frame %>%
  ggplot(aes(x=.)) +
  geom_histogram() +
  xlim(0,1)
```

- The type I error is indeed about 0.05
- The p-values are uniform

---

### Type II error

- Determine the type II error is less evident.
- We have to reason under $H_1$
- In the captopril voorbeeld is $H_1: \mu<0$
- Many alternatives are possible
- The distribution under $H_1$ is not fully specified

- *work-around:* choose one specific distribution under $H_1$.

 $$H_1(\delta): \mu=0-\delta \text{ for }\delta>0.$$

- e.g. a blood pressure difference of 2 mmHg

- 1-type II is also referred to as the power. It is the probability to pick up the alternative.

- It is not guaranteed by the design of the test

- It depends on the experimental design of the study


```r
nsim <- 10000
n <- 15
sigma <- 9
mu <- -2
mu0 <- 0
alpha=0.05

#simulate nsim samples of size n
deltaSim <- matrix(rnorm(n*nsim,mu,sigma),nrow=n,ncol=nsim)
pSim <- apply(deltaSim,2,function(x,mu,alternative) t.test(x,mu=mu,alternative=alternative)$p.value,mu=mu0,alternative="less")

mean(pSim<alpha)
pSim %>%
  as.data.frame %>%
  ggplot(aes(x=.)) +
  geom_histogram() +
  xlim(0,1)
```
- We observe that a power of `r mean(pSim<alpha)` or a type II error of `r 1-mean(pSim<alpha)`.

---

- When we increase the sample size

```r
nsim <- 10000
n <- 30
sigma <- 9
mu <- -2
mu0 <- 0
alpha=0.05

#simulate nsim samples of size n
deltaSim <- matrix(rnorm(n*nsim,mu,sigma),nrow=n,ncol=nsim)
pSim <- apply(deltaSim,2,function(x,mu,alternative) t.test(x,mu=mu,alternative=alternative)$p.value,mu=mu0,alternative="less")

mean(pSim<alpha)
pSim %>%
  as.data.frame %>%
  ggplot(aes(x=.)) +
  geom_histogram() +
  xlim(0,1)
```

- Increasing the sample size leads to a higher power.
- Still the power to pick up such a small blood pressure drop remains very low.
- A drop of 2 mmHg is also not relevant for drug companies.

![](https://www.nature.com/articles/nmeth.2738.pdf){width=100%}

---

### Interpretation

Suppose that given a particular sample $p<\alpha$, i.e. reject $H_0$

- Two possibilities

    - correct decision,
	  - or type I error.

- We known that the probability on a type error is low, i.e. $\alpha=0.05$.


On the other hand, when $p\geq\alpha$ and we do not reject $H_0$ we also have two options:

  - Correct decision,
  - or we made a type II error.

The probability on a type II error ($\beta$) is not controlled at a specific value.

Statistical test is constructed to only control the probability on a type I error at  $\alpha$.

To be scientifically correct we have to take a pessimistic attitude and we have to admit that $\beta$ can be large (i.e. a small power to detect the alternative).

Hence,

- $p < \alpha$ we reject $H_0$

    - We conclude that $H_1$ is probably correct.
	  - We refer to this as a strong conclusion.

- $p \geq \alpha$ accept $H_0$

	  - Does not imply that we accept $H_0$ correctly.
  	- We can only conclude that the data do not have enough evidence against the $H_0$ in favour of $H_1$.
    - We refer to this as a weak conclusion.
    - We typically conclude that the effect of the treatment is not significant.

---

## Conclusions captopril example

The test we have performed is referred to as

- the **one sample t-test** on the difference or

- a **paired t-test**. Indeed we dispose of paired observations for each patient!

- The test is done one-sided because we test against the alternative of a blood pressure drop.

- Both tests (one sample t-test on the difference and paired t-test) give the same results:

```r
t.test(captopril$deltaSBP,alternative="less")
```

```r
t.test(captopril$SBPa,captopril$SBPb,paired=TRUE,alternative="less")
```

---

### Conclusion

There is on average an extremely significant blood pressure drop upon administering captopril to patients with hypertension. The systolic blood pressure decreases on average with 18.9 mmHg upon the treatment with captopril (95% CI [$-\infty,-14.82$] mmHg).

Note that

1. A one-sided interval is reported because we are only interested in a blood pressure drop.

2. Because of the pre-test/post-test design we cannot distinguish between the effect of the treatment and a placebo effect. There was no good control! The lack of a good control typically occurs in  pre-test/post-test designs. How could we have improved the design?

---

## One-sided or two-side testing?

De test in the captopril example was a one-sided test. We only aim to detect if the captopril treatment on average reduces the blood pressure.

Suppose that we defined the blood pressure difference as  $X_{i}^\prime=Y_{i}^\text{before}-Y_{i}^\text{after}$

- Now, a positive value indicates a blood pressure drop

- The average change in blood pressure is now denote as $\mu^\prime=\text{E}[X^\prime]$.

- So now we should use a one-sided test to assess $H_0: \mu^\prime=0$ against $H_1: \mu^\prime>0$.

- p-value now becomes:
$$p=\text{P}_0\left[T\geq t\right].$$

---

Analysis based on $X^\prime$: Argument `alternative="greater"` so that we use $H_1: \mu^\prime>0$:
```r
t.test(captopril$SBPb-captopril$SBPa,alternative="greater")
```

Of course we obtain the same results. Only the sign is swapped.

---

### Two-sided test

Suppose that researchers wanted to assess the mode of action of the new drug captopril in the design phase and suppose that healthy subjects were used in an early phase of the drug development.

In this case it would have been interesting to observe blood pressure drops as well as gains.

Then we would require a two-sided test strategy

$$H_0: \mu=0$$
against the alternative hypothesis

$$H_1: \mu\neq0,$$

so that the mean under the alternative is different from zero.

It can be positive as well as negative changes and we did not know upfront in which direction the real mean will deviate from $H_1$.


We can conduct a two-sided test on the $\alpha=5\%$ significance level by

```r
grid <-seq(-10,10,.01)
tcrit <- qt(0.975,n-1)
reject1 <- c(grid[grid< -tcrit],-tcrit)
reject2 <- c(tcrit,grid[grid>tcrit])

plot(grid,dt(grid,n-1),type="l",lwd=2,xlab="t-statistic",ylab="density",ylim=c(-.05,.4))
abline(v=c(-1,1)*mean(captopril$deltaSBP)/se,col=2,lwd=2,lty=2)
abline(v=c(-1,1)*tcrit,col=2,lty=1,lwd=2)
text(c(-5,-5,5,5),c(-.03,-.05,-.03,-.05),label=c("rejection-","region","rejection-","region"),col=c(2,2,2,2))
text(c(0,0),c(-.03,-.05),label=c("acception-","regio"),col=c(4,4))

arrows(-100,.4,-abs(mean(captopril$deltaSBP)/se),.4,lwd=2,col=2,angle=20,length=.1)
arrows(100,.4,abs(mean(captopril$deltaSBP)/se),.4,lwd=2,col=2,angle=20,length=.1)
text(-10,.35,label="p-value",srt=90,col=2)
text(10,.35,label="p-value",srt=90,col=2)

arrows(-100,-.04,-tcrit,-.04,lwd=2,col=2,angle=20,length=.1)
arrows(100,-.04,tcrit,-.04,lwd=2,col=2,angle=20,length=.1)

polygon(c(reject1,-tcrit,-10),c(dt(reject1,n-1),0,0),col=2,border=2)
polygon(c(tcrit,reject2,tcrit),c(0,dt(reject2,n-1),0),col=2,border=2)

text(-3.5,.05,label=expression(paste(alpha,"/2=2.5%")),col=2)
text(3.6,.05,label=expression(paste(alpha,"/2=2.5%")),col=2)
arrows(-3,0.02,-3.5,.04,col=2,lwd=2,angle=20,length=.1)
arrows(3,0.02,3.5,.04,col=2,lwd=2,angle=20,length=.1)
```

---

The argument `alternative` of the `t.test` function is by default `alternative="two.sided"`.

```r
t.test(captopril$deltaSBP)
```

- We still obtain an extremely significant result.
- The p-value is double as large because we test two-sided.

Indeed

$$p=P_0[T \leq -\vert t \vert] + P_0[T \geq \vert t \vert] = P_0[\vert T \vert \geq \vert t \vert] = 2 \times P_0[T \geq \vert t \vert]$$

- We also obtain a  two-sided confidence interval

---

### One-sided or two-sided test?

With a one-sided test we can more easily reject $H_0$ on condition that $H_1$ is true than with a two-sided test.

- All information is used to test into one direction

- The decision to test one-sided has to be done in the design phase before the experiment is conducted

- Even if we have strong a priori presumptions, we are not entirely sure otherwise we would have no reason to do the research.

- If we propose a one-sided test in the design phase and we observe a result in the opposite direction that would be statistically significant we can not draw conclusions from the experiment.

- In the design phase we have excluded this result because it is so unexpected that it has to be a false positive.

- Hence, one-sided tests are not recommended.

A two-sided test can always be defended and allows you to detect any deviation of $H_0$ and is highly recommended.


It is **never allowed** to change a two-sided test into a one-sided test based on what has been observed in the sample! Otherwise the type I error of the test strategy is not correctly controlled.

---

We illustrate this in the simulation study below:

1. correct two-sided test and
2. one-sided test with its sign based on what was observed in the sample.


```r
mu <- 0
sigma <- 9.0
nSim <- 1000
alpha <- 0.05
n <- 15
pvalsCor <- pvalsInCor<-array(0,nSim)
for (i in 1:nSim)
{
	x <- rnorm(n,mean=mu,sd=sigma)
	pvalsCor[i] <- t.test(x)$p.value
	if (mean(x)<0)
		pvalsInCor[i] <- t.test(x,alternative="less")$p.value else
		pvalsInCor[i] <- t.test(x,alternative="greater")$p.value
}

mean(pvalsCor<0.05)
mean(pvalsInCor<0.05)
```

- Type I error correctly controlled at $\alpha$ for two-sided test.
- Type I error not correctly controlled when we test one-sided based on what we observed in the sample.

---

[← Estimation](04-estimation.md) · [Up: contents](index.md) · [Nature column on testing →](06-nature-column-on-testing.md)
