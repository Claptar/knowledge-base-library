---
title: using vectorization
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/solutions.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/solutions.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# using vectorization

**Source:** [`section/s06/solutions.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/solutions.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

Remember to vectorize the choose function:

```python
v_log_choose = np.vectorize(log_choose)
```

```python
def norm_const_fast(n, p, phi):
    all_k = np.array( range(0, n+1) )

    temp1 = all_k*np.log(all_k)
    temp1[0] = 0

    temp2 = (n - all_k)*np.log(n - all_k)
    temp2[n] = 0

    all_choose = v_log_choose(n, all_k)

    return sum(np.exp(all_choose +
                      (1-phi)*(temp1 + temp2 - n*np.log(n)) +
                      (all_k * phi) * np.log(p) +
                      (n - all_k) * (phi * np.log(1-p))
                     )
              )
```

---

[← problem 2](03-problem-2.md) · [Up: contents](index.md) · [timing →](05-timing.md)
