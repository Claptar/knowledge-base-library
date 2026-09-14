---
title: 6. Object-oriented programming (OOP)
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Object-oriented programming (OOP)

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

OOP involves organizing your code around objects that contain information, and methods that operate in specific ways on those objects.
Objects belong to classes. A class is made up of fields (the data) that store information and methods (functions) that operate on the fields.


By analogy, OOP focuses on the nouns, with the verbs being part of the nouns, while FP focuses on the verbs (the functions), which operate on the nouns (the arguments).

Most of the things we work with in Python are objects.
Functions are also objects, as are classes.

```python
type(len)

def foo(x):
    print(x)

type(foo)

import numpy as np
x = np.array([1.2, 3.4])
type(x)
```


## Principles

Some of the standard concepts in object-oriented programming include *encapsulation*, *inheritance*, *polymorphism*, and *abstraction*.

*Encapsulation* involves preventing direct access to internal data in an object from outside the object. Instead the class is designed so that access (reading or writing) happens through the interface set up by the programmer (e.g., 'getter' and 'setter' methods). However, Python actually doesn't really enforce the notion of internal or private information.

*Inheritance* allows one class to be based on another class, adding more specialized features.  For example in the `statsmodels` package, the OLS class inherits from the WLS class.

*Polymorphism* allows for different behavior of an object or function depending on the context. A polymorphic function behaves differently depending on the input types. For example, think of a print function or an addition operator behaving differently depending on the type of the input argument(s). A polymorphic object is one that can belong to different classes (e.g., based on inheritance), and a given method name can be used with any of the classes. An example would be having a base or super class called 'algorithm' and various specific machine learning algorithms inheriting from that class. All of the classes might have a 'predict' method.

*Abstraction* involves hiding the details of how something is done (e.g., via the method of a class), giving the user an interface to provide inputs and get outputs. By making the actual computation a black box, the programmer can modify the internals without changing how a user uses the system.

Classes generally have *constructors* that initialize objects of the class and *destructors* that remove objects.

## Classes in Python

Python provides a pretty standard approach to writing object-oriented code focused on classes.

Our example is to create a class for working with random time series. Each object of the class has specific parameter values that control the stochastic behavior of the time series. With a given object we can simulate one or more time series (realizations).

Here's the initial definition of the class with methods and fields (aka attributes).

```python
import numpy as np

class tsSimClass:
    '''
    Class definition for time series simulator
    '''
    ## dunder methods (more later)
    def __init__(self, times, mean = 0, cor_param = 1, seed = 1):
        ## This is the constructor, called when `tsSimClass(...)` is invoked
        ## to create an instance of the class.

        ## For robustness, need checks that `cor_param` is numeric of length 1 and `times` is np array.
        ## Public attributes
        self.n = len(times)
        self.mean = mean
        self.cor_param = cor_param
        ## Private attributes (encapsulation)
        self._times = times
        self._current_U = False
        ## Some setup steps
        self._calc_mats()
        np.random.seed(seed)
    def __str__(self):    # 'print' method
        return f"An object of class `tsSimClass` with {self.n} time points."
    def __len__(self):
        return self.n

    ## Public methods: getter and setter (encapsulation)
    def set_times(self, new_times):
        self._times = new_times
        self._current_U = False
        self._calc_mats()
    def get_times(self):
        return self._times

    ## Main public method
    def simulate(self):
        if not self._current_U:
            self._calc_mats()
        ## analogous to mu+sigma*z for generating N(mu, sigma^2)
        return self.mean + np.dot(self.U.T, np.random.normal(size = self.n))

    ## Private method.
    def _calc_mats(self):
        ## Calculates correlation matrix and Cholesky factor (caching).
        lag_mat = np.abs(self._times[:, np.newaxis] - self._times)
        cor_mat = np.exp(-lag_mat ** 2 / self.cor_param ** 2)
        self.U = np.linalg.cholesky(cor_mat)
        print("Done updating correlation matrix and Cholesky factor.")
        self._current_U = True

```


Now let's see how we would use the class.

```python
#| fig-alt: Randomly-generated time series from our object
myts = tsSimClass(np.arange(1, 101), 2, 1)
print(myts)
np.random.seed(1)
## Here's a simulated time series.
y1 = myts.simulate()

import matplotlib.pyplot as plt
plt.plot(myts.get_times(), y1, '-')
plt.xlabel('time')
plt.ylabel('process values')
## Simulate a second series.
y2 = myts.simulate()
plt.plot(myts.get_times(), y2, '--')
plt.show()
```

We could set up a different object that has different parameter values.
That new simulated time series is less wiggly because the `cor_param` value
is larger than before.


```python
#| fig-alt: Another randomly-generated time series
myts2 = tsSimClass(np.arange(1, 101), 2, 4)
np.random.seed(1)
## Here's a simulated time series with a different value of
## the correlation parameter (cor_param).
y3 = myts2.simulate()

plt.plot(myts2.get_times(), y3, '-', color = 'red')
plt.xlabel('time')
plt.ylabel('process values')
plt.show()
```

#### Copies and references

Next let's think about when copies are made. In the next example `myts_ref` is a copy of `myts`
in the sense that both names point to the same underlying object.
But no data were copied when the assignment to `myts_ref` was done.

```python
myts_ref = myts
## 'myts_ref' and 'myts' are names for the same underlying object.
import copy
myts_full_copy = copy.deepcopy(myts)

## Now let's change the values of a field.
myts.set_times(np.arange(1,1001,10))
myts.get_times()[0:4]
myts_ref.get_times()[0:4] # the same as `myts`
myts_full_copy.get_times()[0:4] # different from `myts`
```

In contrast `myts_full_copy` is a reference to a different object, and
all the data from `myts` had to be copied over to `myts_full_copy`. This takes additional memory (and time), but is also safer, as it avoids the possibility that the user might modify `myts` and not realize that they were also affecting `myts_ref`. We'll discuss this more when we discuss copying in the section on memory use.

#### Encapsulation

Those of you familiar with OOP will probably be familiar with the idea of public and private fields and methods.

Why have private fields (i.e., *encapsulation*)? The use of private fields shields them from
    modification by users. Python doesn't really provide this functionality but by convention,
    attributes whose name starts with `_` are considered private.
    In this case, we don't want users to modify the
`times` field. Why is this important? In this example, the correlation matrix and
    the Cholesky factor U are both functions of the array of times. So
    we don't want to allow a user to directly modify `times`. If they did, it would leave the fields of the object in inconsistent states. Instead we want  them to use `set_times`, which correctly keeps all the fields
    in the object internally consistent (by calling `_calc_mats`). It also allows us to improve efficiency
by controlling when computationally expensive operations are carried out.

In a module, objects that start with `_` are a weak form of private attributes. Users can access them, but `from foo import *` does not import them.


### Inheritance

Inheritance can be a powerful way to reduce code duplication and keep your code organized in a logical (nested) fashion.
Special cases can be simple extensions of more general classes. A good example of inheritance in Python and R is how regression models are handled.
E.g., in Python's `statsmodels` package, the [`OLS` class inherits from the `WLS` class](https://www.statsmodels.org/stable/_modules/statsmodels/regression/linear_model.html#OLS). Or if we think back to the random time series example and generalize it, one might have a `StochasticProcess` class, with a `GaussianProcess` class that inherits from it, and a `ExpGaussianProcess` class (implementing a Gaussian process with an exponential covariance` inheriting from the `GaussianProcess` class.

```python
class Bear:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def __str__(self):
          return f"A bear named '{self.name}' of age {self.age}."
      def color(self):
          return "unknown"

class GrizzlyBear(Bear):
      def __init__(self, name, age, num_people_killed = 0):
          super().__init__(name, age)
          self.num_people_killed = num_people_killed
      def color(self):
          return "brown"

yog = Bear("Yogi the Bear", 23)
print(yog)
yog.color()

num399 = GrizzlyBear("Jackson Hole Grizzly 399", 35)
print(num399)
num399.color()
num399.num_people_killed
```

Here the `GrizzlyBear` class has additional fields/methods beyond
those inherited from the base class (the `Bear` class),
i.e., `num_people_killed` (since grizzly bears are much more dangerous
than some other kinds of bears), and perhaps additional or modified
methods. Python uses the methods specific to the `GrizzlyBear`
class if present before falling back to methods of the `Bear` class if not
present in the `GrizzlyBear` class.

The above is an example of polymorphism. Instances of the `GrizzlyBear` class are polymorphic
because they can have behavior from both the `GrizzlyBear` and `Bear` classes. The `color` method is polymorphic
in that it can be used for both classes but is defined to behave differently depending on the class.


## Attributes

Both fields and methods are *attributes*.

We saw the notion of attributes when looking at HTML and XML, where the information was stored as
key-value pairs that in many cases had additional information in the form of attributes.

### Class attributes vs. instance attributes

Here `count` is a class attribute while `name` and `age` are instance attributes.

```python
class Bear:
      count = 0
      def __init__(self, name, age):
          self.name = name
          self.age = age
          Bear.count += 1

yog = Bear("Yogi the Bear", 23)
yog.count
smokey = Bear("Smokey the Bear", 77)
smokey.count
```

The class attribute allows us to manipulate information relating to all instances of the class, as seen here where we keep track of the number of bears that have been created.

### Adding attributes

What do you think will happen if we do the following?

```python
#| eval: false
yog.bizarre = 7
yog.bizarre

def foo(x):
    print(x)

foo.bizarre = 3
foo.bizarre
```

It turns out we can add instance attributes on the fly in some cases, which is a bit disconcerting in some ways.

## Generic function OOP

Let's consider the `len` function in Python. It seems to work magically on various kinds of objects.

```python
x = [3, 5, 7]
len(x)

x = np.random.normal(size = 5)
len(x)

x = {'a': 2, 'b': 3}
len(x)
```

Suppose you were writing the `len` function. What would you have to do to make it work as it did above?
What would happen if a user wants to use `len` with a class that they define?

Instead, Python implements the `len` function by calling the `__len__` method of the class that the argument belongs to.

```python
x = {'a': 2, 'b': 3}
len(x)
x.__len__()
```

`__len__` is a *dunder* method (a "Double-UNDERscore" method), which we'll discuss more in a bit.

Something similar occurs with operators:

```python
x = 3
x + 5
x = 'abc'
x + 'xyz'
x.__add__('xyz')
```

This use of generic functions is convenient in that it allows us to work with a variety of kinds of objects using familiar functions.

The use of such generic functions and operators is similar in spirit to function or method *overloading* in C++ and Java.
It is also how the (very) old S3 system in R works. And it's a key part of the (fairly) new Julia language.

### Why use generic functions?

The Python developers could have written `len` as a regular function with a bunch of `if` statements so that it can handle different kinds of input objects.

This has some disadvantages:

  1. We need to write the code that does the checking.
  2. Furthermore, all the code for the different cases all lives inside one potentially very long function, unless we create class-specific helper functions.
  3. Most importantly, `len` will only work for existing classes. And users can't easily extend it for new classes that they create because they don't control the `len` (built-in) function. So a user could not add the additional conditions/classes in a big if-else statement. The generic function approach makes the system *extensible* -- we can build our own new functionality on top of what is already in Python.


### Multiple dispatch OOP

The dispatch system involved in `len` and `+` involves only the first argument to the function (or operator). In contrast, [Julia emphasizes the importance of multiple dispatch](https://docs.julialang.org/en/v1/manual/methods) as particularly important for mathematical computation. With multiple dispatch, the specific method can be chosen based on more than one argument.

In R, the old (but still used in some contexts) [S4](http://adv-r.had.co.nz/S4.html) system in R and the new [R7](https://rconsortium.github.io/OOP-WG) system both provide for multiple dispatch.

As a very simple example unrelated to any specific language, multiple dispatch would allow one to do the following with the addition operator:

```
3 + 7    # 10
3 + 'a'  # '3a'
'hi' +  ' there'  # 'hi there'
```

The idea of having the behavior of an operator or function adapt to the type of the input(s) is one aspect of *polymorphism*.

## The Python object model and *dunder* methods

Now that we've seen the basics of classes, as well as generic function OOP, we're in a good position to understand the Python object model.

Objects are dictionaries that provide a mapping from attribute names to their values, either fields or methods.

*dunder* methods are special methods that Python will invoke when various functions are called on instances of the class or other standard operations are invoked. They allow classes to interact with Python's built-ins.

Here are some important dunder methods:

 - `__init__` is the constructor (initialization) function that is called when the class name is invoked (e.g., `Bear(...)`)
 - `__len__` is called by `len()`
 - `__str__` is called by `print()`
 - `__repr__` is called when an object's name is invoked
 - `__call__` is called if the instance is invoked as a function call (e.g., `yog()` in the `Bear` case)
 - `__add__` is called by the `+` operator.
 - `__getitem__` is called by the `[` slicing operator.


### The print function

Like `len`, `print` is a generic function, with various
class-specific methods.

We can write a print method for our own class by defining the `__str__`
method. One generally also defines a `__repr__` method giving what to display when the name of an object is typed.

### Dunder methods: example

```python
## Basic class definition
class Bear:
      def __init__(self, name, age):
          self.name = name
          self.age = age

yog = Bear("Yogi the Bear", 23)
print(yog)

## Class definition with various dunder methods
class Bear:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def __str__(self):
          return f"A bear named {self.name} of age {self.age}."
      def __repr__(self):
          return f"Bear(name={self.name}, age={self.age})"
      def __add__(self, value):
          self.age += value
          return None

yogi = Bear("Yogi the Bear", 23)
print(yogi)   # Invokes __str__
yogi          # Invokes __repr__
yogi + 12
print(yogi)
```


!!! tip "Tip"
Let's check our understanding of the object model.

How would you get Python to quit immediately, without asking for any more information, when you simply type `q` (no parentheses!) instead of `quit()`? (Hint: you can do this by understanding what happens when you type `q` and how to exploit the characteristics of Python classes.)
:::

### Python object protocols: Example 1 -- iterators

A container class that supports iteration should provide the `__iter__` and `__next__` methods to implement the iterator protocol.

Here we see that `tuple`s are iterable containers (although they are not iterators themselves):

```python
mytuple = ("apple", "banana", "cherry")

for item in mytuple:
    print(item)

## We can manually create the iterator and iterate through it.
myit = iter(mytuple)
## myit = mytuple.__iter__()  ## This is equivalent to using `iter(mytuple)`.

type(myit)

print(next(myit))
print(next(myit))
myit.__next__()   ## This is equivalent to using `next(myit)`.
```

I think it makes sense that tuples are iterable containers but they are not iterators themselves, because
we wouldn't want to "consume" our tuple (leaving it empty) by iterating over it.

Here's another iterator example. `zip` objects are iterators themselves (and we can see them being consumed).

```python
#| error: true
x = zip(['clinton', 'bush', 'obama', 'trump'], ['Dem', 'Rep', 'Dem', 'Rep'])
next(x)
next(x)
next(x)
next(x)
next(x)
```

We can also go from an iterable object to a standard list:

```python
x = zip(['clinton', 'bush', 'obama', 'trump'], ['Dem', 'Rep', 'Dem', 'Rep'])
list(x)
```


### Python object protocols: Example 2 -- context managers using `with`

We've seen that the standard way to read/write to a file in Python uses `with`, like this:

```python
#| eval: false
with open('myfile.txt', 'r') as file:
     lines = file.readlines()
```

This creates a "context manager" that is equivalent to:

```python
#| eval: false
file = open('myfile.txt', 'r')
try:
    lines = file.readlines()
finally:
    file.close()
```

With either approach, we get (1) exception handling in case something goes wrong with the read/write (in this case `readlines`) and (2) automatic closing of the file, regardless of what happens in the execution of the code, based on the `finally` block that does any needed cleanup.

What does this have to do with *dunder* methods and object protocols?

Well, one can use `with` with any class for which one wants to implements the context manager protocol by providing `__enter__` and `__exit__` methods. These are invoked before and after the code in the scope of the `with` block is run.


Here's a basic example:

```python
import time

class MyTimer(object):
    def __enter__(self):
        print(f"Starting at {time.ctime()}.")

    def __exit__(self, exception_type, exception_value, traceback):
        print(f"Ending at {time.ctime()}.")

with MyTimer():
    x = np.random.normal(size=50000000)
    del x
```

A more useful example would be setting up a context manager to handle database queries by connecting to the database via `__enter__` and disconnecting via `__exit__`.

---

[← OOP: modify objects using class methods](11-oop-modify-objects-using-class-methods.md) · [Up: contents](index.md) · [7. Functional programming →](13-7-functional-programming.md)
