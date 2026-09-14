---
title: 1 Common syntax errors and bugs
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Common syntax errors and bugs

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some of these are not specific to R, though some are.

1. Parenthesis mis-matches

2. _[[. . .]]_ vs. _[. . .]_

3. _==_ vs. _=_

4. Comparing real numbers exactly using ’ _==_ ’ is dangerous (more in a later Unit). Suppose you generate _x = 0.333333_ in some fashion with some code and then check: x == 1/3 # FALSE is the result

1

5. Vectors vs. single values:

   - (a) || vs. _|_ and _&&_ vs. _&_

   - (b) You expect a single value but your code gives you a vector

   - (c) You want to compare an entire vector but your code just compares the first value (e.g., in an _if_ statement) – consider using _identical()_ or _all.equal()_

6. Silent type conversion when you don’t want it, or lack of coercion where you’re expecting it

7. Using the wrong function or variable name

8. Giving unnamed arguments to a function in the wrong order

9. In an if-then-else statement, the _else_ cannot be on its own line (unless all the code is enclosed in {}) because R will see the if-then part of the statement, which is a valid R statement, will execute that, and then will encounter the _else_ and return an error. We saw this in Unit 4.

10. Forgetting to define a variable in the environment of a function and having the function, via lexical scoping, get that variable as a global variable from one of the enclosing environments. At best the types are not compatible and you get an error; at worst, you use a garbage value and the bug is hard to trace. In some cases your code may work fine when you develop the code (if the variable exists in the enclosing environment), but then may not work when you restart R if the variable no longer exists or is different.

11. R (usually helpfully) drops matrix and array dimensions that are extraneous; which can sometimes confuse later code that expects an object of a certain dimension. The ’[’ operator takes an additional optional argument that can avoid dropping dimensions.

mat <- **matrix** (1:4, 2, 2)[1, ] **dim** (mat) ## NULL **print** (mat) ## [1] 1 3 **colSums** (mat)

2

**## Error: ’x’ must be an array of at least two dimensions**

mat <- **matrix** (1:4, 2, 2)[1, , drop = FALSE]

**colSums** (mat)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Unit 05 — debug Part 03 — →](03-unit-05-debug-part-03.md)
