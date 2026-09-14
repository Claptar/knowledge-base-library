---
title: Import the data
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_FEV.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_FEV.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Import the data

**Source:** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_FEV.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_FEV.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
fev <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/fev.txt")
head(fev)
```

There are a few things in the formatting of the
data that can be improved upon:

1. Both the `gender` and `smoking` can be transformed to
factors.
2. The `height` variable is written in inches. Assuming that
this audience is mainly Portuguese/Belgian, inches are hard to
interpret. Let's add a new column, `height_cm`, with the values
converted to centimeter using the `mutate` function.

```r
fev <- fev %>%
  mutate(gender = as.factor(gender)) %>%
  mutate(smoking = as.factor(smoking)) %>%
  mutate(height_cm = height*2.54)

head(fev)
```

That's better!

Now, let's make a first explorative plot, showing
only the FEV for both smoking categories.

Which type of plot do you suggest?

```r
fev %>%
  ggplot(aes(x=smoking,y=fev,fill=smoking)) +
  scale_fill_manual(values=c("dimgrey","firebrick")) +
  theme_bw() +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter(width = 0.2, size=0.1) +
  ggtitle("Boxplot of FEV versus smoking") +
  ylab("fev (l)") +
  xlab("smoking status")
```

Did you expect these results?

It appears that children that smoke have a higher
median FEV than children that do not smoke.
Should we change legislations worldwide and make
smoking obligatory for children?

Maybe there is something else going on in the data.
Now, we will generate a similar plot, but we will
stratify the data based on age (age as factor).

```r
fev %>%
  ggplot(aes(x=as.factor(age),y=fev,fill=smoking)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(width = 0.2, size = 0.1, position = position_jitterdodge()) +
  theme_bw() +
  scale_fill_manual(values=c("dimgrey","firebrick")) +
  ggtitle("Boxplot of FEV versus smoking, stratified on age") +
  ylab("fev (l)") +
  xlab("smoking status")
```

This plot seems to already give us a more
plausible picture. First, it seems that we do not have
any smoking children of ages 6, 7 or 8. Second, when
looking at the results per age "category", it seems
no longer the case that smokers have a much higher FEV
than non-smokers; for the higher ages, the contrary
seems true.

This shows that taking into account important confounders
(in this case) is crucial! If we simply analysed based on
the smoking status and FEV values only, we probably would've
obtained completely incorrect results.

Can provide an even better visualization of the data, taking
into account more useful explanatory variables with respect
to the FEV?

```r
fev %>%
  ggplot(aes(x=as.factor(age),y=fev,fill=smoking)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(width = 0.2, size = 0.1, position = position_jitterdodge()) +
  theme_bw() +
  scale_fill_manual(values=c("dimgrey","firebrick")) +
  ggtitle("Boxplot of FEV versus smoking, stratified on age and gender") +
  ylab("fev (l)") +
  xlab("smoking status") +
  facet_grid(rows = vars(gender))
```

This plot holds one extra level of information, the gender
of the child. Especially for higher ages, the median FEV
is higher for males as compared to females.

The only source of information that is lacking is `height`.
To look at the effect of height, we could simply make a
scatterplot displaying the FEV in function of a child's
height (in cm). Additionally, we could color the dots based
on gender.

```r
fev %>%
  ggplot(aes(x=height_cm,y=fev,color=gender)) +
  geom_point() +
  scale_color_manual(values=c("darkorchid","olivedrab4")) +
  theme_bw() +
  ggtitle("Boxplot of FEV versus height") +
  ylab("fev (l)") +
  xlab("height (cm)")
```

There is a clear relationship between height and FEV.
In addition, we see that for the large height values
(>175cm), we mainly find male subjects.

---

[← Load the required libraries](02-load-the-required-libraries.md) · [Up: contents](index.md)
