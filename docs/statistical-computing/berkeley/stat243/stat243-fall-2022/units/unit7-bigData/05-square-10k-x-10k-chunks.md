---
title: square 10k x 10k chunks
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# square 10k x 10k chunks

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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
import dask
dask.config.set(scheduler='threads', num_workers = 4)
import dask.array as da

---

[← specify dtypes so Pandas doesn't complain about column type heterogeneity](04-specify-dtypes-so-pandas-doesn-t-complain-about-column-type.md) · [Up: contents](index.md) · [x = da.fromarray(x, chunks=(2500, 40000)) # adjust chunk size of existing array →](06-x-da-fromarray-x-chunks-2500-40000-adjust-chunk-size-of-exis.md)
