---
title: of the signals change over time? How does this differ from white noise?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# of the signals change over time? How does this differ from white noise?

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

nwalks = 100
nt=5000
all_r = np.zeros((nt, nwalks))
for n in np.arange(nwalks):
    all_r[:,n]=random_walk(nt)
    plt.plot(all_r[:,n])
    plt.xlabel('Time')

plt.figure()
plt.plot(all_r.mean(1))
plt.ylabel('Mean')
plt.figure()
plt.plot(all_r.var(1))
plt.ylabel('Variance')
```

```
Text(0, 0.5, 'Variance')
```

*(3 figures omitted — see the original notebook.)*

---

[← What do you see about how the mean and variance](19-what-do-you-see-about-how-the-mean-and-variance.md) · [Up: contents](index.md) · [Random Walk with Drift →](21-random-walk-with-drift.md)
