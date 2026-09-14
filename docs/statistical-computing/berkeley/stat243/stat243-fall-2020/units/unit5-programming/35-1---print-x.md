---
title: '[1] "{" "+" "<-" "print" "x"'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "{" "+" "<-" "print" "x"

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Is that result what you would expect? What does it say about my statement that using non-local variables is a bad idea?

**Closures** One way to avoid passing data by value is to associate data with a function, using a _closure_ . This is a functional programming way to achieve something like an OOP class. This Wikipedia entry nicely summarizes the idea, which is not an R-specific construct. This involves creating one (or more functions) within a function call and returning the function(s) as the output. When one executes the original function, the new function(s) is created and returned and one can then call that new function(s). The new function then can access objects in the enclosing environment (the environment of the original function) and can use ‘<<-‘ to assign into the enclosing environment, to which the function (or the multiple functions) have access. The nice thing about this compared to using a global variable is that the data in the closure is bound up with the function(s) and is protected from being changed by the user of the closure. Chambers provides an example of this in Sec. 5.4.

x <- **rnorm** (10) scaler_constructor <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } scaler <- **scaler_constructor** (x) **rm** (x) _# to demonstrate we no longer need x_ **scaler** (3)

59

---

[← Unit 05 — programming Part 34 —](34-unit-05-programming-part-34.md) · [Up: contents](index.md) · [Unit 05 — programming Part 36 — →](36-unit-05-programming-part-36.md)
