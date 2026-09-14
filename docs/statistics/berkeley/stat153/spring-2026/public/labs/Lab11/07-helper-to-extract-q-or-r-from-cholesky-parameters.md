---
title: Helper to extract Q or R from Cholesky parameters
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Helper to extract Q or R from Cholesky parameters

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def extract_chol_matrix(params, start_idx):
    L = np.zeros((3, 3))
    idx = start_idx
    for i in range(3):
        for j in range(i + 1):
            L[i, j] = np.real(params[idx]); idx += 1
    return L @ L.T, idx

params = res.params
Phi_hat = np.real(params[0:9]).reshape(3, 3)
Q_hat, next_idx = extract_chol_matrix(params, 9)
R_hat, _ = extract_chol_matrix(params, next_idx)

marker_names = ['WBC', 'PLT', 'HCT']

print("Estimated Phi:")
print(pd.DataFrame(Phi_hat, index=marker_names, columns=marker_names).round(3))
print(f"\nEstimated Q:")
print(pd.DataFrame(Q_hat, index=marker_names, columns=marker_names).round(4))
print(f"\nEstimated R:")
print(pd.DataFrame(R_hat, index=marker_names, columns=marker_names).round(4))
```

### Interpreting $\hat{\Phi}$

Each row of $\Phi$ is a regression: today's marker value as a function of yesterday's three markers.

**Diagonal entries (persistence):**
- $\phi_{11} \approx 0.95$: log(WBC) is highly persistent — today's value is close to yesterday's
- $\phi_{22} \approx 0.91$: log(PLT) is slightly less persistent
- $\phi_{33} \approx 0.89$: HCT is the least persistent of the three

All diagonal entries are close to 1 but strictly less, consistent with mean-reverting biological processes. A value of exactly 1 would imply a random walk (no mean reversion).

**Off-diagonal entries (cross-coupling):**
- $\phi_{21} \approx 0.07$: yesterday's WBC slightly predicts today's PLT (consistent with WBC recovery preceding platelet recovery during engraftment)
- $\phi_{31} \approx -0.79$ and $\phi_{32} \approx 1.21$: HCT is strongly coupled to both WBC and PLT — its dynamics are driven more by the other markers than by its own history

## Plot the Kalman filter and smoother estimates

The Kalman smoother gives us $x_t^n = E[x_t \mid y_{1:n}]$, which is the best estimate of each marker at every time point using the entire dataset. This fills in the missing values optimally. We can also compare this to the Kalman filter, which uses only the forward step and cannot integrate data from the future.

```python
from ipywidgets import Checkbox, Layout, interactive_output, VBox, HBox
from IPython.display import display

def contiguous_regions(mask):
    """Find contiguous True regions in a boolean array."""
    regions = []
    start = None
    for i, val in enumerate(mask):
        if val and start is None:
            start = i
        elif not val and start is not None:
            regions.append((start, i - 1))
            start = None
    if start is not None:
        regions.append((start, len(mask) - 1))
    return regions

---

[← Fit the model](06-fit-the-model.md) · [Up: contents](index.md) · [Extract filtered states and standard errors →](08-extract-filtered-states-and-standard-errors.md)
