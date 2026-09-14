---
title: More on model fitting using PyTorch
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# More on model fitting using PyTorch

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

## Piecewise Linear Model via Pytorch: importance of scaling

The following dataset is from \url{https://fred.stlouisfed.org/series/TLCOMCONS}. It is slightly different from the dataset used in Lecture 24 (which was \url{https://fred.stlouisfed.org/series/TTLCONS}).

```python
ttlcons = pd.read_csv('TLCOMCONS_23April2025.csv')
print(ttlcons.head(10))
print(ttlcons.tail(10))

y_raw = ttlcons['TLCOMCONS']
n = len(y_raw)
x_raw = np.arange(1, n+1)

plt.figure(figsize = (12, 6))
plt.plot(y_raw)
plt.xlabel("Time (months)")
plt.ylabel('Millions of Dollars')
plt.title("Total Construction Spending in the United States")
plt.show()
```

```
observation_date  TLCOMCONS
0       2002-01-01      68254
1       2002-02-01      65840
2       2002-03-01      66722
3       2002-04-01      64879
4       2002-05-01      62741
5       2002-06-01      60982
6       2002-07-01      58971
7       2002-08-01      61223
8       2002-09-01      61997
9       2002-10-01      61772
    observation_date  TLCOMCONS
268       2024-05-01     126084
269       2024-06-01     125371
270       2024-07-01     124989
271       2024-08-01     125184
272       2024-09-01     125608
273       2024-10-01     124379
274       2024-11-01     125270
275       2024-12-01     125645
276       2025-01-01     124650
277       2025-02-01     125988
```

*(1 figure omitted — see the original notebook.)*

Let us try to fit the model:
\begin{equation*}
  y_t = \beta_0 + \beta_1 t + \beta_2 (x_t - c_1)_+ + \beta_3 (x_t - c_2)_+ + \dots + \beta_{k+1} (x_t - c_k)_+ + \epsilon_t
\end{equation*}
where the unknown parameters are $\beta_0,\beta_1, \dots, \beta_{k+1}$ and $c_1, \dots, c_k$ (as well as $\sigma$ which is the noise level in $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$). We will fix a value of $k$. Here $x_t = t$. In Lecture 24, we fit this model after taking logarithms; here let us work with the original data to see the importance of scaling variables.

In PyTorch, this model can be coded as follows.

```python
class PiecewiseLinearModel(nn.Module):
    def __init__(self, knots_init, beta_init):
        super().__init__()
        self.num_knots = len(knots_init)
        self.beta = nn.Parameter(torch.tensor(beta_init, dtype=torch.float32))
        self.knots = nn.Parameter(torch.tensor(knots_init, dtype=torch.float32))
        # When a tensor is wrapped in nn.Parameter and assigned as an attribute to a nn.Module,
        # it is automatically registered as a parameter of that module.

    def forward(self, x):
        knots_sorted, _ = torch.sort(self.knots)
        out = self.beta[0] + self.beta[1] * x
        for j in range(self.num_knots):
            out += self.beta[j + 2] * torch.relu(x - knots_sorted[j])
        return out
```

The parameters will be estimated simply by least squares, i.e., by minimizing
\begin{equation*}
  \sum_{t=1}^n \left(y_t - \beta_0 - \beta_1 t - \beta_2 (x_t - c_1)_+ - \dots - \beta_{k+1} (x_t - c_k)_+ \right)^2
\end{equation*}
This is possibly a non-convex minimization problem (note that we are optimizing over $c_1, \dots, c_k$ as well). The algorithm used will be gradient descent (or a variant such as Adam). Initialization will be important for the algorithm to work well and not get stuck in bad local minima.

Here is how the least squares minimization is solved in PyTorch. The first step is to convert the data y_raw and x_raw into PyTorch tensors.

```python
y_raw_torch = torch.tensor(y_raw, dtype = torch.float32).unsqueeze(1)
x_raw_torch = torch.tensor(x_raw, dtype = torch.float32).unsqueeze(1)

print(y_raw_torch.shape)
print(x_raw_torch.shape)
```

```
torch.Size([278, 1])
torch.Size([278, 1])
```

The next step is to create suitable initialization. It is natural to take $c_1, \dots, c_k$ to be quantiles of $x_t$ at $1/(k+1), \dots, k/(k+1)$. For $\beta_0, \dots, \beta_{k+2}$, we run a linear regression with these initial $c_1, \dots, c_k$ and then take the corresponding coefficients.

```python

---

[Up: contents](index.md) · [First fix the number of knots →](02-first-fix-the-number-of-knots.md)
