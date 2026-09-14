---
title: Let's plot it and our x and y origin lines
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let's plot it and our x and y origin lines

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize=(5,2))
plt.plot(t, y)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.xlabel('Time')
plt.ylabel('value')
```

```
Text(0, 0.5, 'value')
```

*(1 figure omitted — see the original notebook.)*

## Let's first find f with grid search

```python
print(len(t))
f_grid = np.linspace(0,20,1000)

RSS = np.zeros(len(f_grid))
for idx, f_hat in enumerate(f_grid):
    cos_col = np.cos(2 * np.pi * f_hat * t )
    sin_col = np.sin(2 * np.pi * f_hat * t )
    X = np.column_stack([np.ones(len(t)), cos_col, sin_col])

    model = sm.OLS(y, X).fit()
    betas = model.params
    RSS[idx] = np.sum(model.resid **2)

plt.figure(figsize=(5,1))
plt.plot(f_grid, RSS,'-')
f_hat = f_grid[RSS.argmin()] # Find the best f_hat
plt.axvline(f_hat, color='r', linewidth=0.5, linestyle='--')
plt.text(f_hat + 1, np.min(RSS), f'f={f_hat:.3f}')
plt.xlabel('Frequency')
plt.ylabel('RSS')
```

```
1000
Text(0, 0.5, 'RSS')
```

*(1 figure omitted — see the original notebook.)*

## Use our best f to calculate the other coefficients

We will now make our X matrix as discussed in class:

$$
  X_f = \begin{pmatrix}
    1 & \cos(2\pi \hat{f} t_0) & \sin(2\pi \hat{f} t_0) \\
    \vdots & \vdots & \vdots \\
    1 & \cos(2\pi \hat{f} t_n) & \sin(2\pi \hat{f} t_n) \\
    \end{pmatrix}
$$

and use it to calculate our $\beta$ coefficients with OLS.

```python
cos_col = np.cos(2 * np.pi * f_hat * t )
sin_col = np.sin(2 * np.pi * f_hat * t )
X = np.column_stack([np.ones(len(t)), cos_col, sin_col])

model = sm.OLS(y, X).fit()
betas = model.params
y_hat = model.fittedvalues

plt.figure(figsize=(5,1))
plt.plot(y, label='y')
plt.plot(y_hat, label='yhat')
plt.legend()

plt.figure(figsize=(2,2))
plt.plot(y, y_hat,'.')
plt.xlabel('y')
plt.ylabel('yhat')
```

```
Text(0, 0.5, 'yhat')
```

*(2 figures omitted — see the original notebook.)*

## A Perfect Model

This sinusoidal model looks pretty good, but it doesn't perfectly fit all of the fluctuations in our data - there is still some residual variance not explained. So what if we tried to do even better by increasing the number of parameters?

One (not advised) way is to fit a model where our number of parameters is equal to our number of observations over time ($p=n$). We'll see how this can fit our data well, but still be quite problematic.

This is like doing


$$
  X = \begin{pmatrix}
    1 & \cos(2\pi f_0 t_0) & \sin(2\pi f_0 t_0) & \cdots & \cos(2\pi f_p t_0) & \sin(2\pi f_p t_0) \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    1 & \cos(2\pi f_0 t_n) & \sin(2\pi f_0 t_n) & \cdots & \cos(2\pi f_p t_n) & \sin(2\pi f_p t_n) \\
    \end{pmatrix}
$$

Where we test all possible combinations of sines and cosines at various frequencies $f_0 \dots f_p$.

```python

---

[← Our true sinusoid](02-our-true-sinusoid.md) · [Up: contents](index.md) · [What about if p = n →](04-what-about-if-p-n.md)
