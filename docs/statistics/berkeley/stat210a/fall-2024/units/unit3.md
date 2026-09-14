---
title: 'Unit 3: More'
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/units/unit3.qmd
source_file: sources/berkeley-stat210a/fall-2024/units/unit3.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unit 3: More

**Source:** [`units/unit3.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/units/unit3.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

This is an example of using qmd as the source document with pdf as one target. I've taken out the qmd stuff that doesn't seem to render to pdf.

## Evaluated Python code chunk, with a plot

```python
import numpy as np
x = np.random.normal(size=100)
import matplotlib.pyplot as plt
plt.hist(x)
plt.show()
np.mean(x)
```


## LaTeX

$$
\theta = \int_0^\infty f(x,\theta)d\theta
$$

## LaTeX macro

> **Warning**: need to look back at this as having `include-before-body` in the yaml causes extra space at top of page.

$$
A = X \trans Y
$$

---

[Up: contents](../index.md)
