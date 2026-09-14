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

Now we shall run the optimization algorithm which starts with these initial estimates, and then iteratively updates them. The crucial hyperparameter  in the optimization algorithm is the learning rate (denoted by lr in the code below). This controls how much to adjust the parameters with respect to the gradient during each step of optimization. A smaller value means smaller steps, which can lead to more stable convergence but possibly slower training. A larger learning rate would update the parameters more aggressively, which might speed up training but risks overshooting the minimum.

```python

---

[← This code creates an instance of our custom neural network class](04-this-code-creates-an-instance-of-our-custom-neural-network-c.md) · [Up: contents](index.md) · [Define an optimizer →](06-define-an-optimizer.md)
