---
title: fMRI data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# fMRI data

**Source:** [`public/labs/Lab1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
fmri_data = astsa.load_fmri1()

print(fmri_data)

plt.subplot(3,1,1)
plt.plot(fmri_data['cort1'])
plt.plot(fmri_data['cort2'])
plt.ylabel('BOLD')

plt.subplot(3,1,2)
plt.plot(fmri_data['thal1'])
plt.plot(fmri_data['thal2'])
plt.ylabel('BOLD')

plt.subplot(3,1,3)
plt.plot(fmri_data['cere1'])
plt.plot(fmri_data['cere2'])
plt.xlabel('Time (s)')
plt.ylabel('BOLD')

plt.tight_layout()
```

---

[← Dow Jones Industrial Average Data](02-dow-jones-industrial-average-data.md) · [Up: contents](index.md) · [White Noise →](04-white-noise.md)
