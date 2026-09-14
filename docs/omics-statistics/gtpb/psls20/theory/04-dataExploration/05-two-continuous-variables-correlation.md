---
title: 'Two continuous variables: Correlation'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd
source_file: sources/gtpb-psls20/theory/04-dataExploration.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Two continuous variables: Correlation

**Source:** [`theory/04-dataExploration.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- NHANES study
- Height and Weight Example for females

```r
NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(x=Height,y=Weight)) +
  geom_point()
```

We observe an association between Weight and Height, but we also observe that the Weights tend to be right-skewed.

Lets look at the univariate distributions first.

```r
NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(x=Height)) +
  geom_histogram(aes(y=..density.., fill=..count..)) +
   xlab("Height") +
  ggtitle("All females in study") +
  geom_density(aes(y=..density..))

NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(sample=Height)) +
  geom_qq() +
  geom_qq_line()
```


```r
NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(x=Weight)) +
  geom_histogram(aes(y=..density.., fill=..count..)) +
   xlab("Weight") +
  ggtitle("All females in study") +
  geom_density(aes(y=..density..))

NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(sample=Weight)) +
  geom_qq() +
  geom_qq_line()
```

The weights are indeed skewed!

Upon log transformaton the Weights are less skewed, but still not Normally distributed.

```r
NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(x=Weight%>%log2)) +
  geom_histogram(aes(y=..density.., fill=..count..)) +
   xlab("Weight (log2)") +
  ggtitle("All females in study") +
  geom_density(aes(y=..density..))

NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(sample=Weight%>%log2)) +
  geom_qq() +
  geom_qq_line()
```

Skewness is still there but is reduced already.

```r
NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(x=Height,y=Weight %>% log2)) +
  ylab("Weight (log2)") +
  geom_point()
```

---

## Covariance and Correlation

- Let X and Y be to continuous random variables, and for each subject i we observe $(X_i,Y_i)$.
- Covariance: how deviate X_i and Y_i around their means?

$$\mbox{Covar}(X,Y)=E[(X-E[X])(Y-E[Y])]$$

- Correlation: standardise the covariance according to the variability in each variable:

$$\mbox{Cor}(X,Y)=\frac{E[(X-E[X])(Y-E[Y])]}{\sqrt{E[(X-E[X])^2}\sqrt{E[(Y-E[Y])^2}}$$


## Pearson Correlation

- Association between two continuous covariate:

$$\mbox{Cor}(X,Y)=\frac{\sum_{i=1}^{n}(X_{i}-\bar{X})(Y_{i}-\bar{Y})}{(n-1)s_{X}s_{Y}}
$$

- Positive correlation: $x \ \nearrow \ \Rightarrow \ y \ \nearrow$

- Negative correlation: $x \ \nearrow \ \Rightarrow \ y \ \searrow$

- Correlation always between -1 en 1

```r
means<-NHANES%>% filter(Age>25 & Gender=="female") %>% select(Weight,Height) %>% mutate(log2Weight=Weight%>%log2) %>% apply(.,2,mean,na.rm=TRUE)
ranges<-NHANES%>% filter(Age>25 & Gender=="female") %>% select(Weight,Height) %>% mutate(log2Weight=Weight%>%log2) %>% apply(.,2,range,na.rm=TRUE)

NHANES%>% filter(Age>25 & Gender=="female") %>%
  ggplot(aes(x=Height,y=Weight %>% log2)) +
  ylab("Weight (log2)") +
  geom_point() +
  geom_hline(yintercept=means["log2Weight"],color="red") +
  geom_vline(xintercept=means["Height"],color="red") +
  annotate(geom="text",
           x=c(ranges[1,"Height"],ranges[1,"Height"],ranges[2,"Height"],ranges[2,"Height"]),
           y=c(ranges[1,"log2Weight"],ranges[2,"log2Weight"],ranges[1,"log2Weight"],ranges[2,"log2Weight"]),
           label=c("+","-","-","+"),color="red",size=10)
```

```r
NHANES%>%
  filter(Age>25 & Gender=="female") %>%
  ggplot(aes(x=Height,y=Weight)) +
  ylab("Weight (log2)") +
  geom_point() +
  geom_hline(yintercept=means["Weight"],color="red") +
  geom_vline(xintercept=means["Height"],color="red") +
  annotate(geom="text",
           x=c(ranges[1,"Height"],ranges[1,"Height"],ranges[2,"Height"],ranges[2,"Height"]),
           y=c(ranges[1,"Weight"],ranges[2,"Weight"],ranges[1,"Weight"],ranges[2,"Weight"]),
           label=c("+","-","-","+"),color="red",size=10)
```


```r
NHANES%>%
  filter(Age>25 & Gender=="female") %>%
  select(Weight,Height) %>%
  mutate(log2Weight=Weight%>%log2) %>%
  na.exclude %>%
  cor
```

- Note, that the correlation is lower when the data are not transformed.
- The Pearson correlation is sensitive to outliers!
- Do not use Pearson correlation for skewed distributions or for data with outliers.

### Impact of outliers

Illustration with simulated data that has one outlier.

```r
set.seed(100)
x <- rnorm(20)
simData <- data.frame(x=x,y=x*2 + rnorm(length(x)))
simData %>% ggplot(aes(x=x,y=y)) +
  geom_point() +
  ggtitle(paste("cor =",cor(simData[,1],simData[,2]) %>% round(.,2)))

outlier<- rbind(simData,c(2,-4))
outlier %>% ggplot(aes(x=x,y=y)) +
  geom_point() +
  ggtitle(paste("cor =",cor(outlier[,1],outlier[,2]) %>% round(.,2)))
```

### Only linear association

Note, that the Pearson correlation only captures linear association!

```r
x <- rnorm(100)
quadratic <- data.frame(x=x,y=x^2 + rnorm(length(x)))
quadratic %>% ggplot(aes(x=x,y=y)) +
  geom_point() +
  ggtitle(paste("cor =",cor(quadratic[,1],quadratic[,2]) %>% round(.,2))) +
  geom_hline(yintercept = mean(quadratic[,2]),col="red") +
    geom_vline(xintercept = mean(quadratic[,1]),col="red")
```


## Different magnitudes of correlation

```r
set.seed(100)
x <- rnorm(100)
simData2<-cbind(x,1.5*x,sapply(1:7,function(sd,x) 1.5*x+rnorm(length(x),sd=sd),x=x),rnorm(length(x),sd=7))

colnames(simData2)[-1]<-paste("cor",round(cor(simData2)[1,-1],2),sep="=")

simData2 %>%
  as.data.frame %>%
  gather(cor,y,-x) %>%
  ggplot(aes(x=x,y=y)) +
  geom_point() +
  facet_wrap(~cor)

simData3 <- simData2
simData3[,-1]<--simData2[,-1]
colnames(simData3)[-1]<-paste("cor",round(cor(simData3)[1,-1],2),sep="=")

simData3 %>%
  as.data.frame %>%
  gather(cor,y,-x) %>%
  ggplot(aes(x=x,y=y)) +
  geom_point() +
  facet_wrap(~cor)
```

---

## Spearman correlation

The Spearman correlation is the Pearson correlation after transforming the data to ranks.

- Pearson correlation
```r
cor(outlier)
```

- Spearman correlation
```r
cor(outlier,method="spearman")
```

- Spearman correlation is less sensitive to outliers.

- Pearson correlation on ranks
```r
rankData<-apply(outlier,2,rank)
cor(rankData)
```

- NHANES example

```r
NHANES%>%
  filter(Age>25 & Gender=="female") %>%
  select(Weight,Height) %>%
  mutate(log2Weight=Weight%>%log2) %>%
  na.exclude %>%
  cor(method="spearman")
```


---

---

[← Normale approximation](04-normale-approximation.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) →](06-home-https-gtpb-github-io-psls20.md)
