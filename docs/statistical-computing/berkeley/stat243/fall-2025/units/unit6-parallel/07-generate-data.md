---
title: Generate data
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Generate data

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

n = 1000
p = 50
X = pd.DataFrame(np.random.normal(size = (n, p)),\
                 columns=[f"X{i}" for i in range(1, p + 1)])
Y = X['X1'] + np.sqrt(np.abs(X['X2'] * X['X3'])) +\
    X['X2'] - X['X3'] + np.random.normal(size = n)

n_folds = 10
seq = np.arange(n_folds)
folds = np.random.permutation(np.repeat(seq, 100))
```

To do a parallel map, we need to use the distributed scheduler, but it's
fine to do that with multiple cores on a single machine (such as a
laptop).


```python
n_cores = 2
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers = n_cores)
c = Client(cluster)

tasks = c.map(cv_fit, range(n_folds))
results = c.gather(tasks)

---

[← 5. Illustrating the principles in specific case studies](06-5-illustrating-the-principles-in-specific-case-studies.md) · [Up: contents](index.md) · [We'd need to sort the results appropriately to align them with the observations. →](08-we-d-need-to-sort-the-results-appropriately-to-align-them-wi.md)
