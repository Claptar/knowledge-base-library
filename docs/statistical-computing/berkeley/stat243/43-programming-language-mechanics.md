---
title: "43. Programming Language Mechanics"
course: "Berkeley Stat 243 Fall 2024"
chapter: 43
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 43. Programming Language Mechanics

## What this covers

This chapter is Unit 5 of STAT 243, taught in 2021 (R-centric) and again in 2024 and 2025
(Python-centric, and nearly identical between those two years). It assumes the earlier units —
working in the shell, basic scripting, some exposure to at least one of R or Python — and asks a
different question than "how do I write a script that works": how does the language itself
represent data, resolve names, manage memory, and organize code, and how do those choices differ
between R and Python? It moves through regular expressions, talking to the operating system and to
compiled code, the module and package system, the type model, the object-oriented and functional
paradigms, and how memory is allocated and copied. Where a concept is common to both languages it
is presented once, in whichever treatment was clearer, with the language named explicitly; where
the languages genuinely differ — pass-by-value vs. pass-by-reference; R's three object systems
against Python's one — both are kept.

## Regular expressions and text manipulation

Python's `re` module provides Perl-style regular expressions. `re.search` finds the first match and
returns a match object with `.group()`, `.start()`, `.end()`; `re.findall` returns every match as a
list; `re.finditer` returns a lazy iterator over matches, scanning for the next one only when
asked — useful on a large text, and the same laziness as `pandas.read_csv(chunksize=n)`.

```python
text = "Here's my number: 919-543-3300."
m = re.search(r"\d+", text)
m.group(), m.start(), m.end()          # ('919', 19, 22)
re.findall(r"\d+", text)               # ['919', '543', '3300']
```

Compiling a pattern once with `re.compile` is good practice when the same regex runs against every
line of a file, and a reminder that a regex is a small separate language, compiled into a
finite-state machine that does the matching.

`re.sub` replaces matches, and parenthesized groups do double duty: they control what `findall`
returns — only the *captured* subgroups, so pulling a full alternation out with `findall` needs an
extra outer group, `((http|ftp)://)` — and a replacement can refer back to what was captured via
`\1`, `\2`, ... ("capturing groups"):

```python
re.sub(r"([0-9]+)", r"_\1_", "Call 919-543-3300.")
# 'Call _919_-_543_-_3300_.'
```

**Greedy matching.** By default a repetition operator (`+`, `*`, `{m,n}`) matches as much as
possible — correct for `\d+` on "998 balloons", wrong for stripping HTML tags, where `<.*>` on
`"<b>x</b>"` eats from the first `<` to the *last* `>`. A `?` after the repetition (`<.*?>`) makes
it non-greedy, matching as little as possible instead.

**Escaping.** A character with special meaning to the regex engine (`.`, `^`, `$`, ...) must be
escaped to match it literally, and the backslash used for escaping is *itself* the string literal's
own escape character. As of Python 3.12, `\d` can no longer pass through untouched as regex
syntax — Python tries to interpret it as a string escape first, and there is no such sequence — so
a "digits" pattern now needs `"\\d"`, or the raw-string form `r"\d"`, which turns off string-literal
escaping entirely. Matching a literal backslash is the extreme case, the "backslash plague": four
backslashes to match one (`r"\\"`).

R has the same problem for a different reason: its string literals always treat backslash as an
escape character, with no Python-3.12-style relaxation, so `\.` written in R needs `"\\."`, and
`stringr` inherits the same double-backslash convention.

## Interacting with the operating system and external code

Both languages let you run a shell command and capture the result, query the filesystem portably,
and read environment variables:

```python
import subprocess, os
files = subprocess.run(["ls", "-al"], capture_output=True)
os.path.exists("data.csv")
os.listdir(os.path.join("..", "data"))   # os.path.join is OS-agnostic
os.environ["PATH"]
```

```r
files <- system("ls -al", intern = TRUE)
file.exists("data.csv")
list.files(file.path("..", "data"))       # file.path is the R analogue
Sys.getenv("PATH")
```

`platform.system()`/`Sys.info()` and `platform.python_version()`/`sessionInfo()` report on the
machine and interpreter — worth including whenever you ask for help, since behaviour can be
version- or platform-specific. Either language's script can double as a shell script: a shebang
line (`#!/usr/bin/env python` or `#!/usr/bin/env Rscript`), `chmod +x`, and it runs directly;
arguments arrive via `argparse` in Python or the unparsed character vector `commandArgs(TRUE)` in
R — coercing a wrong-shaped argument silently produces `NA`, so check what actually arrived.

**Calling out to compiled code.** R and Python are both, to varying degrees, wrappers around
faster compiled languages, and calling into C, C++, or Fortran is how they get that speed without
leaving the scripting language. This isn't incidental to R's design: its predecessor S was built at
Bell Labs in the 1970s–80s specifically as an interactive front end onto Fortran, then the standard
numerical language, and a good deal of that Fortran still runs under statistical software today.
Python's `Cython` translates typed Python to C and can define C-callable functions; R's `Rcpp` lets
you write C++ that looks and feels like R, making it easy to pass data between the two.

## Modules, packages, and namespaces

A *module* is a file of related code; a *package* is a directory of modules with an `__init__.py`
that runs on import and controls what's exposed. Importing associates a module's objects with a
name in a *namespace* — rather than dumping them into the caller's own:

```python
import mymod
mymod.x             # explicit: x lives in mymod's own namespace
from mymod import x
x                    # now a name in the caller's namespace, independent from here on
```

`from module import *` is generally avoided for exactly this reason: it risks silent name
collisions and blurs which names came from where. A package's `__init__.py` controls what a user
sees without exposing the internal layout — `numpy.linspace` lives in
`numpy/core/function_base.py` but is re-exported as `numpy.linspace`, while `numpy.linalg` is kept
as its own sub-namespace deliberately. Names starting with `_` are a *weak* form of private —
reachable by name, but skipped by `from ... import *`.

R's package system draws the same distinction with different words: a *library* is a directory on
disk (`.libPaths()` lists them); a *package* is what's installed once (`install.packages()`) and
loaded every session (`library(pkg)`) — conflating the two terms is the fastest way to mark
yourself as new to R. A package's objects live in their own namespace, invisible to `ls()` until
attached; `search()` shows the stack of attached namespaces.

Both ecosystems distinguish a *source* package (raw code, needing a compiler for any
C/C++/Fortran) from a *binary* package (pre-compiled — Python calls these *wheels*), and both let
you freeze an environment for reproducibility (`pip freeze > requirements.txt`,
`conda env export --no-builds > environment.yml`); a Conda environment goes further and pins the
interpreter version itself.

## Types and data structures

**Static vs. dynamic typing.** In a compiled language like C, a variable's type is declared before
use and checked at compile time; the same name can never later hold a different type. R and Python
are *dynamically* typed — a name is a label rebindable to any type at any time:

```python
x = "hello"
x = 7        # legal: x now refers to an int
```

Dynamic typing buys quick, low-ceremony code, at the cost of what static typing gives for free:
catching a type error before the program runs, and speed, since a value's type never needs
checking while running.

**Python's built-in types.** The core containers are lists, tuples, and dictionaries, plus scalar
int/float/str/bool. `numpy` layers a fixed-dtype array on top — a homogeneous, contiguous block of
numbers is what fast numerical code needs — but it will silently upcast a mixed list of ints and
floats to all-float, so force the dtype (`dtype="float64"`) when that matters. **Mutability** cuts
across types: lists, dicts, and sets can be modified in place; tuples and strings cannot.

**Coercion.** Python is comparatively strict about implicit conversion — indexing a list with a
float, `myList[2.73]`, is an error — while R is permissive and silently truncates: `x[2.73]` on an
R vector returns `x[2]`. Neither is unambiguously better: strictness catches bugs a permissive
language would swallow; permissiveness means less friction, at the cost of occasionally hiding a
real mistake.

**R's type model.** Where Python's containers are heterogeneous by default, R's basic container is
the *atomic vector*, holding a single type (`logical`, `integer`, `double`, `character`); a `list`
holds a heterogeneous collection. `class()` and `typeof()` answer different questions — `typeof()`
is internal storage, `class()` is how the object presents itself — and they diverge past the
simplest objects: a `data.frame`'s `typeof` is `"list"` (stored as a list of columns) but its
`class` is `"data.frame"`. R attaches metadata as *attributes* (`names`, `dim`, `class`, ...),
often carried silently through later operations, and this is also how R's class system works:
assigning a `class` attribute to an ordinary list is enough to make it participate in method
dispatch (below). One coercion trap worth knowing: indexing by a `factor` looks like indexing by
its printed label but is actually indexing by its underlying *integer code*, silently retrieving
the wrong element unless converted with `as.character()` first.

**Object protocols.** Broad categories of Python object — `sequence`, `iterator`, `mapping`,
`number` — share an interface a user-defined class opts into via the right dunder methods
(`__iter__`/`__next__` for an iterator, `__len__` for anything with a length, `__getitem__` for
anything indexable): `iter(x)` and `next(it)` are syntax over `x.__iter__()` and `it.__next__()`.

## Programming paradigms

Object-oriented programming (OOP) and functional programming (FP) are two ways of organizing the
same computation. FP is verb-focused: write self-contained functions and run them in sequence, each
a black box consuming inputs and producing outputs. OOP is noun-focused: define classes that bundle
data (*fields*) with the operations on it (*methods*), and drive the computation by calling methods
on objects — a statistical analogy is that an object is to a realization as a class is to a random
variable.

```python
x = np.array([1.2, 3.5, 4.2, 9.7])
x2 = np.transpose(np.reshape(x, (2, 2)))     # functional: chain functions
x2 = x.reshape(2, 2).transpose()             # OOP: chain methods on the object
y = [1.2, 3.5]; y.append(7.9)                # OOP: mutate the object in place
```

Most languages mix both styles — R leans more functional, Python more object-oriented — and which
reads better depends on the task: a pipeline of successive transformations suits the functional
style; a simulation of interacting entities with internal state suits objects.

## Object-oriented programming

Four ideas recur across every OOP system: **encapsulation** (hide an object's internals behind a
controlled interface rather than free access to its fields); **inheritance** (a class specializes
another, adding fields and methods); **polymorphism** (the same method name behaves differently by
class, or a function behaves differently by argument type); **abstraction** (hide *how* a method
does its job behind a stable interface, so internals can change without breaking callers).

### Classes in Python

A class bundles a constructor (`__init__`), fields, and methods. This example simulates a Gaussian
process — an object stores a correlation parameter, and `simulate()` returns a realization:

```python
class tsSimClass:
    def __init__(self, times, mean=0, cor_param=1):
        self.n, self.mean, self.cor_param = len(times), mean, cor_param
        self._times = times            # leading underscore: private by convention only
        self._calc_mats()

    def set_times(self, new_times):
        self._times = new_times
        self._calc_mats()              # keeps U consistent with the new times

    def simulate(self):
        return self.mean + np.dot(self.U.T, np.random.normal(size=self.n))

    def _calc_mats(self):
        lag = np.abs(self._times[:, None] - self._times)
        self.U = np.linalg.cholesky(np.exp(-lag**2 / self.cor_param**2))
```

Hiding `_times` behind `set_times()` matters because the Cholesky factor `U` is a *function of*
`_times`: a direct assignment would leave the object internally inconsistent. Python doesn't
enforce this — `_`-prefixed attributes are convention, not a lock — but it signals "go through the
method." (`myts_ref = myts` aliases rather than copies, exactly as Memory, below, describes for any
Python object.)

**Inheritance and polymorphism.**

```python
class Bear:
    def __init__(self, name, age):
        self.name, self.age = name, age
    def color(self):
        return "unknown"

class GrizzlyBear(Bear):
    def __init__(self, name, age, num_people_killed=0):
        super().__init__(name, age)
        self.num_people_killed = num_people_killed
    def color(self):
        return "brown"
```

`GrizzlyBear` reuses `Bear`'s constructor via `super().__init__(...)` and adds a field; Python looks
for a method on the specific class first, falling back to the base class — the pattern
`statsmodels`'s `OLS` inheriting from `WLS` also follows. `color()` is polymorphic: the same name
means something different per class. A class attribute (in the class body, not `__init__`) is
shared across every instance — e.g. `Bear.count`, incremented on each construction — while an
instance attribute like `self.name` belongs to just that object.

### Generic functions and the object model

`len()` works on a list, a `numpy` array, or a dict interchangeably — not via one large `if`/`elif`
chain needing an edit for every new container type, but by calling the `__len__` method of whatever
class the argument is: `len(x)` really means `x.__len__()`. This *generic function* dispatch is why
the system is extensible: a user's own class automatically works with `len()`, `print()`, and
comparison operators just by implementing the right **dunder** methods — `__init__` (constructor),
`__len__` (`len`), `__str__` (`print`), `__repr__` (bare name), `__add__` (`+`), `__getitem__`
(`[...]`), `__call__` (calling the instance itself). Operator overloading in C++/Java and R's S3
dispatch (below) are the same idea, dispatching on only the *first* argument's class; Julia's
multiple dispatch and R's S4 generalize it to several arguments at once.

### R's object systems

R has three, layered by age and formality. **S3**, the oldest and still most common, is nothing
more than an ordinary list with a `class` attribute attached — `class(mod2)` for a `glm` object is
`c("glm", "lm")`. A generic like `summary()` is a one-line stub, `UseMethod("summary")`, dispatching
to `summary.<class>` and falling back to `summary.default`, with no check that an object claiming a
class actually has the fields a method expects — S3 trusts the programmer completely. **S4** (and
the newer R7) formalizes this with typed *slots*, validity checks, and dispatch on several
arguments' classes at once — common in Bioconductor and `lme4`. **R6** behaves most like Python's:
unlike S3/S4 objects, copied on modification (see Memory, below), an R6 object is a genuine mutable
reference — `myts_ref <- myts` aliases rather than copies — and a true independent copy needs
`$clone()`, R's counterpart of `copy.deepcopy`. R6 also has real private fields, where assignment
from outside is a hard error, not a convention.

## Functional programming

A function is "purely functional" if it only reads its arguments, has no other effect on the
session's state, and returns its result exclusively through `return`. The appeal is that such a
function is a black box: understanding a program reduces to understanding the composition of the
functions it calls, without tracing what each one might quietly have changed elsewhere.

### Pass-by-value vs. pass-by-reference

The sharpest behavioural difference between R and Python covered here. R passes arguments **by
value** — a function receives its own copy of each argument, so modifying it inside the function
cannot affect the caller's copy:

```r
myfun <- function(x) { x[2] <- 7; x }
x <- 1:3
new_x <- myfun(x)
x        # unchanged: 1 2 3
```

Python passes **by reference** — the function receives a reference to the *same* object, so
mutating a mutable argument in place (a list, a `numpy` array — not a tuple) changes it for the
caller too:

```python
def myfun(x):
    x[1] = 7
    return x

x = np.array([1, 2, 3])
myfun(x)
x   # modified! array([1, 7, 3])
```

So Python code can violate the no-side-effects principle by accident; avoiding it means copying
the argument (`y = x.copy()`) before mutating the copy. Whether Python code preserves the caller's
state comes down to whether a name is *replaced* (`x = [99, 2, 3]`, a harmless new local binding)
or *mutated in place* (`x[0] = 99`, visible outside) — the distinction Memory, below, makes precise
via object identity.

### Functions as first-class objects

Everything in Python — a function, a class — is an object: assignable, passable as an argument,
returnable from another function. A function that takes a function as an argument, returns one, or
both, is a *higher-order function* (`map`, `functools.partial`). A *lambda* is a small, unnamed
function defined inline: `list(map(lambda v: v * 2, x))`; `functools.partial` pre-binds some
arguments and returns a new function taking the rest: `round3 = partial(round, ndigits=3)`.

A *map* operation — running one function over every element of a collection — is the functional
alternative to a `for` loop: `.apply()`, list comprehensions, and `map()` itself are all map
operations. The same idea generalized to distributed data is *MapReduce* (Hadoop, Spark); applied
to groups of rows of a `data.frame`, it's *split-apply-combine*, behind `dplyr` and
`pandas.groupby()` — split by a variable, do the same thing to each subset, combine the results.

**Arguments.** Arguments without a default must come first and be supplied by every caller,
positionally or by keyword (`name=value`) once positional arguments are exhausted. `*args` collects
further positional arguments into a tuple; `**kwargs` collects keyword arguments into a dict — used
by, e.g., `os.path.join(*paths)` to accept either a fixed list or an unpacked one.

### The call stack, frames, and scoping

Every function call pushes a *frame* — a fresh namespace of local variables — onto the *call
stack*, popped when the call returns; a chain of nested calls is why a traceback shows the whole
chain (Python's default; R shows only the erroring frame, with the full chain via `traceback()`).

Name lookup follows a fixed order, **LEGB**: **L**ocal (the current frame), **E**nclosing (any
function this one is nested inside — searched *lexically*, by where the function was *defined*,
not where it was *called* from), **G**lobal (the defining module), **B**uilt-in. This *lexical
scoping* is shared with R, and "enclosing, not calling" is the part that trips people up.

A closure exploits it directly: a function defined inside another keeps access to the enclosing
function's variables even after that call returns, because Python keeps the enclosing namespace
alive as long as something references it — `g = scaler_constructor(data)` returns an inner function
`g` that still sees `data` long after the constructor call finished, a functional substitute for a
small stateful object. `global` and `nonlocal` assign into an outer scope, needed because plain
assignment always creates a new local name; R's analogue is `<<-`.

A **decorator** wraps a function to add behaviour without editing its body — logging, timing, or
(later in the course) scheduling work in parallel with `dask` or JIT-compiling with Numba — and is
syntax sugar over passing a function to a function that returns a new one: `@verbosity_wrapper`
above `def myfun(x): ...` is exactly `myfun = verbosity_wrapper(myfun)`.

## Memory and copies

Two facts drive almost everything about memory in a scripting language: a numeric array uses 8
bytes per element (`np.float64`, R's `double`), and knowing *when a new object gets allocated* is
what separates efficient code from code that silently doubles its memory footprint.

Python's `id(x)` reports where an object lives and `x is y` tests whether two names refer to the
*same* object, not merely equal values — so it's possible to see directly when an operation copies
and when it doesn't: `y = x` is a second name for the same object (`id(x) == id(y)` is `True`, no
data copied), while rebinding `x` to a fresh `np.random.normal(...)` costs new memory. Modifying an
element in place (`x[2] = 3.5`) doesn't copy either — if it did, large arrays would be unworkable.
Python tracks how many names refer to an object (`sys.getrefcount`) and frees the memory once that
count reaches zero; `del` only removes the name, not necessarily the memory immediately.

R's mechanism is the same idea under a different name — *copy-on-change*, historically tracked via
a count called `NAMED`, now a reference count much like Python's — with one crucial difference in
*when* the copy happens. Because R is pass-by-value, it must copy proactively, the moment a second
name would otherwise see a mutation the first name didn't ask for; Python (pass-by-reference) never
copies on modification at all:

<figure>
<svg viewBox="0 0 380 160" role="img" aria-label="After y equals x, modifying x mutates the shared object in Python but triggers a silent copy first in R">
  <defs>
    <marker id="arrM" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="10" y="13" font-size="12" fill="currentColor">before: y = x (aliased, one object)</text>

  <text x="10" y="42" font-size="12" fill="currentColor">Python: x[0]=9 mutates in place</text>
  <rect x="10" y="50" width="28" height="20" fill="none" stroke="currentColor"/>
  <text x="24" y="64" font-size="11" text-anchor="middle" fill="currentColor">x</text>
  <rect x="46" y="50" width="28" height="20" fill="none" stroke="currentColor"/>
  <text x="60" y="64" font-size="11" text-anchor="middle" fill="currentColor">y</text>
  <rect x="100" y="46" width="170" height="28" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="185" y="64" font-size="10" text-anchor="middle" fill="currentColor">[9, .56, .70, ...]</text>
  <line x1="38" y1="60" x2="100" y2="60" stroke="currentColor" marker-end="url(#arrM)"/>
  <line x1="60" y1="70" x2="100" y2="66" stroke="currentColor" marker-end="url(#arrM)"/>

  <text x="10" y="96" font-size="12" fill="currentColor">R: x[1]&#60;-9 copies before writing</text>
  <rect x="10" y="104" width="28" height="20" fill="none" stroke="currentColor"/>
  <text x="24" y="118" font-size="11" text-anchor="middle" fill="currentColor">x</text>
  <rect x="46" y="104" width="28" height="20" fill="none" stroke="currentColor"/>
  <text x="60" y="118" font-size="11" text-anchor="middle" fill="currentColor">y</text>
  <rect x="100" y="100" width="170" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="185" y="115" font-size="10" text-anchor="middle" fill="currentColor">new: [9, .56, ...]</text>
  <rect x="100" y="126" width="170" height="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="185" y="141" font-size="10" text-anchor="middle" fill="currentColor">orig: [.52, .56, ...]</text>
  <line x1="38" y1="114" x2="100" y2="110" stroke="currentColor" marker-end="url(#arrM)"/>
  <line x1="60" y1="124" x2="100" y2="136" stroke="currentColor" marker-end="url(#arrM)"/>
</svg>
<figcaption>The same aliasing after y = x resolves differently once one name is modified: Python mutates the shared object in place, so y sees the change too; R's copy-on-change silently forks a new copy so y keeps the original.</figcaption>
</figure>

**Layout matters, at two scales.** A Python list is an array of *pointers* to its elements — two
list elements can legitimately share an `id()`, cheap to extract regardless of size. A `numpy`
array stores its numbers contiguously instead, needed for vectorized arithmetic to be fast, so
`x[1]` manufactures a fresh scalar object each time it's evaluated. R's `inspect()` shows the same
list-of-pointers structure for R lists, with a reference count (`REF(n)`) on every node — the
mechanism copy-on-change is built on. Contiguous layout also matters for speed: a CPU's cache holds
whatever was read most recently, so code that walks memory in the order it's stored — row by row,
`numpy`'s default — beats code that jumps around it, an access-pattern effect unrelated to the
arithmetic itself. And a dictionary or environment looks up a key in constant time via *hashing* —
mapping the key to a bucket directly — instead of scanning labels one at a time; R's plain named
vectors, notably, do *not* hash and so scan linearly, one of the few places its convenient syntax
hides a real performance cost.

### A worked example: tracing allocations

```python
def fastcount(xvar, yvar):
    naline = np.isnan(xvar)          # new object
    naline[np.isnan(yvar)] = True    # temporary, freed almost immediately; naline itself
                                      # is modified in place
    localx, localy = xvar.copy(), yvar.copy()   # two new objects
    localx[naline] = 0               # modified in place, no new object
    localy[naline] = 0               # modified in place, no new object
    useline = ~naline                # new object
    ...
```

Reading a function line by line this way — which names are freshly bound, which are existing
objects being mutated, which temporaries appear and vanish within a line — is the discipline that
catches memory blow-ups before they happen on a real-sized dataset.

**Saving memory:** avoid copies you don't need; let unreferenced objects be garbage-collected
rather than holding names past their use; prefer an iterator or generator to a full list you only
intend to iterate over once; and, when memory is genuinely tight, use a narrower dtype (`float32`,
`int16`) or read data in chunks rather than all at once (Unit 7).

**A closing note on speed.** A vectorized expression like `np.exp(x) + 3 * np.sin(x)` still makes
several passes over the data, allocating a temporary array each time; a JIT compiler that *fuses*
the operations into one pass (JAX's `jax.jit`, via the XLA compiler) avoids that cost. Separately,
R evaluates function arguments *lazily* — an argument the body never uses is never computed — the
same delay-until-needed idea used deliberately in Dask, Spark, and (historically) TensorFlow 1, to
let the system optimize a whole chain of operations jointly rather than step by step. Python itself
evaluates eagerly.

## Exercises

1. Write a regex that flags a spam-like word with digits or non-letter characters substituted into
   it, such as "V1agra" or "Fancy repl!c@ted watches", and one that extracts every email address
   from a block of text.
2. The pattern `((1[-.])?(\d{3}[-.]){1,2}\d{4})` was offered as a compact way to match US phone
   numbers such as "919-543-3300" or "1.919.554.3800". Give a string this pattern would match that
   is not actually a valid phone number.
3. Rather than removing commas that aren't field separators from a CSV-like line (via
   `re.sub(r"([^\",]),", r"\1", text)`), write a substitution that converts the true delimiters to
   pipes (`|`) instead, leaving commas inside quoted fields untouched.
4. A string contains dates written as "Aug-3", "May-9". Write a regex search-and-replace that turns
   them into "3 Aug", "9 May".
5. Rewrite the HTML-tag-stripping substitution `re.sub("<.*?>", "", text)` without relying on the
   `?` non-greedy modifier.
6. Explain, in terms of the object model, what would have to be true for typing `q` with no
   parentheses to quit the interpreter, given that quitting ordinarily requires calling `quit()`.
7. For a diagonal or otherwise structured matrix $D$ and a dense matrix $X$, the naive translations
   `X + D`, `D @ X`, and `X @ D` are far more expensive than they need to be. How would you compute
   each more efficiently, using what you know about structured and sparse matrix representations?
8. Suppose a large matrix is stored row-major but a computation genuinely needs column sums. Design
   an approach that accumulates each number's contribution to its column sum while still visiting
   every number in the order it is actually stored in memory.

## Sources

- **Fall 2025**, `units/unit5-programming/` files `01-overview.md`–`09-8-memory-and-copies.md`,
  plus the split fragments `11-the-following-lines-are-very-inefficient.md` and
  `12-define-the-sum-calculations-as-functions.md` (folded into "Memory and copies" rather than
  given their own section): the primary source throughout for the Python-centric material — regex,
  OS/external code, modules/packages, types, paradigms, OOP, functional programming, memory.
- **Fall 2024**, the same unit one year earlier and nearly identical; used to restore a few
  passages 2025 trimmed (the `print()`-as-generic-function example, the manual `tuple`-iteration
  example under object protocols, the plain "print method" discussion in OOP).
- **Fall 2021** (`stat243-fall-2021/units/unit5-programming/`), the R-centric predecessor,
  reconstructed by a model from a PDF with no text layer (`fidelity: reconstructed` in its front
  matter — treat R output shown there as illustrative, not verified). Source of everything
  R-specific: `system()`/`Sys.info()`/the R-script shebang (file 01); R regex escaping (file 02);
  package/library/namespace terms (file 03); the atomic-vector/list type model, attributes, and
  S3/S4/R6 (file 04); R6 aliasing and `$clone()` (file 05); copy-on-change/`NAMED`/`REF` (file 08).
  File 06 also covers `dplyr` long/wide reshaping and non-standard evaluation; only its
  split-apply-combine framing is used here (Functional programming) — the rest belongs with Unit
  2's data-technology material.
- **Not supplied for this chapter:** the 2021 unit's own "Functions, frames, and variable scope"
  section (named next in files 06's and 08's footers) was not among the files given for
  conversion, so the call stack, frames, and scoping here draw only on the Python-centric years.
- Referred to but not supplied: the "String processing in R and Python" and "Using the bash shell"
  tutorials and an online regex tester (2021, file 02); the R books and manuals listed as unit
  references (file 01 — Adler, Chambers, Wickham, Venables & Ripley, Murrell); Hadley Wickham's
  *Advanced R* (for further R6/S4 detail); the `dplyr` non-standard-evaluation vignette.
- **Not covered by this chapter:** `fall-2026/units/unit5-bigData/`. The course renumbered its
  units for 2026; that year's Unit 5 is a different subject — MapReduce, Dask, databases, and
  storage formats — not the programming-language material collected here.

---

[← 42. Good Practices, Debugging, and Reproducibility](42-good-practices-debugging-and-reproducibility.md) · [Contents](index.md) · [44. Principles of Parallel Computing →](44-principles-of-parallel-computing.md)
