---
title: Unit 03 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit3.html
source_file: sources/berkeley-stat210a/fall-2025/units/unit3.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Unit 03 —

**Source:** [`units/unit3.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/unit3.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

\$\$ \\newcommand{\\trans}{^\\mathsf{T}} \\newcommand{\\eps}{\\epsilon} \$\$

# Unit 3: More {#unit-3-more .title}

Code

- <a href="javascript:void(0)" id="quarto-show-all-code" class="dropdown-item" role="button">Show All Code</a>

- <a href="javascript:void(0)" id="quarto-hide-all-code" class="dropdown-item" role="button">Hide All Code</a>

-

  ------------------------------------------------------------------------

- <a href="javascript:void(0)" id="quarto-view-source" class="dropdown-item" role="button">View Source</a>

This is an example of using qmd as the source document with pdf as one target. I’ve taken out the qmd stuff that doesn’t seem to render to pdf.

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
<p><img src="unit3_files/figure-html/cell-2-output-1.png" class="figure-img" width="566" height="411" /></p>
</figure>

    0.026995820674692316

## LaTeX {.anchored anchor-id="latex"}

<span class="math display">\\$$ \\theta = \\int\_0^\\infty f(x,\\theta)d\\theta \\$$</span>

## LaTeX macro {.anchored anchor-id="latex-macro"}

> **Warning**: need to look back at this as having `include-before-body` in the yaml causes extra space at top of page.

<span class="math display">\\$$ A = X \\trans Y \\$$</span>

---

[Up: contents](../index.md)
