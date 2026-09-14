---
title: 'x = da.fromarray(x, chunks=(2500, 40000)) # adjust chunk size of existing
  array'
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# x = da.fromarray(x, chunks=(2500, 40000)) # adjust chunk size of existing array

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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
import dask
dask.config.set(scheduler='threads', num_workers = 4)
import dask.array as da
import numpy as np
import time
t0 = time.time()
x = np.random.normal(0, 1, size=(40000,40000))
time.time() - t0   # 110 sec.

---

[← square 10k x 10k chunks](05-square-10k-x-10k-chunks.md) · [Up: contents](index.md) · [for some reason the fromarray and da.mean calculations are not done lazily here →](07-for-some-reason-the-fromarray-and-da-mean-calculations-are-n.md)
