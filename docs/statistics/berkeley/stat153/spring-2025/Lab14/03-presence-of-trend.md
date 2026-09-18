---
title: Presence of Trend
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab14.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Presence of Trend

LSTM models do not work well where there is trend in the data. In such cases, remove the trend first (say by fitting a line and considering residuals) before fitting models.

```python
n = 1500
truelag = 85
rng = np.random.default_rng(seed = 0)
#sig_noise = 0.05
sig_noise = 0.01

eps = rng.normal(loc=0, scale=sig_noise, size=n)
y_sim = np.full(shape=n, fill_value=-999.0)
y_sim[0:truelag] = np.linspace(-1, 1, truelag)
for i in range(truelag, n):
    y_sim[i] = 0.9 * np.sin(0.5 * np.pi * y_sim[i - truelag]) + eps[i]
#y_sim = y_sim + eps
y_sim = 0.001 * np.arange(1, n + 1) + y_sim

plt.figure(figsize = (12, 6))
plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This data clearly has a linear trend. AR model will work well (as long as $p$ is correctly chosen).

```python
# Let us fit AR(p)
p = truelag
ar = AutoReg(y_sim, lags=p).fit()

n = len(y_sim)
tme = range(1, n+1)
tme_future = range(n+1, n+n_future+1)
fcast = ar.get_prediction(start=n, end=n+n_future-1).predicted_mean

plt.figure(figsize = (12, 7))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, fcast, label = 'Forecast (AR(p))', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now let us use LSTM for prediction.

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
        self.rnn = nn.LSTM(input_size=1, hidden_size=nh, batch_first=True)
        self.fc  = nn.Linear(nh, 1)      # many-to-many

    def forward(self, x, hc=None):
        out, hc = self.rnn(x, hc)        # out: (batch, seq_len, hidden_size)
        out     = self.fc(out)           # (batch, seq_len, 1)
        return out, hc

torch.manual_seed(0)
np.random.seed(0)

nh = 40
model = lstm_net(nh)
criterion = nn.MSELoss()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

n_epochs = 1000
for epoch in range(1, n_epochs + 1):
    #model.train()
    opt.zero_grad()

    pred, _ = model(X)           # hidden state auto-reset every epoch
    loss = criterion(pred, Y)
    loss.backward()

    opt.step()

    if epoch % 100 == 0:
        print(f"epoch {epoch:4d}/{n_epochs}  |  loss = {loss.item():.6f}")

#model.eval()
with torch.no_grad():
    _, hc = model(X)
    preds = np.zeros(n_future, dtype=np.float32)
    last_in = torch.tensor([[y_std[-1]]], dtype=torch.float32)  # (1, 1, 1) after view

    for t in range(n_future):
        out, hc = model(last_in.view(1, 1, 1), hc)              # reuse hidden state
        next_val = out.squeeze().item()
        preds[t] = next_val
        last_in = torch.tensor([[next_val]], dtype=torch.float32)

lstm_preds_orig = preds * sig + mu
tme_pred_axis = np.arange(n, n + n_future)

plt.figure(figsize=(12,6))
plt.plot(np.arange(n), y_sim, lw=2, label="Data")
plt.plot(tme_pred_axis, lstm_preds_orig, lw=2, color="r", label="Forecast (LSTM)")
plt.plot(tme_pred_axis, fcast, lw=2, color="black", label="Forecast (AR)")
plt.xlabel("Time"); plt.ylabel("Data")
plt.title("Data and Forecast")
plt.legend()
plt.tight_layout()
plt.show()
```

```
epoch  100/1000  |  loss = 0.116244
epoch  200/1000  |  loss = 0.076563
epoch  300/1000  |  loss = 0.059973
epoch  400/1000  |  loss = 0.054006
epoch  500/1000  |  loss = 0.052959
epoch  600/1000  |  loss = 0.050079
epoch  700/1000  |  loss = 0.037976
epoch  800/1000  |  loss = 0.038874
epoch  900/1000  |  loss = 0.030605
epoch 1000/1000  |  loss = 0.025062
```

*(1 figure omitted — see the original notebook.)*

Clearly the predictions flatten out as the prediction horizon increases. This shows that detrending is recommended while working with LSTM models.

---

[← LSTM](02-lstm.md) · [Up: contents](index.md) · [Airline Passengers Dataset →](04-airline-passengers-dataset.md)
