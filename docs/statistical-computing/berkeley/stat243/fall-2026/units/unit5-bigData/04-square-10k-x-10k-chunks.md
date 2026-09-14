---
title: square 10k x 10k chunks
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit5-bigData.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit5-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# square 10k x 10k chunks

**Source:** [`units/unit5-bigData.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit5-bigData.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

mycalc = da.mean(x, axis = 1)  # by row
import time
t0 = time.time()
rs = mycalc.compute()
time.time() - t0  # 41 sec.
```


For a row-based operation, we would presumably only want to chunk things
up by row, but this doesn't seem to actually make a difference,
presumably because the mean calculation can be done in pieces and only a
small number of summary statistics moved between workers.

```python
#| eval: false
import dask
dask.config.set(scheduler='threads', num_workers = 4)
import dask.array as da

---

[← 2. MapReduce and Dask](03-2-mapreduce-and-dask.md) · [Up: contents](index.md) · [x = da.fromarray(x, chunks=(2500, 40000)) # How to adjust chunk size of existing array. →](05-x-da-fromarray-x-chunks-2500-40000-how-to-adjust-chunk-size.md)
