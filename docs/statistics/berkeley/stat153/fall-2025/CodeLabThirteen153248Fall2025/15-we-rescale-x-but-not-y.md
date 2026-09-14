---
title: we rescale x but not y
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# we rescale x but not y

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

x_raw = np.arange(1, n+1)
x_scaled = (x_raw - np.mean(x_raw))/(np.std(x_raw))
y_torch = torch.tensor(y, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)
```

We now select the initial values. We take $c_1, \dots, c_k$ to be quantiles of $x_t$ at $1/(k+1), \dots, k/(k+1)$. For $\beta_0, \dots, \beta_{k+2}$, we run a linear regression of $\log y_t$ on $1, x_t, (x_t - c_1)_+, \dots, (x_t - c_k)_+$ with these initial $c_1, \dots, c_k$ and then take the corresponding coefficients.

```python
k = 8 # this is the number of knots
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_scaled, quantile_levels)

n = len(y)
X = np.column_stack([np.ones(n), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float)) * (x_scaled - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(np.log(np.abs(y)), X).fit()

#print(md_init.summary())
#print(md_init.params)
beta_init = md_init.params
print(knots_init)
print(beta_init)
```

```
[-1.34647722 -0.96176944 -0.57706167 -0.19235389  0.19235389  0.57706167
  0.96176944  1.34647722]
[ 7.44006624  6.59898963 -8.17888252  0.61656712  5.50695701 -1.94742617
 -5.67882692  2.43967538  5.87140635 -4.41572431]
```

We now use PyTorch to estimate $\alpha_t$. The first step is to create the model. We use the same piecewise linear model that we used in Lecture 24.

```python
class PiecewiseLinearModel(nn.Module):
    def __init__(self, knots_init, beta_init):
        super().__init__()
        self.num_knots = len(knots_init)
        self.beta = nn.Parameter(torch.tensor(beta_init, dtype = torch.float32))
        self.knots = nn.Parameter(torch.tensor(knots_init, dtype = torch.float32))

    def forward(self, x):
        knots_sorted, _ = torch.sort(self.knots)
        out = self.beta[0] + self.beta[1] * x
        for j in range(self.num_knots):
            out += self.beta[j + 2] * torch.relu(x - knots_sorted[j])
        return out
```

The following code creates this model.

```python
md_PiecewiseLinear = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)

---

[← Generating Data using the above smooth function](14-generating-data-using-the-above-smooth-function.md) · [Up: contents](index.md) · [This code creates an instance of our custom neural network class →](16-this-code-creates-an-instance-of-our-custom-neural-network-c.md)
