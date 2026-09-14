---
title: Debugging
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/lab3-debugging.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/labs/lab3-debugging.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Debugging

**Source:** [`labs/lab3-debugging.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/lab3-debugging.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

Today we're going to explore the concept of debugging and some of the tooling that allows for debugging python code.

It's widely recognized and accepted that any sizeable code base will have a non-trivial number of bugs (where does the term come from?). The main goal of testing is to make sure the main expected cases are behaving correctly.

Sometime you code doesn't do what you expect or want it to do, and it's not clear just by reading through it, what the problem is.

In interpreted languages (esp. those with interactive shells like python) one can sometimes run the code piece by piece and inspect the state of the variables.

If the code involves a loop or a function, a common practice is to judiciously place a few print statements that dump the state of some variables to the terminal so that you can spot the problem by tracing through it.

When the code involves multiple functions and complex state, this strategy starts to break down. This is where you start rolling up your sleeves and invoking a debugger!

Debugging can be a slow process, so you typically start a debugging session by deciding which line in your code you would like to start tracing the behavior from, and you place a breakpoint. Then you can have the debugger run the program up to that point and stop at it, allowing you to:

1- inspect the current state of variables
2- step through the code line by line
3- step over or into functions as they are called
4- resume program execution

---

[Up: contents](index.md) · [advanced debugging →](02-advanced-debugging.md)
