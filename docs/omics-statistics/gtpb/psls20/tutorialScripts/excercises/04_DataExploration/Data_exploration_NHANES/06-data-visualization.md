---
title: Data Visualization
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Visualization

**Source:** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
library(ggplot2)
```


As you might have have already seen, there are many functions
available in base R that can create plots (e.g. `plot()`, `boxplot()`).
Others include: `hist()`, `qqplot()`, etc.
These functions are great because they come with a basic installation
of R and can be quite powerful when you need a quick visualization
of something when you are exploring data.

We are choosing to introduce `ggplot2` because, in our
opinion, it's one of the most simple ways for beginners to
create relatively complicated plots that are intuitive
and aesthetically pleasing.

## Univariate statistics

In univariate statistics, we focus on a single variable
of interest. Here, we will show different ways to visualize
the `BMI` variable from the NHANES dataset. Importantly,
different types of visualizations will provide us with
different types of information!

Here we will visualize the same data using a dotplot,
a histogram and a boxplot.

### Dotplot

```r
NHANES %>%
  filter(!is.na(BMI)) %>%
  head(NHANES, n=100) %>% ## to make the visualization more clear, we take only the first 100 subjects
  ggplot(aes(x=BMI)) +
  geom_dotplot(method = "histodot")
```

In stead of making a visualization "on the fly"
as we did in the code chunk above, we may also store
the visualization in an object. This allows us to:
- Call upon the object again later
- Add extra layers to the plot.

```r
## store the plot from above in the "p" object
p <- NHANES %>%
  filter(!is.na(BMI)) %>%
  head(NHANES, n=100) %>%
  ggplot(aes(x=BMI)) +
  geom_dotplot(method = "histodot")

## Add additional info to the plot
p <- p + xlab("BMI (kg/m2)") +
  theme_bw()

## Display the plot
p
```

Note that if we are sure we do not want to store
the plot for later retrieval, we shouldn't: it would
simple be a waste of storage space!

In the dotplot, the BMI value for each subject (in this case,
the first 100 subjects of the NHANES study), is plotted on the
x-axis. The y-axis allows us to count how many subjects have
a BMI value that falls within a certain counting bin.
For instance, in the BMI interval [29.5, 30.[
we observe 4 subjects.

Note, however, that the dotplot does not provide us with information
on the mean/median values of the data, which are typically features
of high interest.

### Histogram

```r
NHANES %>%
  filter(!is.na(BMI)) %>%
  head(NHANES, n=100) %>%
  ggplot(aes(x=BMI)) +
  geom_histogram()
```

The information that can be obtained from this histogram
is similar to that of the dotplot. Here, we can read immediately
(i.e. without counting) that the BMI interval [29.5, 30.0[
contains 4 subjects. Again, the histogram does not provide us with
information on the mean/median values of the data, but only on
its distribution.

### Boxplot

```r
set.seed(2) ## to make the horizontal position of the jitter non-random

give.n <- function(x){
  return(c(y = 50, label = length(x)))
}

NHANES %>%
  filter(!is.na(BMI)) %>%
  head(NHANES, n=100) %>%
  ggplot(aes(x="", y=BMI)) +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter(width=0.2) +
  stat_summary(geom="text", fun.y=quantile,
               aes(label=sprintf("%1.1f", ..y..)),
               position=position_nudge(x=0.5), size=4.5) +
  annotate("text", x = c(1.5,1.5,1.5,1.5,1.5,1.05,1.05), y = c(12.5,19,24.5,28.5,45,18,35), label = c("(minimum)","(25%)","(median)","(75%)","(maximum)","whisker","whisker"),size=3) +
  stat_summary(fun.data = give.n, geom = "text")
```

Arguably, the boxplot is the most informative default
visualization strategy. First, it provides us with
similar insights to the shape of the distribution as
the histogram. Second, It clearly displays several useful
summary statistics such as the median, the interquartile
range, whiskers and outliers. Third, with the geom_jitter
functionality we can also project each individual value
of the dataset on the plot.

The only disadvantage of the boxplot as compared to the
dotplot or histogram is that we cannot see (from the figure)
how many subjects have a BMI value within a certain interval.
However, this feature usually is not of primary interest.

## Bivariate statistics

In bivariate statistics, the goal is to study two variables,
including the relationship between both variables.

In terms of visualizations, the scatterplot is the baseline
method for displaying two variables.

### Create scatter plots using `geom_point()`

For the NHANES dataset, we can for instance look
at the relationship between a person's height and weight
values.

```r
NHANES %>%
  ggplot(aes(x = Height, y = Weight)) +
  geom_point() +
  xlab("Height (cm)") +
  ylab("Weight (kg)")
```

We used the `xlab()` and `ylab()` functions
in `ggplot2` to specify the x-axis and y-axis
labels. Note that NA values were automatically
remove by the geom_point function.

ggplot2 also has a very broad panel of aesthetic features
for improving your plot. One very basic feature is that we
can give colors to the ggplot object. For instance, we can
give different colors to the dots in the previous
scatterplot based on a subject's gender.

```r
NHANES %>%
  ggplot(aes(x = Height, y = Weight, color = Gender)) +
  geom_point() +
  xlab("Height (cm)") +
  ylab("Weight (kg)")
```

## Combining dplyr and ggplot2

Note that the previous functions from the dplyr
package can be easily combined with ggplot through
the concept of pipes %>%.

For instance, we could make the same scatterplot as above,
but only for white, married adults.

In addition, we here also show some convenient ggplot features;
1. Setting the colors manually
2. Set to have a white background
3. Set a (main) title for the plot
4. Pick a different shape for the dots in the scatterplot
5. Manually set the limits of the x- and y-axes

Note that this a only the tip of the iceberg of the
the ggplot functionalities!

```r
NHANES %>%
  filter(Age >= 18, Race1 == "White", MaritalStatus == "Married") %>% ## select the required data
  ggplot(aes(x = Height, y = Weight, color = Gender)) +
  geom_point(shape=17, size = 1) + ## set to a different shape (triangle) and size
  ggtitle("Height versus Weight") + ## for the main title
  xlab("Height (cm)") +
  ylab("Weight (kg)") +
  xlim(0,220) + ## set limit of x-axis
  ylim(0,220) + ## set limit of y-axis
  scale_color_manual(values = c("red","blue")) + ## manually set colors
  theme_bw() ## set white background
```

Next to scatterplots, we have a large number of other
types of plots at our disposal. Importantly, some plots
will be more informative than others, depending on the
research question. Therefore, choosing the plot that is
most informative is crucial. We show this with a more
elaborate example later (Data_exploration_captopril.Rmd).

## Final example

### Goal

Set up a reference interval for the systolic blood
pressure in the NHANES dataset.

### Background

The captopril dataset, which we will explore and analyse later,
holds information on  15 patients that have increased blood pressure
values.

Before we may conduct such an experiment, we first need to know
which values should be considered _increased_ and which ones should be
considered _normal_. To find an interval for values that are normal,
we can set up a reference interval. To set up this interval, we will
use the NHANES dataset. The `BPSysAve` column holds data on the systolic
blood pressure. To select healthy subjects, we will need to subset the
data.

### Analysis

First, we will plot the data for all subjects for which we have all
the required data and that are between 40 and 65 years old.

Note, that we  calculate the standard deviation on the average blood pressure measurements. If you have the same number of "technical repeats" on the same person you are allowed to average them first.
Note, however, that if there are some technical measurements missing, averaging is no longer allowed because then the averaged values will be heteroscedastic: some averages are based on more technical repeats than others so they will have a different standard deviation.

```r
## histogram of BPSysAve for subjects wit age between 40 and 65 years old
NHANES %>%
  filter(!is.na(Race1), !is.na(Smoke100n), !is.na(BMI_WHO), !is.na(Age), !is.na(HardDrugs), !is.na(HealthGen), !is.na(Gender), !is.na(AlcoholYear), !is.na(BPSys1), !is.na(BPSys2), !is.na(BPSys3), !is.na(SleepTrouble)) %>% ## retains 4660 subjects with the required data
  filter(between(Age,40,65)) %>% ## filter the subjects on age, retains 2522 subjects
  distinct(ID,.keep_all=TRUE) %>% ## removes duplicated IDs, retains 1467 subjects
  ggplot(aes(x=BPSysAve)) +
  geom_histogram()
```

An important requirement of calculating reference intervals is
that the data are normally distributed. this is clearly not the
case; the data has a long right tail, which is quite common
in biological data (in this easier to have extreme values on the
right-hand side than on the left-hand size, which is additionally
bounded by zero for most biological variables).

By selecting only _healthy_ subjects, we expect the data to be
distributed more normally. We define _healthy_ as being a non-smoker,
without a history of diabetes, hard drugs or sleeping trouble, with a
general health that is not considered poor and that has a BMI between
18.5 and 29.9.

```r
## histogram of BPSysAve for HEALTHY male subjects with age between 40 and 65 years old
NHANES %>%
  filter(!is.na(Race1), !is.na(Smoke100n), !is.na(BMI_WHO), !is.na(Age), !is.na(HardDrugs), !is.na(HealthGen), !is.na(Gender), !is.na(AlcoholYear), !is.na(BPSys1), !is.na(BPSys2), !is.na(BPSys3), !is.na(SleepTrouble)) %>% ## retains 4660 subjects with the required data
  filter(between(Age,40,65)) %>% ## filter the subjects on age, retains 2522 subjects
  distinct(ID,.keep_all=TRUE) %>% ## removes duplicated IDs, retains 1467 subjects
  filter(Smoke100n == "Non-Smoker", Diabetes == "No", HardDrugs == "No", HealthGen != "Poor", SleepTrouble == "No", BMI_WHO%in%c("18.5_to_24.9","25.0_to_29.9")) %>% ## filter to have only healthy subjects, based on multiple health criteria. Retains 275 subjects.
  ggplot(aes(x=BPSysAve)) +
  geom_histogram()
```

We will evaluate if the distribution is normally distributed using a QQ-plot.
In this plot we compare the quantiles in the data with the quantiles of the normal distribution.
If the data are normally distributed then the data in the QQ-plot approximately follows a straight line.
Deviations from the straight line indicate deviations of normality.

```r
NHANES %>%
  filter(!is.na(Race1), !is.na(Smoke100n), !is.na(BMI_WHO), !is.na(Age), !is.na(HardDrugs), !is.na(HealthGen), !is.na(Gender), !is.na(AlcoholYear), !is.na(BPSys1)&!is.na(BPSys2)&!is.na(BPSys3), !is.na(SleepTrouble)) %>%
  filter(between(Age,40,65)) %>%
  distinct(ID,.keep_all=TRUE) %>%
  filter(Smoke100n == "Non-Smoker", Diabetes == "No", HardDrugs == "No", HealthGen != "Poor", SleepTrouble == "No", BMI_WHO%in%c("18.5_to_24.9","25.0_to_29.9")) %>%
  ggplot(aes(sample=BPSysAve))+
  geom_qq()+
  geom_qq_line()
```

We observe that the distribution is slightly skewed too the right.
We will therefore log transform the bloodpressure measurements.
We use the log2 transformation: a difference of 1 on the log scale corresponds to doubling the blood pressure on the original scale:
$log2(B)-log2(A)=log2(B/A)$ \rightarrow $2^{1}=2$.

```r
NHANES %>%
  filter(!is.na(Race1), !is.na(Smoke100n), !is.na(BMI_WHO), !is.na(Age), !is.na(HardDrugs), !is.na(HealthGen), !is.na(Gender), !is.na(AlcoholYear), !is.na(BPSys1)&!is.na(BPSys2)&!is.na(BPSys3), !is.na(SleepTrouble)) %>%
  filter(between(Age,40,65)) %>%
  distinct(ID,.keep_all=TRUE) %>%
  filter(Smoke100n == "Non-Smoker", Diabetes == "No", HardDrugs == "No", HealthGen != "Poor", SleepTrouble == "No", BMI_WHO%in%c("18.5_to_24.9","25.0_to_29.9")) %>%
  ggplot(aes(sample=BPSysAve %>% log2))+
  geom_qq()+
  geom_qq_line()
```

We see that the data is normally distributed upon log transformation.
We can now use the normal distribution to construct a 95% interval at log scale that we will backtransform to the original scale.


```r
## to get the 95% reference interval for the healthy group;

summary_NHANES <- NHANES %>%
  filter(!is.na(Race1), !is.na(Smoke100n), !is.na(BMI_WHO), !is.na(Age), !is.na(HardDrugs), !is.na(HealthGen), !is.na(Gender), !is.na(AlcoholYear), !is.na(BPSys1), !is.na(BPSys2), !is.na(BPSys3), !is.na(SleepTrouble)) %>% ## retains 4660 subjects with the required data
  filter(between(Age,40,65)) %>% ## filter the subjects on age, retains 2522 subjects
  distinct(ID,.keep_all=TRUE) %>% ## removes duplicated IDs, retains 1467 subjects
  filter(Smoke100n == "Non-Smoker", Diabetes == "No", HardDrugs == "No", HealthGen != "Poor", SleepTrouble == "No", BMI_WHO%in%c("18.5_to_24.9","25.0_to_29.9")) %>%
  mutate(BPSysAveLog=BPSysAve %>% log2) %>%
  summarize_at("BPSysAveLog",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))

paste("Mean value (log2):", summary_NHANES$mean)
paste("Geometric mean value (log2):", 2^summary_NHANES$mean)
paste("Standard deviation (log2):", summary_NHANES$sd)
paste0("Reference interval (log2): [", summary_NHANES$mean - 2*summary_NHANES$sd, ";", summary_NHANES$mean + 2*summary_NHANES$sd, "]")
paste0("Reference interval (log2): [", 2^(summary_NHANES$mean - 2*summary_NHANES$sd), ";", 2^(summary_NHANES$mean + 2*summary_NHANES$sd), "]")
```

The log2 systolic blood pressure for healthy subjects is approximately normally distributed. We have calculated the
mean and standard deviation of blood pressure values in this healthy
subset at the log2 scale, which allows us to set up the (95%) reference interval, for
what we can consider to be _normal_ blood pressure values. Any of the
later patients who's values do not fall within this interval, we can
consider _abnormal_.

The log2 mean blood pressure value of the healthy subset is `r round(summary_NHANES$mean,2)`, with
a standard deviation of `r round(summary_NHANES$sd,2)`. When we replace the population average
and population standard deviation with these estimates, we obtain a
95% reference interval of [`r round(summary_NHANES$mean - 2*summary_NHANES$sd,2)`;`r round(summary_NHANES$mean + 2*summary_NHANES$sd,2)`] on log scale and [`r round(2^(summary_NHANES$mean - 2*summary_NHANES$sd),2)`,`r round(2^(summary_NHANES$mean + 2*summary_NHANES$sd),2)`] mmHg on the original scale.

Note, that in the literature a value 140 mmHg for the systolic blood
pressure is typically considered to be the upper limit of _normality_.

---

[← Data wrangling with dplyr](05-data-wrangling-with-dplyr.md) · [Up: contents](index.md)
