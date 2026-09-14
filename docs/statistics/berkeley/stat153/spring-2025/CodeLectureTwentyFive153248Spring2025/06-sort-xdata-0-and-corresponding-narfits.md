---
title: Sort xdata[:,0] and corresponding narfits
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFive153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyFive153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sort xdata[:,0] and corresponding narfits

**Source:** [`CodeLectureTwentyFive153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFive153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

sorted_indices = torch.argsort(x_data[:,0])
x_sorted = x_data[:,0][sorted_indices]
nar_fits_sorted = nar_fits[sorted_indices]


def g(x):
    return 2 * x / (1 + 0.8 * x**2)

true_g_vals = g(x_sorted.detach().numpy())

plt.figure(figsize=(12, 6))
plt.plot(x_sorted.detach().numpy(), nar_fits_sorted.detach().numpy(), label = 'Fitted values')
plt.plot(x_sorted.detach().numpy(), true_g_vals, color = 'red', label = 'Actual g values')
plt.title('Plotting fitted values against y_{t-p}')
plt.xlabel('y_{t-p}')
plt.ylabel('Fitted values')
plt.show()
```

```
torch.Size([1430])
torch.Size([1430])
```

*(1 figure omitted — see the original notebook.)*

---

[← Sort xdata[:,0] and corresponding narfits](05-sort-xdata-0-and-corresponding-narfits.md) · [Up: contents](index.md)
