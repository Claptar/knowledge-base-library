---
title: 'myArray[2.73] # What do you think is going to happen?'
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit5-programming.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# myArray[2.73] # What do you think is going to happen?

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

```

R is less strict and will do conversions in some cases that Python won't:

```r
x <- rnorm(5)
x[2.0]
x[2.73]
```

What are the advantages and disadvantages of the different behaviors of Python and R?

### Dataframes

Hopefully you're also familiar with the Pandas dataframe type.

Pandas picked up the idea of dataframes from R and functionality is similar in many ways to
what you can do with R's `dplyr` package.

`dplyr` and `pandas` provide a lot of functionality for the "split-apply-combine"
framework of working with "rectangular" data.

Often analyses are done in a stratified fashion - the same operation or
analysis is done on subsets of the data set. The subsets might be
different time points, different locations, different hospitals,
different people, etc.

The split-apply-combine framework is intended to operate in this kind of
context:
  - first one splits the dataset by one or more variables,
  - then one does something to each subset, and
  - then one combines the results.

split-apply-combine is also closely related to the famous Map-Reduce framework
underlying big data tools such as Hadoop and Spark.

It's also very similar to standard SQL queries involving filtering, grouping, and
aggregation.

### Python object protocols

There are a number of broad categories of kinds of objects: `mapping`, `number`, `sequence`, `iterator`. These are called object protocols.

All objects that fall in a given category share key characteristics. For example `sequence` objects have a notion of "next", while
`iterator` objects have a notion of "stopping".

If you implement your own class that falls into one of these categories, it should follow the relevant protocol
by providing the required methods. For example a container class that supports iteration should provide the `__iter__` and `__next__` methods.

Here we see that `tuple`s are iterable containers:

```python
mytuple = ("apple", "banana", "cherry")

for item in mytuple:
    print(item)

myit = iter(mytuple)

print(next(myit))
print(next(myit))
myit.__next__()

x = zip(['clinton', 'bush', 'obama', 'trump'], ['Dem', 'Rep', 'Dem', 'Rep'])
next(x)
next(x)
```

We can also go from an iterable object to a standard list:

```python
r = range(5)
r
list(r)
```

---

[← myArray[2.0] # What do you think is going to happen?](06-myarray-2-0-what-do-you-think-is-going-to-happen.md) · [Up: contents](index.md) · [5. Programming paradigms: object-oriented and functional programming →](08-5-programming-paradigms-object-oriented-and-functional-progr.md)
