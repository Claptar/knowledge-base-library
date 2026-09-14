---
title: Unit 02 —
source: https://github.com/berkeley-stat230a/spring-2025/blob/e876671afc2665ae79c2a5263b03c3377f6e2836/unit2.ipynb
source_file: sources/berkeley-stat230a/spring-2025/unit2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Unit 02 —

**Source:** [`unit2.ipynb`](https://github.com/berkeley-stat230a/spring-2025/blob/e876671afc2665ae79c2a5263b03c3377f6e2836/unit2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: "Unit 2: Notebook"
math:
  '\trans': '^\mathsf{T}'
  '\eps': '\epsilon'
---

:::{tip}
Code cells in this notebook are executed when the file is prepared with Jupyter Notebook or Lab. They may also be executed live with JupyterLite! (although the feature is in development)
:::

This is the mean of some random numbers using numpy.

```python
import numpy as np
x = np.random.normal(size=100)
import matplotlib.pyplot as plt
plt.hist(x)
plt.show()
np.mean(x)
```

```
-0.1701530565922348
```

*(1 figure omitted — see the original notebook.)*

$$
\theta = \int_0^\infty f(x,\theta)d\theta
$$

Use a $\LaTeX$ macro.

$$
A = X \trans Y
$$

---

[Up: contents](index.md)
