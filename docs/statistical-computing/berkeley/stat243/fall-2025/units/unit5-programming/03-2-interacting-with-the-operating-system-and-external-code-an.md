---
title: 2. Interacting with the operating system and external code and configuring
  Python
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Interacting with the operating system and external code and configuring Python

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Interacting with the operating system

Scripting languages allow one to interact with the operating system in various ways.
Most allow you to call out to the shell to run arbitrary shell code and save results within your session.

I'll assume everyone knows about the following functions/functionality for interacting with the filesystem and file
in Python: `os.getcwd`, `os.chdir`, `import`, `pickle.dump`, `pickle.load`

Also in IPython there is additional functionality/syntax.

Here are a variety of tools for interacting with the operating system:

-   To run UNIX commands from within Python, use `subprocess.run()`, as follows,
    noting that we can save the result of a system call to an Python object:

    ```python
    import subprocess, io
    subprocess.run(["ls", "-al"])   ## results apparently not shown when compiled...
    files = subprocess.run(["ls", "-al"], capture_output = True)
    files.stdout
    with io.BytesIO(files.stdout) as stream:  # create a file-like object
         content = stream.readlines()
    content[2:4]
    ```

-   There are also a bunch of functions that will do specific queries of
    the filesystem, including

    ```python
    os.path.exists("unit2-dataTech.qmd")
    os.listdir("../data")
    ```

-   There are some tools for dealing with differences between operating
    systems. `os.path.join` is a nice example:

    ```python
    os.listdir(os.path.join("..", "data"))
    ```

    It's best if you can to write your code, as shown here with `os.path.join`, in a way that is *agnostic* to the underlying operating system (i.e., that works regardless of the operating system).

-   To get some info on the system you're running on:

    ```python
    import platform
    platform.system()
    os.uname()
    platform.python_version()
    sys.version
    ```

-   To retrieve environment variables:
    ```python
    os.environ['PATH']
    ```

-   You can have an Python script act as a shell script (like running a bash
    shell script) as follows.

    1.  Write your Python code in a text file, say `example.py`
    2.  As the first line of the file, include `#!/usr/bin/python`
        (like `#!/bin/bash` in a bash shell file, as seen in Unit 2) or
        for more portability across machines, include
        `#!/usr/bin/env python`.
    3.  Make the Python code file executable with `chmod`:
        `chmod ugo+x example.py`.
    4.  Run the script from the command line: `./example.py`

    If you want to pass arguments into your script, you can do so with the
    `argparse` package.

    ```python
    #| eval: false
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', default=2002,
                        help='year to download')
    parser.add_argument('-m', '--month', default=None,
                        help='month to download')
    args = parse.parse_args()
    args.year
    year = int(args.year)
    ```

    Now we can run it as follows in the shell:

    ```bash
    #| eval: false
    ./example.py 2004 January
    ```

-   Use `Ctrl-C` to interrupt execution. This will generally back out
    gracefully, returning you to a state as if the command had not been
    started. Note that if Python is exceeding the amount of memory available, there can
    be a long delay. This can be frustrating, particularly since a
    primary reason you would want to interrupt is when Python runs out of
    memory.


## Interacting with external code

Scripting languages such as R, Python, and Julia allow you to call out to "external code",
which often means C or C++ (but also Fortran, Java and other languages).

Calling out to external code is particularly important in languages like R and Python that are often much slower
than compiled code and less important in a fast language like Julia (which uses Just-In-Time compilation -- more on that later).

In fact, the predecessor language to R,
which was called 'S' was developed specifically (at AT&T's Bell Labs in the 1970s and 1980s) as an interactive
wrapper around Fortran, the numerical programming language most commonly used at the time (and still widely relied on today in various legacy codes).

In Python, one can [directly call out to C or C++ code](https://docs.python.org/3/extending/extending.html) or one can use *Cython* to interact with C. With Cython, one can:

  - Have Cython automatically translate Python code to C, if you provide type definitions for your variables.
  - Define C functions that can be called from your Python code.

In R, one can call directly out to C or C++ code using *.Call* or one can use the [Rcpp package](https://adv-r.hadley.nz/rcpp.html). *Rcpp* is specifically designed to be able to write C++ code that feels somewhat like writing R code and where it is very easy to pass data between R and C++.

---

[← 1. Text manipulation, string processing and regular expressions (regex)](02-1-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [3. Modules and packages →](04-3-modules-and-packages.md)
