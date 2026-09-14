---
title: Let's turn that into a function for later use
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Let's turn that into a function for later use

**Source:** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

def mem_used():
    print("Memory usage:", psutil.Process().memory_info().rss/10**6, " MB.")
```

We can see the size of an object (in bytes) with `sys.getsizeof()`.

```python
my_list = [1, 2, 3, 4, 5]
sys.getsizeof(my_list)

x = np.random.normal(size = 10**7) # should use about 80 MB
sys.getsizeof(x)
```

However, we need to be careful about objects that refer to other objects:

```python
y = [3, x]
sys.getsizeof(y)  # Whoops!
```


Here's a
trick where we serialize the object, as if to export it, and then see
how long the binary representation is.

```python
import pickle
ser_object = pickle.dumps(y)
sys.getsizeof(ser_object)
```

There are also some flags that one can start `python` with that allow
one to see information about memory use and allocation. See `man python`.
You could also look into the `memory_profiler` or `pympler` packages.

## How memory is used in Python

### Two key tools: `id` and `is`

We can use the `id` function to see where in
memory an object is stored and `is` to see if two
object are actually the same objects in memory.
It's particularly useful for understanding storage
and memory use for complicated data structures.
We'll also see that they can be handy tools for
seeing where copies are made and where they are not.

```python
x = np.random.normal(size = 10**7)
id(x)
sys.getsizeof(x)
y = x
id(y)
x is y
sys.getsizeof(y)

z = x.copy()
id(z)
sys.getsizeof(z)
```


### Memory use in specific circumstances

#### How lists are stored

Here we can use `id` to determine how the overall list is stored as
well as the elements of the list.

```python
nums = np.random.normal(size = 5)
obj = [nums, nums, np.random.normal(size = 5), ['adfs']]

id(nums)
id(obj)
id(obj[0])
id(obj[1])
id(obj[2])
id(obj[3])
id(obj[3][0])

obj[0] is obj[1]
obj[0] is obj[2]
```

What do we notice?

  - The list itself appears to be a array of references (pointers) to the component elements.
  - Each element has its own address.
  - Two elements of a list can use the same memory (see the first two elements here, whose contents are at the same memory address).
  - A list element can use the same memory as another object (or part of another object).


A note about calling `id` on list elements, e.g., `id(obj[0])`. Running that code causes execution of `obj[0]`, and the result is passed into `id`. That creates a new temporary object that is passed to `id`. The temporary object references the same object that `obj[0]` does, so we find out the id of `obj[0]`.

#### How character strings are stored.

Similar tricks are used for storing strings (and also integers). We may explore this in a problem set problem.

#### How numpy arrays are stored

To do vectorized calculations and linear algebra efficiently, one needs the data in arrays stored contiguously in memory, and this is how numpy arrays are stored. We've seen that a numpy array involves the actual numbers plus 112 bytes of metadata/overhead associated with the object.

We can't usefully call `id` on elements of the array. Consider this:

```python
x = np.random.normal(size=5)
type(x[1])
id(x[1])
tmp1 = x[1]
tmp2 = x[1]
id(tmp1)
id(tmp2)
```

Each time we get the `x[1]` element we are creating a new numpy float64 scalar object. This is because each element of the array is not its own object (unlike a list element) so extracting the element involves copying the value and making a new object.

Another indication of the array being stored contiguously is that if we pickle the array, its size is just a bit more than the size needed just to store the 8-byte numbers. If we instead pickle a list containing those same numbers, the result is more than twice as big, related to the pointers involved in referring to the individual numbers.

#### Modifying elements in place

What do this simple experiment tell us?

```python
x = np.random.normal(size = 5)
id(x)
x[2] = 3.5
id(x)
```

It makes some sense that modifying elements of an object here doesn't cause a copy -- if it did, working with large objects would be very difficult.

#### Shallow copying

A *shallow* copy only makes a new top-level object. The elements within the object are still shared with the original object.

```python
x = [3, [1,2,3]]
y = x.copy()
id(x)
id(y)
x[0] = 9
y[0]

id(x[1])
id(y[1])
y[1][2] = 99
x
```

We can force a *deep* copy such that nothing is shared between the objects.

```python
import copy
x = [3, [1,2,3]]
y = copy.deepcopy(x)

id(x[1])
id(y[1])
y[1][2] = 99
x
```


### When are copies made?

Let's try to understand when Python uses additional memory for objects, and how it knows when it can delete memory.
We'll use large objects so that we can use `free` or `top` to see how memory use by the Python process changes.

```python
x = np.random.normal(size = 10**8)
id(x)
y = x
id(y)

x = np.random.normal(size = 10**8)
id(x)
```

Only if we re-assign `x` to reference a different object does additional memory get used.


#### How does Python know when it can free up memory?

Python keeps track of how many names refer to an object and only
removes memory when there are no remaining references to an object.

```python
import sys

x = np.random.normal(size = 10**8)
y = x
sys.getrefcount(y)

del x
sys.getrefcount(y)
del y
```

We can see the number of references using `sys.getrefcount`.
Confusingly, the number is one higher than we'd expect,
because it includes the temporary reference from passing
the object as the argument to `getrefcount`.

```python
x = np.random.normal(size = 5)
sys.getrefcount(x)  # In reality, only 1.
y = x
sys.getrefcount(x)  # In reality, 2.
sys.getrefcount(y)  # In reality, 2.

del y
sys.getrefcount(x)  # In reality, only 1.

y = x
x = np.random.normal(size = 5)
sys.getrefcount(y)  # In reality, only 1.
sys.getrefcount(x)  # In reality, only 1.
```


This notion of reference counting occurs in other contexts, such as
shared pointers in C++ and in how R handles copying and garbage collection.

## Strategies for saving memory

A few basic strategies for saving memory include:

-   Avoiding unnecessary copies.
-   Removing objects that are not being used, at which point the Python garbage collector should free up the memory.
-   Use iterators (e.g., `range()`) and [generators](https://wiki.python.org/moin/Generators) to avoid building long lists that are iterated over.


If you're really trying to optimize memory use, you may also consider:

-   Using types that take up less memory (e.g., `Bool`, `Int16`, `Float32`) when
    possible.
    ```python
    x = np.array(np.random.normal(size = 5), dtype = "float32")
    x.itemsize
    x = np.array([3,4,2,-2], dtype = "int16")
    x.itemsize
    ```
-   Reading data in from files in chunks rather than reading the entire dataset (more in Unit 7).
-   Exploring packages such as `arrow` for efficiently using memory, as discussed in [Unit 2](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit2-dataTech.html#reading-data-quickly-arrow-and-polars).


## Example

Let's work through a real example where we keep a running tally of
current memory in use and maximum memory used in a function call. We'll
want to consider hidden uses of memory and when copies of the object are made rather than simply creating a new reference to an existing object.  This
code (translated from the original R code) comes from a PhD student's research. For our purposes here, let's assume
that the input `x` and `y` are very long numpy arrays using a lot of memory.

`np.isnan` returns an boolean array of True/False values indicating whether each input element is a NaN (not a number).

```python
#| eval: false
def fastcount(xvar, yvar):
    naline = np.isnan(xvar)
    naline[np.isnan(yvar)] = True
    localx = xvar.copy()
    localy = yvar.copy()
    localx[naline] = 0
    localy[naline] = 0
    useline = ~naline
    ## We'll ignore the rest of the code.
    ## ....

fastcount(x, y) # Assume x, y are existing large numpy arrays.

```

!!! tip "Tip"
In the code above, note all the places where new memory must be allocated.
:::

---

[← Print the memory usage](26-print-the-memory-usage.md) · [Up: contents](index.md) · [11. Efficiency →](28-11-efficiency.md)
