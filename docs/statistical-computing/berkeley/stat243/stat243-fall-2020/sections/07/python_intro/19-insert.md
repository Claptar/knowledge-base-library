---
title: insert
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/07/python_intro.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/07/python_intro.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# insert

**Source:** [`sections/07/python_intro.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/07/python_intro.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

dice.insert(3, 100)
print("inserted list:", dice)
```

```python
dice.
```

Indexing a list

```python
dice = [1, 2, 3, 4, 5, 6]
print("first entry", dice[0])
print("second entry", dice[1])
```

The 6th index does not exist

```python
dice[6]
```

Using sequencing

```python
dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dice[0::3]
```

```python
dice[1:4:2]
```

```python
dice[1::2] = dice[::2]
dice
```

### Exercises
- What do you get if you multiply a list of numbers by a number?

- What does the following tell you about copying and memory use in Python?

```python
a = [1, 3, 5]
b = a
print("address of a:", id(a))
print("address of a:", id(b))

---

[← extend](18-extend.md) · [Up: contents](index.md) · [update a →](20-update-a.md)
