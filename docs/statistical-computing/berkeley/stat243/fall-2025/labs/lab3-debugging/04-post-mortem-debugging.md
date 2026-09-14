---
title: Post-mortem debugging
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab3-debugging.qmd
source_file: sources/berkeley-stat243/fall-2025/labs/lab3-debugging.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Post-mortem debugging

**Source:** [`labs/lab3-debugging.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab3-debugging.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

A usual workflow to debug a piece of code that is crashing is to run it, investigate the exact location where the crash happens, add a breakpoint statement and rerun the code. Oftentimes, the bug is not deterministic or only happens at certain iterations inside a loop, so a conditional breakpoint will have to be engineered. Post-mortem debugging simplifies such a workflow, sometimes drastically, by running the program until it crashes and automatically placing the user into a debugging session immediately before the crash. To enter post-mortem debugging automatically, a script that exits abnormally can be called via `python -m pdb myscript.py`. Alternatively, one may import `pdb` and call `pdb.pm()` after a function call crashes.

---

[← Integrated GUI debugger (with VS Code)](03-integrated-gui-debugger-with-vs-code.md) · [Up: contents](index.md) · [Acknowledgements →](05-acknowledgements.md)
