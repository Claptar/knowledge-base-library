---
title: Plot the fitted values for the different posterior draws
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the fitted values for the different posterior draws

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

x = np.arange(1, n + 1)
plt.figure(figsize = (15, 6))
plt.plot(y)

for i in range(N):
    c = cpostsamples[i]
    b0 = post_samples[i, 1]
    b1 = post_samples[i, 2]
    b2 = post_samples[i, 3]

    ftdval = b0 + b1 * x + b2 * ((x > c).astype(float)) * (x - c)

    plt.plot(ftdval, color = 'red')
plt.plot(y, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Summary of the posterior samples:
pd.DataFrame(post_samples).describe()
```

```
0              1            2            3            4
count  2000.000000    2000.000000  2000.000000  2000.000000  2000.000000
mean    297.426500  178341.563897   191.135089    32.379440  2221.533224
std       9.176748     236.325641     1.082882     1.523587    56.259513
min     262.000000  177418.875703   187.952460    27.840629  2029.175952
25%     291.000000  178179.981065   190.371263    31.358716  2182.856960
50%     297.000000  178349.875769   191.128412    32.388153  2219.748677
75%     304.000000  178505.520157   191.874330    33.446580  2260.256411
max     323.000000  179087.623121   194.646661    37.195418  2429.107218
```

---

[← Let us plot the posterior samples for c on the original plot](23-let-us-plot-the-posterior-samples-for-c-on-the-original-plot.md) · [Up: contents](index.md)
