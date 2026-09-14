---
title: x.fromhex x.isinteger
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/python_intro.md
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/07/python_intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# x.fromhex x.isinteger

**Source:** [`labs/07/python_intro.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/python_intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

```

Which of those are attributes/metadata ('member data') and which are methods ('member functions')? If it's a method, say `foo`, you can run the method as `x.foo()`. If it's member data, you can see its value with `x.foo`.


Tuples

Tuples are immutable sequences of (zero or more) objects. Functions in
Python often return tuples.

```python
x = 1; y = 'foo'

xy = (x, y)
type(xy)
xy = x,y
type(xy)

xy
xy[1]

xy[1] = 3

a,b = x,y
a
b
```

**Exercises**

- Create the following: `x=5` and `y=6`. Now swap their values using a single line of code. (How would you do this in R?)
- What happens when you multiply a tuple by a number? how is this different than similar syntax in R?
- What's nice about using immutable objects in your code?

Lists

Lists are mutable sequences of (zero or more) objects.

```python
dice = [1, 2, 3, 4, 5, 6]
dice.extend([7,8])

dice.insert(3, 100)
```

Indexing (also called 'slicing') in Python starts at 0 and ends at the length of the object minus 1.

```python
dice = [1, 2, 3, 4, 5, 6]
dice[0]
dice[1]
dice[6]
```

One can also use sequences. Figure out what is going on here:

```python
dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dice[1::2]
dice[1:4:2]

dice[1::2] = dice[::2]

dice
```

**Exercises**

- What do you get if you multiply a list of numbers by a number? We'll need to use numpy if we want this to behave like we might expect based on R.
- What does the following tell you about copying and use of memory in Python?
```python
a = [1, 3, 5]
b = a
id(a)
id(b)

---

[← x.conjugate x.imag](06-x-conjugate-x-imag.md) · [Up: contents](index.md) · [this should confirm what you might suspect →](08-this-should-confirm-what-you-might-suspect.md)
