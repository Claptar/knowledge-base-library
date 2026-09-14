---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentySix153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwentySix153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: LSTM (and RNN, GRU) fitting
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
```

## The LSTM Unit

Before fitting LSTM models, let us first see how the basic LSTM unit in PyTorch (nn.LSTM) works (see \url{https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html} for details). The LSTM unit can be seen as a black box which (for a fixed $p$ and $k$) holds weight matrices $W_{ii}, W_{hi}, W_{if}, W_{hf}, W_{ig}, W_{hg}, W_{io}, W_{ho}$ and bias vectors $b_{ii}, b_{hi}, b_{if} b_{hf}, b_{ig}, b_{hg}, b_{io}, b_{ho}$. In order to create the LSTM unit, we only need to specify $p$ (this is the dimension of $x_t$ and will be referred to as the input size) and $k$ (this is the dimension of $h_t$ and will be referred to as the hidden size).

```python
lstm_net = nn.LSTM(input_size = 1, hidden_size = 5, batch_first = True)
```

The above code line will create a LSTM unit and will randomly initialize all its parameters $W_{ii}, W_{hi}, W_{if}, W_{hf}, W_{ig}, W_{hg}, W_{io}, W_{ho}$ and $b_{ii}, b_{hi}, b_{if} b_{hf}, b_{ig}, b_{hg}, b_{io}, b_{ho}$. Given a sequence $x_1, \dots, x_T$ for some $T$ (here each $x_t$ needs to be of dimension input_size), the LSTM unit will then use the formulas to compute $(c_1, h_1), \dots, (c_T, h_T)$. It will output $h_1, \dots, h_T$ as well as $(h_T, c_T)$.

If we create two sets of input sequences $x_1, \dots, x_T$ and $\tilde{x}_1, \dots, \tilde{x}_T$, then the LSTM unit will use its formulae to output $h_1, \dots, h_T$ (as well as $(h_T, c_T)$) corresponding to $x_1, \dots, x_T$, as well as $\tilde{h}_1, \dots, \tilde{h}_T$, as well as $(\tilde{h}_T, \tilde{c}_T)$ corresponding to $\tilde{x}_1, \dots, \tilde{x}_T$. In general, if we send in $B$ input sequences (i.e., $B$ batches of input sequences), each sequence having length $T$ (and each $x$ in each sequence has dimension input_size), the output of the LSTM will correspond to $B$ sequences of length $T$ (each element of the sequence has dimension equal to hidden_size). The inputs and outputs can therefore both be treated as tensors. The 'batch_first = True' in the specification of lstm_net above indicates that the input tensor should have shape (B, T, input_size) and the output tensor will have shape (B, T, hidden_size). We will only use $B = 1$.

```python
#Let us create an input tensor for lstm_net:
input = torch.randn(1, 10, 1)
#this input has one batch, which is a sequence x_1, \dots, x_10 of length 10. Each x_t is a scalar (input_size = 1).
print(input)

output, (hn, cn) = lstm_net(input)

#output will have shape (1, 10, 5). It is a simply the sequence h_1, \dots, h_10 where each h_t is of dimension hidden_size = 5.
print(output.shape)

print(hn.shape) #h_n is simply the hidden vector h_t corresponding to the last time (here t = 10). You can check that hn is identical to the last element of the output

print(cn.shape) #c_n is the cell state corresponding to the last output

print(output[:, 9, :])
print(hn)
#check that hn and output[:, 9, :] are identical
```

```
tensor([[[-0.6010],
         [ 0.5618],
         [-1.5536],
         [-0.8574],
         [ 0.0943],
         [ 0.6305],
         [ 0.8702],
         [ 0.6343],
         [-0.4735],
         [ 1.1954]]])
torch.Size([1, 10, 5])
torch.Size([1, 1, 5])
torch.Size([1, 1, 5])
tensor([[ 0.0266, -0.0024, -0.1292,  0.0224,  0.0120]],
       grad_fn=<SliceBackward0>)
tensor([[[ 0.0266, -0.0024, -0.1292,  0.0224,  0.0120]]],
       grad_fn=<StackBackward0>)
```

The weight matrices $W_{ii}, W_{if}, W_{ig}, W_{io}$ as well as $W_{hi}, W_{hf}, W_{hg}, W_{ho}$, and the biases $b_{ii}, b_{if}, b_{ig}, b_{io}$ as well as $b_{hi}, b_{hf}, b_{hg}, b_{ho}$ can be accessed as follows.

```python
print(lstm_net.weight_ih_l0.shape)
print(lstm_net.weight_ih_l0) #this contains the four weight matrices W_{ii}, W_{if}, W_{ig}, W_{io}

print(lstm_net.weight_hh_l0.shape)
print(lstm_net.weight_hh_l0) #this contains the four weight matrices W_{hi}, W_{hf}, W_{hg}, W_{ho}

print(lstm_net.bias_ih_l0.shape)
print(lstm_net.bias_ih_l0)  #this contains  the four biases b_{ii}, b_{if}, b_{ig}, b_{io}

print(lstm_net.bias_hh_l0.shape)
print(lstm_net.bias_hh_l0)  #this contains  the four biases b_{hi}, b_{hf}, b_{hg}, b_{ho}

#l0 here refers to the fact that there is a single LSTM layer. Sometimes, it is common to stack multiple LSTM units, in which case there will be weights and biases for each LSTM. We will only deal with a single LSTM layer
```

```
torch.Size([20, 1])
Parameter containing:
tensor([[ 0.2603],
        [-0.2236],
        [ 0.2664],
        [ 0.1512],
        [-0.2186],
        [-0.1205],
        [-0.1810],
        [ 0.1973],
        [-0.1793],
        [ 0.1518],
        [ 0.0319],
        [-0.3571],
        [-0.2811],
        [-0.3101],
        [ 0.2343],
        [ 0.0969],
        [-0.0112],
        [-0.2663],
        [-0.4431],
        [-0.1583]], requires_grad=True)
torch.Size([20, 5])
Parameter containing:
tensor([[-0.3423, -0.4448, -0.4265, -0.2921, -0.4348],
        [ 0.1394,  0.1673,  0.1803, -0.4452,  0.2765],
        [ 0.0872,  0.2287, -0.1099,  0.2148, -0.4241],
        [ 0.1523,  0.3546,  0.1880, -0.4215, -0.1255],
        [-0.0555,  0.2343, -0.1692,  0.0643, -0.1570],
        [-0.0710, -0.0089, -0.2568, -0.3104,  0.3692],
        [ 0.3757, -0.0135,  0.3871,  0.3446, -0.2817],
        [-0.1777, -0.3072,  0.1446,  0.0113, -0.0613],
        [ 0.3320, -0.1748, -0.2448, -0.3179, -0.2275],
        [ 0.4310, -0.2174, -0.1231,  0.2016, -0.3435],
        [-0.2714,  0.3292, -0.1715, -0.2321, -0.0579],
        [-0.0637,  0.0817,  0.1640, -0.3448,  0.4064],
        [-0.4252,  0.1515, -0.1262, -0.1889,  0.4183],
        [-0.4310,  0.0305,  0.2866,  0.3998, -0.3781],
        [ 0.0539,  0.4425, -0.4381,  0.1092, -0.2802],
        [ 0.0726, -0.4045,  0.2200, -0.0992,  0.2673],
        [-0.0067, -0.0637, -0.1086, -0.4095, -0.1900],
        [ 0.0149, -0.3460,  0.3925, -0.2909, -0.1742],
        [-0.0598, -0.3623, -0.0035, -0.2154, -0.3743],
        [ 0.0110,  0.3959,  0.1101,  0.3689, -0.0044]], requires_grad=True)
torch.Size([20])
Parameter containing:
tensor([-0.1561,  0.3604, -0.2381, -0.4137,  0.0979,  0.2229, -0.2673,  0.1574,
        -0.1587, -0.0543, -0.0990, -0.0957, -0.3639,  0.1096, -0.1176,  0.3420,
         0.0746, -0.3657, -0.3402, -0.2331], requires_grad=True)
torch.Size([20])
Parameter containing:
tensor([ 0.2142, -0.2887, -0.2046,  0.0812, -0.3101, -0.2202,  0.4055, -0.2364,
        -0.1490,  0.3198,  0.1002,  0.3510, -0.3940,  0.2235, -0.0684, -0.2865,
        -0.1915, -0.4326,  0.3094, -0.0858], requires_grad=True)
```

The values that we see above for the weights and biases are randomly chosen initial values. Given some data, they will be trained so as to minimize some loss function.

## Simulated Dataset One

Consider the following simple dataset.

```python
n = 1500
truelag = 85
rng = np.random.default_rng(seed = 0)
sig_noise = 0.2
eps = rng.normal(loc = 0, scale = sig_noise, size = n)
y_sim = np.full(shape = n, fill_value = -999.0)
y_sim[0:truelag] = np.linspace(-1, 1, truelag)
for i in range(truelag, n):
    y_sim[i] = y_sim[i - truelag]
y_sim = y_sim + eps
plt.figure(figsize = (12, 6))
plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We first fit the AR($p$) model. If $p$ is taken to be smaller than the true lag which generated the data, the predictions will be quite poor. But the predictions are quite good when $p$ is exactly equal to the true lag.

```python
#Let us fit AR(p) with the truelag
#p = 60
p = truelag
ar = AutoReg(y_sim, lags = p).fit()

n = len(y_sim)
tme = range(1, n+1)
n_future = 1000
tme_future = range(n+1, n+n_future+1)
fcast = ar.get_prediction(start = n, end = n+n_future-1).predicted_mean
plt.figure(figsize = (12, 7))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, fcast, label = 'Forecast (AR(p))', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we apply LSTM (and RNN). The first step is to create the input and output tensors. We scale the data before fitting models.

```python
mu, sig = y_sim.mean(), y_sim.std()
y_std = (y_sim - mu) / sig

X = torch.tensor(y_std[:-1], dtype=torch.float32)
Y = torch.tensor(y_std[1: ], dtype=torch.float32)

X = X.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)
Y = Y.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)

#unsqueeze(0) adds a dimension at the front (the batch dimension)
#unsqueeze(-1) adds a dimension at the end (the input dimension of x_t)

seq_len = X.size(1)
print(seq_len)
```

```
1499
```

We create the LSTM model class below. It consists of the LSTM unit which outputs $h_t$ (or $r_t$ in our notation) followed by a fully connected layer which outputs $\mu_t = \beta_0 + \beta^T h_t$. We take $k$ (below nh) to be 32. Increasing $k$ will make the parameter estimation process slower.

```python
class lstm_net(nn.Module):
    def __init__(self, nh):
        super().__init__()
        self.rnn = nn.LSTM(input_size=1, hidden_size=nh,
                           batch_first=True)
        self.fc  = nn.Linear(nh, 1)
    def forward(self, x, hc=None):
        out, hc = self.rnn(x, hc)
        out     = self.fc(out)
        return out, hc

#lstm_net defined above has an LSTM unit followed by a linear unit ('fc' stands for fully-connected) which converts the output of the LSTM to a scalar (this scalar is mu_t in our notation)

torch.manual_seed(0)
np.random.seed(0)

nh = 32
model = lstm_net(nh)
criterion = nn.MSELoss()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
```

Training is done as follows.

```python
n_epochs = 1000
for epoch in range(1, n_epochs + 1):
    model.train()
    opt.zero_grad()
    pred, _ = model(X)
    loss = criterion(pred, Y)
    loss.backward()
    opt.step()

    if epoch % 100 == 0:
        print(f"epoch {epoch:4d}/{n_epochs}  |  loss = {loss.item():.6f}")
```

```
epoch  100/1000  |  loss = 0.291070
epoch  200/1000  |  loss = 0.196253
epoch  300/1000  |  loss = 0.177559
epoch  400/1000  |  loss = 0.173790
epoch  500/1000  |  loss = 0.169772
epoch  600/1000  |  loss = 0.165050
epoch  700/1000  |  loss = 0.163995
epoch  800/1000  |  loss = 0.158396
epoch  900/1000  |  loss = 0.156533
epoch 1000/1000  |  loss = 0.165788
```

Predictions are obtained as follows.

```python
model.eval()
with torch.no_grad():
    _, hc = model(X)
    preds = np.zeros(n_future, dtype=np.float32)
    last_in = torch.tensor([[y_std[-1]]], dtype=torch.float32)
    for t in range(n_future):
        out, hc = model(last_in.view(1, 1, 1), hc)              # reuse hidden state
        next_val = out.squeeze().item()
        preds[t] = next_val
        last_in = torch.tensor([[next_val]], dtype=torch.float32)
```

Predictions are plotted below.

```python
lstm_preds_orig = preds * sig + mu
tme_pred_axis = np.arange(n, n + n_future)

plt.figure(figsize=(12,6))
plt.plot(np.arange(n), y_sim, lw=2, label="Data")
plt.plot(tme_pred_axis, lstm_preds_orig, lw=2, color="r", label="forecast (LSTM)")
plt.xlabel("Time"); plt.ylabel("Data")
for t in range(0, n + n_future, truelag):
    plt.axvline(x=t, linestyle='--', color='gray', linewidth=1)
plt.axhline(y=1, linestyle='--', color='gray', linewidth=1)
plt.axhline(y=-1, linestyle='--', color='gray', linewidth=1)
plt.title("Data and Forecast")
plt.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us now fit the RNN.

```python
class RNNReg(nn.Module):
    def __init__(self, nh):
        super().__init__()
        self.rnn = nn.RNN(1, nh, nonlinearity="tanh", batch_first=True)
        self.fc  = nn.Linear(nh, 1)
    def forward(self, x, h=None):
        out, h = self.rnn(x, h)
        return self.fc(out), h

nh = 32
model = RNNReg(nh)
criterion = nn.MSELoss()
opt = torch.optim.Adam(model.parameters(),lr = 1e-3)
```

```python
n_epochs = 900
for epoch in range(1, n_epochs + 1):
    model.train()
    opt.zero_grad()
    pred, _ = model(X)
    loss = criterion(pred, Y)
    loss.backward()
    opt.step()

    if epoch % 100 == 0:
        print(f"epoch {epoch:4d}/{n_epochs}  |  loss = {loss.item():.6f}")
```

```
epoch  100/900  |  loss = 0.293481
epoch  200/900  |  loss = 0.271486
epoch  300/900  |  loss = 0.263299
epoch  400/900  |  loss = 0.222172
epoch  500/900  |  loss = 0.199036
epoch  600/900  |  loss = 0.189352
epoch  700/900  |  loss = 0.188009
epoch  800/900  |  loss = 0.179842
epoch  900/900  |  loss = 0.176493
```

Below we obtain predictions for the RNN model.

```python
model.eval()
with torch.no_grad():
    _, h = model(X)
    preds = np.zeros(n_future, np.float32)
    last  = torch.tensor([[y_std[-1]]], dtype=torch.float32)
    for t in range(n_future):
        out, h = model(last.view(1,1,1), h)
        preds[t] = out.item()
        last = torch.tensor([[preds[t]]], dtype=torch.float32)
```

```python
rnn_preds_orig = preds * sig + mu
tme_pred_axis = np.arange(n, n + n_future)

plt.figure(figsize=(12,6))
plt.plot(np.arange(n), y_sim, lw=2, label="Data")
plt.plot(tme_pred_axis, lstm_preds_orig, lw=2, color="red", label="forecast (LSTM)")
plt.plot(tme_pred_axis, rnn_preds_orig, lw=2, color="black", label="forecast (RNN)")
#plt.plot(tme_pred_axis, fcast, lw=2, color="green", label="forecast (AR)")

for t in range(0, n + n_future, truelag):
    plt.axvline(x=t, linestyle='--', color='gray', linewidth=1)

plt.axhline(y=1, linestyle='--', color='gray', linewidth=1)
plt.axhline(y=-1, linestyle='--', color='gray', linewidth=1)

plt.xlabel("Time"); plt.ylabel("Data")
plt.title("Data and Forecast")
plt.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

RNN gives predictions that are similar to the LSTM predictions.

---

[Up: contents](index.md) · [Simulated Dataset Two →](02-simulated-dataset-two.md)
