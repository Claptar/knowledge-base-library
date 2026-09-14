---
title: execute the function across the array of input values
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit6-parallel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# execute the function across the array of input values

**Source:** [`units/unit6-parallel.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

future = c.map(calc_mean_vargs, inputs)
results = c.gather(future)
results
```

The map operation appears to cache results. If you rerun the above with
the same inputs, you get the same result back essentially
instantaneously. HOWEVER, that means that if there is randomness in the
results of your function for a given input, Dask will just continue to
return the original output.

## Futures / delayed evaluation

The analog of using `future()` in R to delay/parallelize tasks is shown
here. We use `delayed` to indicate the tasks and then to actually
evaluate the code we need to run `compute`. This is another example of
lazy evaluation.

```python

---

[← set up and execute the parallel map](11-set-up-and-execute-the-parallel-map.md) · [Up: contents](index.md) · [code in calcmean.py will calculate the mean of many random numbers →](13-code-in-calcmean-py-will-calculate-the-mean-of-many-random-n.md)
