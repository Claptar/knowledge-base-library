---
title: this gives \psij, j = 0, \dots, lags-1
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# this gives \psij, j = 0, \dots, lags-1

**Source:** [`CodeLabTen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(np.column_stack([psi_j, ma_infinity]))
```

```
[[ 1.00000000e+00  1.00000000e+00]
 [ 5.00000000e-01  5.00000000e-01]
 [ 3.53525080e-17  0.00000000e+00]
 [-1.25000000e-01 -1.25000000e-01]
 [-6.25000000e-02 -6.25000000e-02]
 [-8.83812699e-18  0.00000000e+00]
 [ 1.56250000e-02  1.56250000e-02]
 [ 7.81250000e-03  7.81250000e-03]
 [ 1.65714881e-18  0.00000000e+00]
 [-1.95312500e-03 -1.95312500e-03]
 [-9.76562500e-04 -9.76562500e-04]
 [-2.76191468e-19  0.00000000e+00]
 [ 2.44140625e-04  2.44140625e-04]
 [ 1.22070313e-04  1.22070312e-04]
 [ 1.68347800e-19  0.00000000e+00]
 [-3.05175781e-05 -3.05175781e-05]
 [-1.52587891e-05 -1.52587891e-05]
 [-6.47323754e-21  0.00000000e+00]
 [ 3.81469727e-06  3.81469727e-06]
 [ 1.90734863e-06  1.90734863e-06]
 [ 9.44013808e-22  0.00000000e+00]
 [-4.76837158e-07 -4.76837158e-07]
 [-2.38418579e-07 -2.38418579e-07]
 [-1.34859115e-22  0.00000000e+00]
 [ 5.96046448e-08  5.96046448e-08]
 [ 2.98023224e-08  2.98023224e-08]
 [ 1.89645631e-23  0.00000000e+00]
 [-7.45058060e-09 -7.45058060e-09]
 [-3.72529030e-09 -3.72529030e-09]
 [-1.02751343e-23  0.00000000e+00]
 [ 9.31322575e-10  9.31322575e-10]
 [ 4.65661287e-10  4.65661287e-10]
 [-5.92975423e-25  0.00000000e+00]
 [-1.16415322e-10 -1.16415322e-10]
 [-5.82076609e-11 -5.82076609e-11]
 [-4.93868831e-26  0.00000000e+00]
 [ 1.45519152e-11  1.45519152e-11]
 [ 7.27595761e-12  7.27595761e-12]
 [ 2.16119618e-26  0.00000000e+00]
 [-1.81898940e-12 -1.81898940e-12]]
```

We can check from the above that the $\psi_j$ calculated by our formula (which we obtained by  using the Backshift method) coincide with the values output by the statsmodels function.

## AR order selection through PACF

Consider the sunspots dataset to which we previously fit the AR(2) model. Now let us use PACF to see if there is another $p$ for which AR($p$) is a better model.

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
print(sunspots.head())

y = sunspots.iloc[:,1].values
n = len(y)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

```
0     1    2  3  4
0  1700.5   8.3 -1.0 -1  1
1  1701.5  18.3 -1.0 -1  1
2  1702.5  26.7 -1.0 -1  1
3  1703.5  38.3 -1.0 -1  1
4  1704.5  60.0 -1.0 -1  1
```

*(1 figure omitted — see the original notebook.)*

The PACF can be plotted using the inbuilt function plot_pacf in statsmodels.

```python
from statsmodels.graphics.tsaplots import plot_pacf

p_max = 40
plot_pacf(y, lags = p_max)
plt.title("Sample PACF of the Sunspots Data")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The partial PACF clearly has two big spikes at lags 1 and 2, and then mostly small. This suggests that an AR(2) model might be appropriate. One can also consider the sample PACF at lags 7, 8, 9 to be nonnegligible. In this case, we can try to fit AR(9) to the data.

### Calculation of PACF

Let us see how the PACF is calculated. The definition of PACF($h$) is the estimate $\hat{\phi}_h$ of $\phi_h$ when the AR($h$) model is fit to the data.  Let us check if this is indeed the case.

```python
def sample_pacf(dt, p_max):
    pautocorr = []
    for p in range(1, p_max + 1):
        armd = AutoReg(dt, lags = p).fit() # fitting the AR(p) model
        phi_p = armd.params[-1] # taking the last estimated coefficient
        pautocorr.append(phi_p)
    return pautocorr
```

Let us now compare these values with the values given by an inbuilt function for pacf (to verify that they indeed match).

```python
from statsmodels.tsa.stattools import pacf

p_max = 50
pacf_vals = sample_pacf(y, p_max)
pacf_vals_sm = pacf(y, nlags=p_max, method = 'ols')

---

[← (since we are dealing with a pure AR process, there is no theta coefficient)](03-since-we-are-dealing-with-a-pure-ar-process-there-is-no-thet.md) · [Up: contents](index.md) · [these pacf values start with the value 1 at lag 0. →](05-these-pacf-values-start-with-the-value-1-at-lag-0.md)
