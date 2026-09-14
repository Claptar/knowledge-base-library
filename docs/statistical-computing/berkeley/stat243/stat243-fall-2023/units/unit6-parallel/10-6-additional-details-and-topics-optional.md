---
title: 6. Additional details and topics (optional)
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit6-parallel.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Additional details and topics (optional)

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit6-parallel.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

## Avoiding repeated calculations by calling compute once

As far as I can tell, Dask avoids keeping all the pieces of a distributed object or computation in memory. However, in many cases this can mean repeating computations or re-reading data if you need to do multiple operations on a dataset.

For example, if you are create a Dask distributed dataset from data on disk, I think this means that every distinct set of computations (each computational graph) will involve reading the data from disk again.

One implication is that if you can include all computations on a large dataset within a single computational graph (i.e., a call to compute) that may be much more efficient than making separate calls.

Here’s an example with Dask dataframe on some air traffic delay data, where we make sure to do all our computations as part of one graph:

```python
#| eval: false
import dask
dask.config.set(scheduler='processes', num_workers = 6)
import dask.dataframe as ddf
air = ddf.read_csv('/scratch/users/paciorek/243/AirlineData/csvs/*.csv.bz2',
      compression = 'bz2',
      encoding = 'latin1',   # (unexpected) latin1 value(s) 2001 file TailNum field
      dtype = {'Distance': 'float64', 'CRSElapsedTime': 'float64',
      'TailNum': 'object', 'CancellationCode': 'object'})

---

[← First host is the scheduler.](09-first-host-is-the-scheduler.md) · [Up: contents](index.md) · [specify dtypes so Pandas doesn't complain about column type heterogeneity →](11-specify-dtypes-so-pandas-doesn-t-complain-about-column-type.md)
