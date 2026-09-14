---
title: Data exploration
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data exploration

**Source:** [`tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

In a previous tutorial, we already studied the effect of
dose on (the logarithm of) suvival time. There, we did not
account for the fact that fish of the same species and/or
fish of similar weight will probably reacht similarly to
the poison.

When we expect the data more closely, we see that these
factors do indeed matter.

```r
plot(poison)
```


```r
library(GGally)
poison %>% select(-Surv_time) %>% ggpairs()
```

- Survival time seems to be strongly associated with dose,
species and weight.

- There is a strong, positive association between log survival time
and weight.

- For low weights, the log survival time slope seems to flatten.

- The weigths are not equally distributed over the different doses.

- There is an association between species and weight.

Some additional visualizations:

- Plot the log survival time in function of weigth.
Add species as a color.

```r
poison %>%
  ggplot(aes(x=Weight,y=log.Surv_time)) +
  geom_point() +
  stat_smooth(method = "loess") +
  ylab("log survival time") +
  xlab("Weight (g)") +
  geom_point(aes(col=Species)) +
  scale_color_manual(values = c("red","darkgoldenrod","black")) +
  theme_bw()
```

We observe a very strong relationship between weight and log
survial time. The weigth is different for different species.

- Plot the fish weights in function of dose

```r
poison %>%
  ggplot(aes(x=as.factor(Dose),y=Weight,fill=Dose)) +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter(width = 0.2) +
  scale_fill_gradient(low = "darkgreen", high = "red") +
  ylab("Weight (g)") +
  xlab("Dose (mg)") +
  theme_bw()
```

We see that, probably by chance, some dosages were administered
to fish with slightly higher (e.g. dose 1.9 mg) or lower weights.

- Plot the log of survival time in function of dose.

```r
poison %>%
  ggplot(aes(x=Dose,y=log.Surv_time)) +
  stat_smooth(method = "loess") +
  ylab("log survival time") +
  xlab("Dose (mg)") +
  geom_point(aes(col=Species)) +
  scale_color_manual(values = c("red","darkgoldenrod","black")) +
  theme_bw() +
  geom_smooth(aes(group=Species,col=Species), method='lm')
```

There is a clear linear relationship between dose and
log survival time, but especially the intercept of
the linear model will be different for different species.

- Plot the relationship between log survival time and species.

```r
poison %>%
  ggplot(aes(x=Species,y=log.Surv_time,color=Species)) +
  geom_boxplot() +
  geom_jitter() +
  ylab("log urvival time") +
  scale_color_manual(values = c("red","darkgoldenrod","black")) +
  theme_bw()
```

The log survival time is different for different species.

The researchers assume, based on the data exploration, that the
dose effect on survival varies between different species. As such,
a good model should have an interaction effect between dose and
species. We will also include an interaction between weight and
species.

---

[← Data tidying](04-data-tidying.md) · [Up: contents](index.md)
