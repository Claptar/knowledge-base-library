---
title: SVD
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/06/python_intro.ipynb
licence: CC0-1.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# SVD

**Source:** [`sections/06/python_intro.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.ipynb` (lossless)

np.linalg.svd(x)
```

```python
e = np.linalg.eig(x)
e[0]
```

```python
e[1][:, 0]
```

Creating a sequence in numpy

```python
np.linspace(0, 1, 5)
```

Randomly sample from normal distribution

```python
np.random.seed(0)
x = np.random.normal(size = 10)
```

```python
pos = x > 0
pos
```

```python
y = x[pos]
y
```

```python
x[[1, 3, 4]]
```

```python
x[pos] = 0
```

```python
np.cos(x)
```

Some scipy routines

```python
import scipy.stats as st
print(st.norm.cdf(1.96, 0, 1))
print(st.norm.cdf(1.96, 0.5, 2))
print(st.norm(0.5, 2).cdf(1.96))
```

### Excercise
- See what happens if you try to create a numpy array with a mix of numbers and character strings.

- Try to add a vector to a matrix; how does this compare to R?

## Pandas

```python
import pandas as pd
dat = pd.read_csv('gapminder.csv')
dat.head()
```

```python
dat.columns
```

```python
dat['year']
```

```python
dat.year
```

```python
dat[0:5]
```

```python
dat.sort_values(['year', 'country'])
```

```python
dat.loc[0:5, ['year', 'country']]
```

```python
dat[dat.year == 1952]
```

```python
ndat = dat[['pop','lifeExp','gdpPercap']]
ndat.apply(lambda col: col.max() - col.min())
```

```python
dat2007 = dat[dat.year == 2007].copy()
dat2007.groupby('continent', as_index=False).mean()
```

```python
def stdize(vals):
    return((vals - vals.mean()) / vals.std())

dat2007['lifeExpZ'] = dat2007.groupby('continent')['lifeExp'].transform(stdize)
dat2007
```

### Exercise
- Use *pd.merge()* to merge the continent means for life expectancy for 2007 back into the original dat2007 dataFrame.

## Classes

```python
class Rectangle(object):
    dim = 2  # class variable
    counter = 0
    def __init__(self, height, width):
        self.height = height  # instance variable
        self.width = width    # instance variable
        self.set_diagonal()
        Rectangle.counter += 1
    def __repr__(self):
        return("{0} by {1} rectangle".format(self.height, self.width))
    def area(self, verbose = False):
        if verbose:
            print('Computing the area... ')
        return(self.height*self.width)
    def set_diagonal(self):
        self.diagonal = pow(self.height**2 + self.width**2, 0.5)

x = Rectangle(10, 5)
x
```

```python
print(x.dim)
x.dim = 'foo'
print(x.dim) # hmmm
```

```python
x.area()
```

```python
Rectangle.area(x)
```

```python
y = Rectangle(4, 8)
print(y.counter)
print(x.counter)
```

## Strings

```python
import string
print(string.digits)
print(string.digits[1])
print(string.digits[-1])
```

### Slicing

```python
string.digits[1:5]
```

```python
string.digits[1:5:2]
```

```python
string.digits[1::2]
```

```python
string.digits[:5:-1]
```

```python
string.digits[1:5:-1]
```

```python
string.digits[-3:-7:-1]
```

### Subsequence testing

```python
string1 = "my string"
```

Look at string1. followed by a tab to see what methods are available.

```python
string1.upper()
```

```python
string1 + "is your string"
```

```python
"*" * 10
```

```python
string1[3:]
```

```python
string1[3:4]
```

```python
string1[4::2]
```

```python

---

[← transpose](23-transpose.md) · [Up: contents](index.md) · [does not work →](25-does-not-work.md)
