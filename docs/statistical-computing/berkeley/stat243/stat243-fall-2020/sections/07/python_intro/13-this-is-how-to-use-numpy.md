---
title: this is how to use numpy
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/07/python_intro.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/07/python_intro.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# this is how to use numpy

**Source:** [`sections/07/python_intro.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/07/python_intro.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

np.arctan(1)
```

See documentation

```python
np.ndim?
```

## Decoding error messages
days.py is another python script that is included in the sections/07 folder.  This will show you how error messages look in python.

```python
import days
days.print_friday_message()
```

## Data structures

### Numbers

```python
print(2 * 3)
print(2 / 3)
```

```python
x = 1.1
type(x)
```

```python
print("multiplication:", x * 2)
print("exponentiation:", x ** 2)
```

```python
(type(1), type(1.1), type(1 + 2j))
```

```python

---

[← this will not work because we imported as np](12-this-will-not-work-because-we-imported-as-np.md) · [Up: contents](index.md) · [trying various functions from math package we imported earlier →](14-trying-various-functions-from-math-package-we-imported-earli.md)
