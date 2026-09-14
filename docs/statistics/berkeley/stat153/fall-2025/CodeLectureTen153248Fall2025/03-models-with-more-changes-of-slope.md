---
title: Models with more changes of Slope
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Models with more changes of Slope

**Source:** [`CodeLectureTen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We can seek to obtain further improved models by using more points of change of slope. The following model has two points where the slope changes:
\begin{align*}
   y_t = \beta_0 + \beta_1 t + \beta_2 (t - c_1)_+ + \beta_3 (t - c_2)_+ + \epsilon_t.
\end{align*}
The unknown parameters now are $\beta_0,\beta_1, \beta_2, \beta_3$ as well as $c_1, c_2$ (also $\sigma$).

For parameter estimation, we can define the RSS function:
\begin{align*}
   RSS(c_1, c_2) := \min_{\beta_0, \beta_1, \beta_2, \beta_3} \sum_{t=1}^n \left(y_t - \beta_0 - \beta_1 t - \beta_2 (t - c_1)_+ - \beta_3 (t -c_2)_+ \right)^2
\end{align*}
and then we can do some sort of grid optimization for $c_1$ and $c_2$. The code for this is given below.

```python
def rss(c): #c is now a vector of change of slope points
    n = len(y)
    x = np.arange(1, n+1)
    X = np.column_stack((np.ones(n), x))
    if np.isscalar(c):
        c = [c]
    for j in range(len(c)):
        x_c = np.maximum(0, x - c[j])
        X = np.column_stack((X, x_c))
    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    return rss
```

```python
num_c_vals = 200 #this is the number of different values of c we will try
c1_gr = np.linspace(1, n, num_c_vals)
c2_gr = np.linspace(1, n, num_c_vals)
C1, C2 = np.meshgrid(c1_gr, c2_gr)
g = pd.DataFrame({'c1': C1.ravel(), 'c2': C2.ravel()})
g['rss'] = g.apply(lambda row: rss([row['c1'], row['c2']]), axis=1)

min_row = g.loc[g['rss'].idxmin()]
print(min_row)
c_opt = min_row[:-1]
rss_opt = min_row.iloc[-1]
print(c_opt - 1 + tme[0]) #these are the estimated years when the slope changes
print(c_hat) #this was the best c in a single change of slope model
print(rss_smallest) #this was the smallest RSS in a single change of slope model
print(rss_opt)
```

```
c1      62.065327
c2     101.321608
rss      0.198865
Name: 32298, dtype: float64
c1    1961.065327
c2    2000.321608
Name: 32298, dtype: float64
66.28928928928929
0.3490460776066189
0.19886465005670498
```

```python
c = np.array(c_opt)
x = np.arange(1, n+1)
x_c1 = np.maximum(0, x - c[0])
x_c2 = np.maximum(0, x - c[1])
X = np.column_stack((np.ones(n), x, x_c1, x_c2))
md_2 = sm.OLS(y, X).fit()
print(md_2.summary())
#plt.plot(tme, y)
#plt.plot(tme, md.fittedvalues, color = 'orange', label='1 change of slope')
plt.plot(tme, md_2.fittedvalues, color = 'red')
plt.axvline(c[0] - 1 + tme[0], color='green', linestyle='--')
plt.axvline(c[1] - 1 + tme[0], color='green', linestyle='--')
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  CAPOP   R-squared:                       0.998
Model:                            OLS   Adj. R-squared:                  0.998
Method:                 Least Squares   F-statistic:                 2.513e+04
Date:                Wed, 01 Oct 2025   Prob (F-statistic):          6.91e-169
Time:                        00:03:47   Log-Likelihood:                 225.35
No. Observations:                 125   AIC:                            -442.7
Df Residuals:                     121   BIC:                            -431.4
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          7.3642      0.010    744.549      0.000       7.345       7.384
x1             0.0382      0.000    158.341      0.000       0.038       0.039
x2            -0.0198      0.001    -36.636      0.000      -0.021      -0.019
x3            -0.0123      0.001    -11.270      0.000      -0.015      -0.010
==============================================================================
Omnibus:                       13.461   Durbin-Watson:                   0.086
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               19.093
Skew:                           0.563   Prob(JB):                     7.15e-05
Kurtosis:                       4.549   Cond. No.                         209.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

*(1 figure omitted — see the original notebook.)*

The interpretation of this model is that: before 1961, the growth rate is 3.82\%. Between 1961 and 2000, the growth fell to 3.82 - 1.23 = 2.59\%. After 2000, the growth rate further dropped to 2.59 - 1.98 = 0.61 \%.

There is a different way of fitting this model that can be computationally more efficient. This involves jointly minimizing least squares over all the parameters. Specifically, we aim to optimize:
\begin{align*}
   L(\beta_0, \beta_1, \beta_2, \beta_3, c_1, c_2) := \sum_{t=1}^n \left(y_t - \beta_0 - \beta_1 t - \beta_2 (t - c_1)_+ - \beta_3 (t - c_2)_+ \right)^2
\end{align*}
over all the parameters $\beta_0, \beta_1, \beta_2, c_1, c_2$ simultaneously. This optimization is nonlinear and nontrivial but we can use black box optimization libraries. For example, we can use the pytorch library to solve this optimization.

First import the torch libraries.

```python
import torch
import torch.nn as nn
import torch.optim as optim
```

The following is the code for representing the broken stick regression (or change of slope) model in PyTorch. PyTorch organizes models as classes.

```python
class BrokenStickRegression(nn.Module):
    def __init__(self, knots_init, beta_init):
        super().__init__()
        self.num_knots = len(knots_init)
        self.beta = nn.Parameter(torch.tensor(beta_init, dtype=torch.float32))
        self.knots = nn.Parameter(torch.tensor(knots_init, dtype=torch.float32))

    def forward(self, x):
        knots_sorted,_ = torch.sort(self.knots)
        out = self.beta[0] + self.beta[1] * x
        for j in range(self.num_knots):
            out = out + self.beta[j+2] * torch.relu(x - knots_sorted[j])
        return out
```

The class `BrokenStickRegression` inherits from `nn.Module`, which is the base class for all models in PyTorch (linear regression, neural networks, etc.). By subclassing nn.Module, we get access to a lot of PyTorch functionality automatically: for example, it keeps track of parameters, makes them trainable, and allows us to use optimizers like gradient descent.

The term `knots` refers to $c_1, \dots, c_k$.

In the constructor (`__init__`), the code takes two inputs: a list of initial knot positions (`knots_init`) and initial coefficients (`beta_init`). These are wrapped in `nn.Parameter`, which tells PyTorch: “this is a parameter we want to optimize.” So, during training, PyTorch will update both the regression coefficients and the knot locations.

The `forward` method defines the model equation (how does the model convert input $x$ to output $y$). When you pass in an input x, it:

1. Sorts the knot locations (so they are in order).

2. Starts with the base linear trend, $\beta_0 + \beta_1 x$

3. For each knot, adds a term $\beta_j \text{ReLU}(x - c_j)$

The effect is exactly the broken-stick regression function: linear to start, with slope changes at each knot. The nice thing about using `nn.Module` is that all of this can be trained with PyTorch’s optimization tools.

The raw data here is given by $y$ with covariate $x$ given by time $t = 1, \dots, n$. We do not apply the model to this raw data but we scale the raw data first. The algorithm for parameter fitting will work better with scaled data as opposed to raw data.

The code below first standardizes the raw input arrays `y_raw` and `x_raw` by subtracting their means and dividing by their standard deviations, resulting in `y_scaled` and `x_scaled`, respectively. This scaling step ensures that both inputs have mean 0 and standard deviation 1, which helps neural network training converge faster and more reliably. After scaling, the arrays are converted into PyTorch tensors (`y_torch` and `x_torch`) with `dtype=torch.float32`, and an additional singleton dimension is added using `unsqueeze(1)` to ensure each data point is treated as a one-dimensional feature vector. Conversion to PyTorch tensors is necessary because PyTorch models and optimization routines (like gradient computation and parameter updates) operate on tensors, not on NumPy arrays.

```python
y_raw = y
x_raw = np.arange(1, n+1)
y_scaled = (y_raw - np.mean(y_raw)) / np.std(y_raw)
x_scaled = (x_raw - np.mean(x_raw)) / np.std(x_raw)
y_torch = torch.tensor(y_scaled, dtype=torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype=torch.float32).unsqueeze(1)
```

For using PyTorch, the first step is to obtain suitable initial estimates for the parameters. These are deduced as follows. We take $c_1, \dots, c_k$ to be quantiles of the scaled covariate at equal levels. Then we fit the model with $c_1, \dots, c_k$ fixed at these initial values, and obtain the initial values of the coefficients.

```python
k = 2 #this is the number of knots (changes of slope)
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_scaled, quantile_levels)

n = len(y_scaled)
X = np.column_stack((np.ones(n), x_scaled))
for j in range(k):
    x_c = np.maximum(0, x_scaled - knots_init[j])
    X = np.column_stack((X, x_c))
md_init = sm.OLS(y_scaled, X).fit()
beta_init = md_init.params.values
print(knots_init)
print(knots_init * np.std(x_raw) + np.mean(x_raw)) #these are the initial knots in original scale
print(beta_init)
```

```
[-0.5727498  0.5727498]
[42.33333333 83.66666667]
[ 0.47153593  1.47880914 -0.44549948 -0.66986532]
```

The next code line `md_nn = BrokenStickRegression(knots_init=knots_init, beta_init=beta_init)` creates an instance of the custom neural network model `BrokenStickRegression`. It initializes the learnable parameters of the model: the knot locations are set to the values provided in `knots_init`, and the coefficients are set to `beta_init`. This prepares the model for training by defining its initial piecewise linear structure.

```python
md_nn = BrokenStickRegression(knots_init, beta_init)
#This code creates an instance of the BrokenStickRegression class with initial knots and beta values.
```

The next block of code sets up and runs the training loop for the model `BrokenStickRegression`. The `Adam` optimizer is initialized with the model’s parameters and a learning rate of 0.01, and the loss function is set to mean squared error (`MSELoss`). For 10,000 epochs, the code repeatedly performs one training step: it clears previous gradients with `optimizer.zero_grad()`, computes predictions `y_pred` by passing `x_torch` through the model, evaluates the loss between predictions and true values, backpropagates the loss with `loss.backward()`, and updates the model parameters using `optimizer.step()`. Every 100 epochs, the current epoch and loss value are printed to monitor training progress. Running the code multiple times may be necessary to ensure good convergence, especially because this is a non-convex optimization problem.

```python
optimizer = optim.Adam(md_nn.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

for epoch in range(10000):
    optimizer.zero_grad()
    y_pred = md_nn(x_torch)
    loss = loss_fn(y_pred, y_torch)
    loss.backward()
    optimizer.step()
    if epoch % 500 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')
```

```
Epoch 0, Loss: 0.0030975514091551304
Epoch 500, Loss: 0.0016019828617572784
Epoch 1000, Loss: 0.0016019828617572784
Epoch 1500, Loss: 0.0016019828617572784
Epoch 2000, Loss: 0.001605847617611289
Epoch 2500, Loss: 0.0016040573827922344
Epoch 3000, Loss: 0.0016020172042772174
Epoch 3500, Loss: 0.0016019823960959911
Epoch 4000, Loss: 0.0016020506154745817
Epoch 4500, Loss: 0.0016019862378016114
Epoch 5000, Loss: 0.001601983094587922
Epoch 5500, Loss: 0.001601986470632255
Epoch 6000, Loss: 0.0016038458561524749
Epoch 6500, Loss: 0.0016020116163417697
Epoch 7000, Loss: 0.0016099847853183746
Epoch 7500, Loss: 0.001617018016986549
Epoch 8000, Loss: 0.0016035223379731178
Epoch 8500, Loss: 0.001601366326212883
Epoch 9000, Loss: 0.0016012309351935983
Epoch 9500, Loss: 0.001601396594196558
```

The next code prints out the current loss value, the estimated model coefficients (`beta`), and the estimated knot locations after training. The `detach().numpy()` calls are used to move each tensor from the computation graph to a regular NumPy array so they can be easily printed or further processed without tracking gradients. Finally, it prints `rss_opt`, which represents the smallest residual sum of squares (RSS) achieved with two knots using our previous grid-based search method. This provides a measure of the quality of the PyTorch parameter estimates.

```python
print(loss.detach().numpy())
print(md_nn.beta.detach().numpy())
print(md_nn.knots.detach().numpy())
print(rss_opt)
```

```
0.0016011636
[ 0.34637082  1.3828472  -0.7193925  -0.44183147]
[-0.01797236  1.065274  ]
0.19886465005670517
```

`rss_opt` seems to be on a different scale to the loss. This is because of the change of scale when we went from `y_raw` and `x_raw` to `y_scaled` and `x_scaled`, as well as because the loss here is Mean-Squared Error (not just Squared Error). We can bring the loss to the same scale as RSS as follows.

```python
#converting back to original scale
print(loss.detach().numpy() * (np.std(y_raw)**2) * n ) #this rescales the loss to the rss scale
print(md_nn.beta.detach().numpy())
print(md_nn.knots.detach().numpy() * np.std(x_raw) + np.mean(x_raw)) #these are the knots in original scale
print(rss_opt)
```

```
0.19868279855727622
[ 0.34637737  1.3828548  -0.7193962  -0.44181848]
[ 62.35171  101.438324]
0.19886465005670498
```

The loss achieved by PyTorch seems slightly better than the RSS we got from our grid search method. This suggests that PyTorch is working well here. Next let us look at the estimates of $\beta_0, \dots, \beta_{k+1}$ obtained from PyTorch (converted to the original scale). We compare them with the estimates from our previous grid-search method.

```python
#drop intercept
print(md_nn.beta.detach().numpy()[1:] * (np.std(y_raw)/np.std(x_raw)))
print(md_2.params.values[1:])
```

```
[ 0.03818281 -0.01986367 -0.01219931]
[ 0.03823489 -0.01978384 -0.01234546]
```

This is essentially the same model that we found before (in the grid search method, $c_1$ and $c_2$ seem to be swapped though).

This PyTorch method scales easily to higher values of the number of knots i.e., to fit models of the form:
\begin{align*}
   y_t = \beta_0 + \beta_1 t + \beta_2 (t - c_1)_+ \beta_3 (t - c_2)_+ + \dots + \beta_{k+1} (t - c_k)_+ + \epsilon_t
\end{align*}
On the other hand, the grid-search method will take very long to run. Below we fit the model with $k = 3$.

```python
k = 3 #this is the number of knots (changes of slope)
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_scaled, quantile_levels)

n = len(y_scaled)
X = np.column_stack((np.ones(n), x_scaled))
for j in range(k):
    x_c = np.maximum(0, x_scaled - knots_init[j])
    X = np.column_stack((X, x_c))
md_init = sm.OLS(y_scaled, X).fit()
beta_init = md_init.params.values
print(knots_init)
print(knots_init * np.std(x_raw) + np.mean(x_raw)) #these are the initial knots in original scale
print(beta_init)
```

```
[-0.85912469  0.          0.85912469]
[32. 63. 94.]
[ 0.50608904  1.50671232 -0.2370822  -0.53040235 -0.42440376]
```

```python
md_nn_k = BrokenStickRegression(knots_init, beta_init)
#This code creates an instance of the BrokenStickRegression class with initial knots and beta values.
```

```python
optimizer = optim.Adam(md_nn_k.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

for epoch in range(10000):
    optimizer.zero_grad()
    y_pred = md_nn_k(x_torch)
    loss = loss_fn(y_pred, y_torch)
    loss.backward()
    optimizer.step()
    if epoch % 500 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')
```

```
Epoch 0, Loss: 0.0011482465779408813
Epoch 500, Loss: 0.0008120193961076438
Epoch 1000, Loss: 0.0008117101388052106
Epoch 1500, Loss: 0.0008117101970128715
Epoch 2000, Loss: 0.0008117840625345707
Epoch 2500, Loss: 0.0008117103716358542
Epoch 3000, Loss: 0.0008117103716358542
Epoch 3500, Loss: 0.0008117651450447738
Epoch 4000, Loss: 0.0008117102552205324
Epoch 4500, Loss: 0.0008117100223898888
Epoch 5000, Loss: 0.0008117099059745669
Epoch 5500, Loss: 0.0008117102552205324
Epoch 6000, Loss: 0.0008117340039461851
Epoch 6500, Loss: 0.0008117101388052106
Epoch 7000, Loss: 0.0008117136894725263
Epoch 7500, Loss: 0.0008117101388052106
Epoch 8000, Loss: 0.0008117130491882563
Epoch 8500, Loss: 0.0008117096731439233
Epoch 9000, Loss: 0.0008117114193737507
Epoch 9500, Loss: 0.0008117103134281933
```

The estimates of the knots are given below.

```python
c_est = md_nn_k.knots.detach().numpy() * np.std(x_raw) + np.mean(x_raw)
print(c_est)
```

```
[ 24.850475  65.16884  100.91917 ]
```

The rss value and the fitted values are computed as below.

```python
c = c_est
x = np.arange(1, n+1)
X = np.column_stack((np.ones(n), x))
if np.isscalar(c):
    c = [c]
for j in range(len(c)):
    x_c = np.maximum(0, x - c[j])
    X = np.column_stack((X, x_c))
md_k = sm.OLS(y, X).fit()
rss_k = np.sum(md_k.resid ** 2)
print(rss_k)
```

```
0.10071745300736597
```

```python
#plt.plot(tme, y, color= 'black')
plt.plot(tme, md_2.fittedvalues, color = 'blue', label='2 changes of slope')
plt.plot(tme, md_k.fittedvalues, color = 'red', label = 'k changes of slope')
#plt.axvline(c[0] - 1 + tme[0], color='green', linestyle='--')
#plt.axvline(c[1] - 1 + tme[0], color='green', linestyle='--')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fitted values from the $k = 3$ model seem to be quite close to the fitted values for the $k = 2$ model. Go back and run the method for $k = 6$. This should lead to overfitting and the fitted values will look a lot like the data.

## High-dimensional Linear Regression and Regularization

We now consider the model:
\begin{equation*}
  y_t = \beta_0 + \beta_1 (t - 1) + \beta_2 (t - 2)_+ + \beta_3 (t - 3)_+ + \dots + \beta_{n-1} (t - (n-1))_+ + \epsilon_t
\end{equation*}
We can write this as
\begin{equation*}
   y = X_{\text{full}} \beta + \epsilon
\end{equation*}
where $X_{\text{full}}$ is constructed as below.

```python
n = len(y)
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
 [  1. 122. 121. ...   1.   0.  -0.]
 [  1. 123. 122. ...   2.   1.   0.]
 [  1. 124. 123. ...   3.   2.   1.]]
```

If we fit this model without any regularization, we get the following.

```python
mdfull = sm.OLS(y, Xfull).fit()
print(mdfull.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  CAPOP   R-squared:                       1.000
Model:                            OLS   Adj. R-squared:                    nan
Method:                 Least Squares   F-statistic:                       nan
Date:                Tue, 30 Sep 2025   Prob (F-statistic):                nan
Time:                        16:51:38   Log-Likelihood:                 3409.6
No. Observations:                 125   AIC:                            -6569.
Df Residuals:                       0   BIC:                            -6216.
Df Model:                         124
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          7.3065        inf          0        nan         nan         nan
x1             0.0395        inf          0        nan         nan         nan
x2             0.0065        inf          0        nan         nan         nan
x3             0.0015        inf          0        nan         nan         nan
x4             0.0040        inf          0        nan         nan         nan
x5             0.0033        inf          0        nan         nan         nan
x6            -0.0119        inf         -0        nan         nan         nan
x7            -0.0042        inf         -0        nan         nan         nan
x8             0.0121        inf          0        nan         nan         nan
x9             0.0037        inf          0        nan         nan         nan
x10           -0.0016        inf         -0        nan         nan         nan
x11           -0.0011        inf         -0        nan         nan         nan
x12           -0.0003        inf         -0        nan         nan         nan
x13            0.0007        inf          0        nan         nan         nan
x14           -0.0094        inf         -0        nan         nan         nan
x15           -0.0179        inf         -0        nan         nan         nan
x16           -0.0042        inf         -0        nan         nan         nan
x17            0.0113        inf          0        nan         nan         nan
x18           -0.0038        inf         -0        nan         nan         nan
x19           -0.0050        inf         -0        nan         nan         nan
x20            0.0391        inf          0        nan         nan         nan
x21            0.0032        inf          0        nan         nan         nan
x22           -0.0153        inf         -0        nan         nan         nan
x23            0.0172        inf          0        nan         nan         nan
x24           -0.0060        inf         -0        nan         nan         nan
x25           -0.0208        inf         -0        nan         nan         nan
x26            0.0004        inf          0        nan         nan         nan
x27            0.0021        inf          0        nan         nan         nan
x28           -0.0057        inf         -0        nan         nan         nan
x29           -0.0032        inf         -0        nan         nan         nan
x30           -0.0024        inf         -0        nan         nan         nan
x31           -0.0124        inf         -0        nan         nan         nan
x32           -0.0076        inf         -0        nan         nan         nan
x33           -0.0003        inf         -0        nan         nan         nan
x34            0.0045        inf          0        nan         nan         nan
x35            0.0027        inf          0        nan         nan         nan
x36            0.0077        inf          0        nan         nan         nan
x37            0.0025        inf          0        nan         nan         nan
x38           -0.0096        inf         -0        nan         nan         nan
x39           -0.0002        inf         -0        nan         nan         nan
x40            0.0048        inf          0        nan         nan         nan
x41            0.0164        inf          0        nan         nan         nan
x42            0.0261        inf          0        nan         nan         nan
x43            0.0285        inf          0        nan         nan         nan
x44           -0.0447        inf         -0        nan         nan         nan
x45           -0.0067        inf         -0        nan         nan         nan
x46           -0.0209        inf         -0        nan         nan         nan
x47            0.0054        inf          0        nan         nan         nan
x48           -0.0048        inf         -0        nan         nan         nan
x49            0.0034        inf          0        nan         nan         nan
x50            0.0056        inf          0        nan         nan         nan
x51            0.0095        inf          0        nan         nan         nan
x52            0.0021        inf          0        nan         nan         nan
x53            0.0076        inf          0        nan         nan         nan
x54           -0.0120        inf         -0        nan         nan         nan
x55           -0.0097        inf         -0        nan         nan         nan
x56            0.0133        inf          0        nan         nan         nan
x57           -0.0038        inf         -0        nan         nan         nan
x58            0.0029        inf          0        nan         nan         nan
x59           -0.0036        inf         -0        nan         nan         nan
x60           -0.0130        inf         -0        nan         nan         nan
x61            0.0130        inf          0        nan         nan         nan
x62           -0.0045        inf         -0        nan         nan         nan
x63         5.425e-05        inf          0        nan         nan         nan
x64           -0.0073        inf         -0        nan         nan         nan
x65           -0.0033        inf         -0        nan         nan         nan
x66           -0.0090        inf         -0        nan         nan         nan
x67            0.0021        inf          0        nan         nan         nan
x68           -0.0054        inf         -0        nan         nan         nan
x69            0.0049        inf          0        nan         nan         nan
x70           -0.0031        inf         -0        nan         nan         nan
x71            0.0055        inf          0        nan         nan         nan
x72           -0.0069        inf         -0        nan         nan         nan
x73            0.0020        inf          0        nan         nan         nan
x74            0.0008        inf          0        nan         nan         nan
x75            0.0025        inf          0        nan         nan         nan
x76            0.0013        inf          0        nan         nan         nan
x77            0.0005        inf          0        nan         nan         nan
x78            0.0026        inf          0        nan         nan         nan
x79           -0.0031        inf         -0        nan         nan         nan
x80            0.0049        inf          0        nan         nan         nan
x81           -0.0029        inf         -0        nan         nan         nan
x82            0.0016        inf          0        nan         nan         nan
x83           -0.0002        inf         -0        nan         nan         nan
x84           -0.0026        inf         -0        nan         nan         nan
x85            0.0039        inf          0        nan         nan         nan
x86            0.0019        inf          0        nan         nan         nan
x87        -9.855e-05        inf         -0        nan         nan         nan
x88           -0.0002        inf         -0        nan         nan         nan
x89            0.0017        inf          0        nan         nan         nan
x90           -0.0014        inf         -0        nan         nan         nan
x91           -0.0094        inf         -0        nan         nan         nan
x92           -0.0003        inf         -0        nan         nan         nan
x93           -0.0063        inf         -0        nan         nan         nan
x94           -0.0033        inf         -0        nan         nan         nan
x95            0.0002        inf          0        nan         nan         nan
x96            0.0035        inf          0        nan         nan         nan
x97            0.0046        inf          0        nan         nan         nan
x98            0.0007        inf          0        nan         nan         nan
x99           -0.0003        inf         -0        nan         nan         nan
x100           0.0111        inf          0        nan         nan         nan
x101          -0.0108        inf         -0        nan         nan         nan
x102          -0.0030        inf         -0        nan         nan         nan
x103          -0.0004        inf         -0        nan         nan         nan
x104          -0.0018        inf         -0        nan         nan         nan
x105          -0.0020        inf         -0        nan         nan         nan
x106          -0.0017        inf         -0        nan         nan         nan
x107           0.0010        inf          0        nan         nan         nan
x108           0.0034        inf          0        nan         nan         nan
x109         -1.6e-05        inf         -0        nan         nan         nan
x110       -5.495e-05        inf         -0        nan         nan         nan
x111          -0.0012        inf         -0        nan         nan         nan
x112          -0.0003        inf         -0        nan         nan         nan
x113       -4.045e-05        inf         -0        nan         nan         nan
x114           0.0005        inf          0        nan         nan         nan
x115          -0.0005        inf         -0        nan         nan         nan
x116          -0.0019        inf         -0        nan         nan         nan
x117          -0.0015        inf         -0        nan         nan         nan
x118          -0.0023        inf         -0        nan         nan         nan
x119          -0.0025        inf         -0        nan         nan         nan
x120           0.0021        inf          0        nan         nan         nan
x121          -0.0118        inf         -0        nan         nan         nan
x122           0.0096        inf          0        nan         nan         nan
x123           0.0014        inf          0        nan         nan         nan
x124           0.0045        inf          0        nan         nan         nan
==============================================================================
Omnibus:                        2.109   Durbin-Watson:                   0.015
Prob(Omnibus):                  0.348   Jarque-Bera (JB):                1.923
Skew:                          -0.203   Prob(JB):                        0.382
Kurtosis:                       2.548   Cond. No.                     1.78e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.78e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
/Users/aditya/mambaforge/envs/stat153fall2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1795: RuntimeWarning: divide by zero encountered in divide
  return 1 - (np.divide(self.nobs - self.k_constant, self.df_resid)
/Users/aditya/mambaforge/envs/stat153fall2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1795: RuntimeWarning: invalid value encountered in scalar multiply
  return 1 - (np.divide(self.nobs - self.k_constant, self.df_resid)
/Users/aditya/mambaforge/envs/stat153fall2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1717: RuntimeWarning: divide by zero encountered in scalar divide
  return np.dot(wresid, wresid) / self.df_resid
```

In this unregularized estimation, the estimate of $\beta_0$ equals $y_1$, the estimate of $\beta_1$ is $y_2 - y_1$, and the estimate of $\beta_j$ is $y_{j+1} - 2 y_j + y_{j-1}$ for $j = 2, \dots, n-1$. Let us check this.

```python
print(y[0])
print(y[1] - y[0])
print(y[2] - y[1] - y[1] + y[0])
```

```
7.306531398939505
0.03947881097378758
0.006542546627510859
```

We shall study regularization in the next lecture.

---

[← Broken-stick Regression or Change of Slope Model](02-broken-stick-regression-or-change-of-slope-model.md) · [Up: contents](index.md)
