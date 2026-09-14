---
title: 'Unit 1: Intro'
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/units/unit1.qmd
source_file: sources/berkeley-stat210a/fall-2024/units/unit1.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unit 1: Intro

**Source:** [`units/unit1.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/units/unit1.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

This is an example of using qmd as the source document.


## Evaluated Python code chunk, with a plot

```python
import numpy as np
x = np.random.normal(size=100)
import matplotlib.pyplot as plt
plt.hist(x)
plt.show()
np.mean(x)
```


## $\LaTeX$

$$
\theta = \int_0^\infty f(x,\theta)d\theta
$$

## $\LaTeX$ macro

> **Warning**: need to look back at this as having `include-before-body` in the yaml causes extra space at top of page.

$$
A = X \trans Y
$$

## Styled div via direct html

::: {.border}
This content can be styled via the border class.
:::

## A callout

!!! tip "Tip"
## Tip with Title

This is an example of a callout with a title.
:::

## Tabset

::: {.panel-tabset}
## R

This code is not executed.

```{.r}
fizz_buzz <- function(fbnums = 1:50) {
  output <- dplyr::case_when(
    fbnums %% 15 == 0 ~ "FizzBuzz",
    fbnums %% 3 == 0 ~ "Fizz",
    fbnums %% 5 == 0 ~ "Buzz",
    TRUE ~ as.character(fbnums)
  )
  print(output)
}

fizz_buzz(3)
```

## Python

This code is executed.

```python
def fizz_buzz(num):
  if num % 15 == 0:
    print("FizzBuzz")
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0:
    print("Fizz")
  else:
    print(num)

fizz_buzz(3)
```

:::

---

[Up: contents](../index.md)
