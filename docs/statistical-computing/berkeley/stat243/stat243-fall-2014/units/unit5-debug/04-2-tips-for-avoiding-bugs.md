---
title: 2 Tips for avoiding bugs
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Tips for avoiding bugs

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Use core R functionality and algorithms already coded. Figure out if a functionality already exists in (or can be adapted from) an R package (or potentially in a C/Fortran library/package): code that is part of standard mathematical/numerical packages will probably be more efficient and bug-free than anything you would write.

2. Code in a modular fashion, making good use of functions, so that you don’t need to debug the same code multiple times. Smaller functions are easier to debug, easier to understand, and can be combined in a modular fashion (like the UNIX utilities).

3. Write code for clarity and accuracy first; then worry about efficiency. Write an initial version of the code in the simplest way, without trying to be efficient (e.g., you might use _for_ loops even if you’re coding in R); then make a second version that employs efficiency tricks and check that both produce the same output.

4. Plan out your code in advance, including all special cases/possibilities.

5. Write tests for your code early in the process.

6. Build up code in pieces, testing along the way. Make big changes in small steps, sequentially checking to see if the code has broken on test case(s).

7. Remove objects you don’t need, to avoid accidentally using values from an old object via the scoping rules.

8. Be careful that the conditions of _if_ statements and the sequences of _for_ loops are robust when they involve evaluating R code.

3

9. Don’t hard code numbers - use variables (e.g., number of iterations, parameter values in simulations), even if you don’t expect to change the value, as this makes the code more readable and reduces bugs when you use the same number multiple times:

speedOfLight <- 3e+08 nIts <- 1000

10. Check that inputs to and outputs from functions (either functions you call or functions you write) are valid and use _warning()_ and _stop()_ to give a warning or stop execution when something unexpected happens (see Section 5.5).

11. Use _try()_ with functions that may fail (see Section 5.5) in cases where you don’t want overall execution to fail because a single piece of the execution fails.

---

[← Unit 05 — debug Part 03 —](03-unit-05-debug-part-03.md) · [Up: contents](index.md) · [3 Debugging Strategies →](05-3-debugging-strategies.md)
