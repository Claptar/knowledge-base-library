---
title: Data tidying
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data tidying

**Source:** [`tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

There are a few things in the formatting of the
data that can be improved upon:

1. Both the `gender` and `smoking` can be transformed to
factors.
2. The `height` variable is written in inches. Assuming that
this audience is mainly Portuguese/Belgian, inches are hard to
interpret. Let's add a new column, `height_cm`, with the values
converted to centimeters

```r
fev <- fev %>%
  mutate(gender = as.factor(gender)) %>%
  mutate(smoking = as.factor(smoking)) %>%
  mutate(height_cm = height*2.54)

head(fev)
```

That's better!

## Data exploration

```r
fev$height
```


```r
fev %>% mutate(lfev=log(fev)) %>% dplyr::select(smoking,gender,age,height_cm,lfev) %>% ggpairs()
```

```r
plot(log(fev$fev)~fev$age)
```


There a very strong associations between
- age and height
- age and FEV
- heigth and FEV
- gender and height
- gender and FEV
- ...

Remember the "Data_exploration_FEV.Rmd" file? There, we
saw that plotting the FEV in function of smoking status
only, it appeared that the FEV was higher for smokers.

```r
fev %>%
  ggplot(aes(x=smoking,y=age,fill=smoking)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(width = 0.2, size = 0.1, position = position_jitterdodge()) +
  theme_bw() +
  scale_fill_manual(values=c("dimgrey","firebrick")) +
  ggtitle("Boxplot of FEV versus smoking") +
  ylab("fev (l)") +
  xlab("smoking status")
```

```r
plot(fev$age~fev$height_cm)
```


However, if we "corrected" the visualization for a child's
age and/or heigth and/or gender, this completely changed the picture.

Let's again make a nice plot where we make a boxplot of the FEV
in function of age (as factor), stratified on gender (facet)
and colored based on the smoking status.

```r
fev %>%
  ggplot(aes(x=as.factor(age),y=fev,fill=smoking)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(width = 0.2, size = 0.1, position = position_jitterdodge()) +
  theme_bw() +
  scale_fill_manual(values=c("dimgrey","firebrick")) +
  ggtitle("Boxplot of FEV versus smoking, stratified on age and gender") +
  ylab("fev (l)") +
  xlab("age (years)") +
  facet_grid(rows = vars(gender))
```

---

[← Import the data](03-import-the-data.md) · [Up: contents](index.md) · [Analysis →](05-analysis.md)
