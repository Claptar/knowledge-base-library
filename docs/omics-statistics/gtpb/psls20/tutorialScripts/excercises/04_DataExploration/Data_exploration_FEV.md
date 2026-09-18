---
title: 'Tutorial 1.4: Exploring the FEV dataset'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Tutorial 1.4: Exploring the FEV dataset

In this tutorial, you will learn how to import, tidy, wrangle and
visualize data yourself! You will work with one specific dataset;

## The FEV dataset

The FEV, which is an acronym for forced expiratory volume,
is a measure of how much air a person can exhale (in liters)
during  a forced breath. In this dataset, the FEV of 606 children,
between the ages of 6 and 17, were measured. The dataset
also provides additional information on these children:
their `age`, their `height`, their `gender` and, most
importantly, whether the child is a smoker or a non-smoker.

The goal of this experiment was to find out whether or not
smoking has an effect on the FEV of children.

Note: to analyse this dataset properly, we will need some
relatively advanced modeling techniques. At the end of this
week, you will have seen all three required steps to analyse
such a dataset! For now, we will limit ourselves to exploring
the data.

## Load the required libraries

```r
...
```

## Import the data

```r
...
```

Have a first look at the data

```r
...
```

There are a few things in the formatting of the
data that can be improved upon:

1. Both the `gender` and `smoking` can be transformed to
factors.
2. The `height` variable is written in inches. Assuming that
this audience is mainly Portuguese/Belgian, inches are hard to
interpret. Let's add a new column, `height_cm`, with the values
converted to centimeters

```r
...
```

That's better!

Now, let's make a first explorative plot, showing
only the FEV for both smoking categories.

Which type of plot do you suggest? Generate a good-looking,
informative representation of the data.

```r
...
```

Did you expect these results?

Maybe there is something else going on in the data.
By taking more of the information in the dataset into account, can
you provided a more detailed/accurate visualizition of the
variables that effect the FEV?

```r
...


## Try to get a visualization that describes the data as good as possible!!


...
```

---

[Up: contents](../../../index.md)
