---
title: or use Mamba/Conda
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit3-bash.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# or use Mamba/Conda

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

```

You probably wouldn't want to use this code to accomplish this task in reality - you would want to see if there are  packages that can accomplish this. (In the R ecosystem, the `renv` and `packrat` packages do this for R projects.) The main point was to illustrate how one can quickly hack together some code to do fairly complicated tasks.

**Our sixth mission**: suppose I've accidentally started a bunch of jobs
(perhaps with a for loop in bash!) and need to kill them. (This example uses
syntax from the Managing Processes page of the bash tutorial, so it goes
beyond what you were asked to read for this Unit.)

```bash
#| eval: false

---

[← create dummy test files without any spaces](04-create-dummy-test-files-without-any-spaces.md) · [Up: contents](index.md) · [use a 'here document' →](06-use-a-here-document.md)
