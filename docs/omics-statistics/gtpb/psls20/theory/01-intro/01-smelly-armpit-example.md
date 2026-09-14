---
title: Smelly armpit example
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd
source_file: sources/gtpb-psls20/theory/01-intro.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Smelly armpit example

**Source:** [`theory/01-intro.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Smelly armpits are not caused by sweat itself. The smell is caused by specific micro-organisms belonging to the group of *Corynebacterium spp.* that metabolise sweat.
Another group of abundant bacteria are the *Staphylococcus spp.*, these bacteria do not metabolise sweat in smelly compounds.

- The CMET-groep at Ghent University does research on transplanting the armpit microbiome to save people with smelly armpits.

- Proposed Therapy:
  	1. Remove armpit-microbiome with antibiotics
    2. Influence armpit microbiome with microbial  transplant (https://youtu.be/9RIFyqLXdVw)

- Experiment:

    - 20 subjects with smelly armpits are attributed to one of two treatment groups
    - placebo (only antibiotics)
    - transplant (antibiotics followed by microbial transplant).
    - The microbiome is sampled 6 weeks upon the treatment.
    - The relative abundance of *Staphylococcus spp.* on *Corynebacterium spp.* + *Staphylococcus spp.* in the microbiome is measured via DGGE (*Denaturing Gradient Gel Electrophoresis*).

---

## Import the data
```r
read_lines("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/armpit.csv")
```

The file is comma separated and in tidy format

```r
ap<-read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/armpit.csv")
ap
```

---

## Data Exploration and Descriptive Statistics

- Data exploration is extremely important to get insight in the data.
- It is often underrated and overlooked.

### Descriptive statistics
We first summarize the data and calculate the mean, standard deviation, number of observations and standard error and store the result in an object apRelSum via 'apRelSum<-`

1. We pipe the `ap` dataframe to the group_by function to group the data by treatment trt `group_by(trt)`
2. We pipe the result to the `summarize_at` function to summarize the "rel" variable and calculate the mean, standard deviation and the number of observations
3. We pipe the result to the `mutate` function to make a new variable in the data frame `se` for which we calculate the standard error


```r
apRelSum<-ap%>%
  group_by(trt)%>%
  summarize_at("rel",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))

apRelSum
```

---

### Plots
We will use ggplot2 to make our plots.
With the ggplot2 library we can easily build plots by adding layers.

#### barplot

1. We pipe our summarized data to the `ggplot` function and we select the treatment variable trt and the variable mean for plotting `aes(x=trt,y=mean)`

2. We make a barplot based on this data using the `geom_bar` function. The statistic is `stat="identity"` because the bar height should be equal the value for the mean of the relative abundance.

```r
apRelSum%>%
  ggplot(aes(x=trt,y=mean)) +
  geom_bar(stat="identity")
```

- Is this plot informative??

---

We will now add standard errors to the plot
using `geom_errorbar` function and specify the minimum and maximum value for of the error bar, the width command is used to set the width of the error bar smaller than the width of the bar.

```r
apRelSum%>%
  ggplot(aes(x=trt,y=mean)) +
  geom_bar(stat="identity") +
  geom_errorbar(aes(ymin=mean-se,ymax=mean+se),width=.2)
```

- Is this plot informative??

---

#### boxplots

I consider barplots to be bad plots

- They are not informative
- They just visualize a two point summary of the data. It is better to do this in a table
- They use a lot of space (e.g. from zero up to the minimum relative abundance) where no data are present.

It is better to get a view on the distribution of the data. We can use a boxplot for this purpose.
We first explain what a boxplot.

---

```r
fem <- NHANES::NHANES %>% filter(Gender=="female" & !is.na(DirectChol)) %>% select(DirectChol)
boxplot(fem$DirectChol, ylab="Direct cholesterol",cex.lab=1.5,cex.axis=1.5,cex.main=1.5)
rangeCl<-quantile(fem$DirectChol,c(.25,.75))+c(-1,1)*diff(quantile(fem$DirectChol,c(.25,.75)))*1.5
boxYs<-c(range(fem$DirectChol[fem$DirectChol<=rangeCl[2]&fem$DirectChol>=rangeCl[1]]),quantile(fem$DirectChol,c(.25,.5,.75)),rangeCl[2]+(max(fem$DirectChol)-rangeCl[2])/2)
text(1.3,boxYs,labels=c("wisker","wisker","x25","mediaan","x75","outliers"),pos=4,cex=1.3)
lines(c(1.1,1.3,1.3,1.1),c(rangeCl[2],rangeCl[2]+(max(fem$DirectChol)-rangeCl[2])/2,rangeCl[2]+(max(fem$DirectChol)-rangeCl[2])/2,max(fem$DirectChol)),lty=2)
```

---

We will now make a boxplot for the ap data

1. We pipe the `ap` dataframe to the ggplot command
2. We select the data with the command `ggplot(aes(x=trt,y=rel))`
3. We add a boxplot with the command `geom_boxplot()`

```r
ap %>%
  ggplot(aes(x=trt,y=rel)) +
  geom_boxplot()
```

---

- Note, that we do not have so many observations.

- It is always better to show the data as raw as possible!

We will now add the raw data to the plot.

- Note that we set the outlier.shape=NA in the geom_boxplot function because because we will add all raw data anyway.
- We add the raw data using `geom_point(position="jitter")`, with the argument position='jitter' we will add some random noise to the x coordinate so that we can see all data.

```r
ap %>%
  ggplot(aes(x=trt,y=rel)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter")
```

This is an informative plot!

---

## Some concepts

- Why do we need more than one student per group?

- What are the meaning and the consequences of the term "randomly"?

- Consider two designs:

1. A research assistant selects 20 male students with smelly armpits from his faculty.

2. A research assistant selects 20 random people with smelly armpits from the Belgian population.

---

```r
ap2<-ap
hlp<-lm(rel~trt,ap)
ap2$rel<-rnorm(20,mean=hlp$fit-20,sd=sigma(hlp)*2)
```


```r
ap %>%
  ggplot(aes(x=trt,y=rel)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter") +
  ylim(0,100)

ap2 %>%
  ggplot(aes(x=trt,y=rel)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter") +
  ylim(0,100)
```

---

- Design 1: smaller variability

- Design 2: larger variability and lower relative abundance of *Staphylococcus*

- What is the best design?

---

- Random sampling is closely related to the concept of the population or the scope of the study.

- Based on a sample of subjects, the researchers want to come to conclusions that hold for

    - all kinds of people
    - only male students

- Scope of the study should be well specified before the start of the study.

- For the statistical analysis to be valid, it is required that the subjects are selected completely at random from the population to which we want to generalize our conclusions.

- Selecting completely at random from a population implies:
    - all subjects in the population should have the same probability of being selected in the sample,
    - the selection of a subject in the sample should be independent from the selection of the other subjects in the sample.

- The sample is thus supposed to be representative for the population, but still it is random.

- What does this imply?

---

---

[Up: contents](index.md) · [Sample to sample variability →](02-sample-to-sample-variability.md)
