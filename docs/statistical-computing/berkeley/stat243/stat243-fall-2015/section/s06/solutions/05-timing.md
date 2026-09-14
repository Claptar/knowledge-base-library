---
title: timing
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/solutions.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/solutions.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# timing

**Source:** [`section/s06/solutions.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/solutions.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

```python
%timeit -n 100 norm_const_slow(1000, 0.3, 0.5)
```

```
100 loops, best of 3: 5.42 ms per loop
```

```python
%timeit -n 100 norm_const_fast(1000, 0.3, 0.5)
```

```
100 loops, best of 3: 3.87 ms per loop
/Users/hjp/.virtualenvs/py2/lib/python2.7/site-packages/ipykernel/__main__.py:4: RuntimeWarning: divide by zero encountered in log
/Users/hjp/.virtualenvs/py2/lib/python2.7/site-packages/ipykernel/__main__.py:4: RuntimeWarning: invalid value encountered in multiply
/Users/hjp/.virtualenvs/py2/lib/python2.7/site-packages/ipykernel/__main__.py:7: RuntimeWarning: divide by zero encountered in log
/Users/hjp/.virtualenvs/py2/lib/python2.7/site-packages/ipykernel/__main__.py:7: RuntimeWarning: invalid value encountered in multiply
```

```python
norm_const_slow(1000, 0.3, 0.5)
```

```
1.4146589755263277
```

```python
norm_const_fast(1000, 0.3, 0.5)
```

```
/Users/hjp/.virtualenvs/py2/lib/python2.7/site-packages/ipykernel/__main__.py:4: RuntimeWarning: divide by zero encountered in log
/Users/hjp/.virtualenvs/py2/lib/python2.7/site-packages/ipykernel/__main__.py:4: RuntimeWarning: invalid value encountered in multiply
/Users/hjp/.virtualenvs/py2/lib/python2.7/site-packages/ipykernel/__main__.py:7: RuntimeWarning: divide by zero encountered in log
/Users/hjp/.virtualenvs/py2/lib/python2.7/site-packages/ipykernel/__main__.py:7: RuntimeWarning: invalid value encountered in multiply
1.4146589755263277
```

---

[← using vectorization](04-using-vectorization.md) · [Up: contents](index.md)
