---
title: "42. Good Practices, Debugging, and Reproducibility"
course: "Berkeley Stat 243"
chapter: 42
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 42. Good Practices, Debugging, and Reproducibility

## What this covers

This chapter is about writing Python code that survives contact with someone else — including
your own future self. It answers three practical questions that come up as soon as an assignment
or analysis grows past a few dozen lines: how should code be styled and structured so it doesn't
quietly accumulate bugs, how do you find a bug once one has appeared, and how do you organize a
project so that the result can be rerun, by you or anyone else, later? It assumes you can already
write basic Python — functions, loops, `if` statements — and have used a shell and a text editor or
IDE.

None of this is Python-specific in spirit; the same practices apply in R, in a shell script, or in
any language you end up using. Only the syntax of the examples is Python's.

## Code style and structure

Use an editor or IDE that understands the language you're writing (VS Code, Emacs, Sublime, vim,
or RStudio's built-in editor, which can also run Python). The concrete payoff is color-coded syntax,
automatic indentation, parenthesis matching, line numbers for locating bugs, and the ability to run
and debug code from inside the editor rather than by copy-pasting into a terminal.

For the code itself, the [PEP 8 style guide](https://peps.python.org/pep-0008) is the reference for
Python. A few points are worth calling out because they double as bug prevention:

- **Header and docstrings.** Put who/when/what metadata in a comment at the top of a file, and write
  a docstring for every public module, class, function and method. For non-public items a one-line
  comment after the `def` is enough.
- **Indentation and whitespace.** Python enforces indentation, which is a feature: it forces visual
  symmetry, and broken symmetry is often a sign of a bug. Use 4 spaces, not tabs. Put whitespace
  around operators and between arguments even when it isn't required for parsing — `a/y * x` is
  safer to read than `a/y*x`, because in a squeezed expression it's easy to lose track of the actual
  order of operations and introduce a bug without noticing.
- **Comments should earn their place.** Don't narrate the obvious (`x = x + 1 # increment x`).
  Do explain: what a block of code is for, any genuinely complicated piece of code (a hairy regular
  expression, say), and any constant whose value isn't self-explanatory. Comments should generally
  be full sentences, because you will not remember your own reasoning in six months any better than
  a stranger would.
- **Naming.** PEP 8's convention is `UpperCamelCase` for classes and `snake_case` for functions,
  methods and variables, with a leading underscore for non-public names. Names should be
  informative without being long, and should not shadow a built-in (`len`, for instance) — though
  Python's namespace system limits the damage when a clash is unavoidable. Functions should be named
  with verbs (`calc_loglik`, not `loglik` or `loglik_calc`), because a function is the verb of a
  program: it *does* something.
- **Line length and layout.** Keep code lines under about 79 characters and comment/docstring lines
  under 72. For a long pipeline of method calls, wrapping the whole expression in parentheses lets
  you split it across lines and comment each step:

  ```python
  newdf = (
      pd.read_csv('file.csv')
      .rename(columns={'STATE': 'us_state'})  # adjust column names
      .dropna()                                # remove some rows
  )
  ```

Beyond syntax, a few structural habits keep a project from becoming unmanageable:

- Break a task into core units, and write **reusable** code for each rather than lines that operate
  on one specific data object. A function's inputs and outputs are declared, so someone reading it
  doesn't have to read through the body to know what it does — a script that just runs top to bottom
  gives no such guarantee.
- Keep a single copy of each piece of logic (with version control, so you never need two files that
  are "almost" the same). Smaller functions are easier to debug, easier to understand, and compose
  the way UNIX utilities do.
- A function should be modular (one task), meaningfully named, and documented — purpose, inputs,
  outputs. Write a unit test for it.
- Don't hard-code numbers — even ones you're confident won't change, like `speed_of_light = 3e8` —
  because a named variable is more readable and more searchable than a bare literal repeated in
  several places.
- **Practice defensive programming**: check function inputs and warn if the code will do something
  the caller might not expect; give reasonable default arguments; document the valid range of
  inputs; check that the output is valid; and stop execution with an informative error message when
  a check fails. (Recall that in Python, an `if` condition is falsy only for `False`, `0`, `None`,
  or an empty list/tuple/string — everything else is truthy, including things you might not expect.)
- Avoid code that only works on one operating system. Have others review your code, and review
  theirs. And once a project's requirements have stabilized, consider a deliberate rewrite: code
  written while the plan was still moving often no longer fits the job it ends up doing.
- Break large software projects into separate files (roughly 2000–3000 lines each) with meaningful
  names, grouping related functions together.

For style specifically, a **linter** applies a tool to enforce these conventions automatically.
`ruff` (or `black`) will first flag syntax problems (`ruff check file.py`) and then reformat the file
to a consistent style (`ruff format file.py`). Running `diff` on the before/after shows what changed:
fixing an unspaced `=`, re-indenting a misplaced comment, adding a space around `*` — exactly the
kind of small inconsistency that is easy to introduce and easy to automate away.

## Assertions, exceptions, and testing

These three tools exist for the same reason: to make it hard for a bug to hide.

**Exceptions** are what Python raises when the syntax was fine but *running* the code failed — a
missing file, an unreachable URL, invalid input. There are two sides to using them. If you're
writing code whose job is to do something and it can't, you want it to fail loudly and informatively
— either by letting the exception it triggered propagate (perhaps with a clearer message attached),
or by explicitly detecting a bad situation and raising your own:

```python
def myfun(val):
    if val <= 0:
        raise ValueError("`val` should be positive")

myfun(-3)   # ValueError: `val` should be positive
```

The other side is when you want a piece of code to keep going even if something inside it fails —
for instance, a script downloading hundreds of URLs shouldn't necessarily stop because one of them
doesn't respond. Wrap the risky call in `try`/`except`:

```python
import os

def myfun(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
    except Exception as err:
        print(f"{err}\nCheck that the file `{filename}` can be found "
              f"in the current path: `{os.getcwd()}`.")
        return None
    return text.lower()
```

Sometimes you want to intercept an error just to add context, then let it propagate anyway —
`except ...: print(...); raise` (a bare `raise` re-raises the exception currently being handled).

**Assertions** are a quick way to raise `AssertionError` when a condition you expect to hold turns
out not to. They're aimed at development-time sanity checks — verifying pre- and post-conditions —
and can be disabled for production runs to recover the performance cost. A good assertion carries
a message that says what went wrong:

```python
number = -42
assert number > 0, f"number greater than 0 expected, got: {number}"
```

Common patterns: `assert x in y`, `assert x is not y`, `assert isinstance(x, sometype)`,
`assert all(x)`, `assert any(x)`. In a data-analysis pipeline, assertions are a natural place to
check that a dataset has the dimension you expect, or that no unexpected missing or extreme values
have crept in.

**Testing** is what assertions look like once you decide to keep them: instead of a check you type
interactively, you write it into a test file that anyone (including a CI system) can rerun. *Unit
tests* target one small piece of code, typically a single function — which is exactly what small,
modular functions make easy. The `pytest` package is the standard tool:

```python
import pytest
import numpy as np
import dummy

def test_numeric():
    assert dummy.add_one(3) == 4

def test_numpy_array():
    assert np.all(np.equal(dummy.add_one(np.array([3, 4])), np.array([4, 5])))

def test_bad_input():
    with pytest.raises(TypeError):
        dummy.add_one('hello')

def test_warning():
    with pytest.warns(UserWarning, match='complex'):
        dummy.add_one(1 + 3j)
```

`pytest test_dummy.py` runs the file; run with no argument at all and it searches the current
directory (and subdirectories) for anything with "test" in the name. A test suite is worth writing
even before the code it tests, in some people's practice — it clarifies what the code is supposed to
do, and it becomes a second form of documentation.

**Continuous integration (CI)** is running your tests automatically whenever the code changes,
rather than trusting that you remembered to run them locally. The standard mechanism is GitHub
Actions: a YAML file in `.github/workflows/` specifies when to run (e.g. on every push), how to set
up the environment, and what to run.

```yaml
on:
  push:
    branches:
    - main

jobs:
  CI:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: 3.12
    - name: Install package and pytest
      run: |
        pip install pytest
        pip install --user .
    - name: Run tests
      run: |
        cd mytoy
        pytest
```

When triggered, GitHub runs these steps in a fresh virtual machine (the *runner*), which is exactly
what catches the common failure mode of "it works on my machine."

## AI-assisted coding tools

IDEs now commonly integrate AI coding assistance directly — inline completion, accept/reject
suggestions, and a chat window with Chat/Edit/Agent modes that can rewrite or generate code from a
prompt, given files or a directory as context (GitHub Copilot and Gemini Code Assist as VS Code
extensions, or Cursor, which is built on VS Code). This is a faster workflow than copy-pasting from
a chatbot, but the caution is the same: don't accept a large chunk of generated code you don't
understand — it is still prone to bugs and hallucination, and code you don't understand is code you
can't maintain or debug. A reasonable hierarchy of trust: fine for straightforward syntax where
checking the output is enough (formatting a plot); usable for small, testable pieces (a regular
expression) where you can verify behavior; and for anything larger — real analysis or algorithm
code — you should check and understand it fully before relying on it.

## Version control

Use version control — git — even on a solo project; it is the nearest thing to a time machine you
will get. Pair it with an issue tracker (or at minimum a to-do file) for changes you want to make
later, and keep good commit messages alongside running notes on the project. Git itself is covered
in its own unit of this course.

## Debugging

### General strategies

- **Read the traceback from the bottom up.** The bottom line is usually the actual error; higher
  lines are the chain of calls that led there. Often it's less inscrutable than it looks once you
  read it carefully — and a web search on the exact error message (in quotes) is a legitimate first
  move.
- When an error occurs inside a nested chain of calls, the *call stack* is that chain, and the
  traceback shows it. Focus on the function that was executing when the error hit — but if that
  function isn't one you wrote, the actual mistake is usually in the arguments *your* code passed
  into the last function-you-wrote before the trace descends into library code.
- **Fix errors top-down** when several are reported at once: a cascade of errors is very often one
  root cause producing many symptoms.
- Check whether the bug is **reproducible** — does it happen the same way every time? Restarting the
  interpreter can reveal a scoping bug where code was accidentally relying on a global variable.
- If you can't localize the error from the message alone, use **bisection**: build the code up in
  pieces (or tear a failing version down in pieces) until you've isolated the smallest version that
  still fails.
- Code written as small, modular functions can be tested individually — the bug is usually in what
  gets passed between them.
- Failing that, fall back to print statements (the debugging strategy of the 1970s, still
  occasionally the right tool) or step through the code line by line — though line-by-line execution
  becomes impractical once the error is buried in nested calls, in scoping behavior, or inside
  compiled library code you can't step into.

### Using `pdb`

Python's `pdb` (with IPython's `ipdb` as a friendlier wrapper, and VS Code's built-in graphical
debugger as another option) can be entered in several ways: inserting `breakpoint()` at a point of
interest; calling `pdb.pm()` right after an exception to jump to where it occurred (`%debug` in
IPython/Jupyter does the same); running a function under `pdb.run()`; or starting the interpreter
itself under the debugger with `python -m pdb file.py`.

Here's the worked example from lecture: a function that fits a regression separately within each
stratum of some grouped data, with `breakpoint()` inserted at the line that builds the per-stratum
subset.

```python
import run_with_break as run
run.fit(run.data, run.n_cats)
```

```
> .../run_with_break.py(10)fit()
-> sub = data[data['cats'] == i]
(Pdb)
```

`n` runs the current line and stops at the next one; `c` continues to the next breakpoint (here, the
top of the next loop iteration, since `breakpoint()` sits inside the loop); `p i` prints a variable.
Stepping through every iteration by hand would be tedious, so instead it's more efficient to let the
code run and only stop once an error actually occurs — **post-mortem debugging**, via `pdb.pm()`
after the failure:

```python
import pdb
import run_no_break as run
run.fit(run.data, run.n_cats)
pdb.pm()
```

This drops you inside whatever internal function the error actually happened in — often a compiled
NumPy routine, which the debugger can't step into further. Typing `u` ("up") repeatedly walks back
up the call stack until you reach code you wrote:

```
(Pdb) u
> .../run_no_break.py(10)fit()
-> model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
```

and printing the variables at that frame reveals the actual problem:

```
(Pdb) p i
29
(Pdb) p sub
Empty DataFrame
Columns: [y, x, cats]
Index: []
```

Stratum 29 had no data in it — that's why fitting a regression to it failed. The bug wasn't in the
regression call; it was upstream, in whatever produced strata with zero observations.

Useful `pdb` commands: `h`/`help`, `l`/`list` (show surrounding code), `n`/`next`, `s`/`step` (step
*into* a call), `r`/`run` (finish the current function), `unt`/`until` (run to the next line, useful
for letting a loop finish), `c`/`continue`, `b`/`break` and `tbreak` (one-time breakpoint), `where`
(show the call stack), `u`/`up` and `d`/`down` (move through it), `p`/`print`, and `q`/`quit`. You
can also invoke `pdb.run("run.fit(...)")` (step in immediately with `s`), or set a breakpoint on a
line number or function name (`b 9`, `b fit`) when starting a module under `python -m pdb`, which
avoids editing the source to insert `breakpoint()`.

### Common causes of bugs

Parenthesis mismatches; `==` where `=` was meant; comparing floating-point numbers exactly with
`==` (dangerous, because they're only represented to finite precision — `1/3 == 4*(4/12 - 3/12)` is
`False`); expecting a scalar but getting an array back; silent type conversion where none was
wanted, or the reverse; using the wrong function or variable name; passing positional arguments in
the wrong order; and forgetting to define a variable inside a function, so that Python's lexical
scoping quietly reaches out to a global variable of the same name — which may work while you're
developing (because the global happens to exist) and break the moment you restart the interpreter.
Python also silently drops array or matrix dimensions that become redundant, which can confuse code
downstream that expected a particular shape.

### Tips for avoiding bugs

- **Defensive programming**, worked as a function: check the type, warn rather than silently
  producing nonsense, and raise where there's no sensible fallback.

  ```python
  import warnings

  def mysqrt(x):
      if isinstance(x, str):
          raise TypeError(f"What is the square root of '{x}'?")
      if isinstance(x, (float, int)):
          if x < 0:
              warnings.warn("Input value is negative.", UserWarning)
              return float('nan')   # avoid a complex result
          return x**0.5
      raise ValueError(f"Cannot take the square root of {x}")
  ```

- **Catch run-time errors with `try`/`except`** rather than letting one bad case kill a whole loop.
  Returning to the stratified-regression example: some strata may have too few observations to fit
  a model. Wrapping the fit in `try`/`except` lets the loop report the failure for that stratum and
  move on, instead of stopping the entire analysis:

  ```python
  params = np.full((n_cats, 2), np.nan)
  for i in range(n_cats):
      sub = data[data['cats'] == i]
      try:
          model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
          fit = model.fit()
          params[i, :] = fit.params.values
      except Exception as error:
          print(f"Regression cannot be fit for stratum {i}.")
  ```

  Here the stratum with no observations could have been checked for in advance; in general, though,
  you may have no cheap way to know ahead of time whether a call will fail.

- **Maintain dimensionality.** NumPy drops axes that become length-one, which is often convenient
  and occasionally the source of a bug:

  ```python
  mat = np.array([[1, 2], [3, 4]])
  np.sum(mat, axis=0)          # sums columns, as intended

  mat2 = mat[1, :]             # a 1-D row, not a 1x2 matrix
  np.sum(mat2, axis=0)         # sums *elements*, not columns — silently wrong shape

  if len(mat2.shape) != 2:
      mat2 = mat2.reshape(1, -1)
  ```

  It's easier to avoid ever dropping the dimension than to add checks everywhere downstream for
  whether it happened.

- **Find and avoid global variables.** Code that depends on a variable it didn't create or receive
  as an argument breaks whenever that global changes — often silently, because the person changing
  it doesn't know some function depends on it. A useful test is to delete the suspected global and
  see whether the function that used it still works:

  ```python
  del x   # simulate a fresh session

  def f(z):
      y = 3
      print(x + y + z)   # NameError once x is gone, if f relied on it being global

  f(2)
  ```

- **Miscellaneous**: prefer existing, well-tested library functionality over rewriting it; write
  small modular functions so you never debug the same logic twice; get the code *correct* before
  making it *efficient* (write the simple, obviously-correct version first — plain loops are fine —
  then optimize and check the two versions agree); plan for special cases in advance; write tests
  early; build up a program in small steps, checking after each one that nothing broke; and have
  someone else review the code, ideally while it's still being written.

### Tips for running long analyses

Save output at intermediate steps — including the random seed state, e.g. via `pickle.dump()` — so
a long job can be restarted rather than rerun from scratch if it or the machine fails partway.
Always run on a small subset of the problem first, to confirm the code works and saves what it
should, before setting off a job that will run for hours or days.

## Reproducible research

"Reproducible research" has become a live concern as research projects have grown more complex,
published papers have omitted enough detail to make replication difficult, and some published
results have simply failed to hold up (including, in some cases, outright fraud). *Provenance* —
being able to trace an analysis's steps back to its origin — is the underlying idea, and it splits
into two related but distinct properties:

- **Reproducibility**: a second person or group, using the *same* data, methods and code, gets the
  *exact same* result. This is harder than it sounds, and it gets harder as time passes — even for
  the original author.
- **Replicability**: a second person, using *new* data to answer the *same* scientific question,
  gets a *consistent* result.

An open question worth sitting with: what would it actually take for a piece of work to satisfy
either property, and where does that break down in practice?

### Basic strategies

- Give each project a directory with meaningfully named, standardized subdirectories — `code`,
  `data`, `paper` — following, for example, [JASA's template repository](https://github.com/jasa-acs/repro-template).
- Separate the pipeline into stages: a file for pre-processing, one or more for analysis, one for
  producing figures and tables — named so the order is obvious (`1-prep.py`, `2-analysis.py`,
  `3-figs.py`). Pre-processing that's expensive should write its output to a data file the analysis
  script reads in, rather than being rerun every time. The figure-producing code should read from a
  saved file of exactly the objects it needs (a pickle file, say) and reproduce the manuscript
  figures exactly — or the whole pipeline can be a Quarto or Jupyter document instead.
- Keep a running lab book: dated notes on what was done, where data came from and when, what
  pre-processing was applied, what each code file is for, and version numbers for the data with a
  description of what changed between them. Where possible, express any change to the data as code
  that transforms a fixed baseline dataset, rather than editing the data by hand.
- Record the software environment: OS version, language version, and package versions
  (`pip list`/`conda list` to see them, `pip freeze > requirements.txt` or
  `conda env export > env.yml` to capture them as something that can rebuild the environment
  elsewhere with `pip install -r requirements.txt` or `conda env create -f env.yml`). These files
  can embed operating-system-specific details that don't transfer cleanly across systems, but
  recording versions is still worth doing.

### Formal tools

- A complete workflow can sometimes live entirely inside one Quarto document or Jupyter notebook.
- Workflow/pipeline managers (e.g. the `make` utility, ordinarily used for compiling code, repurposed
  for reproducible pipelines; or tools such as Drake) can express the dependency structure between
  pipeline stages explicitly.
- A project can be organized as an installable Python or R package.
- Package management pins the versions of dependencies: Conda environments or virtualenvs for
  Python; `renv` or `packrat` for R (the once-popular `checkpoint` package no longer works, since it
  relies on CRAN snapshots that stopped being available after January 2023).
- When a project spans more than one language or tool, **containers** (Docker being the standard)
  package an entire software environment — versions and all — so it can be shared and rerun
  elsewhere; they underlie tools like GitHub Actions and the [Binder project](https://mybinder.org).
  Conda can often do a lighter-weight version of the same job when the dependencies are not
  Python-specific.

## Sources

- Fall 2025: [`units/unit4-goodPractices.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit4-goodPractices.qmd) —
  overview, "1. Good coding practices," "2. Debugging and recommendations for avoiding bugs," and
  "4. Reproducible research." This is the primary source for this chapter; it is the clearest and
  most recent version of the material (it adds the AI-assisted-coding-tools section and a note on
  operating-system portability of environment files that fall 2024 lacks).
- Fall 2024: the same four sections of
  [`units/unit4-goodPractices.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit4-goodPractices.qmd) —
  nearly identical to fall 2025; used to confirm which material is stable across offerings.
- Stat243 fall 2021: `units/unit4-goodPractices.pdf`, "1 Good coding practices" and
  "4 Reproducible research" — the R-flavored predecessor of the same unit. This file is a model
  reconstruction of a PDF with no text layer (marked `fidelity: reconstructed` in its front matter)
  and was used only to confirm that debugging and testing were, in that offering, deferred to a
  lab session rather than covered in the notes themselves — not as a source of new material.

**Not used here, and why:** the task also supplied fall 2026's `units/unit4-programming.qmd`
(overview plus sections on text manipulation and regex, reading data into Python, output, operating-
system interaction, modules and packages, types and data structures, programming paradigms, OOP,
functional programming, and memory and copies). In fall 2026 the course renumbered its units: good
coding practices, debugging and reproducibility moved to that year's Unit 3, while Unit 4 was
repurposed for general Python programming concepts that, in the 2024 and 2025 offerings, were taught
as a separate "Programming" unit with its own line-for-line matching set of topics. Reproducing that
material here would duplicate the treatment of the same lecture content given elsewhere from its
clearer, unabridged lineage; it is not covered in this chapter.

No slides, transcript, or exercises were supplied for this task — only these converted lecture
notes.

---

[← 41. Bash Shell Basics and Pipelines](41-bash-shell-basics-and-pipelines.md) · [Contents](index.md) · [43. Programming Language Mechanics →](43-programming-language-mechanics.md)
