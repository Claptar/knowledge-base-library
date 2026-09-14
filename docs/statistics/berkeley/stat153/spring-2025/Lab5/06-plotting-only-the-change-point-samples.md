---
title: Plotting only the change-point samples
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plotting only the change-point samples

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize = (15, 6))
plt.plot(y)

for i in range(N):
    c = cpostsamples[i]
    plt.axvline(c, color = 'red')

plt.axvline(5000, color = 'black') # 5000 is the true value of c
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Example with multiple change-points

We now consider an example where there are three change points and the model we want to use is:
\begin{equation*}
   y_t = \beta_0 + \beta_1 I\{t > c_1\} + \beta_2 I\{t > c_2\} + \beta_3 I\{t > c_3\} + \epsilon_t
\end{equation*}
We work on a simulated dataset that is generated as follows.

```python
sig = 1
mu1 = 0
mu2 = 1.5
mu3 = -1
mu4 = 0

truedt = np.concatenate((np.repeat(mu1, 100), np.repeat(mu2, 100), np.repeat(mu3, 100), np.repeat(mu4, 100)), axis = None)
n = len(truedt)
noise = rng.normal(size = n)

y = truedt + sig * noise

plt.plot(y)
plt.show()

cps_true = np.array([100, 200, 300]) # these are true changepoints
print(cps_true)
```

```
[100 200 300]
```

*(1 figure omitted — see the original notebook.)*

The following is the RSS for fitting three change points to the data.

```python
def rss(c):
    n = len(y)
    x = np.arange(1, n + 1)
    X = np.column_stack([np.ones(n)])

    if np.isscalar(c):
        c = [c]

    for j in range(len(c)):
        xc = ((x > c[j]).astype(float))
        X = np.column_stack([X, xc])

    md = sm.OLS(y, X).fit()
    ans = np.sum(md.resid ** 2)

    return ans
```

```python
c1_gr = np.arange(75, 126)
c2_gr = np.arange(175, 226)
c3_gr = np.arange(275, 326)
X, Y, Z = np.meshgrid(c1_gr, c2_gr, c3_gr)

g = pd.DataFrame({'x': X.flatten(), 'y': Y.flatten(), 'z': Z.flatten()})
g['rss'] = g.apply(lambda row: rss([row['x'], row['y'], row['z']]), axis = 1)

---

[← this plot looks similar to the RSS plot](05-this-plot-looks-similar-to-the-rss-plot.md) · [Up: contents](index.md) · [this is taking about 49 secs to run on my laptop →](07-this-is-taking-about-49-secs-to-run-on-my-laptop.md)
