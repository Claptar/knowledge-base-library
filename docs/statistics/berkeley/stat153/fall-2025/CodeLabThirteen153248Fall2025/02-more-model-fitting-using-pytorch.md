---
title: More Model Fitting using PyTorch
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# More Model Fitting using PyTorch

In Lecture 24, we showed how PyTorch can be used for parameter estimation in the following models:
1. $y_t = \beta_0 + \beta_1 x_t + \beta_2 (x_t - c_1)_+ + \dots + \beta_{k+1} (x_t - c_k)_+ + \epsilon_t$
2. $y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$ (with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$)
3. $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$ (with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$)

Today we shall discuss the variance model, and spectrum model (from Lectures 14-15) and use PyTorch to fit the parameters.

## Variance Model

The variance model is simply $y_t \overset{\text{ind}}{\sim} N(0, \tau_t^2)$. We have seen from Lecture 14 that the negative log-likelihood is:
\begin{align*}
   \sum_{t=1}^n \left(\log \tau_t + \frac{y_t^2}{2 \tau^2_t} \right).
\end{align*}
We reparametrize and write the objective function in terms of $\alpha_t = \log \tau_t$ to get:
\begin{align*}
  \sum_{t=1}^n \left(\alpha_t + \frac{y_t^2}{2} e^{-2 \alpha_t} \right).
\end{align*}
We also saw in Lecture 14 that unconstrained minimization of this negative log-likelihood with respect to $\alpha_t$ gives $\alpha_t = \log |y_t|$, which is complete overfitting in this model.  To prevent overfitting, we can consider the following model for $\alpha_t$:
\begin{align*}
   \alpha_t = \beta_0 + \beta_1 t + \beta_2 (t - c_1)_+ + \dots + \beta_{k+1} (t - c_k)_+.
\end{align*}
If $k$ is small, then overfitting is prevented, and we would get useful estimates. The optimization problem now is to minimize the above negative log-likelihood when $\alpha_t$ is of the above form. When $k$ is small, we will not change the objective function by including a regularization penalty.

First let us create a simulation setting for fitting this model. We shall use one of the simulation settings from Lecture 14.

```python
# the following is the true alpha_t function:
def smoothfun(x):
    ans = np.sin(15 * x) + np.exp(-(x ** 2)/2) + 0.5 * ((x - 0.5) ** 2) + 2 * np.log(x + 0.1)
    return ans

n = 2000
xx = np.linspace(0, 1, n)
alpha_true = np.array([smoothfun(x) for x in xx])

plt.figure(figsize = (12, 6))
plt.plot(alpha_true)
plt.title('True Smooth Function (alpha)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We generate data from the above true function using the model: $y_t \overset{\text{ind}}{\sim} N(0, \tau_t^2)$ where $\tau_t = \exp(\alpha_t)$.

```python
# Generating Data using the above smooth function:
tau_t = np.exp(alpha_true)
rng = np.random.default_rng(seed = 42)
y = rng.normal(loc = 0, scale = tau_t)

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The goal is to get back the estimates of $\alpha_t$ from the above data.

We rescale $x$ below (but not $y$). Note that this model is not invariant to rescaling both $y$ and $x$.

```python
# we rescale x but not y
x_raw = np.arange(1, n+1)
x_scaled = (x_raw - np.mean(x_raw))/(np.std(x_raw))
y_torch = torch.tensor(y, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)
```

We now select the initial values. We take $c_1, \dots, c_k$ to be quantiles of $x_t$ at $1/(k+1), \dots, k/(k+1)$. For $\beta_0, \dots, \beta_{k+2}$, we run a linear regression of $\log y_t$ on $1, x_t, (x_t - c_1)_+, \dots, (x_t - c_k)_+$ with these initial $c_1, \dots, c_k$ and then take the corresponding coefficients.

```python
k = 8 # this is the number of knots
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_scaled, quantile_levels)

n = len(y)
X = np.column_stack([np.ones(n), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float)) * (x_scaled - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(np.log(np.abs(y)), X).fit()

#print(md_init.summary())
#print(md_init.params)
beta_init = md_init.params
print(knots_init)
print(beta_init)
```

```
[-1.34647722 -0.96176944 -0.57706167 -0.19235389  0.19235389  0.57706167
  0.96176944  1.34647722]
[ 7.44006624  6.59898963 -8.17888252  0.61656712  5.50695701 -1.94742617
 -5.67882692  2.43967538  5.87140635 -4.41572431]
```

We now use PyTorch to estimate $\alpha_t$. The first step is to create the model. We use the same piecewise linear model that we used in Lecture 24.

```python
class PiecewiseLinearModel(nn.Module):
    def __init__(self, knots_init, beta_init):
        super().__init__()
        self.num_knots = len(knots_init)
        self.beta = nn.Parameter(torch.tensor(beta_init, dtype = torch.float32))
        self.knots = nn.Parameter(torch.tensor(knots_init, dtype = torch.float32))

    def forward(self, x):
        knots_sorted, _ = torch.sort(self.knots)
        out = self.beta[0] + self.beta[1] * x
        for j in range(self.num_knots):
            out += self.beta[j + 2] * torch.relu(x - knots_sorted[j])
        return out
```

The following code creates this model.

```python
md_PiecewiseLinear = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
# This code creates an instance of our custom neural network class
# It also initializes the knots at knots_init
```

The following code runs the optimizer. The only thing that is different from the piecewise linear regression model is the loss function.

```python
optimizer = optim.Adam(md_PiecewiseLinear.parameters(), lr = 0.01)
# the above line tells Python to create an Adam optimizer that will update all parameters
# of md_PiecewiseLinear during training, using a learning rate of 0.01.

for epoch in range(20000):
    optimizer.zero_grad()

    y_pred = md_PiecewiseLinear(x_torch)
    #loss = loss_fn(y_pred, y_torch)
    loss = torch.sum( y_pred + (y_torch**2) / 2 * torch.exp(-2 * y_pred) )

    loss.backward() # calulates gradients

    optimizer.step() # updates parameters using gradients

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
# Run this code a few times to be sure of convergence.
```

```
Epoch 0, Loss: 1876.1447
Epoch 1000, Loss: 384.1796
Epoch 2000, Loss: 382.5848
Epoch 3000, Loss: 380.2390
Epoch 4000, Loss: 378.5027
Epoch 5000, Loss: 376.6567
Epoch 6000, Loss: 374.1023
Epoch 7000, Loss: 373.7757
Epoch 8000, Loss: 373.1777
Epoch 9000, Loss: 372.4913
Epoch 10000, Loss: 372.2776
Epoch 11000, Loss: 372.0750
Epoch 12000, Loss: 372.0114
Epoch 13000, Loss: 372.4420
Epoch 14000, Loss: 371.9330
Epoch 15000, Loss: 371.8340
Epoch 16000, Loss: 371.8694
Epoch 17000, Loss: 371.8499
Epoch 18000, Loss: 372.0723
Epoch 19000, Loss: 371.8283
```

The estimate of $\alpha_t$ is obtained as follows.

```python
alpha_est = md_PiecewiseLinear(x_torch).detach().numpy()
```

```python
plt.figure(figsize = (12, 6))
plt.plot(alpha_est, label = 'PyTorch Estimate')
plt.plot(alpha_true, color = 'red', label = 'true')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The estimate is pretty good.

## Spectrum Model

We have a time series $y_t$ with periodogram $I(j/n)$. The spectrum model is given by:
\begin{equation*}
   I(j/n) \overset{\text{ind}}{\sim} f(j/n) \eta_j
\end{equation*}
for $j = 1, \dots, m$ where $m$ is the largest integer strictly smaller than $n/2$. Here $\eta_j \overset{\text{i.i.d}}{\sim} Exp(1)$. The parameters in this model are $f(j/n), j = 1, \dots, m$ (it is called the power of frequency $j/n$).

The likelihood is given by:
\begin{align*}
   \prod_{j=1}^m \frac{1}{f(j/n)} \exp \left(-\frac{I(j/n)}{f(j/n)} \right).
\end{align*}
So the negative log-likelihood is:
\begin{align*}
   \sum_{j = 1}^{m} \left(\frac{I(j/n)}{f(j/n)} + \log f(j/n)\right).
\end{align*}
We reparametrize this by $\log f(j/n) = \alpha_j$ so the minimization problem becomes:
\begin{align*}
   \sum_{j = 1}^{m} \left(I(j/n) \exp(-\alpha_j) + \alpha_j\right).
\end{align*}
Unconstrained minimization is easily seen to lead to $\alpha_j = \log I(j/n)$, so it makes sense to make further constraining assumptions on $\alpha_j$. We use the assumption:
\begin{align*}
   \alpha_j = \beta_0 + \beta_1 j + \beta_2 (j - c_1)_+ + \dots + \beta_{k+1} (j - c_k)_+.
\end{align*}

## Example One: Sunspots Data

Let us apply the method to the sunspots dataset.

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we compute the periodogram of the data.

```python
def periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, 1/2, 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2)/n
    return fourier_freqs, pgram_y
```

```python
n = len(y)
freqs, pgram = periodogram(y)
m = len(pgram)
```

Below we plot the periodogram and its logarithm.

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, pgram, label = 'Periodogram')
plt.title('Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram), label = 'Log Periodogram')
plt.title('Logarithm of Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Our first step is to get preliminary estimates of $c_1, \dots, c_k$ and $\beta_0, \dots, \beta_{k+1}$. We rescale $j = 1, \dots, n$ to $x_1, \dots, x_m$. Then we take $c_1, \dots, c_k$ to be the quantiles of $x_j$ at $1/(k+1), \dots, k/(k+1)$. For $\beta_0, \dots, \beta_{k+2}$, we run a linear regression of $\log I(j/n)$ on $1, x_j, (x_j - c_1)_+, \dots, (x_j - c_k)_+$ with these initial $c_1, \dots, c_k$ and then take the corresponding coefficients.

```python
k = 10 # this is the number of knots
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
x = np.arange(1, m+1)
x_scaled = (x - np.mean(x))/(np.std(x))
knots_init = np.quantile(x_scaled, quantile_levels)

X = np.column_stack([np.ones(m), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float)) * (x_scaled - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(np.log(pgram), X).fit()

#print(md_init.summary())
#print(md_init.params)
beta_init = md_init.params
print(knots_init)
print(beta_init)
```

```
[-1.40841158 -1.09543123 -0.78245088 -0.46947053 -0.15649018  0.15649018
  0.46947053  0.78245088  1.09543123  1.40841158]
[ -9.0879961  -10.99249551  23.75611862 -26.47556894  16.98756723
  -9.10663734   3.89842712   2.67957451  -3.61744261   3.02132995
   0.94878987  -1.06944189]
```

Below we create the torch objects for use in the PyTorch code.

```python
#y_torch = torch.tensor(pgram/np.std(pgram), dtype = torch.float32).unsqueeze(1)
y_torch = torch.tensor(pgram, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)
```

```python
md_PiecewiseLinear = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
optimizer = optim.Adam(md_PiecewiseLinear.parameters(), lr = 0.01)

for epoch in range(20000):
    optimizer.zero_grad()

    y_pred = md_PiecewiseLinear(x_torch)
    #loss = loss_fn(y_pred, y_torch)
    loss = torch.sum( y_pred + y_torch * torch.exp(- y_pred) )

    loss.backward() # calulates gradients

    optimizer.step() # updates parameters using gradients

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# Run this code a few times to be sure of convergence.
```

```
Epoch 0, Loss: 1230.7987
Epoch 1000, Loss: 1200.7444
Epoch 2000, Loss: 1199.7701
Epoch 3000, Loss: 1199.2241
Epoch 4000, Loss: 1198.9481
Epoch 5000, Loss: 1198.8514
Epoch 6000, Loss: 1198.7220
Epoch 7000, Loss: 1198.5948
Epoch 8000, Loss: 1198.5424
Epoch 9000, Loss: 1198.5123
Epoch 10000, Loss: 1198.4650
Epoch 11000, Loss: 1198.2202
Epoch 12000, Loss: 1198.0922
Epoch 13000, Loss: 1198.0574
Epoch 14000, Loss: 1197.9463
Epoch 15000, Loss: 1197.9348
Epoch 16000, Loss: 1197.8220
Epoch 17000, Loss: 1197.7927
Epoch 18000, Loss: 1197.7850
Epoch 19000, Loss: 1197.7164
```

```python
#alpha_est = md_PiecewiseLinear(x_torch).detach().numpy() + np.log(np.std(pgram))
alpha_est = md_PiecewiseLinear(x_torch).detach().numpy()
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram), label = 'Log Periodogram', color = 'lightblue')
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.title('Logarithm of Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us compare this estimate with our previous method (from Lectures 14-15).

```python
import cvxpy as cp
#import mosek

def spectrum_estimator_lasso(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y)
    alpha = cp.Variable(m)

    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.abs(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)

    problem = cp.Problem(objective)
    problem.solve()
    #problem.solve(solver = cp.MOSEK)
    return alpha.value, freq
```

```python
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 10)
power_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

plt.figure(figsize = (12, 6))
plt.plot(freq, np.log(pgram))
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, np.log(power_lasso), color = 'black', label = "CVXPy LASSO Estimate")
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The estimates are clearly reasonably close to each other.

## Example 2: Earthquake Data

Below is an example where this PyTorch method does not quite seem to work. This is for the earthquake dataset that we previously used in Lecture 15.
This dataset is from the Mathworks (MATLAB) tutorial "Practical Introduction to Frequency-Domain Analysis" (see [this link](https://www.mathworks.com/help/signal/ug/practical-introduction-to-frequency-domain-analysis.html)). From this matlab tutorial: *Active Mass Driver (AMD) control systems are used to reduce vibration in a building under an earthquake. An active mass driver is placed on the top floor of the building and, based on displacement and acceleration measurements of the building floors, a control system sends signals to the driver so that the mass moves to attenuate ground disturbances. Acceleration measurements were recorded on the first floor of a three story test structure under earthquake conditions. Measurements were taken without the active mass driver control system (open loop condition), and with the active control system (closed loop condition).*

We will use the data on the open loop condition.

```python
from scipy.io import loadmat
mat_dict = loadmat('quakevibration.mat')
print(mat_dict.keys())

gfloor1OL_array = mat_dict['gfloor1OL']
print(gfloor1OL_array.shape)

y = gfloor1OL_array.ravel()

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.title('Ground Floor Acceleration Measurements (Open Loop)')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Acceleration (in/s^2)')
plt.show()
```

```
dict_keys(['__header__', '__version__', '__globals__', 'gfloor1OL', 'gfloor1CL'])
(10000, 1)
```

*(1 figure omitted — see the original notebook.)*

The periodogram is given by:

```python
n = len(y)
freqs, pgram = periodogram(y)
m = len(pgram)
```

The initial values of the parameters are obtained below.

```python
k = 10 # this is the number of knots
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
x = np.arange(1, m+1)
x_scaled = (x - np.mean(x))/(np.std(x))
knots_init = np.quantile(x_scaled, quantile_levels)

X = np.column_stack([np.ones(m), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float)) * (x_scaled - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(np.log(pgram), X).fit()

#print(md_init.summary())
#print(md_init.params)
beta_init = md_init.params
print(knots_init)
print(beta_init)
```

```
[-1.41684902 -1.10199369 -0.78713835 -0.47228301 -0.15742767  0.15742767
  0.47228301  0.78713835  1.10199369  1.41684902]
[-40.11567801 -22.89394746  20.3600293   -0.40359563   1.59487819
  -0.05497328   0.36121425   0.53068634  -0.05943841   0.45359363
  -0.23388732   0.40076595]
```

Here is the PyTorch code.

```python
#y_torch = torch.tensor(pgram/np.std(pgram), dtype = torch.float32).unsqueeze(1)
y_torch = torch.tensor(pgram, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)
```

```python
md_PiecewiseLinear = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
optimizer = optim.Adam(md_PiecewiseLinear.parameters(), lr = 0.01)

for epoch in range(20000):
    optimizer.zero_grad()

    y_pred = md_PiecewiseLinear(x_torch)
    #loss = loss_fn(y_pred, y_torch)
    loss = torch.sum( y_pred + y_torch * torch.exp(- y_pred) )

    loss.backward() # calulates gradients

    optimizer.step() # updates parameters using gradients

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
# Run this code a few times to be sure of convergence.
```

```
Epoch 0, Loss: -35967.2383
Epoch 1000, Loss: -41305.5781
Epoch 2000, Loss: -41314.9375
Epoch 3000, Loss: -41330.3047
Epoch 4000, Loss: -41352.2773
Epoch 5000, Loss: -41381.5039
Epoch 6000, Loss: -41415.5938
Epoch 7000, Loss: -41448.9766
Epoch 8000, Loss: -41475.8164
Epoch 9000, Loss: -41494.0078
Epoch 10000, Loss: -41500.9023
Epoch 11000, Loss: -41510.1602
Epoch 12000, Loss: -41519.8242
Epoch 13000, Loss: -41525.5430
Epoch 14000, Loss: -41531.9727
Epoch 15000, Loss: -41537.0273
Epoch 16000, Loss: -41540.6719
Epoch 17000, Loss: -41543.7500
Epoch 18000, Loss: -41545.9062
Epoch 19000, Loss: -41547.5859
```

```python
#alpha_est = md_PiecewiseLinear(x_torch).detach().numpy() + np.log(np.std(pgram))
alpha_est = md_PiecewiseLinear(x_torch).detach().numpy()
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram), label = 'Log Periodogram', color = 'lightblue')
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.title('Logarithm of Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
import cvxpy as cp
import mosek

def spectrum_estimator_lasso(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y)
    alpha = cp.Variable(m)
    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.abs(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    #problem.solve()
    problem.solve(solver = cp.MOSEK)
    return alpha.value, freq
```

```python
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 1000)
power_lasso = (2/n) * (np.exp(2 * alpha_opt_lasso))

plt.figure(figsize = (12, 6))
plt.plot(freq, np.log(pgram), color = 'lightblue')
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, np.log(power_lasso), color = 'black', label = "CVXPy LASSO Estimate")
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The PyTorch is not able to figure out the three main peaks in the log power spectrum. This is probably because of the poor quality of the initialization. Note that the main peaks are all near the initial frequencies so that is where the knots need to be. If we find the peaks and troughs from our spectrum estimate from Lecture 15, and then initialize the PyTorch algorithm using knots near the peaks-troughs, then it will work better.

```python
from scipy.signal import find_peaks
# Find peaks
peaks, _ = find_peaks(np.log(power_lasso))
#find troughs
troughs, _ = find_peaks(-np.log(power_lasso))
print(peaks)
print(troughs)
```

```
[ 55 176 284]
[118 229]
```

```python
k = 8 # this is the number of knots
#quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
x = np.arange(1, m+1)
x_scaled = (x - np.mean(x))/(np.std(x))
#knots_init = np.quantile(x_scaled, quantile_levels)

knots_init = (np.array([50, 120, 175, 230, 285, 340, 400, 500]) - np.mean(x))/(np.std(x))
# these knots are chosen to be roughly near the peaks and troughs

X = np.column_stack([np.ones(m), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float))*(x_scaled-knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(np.log(pgram), X).fit()

#print(md_init.summary())
#print(md_init.params)
beta_init = md_init.params
print(knots_init)
print(beta_init)
```

```
[-1.69774938 -1.64924225 -1.61112951 -1.57301677 -1.53490403 -1.49679129
 -1.45521375 -1.38591786]
[ 207.99767796  121.68086542 -237.90477858  200.25534348 -231.28621121
  208.44914151 -136.58094635   94.09095751  -50.99202009   31.30034846]
```

```python
#y_torch = torch.tensor(pgram/np.std(pgram), dtype = torch.float32).unsqueeze(1)
y_torch = torch.tensor(pgram, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)

md_PiecewiseLinear = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
optimizer = optim.Adam(md_PiecewiseLinear.parameters(), lr = 0.001)

for epoch in range(20000):
    optimizer.zero_grad()

    y_pred = md_PiecewiseLinear(x_torch)
    #loss = loss_fn(y_pred, y_torch)
    loss = torch.sum( y_pred + y_torch * torch.exp(- y_pred) )

    loss.backward() # calulates gradients

    optimizer.step() # updates parameters using gradients

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
# Run this code a few times to be sure of convergence.
```

```
Epoch 0, Loss: -41205.1836
Epoch 1000, Loss: -41896.0898
Epoch 2000, Loss: -41904.6094
Epoch 3000, Loss: -41907.7344
Epoch 4000, Loss: -41907.7227
Epoch 5000, Loss: -41908.2969
Epoch 6000, Loss: -41906.9531
Epoch 7000, Loss: -41904.2344
Epoch 8000, Loss: -41908.1953
Epoch 9000, Loss: -41908.4688
Epoch 10000, Loss: -41907.9727
Epoch 11000, Loss: -41908.5391
Epoch 12000, Loss: -41908.3516
Epoch 13000, Loss: -41897.2539
Epoch 14000, Loss: -41908.6953
Epoch 15000, Loss: -41908.5977
Epoch 16000, Loss: -41908.5781
Epoch 17000, Loss: -41908.1875
Epoch 18000, Loss: -41907.3008
Epoch 19000, Loss: -41906.0352
```

```python
#alpha_est = md_PiecewiseLinear(x_torch).detach().numpy() + np.log(np.std(pgram))
alpha_est = md_PiecewiseLinear(x_torch).detach().numpy()

plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram), label = 'Log Periodogram', color = 'lightblue')
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.title('Logarithm of Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 1000)
power_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

plt.figure(figsize = (12, 6))
plt.plot(freq, np.log(pgram), color = 'lightblue')
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, np.log(power_lasso), color = 'black', label = "CVXPy LASSO Estimate")
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now the two estimates are much closer to each other. This shows how tricky some optimization functions are. They depend sensitively on the initialization. Our estimate from Lectures 14-15 were based on convex optimization problems however which are more stable.

---

[← Piecewise Linear Model via Pytorch: importance of scaling](01-piecewise-linear-model-via-pytorch-importance-of-scaling.md) · [Up: contents](index.md)
