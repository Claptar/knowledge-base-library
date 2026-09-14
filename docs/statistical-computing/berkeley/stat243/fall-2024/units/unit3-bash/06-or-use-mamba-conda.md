---
title: or use Mamba/Conda
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit3-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# or use Mamba/Conda

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit3-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

```

You probably wouldn't want to use this code to accomplish this task in reality - you would want to see if there are  packages that can accomplish this. (In the R ecosystem, the `renv` and `packrat` packages do this for R projects.) The main point was to illustrate how one can quickly hack together some code to do fairly complicated tasks.

**Our sixth mission**: suppose I've accidentally started a bunch of jobs
(perhaps with a for loop in bash!) and need to kill them. (This example uses
syntax from the Managing Processes page of the bash tutorial, so it goes
beyond what you were asked to read for this Unit.)

```bash
#| eval: false

---

[← Create dummy test files without any spaces.](05-create-dummy-test-files-without-any-spaces.md) · [Up: contents](index.md) · [Use a 'here document' →](07-use-a-here-document.md)
