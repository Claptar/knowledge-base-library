---
title: make the plot
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/05/code_review.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# make the plot

**Source:** [`labs/05/code_review.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

ggplot(df, aes(x = x, y = y)) +
  geom_point(aes(color = color), size = 3) +
  geom_line() +
  theme_bw() +
  labs(x = "Label related to data", y = "Label related to data") +
  ggtitle("Short but informative title") +
  scale_color_discrete(name = "Group designation") +
  theme(legend.position = c(1, 1),
        legend.justification = c(1, 1),
        legend.background = element_blank(),
        legend.box.background = element_rect(colour = "black")) +
  ylim(0, 13)
```

## Vectorization

"Vectorization" in R implies using functions that naturally operate over vector
inputs, rather than processing each element one at a time. This ends up being
faster because, under the hood, vectorized functions in R actually call
corresponding code written in C, and the C code itself uses a loop that runs
much more quickly than an equivalent loop in R would. But to do that, it needs
to receive the full vector all at once.

R is vectorized in many basic mathematical operations (addition, subtraction,
multiplication, division, etc.) and any other functions have built-in
vectorization as well. Some functions -- like those for linear algebra -- even
use highly optimized parallel routines in C, adding further speedups. So when
operating on large vectors or matrices, be sure to check the documentation to
see if there is a vectorized function that you can use to your advantage.

```r
#####################

---

[← set things up](14-set-things-up.md) · [Up: contents](index.md) · [vectorized division →](16-vectorized-division.md)
