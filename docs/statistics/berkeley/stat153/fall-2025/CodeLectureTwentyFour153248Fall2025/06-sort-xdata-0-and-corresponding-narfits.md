---
title: Sort xdata[:,0] and corresponding narfits
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sort xdata[:,0] and corresponding narfits

**Source:** [`CodeLectureTwentyFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

sorted_indices = torch.argsort(x_data[:,0])
x_sorted = x_data[:,0][sorted_indices]
nar_fits_sorted = nar_fits[sorted_indices]


def g(x):
    return 2 * x / (1 + 0.8 * x**2)

true_g_vals = g(x_sorted.detach().numpy())


plt.plot(x_sorted.detach().numpy(), nar_fits_sorted.detach().numpy(), label = 'Fitted values')
plt.plot(x_sorted.detach().numpy(), true_g_vals, color = 'red', label = 'Actual g values')
plt.title('Plotting fitted values against y_{t-5}')
plt.xlabel('y_{t-5}')
plt.ylabel('Fitted values')
plt.show()
```

```
torch.Size([1445])
torch.Size([1445])
```

*(1 figure omitted — see the original notebook.)*

```python
#Plot y_t against y_{t-5}
plt.scatter(x_data[:,0].detach().numpy(), y_data.detach().numpy(), s = 5)
plt.plot(x_sorted.detach().numpy(), nar_fits_sorted.detach().numpy(), label = 'Fitted values', color = 'black')
plt.plot(x_sorted.detach().numpy(), true_g_vals, color = 'red', label = 'Actual g values')
plt.xlabel('y_{t-5}')
plt.ylabel('y_t')
plt.title('Scatter plot of y_t against y_{t-5}')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Plot the function](05-plot-the-function.md) · [Up: contents](index.md)
