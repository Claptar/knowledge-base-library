---
title: Display results
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Display results

**Source:** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print("AR(4) coefficients (on original data):")
print(f"a1 = {a1:.4f}, a2 = {a2:.4f}, a3 = {a3:.4f}, a4 = {a4:.4f}\n")

print("Roots of the characteristic polynomial:")
for i, r in enumerate(roots, 1):
    print(f"Root {i}: {r:.4f},  Modulus: {moduli[i-1]:.4f}")

---

[← Characteristic polynomial: 1 - a1z - a2z^2 - a3z^3 - a4z^4 = 0](07-characteristic-polynomial-1---a1z---a2z-2---a3z-3---a4z-4-0.md) · [Up: contents](index.md) · [Check for stationarity →](09-check-for-stationarity.md)
