---
title: 'x = da.fromarray(x, chunks=(2500, 40000)) # How to adjust chunk size of existing
  array.'
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit7-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# x = da.fromarray(x, chunks=(2500, 40000)) # How to adjust chunk size of existing array.

**Source:** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit7-bigData.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

x = da.random.normal(0, 1, size=(40000,40000), chunks=(2500, 40000))
mycalc = da.mean(x, axis = 1)  # row means
import time
t0 = time.time()
rs = mycalc.compute()
time.time() - t0   # 42 sec.
```


Of course, given the lazy evaluation, this timing comparison is not just
timing the actual row mean calculations.

But this doesn't really clarify the story...

```python
#| eval: false
import dask
dask.config.set(scheduler='threads', num_workers = 4)
import dask.array as da
import numpy as np
import time
t0 = time.time()
x = np.random.normal(0, 1, size=(40000,40000))
time.time() - t0   # 110 sec.

---

[← square 10k x 10k chunks](04-square-10k-x-10k-chunks.md) · [Up: contents](index.md) · [For some reason the fromarray and da.mean calculations are not done lazily here. →](06-for-some-reason-the-fromarray-and-da-mean-calculations-are-n.md)
