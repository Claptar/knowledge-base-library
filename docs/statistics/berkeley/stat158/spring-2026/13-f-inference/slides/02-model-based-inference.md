---
title: Model-Based Inference
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/13-f-inference/slides.html
source_file: sources/berkeley-stat158/spring-2026/13-f-inference/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Model-Based Inference

**Source:** [`13-f-inference/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/13-f-inference/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## ANOVA Table in R

The workhorse function: `aov()`.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
babies_anova <- aov(walk ~ factor(program), data = babies)
anova_table <- summary(babies_anova)
anova_table
```

                    Df Sum Sq Mean Sq F value Pr(>F)
    factor(program)  3   9.75    3.25   1.912  0.168
    Residuals       16  27.20    1.70

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
obs_f_stat <- anova_table[[1]]$`F value`[1]
obs_f_stat
```

    [1] 1.911765

## An analytical null

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
ggplot(null_stats, aes(x = f_vec)) +
  geom_histogram(aes(y = ..density..)) +
  stat_function(fun = df, args = list(df1 = 3, df2 = 16),
                color = "goldenrod", size = 2) +
  geom_vline(xintercept = obs_f_stat, color = "tomato", lwd = 2)
```

<figure>

</figure>

---

[← Designs with One Factor {#designs-with-one-factor .title}](01-designs-with-one-factor-designs-with-one-factor-title.md) · [Up: contents](index.md)
