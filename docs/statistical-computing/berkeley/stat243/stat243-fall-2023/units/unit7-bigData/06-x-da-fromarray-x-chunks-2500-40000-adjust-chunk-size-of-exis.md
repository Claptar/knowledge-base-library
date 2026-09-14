---
title: 'x = da.fromarray(x, chunks=(2500, 40000)) # adjust chunk size of existing
  array'
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit7-bigData.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# x = da.fromarray(x, chunks=(2500, 40000)) # adjust chunk size of existing array

**Source:** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit7-bigData.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

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

[← square 10k x 10k chunks](05-square-10k-x-10k-chunks.md) · [Up: contents](index.md) · [for some reason the fromarray and da.mean calculations are not done lazily here →](07-for-some-reason-the-fromarray-and-da-mean-calculations-are-n.md)
