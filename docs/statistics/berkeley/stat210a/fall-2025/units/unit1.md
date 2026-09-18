---
title: Unit 01 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit1.html
source_file: sources/berkeley-stat210a/fall-2025/units/unit1.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/unit1.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit1.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Unit 01 —

$$ \\newcommand{\\trans}{^\\mathsf{T}} \\newcommand{\\eps}{\\epsilon} $\$

## Unit 1: Intro {#unit-1-intro .title}

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

-

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

This is an example of using qmd as the source document.

### Evaluated Python code chunk, with a plot {.anchored anchor-id="evaluated-python-code-chunk-with-a-plot"}

Code

``` {.sourceCode .python .code-with-copy}
import numpy as np
x = np.random.normal(size=100)
import matplotlib.pyplot as plt
plt.hist(x)
plt.show()
np.mean(x)
```

![](https://raw.githubusercontent.com/berkeley-stat210a/fall-2025/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit1_files/figure-html/cell-2-output-1.png)

```
0.15857207845004595
```

### $\LaTeX$ {#math2 .anchored anchor-id="latex"}

$$
\theta = \int_0^\infty f(x,\theta)d\theta
$$

### $\LaTeX$ macro {#math4-macro .anchored anchor-id="latex-macro"}

> **Warning**: need to look back at this as having `include-before-body` in the yaml causes extra space at top of page.

$$
A = X \trans Y
\$\$

### Styled div via direct html {.anchored anchor-id="styled-div-via-direct-html"}

This content can be styled via the border class.

### A callout {.anchored anchor-id="a-callout"}

Tip with Title

This is an example of a callout with a title.

### Tabset {.anchored anchor-id="tabset"}

- R
- Python

This code is not executed.

``` {.sourceCode .r .code-with-copy}
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

This code is executed.

Code

``` {.sourceCode .python .code-with-copy}
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

```
Fizz
```

---

[Up: contents](../index.md)
