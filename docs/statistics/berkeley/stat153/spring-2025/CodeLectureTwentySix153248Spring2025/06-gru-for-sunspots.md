---
title: GRU for Sunspots
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentySix153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# GRU for Sunspots

**Source:** [`CodeLectureTwentySix153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Below we fit the GRU again with 200 hidden units. The code works in exactly the same way as LSTM and RNN.

```python
torch.manual_seed(0)
np.random.seed(0)

nh = 200
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
epoch    0/1000  |  loss = 1.034648
epoch  100/1000  |  loss = 0.124171
epoch  200/1000  |  loss = 0.071740
epoch  300/1000  |  loss = 0.042880
epoch  400/1000  |  loss = 0.033138
epoch  500/1000  |  loss = 0.068680
epoch  600/1000  |  loss = 0.018391
epoch  700/1000  |  loss = 0.074656
epoch  800/1000  |  loss = 0.030435
epoch  900/1000  |  loss = 0.017239
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

---

[← RNN for Sunspots](05-rnn-for-sunspots.md) · [Up: contents](index.md)
