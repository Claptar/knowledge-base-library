---
title: Estimation
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference.Rmd
source_file: sources/gtpb-psls20/theory/05-statisticalInference.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Estimation

**Source:** [`theory/05-statisticalInference.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- No substantial deviations from normality

- We can assume that the differences  $X \sim N(\mu, \sigma^2)$.

- Effect of captopril in the population is captured by the average blood pressure difference $\mu$.

- The average blood pressure $\mu$ in the population can be estimated using the sample mean $\bar x$=`r round(mean(captopril$deltaSBP),2)`

- The standard deviation $\sigma$ with the sample standard deviation $\text{S}$=`r round(sd(captopril$deltaSBP),2)`.

- Is the effect that we observe in the sample large enough to conclude that there is an effect of the captopril treatment on the blood pressure at population level?

- Our estimates will change from sample to sample!

- How are the estimators $\bar X$ and $S$ distributed?


## Point estimator the sample mean

- Suppose that $X$ is a random sample from the population and assume that $X \sim N(\mu,\sigma^2)$

- Estimate $\mu$ based on sample $X_1,...,X_n$, using the sample mean
  $$\bar X = \frac{X_1+ X_2+ ... + X_n}{n} = \frac{\sum_{i=1}^{n} X_i}{n}$$ of random variables $X_1,X_2, ..., X_n$.

- Sample mean $\bar X$ is a random variable that varies from sample to sample

- Study the theoretical distribution of the sample mean to get insight

    1. in how the sample mean can vary in a new similar study
    2. how far $\bar X$ can be from the population mean $\mu$

---

### Overview

1. The sample mean is unbiased
2. Precision of sample mean
3. Distribution of sample mean

---

### The sample mean is unbiased

- We can generalize our observations based on the sample towards the population if the estimate is good approximation of the population value.

- A representative sample is required to generalize the results from the sample towards the population

- Avoid bias (so that the population mean is not systematically under or overestimated)

- Report how the sample is taken!

- Randomisation!

- Draw the subjects at random from population so every subject has the same probability to end up in the sample.

- Subjects with hypertension are sampled at random from the population


- Simple random sample:  $X_1,...,X_n$ for characteristic $X$

- $X_1,...,X_n$ have same distribution
- They have same mean $\mu$ and variance $\sigma^2$

- $E(X_1)=...=E(X_n)=\mu$ and $\text{Var}(X_1)=...=\text{Var}(X_n)=\sigma^2$

- $\bar X$ is an *unbiased estimator* for $\mu$

<details><summary>Click to see proof</summary><p>
\begin{eqnarray*}
E(\bar X) &=& E \left(\frac{X_1+ X_2+ ... + X_n}{n}\right) \\
&= & \frac{E(X_1)+ E(X_2)+ ... + E(X_n)}{n} \\
&=& \frac{\mu + \mu + ... +\mu}{n} \\
&= & \mu
\end{eqnarray*}
</p></details>

---

### Imprecision/standard error

- Also for representative samples the results are imprecise.
\vspace{10pt}
- Different samples from the same population give different results.

- We illustrated this by using the NHANES

    - We will draw 15 females at random from the NHANES study and we will register their log2 direct cholesterol values
    - We repeat this 50 times to assess the variation from sample to sample
    - We will plot the boxplot for each sample and will indicate the mean

```r
library(NHANES)

fem <- NHANES %>%
  filter(Gender=="female" & !is.na(DirectChol)) %>%
  select("DirectChol")

n<-15 # number of subjects per sample
nSim=50 # number of simulations

femSamp<-matrix(nrow=n,ncol=nSim)
for (j in 1:nSim)
{
  femSamp[,j]<-sample(fem$DirectChol,15)
  if (j<4) {
    p <- femSamp %>%
      log2 %>%
      data.frame %>%
      gather("sample","log2cholesterol") %>%
      ggplot(aes(x=sample,y=log2cholesterol)) +
      geom_boxplot() +
      stat_summary(fun.y=mean, geom="point", shape=19, size=3, color="red", fill="red") +
      geom_hline(yintercept = mean(fem$DirectChol %>% log2)) +
      ylab("cholesterol (log2)")
    print(p)
  }
}

femSamp %>%
  log2 %>%
  data.frame %>%
  gather("sample","log2cholesterol") %>%
  ggplot(aes(x=sample,y=log2cholesterol)) +
  geom_boxplot() +
  stat_summary(fun.y=mean, geom="point", shape=19, size=3, color="red", fill="red") +
  geom_hline(yintercept = mean(fem$DirectChol %>% log2)) +
  ylab("cholesterol (log2)")
```

We observe that the mean nicely fluctuates around the population mean.

Copy the code, increase the sample size to 100 subjects and observe what happens!

---

### How to do this based on a single sample?

- Insight in how close we can expect $\bar X$ to $\mu$?

- How varies $\bar X$ from sample to sample?

- Variability on $\bar X$

- We have to determine this based on a single sample!

- We need to make assumptions

- We assume that the random variables $X_1, X_2, ..., X_n$ originate from $n$ *independent* subjects.

- For the captopril study we had dependent observations.

    - Blood pressure measurements before ($Y_{i,before}$) and  after ($Y_{i,after}$) administering captopril for the same subject $i=1,\ldots,n$.
    - We turned them into n independent measurements by taking the difference $Y_{i,after}-Y_{i,before}$

---

### Variance estimator for $\bar X$

$$\sigma^2_{\bar X}=\frac{\sigma^2}{n}$$

- The standard deviation of $\bar X$ around $\mu$ is $\sqrt{n}$ times smaller that the deviation around the original observations $X$.

- The more observations we have the more precise $\bar X$.


<details><summary>Click to see proof</summary><p>
\begin{eqnarray*}
\text{Var}(\bar X)&=&\text{Var} \left(\frac{X_1+ X_2+ ... + X_n}{n}\right) \\
&= & \frac{\text{Var} (X_1+ X_2+ ... + X_n)}{n^2} \\
&\overset{*}{=} & \frac{\text{Var}(X_1)+ \text{Var}(X_2)+ ... + \text{Var}(X_n)}{n^2} \\
&=& \frac{\sigma^2 + \sigma^2 + ... \sigma^2}{n^2} \\
&= & \frac{\sigma^2}{n}.
\end{eqnarray*}

- (*) this is based on the assumption of independence.
$$\text{Var}[X_1 + X_2] = \text{Var}[X_1] + \text{Var}[X_2] + 2 \text{Covar}[X_1,X_2]$$

    - With $Covar[X_1,X_2]=0$ when $X_1$ and $X_2$ are independent.
</p></details>

**Definition: standard error**

The standard deviation of $\bar{X}$ is $\sigma/\sqrt{n}$ and is also referred to as the **standard error** of the mean.
Generally one refers to the standard deviation of an estimator for a particular parameter $\theta$ with the term **standard error** of the estimator, which is denoted as $SE$.

---

### Captopril example


- $n = 15$ differences in systolic blood pressure

- Suppose that the standard deviation of the blood pressure differences in the population is $\sigma = 9.0$ mmHg

- Then, the standard error (SE) on the average systolic blood pressure differs $\bar X$ becomes:

$$
SE= \frac{9.0}{\sqrt{15}}=2.32\text{mmHg.}
$$

- Generally $\sigma$, and thus the SE on the sample mean are unknown.
- So we also have to estimate the standard deviation of the sample to obtain the standard error
- Estimator: $SE=S/\sqrt{n},$
- with $S^2$ the sample variance of $X_1,...,X_n$  and $S$ the sample standard deviation

- For the captopril example we obtain:

```r
n=length(captopril$deltaSBP)
se=sd(captopril$deltaSBP)/sqrt(n)
se
```

---

### standard deviation vs standard error

#### Illustrate via repeated sampling

- Different sample sizes: 10, 50, 100
- Draw 1000 samples per sample size from the NHANES study, for each sample we calculate
    - The mean
    - The sample standard deviation
    - The standard error
- We make a boxplot of the sample standard deviations and the standard errors for the different sample sizes

- Instead of using a for loop we will use the sapply function which is more efficient. It takes a vector or a list as input and applies a function on each element of the vector or on each list element.

```r
femSamp10<-sapply(1:1000,function(j,x,size) sample(x,size),size=10,x=fem$DirectChol)

femSamp50<-sapply(1:1000,function(j,x,size) sample(x,size),size=50,x=fem$DirectChol)

femSamp100<-sapply(1:1000,function(j,x,size) sample(x,size),size=100,x=fem$DirectChol)

res<-rbind(
femSamp10 %>%
  log2%>%
  as.data.frame %>%
  gather(sample,log2Chol) %>%
  group_by(sample)%>%
  summarize_at("log2Chol",
               list(median=~median(.,na.rm=TRUE),
                    mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n)) ,

femSamp50 %>%
  log2 %>%
  as.data.frame %>%
  gather(sample,log2Chol) %>%
  group_by(sample)%>%
  summarize_at("log2Chol",
               list(median=~median(.,na.rm=TRUE),
                    mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n)),

femSamp100 %>%
  log2 %>%
  as.data.frame %>%
  gather(sample,log2Chol) %>%
  group_by(sample)%>%
  summarize_at("log2Chol",
               list(median=~median(.,na.rm=TRUE),
                    mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))
)
```

##### Means

We first illustrate the impact of sample size on the distribution of the means of the different samples

```r
res %>%
ggplot(aes(x=n%>%as.factor,y=mean)) +
geom_boxplot() +
ylab("Direct cholesterol (log2)") +
xlab("sample size")
```

- Note, that the variation of the sample means indeed reduces as the sample size increases. So the estimation gets more precise with increasing sample size.

---

##### Standard deviation

We now illustrate the impact of sample size on the distribution of the standard deviation of the different samples

```r
res %>%
ggplot(aes(x=n%>%as.factor,y=sd)) +
geom_boxplot() +
ylab("standard deviation") +
xlab("sample size")
```


- The standard deviation remains similar across sample size.
It is centred around the same value: the standard deviation in the population. Indeed increasing the sample size does affect the variability in the population!

- Again we see that the variability of the standard deviation reduces with increasing sample size. So the standard deviation can also be estimated more precise with increasing sample size.

---

##### Standard error on the mean

Finally, we illustrate the impact of sample size on the distribution of the standard deviation on the mean of the different samples

```r
res %>%
ggplot(aes(x=n%>%as.factor,y=se)) +
geom_boxplot() +
ylab("standard error") +
xlab("sample size")
```

- The standard error, the estimator for the precision of the sample mean, however, reduces considerably with increasing sample size again confirming that the estimation of the sample mean gets more precise.

---

### Normally distributed data

- For normally distributed data we have multiple estimators for the population mean $\mu$ e.g mean and median.

- But, $\bar{X}$ is the unbiased estimator of $\mu$ with the smallest standard error

-  $\bar{X}$ deviates less from the mean $\mu$ than the median

- We illustrate this for repeated sampling with sample size 10
```r
res %>%
  filter(n==10) %>%
  select(mean,median) %>%
  gather(type,estimate) %>%
  ggplot(aes(x=type,y=estimate)) +
  geom_boxplot()+
  geom_hline(yintercept=fem$DirectChol%>%log2%>%mean) +
  ggtitle("10 subjects")
```

Next, we compare the distribution of mean and median in repeated samples of sample size 50.

```r
res %>%
  filter(n==50) %>%
  select(mean,median) %>%
  gather(type,estimate) %>%
  ggplot(aes(x=type,y=estimate)) +
  geom_boxplot()+
  geom_hline(yintercept=fem$DirectChol%>%log2%>%mean) +
  ggtitle("50 subjects")
```

### Distribution of sample mean


- How varies $\bar X$ from sample to sample?
- Distribution of $\bar X$?
- If $\bar X$ is normally distributed the standard error has a good interpretation: the s.e. is the standard deviation of the sample mean.
- If the data $X_i$ are normally distributed, the sample mean is also normally distributed.

$$X_i \sim N(\mu,\sigma^2) \rightarrow  \bar X \sim N(\mu,  \sigma^2/n)$$

---

#### NHANES: cholesterol

We illustrate this again with simulation using the NHANES study.
The log2 cholesterol levels were normally distributed.

```r
 fem %>%
  ggplot(aes(x=DirectChol%>%log2))+
  geom_histogram(aes(y=..density.., fill=..count..)) +
  xlab("Direct cholesterol (log2)") +
  stat_function(fun=dnorm,color="red",args=list(mean=mean(fem$DirectChol%>%log2), sd=sd(fem$DirectChol%>%log2))) +
  ggtitle("All females in Nhanes study")

fem %>%
  ggplot(aes(sample=DirectChol%>%log2)) +
  stat_qq() +
  stat_qq_line() +
  ggtitle("All females in Nhanes study")
```

---

##### Evaluate distribution for samples with 5 subjects

```r
femSamp5<-sapply(1:1000,function(j,x,size)
  sample(x,size),size=5,x=fem$DirectChol)

femSamp5[,1] %>%
  log2 %>%
  as.data.frame %>%
  ggplot(aes(x=.))+
  geom_histogram(aes(y=..density.., fill=..count..),bins=10) +
  xlab("Direct cholesterol (log2)") +
  stat_function(fun=dnorm,color="red",args=list(mean=femSamp5[,1]%>%log2%>%mean, sd=femSamp5[,1]%>%log2%>%sd)) +
  ggtitle("5 random females") +
  xlim(fem$DirectChol %>% log2 %>% range)


femSamp5 %>%
  log2 %>%
  colMeans %>%
  as.data.frame %>%
  ggplot(aes(x=.)) +
  geom_histogram(aes(y=..density.., fill=..count..),bins=15) +
  xlab("Mean cholesterol (log2)") +
  stat_function(fun=dnorm,color="red",args=list(mean=femSamp5%>%log2%>% colMeans %>% mean, sd=femSamp5%>%log2%>% colMeans %>% sd)) +
ggtitle("Means on 5 females")

femSamp5 %>%
  log2 %>%
  colMeans %>%
  as.data.frame %>%
  ggplot(aes(sample=.)) +
  stat_qq() +
  stat_qq_line() +
  ggtitle("Means on 5 females")
```

---

##### Explore the distribution of the mean for samples of size 10

Now we explore the results for the sample size of 10.

We first illustrate the plot for the first sample.

```r
femSamp10[,1] %>% log2 %>% as.data.frame %>%
ggplot(aes(x=.))+
  geom_histogram(aes(y=..density.., fill=..count..),bins=10) +
  xlab("Direct cholesterol (log2)") +
  stat_function(fun=dnorm,color="red",args=list(mean=femSamp10[,1]%>%log2%>%mean, sd=femSamp10[,1]%>%log2%>%sd)) +
ggtitle("10 random females") +
xlim(fem$DirectChol %>% log2 %>% range)
```

Next we look at the distribution of the sample mean over 1000 samples of sample size 10.

```r
femSamp10 %>% log2 %>% colMeans %>% as.data.frame %>% ggplot(aes(x=.)) +
  geom_histogram(aes(y=..density.., fill=..count..),bins=15) +
  xlab("Mean cholesterol (log2)") +
  stat_function(fun=dnorm,color="red",args=list(mean=femSamp10%>%log2%>% colMeans %>% mean, sd=femSamp10%>%log2%>% colMeans %>% sd)) +
ggtitle("Means on 10 females")

femSamp10 %>% log2%>% colMeans %>% as.data.frame %>%  ggplot(aes(sample=.)) +
stat_qq() +
stat_qq_line() +
ggtitle("Means on 10 females")
```

**So we confirmed that the mean is approximately normally distributed for studies with 5 and 10 females when the original data are approximately normally distributed.**

---

#### Captopril study

- For Captopril study the systolic blood pressure differences are approximatively normally distributed.

- s.e.= 2.32 mm Hg

- In 95 out of 100 studies with n = 15 subjects we expect the sample mean of the systolic blood pressure differences ($\bar X$) on less then $2 \times 2.32 = 4.64$mm Hg of the real population mean of the blood pressure differences ($\mu$).

---

### Non-normally distributed data

- When individual observations do not have a normal distribution,   $\bar X$ is still \textit{approximately} Normally distributed
when the number observations are large enough.

- How large does the sample needs to be for the Normal approximation to work?

- This depends on the skewness of the distribution!

---

#### NHANES: cholesterol

- When can evaluated this in the NHanes study if we do not log2 transform the data.

```r
fem %>% ggplot(aes(x=DirectChol))+
   geom_histogram(aes(y=..density.., fill=..count..)) +
   xlab("Direct cholesterol") +
   stat_function(fun=dnorm,color="red",args=list(mean=mean(fem$DirectChol), sd=sd(fem$DirectChol))) +
   ggtitle("All females in Nhanes study")

 fem %>% ggplot(aes(sample=DirectChol)) +
 stat_qq() +
 stat_qq_line() +
 ggtitle("All females in Nhanes study")
```

The cholesterol data is clearly non-Normally distributed.

##### Distribution of the sample mean for different sample sizes

```r
femSamp5 %>% colMeans %>% as.data.frame %>% ggplot(aes(x=.)) +
  geom_histogram(aes(y=..density.., fill=..count..),bins=15) +
  xlab("Mean cholesterol") +
  stat_function(fun=dnorm,color="red",args=list(mean=femSamp5%>% colMeans %>% mean, sd=femSamp5%>% colMeans %>% sd)) +
ggtitle("Means on 5 females")

femSamp5 %>% colMeans %>% as.data.frame %>%  ggplot(aes(sample=.)) +
stat_qq() +
stat_qq_line() +
ggtitle("Means on 5 females")


femSamp10 %>% colMeans %>% as.data.frame %>% ggplot(aes(x=.)) +
  geom_histogram(aes(y=..density.., fill=..count..),bins=15) +
  xlab("Mean cholesterol") +
  stat_function(fun=dnorm,color="red",args=list(mean=femSamp10%>% colMeans %>% mean, sd=femSamp10%>% colMeans %>% sd)) +
ggtitle("Means on 10 females")

femSamp10 %>% colMeans %>% as.data.frame %>%  ggplot(aes(sample=.)) +
stat_qq() +
stat_qq_line() +
ggtitle("Means on 10 females")

femSamp50 %>% colMeans %>% as.data.frame %>%  ggplot(aes(sample=.)) +
stat_qq() +
stat_qq_line() +
ggtitle("Means on 50 females")

femSamp100 %>% colMeans %>% as.data.frame %>%  ggplot(aes(sample=.)) +
stat_qq() +
stat_qq_line() +
ggtitle("Means on 100 females")
```

- **We observe that when the data are not normally distributed the distribution of the sample mean is not normally distributed in small samples**

- **For large samples, however, the sample mean of non normal data is still approximately normally distributed.**

---

### Centrale Limit Theorem

Let $X_1, \ldots, X_n$ are sequence of random variables that are drawn independently from the same distribution (population).
As long as the sample size n is sufficiently large, the sample mean $\bar X$ is approximately normally distributed, irrespective of the distribution of the observations $X_i$.

### Overview on the distribution of the mean

![](https://www.nature.com/articles/nmeth.2613.pdf){width=100%}

---

#Interval estimators

- $\bar X$ varies around $\mu$

- Here we will develop an interval around $\bar X$ that will contain the value of $\mu$ with a probability of 95% for a random sample.

- We first assume $\sigma^2$ to be known and we will later relax this assumption.

---

## Normally distributed data with known variance

- $X\sim N(\mu,\sigma^2) \rightarrow \bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right)$

- 95% reference-interval for sample mean

\begin{equation*}
\left[\mu - 1.96 \frac{\sigma}{\sqrt{n}},\mu + 1.96 \frac{\sigma}{\sqrt{n}}%
\right]
\end{equation*}

- The interval contains the sample mean of a random sample with a probability of 95%.

- We can not calculate it because $\mu$ is unknown.

- Estimate $\mu$ by $\bar X$.
\begin{equation*}
\left[\bar X - 1.96 \frac{\sigma}{\sqrt{n}},\bar X + 1.96 \frac{\sigma}{\sqrt{n}}\right]
\end{equation*}


- More useful interpretation:
\vspace{15pt}
- Rewrite $\mu - 1.96 \ \sigma/\sqrt{n} < \bar{X}$ as $\mu < \bar{X} + 1.96 \ \sigma/\sqrt{n}$.

So that we can write
\begin{eqnarray*}
95\% &=& P( \mu - 1.96 \ \sigma/\sqrt{n} < \bar{X} < \mu + 1.96 \ \sigma/\sqrt{n} ) \\
&=&P( \bar{X} - 1.96 \ \sigma/\sqrt{n} < \mu < \bar{X} + 1.96 \ \sigma/\sqrt{n} )
\end{eqnarray*}

---

**Definition of 95% confidence interval on mean**
For a random sample, the interval
\begin{equation}
[\bar{X} - 1.96 \ \sigma/\sqrt{n} , \bar{X} + 1.96 \ \sigma/\sqrt{n} ],
\end{equation}
contains the population mean $\mu$ with a probability of 95%.

---

- The probability that the CI for a random sample contains the population parameter $\mu$, i.e. 95%, is also referred to as the **confidence level**.

- Note, that the lower and upper limit of the interval are also random variables that vary from sample to sample. Different samples indeed result in different confidence intervals because they are based on different observation.

- So they are *stochastic intervals*

- 95% of the samples will produce a 95% confidence interval that will contain the population mean $\mu$. The remaining 5% will produce intervals that do not contain the population mean.

- Based on one interval you cannot conclude that it contains the real population parameter, because its value is unknown.

Generally the standard deviation is unknown and has to be estimated e.g. by $S$

- For large $n$ $[\bar{X} - 1.96 \ s/\sqrt{n} , \bar{X} + 1.96 \ s/\sqrt{n} ]$ will contain the population mean with a probability of approximately 95%.

---

### NHANES log2 cholesterol example

#### One sample
```r
samp50<-sample(fem$DirectChol,50)

ll<-mean(samp50 %>% log2) - 1.96*sd(samp50 %>% log2)/sqrt(50)
ul<-mean(samp50 %>% log2) + 1.96*sd(samp50 %>% log2)/sqrt(50)
popMean<-mean(fem$DirectChol%>%log2)

c(ll=ll,ul=ul,popMean=popMean)
```

#### Repeated sampling
```r
res$ll<-res$mean-1.96*res$se
res$ul<-res$mean+1.96*res$se
mu<-fem$DirectChol%>%log2%>%mean
res$inside<-res$ll<=mu & mu<=res$ul
res$n <- as.factor(res$n)
res %>%
  group_by(n) %>%
  summarize(coverage=mean(inside)) %>%
  spread(n,coverage)
```

- Note, that the coverage in the samples with 10 observations is too low because we do not account for the uncertainty in the estimation of the standard deviation.

- If we look to the first 20 intervals, `r sum((!res[res$n==10,"inside"])[1:20])`  out of 20 do not contain the population mean.

```r
res %>%
  filter(n==10) %>%
  slice(1:20) %>%
  ggplot(aes(x=sample,y=mean,color=inside)) +
  geom_point() +
  geom_errorbar(aes(ymin=mean-1.96*se,ymax=mean+1.96*se))+
  geom_hline(yintercept = fem$DirectChol%>% log2 %>% mean) +
  ggtitle("20 CI for N=10") +
  ylim(range(fem$DirectChol %>% log2))
```

---

- For large sample sizes (100) the coverage is fine because we can estimate the standard deviation with a relative high precision.

```r
res %>%
  filter(n==50) %>%
  slice(1:20) %>%
  ggplot(aes(x=sample,y=mean,color=inside)) +
  geom_point() +
  geom_errorbar(aes(ymin=mean-1.96*se,ymax=mean+1.96*se))+
  geom_hline(yintercept = fem$DirectChol%>% log2 %>% mean) +
  ggtitle("20 CI for N=50") +
  ylim(range(fem$DirectChol %>% log2))

res %>%
  filter(n==100) %>%
  slice(1:20) %>%
  ggplot(aes(x=sample,y=mean,color=inside)) +
  geom_point() +
  geom_errorbar(aes(ymin=mean-1.96*se,ymax=mean+1.96*se))+
  geom_hline(yintercept = fem$DirectChol%>% log2 %>% mean) +
  ggtitle("20 CI for N=100") +
  ylim(range(fem$DirectChol %>% log2))
```

- What have you observed for the interval width?

---

### Other confidence levels

- We can replace the $z_{2.5\%}=1.96$ by another quantile of the normal distribution $z_{\alpha/2} to obtain an interval with another confidence level $1-\alpha$.

- Confidence intervals are not only used for the mean but also for other population parameters.

---

## Unknown variance

In real examples $\sigma$ is unknown and estimated based on the sample using the sample standard deviation $S$.

- The previous intervals were a bit to small because they did not account for the uncertainty on the estimation of $S$.

- When $n$ is large, $S$ is close to $\sigma$.

- Hence, ${(\bar{X} - \mu)}/{(S/\sqrt{n}) }$ is approximately standard normal and
\begin{equation*}
\left[\bar{X} - z_{\alpha/2} \ \frac{S}{\sqrt{n}} , \bar{X} + z_{\alpha/2} \
\frac{S}{\sqrt{n}}\right]
\end{equation*}
is an approximate $(1- \alpha)100\%$ CI for $\mu$.

- For small samples this no longer holds (e.g. n=10)

The estimation of $S$ introduces additional uncertainty in the standardized value ${(\bar{X} - \mu)}/{(S/\sqrt{n})}$. Its distribution

- is still symmetric but has heavier tails that the normal distribution.

- it depends on $n$ how much heavier the tails are

- is a (Student) $t$-distribution with $n-1$ *degrees of freedom*.

---

### T-distribution

More formally: Let $X_1, X_2, ..., X_n$ be an independent random sample from a Normal distribution $N(\mu, \sigma^2)$, then $(\bar{X} - \mu)/(S/\sqrt{n})$ follows a $t$-distribution with $n-1$ degrees of freedom.

The density of a t-distribution can be calculated in R using the function `dt`. It has arguments `x` for the quantile and `df` for the degrees of freedom.

```r
grid <- seq(-5,5,.1)
densDist<-cbind(grid,dnorm(grid), sapply(c(2,5,10),dt,x=grid))
colnames(densDist)<-c("x","normal",paste0("t",c(2,5,10)))

densDist %>% as.data.frame %>% gather(dist,dens,-x) %>%
ggplot(aes(x=x,y=dens,color=dist)) +
geom_line() +
ylab("Density")
```


t-distributions have heavier tails then the normal distribution $\rightarrow$ larger quantiles so broader intervals for the same confidence level.

- This captures the additional uncertainty for estimating $S$.

- If $n \rightarrow \infty$ then $t(df) \rightarrow N(0,1)$


- quantiles of the $t$-distribution can be calculated in R using `qt`. e.g. 95%, 97.5%, 99.5% quantile for a t-distribution with 14 degrees of freedom:
```r
qt(.975,df=14)
qt(c(.95,.975,.995),df=14)
```

- These quantiles can be used to calculate 90%, 95% and 99% CI.

- 97.5% quantile`r round(qt(.975,df=14),2)` of a t-distribution with $n-1=14$ degrees of freedom is indeed larger than that of a standard Normal distribution `r round(qnorm(.975),2)`.

---

### Confidence interval based on the t-distribution

The $100\% (1-\alpha)$ CI for the mean $\mu$ of a
Normal distributed random variable $X$ with unknown variance is

\begin{equation*}
\left[\bar{X} - t_{n-1, \alpha/2} \frac{s}{\sqrt{n}} , \bar{X} + t_{n-1,
\alpha/2} \frac{s}{\sqrt{n}}\right]
\end{equation*}

- We simply replace the $(1-\alpha/2)100\%$ quantile of the Normal distribution by that of the t-distribution with $n-1$ degrees of freedom.

#### Captopril example


95% CI for the average blood pressure change becomes

```r
mean(captopril$deltaSBP) -  qt(.975,df=14)*sd(captopril$deltaSBP)/sqrt(15)
mean(captopril$deltaSBP) + qt(.975,df=14)*sd(captopril$deltaSBP)/sqrt(15)
```

The 99% CI is given by
```r
mean(captopril$deltaSBP) -  qt(.995,df=14)*sd(captopril$deltaSBP)/sqrt(15)
mean(captopril$deltaSBP) + qt(.995,df=14)*sd(captopril$deltaSBP)/sqrt(15)
```

Note, that zero is outside the interval and that the entire interval is negative indicating that there is on average a large effect by administrating captopril on the blood pressure of patients with hypertension.

---

### Interpretation of the confidence interval

- We will revisit the results for sampling log2 cholesterol levels from the large NHANES study. We first focus on the repeated experiments with sample size 10.

```r
res$n<-as.character(res$n) %>% as.double(res$n)
res$ll<-res$mean-qt(0.975,df=res$n-1)*res$se
res$ul<-res$mean+qt(0.975,df=res$n-1)*res$se
mu<-fem$DirectChol%>%log2%>%mean
res$inside<-res$ll<=mu & mu<=res$ul
res$n <- as.factor(res$n)
res %>% group_by(n) %>% summarize(coverage=mean(inside)) %>% spread(n,coverage)
```

We observe that all the coverages of the intervals are now controlled at their nominal 95% confidence level.

```r
res %>%
  filter(n==10) %>%
  slice(1:20) %>%
  ggplot(aes(x=sample,y=mean,color=inside)) +
  geom_point() +
  geom_errorbar(aes(ymin=mean-qt(0.975,df=9)*se,ymax=mean+qt(0.975,df=9)*se))+
  geom_hline(yintercept = fem$DirectChol%>% log2 %>% mean) +
  ggtitle("20 CI for N=10") +
  ylim(range(fem$DirectChol %>% log2))
```

![](https://www.nature.com/articles/nmeth.2659.pdf){width=100%}

---

## Reporting?

- Always report the uncertainty on the results!

- Conclusions based on a point estimate can be very misleading.

- Upon a statistical analysis we therefore always report confidence intervals

- They are small enough to be informative but almost never misleading

- They form a good trade-off between statistical significance and biological relevance.

- We conclude that the population parameter lays in the interval and know that this statement holds with a probability of 95% for random samples.

### Captopril example

We conclude that the blood pressure decreases on average with
`r abs(round(mean(captopril$deltaSBP),1))`mmHg upon administering captopril (95% CI [`r paste(round(mean(captopril$deltaSBP)+qt(c(0.025,.975),n-1)*sd(captopril$deltaSBP)/sqrt(n),1),collapse=",")`]mmHg).

Based on these results it is obvious that the treatment causes a strong blood pressure drop for patients with hypertension.

---

[← Data exploration and Descriptive Statistics](03-data-exploration-and-descriptive-statistics.md) · [Up: contents](index.md) · [Hypothesis tests →](05-hypothesis-tests.md)
