---
title: update a
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/06/python_intro.ipynb
licence: CC0-1.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# update a

**Source:** [`sections/06/python_intro.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.ipynb` (lossless)

a[1] = 5
print("address of updated a:", id(a))
```

## Dictionaries

```python
students = {"Jarrod Millman": ['A', 'B+', 'A-'],
            "Thomas Kluyver": ['A-', 'A-'],
            "Stefan van der Wait": 'and now for something completely different.'
           }
students
```

```python
students.keys()
```

```python
students.values()
```

```python
students["Jarrod Millman"]
```

```python
students["Jarrod Millman"][1]
```

Try typing students. followed by a tab to see what methods are available for dictionaries

```python
students.
```

## Control flow

```python
x = 2
if(x >= 4):
    print("a is big")
    if(a == 4):
        print("a is small")
else:
    print("a is small")
```

```python
if(x >= 4):
    print("a is big")
    if(a == 4):
        print("a is small")
    else:
        print("a is small")
```

### For loops and list comprehension

```python
for x in [1, 2, 3, 4]:
    print(x)
```

```python
for x in [1, 2, 3, 4]:
    y = x * 2
    print(y, end = " ")
```

```python
for x in range(30):
    print(x)
    y = x
```

```python
print(y)
```

```python
y = [x for x in range(4)]
y
```

List comprehension

```python
vals = [-4, 3, -1, 2.5, 7]
[x for x in vals if x > 0]
```

### Exercises
- See what [1, 2, 3] + 3 returns. Try to explain what happened and why.

- Use list comprehension to perform element-wise addition of a scalar to a list of scalars

## Functions

```python
def add(x, y = 1, absol = False):
    if absol:
        return(abs(x + y))
    else:
        return(x + y)
```

```python
add(3)
```

```python
add(3, 5)
```

```python
add(3, absol = True, y = 5)
```

```python
add(y = -5, x = 3)
```

```python
add(y = -5, 3)
```

### Excercise
- Define a function that will take the square root of a number of will (if requested by the user) set the square root of a negative number to 0.

## Math and statistics: NumPy and SciPy

```python
z = [0, 1, 2]
```

```python
y = np.array(z)
y
```

```python
y.dtype
```

```python
x = np.array([[1, 2], [3, 4]], dtype = np.float64)

---

[← insert](19-insert.md) · [Up: contents](index.md) · [element-wise multiplication →](21-element-wise-multiplication.md)
