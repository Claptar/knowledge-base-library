---
title: CodeLabThree153248Fall2025
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThree153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThree153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# CodeLabThree153248Fall2025

**Source:** [`CodeLabThree153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThree153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Inference in Sinusoid Models
---

Consider the following dataset simulated using the model:
\begin{equation*}
    y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin( 2 \pi f t) + \epsilon_t,
\end{equation*}
for $t = 1, \dots, n$ with some fixed values of $f, \beta_0, \beta_1, \beta_2$ and $\sigma$. The goal of this problem is to estimate $f$ along with associated uncertainty quantification.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python
f = 0.2035
n = 400
b0 = 0
b1 = 3
b2 = 5
sig = 10
rng = np.random.default_rng(seed = 42)
errorsamples = rng.normal(loc=0, scale = sig, size = n)
t = np.arange(1, n+1)
y = b0 * np.ones(n) + b1 * np.cos(2 * np.pi * f * t) + b2 * np.sin(2 * np.pi * f * t) + errorsamples
```

```python
plt.figure(figsize = (10, 6))
plt.plot(y)
plt.xlabel('Time')
plt.ylabel('y')
plt.title('A simulated dataset')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To obtain the parameter estimates, we first obtain the estimate of $f$ (by minimizing RSS), then plug in $f = \hat{f}$, and run linear  regression to estimate the other parameters.

```python
def rss(f):
    x = np.arange(1, n+1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])
    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    return rss
```

```python
#We can minimize rss(f) over a fine grid of possible f values. Since n is not very big here, we can work with a dense grid.
ngrid = 100000
allfvals = np.linspace(0, 0.5, ngrid)
rssvals = np.array([rss(f) for f in allfvals])
fhat = allfvals[np.argmin(rssvals)]
print(fhat)
plt.plot(allfvals, rssvals)
plt.show()
```

```
0.2035520355203552
```

*(1 figure omitted — see the original notebook.)*

Compare the estimate $\hat{f}$ with the true value of $f$ which generated the data.

After obtaining $\hat{f}$, we can do linear regression (where $f$ is fixed at $\hat{f}$) to compute the MLEs of the coefficient parameters and  $\sigma$.

```python
x = np.arange(1, n+1)
xcos = np.cos(2 * np.pi * fhat * x)
xsin = np.sin(2 * np.pi * fhat * x)
Xfhat = np.column_stack([np.ones(n), xcos, xsin])
md = sm.OLS(y, Xfhat).fit()
print(md.params) #this gives estimates of beta_0, beta_1, beta_2 (compare them to the true values which generated the data)
b0_est = md.params[0]
b1_est = md.params[1]
b2_est = md.params[2]
print(np.column_stack((np.array([b0_est, b1_est, b2_est]), np.array([b0, b1, b2]))))
rss_fhat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_fhat/n)
sigma_unbiased = np.sqrt((rss_fhat)/(n-3))
print(np.array([sigma_mle, sigma_unbiased, sig])) #sig is the true value of sigma which generated the data
```

```
[-0.05332889  3.00407151  5.63909328]
[[-0.05332889  0.        ]
 [ 3.00407151  3.        ]
 [ 5.63909328  5.        ]]
[ 9.50176964  9.53760297 10.        ]
```

Now let us use Bayesian inference for uncertainty quantification.  The Bayesian posterior for $f$ is:
\begin{equation*}
   I\{0 \leq f \leq 1/2\} |X_f^T X_f|^{-1/2} \left(\frac{1}{RSS(f)} \right)^{(n-p)/2}
\end{equation*}
where $p = 3$ and $|X_f^T X_f|$ denotes the determinant of $X_f^T X_f$.

It is better to compute the logarithm of the posterior (as opposed to the posterior directly) because of numerical issues.

```python
def logpost(f):
    x = np.arange(1, n+1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])
    p = X.shape[1]
    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X)) #sgn gives the sign of the determinant (in our case, this should 1)
    #log_det gives the logarithm of the absolute value of the determinant
    logval = ((p-n)/2) * np.log(rss) - (0.5)*log_det
    return logval
```

While evaluating the log posterior on a grid, it is important to make sure that we do not include frequencies $f$ for which $X_f^T X_f$ is singular. This will be the case for $f = 0$ and $f = 1/2$. When $f$ is very close to 0 or $0.5$, the term $|X_f^T X_f|^{-1/2}$ will be very large because of near-singularity of $X_f^T X_f$. We will therefore exclude frequencies very close to 0 and 0.5 from the grid while calculating posterior probabilities.

From the Periodogram plotted above, it is clear that the maximizing frequency is around 0.2. So we will take a grid that around 0.2 (such as 0.05 to 0.35)

```python
ngrid = 10000
allfvals = np.linspace(0.05, 0.35, ngrid)
print(np.min(allfvals), np.max(allfvals))
logpostvals = np.array([logpost(f) for f in allfvals])
plt.plot(allfvals, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
```

```
0.05 0.35
```

*(1 figure omitted — see the original notebook.)*

Note that the Logarithm of the posterior looks similar to the periodogram. But the posterior itself looks will have only one peak (which dominates all other peaks).

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized/(np.sum(postvals_unnormalized))
plt.plot(allfvals, postvals)
plt.xlabel('Frequency')
plt.ylabel('Probability')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Using the posterior distribution, we can calculate posterior mean etc. and obtain credible intervals for $f$.

```python
#Posterior mean of f:
fpostmean = np.sum(postvals * allfvals)
#Posterior mode of f:
fpostmode = allfvals[np.argmax(postvals)]
print(fpostmean, fpostmode, fhat)
```

```
0.2035529220195366 0.20355535553555354 0.2035520355203552
```

Note that the posterior mode is very close to least squares estimator. Let us now compute a credible interval for $f$. A 95\% credible interval is an interval for which the posterior probability is about 95\%. The following function takes an input value $m$ and compute the posterior probability assigned to the interval $\hat{f} - m*\delta, \hat{f} + m*\delta$ where $\delta$ is the grid resolution that we used for computing the posterior.

We now start with a small value of $m$ (say $m = 0$) and keep increasing it until the posterior probability reaches 0.95.

```python
def PostProbAroundMax(m):
    est_ind = np.argmax(postvals)
    ans = np.sum(postvals[(est_ind-m):(est_ind+m)])
    return(ans)
```

```python
m = 0
while PostProbAroundMax(m) <= 0.95:
    m = m+1
print(m)
```

```
10
```

The credible interval for $f$ can then be computed in the following way.

```python
est_ind = np.argmax(postvals)
f_est = allfvals[est_ind]
#95% credible interval for f:
ci_f_low = allfvals[est_ind - m]
ci_f_high = allfvals[est_ind + m]
print(np.array([f_est, ci_f_low, ci_f_high]))
```

```
[0.20355536 0.20325533 0.20385539]
```

We can draw posterior samples from f as follows.

```python
N = 2000
fpostsamples = rng.choice(allfvals, N, replace = True, p = postvals)
```

Given a posterior sample of $f$, a posterior sample of $\sigma$ can be drawn (this result was proved in Problem 5 of Homework one):
\begin{equation*}
   \frac{RSS(f)}{\sigma^2} \mid \text{data}, f \sim \chi^2_{n-3}
\end{equation*}
Further, given posterior samples from $f$ and $\sigma$, a posterior sample from $\beta = (\beta_0, \beta_1, \beta_2)$ is drawn using:
\begin{equation*}
   \beta \mid \text{data}, \sigma, f \sim N_3 \left(\hat{\beta}_f, \sigma^2 (X_f^T X_f)^{-1} \right)
\end{equation*}
This is done in code as follows.

```python
post_samples = np.zeros(shape = (N, 5))
post_samples[:,0] = fpostsamples
for i in range(N):
    f = fpostsamples[i]
    x = np.arange(1, n+1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])
    p = X.shape[1]
    md_f = sm.OLS(y, X).fit()
    chirv = rng.chisquare(df = n-p)
    sig_sample = np.sqrt(np.sum(md_f.resid ** 2)/chirv) #posterior sample from sigma
    post_samples[i, (p+1)] = sig_sample
    covmat = (sig_sample ** 2) * np.linalg.inv(np.dot(X.T, X))
    beta_sample = rng.multivariate_normal(mean = md_f.params, cov = covmat, size = 1)
    post_samples[i, 1:(p+1)] = beta_sample
print(post_samples)
```

```
[[ 0.20340534 -0.56189444  3.28165364  5.35964685  9.18963362]
 [ 0.20367537 -1.22669044  3.16545782  6.3549404   9.63517389]
 [ 0.20343534 -0.18052831  3.81020787  5.08243908  9.38448971]
 ...
 [ 0.20355536 -0.24135565  2.17378505  5.44757671  9.50053706]
 [ 0.20355536 -0.37830076  2.90179999  6.50300091  9.49852951]
 [ 0.20337534 -0.52307159  4.11483084  4.68294379  9.84908592]]
```

Let us plot the posterior functions along with the original data to visualize uncertainty.

```python
x = np.arange(1, n+1)
plt.figure(figsize = (15, 6))
plt.plot(y)
for i in range(N):
    f = fpostsamples[i]
    b0 = post_samples[i, 1]
    b1 = post_samples[i, 2]
    b2 = post_samples[i, 3]
    ftdval = b0 + b1 * np.cos(2 * np.pi * f * x) + b2 * np.sin(2 * np.pi * f * x)
    plt.plot(ftdval, color = 'red')
```

*(1 figure omitted — see the original notebook.)*

A simple summary of the posterior samples can be obtained as follows.

```python
pd.DataFrame(post_samples).describe()
#note that the true value of f is 0.2035, b0 is 0, b1 is 3, b2 is 5 and sigma is 10
```

```
0            1            2            3            4
count  2000.000000  2000.000000  2000.000000  2000.000000  2000.000000
mean      0.203554    -0.048116     2.926668     5.487344     9.567343
std       0.000154     0.479084     1.240482     0.894120     0.337935
min       0.203045    -2.282401    -1.430247     1.670873     8.564508
25%       0.203435    -0.359168     2.134556     4.928442     9.343711
50%       0.203555    -0.061192     3.009265     5.519098     9.567323
75%       0.203645     0.268955     3.769393     6.097100     9.787657
max       0.204095     1.614744     6.128241     8.477974    10.710101
```

## Frequency Aliasing

Now consider the same simulation setting as the previous problem but change the true frequency to $f = 2 - 0.2035$ as opposed to $f = 0.2035$. The analysis then would still yield an estimate which is close to 0.2035. This is because the frequency $f_0 = 0.2035$ is an alias of $f = 2 - 0.2035$ in the sense that the two sinusoids $s_t = R \cos (2 \pi f t + \phi)$ and $s_t = R \cos (2 \pi f_0 t - \phi)$ are identical when $t$ is integer-valued. One can note that the estimate of $\beta_2$ will have a flipped sign however.

It is very important to note that aliasing is a consequence of our time variable taking the equally spaced values $1, \dots, n$. If we change the time variable to some non-uniform values (i.e., if we sample the sinusoid at a non-uniform set of values), then it is possible to estimate frequencies which are outside of the range $[0, 0.5]$. This is illustrated below with $f = 1.8$. We take time to be randomly chosen points in the range $[1, n]$.

```python
f = 2 - 0.2035
n = 400
b0 = 0
b1 = 3
b2 = 5
sig = 10
rng = np.random.default_rng()
errorsamples = rng.normal(loc=0, scale = sig, size = n)
#t = np.arange(1, n+1)
t = np.sort(rng.uniform(low = 1, high = n, size = n))
y = b0 * np.ones(n) + b1 * np.cos(2 * np.pi * f * t) + b2 * np.sin(2 * np.pi * f * t) + errorsamples
```

```python
print(t) #time again ranges roughly between 1 and 400 but this time the values are not equally spaced
```

```
[  1.14975602   1.2120058    1.74037229   2.93828141   2.99555488
   3.22544303   3.42684266   3.46440704   3.84792778   4.12969
   4.40549321   5.92805797   7.30139115   8.56396777   9.27155691
   9.30912776   9.94332563  10.62717676  10.70331524  11.5338629
  12.89644896  14.38579427  15.17741209  15.8571532   18.97148464
  19.02467279  21.55042309  22.91270338  23.96687953  26.25990635
  26.65910504  26.78859856  26.92745295  27.01809884  28.07972662
  28.47621567  30.54669751  30.61933994  30.92850461  33.39876022
  34.82075941  37.41575987  37.64827907  38.09008891  38.51396405
  39.49557342  42.22266621  44.08835013  44.83343818  46.10338995
  47.49012765  47.49287564  47.92921263  48.3728239   50.73947705
  51.85128768  52.18202989  52.99353689  54.65041079  55.87703368
  56.38086113  56.63094771  58.37701761  59.81095746  60.93499155
  63.10985177  63.2705136   63.45129725  64.88098453  65.18193867
  66.19633902  66.74122819  67.77920012  67.80761924  68.11184098
  70.88549113  71.85240605  72.2538873   72.39801878  72.869587
  73.97811193  74.85239971  76.27213133  76.27509647  76.35339171
  77.92776395  79.48776195  79.62962882  80.36384925  81.51670982
  81.75057868  84.38144381  84.58142443  85.81994173  90.621362
  91.56208645  91.76884998  91.83545061  92.87523979  92.87528154
  92.89638539  93.12640875  97.67343583  98.1418956  101.22213607
 104.54395624 106.56937006 106.5959107  106.76696931 108.66001097
 110.71454397 112.32182343 112.72670337 113.86346257 113.9515447
 117.01639652 118.49290281 118.54291654 118.59019886 119.3343052
 122.2666112  122.94365419 126.21719182 126.69637631 129.25089034
 131.30392978 131.30452988 131.6190979  133.15996108 133.57092021
 133.732862   133.76391123 134.27115039 135.86504263 138.36237838
 139.74170064 140.68251344 140.69614312 142.42033115 145.18301403
 145.42854433 146.68265496 147.55117594 148.23696712 148.91671886
 148.99162975 149.75229481 150.82995108 150.83503052 153.02355458
 153.54958241 153.68988727 154.20475807 154.43666597 154.58707498
 156.03167248 156.23481809 156.48660925 157.78022645 157.807631
 158.4281917  158.65165405 159.17683526 160.0641088  160.75257922
 161.92787358 163.39922552 163.5719167  163.61838881 165.47411952
 166.83046092 168.33574425 169.17375065 169.59573937 170.50779378
 171.13456825 171.81736744 172.09221792 175.89078408 176.63263738
 176.90819914 177.07019742 178.8371989  178.9023812  179.59983862
 183.79888126 184.90724928 185.85693091 187.02986278 187.64517122
 187.86645812 188.63010187 190.26374548 190.67172966 191.46900612
 191.794707   194.06468573 198.07829534 199.44362453 200.80157927
 201.50815344 201.80118088 203.63484572 204.27450829 204.8108396
 204.9170553  205.47906787 207.58038725 208.11136753 209.7971164
 213.35435474 213.95175619 214.44678624 214.88359126 214.93318396
 220.0426503  220.14983079 222.42302073 222.54406452 222.97617472
 226.1363906  226.54976039 227.07494916 227.95854416 229.36848951
 229.55361063 231.10995964 231.59959615 232.04287232 232.70373362
 235.7402208  236.22016561 238.0441124  238.45195194 239.95218925
 240.33768011 241.30542954 242.04316455 242.85259031 243.8872196
 244.49096049 244.66848541 245.0247126  245.03627428 246.27694626
 246.55637969 247.77970489 249.52188895 253.75262492 254.36842125
 258.04885329 259.8970497  260.93856371 262.98945489 266.19939553
 266.69575816 268.80075606 269.1020868  269.37728955 272.08459407
 272.32312296 272.32869817 272.38920771 273.35766372 274.96785479
 277.31360101 277.66744162 281.31665101 282.96238729 284.33574164
 286.24028312 288.1616026  290.75909994 291.20408907 292.47174796
 292.50733559 292.81914852 293.22332171 293.54713287 294.74374457
 295.3917135  296.14351596 297.58044603 298.06722323 299.65760426
 299.71811694 300.6096668  303.00634792 304.57307659 305.54233047
 306.24045749 306.84926148 311.06675713 311.20576129 311.90685024
 312.21777301 314.13209233 315.41589748 315.67577489 317.07347911
 318.14490509 318.58210047 318.59995118 320.03624268 320.49141714
 321.03358891 321.19640823 321.3420951  321.73886301 321.87463389
 323.50556132 324.65250523 327.19657664 327.47902576 327.71915566
 328.73978118 330.48116646 330.68722563 331.34038983 331.54601887
 332.22657341 333.04986446 333.80259402 335.68059898 336.12887768
 337.04616806 337.28733766 337.70112299 337.74425358 338.31078983
 339.22692806 339.31266766 339.85486352 341.26990325 341.46785857
 342.17723501 344.10957778 346.18572716 347.12735797 347.81912912
 348.45635558 349.77974368 350.71491278 351.85162086 353.21994423
 353.25110961 353.2789414  353.93025341 354.36751296 354.97848351
 355.10765459 355.93388728 356.19098415 356.71066937 357.92652289
 359.08672517 359.52734241 360.27233493 360.78517193 361.59801568
 362.40843703 364.04826543 364.93648927 365.36727746 365.39902752
 367.52856221 372.31709684 372.49335902 373.65825496 374.07669621
 375.07381753 377.1224984  378.46985438 378.51583207 378.94473792
 379.1748648  380.18149507 380.72704557 381.06287855 381.092998
 381.26165625 381.60739528 381.75346216 382.06171516 382.76003679
 384.70447045 385.81508984 386.17359831 386.28265191 387.07500338
 388.04929286 389.04024158 390.07700029 390.22306184 390.45008933
 391.71633029 396.1560395  396.99758397 398.08977033 398.7514625 ]
```

```python
plt.figure(figsize = (10, 6))
plt.plot(y)
plt.xlabel('Time')
plt.ylabel('y')
plt.title('A simulated dataset')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We will again use RSS-minimization to estimate $f$.

```python
def rss(f):
    xcos = np.cos(2 * np.pi * f * t)
    xsin = np.sin(2 * np.pi * f * t)
    X = np.column_stack([np.ones(n), xcos, xsin])
    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    return rss
```

To evaluate the criterion function, we shall take the grid to be spaced over the larger range $[0, 10]$. Note that we cannot restrict the frequency parameter to $[0, 1/2]$ because time is not equally spaced.

```python
ngrid = 100000
allfvals = np.linspace(0, 10, ngrid)
rssvals = np.array([rss(f) for f in allfvals])
```

```python
plt.plot(allfvals, rssvals)
plt.xlabel('Frequency')
plt.ylabel('Sum of Squares')
plt.title('Least Squares Criterion Function')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#the least squares estimate of f is now:
fhat = allfvals[np.argmin(rssvals)]
print(fhat)
```

```
1.796517965179652
```

This $\hat{f}$ is very close to $2 - 0.2035$. The Bayesian analysis will also give a posterior that is tightly concentrated around $(2 - 0.2035)$.

```python
def logpost(f):
    xcos = np.cos(2 * np.pi * f * t)
    xsin = np.sin(2 * np.pi * f * t)
    X = np.column_stack([np.ones(n), xcos, xsin])
    p = X.shape[1]
    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X)) #sgn gives the sign of the determinant (in our case, this should 1)
    #log_det gives the logarithm of the absolute value of the determinant
    logval = ((p-n)/2) * np.log(rss) - (0.5)*log_det
    return logval
```

```python
allfvals = allfvals[100:ngrid] #we are removing some values near 0 to prevent singularity of X_f^T X_f
print(np.min(allfvals), np.max(allfvals))
logpostvals = np.array([logpost(f) for f in allfvals])
plt.plot(allfvals, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
```

```
0.01000010000100001 10.0
```

*(1 figure omitted — see the original notebook.)*

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized/(np.sum(postvals_unnormalized))
plt.plot(allfvals, postvals)
plt.xlabel('Frequency')
plt.ylabel('Probability')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Posterior mean of f:
fpostmean = np.sum(postvals * allfvals)
#Posterior mode of f:
fpostmode = allfvals[np.argmax(postvals)]
print(fpostmean, fpostmode, fhat)
```

```
1.7965379811361581 1.796517965179652 1.796517965179652
```

---

[Up: contents](index.md)
