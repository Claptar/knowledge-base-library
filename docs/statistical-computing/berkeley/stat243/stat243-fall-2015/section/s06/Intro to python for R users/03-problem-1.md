---
title: problem 1
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/Intro
  to python for R users.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/Intro to python
  for R users.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# problem 1

**Source:** [`section/s06/Intro to python for R users.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/Intro to python for R users.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

We are going to implement an efficient version of the function `table()` from R using dictionaries and functions. Write a function that takes 2 arguments: `value`, and `counter`. The variable counter will be a dictionary that keeps track of the pair (value, count). The signature will look something like this:

```python
def table(a_list):
    counter = {}
    for value in a_list:
        add_occurrence(value, counter)

    return counter
```

```python
def add_occurrence(value, counter):
    # add in code here
    pass
```

---

[← numpy, scipy, and importing packages](02-numpy-scipy-and-importing-packages.md) · [Up: contents](index.md) · [problem 2 →](04-problem-2.md)
