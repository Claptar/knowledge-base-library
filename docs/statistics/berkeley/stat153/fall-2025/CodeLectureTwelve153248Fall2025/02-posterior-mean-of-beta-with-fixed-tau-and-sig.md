---
title: Posterior mean of beta with fixed tau and sig
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Posterior mean of beta with fixed tau and sig

**Source:** [`CodeLectureTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwelve153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

C = 10**10
tau = 0.0001
tau = 1
#tau = .0001
sig = 0.2
Q = np.diag(np.concatenate([[C, C], np.repeat(tau**2, n-2)]))

XTX = np.dot(X.T, X)
TempMat = np.linalg.inv(np.linalg.inv(Q) + (XTX/(sig ** 2)))
XTy = np.dot(X.T, y)

betahat = np.dot(TempMat, XTy/(sig ** 2))
muhat = np.dot(X, betahat)

plt.figure(figsize = (10, 6))
plt.plot(y)
plt.plot(muhat)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We showed in class that this posterior mean coincides with the ridge regression estimate from last lecture provided the tuning parameter $\lambda$ in ridge regression is related to $\tau$ and $\sigma$ via $\lambda = \sigma^2/\tau^2$. This can be verified as follows.

```python
#below penalty_start = 2 means that b0 and b1 are not included in the penalty
def solve_ridge(X, y, lambda_val, penalty_start=2):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.sum_squares(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

```python
b_ridge = solve_ridge(X, y, lambda_val = (sig ** 2)/(tau ** 2))
ridge_fitted = np.dot(X, b_ridge)
plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray', label = 'data')
plt.plot(ridge_fitted, color = 'red', label = 'Ridge')
plt.plot(muhat, color = 'blue', label = 'Posterior mean')
plt.legend()
plt.show()
print(np.column_stack((ridge_fitted, muhat)))
```

```
[[-4.54318547e-01 -4.54318548e-01]
 [-1.71984865e-01 -1.71984865e-01]
 [-3.16875161e-02 -3.16875106e-02]
 [-1.25841198e-01 -1.25841197e-01]
 [-2.54672707e-01 -2.54672707e-01]
 [-7.23788867e-02 -7.23788882e-02]
 [ 1.33661090e-01  1.33661091e-01]
 [-1.14459781e-01 -1.14459774e-01]
 [-1.36175761e-01 -1.36175758e-01]
 [-1.39426580e-01 -1.39426585e-01]
 [-1.77757943e-01 -1.77757940e-01]
 [-5.69051044e-01 -5.69051042e-01]
 [-4.37238510e-01 -4.37238509e-01]
 [-1.79976871e-01 -1.79976871e-01]
 [-2.63959894e-01 -2.63959891e-01]
 [ 9.35404352e-02  9.35404360e-02]
 [ 2.42494730e-02  2.42494753e-02]
 [-1.78618302e-01 -1.78618301e-01]
 [-3.28085237e-01 -3.28085237e-01]
 [-2.17161205e-02 -2.17161196e-02]
 [-1.54944818e-01 -1.54944816e-01]
 [-3.30302181e-01 -3.30302181e-01]
 [-2.76698624e-01 -2.76698624e-01]
 [-2.15490024e-01 -2.15490021e-01]
 [-2.00566655e-01 -2.00566657e-01]
 [-1.48568204e-01 -1.48568203e-01]
 [-2.11967970e-01 -2.11967969e-01]
 [-7.90341525e-02 -7.90341505e-02]
 [ 1.11164291e-01  1.11164290e-01]
 [-5.45877845e-02 -5.45877837e-02]
 [-2.68612799e-01 -2.68612797e-01]
 [-1.08538558e-01 -1.08538558e-01]
 [ 6.33271002e-02  6.33271017e-02]
 [-1.51859724e-01 -1.51859724e-01]
 [-2.36120433e-01 -2.36120433e-01]
 [-3.74983329e-01 -3.74983328e-01]
 [-3.50965885e-01 -3.50965885e-01]
 [-5.72002337e-01 -5.72002336e-01]
 [-1.71879796e-01 -1.71879797e-01]
 [ 1.56730467e-02  1.56730480e-02]
 [-2.96077584e-01 -2.96077585e-01]
 [-2.85691635e-01 -2.85691635e-01]
 [-2.29789442e-01 -2.29789442e-01]
 [-5.12700476e-01 -5.12700475e-01]
 [-5.24018144e-01 -5.24018146e-01]
 [-3.35823962e-01 -3.35823969e-01]
 [-1.69745834e-01 -1.69745826e-01]
 [-1.01812623e-01 -1.01812611e-01]
 [-2.14407329e-01 -2.14407348e-01]
 [-2.94597376e-01 -2.94597372e-01]
 [-2.69266977e-01 -2.69266970e-01]
 [-2.00365935e-01 -2.00365944e-01]
 [-1.68169616e-01 -1.68169609e-01]
 [-2.43805006e-01 -2.43805012e-01]
 [-5.44158699e-01 -5.44158696e-01]
 [-3.40992143e-01 -3.40992148e-01]
 [-3.02099298e-01 -3.02099297e-01]
 [-3.20470559e-01 -3.20470559e-01]
 [-4.86613872e-01 -4.86613873e-01]
 [-6.29273219e-01 -6.29273220e-01]
 [-4.11845773e-01 -4.11845775e-01]
 [-5.15898222e-01 -5.15898223e-01]
 [-3.26852927e-01 -3.26852928e-01]
 [-3.32676699e-01 -3.32676698e-01]
 [-1.00013183e-01 -1.00013185e-01]
 [-1.28588548e-01 -1.28588549e-01]
 [-1.67799397e-01 -1.67799398e-01]
 [-5.02328639e-01 -5.02328640e-01]
 [-4.71874249e-01 -4.71874250e-01]
 [-1.07918241e-01 -1.07918243e-01]
 [-1.45086389e-01 -1.45086390e-01]
 [-1.20048454e-01 -1.20048455e-01]
 [-1.92314470e-01 -1.92314471e-01]
 [-2.70183107e-01 -2.70183109e-01]
 [-2.04091297e-01 -2.04091298e-01]
 [-3.39898284e-01 -3.39898286e-01]
 [ 7.88191109e-02  7.88191095e-02]
 [-1.94058827e-01 -1.94058829e-01]
 [-1.25129586e-01 -1.25129588e-01]
 [-3.29519970e-01 -3.29519971e-01]
 [-2.94117145e-01 -2.94117147e-01]
 [-1.78090202e-02 -1.78090215e-02]
 [ 1.03445121e-01  1.03445119e-01]
 [-1.31088499e-01 -1.31088502e-01]
 [-2.58271686e-01 -2.58271688e-01]
 [-2.87753764e-01 -2.87753766e-01]
 [-2.72391906e-01 -2.72391908e-01]
 [-7.11991705e-02 -7.11991729e-02]
 [ 1.66090214e-02  1.66090174e-02]
 [-2.82034882e-02 -2.82034860e-02]
 [ 1.09901608e-01  1.09901602e-01]
 [ 2.01549820e-01  2.01549819e-01]
 [ 2.69826469e-01  2.69826466e-01]
 [ 4.90713752e-02  4.90713730e-02]
 [ 2.77962645e-01  2.77962642e-01]
 [ 2.18394004e-01  2.18394002e-01]
 [ 1.83193045e-01  1.83193042e-01]
 [ 2.53372601e-02  2.53372571e-02]
 [ 1.79780091e-02  1.79780061e-02]
 [ 5.08351516e-02  5.08351488e-02]
 [-1.85821680e-01 -1.85821684e-01]
 [-2.72601645e-01 -2.72601648e-01]
 [ 1.05428106e-01  1.05428103e-01]
 [ 7.82415614e-02  7.82415583e-02]
 [-1.09889945e-01 -1.09889949e-01]
 [ 7.92658863e-02  7.92658834e-02]
 [-6.88100094e-02 -6.88100129e-02]
 [-2.83856668e-04 -2.83860307e-04]
 [ 3.08928354e-01  3.08928351e-01]
 [ 1.40007049e-01  1.40007046e-01]
 [ 5.09238037e-02  5.09238001e-02]
 [ 9.94739632e-02  9.94739595e-02]
 [ 7.03577817e-02  7.03577782e-02]
 [ 1.14264327e-02  1.14264288e-02]
 [-3.84134539e-02 -3.84134575e-02]
 [-7.59160656e-02 -7.59160700e-02]
 [-1.37499244e-01 -1.37499247e-01]
 [-1.11679188e-01 -1.11679192e-01]
 [-1.99491008e-01 -1.99491013e-01]
 [-5.99901152e-02 -5.99901195e-02]
 [ 1.35043291e-01  1.35043287e-01]
 [-3.64181095e-02 -3.64181137e-02]
 [-1.22483918e-01 -1.22483922e-01]
 [ 2.39189002e-01  2.39188998e-01]
 [-2.69582683e-02 -2.69582730e-02]
 [ 2.37902998e-02  2.37902951e-02]
 [ 1.01074433e-02  1.01074390e-02]
 [ 2.05908404e-01  2.05908399e-01]
 [ 1.32422341e-01  1.32422336e-01]
 [ 1.63168326e-01  1.63168321e-01]
 [ 3.61106906e-01  3.61106902e-01]
 [ 4.59990484e-01  4.59990479e-01]
 [ 1.65898802e-01  1.65898797e-01]
 [ 4.35149510e-01  4.35149505e-01]
 [ 3.26590208e-01  3.26590203e-01]
 [ 2.70330735e-01  2.70330730e-01]
 [ 2.81725730e-01  2.81725725e-01]
 [ 3.67861445e-01  3.67861440e-01]
 [ 4.92680887e-01  4.92680882e-01]
 [ 1.73590941e-01  1.73590936e-01]
 [ 3.60976302e-01  3.60976296e-01]
 [ 4.15448147e-01  4.15448141e-01]
 [ 4.23210109e-01  4.23210104e-01]
 [ 3.34262159e-01  3.34262154e-01]
 [ 2.68351529e-01  2.68351523e-01]
 [ 4.88671476e-01  4.88671471e-01]
 [ 2.99627047e-01  2.99627041e-01]
 [ 2.88836380e-01  2.88836375e-01]
 [ 5.53241448e-01  5.53241442e-01]
 [ 4.68874715e-01  4.68874709e-01]
 [ 3.30732459e-01  3.30732453e-01]
 [ 4.61943091e-01  4.61943085e-01]
 [ 6.67323549e-01  6.67323543e-01]
 [ 7.03113490e-01  7.03113484e-01]
 [ 6.42463861e-01  6.42463855e-01]
 [ 7.30688352e-01  7.30688346e-01]
 [ 6.51504126e-01  6.51504120e-01]
 [ 8.21419554e-01  8.21419548e-01]
 [ 3.69339859e-01  3.69339853e-01]
 [ 6.38681418e-01  6.38681412e-01]
 [ 7.39364120e-01  7.39364114e-01]
 [ 5.64272400e-01  5.64272393e-01]
 [ 5.22187693e-01  5.22187686e-01]
 [ 6.65081438e-01  6.65081431e-01]
 [ 7.40232763e-01  7.40232756e-01]
 [ 8.67884843e-01  8.67884836e-01]
 [ 1.16246179e+00  1.16246179e+00]
 [ 1.04126664e+00  1.04126663e+00]
 [ 8.60057632e-01  8.60057625e-01]
 [ 9.42926960e-01  9.42926953e-01]
 [ 1.11252602e+00  1.11252601e+00]
 [ 8.68332208e-01  8.68332201e-01]
 [ 8.96672496e-01  8.96672489e-01]
 [ 9.25568655e-01  9.25568648e-01]
 [ 1.26623005e+00  1.26623004e+00]
 [ 1.34064967e+00  1.34064966e+00]]
```

*(1 figure omitted — see the original notebook.)*

We next perform posterior inference for all the parameters $\beta, \sigma, \tau$. We follow the method described in lecture. First we take a grid of values of $\tau$ and $\sigma$ and compute the posterior (on the logarithmic scale) of $\tau$ and $\sigma$. The posterior for $\tau$ and $\sigma$ (derived in class) is given by:
\begin{align*}
&  f_{\tau, \sigma \mid \text{data}}(\tau, \sigma) \\ &\propto
  \frac{\sigma^{-n-1} \tau^{-1}}{\sqrt{\det Q}}  \sqrt{\det
  \left(\frac{X^T X}{\sigma^2} + Q^{-1} \right)^{-1}} \exp \left(-\frac{y^T y}{2 \sigma^2} \right)\exp
  \left(\frac{y^T X}{2\sigma^2} \left(\frac{X^T
  X}{\sigma^2} +
   Q^{-1} \right)^{-1} \frac{X^T y}{\sigma^2}  \right).
\end{align*}
where $Q$ is the diagonal matrix with diagonal entries $C, C, \tau^2, \dots, \tau^2$. We can simplify this formula slightly in order to avoid specifying $C$ explicitly. Note that
\begin{align*}
   \det Q  = C \times C \times \tau^2 \times \dots \times \tau^2 = C^2 \tau^{2(n-2)} \propto \tau^{2(n-2)}.
\end{align*}
Also
\begin{align*}
   Q^{-1} = \text{diag}(1/C, 1/C, 1/\tau^2, \dots, 1/\tau^2) \approx \text{diag}(0, 0, 1/\tau^2, \dots, 1/\tau^2).
\end{align*}
Let $Q^{-1}_{\text{approx}}$ be the above diagonal matrix with diagonal entries $0, 0, 1/\tau^2, \dots, 1/\tau^2$. We shall use $Q^{-1}_{\text{approx}}$ as our proxy for $Q^{-1}$. Note that $Q^{-1}_{\text{approx}}$ does not involve any specification of $C$. With this, we rewrite the posterior of $\tau, \sigma$ as:
\begin{align*}
&  f_{\tau, \sigma \mid \text{data}}(\tau, \sigma) \\ &\propto
  \sigma^{-n-1} \tau^{-n+1}   \sqrt{\det
  \left(\frac{X^T X}{\sigma^2} + Q_{\text{approx}}^{-1} \right)^{-1}} \exp \left(-\frac{y^T y}{2 \sigma^2} \right)\exp
  \left(\frac{y^T X}{2\sigma^2} \left(\frac{X^T
  X}{\sigma^2} +
   Q^{-1}_{\text{approx}} \right)^{-1} \frac{X^T y}{\sigma^2}  \right).
\end{align*}
Below we compute this posterior on log-scale for each value in a grid chosen for $\tau$ and $\sigma$.

```python
tau_gr = np.logspace(np.log10(0.0001), np.log10(1), 100)
sig_gr = np.logspace(np.log10(0.1), np.log10(1), 100)

t, s = np.meshgrid(tau_gr, sig_gr)

g = pd.DataFrame({'tau': t.flatten(), 'sig': s.flatten()})

for i in range(len(g)):
    tau = g.loc[i, 'tau']
    sig = g.loc[i, 'sig']
    Qinv_approx = np.diag(np.concatenate([[0, 0], np.repeat(tau**(-2), n-2)]))
    Mat = Qinv_approx + (X.T @ X)/(sig ** 2)
    Matinv = np.linalg.inv(Mat)
    sgn, logcovdet = np.linalg.slogdet(Matinv)
    g.loc[i, 'logpost'] = (-n-1)*np.log(sig) + (-n+1)*np.log(tau) + 0.5 * logcovdet - ((np.sum(y ** 2))/(2*(sig ** 2))) + (y.T @ X @ Matinv @ X.T @ y)/(2 * (sig ** 4))
```

Point estimates of $\tau$ and $\sigma$ can be obtained either by maximizers of the posterior or posterior means.

```python
#Posterior maximizers:
max_row = g['logpost'].idxmax()
print(max_row)
tau_opt = g.loc[max_row, 'tau']
sig_opt = g.loc[max_row, 'sig']
print(tau_opt, sig_opt)
```

```
2333
0.0021544346900318843 0.1707352647470691
```

Below, we fix $\tau$ and $\sigma$ to be the posterior maximizers, and then find the posterior mean of $\beta$.

```python

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Posterior mean of beta with tauopt and sigopt →](03-posterior-mean-of-beta-with-tauopt-and-sigopt.md)
