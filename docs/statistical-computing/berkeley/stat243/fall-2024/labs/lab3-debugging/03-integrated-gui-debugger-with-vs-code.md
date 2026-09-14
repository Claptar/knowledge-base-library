---
title: Integrated GUI debugger (with VS Code)
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab3-debugging.qmd
source_file: sources/berkeley-stat243/fall-2024/labs/lab3-debugging.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Integrated GUI debugger (with VS Code)

**Source:** [`labs/lab3-debugging.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab3-debugging.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Today we will experiment with the visual debugging tools integrated with IDEs. We will do that in VS Code (unless you have another IDE with debugger integration). We will load a piece of code, go through it to understand what it does, then try to discover the problem with it and fix it.

Here's a piece of code that implements the binary search algorithm to locate the first occurrence of a number in a list of numbers:

```python
import math
def binary_search(lst, T):
    L = 0
    R = len(lst) - 1
    while L < R:
        m = math.floor((L + R) / 2)
        if lst[m] <= T:
            L = m + 1
        else:
            R = m - 1
    if lst[L] == T:
        return L
    return -1
```

There are a couple of things not quite right with this implementation, even though it will run and produce correct results for some cases.

Here's another piece of code implementing merge sort (also with some bugs in it):

```python
def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    return merge(merge_sort(lst[:n//2]), merge_sort(lst[n//2:]))

def merge(lst1, lst2):
    merged = []
    i, j = 0,0
    while i < len(lst1) and j < len(lst2):
        if i < len(lst1) and j < len(lst2) and lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst1[j])
            j += 1
    while i < len(lst1):
        merged.append(lst1[i])
        i += 1
    while j < len(lst2):
            merged.append(lst2[j])
            j += 1
    return merged

merge_sort([3, 1, 5, 1, 6, 3, 9, 12, 8])
```

You can use this to practice stepping inside functions, and thinking about recursion.

Incidentally, if you first sort, then find, you can get the quantile of a particular value within a collection (you'll need to adjust the binary search a little to achieve this).

Alternatively you could start by implementing (without using any existing functions) a function that inverts the order of the words in a string, and debug it until it works.

Here's a version of this function with a couple of bugs injected, if you prefer to start from there:

```python
def reverse_words(input):
    working = list(input)
    invert(working)
    start = 0
    for i, c in enumerate(working):
        if c == ' ' and i != start:
            invert(working, start, i)
            start = i+1
    return ''.join(working)

def invert(lst, start=None, end=None):
    if None == start:
        start = 0
    if None == end:
        end = len(lst)-1

    while start < end:
        tmp = lst[start]
        lst[start] = lst[start]
        lst[end] = tmp
        start += 1
        end -= 1

reverse_words("These are my words.   I have spoken!")
```

---

[← Advanced debugging](02-advanced-debugging.md) · [Up: contents](index.md) · [Post-mortem debugging →](04-post-mortem-debugging.md)
