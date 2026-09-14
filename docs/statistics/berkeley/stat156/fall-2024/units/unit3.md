---
title: 'Unit 3: More'
source: https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/units/unit3.qmd
source_file: sources/berkeley-stat156/fall-2024/units/unit3.qmd
licence: CC BY-NC 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unit 3: More

**Source:** [`units/unit3.qmd`](https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/units/unit3.qmd) · **Licence:** CC BY-NC 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

[UNDER CONSTRUCTION]

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

> **Warning**: having `include-before-body` in the yaml header of this file, as seemingly needed to enable macros, causes extra space at top of page.

$$
A = X \trans Y
$$

---

[Up: contents](../index.md)
