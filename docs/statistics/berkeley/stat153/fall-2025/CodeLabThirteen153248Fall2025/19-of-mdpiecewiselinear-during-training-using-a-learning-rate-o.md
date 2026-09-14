---
title: of mdPiecewiseLinear during training, using a learning rate of 0.01.
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# of mdPiecewiseLinear during training, using a learning rate of 0.01.

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

for epoch in range(20000):
    optimizer.zero_grad()

    y_pred = md_PiecewiseLinear(x_torch)
    #loss = loss_fn(y_pred, y_torch)
    loss = torch.sum( y_pred + (y_torch**2) / 2 * torch.exp(-2 * y_pred) )

    loss.backward() # calulates gradients

    optimizer.step() # updates parameters using gradients

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

---

[← the above line tells Python to create an Adam optimizer that will update all parameters](18-the-above-line-tells-python-to-create-an-adam-optimizer-that.md) · [Up: contents](index.md) · [Run this code a few times to be sure of convergence. →](20-run-this-code-a-few-times-to-be-sure-of-convergence.md)
