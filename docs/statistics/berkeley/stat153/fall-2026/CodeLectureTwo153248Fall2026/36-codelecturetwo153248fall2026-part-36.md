---
title: CodeLectureTwo153248Fall2026 Part 36 —
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# CodeLectureTwo153248Fall2026 Part 36 —

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

x = np.arange(1, len(y) + 1)
x_future = np.arange(len(y) + 1, len(y) + r + 1)

plt.figure(figsize=(12, 5))

plt.plot(x, y, label="Observed data")
plt.plot(x, y_fitted, label="Fitted values")
plt.plot(x_future, y_future, label="Future predictions")

plt.xlabel("Time (months)")
plt.ylabel("Population (thousands)")
plt.title("Model 7: Observed Data, Fitted Values, and Predictions")
plt.legend()

plt.show()

---

[← Plot population: data, fitted values, predictions](35-plot-population-data-fitted-values-predictions.md) · [Up: contents](index.md) · [CodeLectureTwo153248Fall2026 Part 37 — →](37-codelecturetwo153248fall2026-part-37.md)
