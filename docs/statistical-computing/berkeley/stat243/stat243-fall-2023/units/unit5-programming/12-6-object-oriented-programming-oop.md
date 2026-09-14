---
title: 6. Object-oriented programming (OOP)
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit5-programming.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Object-oriented programming (OOP)

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

OOP involves organizing your code around objects that contain information, and methods that operate in specific ways on those objects.
Objects belong to classes. A class is made up of fields (the data) that store information and methods (functions) that operate on the fields.


By analogy, OOP focuses on the nouns, with the verbs being part of the nouns, while FP focuses on the verbs (the functions), which operate on the nouns (the arguments).

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

Here's the initial definition of the class with methods and fields.

```python
import numpy as np

class tsSimClass:
    '''
    Class definition for time series simulators
    '''
    def __init__(self, times, mean = 0, corParam = 1):
        ## add assertions that corParam is numeric, length 1 and times is np array
        self._times = times
        self.n = len(times)
        self.mean = mean
        self.corParam = corParam
        self._currentU = False
        self._calcMats()
    def __str__(self):    # 'print' method
        return f"An object of class `tsSimClass` with {self.n} time points."
    def __len__(self):
        return self.n
    def setTimes(self, newTimes):
        self._times = newTimes
        self._calcMats()
    def getTimes(self):
        return self._times
    def simulate(self):
        if not self._currentU:
            self._calcMats()
        ## analogous to mu+sigma*z for generating N(mu, sigma^2)
        return self.mean + np.dot(self.U.T, np.random.normal(size = self.n))
    def _calcMats(self):
        ## calculates correlation matrix and Cholesky factor
        lagMat = np.abs(self._times[:, np.newaxis] - self._times)
        corMat = np.exp(-lagMat ** 2 / self.corParam ** 2)
        self.U = np.linalg.cholesky(corMat)
        print("Done updating correlation matrix and Cholesky factor.")
        self._currentU = True

```


Now let's see how we would use the class.

```python
myts = tsSimClass(np.arange(1, 101), 2, 1)
print(myts)
np.random.seed(1)
## here's a simulated time series
y1 = myts.simulate()

import matplotlib.pyplot as plt
plt.plot(myts.getTimes(), y1, '-')
plt.xlabel('time')
plt.ylabel('process values')
## simulate a second series
y2 = myts.simulate()
plt.plot(myts.getTimes(), y2, '--')
plt.show()
```

We could set up a different object that has different parameter values.
That new simulated time series is less wiggly because the `corParam` value
 is larger than before.


```python
myts2 = tsSimClass(np.arange(1, 101), 2, 4)
np.random.seed(1)
## here's a simulated time series with a different value of
## the correlation parameter (corParam)
y3 = myts2.simulate()

plt.plot(myts2.getTimes(), y3, '-', color = 'red')
plt.xlabel('time')
plt.ylabel('process values')
plt.show()
```

#### Copies and references

Next let's think about when copies are made. In the next example `mytsRef` is a copy of `myts`
in the sense that both names point to the same underlying object.
But no data were copied when the assignment to `mytsRef` was done.

```python
mytsRef = myts
## 'mytsRef' and 'myts' are names for the same underlying object
import copy
mytsFullCopy = copy.deepcopy(myts)

## Now let's change the values of a field
myts.setTimes(np.arange(1,1001,10))
myts.getTimes()[0:4]
mytsRef.getTimes()[0:4] # the same as `myts`
mytsFullCopy.getTimes()[0:4] # different from `myts`
```

In contrast `mytsFullCopy` is a reference to a different object, and
all the data from `myts` had to be copied over to `mytsFullCopy`. This takes additional memory (and time), but is also safer, as it avoids the possibility that the user might modify `myts` and not realize that they were also affecting `mytsRef`. We'll discuss this more when we discuss copying in the section on memory use.

#### Encapsulation

Those of you familiar with OOP will probably be familiar with the idea of public and private fields and methods.

Why have private fields (i.e., *encapsulation*)? The use of private fields shields them from
    modification by users. Python doesn't really provide this functionality but by convention,
    attributes whose name starts with `_` are considered private.
    In this case, we don't want users to modify the
`times` field. Why is this important? In this example, the correlation matrix and
    the Cholesky factor U are both functions of the vector of times. So
    we don't want to allow a user to directly modify `times`. If they did, it would leave the fields of the object in inconsistent states. Instead we want  them to use `setTimes`, which correctly keeps all the fields
    in the object internally consistent (by calling `_calcMats`). It also allows us to improve efficiency
by controlling when computationally expensive operations are carried out.

In a module, objects that start with `_` are a weak form of private attributes. Users can access them, but `from foo import *` does not import them.

#### Challenge

> **Challenge**
>
> How would you get Python to quit immediately, without asking for any more information, when you simply type `q` (no parentheses!) instead of `quit()`? There are actually a couple ways to do this. (Hint: you can do this by understanding what happens when you type `q` and how to exploit the characteristics of Python classes.)


### Inheritance

Inheritance can be a powerful way to reduce code duplication and keep your code organized in a logical (nested) fashion.
Special cases can be simple extensions of more general classes.

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

More relevant examples of inheritance in Python and R include how regression models are handled.
E.g., in Python's `statsmodels`, the [`OLS` class inherits from the `WLS` class](https://www.statsmodels.org/stable/_modules/statsmodels/regression/linear_model.html#OLS).


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
smoke = Bear("Smoky the Bear", 77)
smoke.count
```

The class attribute allows us to manipulate information relating to all instances of the class, as seen here where we keep track of the number of bears that have been created.

### Adding attributes

It turns out we can add instance attributes on the fly in some cases, which is a bit disconcerting in some ways.

```python
yog.bizarre = 7
yog.bizarre

def foo(x):
    print(x)

foo.bizarre = 3
foo.bizarre
```


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

#### The print function

Like `len`, `print` is a generic function, with various
class-specific methods.

We can write a print method for our own class by defining the `__str__`
method as well as a `__repr__` method giving what to display when the name of an object is typed.

```python
class Bear:
      def __init__(self, name, age):
          self.name = name
          self.age = age

yog = Bear("Yogi the Bear", 23)
print(yog)

class Bear:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def __str__(self):
          return f"A bear named {self.name} of age {self.age}."
      def __repr__(self):
          return f"Bear(name={self.name}, age={self.age})"

yog = Bear("Yogi the Bear", 23)
print(yog)   # Invokes __str__
yog          # Invokes __repr__
```


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

## The Python object model and *dunder* methods.

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

Let's see an example of defining a dunder method for the `Bear` class.

```python
class Bear:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def __str__(self):
          return f"A bear named {self.name} of age {self.age}."
      def __add__(self, value):
          self.age += value

yog = Bear("Yogi the Bear", 23)
yog + 12
print(yog)
```


Most of the things we work with in Python are objects.
Functions are also objects, as are classes.

```python
type(len)

def foo(x):
    print(x)

type(foo)

type(Bear)
```

---

[← OOP: modify objects using class methods](11-oop-modify-objects-using-class-methods.md) · [Up: contents](index.md) · [7. Functional programming →](13-7-functional-programming.md)
