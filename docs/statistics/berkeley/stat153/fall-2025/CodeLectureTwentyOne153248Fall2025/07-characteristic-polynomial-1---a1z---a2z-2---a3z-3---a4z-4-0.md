---
title: 'Characteristic polynomial: 1 - a1z - a2z^2 - a3z^3 - a4z^4 = 0'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Characteristic polynomial: 1 - a1z - a2z^2 - a3z^3 - a4z^4 = 0

**Source:** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

coeffs = [1, -a1, -a2, -a3, -a4]
roots = np.roots(coeffs)
moduli = np.abs(roots)

---

[← Convert differenced AR(3) model to AR(4) model for the original data](06-convert-differenced-ar-3-model-to-ar-4-model-for-the-origina.md) · [Up: contents](index.md) · [Display results →](08-display-results.md)
