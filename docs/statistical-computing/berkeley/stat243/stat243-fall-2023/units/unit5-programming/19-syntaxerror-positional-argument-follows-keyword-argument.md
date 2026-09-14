---
title: 'SyntaxError: positional argument follows keyword argument'
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit5-programming.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# SyntaxError: positional argument follows keyword argument

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

```


Functions may have unspecified arguments, which are designated using `*args`.
('args' is a convention - you can call it something else).
Unspecified arguments occurring at the beginning of the argument
list are generally a collection of like objects that will be manipulated
(consider `print`).

Here's an example where we see that we can manipulate *args*, which is a tuple,
as desired.

```python
def sum_args(*args):
    print(args[2])
    total = sum(args)
    return total

result = sum_args(1, 2, 3, 4, 5)
print(result)  # Output: 15
```

This syntax also comes in handy for some existing functions, such as
`os.path.join`, which can take either an arbitrary number of inputs or a list.

```python
os.path.join('a','b','c')
x = ['a','b','c']
os.path.join(*x)
```

### Function outputs

`return x` will specify `x` as the output of the function.  `return` can occur anywhere in the function, and
allows the function to exit as soon as it is done.

We can return multiple outputs using `return` - the return value will then be a tuple.

```python
def f(x):
    if x < 0:
        return -x**2
    else:
        res = x^2
        return x, res


f(-3)
f(3)
out1,out2 = f(3)
```


If you want a function to be invoked for its side effects, you can omit `return` or
explicitly have `return None` or simply `return`.


## Pass by value vs. pass by reference

When talking about programming languages, one often distinguishes
*pass-by-value* and *pass-by-reference*.

*Pass-by-value* means that when a
function is called with one or more arguments, a copy is made of each
argument and the function operates on those copies. In pass-by-value, changes to an
argument made within a function do not affect the value of the argument
in the calling environment.

*Pass-by-reference*
means that the arguments are not copied, but rather that information is
passed allowing the function to find and modify the original value of
the objects passed into the function. In pass-by-reference changes inside a
function can affect the object outside of the function.

Pass-by-value is elegant and modular in that functions do not have side
effects - the effect of the function occurs only through the return
value of the function. However, it can be inefficient in terms of the
amount of computation and of memory used. In contrast, pass-by-reference
is more efficient, but also more dangerous and less modular. It's more
difficult to reason about code that uses pass-by-reference because
effects of calling a function can be hidden inside the function.
Thus pass-by-value is directly related to functional programming.

Arrays and other non-scalar objects in Python are pass-by-reference (but note that tuples are immutable,
so one could not modify a tuple that is passed as an argument).

```python
def myfun(x):
    x[1] = 99

y = [0, 1, 2]
z = myfun(y)
type(z)
y
```


Let's see what operations cause arguments modified in a function to affect state outside of the function:

```python
def myfun(f_scalar, f_x, f_x_new, f_x_newid, f_x_copy):

    f_scalar = 99                 # global input unaffected
    f_x[0] = 99                   # global input MODIFIED
    f_x_new = [99,2,3]            # global input unaffected

    newx = f_x_newid
    newx[0] = 99                  # global input MODIFIED

    xcopy = f_x_copy.copy()
    xcopy[0] = 99                 # global input unaffected


scalar = 1
x = [1,2,3]
x_new = np.array([1,2,3])
x_newid = np.array([1,2,3])
x_copy = np.array([1,2,3])


myfun(scalar, x, x_new, x_newid, x_copy)
```

Here are the cases where state is preserved:

```python
scalar
x_new
x_copy
```

And here are the cases where state is modified:

```python
x
x_newid
```

Basically if you replace the reference (object name) then the state outside the function is preserved.
That's because a new local variable in the function scope is created. However in the
`
If you modify part of the object, state is not preserved.

The same behavior occurs with other mutable objects such as numpy arrays.

### Pointers

To put pass-by-value vs. pass-by-reference in a broader context, I want to briefly discuss
the idea of a pointer, common in compiled languages such as C.

```c
#| eval: false
int x = 3;
int* ptr;
ptr = &x;
*ptr * 7; // returns 21
```

  - The `int*` declares `ptr` to be a pointer to (the address of) the integer `x`.
  - The `&x` gets the address where `x` is stored.
  - `*ptr` dereferences `ptr`, returning the value in that address (which is 3 since `ptr` is the address of `x`.

Arrays in C are really pointers to a block of memory:

```c
#| eval: false
int x[10];
```

In this case `x` will be the address of the first element of the vector.
We can access the first element as `x[0]` or `*x`.

Why have we gone into this? In C, you can pass a pointer as an argument
to a function. The result is that only the scalar address is copied and
not the entire object, and inside the function, one can modify the
original object, with the new value persisting on exit from the
function. For example in the following example one passes in the address of an
object and that object is then modified in place, affecting its value when the function
call finishes.

```c
#| eval: false
int myCal(int* ptr){
    *ptr = *ptr + *ptr;
}

myCal(&x)  # x itself will be modified
```

So Python behaves similarly to the use of pointers in C.


## Namespaces and scopes

As discussed [here in the Python docs](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces),
a *namespace* is a mapping from names to objects that allows Python to find objects by name via clear rules that
enforce modularity and avoid name conflicts.

Namespaces are created and removed through the course of executing Python code. When a function is run, a namespace for the local
variables in the function is created, and then deleted when the function finishes executing. Separate function calls
(including recursive calls) have separate namespaces.

*Scope* is closely related concept -- a scope determines what namespaces are accessible from a given place in one's code. Scopes are nested and determine where and in what order Python searches the various namespaces for objects.

Note that the ideas of namespaces and scopes are relevant in most other languages, though the details of how they work can differ.

These ideas are very important for modularity, isolating the names of objects to avoid conflicts.

This allows you to use the same name in different modules or submodules, as well as different packages using the same name.

Of course to make the objects in a module or package available we need to use `import`.

Consider what happens if you have two modules that both use `x` and you import `x` using `from`.

```python
#| eval: false
from mypkg.mymod import x
from mypkg.mysubpkg import x
x  # which x is used?
```

We've added `x` twice to the namespace of the global scope. Are both available? Did one 'overwrite' the other? How do I access the other one?

This is much better:

```python
import mypkg
mypkg.x

import mypkg.mysubpkg
mypkg.mysubpkg.x
```

Side note: notice that `import mypkg` causes the name `mypkg` itself to be in the current (global) scope.


We can see the objects in a given namespace/scope using `dir()`.

```python
xyz = 7
dir()

import mypkg
dir(mypkg)
import mypkg.mymod
dir(mypkg.mymod)

import builtins
dir(builtins)
```

Here are the key scopes to be aware of, in order ("LEGB") of how the namespaces are searched:

 - **L**ocal scope: objects available within function (or class method).
 - non-local (**E**nclosing) scope: objects available from functions enclosing a given function (we'll talk about this more later; this relates to *lexical scoping*).
 - **G**lobal (aka 'module') scope: objects available in the module in which the function is defined (which may simply be the default global scope when you start the Python interpreter). This is also the local scope if the code is not executing inside a function.
 - **B**uilt-ins scope: objects provided by Python through the built-ins module but available from anywhere.

Note that `import` adds the name of the imported module to the namespace of the current (i.e., local) scope.

We can see the local and global namespaces using `locals()` and `globals()`.

```bash
cat local.py
```

Run the following code to see what is in the different namespaces:

```python
#| eval: false
import local

gx = 99
local.myfun(3)
```

Strangely (for me being more used to R, where package namespaces are locked), we can add an object to a namespace created from a module or package:

```python
mymod.x = 33
dir(mymod)

import numpy as np
np.x = 33
'x' in dir(np)
```

As more motivation, consider this example.

Suppose we have this code in a module named `test_scope.py`:

```bash
cat test_scope.py
```

Now suppose we also define `magic_number` in the scope in which `myfun` is called from.

```python
import test_scope
magic_number = 900
test_scope.myfun(3)
```

We see that Python uses `magic_number` from the module.
What would be bad about using `magic_number` from the global scope of the Python session
rather than the global scope of the module? Consider a case where instead of using the `test_scope.py` module we were using
code from a package.

### Lexical scoping (enclosing scopes)

In this section, we seek to understand what happens in the following
circumstance. Namely, where does Python get the value for the object `x`?

```python
#| eval: false
def f(y):
  return(x + y)

f(3)
```


Variables in the enclosing scope are available within a function.
 **The enclosing scope is the
scope in which a function is defined, not the scope from
which a function is called.**

This approach is called *lexical scoping*. R and many other languages
also use lexical scoping.

The behavior of basing lookup on where functions are defined rather than where they are called from extends the local-global scoping discussed in the previous section, with similar motivation.


Let's dig deeper to understand where Python looks for non-local variables, illustrating lexical scoping:

```python
#| eval: false
## Case 1
x = 3
def f2():
    print(x)

def f():
    x = 7
    f2()

f() # what will happen?

## Case 2
x = 3
def f2()
    print(x)

def f():
    x = 7
    f2()

x = 100
f() # what will happen?

## Case 3
x = 3
def f():
    def f2():
        print(x)
    x = 7
    f2()

x = 100
f() # what will happen?

## Case 4
x = 3
def f():
    def f2():
        print(x)
    f2()

x = 100
f() # what will happen?
```

Here's a tricky example:

```python
#| eval: false
y = 100
def fun_constructor():
	y = 10
	def g(x):
            return(x + y)
	return(g)

## fun_constructor() creates functions
myfun = fun_constructor()
myfun(3)
```

Let's work through this:

1.  What is the enclosing scope for the function `g()`?
2.  Which `y` does `g()` use?
3.  Where is `myfun` defined (this is tricky -- how does `myfun` relate to `g`)?
4.  What is the enclosing scope for `myfun()`?
5.  When `fun_constructor()` finishes, does its namespace disappear?
    What would happen if it did?
6.  What does `myfun` use for `y`?


We can use the `inspect` package to see information about the closure.

```python
import inspect
inspect.getclosurevars(myfun)
```

(Note that I haven't fully investigated the use of `inspect`,
but it looks like it has a lot of useful tools.)

Be careful when using variables from non-local scopes as the
value of that variable may well not be what
you expect it to be. In general one wants to think carefully before using variables that
are taken from outside the local scope, but in some cases it can be useful.

Next we'll see some ways of accessing variables outside of the local scope.

### Global and non-local variables

We can create and modify global variables and variables in the enclosing scope using
`global` and `nonlocal` respectively. Note that *global* is in the context of the current module
so this could be a variable in your current Python session if you're working with functions defined
in that session or a global variable in a module or package.

```python
del x

def myfun():
    global x
    x = 7

myfun()
print(x)

x = 9
myfun()
print(x)
```

```python
def outer_function():
    x = 10  # Outer variable
    def inner_function():
        nonlocal x
        x = 20  # Modifying the outer variable
    print(x)  # Output: 10
    inner_function()
    print(x)  # Output: 20

outer_function()
```

In R, one can do similar things using the global assignment operator `<<-`.

### Closures

One way to associate data with functions is to use a *closure*.
This is a functional programming way to
achieve something like an OOP class. This [Wikipedia
entry](https://en.wikipedia.org/wiki/Closure_(computer_programming))
nicely summarizes the idea, which is a general functional programming idea and not specific to Python.

Using a closure
involves creating one (or more functions) within a function call and
returning the function(s) as the output. When one executes the original
function (the constructor), the new function(s) is created and returned and one can then
call that function(s). The function then can access objects in
the enclosing scope (the scope of the constructor) and
can use `nonlocal` to assign into the enclosing scope, to which the
function (or the multiple functions) have access. The nice thing about
this compared to using a global variable is that the data in the closure
is bound up with the function(s) and is protected from being changed by
the user.

```python
x = np.random.normal(size = 5)
def scaler_constructor(input):
	data = input
	def g(param):
            return(param * data)
	return(g)

scaler = scaler_constructor(x)
del x # to demonstrate we no longer need x
scaler(3)
scaler(6)
```

So calling `scaler(3)` multiplies 3 by the value of `data` stored in the closure (the namespace of the enclosing scope) of the function `scaler`.

Note that it can be hard to see the memory use involved in the closure.

Here's a more realistic example. There are other ways you could do this, but this is slick:

```python
def make_container(n):
    x = np.zeros(n)
    i = 0
    def store(value = None):
        nonlocal x, i
        if value is None:
            return x
        else:
            x[i] = value
            i += 1
    return store


nboot = 20
bootmeans = make_container(nboot)

import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/iris.csv')
data = iris['SepalLength']

for i in range(nboot):
    bootmeans(np.mean(np.random.choice(data, size = len(data), replace = True)))


bootmeans()

bootmeans.__closure__
```

## Decorators

Now that we've seen function generators, it's straightforward to discuss *decorators*.

A decorator is a wrapper around a function that extends the functionality of the function without actually modifying the function.

We can create a simple decorator "manually" like this:

```python
def verbosity_wrapper(myfun):
    def wrapper(*args, **kwargs):
        print(f"Starting {myfun.__name__}.")
        output = myfun(*args, **kwargs)
        print(f"Finishing {myfun.__name__}.")
        return output
    return wrapper

verbose_rnorm = verbosity_wrapper(np.random.normal)

x = verbose_rnorm(size = 5)
x
```

Python provides syntax that helps you create decorators with less work (this is an example of the general idea of *syntactic sugar*).

We can easily apply our decorator defined above to a function as follows. Now the function name refers to the wrapped version of the function.

```python
@verbosity_wrapper
def myfun(x):
    return x

y = myfun(7)
y
```

Our decorator doesn't do anything useful, but hopefully you can imagine that the idea of being able to have more control over the operation of functions could be useful. For example we could set up a timing wrapper so that when we run a function, we get a report on how long it took to run the function. Or using the idea of a closure, we could keep a running count of the number of times a function has been called.

One real-world example of using decorators is in setting up functions to run in parallel in `dask`, which we'll discuss in Unit 7.

---

[← for loop: needs storage set up and multiple lines](18-for-loop-needs-storage-set-up-and-multiple-lines.md) · [Up: contents](index.md) · [8. Memory and copies →](20-8-memory-and-copies.md)
