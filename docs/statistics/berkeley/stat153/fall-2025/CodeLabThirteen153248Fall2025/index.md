---
title: More on model fitting using PyTorch
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# More on model fitting using PyTorch

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Split into 25 sections.

1. [More on model fitting using PyTorch](01-more-on-model-fitting-using-pytorch.md)
2. [First fix the number of knots](02-first-fix-the-number-of-knots.md)
3. [Define a model](03-define-a-model.md)
4. [This code creates an instance of our custom neural network class](04-this-code-creates-an-instance-of-our-custom-neural-network-c.md)
5. [It also initializes the knots at knotsinit](05-it-also-initializes-the-knots-at-knotsinit.md)
6. [Define an optimizer](06-define-an-optimizer.md)
7. [https://docs.pytorch.org/docs/stable/optim.html](07-https-docs-pytorch-org-docs-stable-optim-html.md)
8. [try lr = 0.01, 0.1 and 1](08-try-lr-0-01-0-1-and-1.md)
9. [Define a loss function](09-define-a-loss-function.md)
10. [CodeLabThirteen153248Fall2025 Part 10 —](10-codelabthirteen153248fall2025-part-10.md)
11. [but is detached from the computation graph.](11-but-is-detached-from-the-computation-graph.md)
12. [First fix the number of knots](12-first-fix-the-number-of-knots.md)
13. [the following is the true alphat function](13-the-following-is-the-true-alphat-function.md)
14. [Generating Data using the above smooth function](14-generating-data-using-the-above-smooth-function.md)
15. [we rescale x but not y](15-we-rescale-x-but-not-y.md)
16. [This code creates an instance of our custom neural network class](16-this-code-creates-an-instance-of-our-custom-neural-network-c.md)
17. [It also initializes the knots at knotsinit](17-it-also-initializes-the-knots-at-knotsinit.md)
18. [the above line tells Python to create an Adam optimizer that will update all parameters](18-the-above-line-tells-python-to-create-an-adam-optimizer-that.md)
19. [of mdPiecewiseLinear during training, using a learning rate of 0.01.](19-of-mdpiecewiselinear-during-training-using-a-learning-rate-o.md)
20. [Run this code a few times to be sure of convergence.](20-run-this-code-a-few-times-to-be-sure-of-convergence.md)
21. [Run this code a few times to be sure of convergence.](21-run-this-code-a-few-times-to-be-sure-of-convergence.md)
22. [Run this code a few times to be sure of convergence.](22-run-this-code-a-few-times-to-be-sure-of-convergence.md)
23. [Find peaks](23-find-peaks.md)
24. [these knots are chosen to be roughly near the peaks and troughs](24-these-knots-are-chosen-to-be-roughly-near-the-peaks-and-trou.md)
25. [Run this code a few times to be sure of convergence.](25-run-this-code-a-few-times-to-be-sure-of-convergence.md)

---

[Up: contents](../index.md)
