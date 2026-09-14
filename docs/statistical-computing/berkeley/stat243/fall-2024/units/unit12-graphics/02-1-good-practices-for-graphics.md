---
title: 1. Good practices for graphics
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit12-graphics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Good practices for graphics

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit12-graphics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

There are a number of principles that can be used in developing and
critiquing graphics. Let's skim over the principles and then think about them in the context of some examples, some of which show those
principles being violated.


## Best practices

Here's a list of some guidelines to consider in creating graphics.

1.  Have a high density of information to space

2.  Show the data clearly: are the relationships and patterns that are
    clearly seen in the graph the ones you want to represent?

3.  Can you reorder groups or variables to better illustrate the key
    points?

4.  Strategies for going beyond two dimensions

    1.  Use color, but avoid excessive use of color that is not informative.

    2.  Use varying symbol or line types

    3.  Use multiple panel plots

5.  Avoid 3-d graphics unless they truly add information

6.  Multi-panel (trellis) plots (called "small multiples" when using the same
    scale/axes) is a key strategy

7.  Think carefully about your baseline (e.g., the lowest level on the
    y-axis)

    1.  Zero is often a good baseline

    2.  Avoid stacked barplots (see demo code) and other plots with
        shifting baselines, as it's hard to assess anything except the
        total and the baseline category.

8.  Studies indicate that humans have a hard time comparing areas,
    volumes, or angles, so try to avoid plots that represent data using
    any of these, including pie charts. Instead use position or length
    (horizontal is better than vertical) to display data values

9.  Label axes and include units

10. Keep the ranges of axes (and other features) the same for multiple
    panels, when possible

11. Use a legend where appropriate

12. Jitter values if needed so that all the data points can be seen, but
    if you have too many points to avoid a lot of overplotting, use
    [strategies discussed below](08-4-colors.md#overplotting-of-points).

13. Use vector graphics formats such as PDF or Postscript/EPS as these
    scale without pixelation when resized. Raster formats such as JPEG,
    PNG, and TIFF don't rescale well and when they have high resolution
    also have large file sizes. See Section 3 for more details.

Rob Hyndman has a [list of 20 rules for good
graphics](http://robjhyndman.com/hyndsight/graphics/), including some of
the ones above. There is also a list of guidelines in [this article](https://www.tandfonline.com/doi/full/10.1080/10618600.2014.989324).

## Some example graphics

1. This [pie chart](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/graphics_files/trafficking.jpeg) circulating online is intended to raise awareness of human trafficking. What do you
   like or not like about the graphical presentation?

2.  Here are various plots showing time series of categorical data. What do you like or not like about
    the graphical approaches shown?
    - This [NY Times article](https://www.nytimes.com/interactive/2024/09/27/opinion/fentanyl-overdose-deaths.html) shows deaths from drug overdoses over time.
    - This [graphic from the FlowingData website](https://flowingdata.com/2016/01/05/causes-of-death) shows causes of mortality by age and sex in the United States.
    - This [NY Times article](https://www.nytimes.com/interactive/2024/08/02/climate/electricity-generation-us-states.html) shows the sources of electricity for the US and specific states.
    - This [NY Times article](http://www.nytimes.com/interactive/2016/08/08/sports/olympics/history-olympic-dominance-charts.html)
    presents time-series graphics about how many Olympic medals have been won by different countries.

3.  Consider [this scatterplot of life expectancy statistics](https://academic.oup.com/view-large/figure/81018073/dyr146f2.gif)
    from [this article](https://academic.oup.com/ije/article/40/6/1703/801755) on variation in lifespan in European countries in the International Journal of Epidemiology. What
    are you able to learn from this presentation of the data. What other
    ways could you plot the data to better illustrate patterns in the data? The data are in [this CSV](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/graphics_files/life_exp.csv) with
    [some initial exploration of plotting approaches using `ggplot` in R](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/graphics_files/liffe_exp.R).

4.  Here's [another online graphic](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/graphics_files/exampleGraphic.png). What
    aspects of the graph could be improved? What aspects do you like?

5.  [This file](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/graphics_files/shell.pdf) in the repository has an example of a crazy pie
    chart from an advertisement in the NY Times from December 2014.

6.  [This article](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/graphics_files/wainer1984.pdf) in the repository is rather old but the
    ideas are still relevant and while the example figures are dated in
    terms of appearance, the same issues arise with more modern-looking
    graphics.

7.  [This article](../graphics_files/gelmanUnwin2013/index.md) in the repository presents a
    modern-day reinterpretation of a famous graphic from Florence
    Nightingale regarding causes of death in the British Army during the
    Crimean War in the 1850s.

8.  This [somewhat recent blog](https://www.r-bloggers.com/2021/07/improving-a-visualization/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29%20)
    post nicely discusses the process of improving a visualization
    regarding streaming services market share in 2020 vs. 2021.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Graphics devices →](03-2-graphics-devices.md)
