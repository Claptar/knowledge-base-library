---
title: How are the Prediction Uncertainties actually calculated?
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEighteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureEighteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# How are the Prediction Uncertainties actually calculated?

**Source:** [`CodeLectureEighteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEighteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We now calculate the prediction standard errors directly using the method described in class. The first step is to fit the AR(p) model and then to obtain estimates of $\phi_0, \dots, \phi_p$ as well as $\sigma$. There are two estimates of $\sigma$ (only difference being the denominators: $n-p$ vs $n-2p-1$).

```python
yreg = ylog_train[p:] #these are the response values in the autoregression
Xmat = np.ones((n_train-p, 1)) #this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = ylog_train[p-j : n_train-j]
    Xmat = np.column_stack([Xmat, col])

armod = sm.OLS(yreg, Xmat).fit()
sighat = np.sqrt(np.mean(armod.resid ** 2)) #note that this mean is taken over n-p observations (this is the MLE for sigma)
resdf = n_train - 2*p - 1
sigols = np.sqrt((np.sum(armod.resid ** 2))/resdf)
print(sighat, sigols)
```

```
0.023188223680961746 0.023345433777514888
```

The two estimates of $\sigma$ lead to two values for standard errors.

```python
covmat = (sighat ** 2) * np.linalg.inv(np.dot(Xmat.T, Xmat))
covmat_ols = (sigols ** 2) * np.linalg.inv(np.dot(Xmat.T, Xmat))
print(np.sqrt(np.diag(covmat)))
print(armod_sm.bse)
print(np.sqrt(np.diag(covmat_ols)))
print(armod.bse)
```

```
[0.02770428 0.00248065]
[0.02770428 0.00248065]
[0.02789211 0.00249746]
[0.02789211 0.00249746]
```

The following code computes the prediction standard errors. It uses the matrix recursion method described in class.

```python
sigest = sighat
Gamhat = np.array([[sigest ** 2]])
vkp = np.array([[armod.params[1]]])

for i in range(1, k):
    covterm = Gamhat @ vkp
    varterm = sigest**2 + (vkp.T @ (Gamhat @ vkp))
    Gamhat = np.block([
        [Gamhat,    covterm],
        [covterm.T, varterm ]
    ])
    if i < p:
        new_coef = armod.params[i+1]
        vkp = np.vstack([ [new_coef], vkp ])
    else:
        vkp = np.vstack([ [0], vkp ])
predsd = np.sqrt(np.diag(Gamhat))

#Check that this method produces the same standard errors as those computed by .se_mean:
print(np.column_stack([predsd, fcast_se]))
```

```
[[0.02318822 0.02318822]
 [0.03273842 0.03273842]
 [0.04002943 0.04002943]
 [0.04614511 0.04614511]
 [0.05150606 0.05150606]
 [0.05632841 0.05632841]
 [0.06074075 0.06074075]
 [0.06482705 0.06482705]
 [0.06864572 0.06864572]
 [0.07223936 0.07223936]
 [0.07564022 0.07564022]
 [0.07887337 0.07887337]
 [0.08195881 0.08195881]
 [0.08491276 0.08491276]
 [0.08774863 0.08774863]
 [0.09047764 0.09047764]
 [0.09310931 0.09310931]
 [0.09565179 0.09565179]
 [0.09811212 0.09811212]
 [0.10049644 0.10049644]
 [0.10281014 0.10281014]
 [0.10505799 0.10505799]
 [0.10724422 0.10724422]
 [0.10937263 0.10937263]
 [0.11144661 0.11144661]
 [0.11346926 0.11346926]
 [0.11544334 0.11544334]
 [0.1173714  0.1173714 ]
 [0.11925576 0.11925576]
 [0.12109854 0.12109854]
 [0.12290168 0.12290168]
 [0.12466699 0.12466699]
 [0.12639613 0.12639613]
 [0.12809063 0.12809063]
 [0.12975194 0.12975194]
 [0.13138138 0.13138138]
 [0.1329802  0.1329802 ]
 [0.13454956 0.13454956]
 [0.13609054 0.13609054]
 [0.13760417 0.13760417]
 [0.1390914  0.1390914 ]
 [0.14055315 0.14055315]
 [0.14199025 0.14199025]
 [0.14340353 0.14340353]
 [0.14479373 0.14479373]
 [0.14616157 0.14616157]
 [0.14750774 0.14750774]
 [0.14883289 0.14883289]
 [0.15013762 0.15013762]
 [0.15142254 0.15142254]
 [0.15268818 0.15268818]
 [0.15393509 0.15393509]
 [0.15516377 0.15516377]
 [0.1563747  0.1563747 ]
 [0.15756836 0.15756836]
 [0.15874517 0.15874517]
 [0.15990556 0.15990556]
 [0.16104995 0.16104995]
 [0.16217871 0.16217871]
 [0.16329223 0.16329223]
 [0.16439086 0.16439086]
 [0.16547495 0.16547495]
 [0.16654482 0.16654482]
 [0.16760081 0.16760081]
 [0.16864321 0.16864321]
 [0.16967233 0.16967233]
 [0.17068844 0.17068844]
 [0.17169183 0.17169183]
 [0.17268276 0.17268276]
 [0.1736615  0.1736615 ]
 [0.17462827 0.17462827]
 [0.17558334 0.17558334]
 [0.17652692 0.17652692]
 [0.17745925 0.17745925]
 [0.17838054 0.17838054]
 [0.17929101 0.17929101]
 [0.18019085 0.18019085]
 [0.18108027 0.18108027]
 [0.18195946 0.18195946]
 [0.18282861 0.18282861]
 [0.18368789 0.18368789]
 [0.18453748 0.18453748]
 [0.18537756 0.18537756]
 [0.18620829 0.18620829]
 [0.18702983 0.18702983]
 [0.18784233 0.18784233]
 [0.18864596 0.18864596]
 [0.18944085 0.18944085]
 [0.19022717 0.19022717]
 [0.19100503 0.19100503]
 [0.19177459 0.19177459]
 [0.19253598 0.19253598]
 [0.19328932 0.19328932]
 [0.19403474 0.19403474]
 [0.19477238 0.19477238]
 [0.19550234 0.19550234]
 [0.19622475 0.19622475]
 [0.19693973 0.19693973]
 [0.19764737 0.19764737]
 [0.19834781 0.19834781]]
```

---

[← Dataset Two: House Price Data from FRED](02-dataset-two-house-price-data-from-fred.md) · [Up: contents](index.md)
