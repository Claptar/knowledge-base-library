---
title: Time and Hardness
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Time and Hardness

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

ggplot(group_means, aes(x = time,
                        y = avg_strength,
                        color = hard,
                        group = hard)) +
  geom_point(shape = 15, size = 4) +
  geom_line(lwd = 2) +
  theme_bw()
```

<figure>

</figure>

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}

---

[← Time and Hardness](06-time-and-hardness.md) · [Up: contents](index.md) · [Pressure and Hardness →](08-pressure-and-hardness.md)
