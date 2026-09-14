---
title: Sample to sample variability
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd
source_file: sources/gtpb-psls20/theory/01-intro.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Sample to sample variability

**Source:** [`theory/01-intro.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

National Health NHanes study

  - Since 1960 individuals of all ages are interviewed in their homes every year
  - The health examination component of the survey is conducted in a mobile examination centre (MEC).
  - We will use this large study to select random subjects from the American population.
  - This will help us to understand how the results of an analysis and the conclusions vary from sample to sample.

---

```r
library(NHANES)
head(NHANES)
glimpse(NHANES)
```

---

## Data exploration


Suppose that we are interested in assessing the difference in direct cholesterol levels between males and females older than 25 years.

1. We pipe the dataset to the function `filter` to filter the data according to age.
2. We plot the direct cholesterol levels.
    - We select the data with the command `ggplot(aes(x=DirectChol))`
    - We add a histogram with the command `geom_histogram()`
    - We make to vertical panels using the command `facet_grid(Gender~.)`
    - We customize the label of the x-axis with the `xlab` command.

```r
NHANES%>%filter(Age>25)%>%
  ggplot(aes(x=DirectChol))+
  geom_histogram() +
  facet_grid(Gender~.) +
  xlab("Direct cholesterol (mg/dl)")
```

---

- Cholesterol levels and concentration measurements are often skewed.
- Concentrations cannot be lower than 0.
- They are often log transformed.

```r
NHANES%>%
  filter(Age>25)%>%
  ggplot(aes(x=DirectChol%>%log2))+
  geom_histogram() +
  facet_grid(Gender~.) +
  xlab("Direct cholesterol (log2)")
```

We see that the data are more or less bell shaped upon log transformation.

---

We will now create a subset of the data that we will use to sample from in the next sections.

  1. We filter on age and remove subjects with missing values (NA).
  2. We only select the variables Gender and DirectChol from the dataset to avoid unnecessary variables.
  3. With the mutate function we can add a new variable logChol with log transformed direct cholesterol levels.

```r
nhanesSub<- NHANES%>%
  filter(Age>25&!is.na(DirectChol)) %>%
  select(c("Gender","DirectChol")) %>%
  mutate(cholLog=log2(DirectChol))
```

---

We will calculate the summary statistics for the cholLog variable for males and females in the large dataset.
So we group by Gender

```r
cholLogSum<- nhanesSub %>%
  group_by(Gender) %>%
   summarize_at("cholLog",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))

cholLogSum
```

---

## Experiment

- Suppose that we have no access to cholesterol levels of the American population,
- we will have to setup an experiment.
- Suppose we have a budget for assessing 10 females and 10 males,
- we will subset 10 females and 10 males at random from the American population and measure their direct cholesterol levels.

```r
fem<-nhanesSub%>%filter(Gender=="female")%>%sample_n(size=10)
mal<-nhanesSub%>%filter(Gender=="male")%>%sample_n(size=10)

samp<-rbind(fem,mal)
samp
```

---

We will now plot the data with a histogram and boxplots

```r
samp %>%
  ggplot(aes(x=cholLog))+
  geom_histogram(binwidth = .1) +
  facet_grid(Gender~.) +
  xlab("Direct cholesterol (log2)")

samp%>%
  ggplot(aes(x=Gender,y=cholLog)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")
```

---

We summarize the data
```r
samp %>%
  group_by(Gender) %>%
   summarize_at("cholLog",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))
```

Note that the sample mean is different from that of the large experiment ("population") we sampled from.

We test for the difference between Males and females

```r
t.test(cholLog~Gender,samp,var.equal=TRUE)
```

---

## Repeat the experiment

If we do the experiment again we select other people and we obtain different results.


```r
fem<-nhanesSub%>%filter(Gender=="female")%>%sample_n(size=10)
mal<-nhanesSub%>%filter(Gender=="male")%>%sample_n(size=10)

samp2<-rbind(fem,mal)
samp2%>%
  ggplot(aes(x=DirectChol%>%log))+
  geom_histogram(binwidth = .1) +
  facet_grid(Gender~.) +
  xlab("Direct cholesterol (log)")

samp2%>%
  ggplot(aes(x=Gender,y=cholLog)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")

samp2 %>%
  group_by(Gender) %>%
   summarize_at("cholLog",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))

t.test(cholLog~Gender,samp2,var.equal=TRUE)
```

---

## And again

```r
set.seed(12857)
fem<-nhanesSub%>%filter(Gender=="female")%>%sample_n(size=10)
mal<-nhanesSub%>%filter(Gender=="male")%>%sample_n(size=10)

samp3<-rbind(fem,mal)
samp3%>%
  ggplot(aes(x=DirectChol%>%log))+
  geom_histogram(binwidth = .1) +
  facet_grid(Gender~.) +
  xlab("Direct cholesterol (log)")

samp3%>%
  ggplot(aes(x=Gender,y=cholLog)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")


samp3 %>%
  group_by(Gender) %>%
   summarize_at("cholLog",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))

t.test(cholLog~Gender,samp3,var.equal=TRUE)
```

---

## Summary

- Because we sampled other subjects in each sample, we obtain different cholesterol levels.
- However, not only the cholesterol levels differ from sample to sample but also the summary statistics: means, standard deviations and standard errors.
- Note, that in the last sample the log cholesterol levels are on average lower for females than for males; based on this sample we even would wrongly conclude that the cholesterol levels for females are on average larger than those of males.

- This implies that our conclusions are also subjected to uncertainty and might change from sample to sample.

- Samples as the one where the effect swaps and is statistically significant, however, are very rare.
- This is illustrated with the code below, where we will draw 20000 repeated samples with sample size 10 for females and males from the NHanes study.

```r
nsim<-20000
nSamp<-10
res<-matrix(0,nrow=nsim,ncol=2)
fem<-nhanesSub%>%filter(Gender=="female")
mal<-nhanesSub%>%filter(Gender=="male")

for (i in 1:nsim)
{
 femSamp<-sample(fem$cholLog,nSamp)
 malSamp<-sample(mal$cholLog,nSamp)

meanFem<-mean(femSamp)
 meanMal<-mean(malSamp)
 delta<-meanFem-meanMal
 sdFem<-sd(femSamp)
 sdMal<-sd(malSamp)
 seFem<-sdFem/sqrt(nSamp)
 seFem<-sdFem/sqrt(nSamp)
 sdPool<-sqrt((sdFem^2*(nSamp-1) + sdMal^2*(nSamp-1))/(2*nSamp-2))
tvalue<-(delta)/(sdPool*sqrt(1/nSamp+1/nSamp))
pvalue<-pt(abs(tvalue),lower.tail = FALSE,df=2*nSamp-2)*2
 res[i,]<-c(delta,pvalue)
}
sum(res[,2]<0.05&res[,1]>0)
sum(res[,2]>0.05)
sum(res[,2]<0.05&res[,1]<0)

res<-res %>% as.data.frame
names(res) <- c("delta","pvalue")
res %>%
  ggplot(aes(x=delta,y=-log10(pvalue),color=pvalue<0.05)) +
  geom_point() +
  xlab("Average cholesterol difference") +
  ylab("- log10(pvalue)") +
  scale_color_manual(values=c("black","red"))

res %>%
  ggplot(aes(y=delta)) +
  geom_boxplot() +
  geom_point(aes(x=0,y=c(mean(fem$cholLog)-mean(mal$cholLog)),color="pop. diff")) +
  xlab("")
```

Only in `r sum(res[,2]<0.05&res[,1]<0)` out of 20000 samples we conclude that the mean cholesterol level of males is significantly lower than for females. For the remaining samples the cholesterol levels for males were on average significantly lower than for females (`r sum(res[,2]<0.05&res[,1]>0)` samples) or the average difference in cholesterol levels were not statistically significant (`r sum(res[,2]>0.05)` samples). The latter is because the power is rather low to detect the difference with 10 samples in each group.

---

## Assignment

1. Copy the code chunk with the simulation study
2. Add it here below
3. Modify the sample size to 50.
4. What do you observe?

---

---

[← Smelly armpit example](01-smelly-armpit-example.md) · [Up: contents](index.md) · [Salk Study →](03-salk-study.md)
