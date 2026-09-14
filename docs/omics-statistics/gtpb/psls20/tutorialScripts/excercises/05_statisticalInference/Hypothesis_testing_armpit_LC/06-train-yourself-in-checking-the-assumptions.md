---
title: Train yourself in checking the assumptions
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Train yourself in checking the assumptions

**Source:** [`tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

In order for the learners to get more proficient in evaluating the assumptions we will simulate 9 dataset with sample sizes similar to our data for which the assumptions of normality and equal variance do hold. For the QQ-plots we will only plot the one from one of the groups.

## Simulate data

We simulate 9 datasets with the same sample sizes, means and pooled variance as in the sample.

```r
nSamp <- 9
## descriptive statistics
apRelSum<-ap%>%
  group_by(trt)%>%
  summarize_at("rel",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))

sigma <- sqrt(sum(apRelSum$sd^2*(apRelSum$n-1))/(sum(apRelSum$n)-2))

normSim <- matrix(rnorm(sum(apRelSum$n)*nSamp,
              mean=c(rep(apRelSum$mean[1],apRelSum$n[1]),
                     rep(apRelSum$mean[2],apRelSum$n[2])),
                     sd=sigma),nrow=sum(apRelSum$n)) %>%
  as.data.frame %>%
  mutate(trt=ap$trt)
```

## Comparisons of variances

```r
normSim %>% gather(samp,data,-trt) %>%
  ggplot(aes(x=trt,y=data)) +
  geom_boxplot() +
  facet_wrap(~samp)
```

## Evaluation of normality

### Placebo group

```r
normSim %>%
  gather(samp,data,-trt) %>%
  filter(trt=="placebo") %>%
  ggplot(aes(sample=data)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~samp)
```

### Transplant group


```r
normSim %>%
  gather(samp,data,-trt) %>%
  filter(trt=="transplant") %>%
  ggplot(aes(sample=data)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~samp)
```

---

[← Assess the research question with the two-sample t-test](05-assess-the-research-question-with-the-two-sample-t-test.md) · [Up: contents](index.md)
