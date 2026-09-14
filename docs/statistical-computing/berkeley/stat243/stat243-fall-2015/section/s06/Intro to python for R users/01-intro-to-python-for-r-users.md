---
title: Intro to python for R users
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/Intro
  to python for R users.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/Intro to python
  for R users.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Intro to python for R users

**Source:** [`section/s06/Intro to python for R users.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/Intro to python for R users.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

You will find that python and R have a number of similarities, but python has a bit more general-purpose tooling.

## indentation and "blocks"

Unlike in R, blocks are defined by whitespace. By indenting with a tab, you are essentially adding a `{}` as you would in R. For example, this is an if else in python:

```python
value = 3
if value < 100:
    print 'value is less than 100'
else:
    print 'value is greater than 100'
```

```
value is less than 100
```

Instead of using the symbols `&` and `|`, python uses the keywords `and` and `or`:

```python
True or False
```

```
True
```

```python
True and False
```

```
False
```

```python
not False
```

```
True
```

## primitives and datatypes

Like R, python is dynamically typed and thus datatypes are inferred at runtime. Python also has

```python
x = 3
print x
type(x)
```

```
3
int
```

```python
type(3.14)
```

```
float
```

```python
type('this is string')
```

```
str
```

## containers

Python also has container data structures similar to R. You can create a list and using either `[]` or `list()`:

```python
a_list = []
a_list.append(3)
a_list.append(7)
a_list
```

```
[3, 7]
```

Lists can only be indexed using integers and indices start at 0 not 1 (unlike R lists). Like R lists, they can contain mixed data types:

```python
a_list.append('adding a string')
a_list
```

```
[3, 7, 'adding a string']
```

```python
a_list[0]
```

```
3
```

```python
a_list[2]
```

```
'adding a string'
```

You can also check if a value is inside of a list by using the keyword `in`:

```python
7 in a_list
```

```
True
```

```python
0 in a_list
```

```
False
```

I generally do not recommend this as the run time is linear in the size of the list. If you find yourself doing this type of a lookup often, you might want to use a dictionary instead (below).

To get behavior similar to named lists in R, you have to use a different data structure called a dictionary. A dictionary is essentially a hash table. You can create a new dictionary using `{}` or `dict()`.

```python
a_dict = {}
a_dict['name 1'] = 3
a_dict[3] = 0
a_dict
```

```
{3: 0, 'name 1': 3}
```

For every entry in a dictionary, there is a "key" (analogous to the name in R) and a "value". Notice that we can use integers or strings as keys. The keys above are `3` and `'name 1'` with values 0 and 3, respectively.

You can also use the keyword `in`, but it is much more efficient here, as the lookup is constant time

```python
3 in a_dict
```

```
True
```

```python
0 in a_dict
```

```
False
```

## loops

The most common loop in python is a for loop. They work very similarly as they do in R. The function `range` (python) is very similar to the function `seq` (R), but keep in mind that indexing starts at 0 and the end is exclusive (is not included).

```python
some_numbers = range(10)
for x in some_numbers:
    if x % 2 == 0:
        print x, 'is even'
```

```
0 is even
2 is even
4 is even
6 is even
8 is even
```

## functions

```python
def is_even(x):
    return x % 2 == 0
```

```python
is_even(3)
```

```
False
```

```python
is_even(10)
```

```
True
```

---

[Up: contents](index.md) · [numpy, scipy, and importing packages →](02-numpy-scipy-and-importing-packages.md)
