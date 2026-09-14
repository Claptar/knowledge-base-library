---
title: Describing the population
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd
source_file: sources/gtpb-psls20/theory/02-concepts.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Describing the population

**Source:** [`theory/02-concepts.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- It is impossible to predict the value of a random variable.

- The realised value of $X$ is subject to random variability.

- Suppose that we are interested in the IQ of subject. If we know how the data are distributed, we can use probability theory to calculate the probability that the IQ of a random subject of the population will be above 110.

---

##Intermezzo probability theory

### Discrete random variables

- Supose that we measure a discrete random variable $X$

- All possible values for the random variable $X$ are called the sample space $\Omega$.

    - For gender the sample space is $\Omega=(0,1)$ with 0 (male) or 1 (female).
    - Suppose that we role a dice, then the sample space is $\Omega=(1,2,3,4,5,6)$.

- An event $A$  is a subset of the sample space

      - Get an even number when rolling a dice: $A=(2,4,6)$.
      - Can also be $A=(1)$ one  subset of the sample space.

- Event space $\mathcal{A}$ is the class of all possible events associated with a given experiment.

- Two events ($A_1$ and $A_2$) are multiple exclusive if they cannot occur together

    - e.g. event of the odd numbers $A_1=(1,3,5)$ and the event of getting $A_2=(6)$
    - so $A_1 \bigcap A_2=\emptyset$.

- Probability $P(A)$  is a function $P: A \rightarrow [0,1]$ which satisfies

    1. $P(A) \geq 0$ and $P(A) \leq 1$ for each $A \in \mathcal{A}$
    2. $P(\Omega)=1$
    3. For multiple exclusive events $A_1, A_2, \ldots A_k$ the probability $P(A_1 \cup A_2 \ldots \cup A_k)= P(A_1) + \ldots + P(A_k)$

- Dice example

    - odd number $A=(1,3,5)$: this is the union of 3 multiple exclusive events $A_1=1$, $A_2=5$ and $A_3=5$ so
    $P(A)=P(1)+P(3)+P(5)=1/6+1/6+1/6=0.5$
    - $\Omega=(1,2,3,4,5,6)$: $P(\Omega)=1$

- If we draw two subjects (j and k) independently from the population then the joint probability on
$P(X_j,X_k)= P(X_j)P(X_j)$

---

#### Probability mass function

- The probability mass function for a random variable $X$ describes the probability of each possible value of the sample space.

- Example: Gender is a binary variable (0:male, 1:female) and binary variables are Bernoulli distributed. 50.8% of the subjects of the American population are female and 49.2% are male. Let $\pi$ be the probability on a female $\pi=0.508$.
    so
    $$ X\sim \left \{
    \begin{array}{lcl}
    P(X=0) &=& 1-\pi\\
    P(X=1) &=& \pi
    \end{array} \right . $$

    ```r
    data.frame(X=c(0,1),prob=c(0.492,0.508)) %>%
      ggplot(aes(x=X,xend=X,y=0,yend=prob)) +
      geom_segment() +
      ylab("Probability")
    ```

Random variable $X$ follows an Bernoulli distribution $B(\pi)$ with parameter $\pi=0.508$,
    $$B(\pi)= \pi^x(1-\pi)^{(x-1)}$$

---

#### Cumulative distribution function

- The cumulative distribution function is the function F(x) that calculates the probability to observe a random variable X for which $X\leq x$:
$$ F(x) = \sum\limits_{\forall X\leq x} P(x)$$

- Gender example $F(0)=1-\pi$ and F(1)=P(X=0) + P(X=1)=1

    ```r
    data.frame(X=c(0,1),cumprob=c(0.492,1)) %>%
      ggplot(aes(x=X,xend=X,y=0,yend=cumprob)) +
      geom_segment() +
      ylab("F(x)")
    ```

- Dice:

    ```r
    data.frame(X=1:6,cumprob=cumsum(rep(1/6,6))) %>%
      ggplot(aes(x=X,xend=X,y=rep(0,6),yend=cumprob)) +
      geom_segment() +
      ylab("F(x)")
    ```

---

#### Mean

The mean or the expected value $E[X]$ of a discrete random variable is given by

$$E[X]=\sum\limits_{x\in\Omega} x P(X=x)$$

- Gender example

    - $E[X]= 0 \times (1-\pi) + 1 \times \pi = \pi$
    - The mean equals $E[X]=0.508$.

- Dice example:
$ E[X]= 1 \times 1/6 + 2 \times 1/6 + \ldots + 6 \times 1/6 = $ `r sum(1:6)/6`

---

#### Variance

The variance is a measure for the variability of a random variable and  is given by

$$E[(X-E[X])^2]=\sum\limits_{x\in\Omega} (x-E[X])^2 P(X=x)$$

- Gender example
    \begin{eqnarray}
    E[(X-E[X])^2]&=&(0-\pi)^2\times (1-\pi)+(1-\pi)^2 \times \pi\\
    &=& \pi^2 (1-\pi) + (1-\pi)^2 \pi\\
    &=&\pi (1-\pi)(\pi+1-\pi)\\
    &=&\pi(1-\pi)
    \end{eqnarray}

---

### Continuous random variable


- The density function $f(x)$ describes how likely it is to observe a particular value of random variable X when we sample a random subject from the population.

- Many biological characteristics are approximatively normally distributed (upon transformation)
    $$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

- This is denoted in shorthand as $f(x) = N(\mu,\sigma^2)$

- The IQ in the population is known to follow a normal distribution with mean $\mu=100$ and standard deviation $\sigma=15$.
$$IQ \sim N(100,15^2)$$


- R we can use the dnorm function to calculate the density of particular values of X=x.

- The arguments of `dnorm` are `mean` ($\mu$) and `sd` (standard deviation $\sigma$).

```r
par(mar=c(5, 4, 4, 2) + 0.1, mai=c(1.02,0.82,0.82,0.42))
grid <- seq(40,160,.1)
plot(grid,dnorm(grid,mean=100,sd=15),
     xlab="IQ",
     col=2,ylab="Densiteit",type="l",lwd=2,cex.lab=1.5,cex.axis=1.5)
```

- Within certain limits, continuous variables can take all possible values so the sample space $\Omega$ is infinitely large.

---

####Cumulative distribution

- Again the cumulative distribution $F(X)=P(X\leq x)$.

- Because X is continuous we will calculate this probability using an integral
$$F(x)=\int \limits_{-\infty}^x f(x) dx$$

- Note that $f(x)=0$ if x does not belong to the sample space.

- We can calculate $F(x)$ for a normally distributed random variable using the `pnorm` function again with arguments `mean` and `sd`.

```r
plot(grid,pnorm(grid,mean=100,sd=15),type="l",xlab="IQ",ylab="Probability")
```

So the probability that the IQ of a random subject is below 80 can be obtained by

```r
pnorm(80,mean=100,sd=15)
```

```r
grid2<-seq(40,80,.01)
plot(grid,dnorm(grid,mean=100,sd=15),
     xlab="IQ",
     col=2,ylab="Densiteit",type="l",lwd=2,cex.lab=1.5,cex.axis=1.5)
polygon(x=c(grid2,80,40),y=c(dnorm(grid2,100,15),0,0),col=2,border=2)
text(80,dnorm(80,mean=100,sd=15),paste0("P(X < 80) = ",round(pnorm(80,100,15)*100,1),"%"),col=2,cex=1.5,pos=4)
```

```r
plot(grid,pnorm(grid,mean=100,sd=15),type="l",xlab="IQ",ylab="Probability",lwd=2,col=2)
lines(c(80,80,80,0),c(0,rep(pnorm(80,100,15),3)),lty=2)
```

- For the largest possible value of $X$ we integrate over the entire sample space $\Omega$ so
$$\int \limits_{x \in \Omega} f(x) dx=1$$

- So the area under the density function equals 1!

---

#### Mean and Variance.

- The mean or the expected value $E[X]$ of a continuous random variable is given by

$$\int \limits_{x \in \Omega} x f(x) dx$$

- For the normal distribution
$$\int \limits_{-\infty}^{+\infty} x f(x) dx = \mu$$

- The variance $E[(X-E[X])^2]$ is given by

$$\int \limits_{x \in \Omega} (x-E[X])^2 f(x) dx$$

- For the normal distribution we get

$$\int \limits_{-\infty}^{+\infty} (x-\mu)^2 f(x) dx = \sigma^2$$

- It is often difficult to interpret the variance because it is not in the same unit as the random variable and the mean.
We therefore often use the standard deviation

$$SD=\sqrt{E[(X-E[X])^2]}$$


The SD for a normal distribution, $\sigma$ has the nice interpretation that approximately 68% of the population has a value for the characteristic X within the interval of one standard deviation ($\sigma$) around the mean:

$$P(\mu-\sigma < X < \mu + \sigma) \approx 0.68$$


```r
grid2<-seq(85,115,.01)
plot(grid,dnorm(grid,mean=100,sd=15),
     xlab="IQ",
     col=2,ylab="Densiteit",type="l",lwd=2,cex.lab=1.5,cex.axis=1.5)
polygon(x=c(grid2,115,85),y=c(dnorm(grid2,100,15),0,0),col="grey",border="grey")
text(115,dnorm(115,mean=100,sd=15),paste0("P(85<X<115) = ",round((pnorm(115,100,15)-pnorm(85,100,15))*100,1),"%"),col=2,cex=1.3,pos=4)
abline(v=100)
text(4,0,expression(mu))
lines(c(85,115),rep(dnorm(115,100,15),2))
text(107.5,dnorm(114.5,100,15),expression(sigma))
text(100-15/2,dnorm(114.5,100,15),expression(sigma))
```

- For normally distributed random variables approximately 95% of the subjects in the population have a value that lays in two standard deviations ($2 \sigma$) of the mean

$$P[\mu - 2 \sigma < X < \mu + 2 \sigma]\approx 0.95$$
```r
grid2<-seq(70,130,.01)
plot(grid,dnorm(grid,mean=100,sd=15),
     xlab="IQ",
     col=2,ylab="Densiteit",type="l",lwd=2,cex.lab=1.5,cex.axis=1.5)
polygon(x=c(grid2,130,70),y=c(dnorm(grid2,100,15),0,0),col="grey",border="grey")
text(115,dnorm(115,mean=100,sd=15),paste0("P(85<X<115) = ",round((pnorm(130,100,15)-pnorm(70,100,15))*100,1),"%"),col=2,cex=1.3,pos=4)
abline(v=100)
text(4,0,expression(mu))
lines(c(70,130),rep(dnorm(130,100,15),2))
text(115,dnorm(128,100,15),expression(sigma))
text(85,dnorm(128,100,15),expression(sigma))
```

---

- In R cumulative distribution can be calculated with the function rnorm. This function has arguments q the quantile, the mean and the standard deviation.

- If you want help you can always type:

```r
?pnorm
```

- What is the probability that a random subject in the population will have an IQ below 90?

```r
pnorm(q=90,mean=100,sd=15)
```

- What is the probability that a random subject in the population will have an IQ below 110?

- What is the probability that a random subject in the population will have an IQ between 90 and 110?

---

## Standardization

- Normal data are often standardized.

$$z=\frac{x-\mu}{\sigma}$$

- Upon standardization the data follow a standard normal distribution with mean $\mu=0$ and variance $\sigma^2=1$:
$$z \sim N(0,1)$$

We can use the qnorm function to calculate the quantile $z_{2.5\%}$ and $z_{97.5\%}$ corresponding to $F(z_{2.5\%})=0.025$ and $F(z_{97.5\%})=0.975$, respectively.

```r
qnorm(0.025)
qnorm(0.975)

```

This indeed  indicates that about 97.5%-2.5%=95% of a standard normal random variable falls within the interval [-2,2], or within 2 times the standard deviation ($\sigma=1$) from the mean ($\mu=0$).

---

---

[← Random Variables](05-random-variables.md) · [Up: contents](index.md) · [Sample →](07-sample.md)
