---
title: Addresses and default lists
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/addresses
  and default lists.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/addresses and
  default lists.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Addresses and default lists

**Source:** [`section/s06/addresses and default lists.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/addresses and default lists.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

```python
def extendList(val, lst=[]):
    print 'the address of the list:', hex(id(lst))
    lst.append(val)
    return lst
```

```python
list1 = extendList(10)
```

```
the address of the list: 0x10f7d39e0
```

```python
print list1
```

```
[10]
```

```python
print hex(id(list1))
```

```
0x10f7d39e0
```

```python
list2 = extendList('hello', [])
```

```
the address of the list: 0x10f7c14d0
```

```python
print list2
```

```
['hello']
```

```python
print hex(id(list2))
```

```
0x10f7c14d0
```

```python
list3 = extendList('a')
```

```
the address of the list: 0x10f7d39e0
```

```python
print list1
```

```
[10, 'a']
```

```python
print hex(id(list1))
```

```
0x10f7d39e0
```

```python
print list2
```

```
['hello']
```

```python
print hex(id(list2))
```

```
0x10f7c14d0
```

```python
print list3
```

```
[10, 'a']
```

---

[Up: contents](../../index.md)
