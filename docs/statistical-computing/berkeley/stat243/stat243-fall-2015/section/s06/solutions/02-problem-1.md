---
title: problem 1
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/solutions.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/solutions.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# problem 1

**Source:** [`section/s06/solutions.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/solutions.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

The key here (ha) is to remember that dictionaries are mutable. So, in the function below, counter is modified.

```python
def table(a_list):
    counter = {}
    for value in a_list:
        add_occurrence(value, counter)

    return counter
```

```python
def add_occurrence(value, counter):
    if value not in counter:
        counter[value] = 0
    counter[value] += 1
```

```python
tmp = [1, 2, 3, 1, 2, 3, 10]
result = table(tmp)
result.keys()

result.values()
```

```
[2, 2, 2, 1]
```

---

[← solutions to problems](01-solutions-to-problems.md) · [Up: contents](index.md) · [problem 2 →](03-problem-2.md)
