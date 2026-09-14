---
title: code in calcmean.py will calculate the mean of many random numbers from calcmean
  import
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit7-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit7-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# code in calcmean.py will calculate the mean of many random numbers from calcmean import

**Source:** [`units/unit7-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit7-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

p = 20 n = 100000000 # must be of type integer # set up and execute the parallel map inputs = [(i, n) for i in range(p)] # execute the function across the array of input values future = c.map(calc_mean_vargs, inputs) results = c.gather(future) results

The map operation appears to cache results. If you rerun the above with the same inputs, you get the same result back essentially instantaneously. HOWEVER, that means that if there is randomness in the results of your function for a given input, Dask will just continue to return the original output.

### **7.3 Futures / delayed evaluation**

The analog of using _future()_ in R to delay/parallelize tasks is shown here. We use _delayed_ to indicate the tasks and then to actually evaluate the code we need to run _compute_ . This is another example of lazy evaluation.

22

---

[← Unit 7: Parallel Processing](01-unit-7-parallel-processing.md) · [Up: contents](index.md) · [code in calcmean.py will calculate the mean of many random numbers from calcmean import →](03-code-in-calcmean-py-will-calculate-the-mean-of-many-random-n.md)
