---
title: Download S&P 500 data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Download S&P 500 data

**Source:** [`CodeLectureThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

sp500 = yf.download('^GSPC', start='2000-01-01', end='2024-01-01', auto_adjust=True)

sp500_closeprice = sp500['Close'].to_numpy().flatten() #this is the daily closing price of the S&P 500 index

plt.figure(figsize=(12,6))
plt.plot(sp500_closeprice, label="Price")
plt.xlabel("Date")
plt.title("S&P 500 daily closing price")
plt.ylabel("Price (dollar)")
plt.legend()
plt.show()
```

```
[*********************100%***********************]  1 of 1 completed
```

*(1 figure omitted — see the original notebook.)*

Instead of working with the prices directly, we work with percentage daily returns.

```python
log_prices = np.log(sp500_closeprice)
y = 100 * np.diff(log_prices) #these are the percentage daily returns
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.title('SNP Daily Percentage Returns')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This clearly shares features with the simulated datasets.

We shall study estimation of $\tau_t$ from these datasets in the next lecture.

---

[← Summary statistics](06-summary-statistics.md) · [Up: contents](index.md)
