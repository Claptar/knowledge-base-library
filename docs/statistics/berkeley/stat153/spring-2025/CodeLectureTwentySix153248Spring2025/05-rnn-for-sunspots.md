---
title: RNN for Sunspots
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentySix153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# RNN for Sunspots

**Source:** [`CodeLectureTwentySix153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Next we apply the RNN (again with 200 hidden units).

```python
torch.manual_seed(0)
np.random.seed(0)

nh = 200
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
epoch    0/1000  |  loss = 1.003679
epoch  100/1000  |  loss = 0.141562
epoch  200/1000  |  loss = 0.082867
epoch  300/1000  |  loss = 0.056757
epoch  400/1000  |  loss = 0.047312
epoch  500/1000  |  loss = 0.025869
epoch  600/1000  |  loss = 0.014358
epoch  700/1000  |  loss = 0.008335
epoch  800/1000  |  loss = 0.133992
epoch  900/1000  |  loss = 0.089119
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

---

[← LSTM for Sunspots](04-lstm-for-sunspots.md) · [Up: contents](index.md) · [GRU for Sunspots →](06-gru-for-sunspots.md)
