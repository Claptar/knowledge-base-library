---
title: Direct cholesterol example
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd
source_file: sources/gtpb-psls20/theory/02-concepts.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`theory/02-concepts.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Direct cholesterol example

### Empirical distribution

- We can estimate the direct cholesterol distribution of females using a histogram

```r
NHANES %>% filter(Gender=="female") %>%
ggplot(aes(x=DirectChol)) +
geom_histogram()
```

- Note, that the distribution is skewed with a tail to the right.

- We can estimate the cumulative distribution function using the empirical cumulative distribution function.
    - Every observation in the sample is observed once.
    - So the empirical distribution of the sample is a discrete distribution with probability of 1/n on every observation.
    - The empirical cumulative distribution function then becomes
    $$ECDF(x) = \sum\limits_{x_i \leq x} \frac{1}{n} = \frac{# (x_i \leq x)}{n}$$

```r
fem <- NHANES %>% filter(Gender=="female"&!is.na(DirectChol))
fem %>%
ggplot(aes(x=DirectChol)) +
stat_ecdf()
```

```
- We also illustrate this for a sample with sample size 10
```

```r
set.seed(1)
fem10<- NHANES %>% filter(Gender=="female"&!is.na(DirectChol)) %>% sample_n(size=10)
fem10 %>% ggplot(aes(x=DirectChol)) +
stat_ecdf()
```

---

### Normal approximation

- In the introduction we have seen that the log transformed direct cholesterol levels had a nice bell shape.

```r
  fem %>% ggplot(aes(x=DirectChol%>%log2))+
  geom_histogram(aes(y=..density.., fill=..count..)) +
  xlab("Direct Cholesterol (log2)") +
  stat_function(fun=dnorm,color="red",args=list(mean=mean(fem$DirectChol%>%log2), sd=sd(fem$DirectChol%>%log2)))
```

- We can now approximate the distribution of log2 transformed direct cholesterol levels using a normal distribution.

- We only have to estimate two parameters: the mean and the variance. We can do this based on the sample mean ($\bar x$) and sample variance ($s^2$) or sample standard deviation ($s$).

```r
xBar<-mean(fem$DirectChol%>%log2)
sdBar<-sd(fem$DirectChol%>%log2)
xBar
sdBar
```

- We can do the same thing for the small sample with 10 women.

```r
  fem10 %>% ggplot(aes(x=DirectChol%>%log2))+
  geom_histogram(aes(y=..density.., fill=..count..),bins=10) +
  xlab("Direct Cholesterol (log2)") +
  stat_function(fun=dnorm,color="red",args=list(mean=mean(fem10$DirectChol%>%log2), sd=sd(fem10$DirectChol%>%log2))) +
  xlim(-2,2)
```

```r
xBar10<-mean(fem10$DirectChol%>%log2)
sdBar10<-sd(fem10$DirectChol%>%log2)
xBar10
sdBar10
```

---

### Reference intervals

- Normal values for the cholesterol levels in the population can be calculated using a reference interval. Typically a 95% reference interval is used, so that 95% of the subjects in the population are expected to have a value for the characteristic that falls into the reference interval.

- We can do this based on the empirical distribution using the quantile function. We need to calculate the quantiles $\hat{F}(x_{2.5\%})=0.025$ and $\hat{F}(x_{97.5\%})=0.975$ so that 95% of the values are located in the interval [x_{2.5%},x_{97.5%}] .

- Large sample

```r
quantile(fem$DirectChol,prob=c(0.025,0.975))
```

- So based on the large sample, we estimate that 95% of the females in the population have a direct cholesterol level in the interval [`r quantile(fem$DirectChol,prob=c(0.025,0.975))`].

- Small sample

```r
quantile(fem10$DirectChol,prob=c(0.025,0.975))
```

- Note, that this estimate is very crude. In the small sample,  We do not have enough observations to have a good approximation of the extreme quantiles.

#### Normal approximation

- We can use the function qnorm to calculate quantiles from the normal distribution.

- We also know that a 95% reference interval is located rougly in two standard deviations around the mean.

- We will have to use the function `2^` to transform the result back to the direct cholesterol domain.

- Large sample
```r
qnorm(0.025,mean=xBar,sd=sdBar) %>% .^2
qnorm(0.975,mean=xBar,sd=sdBar) %>% .^2
2^(xBar - 2 * sdBar)
2^(xBar + 2 * sdBar)
```

- Small sample
```r
qnorm(0.025,mean=xBar10,sd=sdBar10) %>% .^2
qnorm(0.975,mean=xBar10,sd=sdBar10) %>% .^2
2^(xBar10 - 2 * sdBar10)
2^(xBar10 + 2 * sdBar10)
```

---

### Conclusions

- For the large sample, the empirical distribution (quantile function) and the normal approximation gives us approximately the same result.

- For the small sample, however, the normal approximation works much better than the one based on the empirical distribution.

    - This is because we are looking at extreme quantiles 2.5% and 97.5%.
    - Indeed, we have very few observations at our disposal in the small sample to estimate these quantiles directly from the observations.
    - With the normal approximation we can use all the data to estimate the mean and the variance. So if the normal assumption holds, we get better estimates for these extreme quantiles.

---

## Statistics

- Formula will be used to estimate the parameters of a distribution in the population based on the sample. We call these statistics or estimators.

- The numeric result obtained by evaluating these formula are also called statistics or estimates.

- Researcher want to known the unknown parameters from the population and will thus estimate them using the statistics observed or calculated based on the sample

- Because we calculate the statistics based on the observations in the sample, they will also vary from sample to sample and are random variables and we denote them with capital letters (e.g. $\bar X$ for the sample mean and $S^2$ for the sample variance).

- So when we analyse data, we have to reason on how the statistics of interest will vary from sample to sample.

- When the statistics refer to a numeric value realised in a particular sample, we will use a small letter: $\bar x$ and $s^2$.

---

## Convention

- **Population parameters**  are fixed but unknown and we will denote them with $\rightarrow$ **Greek symbols**.

- **Statistics** that we use to estimate unknown parameters based on the sample are denoted with **letters** are with a hat.

- e.g. for normal distribution

| Population | Sample|
| :---: | :---: |
| $\mu$ | $\bar X$ or $\hat \mu$ |
| $\sigma^2$ | $S^2$ or $\hat \sigma$|

---

## [Home](https://gtpb.github.io/PSLS20/) {-}

---

[← Gender Example](05-gender-example.md) · [Up: contents](index.md)
