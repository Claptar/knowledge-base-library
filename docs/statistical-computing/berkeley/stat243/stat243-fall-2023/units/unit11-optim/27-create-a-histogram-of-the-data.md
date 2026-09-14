---
title: Create a histogram of the data
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Create a histogram of the data

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(y, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Precipitation (inches)')
plt.ylabel('Frequency')
plt.title('Histogram of All Data')

plt.subplot(1, 2, 2)
plt.hist(y[y > thresh], bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Precipitation (inches)')
plt.ylabel('Frequency')
plt.title(f'Histogram of Wet Days (Precip > {np.round(thresh,2)} inches)')
plt.tight_layout()
plt.show()

---

[← Arbitrarily bad starting values](26-arbitrarily-bad-starting-values.md) · [Up: contents](index.md) · [Define objective (negative log-likelihood) function →](28-define-objective-negative-log-likelihood-function.md)
