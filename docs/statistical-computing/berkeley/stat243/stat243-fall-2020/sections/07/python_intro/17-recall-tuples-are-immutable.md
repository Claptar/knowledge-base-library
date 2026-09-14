---
title: recall tuples are immutable
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/07/python_intro.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/07/python_intro.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# recall tuples are immutable

**Source:** [`sections/07/python_intro.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/07/python_intro.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

xy[1] = 3
```

```python
a, b = x, y
print(a)
print(b)
type(a)
```

### Exercises
- Store x = 5 and y = 6.  Swap their values in a single line of code.  (How would you do this in R?)

```python
x = 5
y = 6
y, x = x, y
print(x, y)
```

- What happens when you multiple a tuple by a number? How is this different than similar syntax in R?

- What's nice about using immutable objects?

## Lists

```python
dice = [1, 2, 3, 4, 5, 6]
print("original list:", dice)

---

[← another way to do it](16-another-way-to-do-it.md) · [Up: contents](index.md) · [extend →](18-extend.md)
