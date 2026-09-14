---
title: Plot observed data, fitted values, and future predictions
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot observed data, fitted values, and future predictions

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize=(6, 4))

plt.plot(x, y, label="Observed data")
plt.plot(x, y_fitted, label="Fitted values")
plt.plot(x_future, y_future, label="Future predictions")

plt.xlabel("Time (months)")
plt.ylabel("Population (thousands)")
plt.title("Model 2: Log-Linear Trend")
plt.legend()

plt.show()

---

[← Convert back to population scale](07-convert-back-to-population-scale.md) · [Up: contents](index.md) · [Prediction 168 months ahead →](09-prediction-168-months-ahead.md)
