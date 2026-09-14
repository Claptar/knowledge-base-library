---
title: x.fromhex x.isinteger
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python.md
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/06/python.md
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# x.fromhex x.isinteger

**Source:** [`sections/06/python.md`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python.md) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.md` (lossless)

```

Which of those are attributes/metadata ('member data') and which are methods ('member functions')? If it's a method, say `foo`, you can run the method as `x.foo()`. If it's member data, you can see its value with `x.foo`.


Tuples
------

Tuples are immutable sequences of (zero or more) objects. Functions in
Python often return tuples.

``` {.sourceCode .python}
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
----

Lists are mutable sequences of (zero or more) objects.

``` {.sourceCode .python}
dice = [1, 2, 3, 4, 5, 6]
dice.extend([7,8])

dice.insert(3, 100)
```

Indexing (also called 'slicing') in Python starts at 0 and ends at the length of the object minus 1.

``` {.sourceCode .python}
dice = [1, 2, 3, 4, 5, 6]
dice[0]
dice[1]
dice[6]
```

One can also use sequences. Figure out what is going on here:

``` {.sourceCode .python}
dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dice[1::2]
dice[1:4:2]

dice[1::2] = dice[::2]

dice
```

**Exercises**

- What do you get if you multiply a list of numbers by a number? We'll need to use numpy if we want this to behave like we might expect based on R.
- What does the following tell you about copying and use of memory in Python?
``` {.sourceCode .python}
a = [1, 3, 5]
b = a
id(a)
id(b)

---

[← x.conjugate x.imag](05-x-conjugate-x-imag.md) · [Up: contents](index.md) · [this should confirm what you might suspect →](07-this-should-confirm-what-you-might-suspect.md)
