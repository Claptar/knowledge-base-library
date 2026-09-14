---
title: Import the data
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Import the data

**Source:** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[← Load the required libraries](02-load-the-required-libraries.md) · [Up: contents](index.md) · [Try to get a visualization that describes the data as good as possible!! →](04-try-to-get-a-visualization-that-describes-the-data-as-good-a.md)
