---
title: Simulated Dataset One
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentySix153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Simulated Dataset One

**Source:** [`CodeLectureTwentySix153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

Next we apply LSTM (and RNN). The first step is to create the input and output tensors.

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

We create the LSTM model class below.

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

nh = 100
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
epoch  100/1000  |  loss = 0.238784
epoch  200/1000  |  loss = 0.183601
epoch  300/1000  |  loss = 0.178046
epoch  400/1000  |  loss = 0.165648
epoch  500/1000  |  loss = 0.161582
epoch  600/1000  |  loss = 0.155341
epoch  700/1000  |  loss = 0.151636
epoch  800/1000  |  loss = 0.158860
epoch  900/1000  |  loss = 0.158528
epoch 1000/1000  |  loss = 0.139661
```

Predictions are obtained as follows.

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

In the code above, the LSTM receives a single stream of length $T \approx 1500$ (with batch = 1), so every training step must iterate through 1500 recurrent updates, store all intermediate gate outputs, cell states, and hidden states for back-propagation-through-time, and then sweep backward through those same 1500 steps. The result is a high per-epoch cost--roughly proportional to $T$ both in floating-point operations and in memory.

To make the code faster, we can attempt to chunk the original time series into a small number (say $3$) of batches of a smaller number (say 450) samples, and then to stack them so that the input tensor is of shape (3, 450, 1). Each forward/backward pass now unrolls only 450 steps (a 3.3 times reduction) and the three batches can even be procesed in parallel along the batch dimension. This combination of a shallower time depth and batching typically leads to a speed up in the code. However, the trade‑off is that the hidden state is implicitly reset at every window boundary, so the model cannot capture dependencies that span more than 450 time steps; for tasks that truly require very long‑range memory, the slower single‑sequence approach is safer.

Below we illustrate this batching idea.

### Batching

```python
seq_len_batch = 450
n_batches = (len(y_std) - 1) // seq_len_batch
print(n_batches)

X_batches = []
Y_batches = []
for i in range(n_batches):
    start_idx = i * seq_len_batch
    end_idx = start_idx + seq_len_batch
    X_batches.append(y_std[start_idx : end_idx])
    Y_batches.append(y_std[(start_idx + 1): (end_idx + 1)])

X = torch.tensor(X_batches, dtype = torch.float32).unsqueeze(-1)
Y = torch.tensor(Y_batches, dtype = torch.float32).unsqueeze(-1)

print(X.shape)
print(Y.shape)
```

```
3
torch.Size([3, 450, 1])
torch.Size([3, 450, 1])
```

```python
class lstm_net(nn.Module):
    def __init__(self, nh):
        super().__init__()
        self.rnn = nn.LSTM(input_size=1, hidden_size=nh,
                           batch_first=True)
        self.fc  = nn.Linear(nh, 1)          # many-to-many
    def forward(self, x, hc=None):
        out, hc = self.rnn(x, hc)            # out: (B, T, nh)
        out     = self.fc(out)               # (B, T, 1)
        return out, hc

torch.manual_seed(0)
np.random.seed(0)

nh = 100
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
epoch  100/1000  |  loss = 0.235551
epoch  200/1000  |  loss = 0.190747
epoch  300/1000  |  loss = 0.169411
epoch  400/1000  |  loss = 0.158637
epoch  500/1000  |  loss = 0.159057
epoch  600/1000  |  loss = 0.144519
epoch  700/1000  |  loss = 0.151861
epoch  800/1000  |  loss = 0.132501
epoch  900/1000  |  loss = 0.123780
epoch 1000/1000  |  loss = 0.176492
```

Once the model is trained, I revert back to the previous $X$ and $Y$ (without batching) in order to calculate predictions.

```python
mu, sig = y_sim.mean(), y_sim.std()
y_std = (y_sim - mu) / sig

X = torch.tensor(y_std[:-1], dtype=torch.float32)
Y = torch.tensor(y_std[1: ], dtype=torch.float32)

X = X.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)
Y = Y.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)

seq_len = X.size(1)
print(seq_len)

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

lstm_preds_orig_batch = preds * sig + mu
tme_pred_axis = np.arange(n, n + n_future)

plt.figure(figsize=(12,6))
plt.plot(np.arange(n), y_sim, lw=2, label="Data")
plt.plot(tme_pred_axis, lstm_preds_orig, lw=2, color="r", label="forecast (LSTM)")
plt.plot(tme_pred_axis, lstm_preds_orig_batch, lw=2, color="green", label="forecast (LSTM Batch)")
plt.xlabel("Time"); plt.ylabel("Data")
plt.title("Data and Forecast")
for t in range(0, n + n_future, truelag):
    plt.axvline(x=t, linestyle='--', color='gray', linewidth=1)
plt.axhline(y=1, linestyle='--', color='gray', linewidth=1)
plt.axhline(y=-1, linestyle='--', color='gray', linewidth=1)
plt.legend()
plt.tight_layout()
plt.show()
```

```
1499
```

*(1 figure omitted — see the original notebook.)*

In this example, the predictions with and without batching are nearly identical. However batching makes the code run much faster.

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

nh = 50
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
epoch  100/1000  |  loss = 0.283465
epoch  200/1000  |  loss = 0.230474
epoch  300/1000  |  loss = 0.199063
epoch  400/1000  |  loss = 0.190025
epoch  500/1000  |  loss = 0.182842
epoch  600/1000  |  loss = 0.219429
epoch  700/1000  |  loss = 0.221646
epoch  800/1000  |  loss = 0.171874
epoch  900/1000  |  loss = 0.169135
epoch 1000/1000  |  loss = 0.171711
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

RNN gives predictions that are basically the same as the LSTM predictions.

# Simulated Dataset Two

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

Let us see how the LSTM and RNN do. First we fit LSTM without any batching.

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

nh = 100
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
epoch  100/1000  |  loss = 0.234757
epoch  200/1000  |  loss = 0.207985
epoch  300/1000  |  loss = 0.206311
epoch  400/1000  |  loss = 0.195433
epoch  500/1000  |  loss = 0.189044
epoch  600/1000  |  loss = 0.179978
epoch  700/1000  |  loss = 0.173883
epoch  800/1000  |  loss = 0.174173
epoch  900/1000  |  loss = 0.168488
epoch 1000/1000  |  loss = 0.162189
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

Now let us apply batching.

```python
seq_len_batch = 650
n_batches = (len(y_std) - 1) // seq_len_batch
print(n_batches)

X_batches = []
Y_batches = []
for i in range(n_batches):
    start_idx = i * seq_len_batch
    end_idx = start_idx + seq_len_batch
    X_batches.append(y_std[start_idx : end_idx])
    Y_batches.append(y_std[(start_idx + 1): (end_idx + 1)])

X = torch.tensor(X_batches, dtype = torch.float32).unsqueeze(-1)
Y = torch.tensor(Y_batches, dtype = torch.float32).unsqueeze(-1)

print(X.shape)
print(Y.shape)
```

```
2
torch.Size([2, 650, 1])
torch.Size([2, 650, 1])
```

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

nh = 100
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
epoch  100/1000  |  loss = 0.196386
epoch  200/1000  |  loss = 0.172178
epoch  300/1000  |  loss = 0.158832
epoch  400/1000  |  loss = 0.158074
epoch  500/1000  |  loss = 0.177489
epoch  600/1000  |  loss = 0.157444
epoch  700/1000  |  loss = 0.150786
epoch  800/1000  |  loss = 0.147682
epoch  900/1000  |  loss = 0.143554
epoch 1000/1000  |  loss = 0.136835
```

```python
mu, sig = y_sim.mean(), y_sim.std()
y_std = (y_sim - mu) / sig

X = torch.tensor(y_std[:-1], dtype=torch.float32)
Y = torch.tensor(y_std[1: ], dtype=torch.float32)

X = X.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)
Y = Y.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)

seq_len = X.size(1)
print(seq_len)

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

lstm_preds_orig_batch = preds * sig + mu
tme_pred_axis = np.arange(n, n + n_future)

plt.figure(figsize=(12,6))
plt.plot(np.arange(n), y_sim, lw=2, label="Data")
plt.plot(tme_pred_axis, lstm_preds_orig, lw=2, color="r", label="forecast (LSTM)")
plt.plot(tme_pred_axis, lstm_preds_orig_batch, lw=2, color="green", label="forecast (LSTM Batch)")
plt.xlabel("Time"); plt.ylabel("Data")
plt.title("Data and Forecast")
for t in range(0, n + n_future, truelag):
    plt.axvline(x=t, linestyle='--', color='gray', linewidth=1)
plt.axhline(y=1, linestyle='--', color='gray', linewidth=1)
plt.axhline(y=-1, linestyle='--', color='gray', linewidth=1)
plt.legend()
plt.tight_layout()
plt.show()
```

```
1499
```

*(1 figure omitted — see the original notebook.)*

The predictions with and without batching are similar (I am using sequence length equaling 650 here; for different values of this parameter, the predictions seem different from the full-sequence predictions).

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
epoch  100/1000  |  loss = 0.234295
epoch  200/1000  |  loss = 0.228924
epoch  300/1000  |  loss = 0.224068
epoch  400/1000  |  loss = 0.208632
epoch  500/1000  |  loss = 0.220152
epoch  600/1000  |  loss = 0.195136
epoch  700/1000  |  loss = 0.190942
epoch  800/1000  |  loss = 0.219482
epoch  900/1000  |  loss = 0.197227
epoch 1000/1000  |  loss = 0.197343
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

---

[← The LSTM Unit](01-the-lstm-unit.md) · [Up: contents](index.md) · [Sunspots Data →](03-sunspots-data.md)
