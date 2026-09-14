---
title: this is how to use numpy
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/06/python_intro.ipynb
licence: CC0-1.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# this is how to use numpy

**Source:** [`sections/06/python_intro.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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
