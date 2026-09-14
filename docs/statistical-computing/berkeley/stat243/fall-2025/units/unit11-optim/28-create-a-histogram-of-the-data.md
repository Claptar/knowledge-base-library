---
title: Create a histogram of the data
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Create a histogram of the data

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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
plt.show(block=False)

---

[← Arbitrarily bad starting values](27-arbitrarily-bad-starting-values.md) · [Up: contents](index.md) · [Define objective (negative log-likelihood) function →](29-define-objective-negative-log-likelihood-function.md)
