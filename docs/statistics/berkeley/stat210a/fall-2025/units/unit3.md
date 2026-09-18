---
title: Unit 03 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit3.html
source_file: sources/berkeley-stat210a/fall-2025/units/unit3.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/unit3.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit3.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Unit 03 —

$$ \\newcommand{\\trans}{^\\mathsf{T}} \\newcommand{\\eps}{\\epsilon} $\$

## Unit 3: More {#unit-3-more .title}

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

-

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

This is an example of using qmd as the source document with pdf as one target. I’ve taken out the qmd stuff that doesn’t seem to render to pdf.

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

![](https://raw.githubusercontent.com/berkeley-stat210a/fall-2025/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit3_files/figure-html/cell-2-output-1.png)

```
0.026995820674692316
```

### LaTeX {.anchored anchor-id="latex"}

$$
\theta = \int_0^\infty f(x,\theta)d\theta
$$

### LaTeX macro {.anchored anchor-id="latex-macro"}

> **Warning**: need to look back at this as having `include-before-body` in the yaml causes extra space at top of page.

$$
A = X \trans Y
\$\$

---

[Up: contents](../index.md)
