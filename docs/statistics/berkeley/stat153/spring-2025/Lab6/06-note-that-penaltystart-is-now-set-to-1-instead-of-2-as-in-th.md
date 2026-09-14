---
title: note that penaltystart is now set to 1 (instead of 2 as in the model used in
  class)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab6.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab6.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# note that penaltystart is now set to 1 (instead of 2 as in the model used in class)

**Source:** [`Lab6.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab6.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def solve_ridge(X, y, lambda_val, penalty_start = 1):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.sum_squares(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

```python

---

[← It is very easy to create the above matrix in python](05-it-is-very-easy-to-create-the-above-matrix-in-python.md) · [Up: contents](index.md) · [note that penaltystart is now set to 1 (instead of 2 as in the model used in class) →](07-note-that-penaltystart-is-now-set-to-1-instead-of-2-as-in-th.md)
