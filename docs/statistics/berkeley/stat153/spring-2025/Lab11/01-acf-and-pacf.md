---
title: ACF and PACF
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ACF and PACF

**Source:** [`Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import pacf
```

Let us illustrate the concepts of ACF and PACF through the sunspots dataset.

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header=None, sep=';')
print(sunspots.head())

y = sunspots.iloc[:, 1].values
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

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))

plot_acf(y, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF of Sunspots Series")

plot_pacf(y, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF of Sunspots Series")

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The sample ACF has an oscillatory pattern, and the sample autocorrelations only become negligible after lag 12 (even though sample autocorrelations at lags 15, 16, 17 also seem nontrivial). This suggests that MA models may not be appropriate for this dataset. The partial PACF clearly has two big spikes at lags 1 and 2, and then mostly small. This suggests that an AR(2) model might be appropriate. One can also consider the sample PACF at lags 7, 8, 9 to be nonnegligible. In this case, we can try to fit AR(9) to the data.

## Calculation of PACF

Let us see how the PACF is calculated. The definition of PACF($h$) is the estimate $\hat{\phi}_h$ of $\phi_h$ when the AR($h$) model is fit to the data.  Let us check if this is indeed the case.

```python
def sample_pacf(y, p_max):
    pautocorr = []
    for p in range(1, p_max + 1):
        armd = AutoReg(y, lags = p).fit() # fitting the AR(p) model
        phi_p = armd.params[-1] # taking the last estimated coefficient
        pautocorr.append(phi_p)
    return pautocorr
```

Let us now compare these values with the values given by an inbuilt function for pacf.

```python
p_max = 50
pacf_vals = sample_pacf(y, p_max)

pacf_vals_sm = pacf(y, nlags=p_max, method='ols') # these pacf values start with the value 1 at lag 0.
print(np.column_stack([pacf_vals, pacf_vals_sm[1:]]))
```

```
[[ 0.81814243  0.81814243]
 [-0.69646032 -0.69646032]
 [-0.14551566 -0.14551566]
 [ 0.01078091  0.01078091]
 [-0.00988486 -0.00988486]
 [ 0.13721057  0.13721057]
 [ 0.20129653  0.20129653]
 [ 0.22159369  0.22159369]
 [ 0.21768779  0.21768779]
 [ 0.01979271  0.01979271]
 [ 0.01220908  0.01220908]
 [-0.01159196 -0.01159196]
 [ 0.00638536  0.00638536]
 [ 0.04363913  0.04363913]
 [-0.05535382 -0.05535382]
 [-0.07389671 -0.07389671]
 [-0.16269894 -0.16269894]
 [-0.12338723 -0.12338723]
 [ 0.05099077  0.05099077]
 [-0.02507587 -0.02507587]
 [ 0.09908343  0.09908343]
 [ 0.01560164  0.01560164]
 [-0.12666585 -0.12666585]
 [-0.07148407 -0.07148407]
 [ 0.00513059  0.00513059]
 [-0.11203047 -0.11203047]
 [ 0.05033772  0.05033772]
 [ 0.07062661  0.07062661]
 [-0.13345508 -0.13345508]
 [-0.0234795  -0.0234795 ]
 [-0.00607123 -0.00607123]
 [-0.01538124 -0.01538124]
 [-0.02963781 -0.02963781]
 [-0.00909349 -0.00909349]
 [-0.01330015 -0.01330015]
 [-0.05143092 -0.05143092]
 [ 0.06104478  0.06104478]
 [-0.00216343 -0.00216343]
 [ 0.02005769  0.02005769]
 [ 0.04261196  0.04261196]
 [-0.02111046 -0.02111046]
 [-0.00650194 -0.00650194]
 [-0.03813196 -0.03813196]
 [-0.00691118 -0.00691118]
 [ 0.05843472  0.05843472]
 [ 0.04757612  0.04757612]
 [ 0.09585197  0.09585197]
 [-0.12695263 -0.12695263]
 [-0.02920994 -0.02920994]
 [-0.03182224 -0.03182224]]
```

See that the two sets of sample pacf values coincide exactly.

---

[Up: contents](index.md) · [Regression and Partial Correlation →](02-regression-and-partial-correlation.md)
