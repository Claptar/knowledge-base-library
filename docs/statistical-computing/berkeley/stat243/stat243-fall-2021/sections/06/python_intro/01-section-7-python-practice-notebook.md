---
title: 'Section 7: python practice notebook'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/06/python_intro.ipynb
licence: CC0-1.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Section 7: python practice notebook

**Source:** [`sections/06/python_intro.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.ipynb` (lossless)

In this section we are going through an introduction to python.  The .html file has more details but this notebook will serve as a place to illustrate the code from the html file and do the exercises

Note, to run the code chunks the keyboard shortcut is Shift + Enter.  For a list of useful keyboard shortcuts in jupyter notebook you can go to this [link](https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330)

## Objects
First, we create a list and print it out

```python
myList = [1, 2, 'foo']
print("original list:", myList)
```

Note that the indexing in python starts at 0

```python
print("First item:", myList[0])
print("Second item:", myList[1])
```

You can also update parts of the list

```python
myList[1] = 2.5
myList
```

However, you cannot do that with tuples

```python
myTuple = (1, 2, 'foo')
print("original tuple:", myTuple)

---

[Up: contents](index.md) · [try to update the tuple →](02-try-to-update-the-tuple.md)
