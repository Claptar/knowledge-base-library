---
title: Sunspots Data
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentySix153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sunspots Data

**Source:** [`CodeLectureTwentySix153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

Because the data size is not very large, we do not use any batching and directly apply the models on the full sequence. First we prepare $X$ and $Y$.

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

We fit LSTM with the number of hidden units equaling 200.

---

[← Simulated Dataset One](02-simulated-dataset-one.md) · [Up: contents](index.md) · [LSTM for Sunspots →](04-lstm-for-sunspots.md)
