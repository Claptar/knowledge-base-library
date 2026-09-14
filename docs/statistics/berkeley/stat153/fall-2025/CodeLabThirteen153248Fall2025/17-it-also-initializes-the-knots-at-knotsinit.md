---
title: It also initializes the knots at knotsinit
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# It also initializes the knots at knotsinit

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

The following code runs the optimizer. The only thing that is different from the piecewise linear regression model is the loss function.

```python
optimizer = optim.Adam(md_PiecewiseLinear.parameters(), lr = 0.01)

---

[← This code creates an instance of our custom neural network class](16-this-code-creates-an-instance-of-our-custom-neural-network-c.md) · [Up: contents](index.md) · [the above line tells Python to create an Adam optimizer that will update all parameters →](18-the-above-line-tells-python-to-create-an-adam-optimizer-that.md)
