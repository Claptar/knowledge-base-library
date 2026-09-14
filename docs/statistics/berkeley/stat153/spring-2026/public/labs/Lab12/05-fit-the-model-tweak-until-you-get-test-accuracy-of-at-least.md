---
title: Fit the model! Tweak until you get test accuracy of at least 80%
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fit the model! Tweak until you get test accuracy of at least 80%

**Source:** [`public/labs/Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Try changing `optimizer = torch.optim.SGD(model.parameters(), lr=.005)` with higher learning rate `lr`, try adding more epochs, switch optimizer from SGD to AdamW - `torch.optim.AdamW(model.parameters(), lr=1e-3)`.

```python
# Main training loop. One iteration of the outer for-loop = one epoch.
# scheduler.step() is called once per epoch to advance the learning-rate schedule.
n_epoch = 2

for epoch in range(n_epoch):
    train_one_epoch(model)
    test(model)
    scheduler.step()
```

---

[← Write the training and test functions](04-write-the-training-and-test-functions.md) · [Up: contents](index.md) · [Create contingency matrix to show performance →](06-create-contingency-matrix-to-show-performance.md)
