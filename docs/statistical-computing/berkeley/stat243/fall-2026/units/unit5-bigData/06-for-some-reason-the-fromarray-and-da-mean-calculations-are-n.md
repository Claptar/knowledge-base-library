---
title: For some reason the fromarray and da.mean calculations are not done lazily
  here.
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit5-bigData.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit5-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# For some reason the fromarray and da.mean calculations are not done lazily here.

**Source:** [`units/unit5-bigData.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit5-bigData.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

t0 = time.time()
dx = da.from_array(x, chunks=(2500, 40000))
time.time() - t0   # 27 sec.
t0 = time.time()
mycalc = da.mean(x, axis = 1)  # What is this doing given .compute() also takes time?
time.time() - t0   # 28 sec.
t0 = time.time()
rs = mycalc.compute()
time.time() - t0   # 21 sec.
```


Dask will avoid storing all the chunks in memory. (It appears to just
generate them on the fly.) Here we have an 80 GB array, but we never use
more than a few GB of memory (based on `top` or `free -h`).

```python
#| eval: false
import dask
dask.config.set(scheduler='threads', num_workers = 4)
import dask.array as da
x = da.random.normal(0, 1, size=(100000,100000), chunks=(10000, 10000))
mycalc = da.mean(x, axis = 1)  # row means
import time
t0 = time.time()
rs = mycalc.compute()
time.time() - t0   # 205 sec.
rs[0:5]
```


#### Distributed arrays

Using arrays distributed across multiple machines should be straightforward based on using *Dask distributed*. However,
one would want to be careful about creating arrays by distributing the
data from a single Python process as that would involve copying between
machines.

---

[← x = da.fromarray(x, chunks=(2500, 40000)) # How to adjust chunk size of existing array.](05-x-da-fromarray-x-chunks-2500-40000-how-to-adjust-chunk-size.md) · [Up: contents](index.md) · [3. Databases →](07-3-databases.md)
