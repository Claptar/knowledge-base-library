---
title: Airline Passengers Dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab14.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Airline Passengers Dataset

The airline passengers dataset is a popular dataset for evaluating prediction accuracy of various models. It contains monthly data on the number of international airline passengers (in thousands) from January 1949 to December 1960.

```python
data = sm.datasets.get_rdataset("AirPassengers").data
print(data.head())

y = data['value'].to_numpy()

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

```
time  value
0  1949.000000    112
1  1949.083333    118
2  1949.166667    132
3  1949.250000    129
4  1949.333333    121
```

*(1 figure omitted — see the original notebook.)*

Let us apply the LSTM model to predict future observations for this dataset. We first remove the increasing trend from the data by fitting a line and taking the residuals.

```python
n = len(y)
tme = np.arange(0, n)
X = np.column_stack([np.ones(n), tme])

linmod = sm.OLS(y, X).fit()
y_notrend = linmod.resid

plt.figure(figsize = (12, 6))
plt.plot(y_notrend)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now let us use LSTM. We will first fit the model to the detrended data, then obtain predictions for the detrended data, and convert these into predictions for the original data.

```python
mu, sig = y_notrend.mean(), y_notrend.std()
y_std = (y_notrend - mu) / sig

X = torch.tensor(y_std[:-1], dtype=torch.float32)
Y = torch.tensor(y_std[1: ], dtype=torch.float32)

X = X.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)
Y = Y.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)

seq_len = X.size(1)
print(seq_len)
```

```
143
```

```python
class lstm_net(nn.Module):
    def __init__(self, nh):
        super().__init__()
        self.rnn = nn.LSTM(input_size=1, hidden_size=nh,
                           batch_first=True)
        self.fc  = nn.Linear(nh, 1)      # many-to-many

    def forward(self, x, hc=None):
        out, hc = self.rnn(x, hc)        # out: (batch_size, seq_len, hidden_size)
        out     = self.fc(out)           # (batch_size, seq_len, 1)
        return out, hc

torch.manual_seed(0)
np.random.seed(0)

nh = 200
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

n_future = 60
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

tme_pred_axis = np.arange(n, n+n_future)
lstm_preds_orig = (preds * sig + mu) + linmod.params[0] + linmod.params[1] * tme_pred_axis

plt.figure(figsize = (12,6))
plt.plot(np.arange(n), y, lw = 2, label = "Data")
plt.plot(tme_pred_axis, lstm_preds_orig, lw = 2, color = "r", label = "Forecast (LSTM)")
plt.xlabel("Time"); plt.ylabel("Data")
plt.title("Airlines Passengers Data and Forecast using LSTM")
plt.legend()
plt.tight_layout()
plt.show()
```

```
epoch  100/1000  |  loss = 0.133838
epoch  200/1000  |  loss = 0.074407
epoch  300/1000  |  loss = 0.063738
epoch  400/1000  |  loss = 0.053620
epoch  500/1000  |  loss = 0.040483
epoch  600/1000  |  loss = 0.024853
epoch  700/1000  |  loss = 0.014565
epoch  800/1000  |  loss = 0.006797
epoch  900/1000  |  loss = 0.007944
epoch 1000/1000  |  loss = 0.004411
```

*(1 figure omitted — see the original notebook.)*

---

[← Presence of Trend](03-presence-of-trend.md) · [Up: contents](index.md)
