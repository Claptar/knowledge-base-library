---
title: 7. Functional programming
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 7. Functional programming

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

This section covers an approach to programming called *functional programming* as well as various
concepts related to writing and using functions.

## Functional programming (in Python)

### Overview of functional programming

Functional programming is an approach to programming that emphasizes the use of modular, self-contained functions.
Such functions should operate only on arguments provided to
them (avoiding global variables), and **produce no side effects**, although in some cases there are good
reasons for making an exception. Another aspect of functional programming is
that functions are considered 'first-class' citizens in that they can be passed as arguments to another function,
returned as the result of a function, and assigned to variables. In other words, a function can be treated as any other variable.

In many cases (including Python and R), anonymous functions (also called 'lambda functions') can be created on-the-fly for use in various circumstances.

One can do functional programming in Python by focusing on writing modular, self-contained functions rather than classes. And functions are first-class citizens. However, there are aspects of Python that do not align with the principles mentioned above.

  - Python's pass-by-reference behavior causes functions to potentially have the important side effects of modifying arguments that are mutable (e.g., lists and numpy arrays but not tuples) if the programmer is not careful about not modifying arguments within functions.
  - Some operations are carried out by statements (e.g., `import`, `def`) rather than functions.

In contrast, R functions have pass-by-value behavior, which is more consistent with a pure functional programming approach.


### The principle of no side effects

Before we discuss Python further, let's consider how R behaves in more detail as R conforms more strictly to a functional programming perspective.

Most functions available in R (and ideally functions that you write as well) operate by taking in arguments and producing output that is then (presumably) used subsequently. The functions generally don't have any effect on the state of your R environment/session other than the output they produce.

An important reason for this (plus for not using global variables) is that it means that it is easy for people using the language to understand what code does. Every function can be treated a black box -- you don't need to understand what happens in the function or worry that the function might do something unexpected (such as changing the value of one of your variables). The result of running code is simply the result of a composition of functions, as in mathematical function composition.

One aspect of this is that R uses a *pass-by-value* approach to function arguments.
In R (but not Python), when you pass an object in as an argument and then modify it in the function, you are modifying a local copy of the variable that exists in the context (the *frame*) of the function and is deleted when the function call finishes:

```r
x <- 1:3
myfun <- function(x) {
      x[2] <- 7
      print(x)
      return(x)
}

new_x <- myfun(x)
x   # unmodified
```

In contrast, Python uses a *pass-by-reference* approach, seen here:

```python
x = np.array([1,2,3])
def myfun(x):
  x[1] = 7
  return x

new_x = myfun(x)
x   # modified!
```

And actually, given the pass-by-reference behavior, we would probably use a version of `myfun`
that looks like this:

```python
x = np.array([1,2,3])
def myfun(x):
  x[1] = 7
  return None

myfun(x)
x   # modified!
```


Note how easy it would be for a Python programmer to violate the 'no side effects' principle.
In fact to avoid it, we need to do some additional work in terms of making a copy of `x`
to a new location in memory before modifying it in the function.

```python
x = np.array([1,2,3])
def myfun(x):
  y = x.copy()
  y[1] = 7
  return y

new_x = myfun(x)
x   # no side effects!
```

More on pass-by-value vs. pass-by-reference later.

Even in R, there are some (necessary) exceptions to the idea of no side effects, such as `par()`, `library()`,  and `plot()`.

### Functions are first-class objects

Everything in Python is an object, including functions and classes. We can assign
functions to variables in the same way we assign numeric and other
values.

When we make an assignment we associate a name (a 'reference') with an object in memory.
Python can find the object by using the name to look up the object in the namespace.

```python
x = 3
type(x)
try:
    x([1,3,5])  # x is not a function (yet)
except Exception as error:
    print(error)

x = sum

x([1,3,5])
type(x)
```

We can call a function based on the text name of the function.

```python
function = getattr(np, "mean")
function(np.array([1,2,3]))
```

We can also pass a function into another function as the actual function
object. This is an important aspect of functional programming.
We can do it with our own function or (as we'll see shortly) with various built-in functions, such as `map`.

```python
def apply_fun(fun, a):
    return fun(a)

apply_fun(round, 3.5)
```

A function that takes a function as an argument, returns a function as a result, or both is known as a *higher-order function*.

### Which operations are function calls?

Python provides various statements that are not formal function calls but allow one to modify the current Python session:

 - `import`: import modules or packages
 - `def`: define functions or classes
 - `return`: return results from a function
 - `del`: remove an object

As we saw earlier with `+` (`__add__`), operators are examples of generic function OOP, where the appropriate method of the class of the first operand is called.

```python
x = np.array([0,1,2])
x - 1
x.__sub__(1)
x
```

Note that the use of the operator does not modify the object.

(Note that you can use `return(x)` and `del(x)` but behind the scenes the Python interpreter is intepreting those
as `return x` and `del x`.)

### Map operations

A *map* operation takes a function and runs the function on each element of some collection of items,
analogous to a mathematical map. This kind of operation is very commonly used in programming, particularly functional programming,
and often makes for clean, concise, and readable code.

Python provides a variety of map-type functions: `map` (a built-in) and `pandas.apply`. These are examples of higher-order functions -- functions that take a function as an argument. Another map-type operation is *list comprehension*, shown here:

```python
x = [1,2,3]
y = [pow(val, 2) for val in x]
y
```

In Python, `map` is run on the elements of an *iterable* object. Such objects include lists  as well as the result of `range()` and other functions that produce iterables.


```python
x = [1.0, -2.7, 3.5, -5.1]
list(map(abs, x))

list(map(pow, x, [2,2,2,2]))

```

Or we can use *lambda* functions to define a function on the fly:

```python
x = [1.0, -2.7, 3.5, -5.1]
result = list(map(lambda vals: vals * 2, x))
```

A lambda function is a temporary function that is defined "on-the-fly" rather than in advance and is never given a name. (These are also sometimes called *anonymous* functions.)

If you need to pass another argument to the function you can use a lambda function as above or `functools.partial`:

```python
from functools import partial

---

[← 6. Object-oriented programming (OOP)](12-6-object-oriented-programming-oop.md) · [Up: contents](index.md) · [Create a new round function with 'ndigits' argument pre-set →](14-create-a-new-round-function-with-ndigits-argument-pre-set.md)
