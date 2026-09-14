---
title: '---- Output ----'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ---- Output ----

**Source:** [`CodeLabTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print("Estimated mu:", alphaest[0])
print("Estimated theta:", alphaest[1])
print("Estimated sigma:", sighat)
print("Covariance matrix:\n", covmat)
print("Standard errors:", stderrs)

#The standard errors of mu and theta reported by ARIMA function are:
print("ARIMA standard errors:", md.bse[0:2])
```

```
Estimated mu: 5.009073896055675
Estimated theta: -0.6582279929829957
Estimated sigma: 0.9824318225976606
Covariance matrix:
 [[ 2.84046626e-04 -2.35806811e-06]
 [-2.35806811e-06  1.33611939e-03]]
Standard errors: [0.01685368 0.03655297]
ARIMA standard errors: [0.01689423 0.03682785]
```

It is easy to see that the standard errors obtained by our formula are very close to the standard errors reported by the ARIMA function.

## Varve Dataset from Lecture 21

Let us see if the numbers from the calculations above match with those reported by ARIMA on the varve dataset (which we used in Lecture 21).

```python
varve_data = pd.read_csv("varve.csv")
yraw = varve_data['x']
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

In Lecture 21, we fit the MA(1) model to the differences of logarithms of this dataset.

```python

---

[← this library has functions to calculate first and second derivatives](04-this-library-has-functions-to-calculate-first-and-second-der.md) · [Up: contents](index.md) · [First take logarithms →](06-first-take-logarithms.md)
