---
title: Unit 01 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit1.html
source_file: sources/berkeley-stat210a/fall-2025/units/unit1.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Unit 01 —

**Source:** [`units/unit1.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit1.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

\$\$ \\newcommand{\\trans}{^\\mathsf{T}} \\newcommand{\\eps}{\\epsilon} \$\$

# Unit 1: Intro {#unit-1-intro .title}

Code

- <a href="javascript:void(0)" id="quarto-show-all-code" class="dropdown-item" role="button">Show All Code</a>

- <a href="javascript:void(0)" id="quarto-hide-all-code" class="dropdown-item" role="button">Hide All Code</a>

-

  ------------------------------------------------------------------------

- <a href="javascript:void(0)" id="quarto-view-source" class="dropdown-item" role="button">View Source</a>

This is an example of using qmd as the source document.

## Evaluated Python code chunk, with a plot {.anchored anchor-id="evaluated-python-code-chunk-with-a-plot"}

Code

``` {.sourceCode .python .code-with-copy}
import numpy as np
x = np.random.normal(size=100)
import matplotlib.pyplot as plt
plt.hist(x)
plt.show()
np.mean(x)
```

<figure class="figure">
<p><img src="unit1_files/figure-html/cell-2-output-1.png" class="figure-img" width="566" height="411" /></p>
</figure>

    0.15857207845004595

## <span class="math inline">\$\\LaTeX\$</span> {.anchored anchor-id="latex"}

<span class="math display">\\$$ \\theta = \\int\_0^\\infty f(x,\\theta)d\\theta \\$$</span>

## <span class="math inline">\$\\LaTeX\$</span> macro {.anchored anchor-id="latex-macro"}

> **Warning**: need to look back at this as having `include-before-body` in the yaml causes extra space at top of page.

<span class="math display">\\$$ A = X \\trans Y \\$$</span>

## Styled div via direct html {.anchored anchor-id="styled-div-via-direct-html"}

This content can be styled via the border class.

## A callout {.anchored anchor-id="a-callout"}

Tip with Title

This is an example of a callout with a title.

## Tabset {.anchored anchor-id="tabset"}

- <span id="tabset-1-1-tab" class="nav-link active" bs-toggle="tab" bs-target="#tabset-1-1" role="tab" aria-controls="tabset-1-1" aria-selected="true">R</span>
- <span id="tabset-1-2-tab" class="nav-link" bs-toggle="tab" bs-target="#tabset-1-2" role="tab" aria-controls="tabset-1-2" aria-selected="false">Python</span>

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

    Fizz

---

[Up: contents](../index.md)
