---
title: numpy, scipy, and importing packages
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/Intro
  to python for R users.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/Intro to python
  for R users.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# numpy, scipy, and importing packages

**Source:** [`section/s06/Intro to python for R users.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/Intro to python for R users.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

Python doesn't normally do vectorization, but there are packages that can do vectorization. One such package is numpy. Python also doesn't normally do statistics, but the package scipy does a lot of basic stuff (distributions, extensions on random samples, etc.).

To import packages in python, you can use the `import` keyword:

```python
import numpy
```

Unlike R, python will not bring package 'numpy' into the global namespace, but rather into the namespace 'numpy'. That means that to use the numpy log function, you would need to prefix it with 'numpy.':

```python
numpy.log([3, 1, 10])
```

```
array([ 1.09861229,  0.        ,  2.30258509])
```

Alternatively, python allows you to alias a namespace using the `as` keyword

```python
import numpy as np
np.log([3, 1, 10])
```

```
array([ 1.09861229,  0.        ,  2.30258509])
```

You can also use the keyword `from` to import only a few functions directly into the global namespace

```python
from math import log, exp
log(3)
```

```
1.0986122886681098
```

All vectorized operations in numpy are on `array` objects. They are very similar to lists, except they are more efficient because they cannot be shrunk or grown. You can create one by either specifying the dimensions (into the function `zeros`), or passing in a list (`array`):

```python
arr_1 = np.array([1, 15, 9])
arr_1
```

```
array([ 1, 15,  9])
```

```python
arr_2 = np.zeros(10)
arr_2
```

```
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
```

You can also make an n-dimensional arrays using the function `ndarray` (this is how you would make a matrix). Notice that the matrix is setup row-wise rather than column-wise in R.

```python
np.ndarray((3, 2))
```

```
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])
```

Unlike lists, every single element must be of the same data type (like vectors or matrices in R). You can specify the data type as an optional second argument. If you do not, numpy tries to infer it. Note that this might not be correct:

```python
arr_1.dtype
```

```
dtype('int64')
```

```python
arr_2.dtype
```

```
dtype('float64')
```

```python
arr_3 = np.array([1.0, 15, 9], dtype = np.int32)
arr_3.dtype
```

```
dtype('int32')
```

### vectorization

Numpy allows you to do vectorization as you would in R. For example, we can take the log of a series of numbers and multiply them:

```python
all_x = np.array(range(1, 11))
np.log(all_x) * 5.0
```

```
array([  0.        ,   3.4657359 ,   5.49306144,   6.93147181,
         8.04718956,   8.95879735,   9.72955075,  10.39720771,
        10.98612289,  11.51292546])
```

Note that log function called here is different than the function from the package `math`.

```python
log(all_x) * 5.0
```

You can make any function that accepts primitive data types vectorized using the numpy function `np.vectorize`:

```python
def my_abs(x):
    if x >= 0:
        return x
    return -x
```

```python
test_list = [1, -1, 0, -30, 100]

v_my_abs = np.vectorize(my_abs)
v_my_abs(test_list)
```

```
array([  1,   1,   0,  30, 100])
```

```python
np.sum(v_my_abs(test_list))
```

```
132
```

You can also use the map reduce paradigm without using numpy.

The function `map` is very similar to `lapply`. It takes a function and a variable length number of lists and applies the function to all of the lists.

```python
map(my_abs, test_list)
```

```
[1, 1, 0, 30, 100]
```

You can then aggregate things using `reduce`:

```python
all_abs = map(my_abs, test_list)
all_abs
```

```
[1, 1, 0, 30, 100]
```

```python
reduce(lambda x, y: x + y, all_abs, 0)
```

```
132
```

Of course, we could have also use the built-in function `sum`

```python
sum(all_abs)
```

```
132
```

---

[← Intro to python for R users](01-intro-to-python-for-r-users.md) · [Up: contents](index.md) · [problem 1 →](03-problem-1.md)
