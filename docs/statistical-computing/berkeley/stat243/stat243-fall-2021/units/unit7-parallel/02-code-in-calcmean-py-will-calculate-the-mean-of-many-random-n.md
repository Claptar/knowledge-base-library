---
title: code in calcmean.py will calculate the mean of many random numbers from calcmean
  import
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit7-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit7-parallel.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# code in calcmean.py will calculate the mean of many random numbers from calcmean import

**Source:** [`units/unit7-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit7-parallel.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

p = 20 n = 100000000 # must be of type integer # set up and execute the parallel map inputs = [(i, n) for i in range(p)] # execute the function across the array of input values future = c.map(calc_mean_vargs, inputs) results = c.gather(future) results

22

The map operation appears to cache results. If you rerun the above with the same inputs, you get the same result back essentially instantaneously. HOWEVER, that means that if there is randomness in the results of your function for a given input, Dask will just continue to return the original output.

### **7.3 Futures / delayed evaluation**

The analog of using _future()_ in R to delay/parallelize tasks is shown here. We use _delayed_ to indicate the tasks and then to actually evaluate the code we need to run _compute_ . This is another example of lazy evaluation.

---

[← Unit 7: Parallel Processing](01-unit-7-parallel-processing.md) · [Up: contents](index.md) · [code in calcmean.py will calculate the mean of many random numbers from calcmean import →](03-code-in-calcmean-py-will-calculate-the-mean-of-many-random-n.md)
