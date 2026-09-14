---
title: Dow Jones Industrial Average Data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dow Jones Industrial Average Data

**Source:** [`public/labs/Lab1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import matplotlib.dates as mdates
locator = mdates.AutoDateLocator(minticks=7, maxticks=10)

djia_data = astsa.load_djia()
# Calculate the return
djia_return = np.diff(np.log(djia_data['Close']))

plt.figure()
plt.subplot(2,1,1)
plt.plot(djia_data['Date'],djia_data['Close'])
plt.gca().xaxis.set_major_locator(locator)
plt.gca().set_xticklabels([]) # Hide labels since they're the same for both subplots
plt.ylabel('Returns')
plt.gca().grid(True)

plt.subplot(2,1,2)
plt.plot(djia_data['Date'][1:],djia_return)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().tick_params(axis='x', labelrotation=45)
plt.ylabel('Returns')
plt.gca().grid()

plt.tight_layout()
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [fMRI data →](03-fmri-data.md)
