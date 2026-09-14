---
title: Model Fitting using PyTorch
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Model Fitting using PyTorch

**Source:** [`CodeLectureTwentyFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Our next topic involves some neural network models for time series. The main model that we shall look at is Recurrent Neural Networks (RNN). We shall fit these models using functions from the Python library PyTorch. This is a general optimization library that can be used to fit many models including neural networks. To illustrate how PyTorch works, let us first look at some simple examples of model fitting using PyTorch.

## Model One: Piecewise Linear Trend Fitting

Given a time series $y_t$, suppose we want to fit the model:
\begin{equation*}
   y_t = \beta_0 + \beta_1 t + \beta_2 (t - c_1)_+ + \dots + \beta_{k+1} (t - c_k)_+ + \epsilon_t.
\end{equation*}
We can do this via minimizing the least squares:
\begin{align*}
   \sum_{t=1}^n \left(y_t - \beta_0 - \beta_1 t - \beta_2 (t  - c_1)_+ - \dots - \beta_{k+1} (t - c_k)_+ \right)^2.
\end{align*}
If $k$ is not very big, we can minimize the above without any regularization. If $k$ becomes large, then we can add either an $L_1$ or $L_2$ regularization: $\sum_{j=2}^{k+1}  \beta_j^2$ or $\sum_{j=2}^{k+1}  |\beta_j|$.

Below we use PyTorch to fit this model. Let us first import the torch libraries.

```python
import torch
import torch.nn as nn
import torch.optim as optim
```

The following is the code for representing the piecewise linear trend model in PyTorch. PyTorch organizes models as classes.

```python
class PiecewiseLinearModel(nn.Module):
    def __init__(self, knots_init, beta_init):
        super().__init__()
        self.num_knots = len(knots_init)
        self.beta = nn.Parameter(torch.tensor(beta_init, dtype=torch.float32))
        self.knots = nn.Parameter(torch.tensor(knots_init, dtype=torch.float32))

    def forward(self, x):
        knots_sorted, _ = torch.sort(self.knots)
        out = self.beta[0] + self.beta[1] * x
        for j in range(self.num_knots):
            out += self.beta[j + 2] * torch.relu(x - knots_sorted[j])
        return out
```

Let us apply this model to the following dataset from FRED.

```python
ttlcons = pd.read_csv('TTLCONS_17Nov2025.csv')
print(ttlcons.head(10))
print(ttlcons.tail(10))
y_raw = np.log(ttlcons['TTLCONS'])
n = len(y_raw)
x_raw = np.arange(1, n+1)
plt.figure(figsize = (12, 6))
plt.plot(y_raw)
plt.xlabel("Time (months)")
plt.ylabel('Log(Millions of Dollars)')
plt.title("Logarithms of Total Construction Spending in the United States")
plt.show()
```

```
observation_date  TTLCONS
0       1993-01-01   458080
1       1993-02-01   462967
2       1993-03-01   458399
3       1993-04-01   469425
4       1993-05-01   468998
5       1993-06-01   480247
6       1993-07-01   483571
7       1993-08-01   491494
8       1993-09-01   497297
9       1993-10-01   492823
    observation_date  TTLCONS
382       2024-11-01  2192932
383       2024-12-01  2176642
384       2025-01-01  2169595
385       2025-02-01  2165431
386       2025-03-01  2150847
387       2025-04-01  2153440
388       2025-05-01  2149124
389       2025-06-01  2160743
390       2025-07-01  2165016
391       2025-08-01  2169468
```

*(1 figure omitted — see the original notebook.)*

We do not apply the model to the raw data but we scale the raw data first. The algorithm for parameter fitting will work better with scaled data as opposed to raw data.

The code below first standardizes the raw input arrays `y_raw` and `x_raw` by subtracting their means and dividing by their standard deviations, resulting in `y_scaled` and `x_scaled`, respectively. This scaling step ensures that both inputs have mean 0 and standard deviation 1, which helps neural network training converge faster and more reliably. After scaling, the arrays are converted into PyTorch tensors (`y_torch` and `x_torch`) with `dtype=torch.float32`, and an additional singleton dimension is added using `unsqueeze(1)` to ensure each data point is treated as a one-dimensional feature vector. Conversion to PyTorch tensors is necessary because PyTorch models and optimization routines (like gradient computation and parameter updates) operate on tensors, not on NumPy arrays.

```python
#Below we first scale y_raw and x_raw and then convert them to tensors for training the neural network model
y_scaled = (y_raw - np.mean(y_raw))/(np.std(y_raw))
x_scaled = (x_raw - np.mean(x_raw))/(np.std(x_raw))
y_torch = torch.tensor(y_scaled, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)
```

We will fit the piecewise linear trend model for a fixed $k$ and use PyTorch for estimating the parameters. The first step is to obtain suitable initial estimates for the parameters. These are deduced as follows. We take $c_1, \dots, c_k$ to be quantiles of the scaled covariate at equal levels. Then we fit the model with $c_1, \dots, c_k$ fixed at these initial values, and obtain the initial values of the coefficients $\beta_2, \dots, \beta_{k+1}$.

```python
k = 6 #this is the number of knots
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_scaled, quantile_levels)

n = len(y_scaled)
X = np.column_stack([np.ones(n), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float))*(x_scaled-knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(y_scaled, X).fit()
beta_init = md_init.params.values
print(knots_init)
print(beta_init)
```

```
[-1.23402709 -0.74041626 -0.24680542  0.24680542  0.74041626  1.23402709]
[ 1.0710101   1.74855865 -0.35825556  0.34626208 -4.09160644  4.7038143
 -0.94807517  0.77804141]
```

The next code line `md_PiecewiseLinear = PiecewiseLinearModel(knots_init=knots_init, beta_init=beta_init)` creates an instance of the custom neural network model `PiecewiseLinearModel`. It initializes the learnable parameters of the model: the knot locations are set to the values provided in `knots_init`, and the coefficients are set to `beta_init`. This prepares the model for training by defining its initial piecewise linear structure.

```python
md_PiecewiseLinear = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
#This code creates an instance of our custom neural network class
#It also initializes the knots at knots_init
```

The next block of code sets up and runs the training loop for the `PiecewiseLinearModel`. The `Adam` optimizer is initialized with the model’s parameters and a learning rate of 0.01, and the loss function is set to mean squared error (`MSELoss`). For 20,000 epochs, the code repeatedly performs one training step: it clears previous gradients with `optimizer.zero_grad()`, computes predictions `y_pred` by passing `x_torch` through the model, evaluates the loss between predictions and true values, backpropagates the loss with `loss.backward()`, and updates the model parameters using `optimizer.step()`. Every 100 epochs, the current epoch and loss value are printed to monitor training progress. Running the code multiple times may be necessary to ensure good convergence, especially for non-convex optimization problems.

```python
optimizer = optim.Adam(md_PiecewiseLinear.parameters(), lr = 0.01)
#the above line tells Python to create an Adam optimizer that will update all parameters of md_PiecewiseLinear during training, using a learning rate of 0.01.
loss_fn = nn.MSELoss()

for epoch in range(20000):
    optimizer.zero_grad()
    y_pred = md_PiecewiseLinear(x_torch)
    loss = loss_fn(y_pred, y_torch)
    loss.backward() #calulates gradients
    optimizer.step() #updates parameters using gradients
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
#Run this code a few times to be sure of convergence.
```

```
Epoch 0, Loss: 0.0079
Epoch 100, Loss: 0.0062
Epoch 200, Loss: 0.0059
Epoch 300, Loss: 0.0057
Epoch 400, Loss: 0.0056
Epoch 500, Loss: 0.0055
Epoch 600, Loss: 0.0054
Epoch 700, Loss: 0.0053
Epoch 800, Loss: 0.0053
Epoch 900, Loss: 0.0052
Epoch 1000, Loss: 0.0052
Epoch 1100, Loss: 0.0051
Epoch 1200, Loss: 0.0051
Epoch 1300, Loss: 0.0051
Epoch 1400, Loss: 0.0051
Epoch 1500, Loss: 0.0050
Epoch 1600, Loss: 0.0050
Epoch 1700, Loss: 0.0050
Epoch 1800, Loss: 0.0050
Epoch 1900, Loss: 0.0050
Epoch 2000, Loss: 0.0050
Epoch 2100, Loss: 0.0050
Epoch 2200, Loss: 0.0050
Epoch 2300, Loss: 0.0050
Epoch 2400, Loss: 0.0049
Epoch 2500, Loss: 0.0049
Epoch 2600, Loss: 0.0049
Epoch 2700, Loss: 0.0052
Epoch 2800, Loss: 0.0049
Epoch 2900, Loss: 0.0049
Epoch 3000, Loss: 0.0049
Epoch 3100, Loss: 0.0049
Epoch 3200, Loss: 0.0049
Epoch 3300, Loss: 0.0049
Epoch 3400, Loss: 0.0049
Epoch 3500, Loss: 0.0049
Epoch 3600, Loss: 0.0049
Epoch 3700, Loss: 0.0049
Epoch 3800, Loss: 0.0049
Epoch 3900, Loss: 0.0049
Epoch 4000, Loss: 0.0049
Epoch 4100, Loss: 0.0049
Epoch 4200, Loss: 0.0049
Epoch 4300, Loss: 0.0049
Epoch 4400, Loss: 0.0049
Epoch 4500, Loss: 0.0049
Epoch 4600, Loss: 0.0049
Epoch 4700, Loss: 0.0049
Epoch 4800, Loss: 0.0049
Epoch 4900, Loss: 0.0049
Epoch 5000, Loss: 0.0049
Epoch 5100, Loss: 0.0049
Epoch 5200, Loss: 0.0049
Epoch 5300, Loss: 0.0049
Epoch 5400, Loss: 0.0049
Epoch 5500, Loss: 0.0049
Epoch 5600, Loss: 0.0049
Epoch 5700, Loss: 0.0049
Epoch 5800, Loss: 0.0049
Epoch 5900, Loss: 0.0049
Epoch 6000, Loss: 0.0049
Epoch 6100, Loss: 0.0049
Epoch 6200, Loss: 0.0049
Epoch 6300, Loss: 0.0048
Epoch 6400, Loss: 0.0048
Epoch 6500, Loss: 0.0048
Epoch 6600, Loss: 0.0048
Epoch 6700, Loss: 0.0048
Epoch 6800, Loss: 0.0052
Epoch 6900, Loss: 0.0048
Epoch 7000, Loss: 0.0049
Epoch 7100, Loss: 0.0048
Epoch 7200, Loss: 0.0054
Epoch 7300, Loss: 0.0048
Epoch 7400, Loss: 0.0048
Epoch 7500, Loss: 0.0048
Epoch 7600, Loss: 0.0048
Epoch 7700, Loss: 0.0048
Epoch 7800, Loss: 0.0048
Epoch 7900, Loss: 0.0048
Epoch 8000, Loss: 0.0048
Epoch 8100, Loss: 0.0048
Epoch 8200, Loss: 0.0048
Epoch 8300, Loss: 0.0048
Epoch 8400, Loss: 0.0048
Epoch 8500, Loss: 0.0048
Epoch 8600, Loss: 0.0048
Epoch 8700, Loss: 0.0048
Epoch 8800, Loss: 0.0048
Epoch 8900, Loss: 0.0048
Epoch 9000, Loss: 0.0048
Epoch 9100, Loss: 0.0048
Epoch 9200, Loss: 0.0050
Epoch 9300, Loss: 0.0048
Epoch 9400, Loss: 0.0048
Epoch 9500, Loss: 0.0048
Epoch 9600, Loss: 0.0048
Epoch 9700, Loss: 0.0049
Epoch 9800, Loss: 0.0048
Epoch 9900, Loss: 0.0048
Epoch 10000, Loss: 0.0048
Epoch 10100, Loss: 0.0048
Epoch 10200, Loss: 0.0048
Epoch 10300, Loss: 0.0048
Epoch 10400, Loss: 0.0048
Epoch 10500, Loss: 0.0048
Epoch 10600, Loss: 0.0048
Epoch 10700, Loss: 0.0048
Epoch 10800, Loss: 0.0048
Epoch 10900, Loss: 0.0048
Epoch 11000, Loss: 0.0048
Epoch 11100, Loss: 0.0048
Epoch 11200, Loss: 0.0048
Epoch 11300, Loss: 0.0048
Epoch 11400, Loss: 0.0048
Epoch 11500, Loss: 0.0048
Epoch 11600, Loss: 0.0048
Epoch 11700, Loss: 0.0048
Epoch 11800, Loss: 0.0048
Epoch 11900, Loss: 0.0048
Epoch 12000, Loss: 0.0048
Epoch 12100, Loss: 0.0048
Epoch 12200, Loss: 0.0048
Epoch 12300, Loss: 0.0048
Epoch 12400, Loss: 0.0048
Epoch 12500, Loss: 0.0048
Epoch 12600, Loss: 0.0048
Epoch 12700, Loss: 0.0048
Epoch 12800, Loss: 0.0048
Epoch 12900, Loss: 0.0048
Epoch 13000, Loss: 0.0048
Epoch 13100, Loss: 0.0048
Epoch 13200, Loss: 0.0055
Epoch 13300, Loss: 0.0048
Epoch 13400, Loss: 0.0048
Epoch 13500, Loss: 0.0048
Epoch 13600, Loss: 0.0048
Epoch 13700, Loss: 0.0048
Epoch 13800, Loss: 0.0048
Epoch 13900, Loss: 0.0048
Epoch 14000, Loss: 0.0048
Epoch 14100, Loss: 0.0048
Epoch 14200, Loss: 0.0049
Epoch 14300, Loss: 0.0048
Epoch 14400, Loss: 0.0048
Epoch 14500, Loss: 0.0048
Epoch 14600, Loss: 0.0048
Epoch 14700, Loss: 0.0048
Epoch 14800, Loss: 0.0048
Epoch 14900, Loss: 0.0048
Epoch 15000, Loss: 0.0048
Epoch 15100, Loss: 0.0048
Epoch 15200, Loss: 0.0048
Epoch 15300, Loss: 0.0049
Epoch 15400, Loss: 0.0048
Epoch 15500, Loss: 0.0048
Epoch 15600, Loss: 0.0048
Epoch 15700, Loss: 0.0048
Epoch 15800, Loss: 0.0048
Epoch 15900, Loss: 0.0048
Epoch 16000, Loss: 0.0048
Epoch 16100, Loss: 0.0048
Epoch 16200, Loss: 0.0048
Epoch 16300, Loss: 0.0048
Epoch 16400, Loss: 0.0048
Epoch 16500, Loss: 0.0048
Epoch 16600, Loss: 0.0048
Epoch 16700, Loss: 0.0048
Epoch 16800, Loss: 0.0048
Epoch 16900, Loss: 0.0048
Epoch 17000, Loss: 0.0048
Epoch 17100, Loss: 0.0048
Epoch 17200, Loss: 0.0048
Epoch 17300, Loss: 0.0048
Epoch 17400, Loss: 0.0048
Epoch 17500, Loss: 0.0048
Epoch 17600, Loss: 0.0048
Epoch 17700, Loss: 0.0048
Epoch 17800, Loss: 0.0048
Epoch 17900, Loss: 0.0048
Epoch 18000, Loss: 0.0048
Epoch 18100, Loss: 0.0048
Epoch 18200, Loss: 0.0048
Epoch 18300, Loss: 0.0054
Epoch 18400, Loss: 0.0048
Epoch 18500, Loss: 0.0048
Epoch 18600, Loss: 0.0048
Epoch 18700, Loss: 0.0048
Epoch 18800, Loss: 0.0048
Epoch 18900, Loss: 0.0048
Epoch 19000, Loss: 0.0048
Epoch 19100, Loss: 0.0048
Epoch 19200, Loss: 0.0048
Epoch 19300, Loss: 0.0048
Epoch 19400, Loss: 0.0048
Epoch 19500, Loss: 0.0048
Epoch 19600, Loss: 0.0048
Epoch 19700, Loss: 0.0048
Epoch 19800, Loss: 0.0048
Epoch 19900, Loss: 0.0048
```

The next code prints out the current loss value, the estimated model coefficients (`beta`), and the estimated knot locations after training. The `detach().numpy()` calls are used to move each tensor from the computation graph to a regular NumPy array so they can be easily printed or further processed without tracking gradients.

```python
print(loss.detach().numpy())
print(md_PiecewiseLinear.beta.detach().numpy())
print(md_PiecewiseLinear.knots.detach().numpy())
```

```
0.0047988915
[ 0.99718404  1.7058834  -1.6600022   2.086846   -5.034503    5.0382504
 -1.4400616   1.3958895 ]
[-0.84136385 -0.69282526 -0.2414546   0.19208266  0.81079537  1.0259839 ]
```

The next code computes the model’s fitted values by passing `x_torch` through the trained `PiecewiseLinearModel` and applying `.detach().numpy()` to convert the output tensor into a NumPy array, which disconnects it from the PyTorch computation graph. The fitted values (`nn_fits`) represent the model’s predicted outputs on the training data and are printed for inspection.

```python
fitvals = md_PiecewiseLinear(x_torch).detach().numpy()
fitvals_original_scale = (fitvals * np.std(y_raw)) + np.mean(y_raw)
```

```python
plt.figure(figsize = (12, 6))
plt.plot(y_raw, color = 'blue', label = 'Data')
plt.plot(fitvals_original_scale, color = 'red', label = 'PyTorch Fitted Values')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Adding a Regularizer

Suppose we increase the number of knots (go back to the previous code and increase $k$ say to 50). Then the fitted values will resemble the actual data i.e., we will overfit. To fix overfitting, we can employ  regularization.

```python
k = 50 #this is the number of knots
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_scaled, quantile_levels)

n = len(y_scaled)
X = np.column_stack([np.ones(n), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float))*(x_scaled-knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(y_scaled, X).fit()
beta_init = md_init.params.values
print(knots_init)
print(beta_init)
```

```
[-1.65988742 -1.59213692 -1.52438641 -1.4566359  -1.3888854  -1.32113489
 -1.25338438 -1.18563387 -1.11788337 -1.05013286 -0.98238235 -0.91463185
 -0.84688134 -0.77913083 -0.71138032 -0.64362982 -0.57587931 -0.5081288
 -0.4403783  -0.37262779 -0.30487728 -0.23712677 -0.16937627 -0.10162576
 -0.03387525  0.03387525  0.10162576  0.16937627  0.23712677  0.30487728
  0.37262779  0.4403783   0.5081288   0.57587931  0.64362982  0.71138032
  0.77913083  0.84688134  0.91463185  0.98238235  1.05013286  1.11788337
  1.18563387  1.25338438  1.32113489  1.3888854   1.4566359   1.52438641
  1.59213692  1.65988742]
[ 3.70479589  3.31920328 -0.61975363 -2.12706708 -0.23358562  2.23215961
 -0.56357887 -1.18544788  0.9441146   1.09234493 -1.82968666  2.13420425
 -2.74675755  1.25348588 -1.03545406 -1.23588121  1.39025268  2.2545587
 -0.53448749 -0.13166522  1.67493038 -4.31556708 -1.06919549  2.09639669
 -2.63356884 -1.71921202 -1.14300924  2.02097122  0.79213502  2.42831366
  1.81811678 -1.14015569  0.16206003  2.60669411 -3.07219589  3.30831531
 -3.56317409  1.80541613 -1.50718342  0.63154413 -1.1804686  -1.04151303
  5.27861806 -4.99525688  3.62377708 -0.99329926  2.63499583 -4.73988759
  3.47316719 -2.38590382 -1.86300276  0.30008223]
```

```python
md_large_k = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
```

As we have seen previously, natural regularizers here are $\lambda \sum_{j=2}^{k+1} |\beta_j|$ or $\lambda \sum_{j=2}^{k+1} \beta_j^2$ ($\lambda$ needs to be chosen carefully).

```python
#Adding a regularizer to the loss function.
optimizer = optim.Adam(md_large_k.parameters(), lr = 0.01)
loss_fn = nn.MSELoss()
lambda_l1 = 0.0007 #this works pretty well
#lambda_l2 = .002

for epoch in range(10000):
    optimizer.zero_grad()
    y_pred = md_large_k(x_torch)
    mse_loss = loss_fn(y_pred, y_torch)
    l1_penalty = torch.norm(md_large_k.beta[2:], p = 1)
    #l2_penalty = torch.sum(md_large_k.beta[2:] ** 2)
    loss = mse_loss + lambda_l1 * l1_penalty
    #loss = mse_loss + lambda_l2 * l2_penalty
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
#Run this code a few times to be sure of convergence.
```

```
Epoch 0, Loss: 0.0676
Epoch 100, Loss: 0.0663
Epoch 200, Loss: 0.0652
Epoch 300, Loss: 0.0640
Epoch 400, Loss: 0.0627
Epoch 500, Loss: 0.0614
Epoch 600, Loss: 0.0601
Epoch 700, Loss: 0.0587
Epoch 800, Loss: 0.0571
Epoch 900, Loss: 0.0556
Epoch 1000, Loss: 0.0540
Epoch 1100, Loss: 0.0526
Epoch 1200, Loss: 0.0513
Epoch 1300, Loss: 0.0498
Epoch 1400, Loss: 0.0485
Epoch 1500, Loss: 0.0474
Epoch 1600, Loss: 0.0464
Epoch 1700, Loss: 0.0454
Epoch 1800, Loss: 0.0446
Epoch 1900, Loss: 0.0438
Epoch 2000, Loss: 0.0425
Epoch 2100, Loss: 0.0416
Epoch 2200, Loss: 0.0409
Epoch 2300, Loss: 0.0401
Epoch 2400, Loss: 0.0393
Epoch 2500, Loss: 0.0385
Epoch 2600, Loss: 0.0376
Epoch 2700, Loss: 0.0369
Epoch 2800, Loss: 0.0361
Epoch 2900, Loss: 0.0353
Epoch 3000, Loss: 0.0345
Epoch 3100, Loss: 0.0346
Epoch 3200, Loss: 0.0333
Epoch 3300, Loss: 0.0322
Epoch 3400, Loss: 0.0315
Epoch 3500, Loss: 0.0317
Epoch 3600, Loss: 0.0304
Epoch 3700, Loss: 0.0301
Epoch 3800, Loss: 0.0295
Epoch 3900, Loss: 0.0298
Epoch 4000, Loss: 0.0289
Epoch 4100, Loss: 0.0282
Epoch 4200, Loss: 0.0278
Epoch 4300, Loss: 0.0274
Epoch 4400, Loss: 0.0270
Epoch 4500, Loss: 0.0266
Epoch 4600, Loss: 0.0262
Epoch 4700, Loss: 0.0258
Epoch 4800, Loss: 0.0255
Epoch 4900, Loss: 0.0251
Epoch 5000, Loss: 0.0248
Epoch 5100, Loss: 0.0244
Epoch 5200, Loss: 0.0241
Epoch 5300, Loss: 0.0237
Epoch 5400, Loss: 0.0234
Epoch 5500, Loss: 0.0230
Epoch 5600, Loss: 0.0228
Epoch 5700, Loss: 0.0224
Epoch 5800, Loss: 0.0221
Epoch 5900, Loss: 0.0219
Epoch 6000, Loss: 0.0217
Epoch 6100, Loss: 0.0214
Epoch 6200, Loss: 0.0212
Epoch 6300, Loss: 0.0210
Epoch 6400, Loss: 0.0228
Epoch 6500, Loss: 0.0206
Epoch 6600, Loss: 0.0209
Epoch 6700, Loss: 0.0203
Epoch 6800, Loss: 0.0201
Epoch 6900, Loss: 0.0199
Epoch 7000, Loss: 0.0199
Epoch 7100, Loss: 0.0196
Epoch 7200, Loss: 0.0193
Epoch 7300, Loss: 0.0192
Epoch 7400, Loss: 0.0190
Epoch 7500, Loss: 0.0190
Epoch 7600, Loss: 0.0186
Epoch 7700, Loss: 0.0185
Epoch 7800, Loss: 0.0192
Epoch 7900, Loss: 0.0182
Epoch 8000, Loss: 0.0183
Epoch 8100, Loss: 0.0179
Epoch 8200, Loss: 0.0178
Epoch 8300, Loss: 0.0185
Epoch 8400, Loss: 0.0176
Epoch 8500, Loss: 0.0175
Epoch 8600, Loss: 0.0174
Epoch 8700, Loss: 0.0174
Epoch 8800, Loss: 0.0172
Epoch 8900, Loss: 0.0171
Epoch 9000, Loss: 0.0171
Epoch 9100, Loss: 0.0179
Epoch 9200, Loss: 0.0169
Epoch 9300, Loss: 0.0169
Epoch 9400, Loss: 0.0176
Epoch 9500, Loss: 0.0167
Epoch 9600, Loss: 0.0169
Epoch 9700, Loss: 0.0166
Epoch 9800, Loss: 0.0166
Epoch 9900, Loss: 0.0165
```

```python
fitvals = md_large_k(x_torch).detach().numpy()
fitvals_original_scale = (fitvals * np.std(y_raw)) + np.mean(y_raw)
plt.figure(figsize = (12, 6))
plt.plot(y_raw, color = 'blue', label = 'Data')
plt.plot(fitvals_original_scale, color = 'red', label = 'PyTorch Fitted Values')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## MA(1) and AR(1) model fitting via PyTorch

### MA(1) model fitting

The algorithms from PyTorch can also be used to fit classical time series models. Here we illustrate how to fit MA(1) and AR(1) models. We will use the varve dataset from Lecture 21.

```python
varve_data = pd.read_csv("varve.csv")
yraw = varve_data['x']
plt.figure(figsize = (12, 6))
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

In Lecture 20, we took logarithms of this dataset, then differenced, and then fitted the MA(1) model. We will now fit this model (as well as AR(1)) using PyTorch (instead of ARIMA).  First let us recall how we fit this using the ARIMA function.

```python
from statsmodels.tsa.arima.model import ARIMA
ylogdiff = np.diff(np.log(yraw))
mamod_ARIMA = ARIMA(ylogdiff, order = (0, 0, 1)).fit()
print(mamod_ARIMA.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -440.678
Date:                Tue, 25 Nov 2025   AIC                            887.356
Time:                        16:16:54   BIC                            900.707
Sample:                             0   HQIC                           892.541
                                - 633
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0013      0.004     -0.280      0.779      -0.010       0.008
ma.L1         -0.7710      0.023    -33.056      0.000      -0.817      -0.725
sigma2         0.2353      0.012     18.881      0.000       0.211       0.260
===================================================================================
Ljung-Box (L1) (Q):                   9.16   Jarque-Bera (JB):                 7.58
Prob(Q):                              0.00   Prob(JB):                         0.02
Heteroskedasticity (H):               0.95   Skew:                            -0.22
Prob(H) (two-sided):                  0.69   Kurtosis:                         3.30
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

We next fit the MA(1) model using PyTorch. Below we describe the optimization problem that we need to solve in order to estimate the MA(1) parameters $\mu, \theta, \sigma$. Recall that the MA(1) model is given by
\begin{equation*}
  y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}
\end{equation*}
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. The likelihood is $f_{y_1, \dots, y_n}(y_1, \dots, y_n)$ can be written in terms of the covariance matrix of $y_1, \dots, y_n$. This is somewhat complicated. A simplification trick is to condition on $\epsilon = 0$ i.e., one attempts to write the conditional likelihood:
\begin{equation*}
   f_{y_1, \dots, y_n \mid \epsilon_0 = 0}(y_1, \dots, y_n).
\end{equation*}
This likelihood is much simpler to write by breaking it down as
\begin{equation*}
  f_{y_1 \mid \epsilon_0 = 0}(y_1) f_{y_2 \mid y_1, \epsilon_0 = 0}(y_2) f_{y_3 \mid y_1, y_2, \epsilon_0 = 0}(y_3) \dots f_{y_n \mid y_1, \dots, y_{n-1}, \epsilon_0 = 0}(y_n)
\end{equation*}
Each of the terms above can be written explicitly. Let $\hat{\epsilon}_1 = y_1 - \mu$ and, for $t = 2, \dots, n$,
\begin{equation*}
    \hat{\epsilon}_t = y_t- \mu - \theta \hat{\epsilon}_{t-1}
\end{equation*}
Then
\begin{equation*}
   f_{y_1 \mid \epsilon_0 = 0}(y_1) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{(y_1 - \mu)^2}{2 \sigma^2} \right)
\end{equation*}
and
\begin{align*}
  f_{y_t \mid y_1, \dots, y_{t-1}, \epsilon = 0}(y_t) &= f_{y_t \mid \epsilon_1 = \hat{\epsilon}_1, \epsilon_2 = \hat{\epsilon}_2, \dots, \epsilon_{t-1} = \hat{\epsilon}_{t-1}, \epsilon_0 = 0}(y_t) \\
  &= f_{\epsilon_t}(y_t - \mu - \theta \hat{\epsilon}_{t-1}) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{1}{2 \sigma^2} (y_t - \mu - \theta \hat{\epsilon}_{t-1})^2 \right).
\end{align*}
Thus the conditional likelihood given $\epsilon_0 = 0$ is given by
\begin{align*}
   \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{(y_1 - \mu)^2}{2 \sigma^2} \right) \left[\prod_{t=2}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{1}{2 \sigma^2} (y_t - \mu - \theta \hat{\epsilon}_{t-1})^2 \right) \right] = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\hat{\epsilon}_1^2}{2 \sigma^2} \right) \left[\prod_{t=2}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\hat{\epsilon}_t^2}{2 \sigma^2}  \right) \right]
\end{align*}
so that the negative log-likelihood  becomes:
\begin{align*}
   \frac{n}{2} \log (2 \pi) + 0.5 \sum_{t=1}^n \left(\log \sigma^2 + \frac{\hat{\epsilon}_t^2}{\sigma^2} \right).
\end{align*}

```python
class MA1Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.mu = nn.Parameter(torch.tensor(0.0)) #initialized at 0
        self.theta = nn.Parameter(torch.tensor(0.0)) #initialized at 0
        self.log_sigma = nn.Parameter(torch.tensor(0.0))  # log(sigma)

    def forward(self, y): #this function computes the negative log-likelihood given data y
        n = len(y)
        eps_list = []
        eps_prev = y[0] - self.mu  # ε_0
        eps_list.append(eps_prev)
        for t in range(1, n):
            eps_t = y[t] - self.mu - self.theta * eps_prev
            eps_list.append(eps_t)
            eps_prev = eps_t
        eps = torch.stack(eps_list)
        sigma = torch.exp(self.log_sigma)
        nll = (0.5 * n * np.log(2 * np.pi)) + 0.5 * torch.sum(torch.log(sigma**2) + (eps**2) / (sigma**2))
        return nll
```

```python
ylogdiff_tensor = torch.tensor(ylogdiff, dtype = torch.float32)
mamod = MA1Model()
optimizer = optim.Adam(mamod.parameters(), lr=0.001)
for epoch in range(4000):
    optimizer.zero_grad()
    loss = mamod(ylogdiff_tensor)
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        sigma = torch.exp(mamod.log_sigma).item()
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}, mu: {mamod.mu.item():.4f}, "
              f"theta: {mamod.theta.item():.4f}, sigma: {sigma:.4f}")
```

```
Epoch 0, Loss: 686.6678, mu: -0.0010, theta: -0.0010, sigma: 0.9990
Epoch 100, Loss: 637.9557, mu: -0.0011, theta: -0.1006, sigma: 0.9050
Epoch 200, Loss: 593.8228, mu: -0.0011, theta: -0.1994, sigma: 0.8229
Epoch 300, Loss: 554.7609, mu: -0.0010, theta: -0.2977, sigma: 0.7518
Epoch 400, Loss: 521.1600, mu: -0.0011, theta: -0.3950, sigma: 0.6909
Epoch 500, Loss: 493.3359, mu: -0.0010, theta: -0.4902, sigma: 0.6394
Epoch 600, Loss: 471.5910, mu: -0.0010, theta: -0.5805, sigma: 0.5968
Epoch 700, Loss: 456.2417, mu: -0.0011, theta: -0.6599, sigma: 0.5624
Epoch 800, Loss: 447.1696, mu: -0.0011, theta: -0.7199, sigma: 0.5359
Epoch 900, Loss: 442.9311, mu: -0.0011, theta: -0.7544, sigma: 0.5167
Epoch 1000, Loss: 441.2652, mu: -0.0011, theta: -0.7682, sigma: 0.5038
Epoch 1100, Loss: 440.6577, mu: -0.0012, theta: -0.7719, sigma: 0.4956
Epoch 1200, Loss: 440.4542, mu: -0.0012, theta: -0.7727, sigma: 0.4907
Epoch 1300, Loss: 440.3933, mu: -0.0011, theta: -0.7728, sigma: 0.4880
Epoch 1400, Loss: 440.3770, mu: -0.0011, theta: -0.7728, sigma: 0.4865
Epoch 1500, Loss: 440.3732, mu: -0.0011, theta: -0.7728, sigma: 0.4858
Epoch 1600, Loss: 440.3724, mu: -0.0011, theta: -0.7728, sigma: 0.4854
Epoch 1700, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4853
Epoch 1800, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 1900, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2000, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2100, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2200, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2300, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2400, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2500, Loss: 440.3723, mu: -0.0012, theta: -0.7728, sigma: 0.4852
Epoch 2600, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2700, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2800, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 2900, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3000, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3100, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3200, Loss: 440.3722, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3300, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3400, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3500, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3600, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3700, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3800, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
Epoch 3900, Loss: 440.3723, mu: -0.0011, theta: -0.7728, sigma: 0.4852
```

The following code prints out the estimates given by this code, along with the estimates given by the ARIMA function.

```python
ma1_pars = np.array([mamod.mu.detach().numpy(), mamod.theta.detach().numpy(), np.exp(2*mamod.log_sigma.detach().numpy())]) #mu, theta and sigma^2
print(np.column_stack([mamod_ARIMA.params, ma1_pars]))
#the parameter estimates are quite close to each other
```

```
[[-0.00125667 -0.0011363 ]
 [-0.77099236 -0.77283096]
 [ 0.23528045  0.23539422]]
```

### AR(1) model fitting

Next let us fit the AR(1) model using PyTorch. Note that the full likelihood in the AR(1) model (stationary case) is given by (see Equation (7) in the notes for Lecture 17):
\begin{align*}
\frac{\sqrt{1 - \phi_1^2}}{\sqrt{2 \pi}
      \sigma} \exp \left(-\frac{1 - \phi_1^2}{2 \sigma^2} \left(y_1 -
        \frac{\phi_0}{1 - \phi_1} \right)^2 \right) \left(\frac{1}{\sqrt{2 \pi} \sigma}
    \right)^{n-1} \exp \left(-\frac{1}{2 \sigma^2} \sum_{t=2}^n (y_t -
    \phi_0 - \phi_1 y_{t-1})^2 \right).
\end{align*}
Below we first fit AR(1) using ARIMA, and then fit it by maximizing the log of the likelihood written above.

```python
armod_ARIMA = ARIMA(ylogdiff, order = (1, 0, 0)).fit()
print(armod_ARIMA.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(1, 0, 0)   Log Likelihood                -494.562
Date:                Tue, 25 Nov 2025   AIC                            995.124
Time:                        16:20:33   BIC                           1008.475
Sample:                             0   HQIC                          1000.309
                                - 633
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0010      0.015     -0.067      0.946      -0.031       0.029
ar.L1         -0.3970      0.036    -10.989      0.000      -0.468      -0.326
sigma2         0.2793      0.015     18.916      0.000       0.250       0.308
===================================================================================
Ljung-Box (L1) (Q):                   5.88   Jarque-Bera (JB):                 5.22
Prob(Q):                              0.02   Prob(JB):                         0.07
Heteroskedasticity (H):               0.77   Skew:                            -0.17
Prob(H) (two-sided):                  0.05   Kurtosis:                         3.29
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
class AR1Model(nn.Module):
    def __init__(self):
        super().__init__()
        # Learnable parameters: phi0 (intercept), phi1 (AR coefficient), log_sigma (for positivity)
        self.phi0 = nn.Parameter(torch.tensor(0.0))
        self.phi1 = nn.Parameter(torch.tensor(0.0))
        self.log_sigma = nn.Parameter(torch.tensor(0.0))  # log(sigma) to ensure sigma > 0

    def forward(self, y):
        n = len(y)
        sigma = torch.exp(self.log_sigma)
        phi0 = self.phi0
        phi1 = self.phi1
        #If the model is non-stationary, return infinite negative log-likelihood (and None for log-likelihood)
        if torch.abs(phi1) >= 1:
            return torch.tensor(float("inf")), None

        # Stationary mean of y_1
        y1_mean = phi0 / (1 - phi1)

        # Compute log-likelihood parts
        part1 = -0.5 * n * torch.log(torch.tensor(2 * torch.pi))
        part2 = -n * torch.log(sigma)
        part3 = 0.5 * torch.log(1 - phi1**2)
        part4 = - (1 - phi1**2) / (2 * sigma**2) * (y[0] - y1_mean)**2
        part5 = - (1 / (2 * sigma**2)) * torch.sum((y[1:] - phi0 - phi1 * y[:-1])**2)

        log_likelihood = part1 + part2 + part3 + part4 + part5
        negative_log_likelihood = -log_likelihood  # because we minimize

        return negative_log_likelihood, log_likelihood
```

```python

---

[Up: contents](index.md) · [Fit the model →](02-fit-the-model.md)
