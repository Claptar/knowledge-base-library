---
title: Fitting AR(2) to the sunspots dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureEighteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureEighteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fitting AR(2) to the sunspots dataset

**Source:** [`CodeLectureEighteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureEighteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To fit an AR(p) model, we can use the function AutoReg from statsmodels. This implements the conditional MLE method, and gives frequentist standard errors based on the z-score.

```python
armod_sm = AutoReg(y, lags = 2, trend = 'c').fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  325
Model:                     AutoReg(2)   Log Likelihood               -1505.524
Method:               Conditional MLE   S.D. of innovations             25.588
Date:                Tue, 01 Apr 2025   AIC                           3019.048
Time:                        23:13:59   BIC                           3034.159
Sample:                             2   HQIC                          3025.080
                                  325
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         24.4561      2.372     10.308      0.000      19.806      29.106
y.L1           1.3880      0.040     34.685      0.000       1.310       1.466
y.L2          -0.6965      0.040    -17.423      0.000      -0.775      -0.618
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9965           -0.6655j            1.1983           -0.0937
AR.2            0.9965           +0.6655j            1.1983            0.0937
-----------------------------------------------------------------------------
```

Alternatively, one can simply create $y$ and $X$ and run the usual OLS. This inference method is also valid and can be seen as the result of Bayesian analysis.

```python
p = 2
n = len(y)
yreg = y[p:] #these are the response values in the autoregression
Xmat = np.ones((n-p, 1)) #this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = y[p-j : n-j].reshape(-1, 1)
    Xmat = np.column_stack([Xmat, col])

armod = sm.OLS(yreg, Xmat).fit()
print(armod.params)
print(armod.summary())
sighat = np.sqrt(np.mean(armod.resid ** 2)) #note that this mean is taken over n-p observations
resdf = n - 2*p - 1
sigols = np.sqrt((np.sum(armod.resid ** 2))/resdf)
print(sighat, sigols)
```

```
[24.45610705  1.38803272 -0.69646032]
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.829
Model:                            OLS   Adj. R-squared:                  0.828
Method:                 Least Squares   F-statistic:                     774.7
Date:                Tue, 01 Apr 2025   Prob (F-statistic):          2.25e-123
Time:                        23:14:00   Log-Likelihood:                -1505.5
No. Observations:                 323   AIC:                             3017.
Df Residuals:                     320   BIC:                             3028.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         24.4561      2.384     10.260      0.000      19.767      29.146
x1             1.3880      0.040     34.524      0.000       1.309       1.467
x2            -0.6965      0.040    -17.342      0.000      -0.775      -0.617
==============================================================================
Omnibus:                       33.173   Durbin-Watson:                   2.200
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               50.565
Skew:                           0.663   Prob(JB):                     1.05e-11
Kurtosis:                       4.414   Cond. No.                         231.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
25.588082517109108 25.70774684491223
```

Here are some observations comparing the above two outputs:
1. The parameter estimates are exactly the same.
2. The regression summary gives t-scores corresponding to each parameter estimate while the AutoReg summary only gives z-scores
3. The standard errors are slightly different.

The standard errors given by the regression summary correspond to the square roots of the diagonal entries of:
\begin{equation*}
   \hat{\sigma}^2 (X^T X)^{-1} ~~~ \text{ where } \hat{\sigma}^2 = \sqrt{\frac{\|Y - X \hat{\beta}\|^2}{n-2p-1}}
\end{equation*}
while the standard errors reported by AutoReg summary correspond to the square roots of the diagonal entries of:
\begin{equation*}
   \hat{\sigma}_{\text{MLE}}^2 (X^T X)^{-1} ~~~ \text{ where } \hat{\sigma}_{\text{MLE}}^2 = \sqrt{\frac{\|Y - X \hat{\beta}\|^2}{n-p}}
\end{equation*}

```python
covmat = (sighat ** 2) * np.linalg.inv(np.dot(Xmat.T, Xmat))
covmat_ols = (sigols ** 2) * np.linalg.inv(np.dot(Xmat.T, Xmat))
print(np.sqrt(np.diag(covmat)))
print(np.sqrt(np.diag(covmat_ols)))
print(armod_sm.bse)
print(armod.bse)
```

```
[2.37245465 0.04001781 0.03997354]
[2.38354959 0.04020495 0.04016048]
[2.37245465 0.04001781 0.03997354]
[2.38354959 0.04020495 0.04016048]
```

Point predictions for future observations can be obtained by running the recursions discussed in class. One can also obtain predictions from the AutoReg object. The following code verifies that both these prediction methods lead to the same output.

```python
#Predictions
k = 100
yhat = np.concatenate([y, np.full(k, -9999)]) #extend data by k placeholder values
phi_vals = armod.params
for i in range(1, k+1):
    ans = phi_vals[0]
    for j in range(1, p+1):
        ans += phi_vals[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues = yhat[n:]

#Predictions using Autoreg:
predvalues_sm = armod_sm.predict(start = n, end = n+k-1)

#Check that both predictions are identical:
print(np.column_stack([predvalues, predvalues_sm]))
```

```
[[151.77899784 151.77899784]
 [127.38790987 127.38790987]
 [ 95.56664388  95.56664388]
 [ 68.38511059  68.38511059]
 [ 52.81850228  52.81850228]
 [ 50.14240008  50.14240008]
 [ 57.26940772  57.26940772]
 [ 69.0257265   69.0257265 ]
 [ 80.38020354  80.38020354]
 [ 87.9527796   87.9527796 ]
 [ 90.55582018  90.55582018]
 [ 88.89492689  88.89492689]
 [ 84.7766382   84.7766382 ]
 [ 80.21706503  80.21706503]
 [ 76.75645296  76.75645296]
 [ 75.128572    75.128572  ]
 [ 75.27919896  75.27919896]
 [ 76.6220286   76.6220286 ]
 [ 78.38101438  78.38101438]
 [ 79.88731663  79.88731663]
 [ 80.75304962  80.75304962]
 [ 80.90563559  80.90563559]
 [ 80.51448123  80.51448123]
 [ 79.86527611  79.86527611]
 [ 79.23658165  79.23658165]
 [ 78.81607878  78.81607878]
 [ 78.67026779  78.67026779]
 [ 78.76074092  78.76074092]
 [ 78.98787216  78.98787216]
 [ 79.24012681  79.24012681]
 [ 79.43207661  79.43207661]
 [ 79.52282387  79.52282387]
 [ 79.51509861  79.51509861]
 [ 79.44117383  79.44117383]
 [ 79.34394415  79.34394415]
 [ 79.26047186  79.26047186]
 [ 79.2123262   79.2123262 ]
 [ 79.20363358  79.20363358]
 [ 79.22509949  79.22509949]
 [ 79.26094894  79.26094894]
 [ 79.29575899  79.29575899]
 [ 79.31910876  79.31910876]
 [ 79.32727519  79.32727519]
 [ 79.32234827  79.32234827]
 [ 79.30982195  79.30982195]
 [ 79.29586641  79.29586641]
 [ 79.28521975  79.28521975]
 [ 79.28016132  79.28016132]
 [ 79.28055503  79.28055503]
 [ 79.2846245   79.2846245 ]
 [ 79.28999886  79.28999886]
 [ 79.29462443  79.29462443]
 [ 79.29730183  79.29730183]
 [ 79.29779663  79.29779663]
 [ 79.29661873  79.29661873]
 [ 79.29463915  79.29463915]
 [ 79.29271179  79.29271179]
 [ 79.29141526  79.29141526]
 [ 79.29095795  79.29095795]
 [ 79.29122618  79.29122618]
 [ 79.29191698  79.29191698]
 [ 79.29268904  79.29268904]
 [ 79.29327955  79.29327955]
 [ 79.2935615   79.2935615 ]
 [ 79.29354158  79.29354158]
 [ 79.29331757  79.29331757]
 [ 79.29302051  79.29302051]
 [ 79.29276419  79.29276419]
 [ 79.29261531  79.29261531]
 [ 79.29258716  79.29258716]
 [ 79.29265179  79.29265179]
 [ 79.2927611   79.2927611 ]
 [ 79.29286781  79.29286781]
 [ 79.2929398   79.2929398 ]
 [ 79.29296541  79.29296541]
 [ 79.29295081  79.29295081]
 [ 79.29291272  79.29291272]
 [ 79.29287     79.29287   ]
 [ 79.29283725  79.29283725]
 [ 79.29282154  79.29282154]
 [ 79.29282254  79.29282254]
 [ 79.29283487  79.29283487]
 [ 79.29285129  79.29285129]
 [ 79.29286549  79.29286549]
 [ 79.29287377  79.29287377]
 [ 79.29287537  79.29287537]
 [ 79.29287182  79.29287182]
 [ 79.29286579  79.29286579]
 [ 79.29285988  79.29285988]
 [ 79.29285588  79.29285588]
 [ 79.29285445  79.29285445]
 [ 79.29285524  79.29285524]
 [ 79.29285734  79.29285734]
 [ 79.29285971  79.29285971]
 [ 79.29286152  79.29286152]
 [ 79.2928624   79.2928624 ]
 [ 79.29286235  79.29286235]
 [ 79.29286167  79.29286167]
 [ 79.29286076  79.29286076]
 [ 79.29285998  79.29285998]]
```

---

[Up: contents](index.md) · [DATASET TWO →](02-dataset-two.md)
