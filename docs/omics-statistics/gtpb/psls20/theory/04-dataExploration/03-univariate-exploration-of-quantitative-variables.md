---
title: Univariate exploration of quantitative variables
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd
source_file: sources/gtpb-psls20/theory/04-dataExploration.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Univariate exploration of quantitative variables

**Source:** [`theory/04-dataExploration.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

## Histogram

```r
library(NHANES)
```

```r
NHANES %>% filter(Gender=="female") %>%
ggplot(aes(x=DirectChol)) +
geom_histogram(aes(y=..density.., fill=..count..),bins=30) +
geom_density(aes(y=..density..))
```


1. Select females and pipe results to ggplot.
```
NHANES %>% filter(Gender=="female")
```

2. Select data to plot.

```
ggplot(aes(x=DirectChol)) +
```

3. Equal bins for interpretation, the number of bins can be selected with the bins argument to the geom_hist.

4. *Relative* frequenties to enable visual comparison between histograms.

```
geom_histogram(aes(y=..density.., fill=..count..)) +
```

5. If we have enough observations we can use a kernel density estimator of f(x).

```
geom_density(aes(y=..density..))
```

---

## Boxplot

- A quantile, $x_{a\%}$, is the value of the random variable that correspond to a certain probability $F(x_{a\%})=P[X\leq x_{a\%}=a\%]$.

```r
fem <- NHANES %>% filter(Gender=="female" & !is.na(DirectChol)) %>% select(DirectChol)
boxplot(fem$DirectChol, ylab="Direct Cholesterol",cex.lab=1.5,cex.axis=1.5,cex.main=1.5)
rangeCl<-quantile(fem$DirectChol,c(.25,.75))+c(-1,1)*diff(quantile(fem$DirectChol,c(.25,.75)))*1.5
boxYs<-c(range(fem$DirectChol[fem$DirectChol<=rangeCl[2]&fem$DirectChol>=rangeCl[1]]),quantile(fem$DirectChol,c(.25,.5,.75)),rangeCl[2]+(max(fem$DirectChol)-rangeCl[2])/2)
text(1.3,boxYs,labels=c("wisker","wisker","x25","mediaan","x75","outliers"),pos=4,cex=1.3)
lines(c(1.1,1.3,1.3,1.1),c(rangeCl[2],rangeCl[2]+(max(fem$DirectChol)-rangeCl[2])/2,rangeCl[2]+(max(fem$DirectChol)-rangeCl[2])/2,max(fem$DirectChol)),lty=2)
```

With ggplot we always have to define an x variable if we make a boxplot. If we use a string then all data is considered to originate from one category and one boxplot is constructed.

```r
NHANES %>%
  filter(Gender=="female") %>%
  ggplot(aes(x="",y=DirectChol)) +
  geom_boxplot()
```

So we can add a boxplot to a ggplot figure by using the `geom_boxplot()` function.

If the dataset is small to moderate in size we can also add the raw data to the plot with the `geom_point()` function and the `position="jitter"` argument. Note, that we then also set the `outlier.shape` argument in the `geom_boxplot` function on NA so that the outliers are not plotted twice.

Here, we will plot again the relative abundances of **Staphylococcus** from the armpit transplant experiment.

```r
ap<-read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/armpit.csv")
ap

ap %>%
  ggplot(aes(x=trt,y=rel)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")
```

When we specify a factor variable for x, we get a boxplot for each treatment group.

---

## Descriptive statistics

### Central location: Mean or Median?

#### Mean
- In a period of 30 years, males hope to have on average 64.3 partners and females 2.8  \tiny{(Miller and Fishkin, 1997)}.\Normalsize

---

#### Median

- The median of the number of partners males and females want to have is both 1 \tiny{(Miller and Fishkin, 1997)}\Normalsize

---

#### What happens?

![](https://raw.githubusercontent.com/GTPB/PSLS20/gh-pages/assets/figs/partners.png){width=75%}

- Mean is very sensitive towards outliers!

---

### Geometric mean

$$\sqrt[n]{\prod\limits_{i=1}^n x_i} = \exp\left\{\frac{1}{n} \sum_{i=1}^n \log(x_i)\right\}$$

- Geometric mean is closer to the median then the mean

- log-transformation removes skewness

- Often a more useful measure for the central location than median:

1. Uses all observations: is more precise
2. It is the ordinary mean on log-transformed data $\rightarrow$ classical statistical methods can be directly applied, e.g. hypothesis tests and confidence intervals (see chapter 5)
3. Useful for many biological characteristics e.g. concentrations that cannot be negative.
4. Differences on a log scale have the interpretation of a log fold change:

$$\log (B) - \log(A)= \log(\frac{B}{A})=\log(FC_\text{B vs A})$$

In Genomics often the $log_2$ transformation is used. A difference of 1 corresponds to a $FC=2$.

```r
logSummary <-
NHANES %>% filter(Gender=="female") %>% summarize(logMean=mean(DirectChol %>% log2,na.rm=TRUE),sd=sd(DirectChol %>% log2,na.rm=TRUE),mean=mean(DirectChol,na.rm=TRUE),median=median(DirectChol,na.rm=TRUE)) %>% mutate(geoMean=2^logMean)

NHANES %>% filter(Gender=="female") %>%
ggplot(aes(x=DirectChol %>% log2)) +
geom_histogram(aes(y=..density.., fill=..count..),bins=30) +
geom_density(aes(y=..density..)) +
  stat_function(fun=dnorm,color="red",args=list(mean=logSummary$logMean, sd=logSummary$sd))

logSummary
```

- Indeed the mean is pulled to larger values by the skewed data.
- The geometric mean is closer to the median.
- The cholesterol data are much more symmetric upon log transformation and the approximation by a Normal distribution is good.


## Descriptive Statistics for Variability

The variability around the central value is crucial:

1. Biologists are often interested in how animals or plants are spread in the study region.
2. Compare groups: the group effect is more clear when the response has less variability. Quantifying variability is crucial to distinguish between systematic and random patterns.

- The response varies between and within individuals and is the reason why we need statistics.

- Crucial to describe both the central location and the variability.
- Which part of the variability can we explain (e.g. with characteristics treatment, age, etc,) and which part is unexplained?
### Sample variance and sample standard deviation

- Sample variance: $$
s_X^2= \sum\limits_{i=1}^n \frac{(X-\bar X)^2}{n-1}
$$
- Interpretation is often difficult because it is in another unit than the measurements.

- *Standard deviation*: $$
s_X= \sqrt{s_x^2}
$$

- Very useful for Normal distributed observations:

    - 68% of the observations falls in the interval  $\bar{x} - s_x$ en $\bar{x} + s_x$
    - 95% of the observations falls in the interval $\bar{x} - 2 s_x$ en $\bar{x} + 2 s_x$.

- These intervals are referred to as 68% en 95% *reference-intervals*.

- If the data are not Normally distributed, reference intervals are not valid.

---

### Interquartile range

For skewed data the standard deviation is not useful
- It is very sensitive to outliers
- *Inter Quartile Range*: Distance between first and third quartile
- Width of the boxplot!

```r
NHANES %>% filter(Gender=="female") %>% summarize(IQR=IQR(DirectChol,na.rm=TRUE))
```


```r
NHANES %>% filter(Gender=="female") %>%
  ggplot(aes(x="",y=DirectChol)) +
  geom_boxplot()
```

---

---

[← Why data exploration and descriptive statistics?](02-why-data-exploration-and-descriptive-statistics.md) · [Up: contents](index.md) · [Normale approximation →](04-normale-approximation.md)
