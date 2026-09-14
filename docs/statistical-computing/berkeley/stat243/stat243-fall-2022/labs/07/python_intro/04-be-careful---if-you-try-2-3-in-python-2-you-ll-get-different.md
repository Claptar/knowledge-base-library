---
title: be careful - if you try 2/3 in Python 2, you'll get different behavior.
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/python_intro.md
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/07/python_intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# be careful - if you try 2/3 in Python 2, you'll get different behavior.

**Source:** [`labs/07/python_intro.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/python_intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

x = 1.1
type(x)

x * 2
x ** 2

(type(1), type(1.1), type(1+2j))
y = 1+2j
```


We can apply various functions to numbers, as expected.
```python
import math
math.cos(0)
math.cos(math.pi)
```

The *math* package in the standard library includes many additional
numerical operations.

If you type the name of a module or package followed by period (.) and tab
you should see the objects and functions in that module/package.

```python
math.
```

```
math.acos       math.degrees    math.fsum       math.pi
math.acosh      math.e          math.gamma      math.pow
math.asin       math.erf        math.hypot      math.radians
math.asinh      math.erfc       math.isinf      math.sin
math.atan       math.exp        math.isnan      math.sinh
math.atan2      math.expm1      math.ldexp      math.sqrt
math.atanh      math.fabs       math.lgamma     math.tan
math.ceil       math.factorial  math.log        math.tanh
math.copysign   math.floor      math.log10      math.trunc
math.cos        math.fmod       math.log1p
math.cosh       math.frexp      math.modf
```


**Exercises**

- Using the section on "Built-in Types" from the [official "The Python
Standard Library" reference](https://docs.python.org/3/library/index.html), figure out how to compute:
    1.  $(\lceil \frac{3}{4} \rceil \times 4)^3$,
    and
    2.  $\sqrt{-1}$.


Objects and object-oriented programming

We'll talk about this in more detail later, but it's worth mentioning here that Python is an object-oriented language.  What this means is that variables in Python are objects that are instances of a class.

Objects have methods that can be used on them and attributes (member data) that are part of the object. All objects in a class have the same methods and same member data 'slots', but different objects will have different values in those slots.

Note that even the basic numeric structures behave like objects. We can use tab completion to see what methods are available for an object and what member data are part of an object.

```python
x = 3.0
type(x)
x.

---

[← Introduction](03-introduction.md) · [Up: contents](index.md) · [x.asintegerratio x.hex x.real →](05-x-asintegerratio-x-hex-x-real.md)
