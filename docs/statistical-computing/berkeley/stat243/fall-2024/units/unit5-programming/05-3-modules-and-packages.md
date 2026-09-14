---
title: 3. Modules and packages
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Modules and packages

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Scripting languages that become popular generally have an extensive collection
of add-on packages available online (the causal relationship of the popularity and
the extensive add-on packages goes in both directions).

A big part of Python's popularity is indeed the extensive collection of add-on
packages on [PyPI](https://pypi.org) (and GitHub and elsewhere) and
via `Conda` that provide
much of Python's functionality (including core numerical capabilities via `numpy` and `scipy`).

To make use of a package it needs to be
installed on your system (using `pip install` or `conda install`) *once* and
loaded into Python (using the `import` statement) *every time you start a new session*.

Some modules are *installed* by default with Python (e.g., `os` and `re`),
but all need to be loaded by the user in a given Python session.

## Modules

A *module* is a collection of related code in a file with the extension `.py`.
The code can include functions, classes, and variables, as well as
runnable code. To access the objects in the module, you need to import the module.

Here we'll create `mymod.py` from the shell, but of course usually one would create it in an editor.

```bash
#| eval: false
cat << EOF > mymod.py
x = 7
range = 3
def myfun(x):
    print("The arg is: ", str(x), ".", sep = '')
EOF
```

```python
import mymod
print(mymod.x)
mymod.myfun(7)
```

## The import statement

The import statement allows one to get access to code in a module.
Importantly it associates the names of the objects in the module with
a name accessible in the scope in which it was imported (i.e., the current context). The mapping of
names (references) to objects is called a *namespace*. We discuss
[scopes and namespaces](20-syntaxerror-positional-argument-follows-keyword-argument.md#namespaces-and-scopes) in more detail later.

```python
#| error: true
del mymod
try:           # Check if `mymod` is in scope.
    mymod.x
except Exception as error:
    print(error)

y = 3

import mymod
mymod         # This is essentially a dictionary in the current (global) scope.
x             # This is not a name in the current (global) scope.
range         # This is a builtin, not from the module.
mymod.x
dir(mymod)
mymod.x
mymod.range
```

So `y` and `mymod` are in the global namespace and `range` and `x` are in the module namespace of `mymod`. You can access the built-in `range` function from the global namespace but it turns out it's actually in the built-ins scope (more later).

Note the usefulness of distinguishing the objects in a module from those in the global namespace.
We'll discuss this more in a bit.

That said, we can make an object defined in a module directly accessible in the current scope (adding it to the global namespace in this example) at which point it is distinct from the object in the module:

```python
from mymod import x
x   # now part of global namespace
dir()
mymod.x = 5
x = 3
mymod.x
x
```

But in general we wouldn't want to use `from` to import objects in that fashion because we could introduce name *conflicts* and we reduce modularity.

That said, it can be tedious to always have to type the module name (and in many cases there are multiple submodule names you'd also need to type).

```python
import mymod as m
m.x
```

## Packages

A package is a directory containing one or more modules and with a file
named `__init__.py` that is called when a package is imported and
serves to initialize the package.

Let's create a basic package.

```bash
#| eval: false
mkdir mypkg

cat << EOF > mypkg/__init__.py
## Make objects from mymod.py available as mypkg.foo rather than mypkg.mymod.foo.
## The "." is a "relative" import that means find "mymod" here in this directory.
from .mymod import *

print("Welcome to my package.")
EOF

cat << EOF > mypkg/mymod.py
x = 7

def myfun(val):
    print(f"Converting {val} to integer: {int(val)}.")
EOF
```

Note that if there were other modules, we could have imported from those as well.

Now we can use the objects from the module without having to know
that it was in a particular module (because of how `__init__.py` was set up).

```python
import mypkg
mypkg.x
mypkg.myfun(7.3)
```

Note, one can set `__all__` in an `__init__.py` to define what is imported,
which makes clear what is publicly available and hides what is considered
internal.

### Internal/private objects

We could add another module that the main module uses but that is not intended
for direct use by the user. Here we name the function to start with `_` following
the convention that this indicates a private/internal function.

```bash
#| eval: false
cat << EOF > mypkg/auxil.py

def _helper(val):
    return val + 10
EOF


cat << EOF >> mypkg/mymod.py

from .auxil import _helper

def myfun10(val):
    print(f"Converting {val} to integer plus 10: {int(_helper(val))}.")
EOF
```

```python
del mypkg
import mypkg
mypkg.myfun10(7.3)
del mypkg
```


### Subpackages

Packages can also have modules in nested directories, achieving additional modularity
via *subpackages*.
A package can automatically import the subpackages via the main `__init__.py`
or require the user to import them manually, e.g., `import mypkg.mysubpkg`.

```bash
#| eval: false
mkdir mypkg/mysubpkg

cat << EOF > mypkg/mysubpkg/__init__.py
from .values import *
print("Welcome to my package's subpackage.")
EOF

cat << EOF > mypkg/mysubpkg/values.py
x = 999
b = 7
d = 9
EOF
```

```python
import mypkg.mysubpkg     ## Note that __init__.py is invoked
mypkg.mysubpkg.b
mypkg.x
```

Note that a given `__init__.py` is invoked when importing anything nested within the
directory containing the `__init__.py`; in the case above the `__init__.py` from `mypkg`
is invoked, though for some reason the "Welcome to my package." output is not showing
up in this rendered document.

If we wanted to automatically import the subpackage we would add
`from . import mysubpkg` to `mypkg/__init__.py`, which uses [relative imports](https://docs.python.org/3/reference/import.html). The alternative "absolute" import would be `import mypkg.mysubpkg`, which finds `mypkg` using `sys.path` (which specifies a set of paths of where to look).


One would generally not import the items from `mysubpkg` directly into the `mypkg` namespace
but there may be cases one would do something like this. For example `numpy.linspace` is actually
found in `numpy/core/function_base.py`, but we don't need to refer to `numpy.core.linspace`
because of how `numpy` structures the `import` statements in `__init__.py`. In contrast, the linear algebra
functions are available via the subpackage namespace as `numpy.linalg.<function_name>`.

Take a look at `dir(numpy)`, `dir(numpy.linalg)`, and `dir(numpy.core)` to get a better sense for this in a real package.

## Installing packages

If a package is on PyPI or available through Conda but not on your system, you can install it
easily (usually). You don't need root permission on a machine to install
a package, though you may need to use `pip install --user` or set up a new Conda environment.

Packages often depend on other packages. In general, if one package depends on another,
pip or conda will generally install the dependency automatically.

One advantage of Conda is that it can also install non-Python packages on which a Python
package depends, whereas with pip you sometimes need to install a system package to
satisfy a dependency.

!!! note "Note"
It's not uncommon to run into a case where conda has trouble installing a package
because of version inconsistencies amongst the dependencies. `mamba` is a drop-in
replacement for `conda` and often does a better job of this "dependency resolution".
[We use `mamba` by default on the SCF](https://statistics.berkeley.edu/computing/software/install).
In recent versions of Conda, you can also use the Mamba's dependency resolver when running `conda` commands by running
`conda config --set solver libmamba`, which puts `solver: libmamba` in your `.condarc` file.
It's also generally recommended to use the `conda-forge` *channel* (i.e., location) when installing packages with Conda
(this is done automatically when using `mamba`). `conda-forge` provides a wide variety of up-to-date packages, maintained by the community.
:::


### Making your package installable (optional)

It's pretty easy to configure your package so that it can be built and installed via `pip`. See the structure of
[this example repository](https://github.com/fperez/mytoy). In fact, one can install the package with only
either `setup.py` or `pyproj.toml`, but the other files listed here are recommended:

- `pyproj.toml` (or `pyproject.toml`): this is a configuration file used by packaging tools. In the `mytoy` example it specifies to use `setuptools` to build and install the package.
- `setup.py`: this is run when the package is built and installed when using `setuptools`. In the example, it simply runs `setuptools.setup()`. With recent versions of
`setuptools`, you don't actually need this so long as you have the `pyproj.toml` file.
- `setup.cfg`: provides metadata about the package when using `setuptools`.
- `environment.yml`: provides information about the full environment in which your package should be used (including examples, documentation, etc.). For projects using `setuptools`, a minimal list of dependencies needed for installation and use of the package can instead be included in the `install_requires` option of `setup.cfg`.
- `LICENSE`: specifies the license for your package giving the terms under which others can use it.

The `postBuild` file is  a completely optional file only needed if you want to use the package with a MyBinder environment.

At the [numpy GitHub repository](https://github.com/numpy/numpy), by looking in  `pyproject.toml`, you can see that `numpy` is build and installed using a system called *Meson*,
while at the [Jupyter GitHub repository](https://github.com/jupyter/jupyter) you can see that the `jupyter` package is built and installed using `setuptools`.

*Building* a package usually refers to compiling source code but for a Python package that just has Python code, nothing needs to be compiled. *Installing* a package means putting the built package into a location on your computer where packages are installed.

You can also make your package public on PyPI or through Conda, but that is not something we'll cover here.

### Reproducibility and package management

For reproducibility, it's important to know the versions of the packages you use (and the version of Python).
`pip` and `conda` make it easy to do this. You can create a *requirements* file that captures the packages you are currently using (and, critically, their versions) and then install exactly that set of packages (and versions) based on that requirements file.

```bash
#| eval: false
pip freeze > requirements.txt
pip install -r requirements.txt

conda env export > environment.yml
conda env create -f environment.yml
```

Conda is a general package manager. You can use it to manage Python packages but lots of other software as well, including R and Julia.

Conda environments provide an additional layer of modularity/reproducibility, allowing you to set up a fully reproducible environment for your computation. Here (by explicitly giving `python=3.12`) the Python 3.12 executable and all packages you install in the environment are fully independent of whatever Python executables are installed on the system.

```bash
#| eval: false
conda create -n myenv python=3.12
source activate myenv
conda install numpy
```

!!! warning "Warning"
If you use `conda activate` rather than `source activate`, Conda will prompt you to run `conda init`, which will make changes to your `~/.bashrc` that, for one, activate the Conda base environment automatically when a shell is started. This may be fine, but it's helpful to be aware.
:::

### Package locations

Packages in Python (and in R, Julia, etc.) may be installed in various places
on the filesystem, and it sometimes it is helpful (e.g., if you end up with multiple
versions of a package installed on your system) to be able to figure out
where on the filesystem the package is being loaded from.

We can use the `__file__` and `__version__` objects in a package to see where on the filesystem a package is installed and what version it is:

```python
import numpy as np
np.__file__
np.__version__
```

(`pip list` or `conda list` will also show version numbers, for all packages.)

`sys.path` shows where Python looks for packages on your system.

### Source vs. binary packages

The difference between a *source* package and a *binary* package is that
the source package has the raw Python (and C/C++ and Fortran, in some cases) code
as text files, while the binary package has all the non-Python code in a
binary/non-text format, with the  C/C++ and Fortran code already having been
compiled.

If you install a package from source, C/C++/Fortran code will be compiled on your system
(if the package has such code).
That should mean the compiled code will work on your system, but requires you to have a
compiler available and things properly configured. A binary package doesn't need to be
compiled on your system, but in some cases the code may not run on your system because
it was compiled in such a way that is not compatible with your system.

Python *wheels* are a binary package format for Python packages. Wheels for some packages will vary by platform
(i.e., operating system) so that the package will install correctly on the system where it is being installed.

---

[← 2. Interacting with the operating system and external code and configuring Python](04-2-interacting-with-the-operating-system-and-external-code-an.md) · [Up: contents](index.md) · [4. Types and data structures →](06-4-types-and-data-structures.md)
