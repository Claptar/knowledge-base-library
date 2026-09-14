---
title: Simulated Dataset Two
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentySix153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Simulated Dataset Two

**Source:** [`CodeLectureTwentySix153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We now make two changes to the first simulation above. We increase the true lag. We also add noise slightly differently (noise is now added to the equation $y_t = y_{t-\text{truelag}} + \epsilon_t$).

```python
n = 1500
truelag = 344
rng = np.random.default_rng(seed = 0)
sig_noise = 0.2
eps = rng.normal(loc = 0, scale = sig_noise, size = n)
y_sim = np.full(shape = n, fill_value = -999.0)
y_sim[0:truelag] = np.linspace(-1, 1, truelag)
for i in range(truelag, n):
    y_sim[i] = y_sim[i - truelag] + eps[i]
#y_sim = y_sim + eps
plt.figure(figsize = (12, 6))
plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This is a long range prediction problem. In this example, AR($p$) with $p$ taken to be the true lag gives very noisy predictions (as shown below)

```python
#Let us fit AR(p)
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

Let us see how the LSTM and RNN do.

```python
mu, sig = y_sim.mean(), y_sim.std()
y_std = (y_sim - mu) / sig

X = torch.tensor(y_std[:-1], dtype=torch.float32)
Y = torch.tensor(y_std[1: ], dtype=torch.float32)

X = X.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)
Y = Y.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)

seq_len = X.size(1)
print(seq_len)
```

```
1499
```

Below is the LSTM again with 32 hidden size.

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

torch.manual_seed(0)
np.random.seed(0)

nh = 32
model = lstm_net(nh)
criterion = nn.MSELoss()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
```

Parameter estimation (training) is done below.

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
epoch  100/1000  |  loss = 0.243756
epoch  200/1000  |  loss = 0.227583
epoch  300/1000  |  loss = 0.218399
epoch  400/1000  |  loss = 0.209345
epoch  500/1000  |  loss = 0.188405
epoch  600/1000  |  loss = 0.184548
epoch  700/1000  |  loss = 0.181477
epoch  800/1000  |  loss = 0.179199
epoch  900/1000  |  loss = 0.177259
epoch 1000/1000  |  loss = 0.175526
```

Below we obtain predictions.

```python
model.eval()
with torch.no_grad():
    _, hc = model(X)
    preds = np.zeros(n_future, dtype=np.float32)
    last_in = torch.tensor([[y_std[-1]]], dtype=torch.float32)  # (1, 1, 1) after view
    for t in range(n_future):
        out, hc = model(last_in.view(1, 1, 1), hc)              # reuse hidden state
        next_val = out.squeeze().item()
        preds[t] = next_val
        last_in = torch.tensor([[next_val]], dtype=torch.float32)
```

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

The predictions are decent. Note that the nature of the predictions (which seem quite clean) is quite different from the predictions given by the AR model (these were very noisy).

RNN does not seem to work for this predictions as shown below (this is because of the lack of ability to capture long range dependencies).

```python
class RNNReg(nn.Module):
    def __init__(self, nh):
        super().__init__()
        self.rnn = nn.RNN(1, nh, nonlinearity="tanh", batch_first=True)
        self.fc  = nn.Linear(nh, 1)
    def forward(self, x, h=None):
        out, h = self.rnn(x, h)
        return self.fc(out), h

torch.manual_seed(0)
np.random.seed(0)

nh = 50 #I could not find any value of nh for which the RNN is giving good predictions for this data
model = RNNReg(nh)
criterion = nn.MSELoss()
opt = torch.optim.Adam(model.parameters(),lr = 1e-3)
```

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
epoch  100/1000  |  loss = 0.236083
epoch  200/1000  |  loss = 0.228475
epoch  300/1000  |  loss = 0.221912
epoch  400/1000  |  loss = 0.209255
epoch  500/1000  |  loss = 0.197350
epoch  600/1000  |  loss = 0.200900
epoch  700/1000  |  loss = 0.196046
epoch  800/1000  |  loss = 0.204768
epoch  900/1000  |  loss = 0.205714
epoch 1000/1000  |  loss = 0.182275
```

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

These RNN predictions seem decent initially but they deviate considerably from the LSTM predictions as we go further into the future.

## Sunspots Data

Below we apply LSTM, RNN and GRU to obtain predictions for the sunspots dataset.

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
print(sunspots.head())
y = sunspots.iloc[:,1].values
n = len(y)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
print(n)
n_future = 300
```

```
0     1    2  3  4
0  1700.5   8.3 -1.0 -1  1
1  1701.5  18.3 -1.0 -1  1
2  1702.5  26.7 -1.0 -1  1
3  1703.5  38.3 -1.0 -1  1
4  1704.5  60.0 -1.0 -1  1
325
```

*(1 figure omitted — see the original notebook.)*

First we prepare $X$ and $Y$.

```python
mu, sig = y.mean(), y.std()
y_std = (y - mu) / sig

X = torch.tensor(y_std[:-1], dtype=torch.float32)
Y = torch.tensor(y_std[1: ], dtype=torch.float32)

X = X.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)
Y = Y.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)

seq_len = X.size(1)
print(seq_len)
```

```
324
```

We fit LSTM with the number of hidden units equaling 64.

## LSTM for Sunspots

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

torch.manual_seed(0)
np.random.seed(0)

nh = 64
model = lstm_net(nh)
criterion = nn.MSELoss()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
```

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
epoch  100/1000  |  loss = 0.178550
epoch  200/1000  |  loss = 0.089431
epoch  300/1000  |  loss = 0.063866
epoch  400/1000  |  loss = 0.042808
epoch  500/1000  |  loss = 0.036359
epoch  600/1000  |  loss = 0.030837
epoch  700/1000  |  loss = 0.025321
epoch  800/1000  |  loss = 0.021516
epoch  900/1000  |  loss = 0.017578
epoch 1000/1000  |  loss = 0.015462
```

```python
model.eval()
with torch.no_grad():
    _, hc = model(X)
    preds = np.zeros(n_future, dtype=np.float32)
    last_in = torch.tensor([[y_std[-1]]], dtype=torch.float32)  # (1, 1, 1) after view
    for t in range(n_future):
        out, hc = model(last_in.view(1, 1, 1), hc)              # reuse hidden state
        next_val = out.squeeze().item()
        preds[t] = next_val
        last_in = torch.tensor([[next_val]], dtype=torch.float32)
```

```python
lstm_preds_orig = preds * sig + mu
tme_pred_axis = np.arange(n, n + n_future)

plt.figure(figsize=(12,6))
plt.plot(np.arange(n), y, lw=2, label="Data")
plt.plot(tme_pred_axis, lstm_preds_orig, lw=2, color="r", label="forecast (LSTM)")
plt.xlabel("Time"); plt.ylabel("Data")
plt.title("Data and Forecast")
plt.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions for the LSTM look quite realistic. They are quite different in characteristic from the predictions generated by an AR($p$) model (the AR($p$) predictions oscillate for a short while before settling to a constant value; in contrast, the LSTM predictions seem to oscillate well into the future in a way that is visually similar to the true dataset).

## RNN for Sunspots

Next we apply the RNN (again with 64 hidden units).

```python
torch.manual_seed(0)
np.random.seed(0)

nh = 64
class RNNReg(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(1, nh, nonlinearity="tanh", batch_first=True)
        self.fc  = nn.Linear(nh, 1)
    def forward(self, x, h=None):
        out, h = self.rnn(x, h)
        return self.fc(out), h

model = RNNReg()
opt   = torch.optim.Adam(model.parameters(), lr=1e-3)
lossf = nn.MSELoss()


for epoch in range(1000):
    opt.zero_grad()
    pred,_ = model(X)
    loss   = lossf(pred, Y)
    loss.backward();  opt.step()
    if epoch % 100 == 0:
        print(f"epoch {epoch:4d}/{n_epochs}  |  loss = {loss.item():.6f}")
```

```
epoch    0/1000  |  loss = 0.904697
epoch  100/1000  |  loss = 0.177153
epoch  200/1000  |  loss = 0.113939
epoch  300/1000  |  loss = 0.086803
epoch  400/1000  |  loss = 0.066403
epoch  500/1000  |  loss = 0.062139
epoch  600/1000  |  loss = 0.050468
epoch  700/1000  |  loss = 0.035208
epoch  800/1000  |  loss = 0.030020
epoch  900/1000  |  loss = 0.031938
```

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
rnn_preds_orig = preds*sig + mu
tme_pred_axis = np.arange(n, n + n_future)

plt.figure(figsize=(12,6))
plt.plot(np.arange(n), y, lw=2, label="Data")
plt.plot(tme_pred_axis, rnn_preds_orig, lw=2, color="r", label="forecast (RNN)")
plt.xlabel("Time"); plt.ylabel("Data")
plt.title("Data and Forecast")
plt.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

These predictions do not appear as realistic as the LSTM forecasts.

## GRU for Sunspots

Below we fit the GRU again with 64 hidden units. The code works in exactly the same way as LSTM and RNN.

```python
torch.manual_seed(0)
np.random.seed(0)

nh = 64
class GRUReg(nn.Module):
    def __init__(self):
        super().__init__()
        self.gru = nn.GRU(1, nh, batch_first=True)
        self.fc  = nn.Linear(nh,1)
    def forward(self,x,h=None):
        out,h = self.gru(x,h)
        return self.fc(out),h
model = GRUReg()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
lossf = nn.MSELoss()
```

```python
for epoch in range(1000):
    opt.zero_grad()
    pred,_ = model(X)
    loss = lossf(pred, Y)
    loss.backward(); opt.step()
    if epoch % 100 == 0:
        print(f"epoch {epoch:4d}/{n_epochs}  |  loss = {loss.item():.6f}")
```

```
epoch    0/1000  |  loss = 1.017522
epoch  100/1000  |  loss = 0.193518
epoch  200/1000  |  loss = 0.111449
epoch  300/1000  |  loss = 0.082548
epoch  400/1000  |  loss = 0.063553
epoch  500/1000  |  loss = 0.054251
epoch  600/1000  |  loss = 0.041851
epoch  700/1000  |  loss = 0.056074
epoch  800/1000  |  loss = 0.028392
epoch  900/1000  |  loss = 0.046378
```

```python
model.eval()
with torch.no_grad():
    _,h = model(X)
    preds = np.zeros(n_future,np.float32)
    last  = torch.tensor([[y_std[-1]]], dtype=torch.float32)
    for t in range(n_future):
        out,h = model(last.view(1,1,1),h)
        preds[t]=out.item()
        last = torch.tensor([[preds[t]]], dtype=torch.float32)

gru_preds_orig = preds*sig+mu
plt.figure(figsize=(12,6))
plt.plot(np.arange(len(y)),y,lw=2,label="Data")
plt.plot(np.arange(len(y),len(y)+n_future),gru_preds_orig, lw=2,label="Forecast (GRU)",color="orange")
plt.legend()
plt.title("Data and Forecast"); plt.legend(); plt.tight_layout(); plt.show()
```

*(1 figure omitted — see the original notebook.)*

Again the predictions do not look as realistic as those produced by the LSTM.

## Simulation Three

The following dataset is simulated according to the model:
\begin{equation*}
   y_t = 0.9 \sin (0.5\pi y_{t - p}) + \epsilon_t
\end{equation*}
for some fixed $p$. This equation is for $t \geq p+1$. For $t \leq p$, we take $y_t$ to be linear. We take $p$ to be a large value.

```python
n = 1500
truelag = 85
rng = np.random.default_rng(seed=0)
#sig_noise = 0.05
sig_noise = 0.01

eps = rng.normal(loc=0, scale=sig_noise, size=n)
y_sim = np.full(shape=n, fill_value=-999.0)
y_sim[0:truelag] = np.linspace(-1, 1, truelag)
for i in range(truelag, n):
    y_sim[i] = 0.9 * np.sin(0.5 * np.pi * y_sim[i - truelag]) + eps[i]
#y_sim = y_sim + eps

plt.figure(figsize = (12, 6))
plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us obtain predictions for future values using the actual function $g(y) = 0.9 \sin(0.5 \pi y)$ from which the data were generated. These predictions (which we can refer to as Oracle Predictions) will form the benchmark which we can use to compare the predictions of various methods (AR, LSTM, RNN, GRU).

```python

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Oracle Predictions →](03-oracle-predictions.md)
