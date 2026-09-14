---
title: 'myList[2.73] # What do you think is going to happen?'
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# myList[2.73] # What do you think is going to happen?

**Source:** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

```

R is less strict and will do conversions in some cases that Python won't:

```r
x <- rnorm(5)
x[2.0]
x[2.73]
```

Question: What are the advantages and disadvantages of the different behaviors of Python and R?

### Dataframes

Hopefully you're also familiar with the Pandas dataframe type.

Pandas picked up the idea of dataframes from R and functionality is similar in many ways to
what you can do with R's `dplyr` package.

`dplyr` and `pandas` provide a lot of functionality for the "split-apply-combine"
framework of working with "rectangular" data. Unfortunately, using Pandas can be a bit hard to learn/remember. I suggest looking into learning [`polars`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit2-dataTech.html#reading-data-quickly-arrow-and-polars) as an alternative.

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

All objects that fall in a given category share key characteristics. For example `sequence` objects have notions of length and accessing (ordered) elements by index, while `iterator` objects have notions of "next" and of "stopping".

Object protocols are implemented based on the [Python object model](16-8-object-oriented-programming-oop.md#the-python-object-model-and-dunder-methods) using **dunder** methods.
For a class (such as one you write) to implement an object protocol, it must define a particular set of class methods, discussed at the link above.

---

[← myList[2.0] # What do you think is going to happen?](10-mylist-2-0-what-do-you-think-is-going-to-happen.md) · [Up: contents](index.md) · [7. Programming paradigms: object-oriented and functional programming →](12-7-programming-paradigms-object-oriented-and-functional-progr.md)
