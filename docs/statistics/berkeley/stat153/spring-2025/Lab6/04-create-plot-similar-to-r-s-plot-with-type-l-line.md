---
title: Create plot similar to R's plot with type="l" (line)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab6.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab6.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Create plot similar to R's plot with type="l" (line)

**Source:** [`Lab6.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab6.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize = (10, 6))
plt.plot(truth)
plt.title("Blocks Function")
plt.xlabel("Time")
plt.ylabel("y")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
sig = 5
rng = np.random.default_rng(seed = 42)
errorsamples = rng.normal(loc = 0, scale = sig, size = n)
y = truth + errorsamples
```

```python
plt.plot(y, label = 'Data')
plt.plot(truth, label = 'true trend', color = 'red')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We will use the following model for this dataset:
\begin{equation*}
    y_t = \beta_0 + \beta_1 I\{t \geq 2 \} + \beta_2 I\{t \geq 3 \} + \dots + \beta_{n-1} I\{t \ge n \} + \epsilon_t
\end{equation*}
This model is slightly different from the one used in class. It has indicators instead of ReLUs. This model is more appropriate in this problem because of the change point structure.

This model can be written as $y = X \beta + \epsilon$ where
\begin{equation*}
   X = \begin{pmatrix} 1 & 0 & 0 & \cdot & \cdot & \cdot & 0 \\
   1 & 1 & 0 & \cdot & \cdot & \cdot & 0 \\
   1 & 1 & 1 & \cdot & \cdot & \cdot & 0 \\
   \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
   \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
   \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
   1 & 1 & 1 & \cdot & \cdot & \cdot & 1
    \end{pmatrix}
\end{equation*}

```python

---

[← Generate the function values](03-generate-the-function-values.md) · [Up: contents](index.md) · [It is very easy to create the above matrix in python →](05-it-is-very-easy-to-create-the-above-matrix-in-python.md)
