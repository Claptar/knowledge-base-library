---
title: advanced debugging
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/lab3-debugging.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/labs/lab3-debugging.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# advanced debugging

**Source:** [`labs/lab3-debugging.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/lab3-debugging.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

Some bugs are really tricky to catch. Those are typically the bugs that happen very rarely, and in unclear circumstances. In statistical computing and data analysis settings these might be conditions that happen in iterative algorithms sometimes, but not very often, and can be hard to reproduce.

One way to deal with these bugs is to start the debugging session with placing one or more **conditional** breakpoints. These are similar to regular breakpoints but are not going to cause the debugger to stop the execution of the program and hand you the controls unless a specific condition (that you specify) evaluates to true as the program is executing that particular line of code. You may use some conditions that are similar to what you would place in an assert statement (conditions that shouldn't happen) or any other conditions that you think may be associated with the occurrence of the anomalous behavior your are debugging.

---

[← Debugging](01-debugging.md) · [Up: contents](index.md) · [Integrated GUI debugger (with VS Code) →](03-integrated-gui-debugger-with-vs-code.md)
