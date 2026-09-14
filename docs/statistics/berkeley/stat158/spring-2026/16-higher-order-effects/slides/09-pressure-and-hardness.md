---
title: Pressure and Hardness
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Pressure and Hardness

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

ggplot(group_means, aes(x = pressure,
                        y = avg_strength,
                        color = hard,
                        group = hard)) +
  geom_point(shape = 15, size = 4) +
  geom_line(lwd = 2) +
  theme_bw()
```

<figure>

</figure>

## 3-way Interaction Plots

You’ll need at least one interaction plot for each <s>pairwise combination</s> *level of one of the three factors*.

- *Filter the data for just one level of the first factor.*
- Calculate the mean response over every treatment combination of the two factors.
- Plot those means on the y axis, with the first factor on the x and the second factor differentiated by color, linetype or shape.
- *Label the plot with the level of the third factor.*
- Draw lines between the means with the same level of the second factor.

## 3-way Interaction Plots (gg-style)

You’ll need at least one interaction plot for each <s>pairwise combination</s> *level of one of the three factors*.

- Calculate the mean response over every treatment combination of the three factors.
- Plot those means on the y axis, with the first factor on the x and the second factor differentiated by color, linetype or shape.
- Draw lines between the means with the same level of the second factor.
- Create a separate facet for each level of the third factor.

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}

---

[← Pressure and Hardness](08-pressure-and-hardness.md) · [Up: contents](index.md) · [Time and Pressure and Hardness →](10-time-and-pressure-and-hardness.md)
