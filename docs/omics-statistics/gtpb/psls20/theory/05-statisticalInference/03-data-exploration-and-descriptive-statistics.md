---
title: Data exploration and Descriptive Statistics
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference.Rmd
source_file: sources/gtpb-psls20/theory/05-statisticalInference.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data exploration and Descriptive Statistics

**Source:** [`theory/05-statisticalInference.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
captopril <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/captopril.txt")
head(captopril)
summary(captopril)
```

```r
captoprilTidy <- captopril %>% gather(type,bp,-id)
captoprilTidy %>%
  group_by(type) %>%
  summarize_at("bp",list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))

captoprilTidy %>%
  group_by(type) %>%
  summarize_at("bp",list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n)) %>%
  ggplot(aes(x=type,y=mean)) +
  geom_bar(stat="identity") +
  geom_errorbar(aes(ymin=mean-se, ymax=mean+se),width=.2) +
  ylim(0,210) +
  ylab("blood pressure (mmHg)")
```

- This figure is not informative! It does not show the raw data.

```r
captoprilTidy %>%
  ggplot(aes(x=type,y=bp)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter") +
  ylim(0,210)
```

We see that a lot of the space that was taken by the barplot does not contain data!

```r
captoprilTidy %>%
  ggplot(aes(x=type,y=bp)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")
```

- This plot would have been informative if the data was gathered on different individuals.

- However, the blood pressures are measured op the same subject!

- We will make a plot by filtering the systolic blood pressures

```r
captoprilTidy %>%
  filter(type%in%c("SBPa","SBPb")) %>%
  mutate(type=factor(type,levels=c("SBPb","SBPa"))) %>%
  ggplot(aes(x=type,y=bp)) +
  geom_line(aes(group = id)) +
  geom_point()
```

- We have paired data. So we might estimate the effect of the treatment directly by comparing the blood pressure after treatment to the blood pressure before the treatment.

```r
captopril$deltaSBP<-captopril$SBPa-captopril$SBPb
captopril%>%
  ggplot(aes(x="Systolic blood pressure",y=deltaSBP)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")+
  ylab("Difference (mm mercury)") +
  xlab("")
```

```r
captopril %>%
  summarize_at("deltaSBP",list(mean=~mean(.,na.rm=TRUE),
              sd=~sd(.,na.rm=TRUE),
              n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))
```


- Pre-test/post-test design: Effect of captopril in sample using  $X=\Delta_\text{after-before}$!

- How will we model $X=\Delta_\text{after-na}$ and estimate the effect of captopril?

```r
captopril%>%
  ggplot(aes(sample=deltaSBP)) +
  stat_qq() +
  stat_qq_line()
```

The systolic blood pressure differences are approximately normally distributed.

---

---

[← Experimental Design](02-experimental-design.md) · [Up: contents](index.md) · [Estimation →](04-estimation.md)
