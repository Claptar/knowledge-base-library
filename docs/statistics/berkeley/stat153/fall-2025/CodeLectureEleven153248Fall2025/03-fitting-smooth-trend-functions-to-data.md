---
title: Fitting Smooth Trend Functions to Data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Fitting Smooth Trend Functions to Data

These models and the corresponding Ridge and LASSO estimators are useful for fitting trend functions to data.

The following two datasets are from [NOAA climate at a glance](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/tavg/land_ocean/1/1/1850-2025). They contain temperature anomalies for the months of January and June (for each year from 1850 to 2025). Anomalies are in celsius and are with respect to the 1901-2000 average.

```python
temp_jan = pd.read_csv('TempAnomalies_January.csv', skiprows=4)
temp_june = pd.read_csv('TempAnomalies_June.csv', skiprows=3)
print(temp_jan)
y_jan = temp_jan['Anomaly']
y_june = temp_june['Anomaly']
plt.plot(temp_jan['Year'], y_jan, label='January')
plt.plot(temp_jan['Year'], y_june, label='June')
plt.legend()
plt.xlabel('year')
plt.ylabel('Celsius')
plt.title('Temperature anomalies (from 1901-2000 average) for January')
plt.show()
```

```
Year  Anomaly
0    1850    -0.46
1    1851    -0.17
2    1852    -0.02
3    1853    -0.12
4    1854    -0.28
..    ...      ...
171  2021     0.83
172  2022     0.92
173  2023     0.89
174  2024     1.30
175  2025     1.33

[176 rows x 2 columns]
```

*(1 figure omitted — see the original notebook.)*

We shall fit a trend function to each of these two datasets. The first step is to create the $X$ matrix.

```python
n = len(y_jan) #both datasets have the same length, so the X matrix will be the same for both
x = np.arange(1, n+1)
Xfull = np.column_stack([np.ones(n), x-1])
for i in range(n-2):
    c = i+2
    xc = ((x > c).astype(float))*(x-c)
    Xfull = np.column_stack([Xfull, xc])
print(Xfull)
```

```
[[  1.   0.  -0. ...  -0.  -0.  -0.]
 [  1.   1.   0. ...  -0.  -0.  -0.]
 [  1.   2.   1. ...  -0.  -0.  -0.]
 ...
 [  1. 173. 172. ...   1.   0.  -0.]
 [  1. 174. 173. ...   2.   1.   0.]
 [  1. 175. 174. ...   3.   2.   1.]]
```

The ridge regression estimate is computed below. Start with some standard choice of $\lambda$ (e.g., $\lambda = 1$) and then increase or decrease it by factors of 10 until you get a fit that is visually nice (smooth while capturing patterns in the data).

```python
b_ridge_jan = solve_ridge(Xfull, y_jan, lambda_val = 1000)
ridge_fitted_jan = np.dot(Xfull, b_ridge_jan)

b_ridge_june = solve_ridge(Xfull, y_june, lambda_val = 1000)
ridge_fitted_june = np.dot(Xfull, b_ridge_june)

plt.figure(figsize = (10, 6))
#plt.plot(temp_jan['Year'], y_jan, color = 'lightgray')
plt.plot(temp_jan['Year'], ridge_fitted_jan, color = 'red', label = 'January Ridge')
plt.plot(temp_jan['Year'], ridge_fitted_june, color = 'blue', label = 'June Ridge')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We repeat the exercise with LASSO below.

```python
b_lasso_jan = solve_lasso(Xfull, y_jan, lambda_val = 10)
lasso_fitted_jan = np.dot(Xfull, b_lasso_jan)

b_lasso_june = solve_lasso(Xfull, y_june, lambda_val = 10)
lasso_fitted_june = np.dot(Xfull, b_lasso_june)

plt.figure(figsize = (10, 6))
#plt.plot(temp_jan['Year'], y, color = 'lightgray')
plt.plot(temp_jan['Year'], lasso_fitted_jan, color = 'red', label = 'January LASSO')
plt.plot(temp_jan['Year'], lasso_fitted_june, color = 'blue', label = 'June LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Ridge and LASSO regularized estimation](02-ridge-and-lasso-regularized-estimation.md) · [Up: contents](index.md) · Cross-validation for picking $\lambda$ →
