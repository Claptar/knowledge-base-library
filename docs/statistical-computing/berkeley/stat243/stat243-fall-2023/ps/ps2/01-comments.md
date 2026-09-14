---
title: Comments
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/ps/ps2.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/ps/ps2.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Comments

**Source:** [`ps/ps2.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/ps/ps2.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

- This covers material in Units 3 and 4.
- It's due at 10 am (Pacific) on September 15, both submitted as a PDF to Gradescope as well as committed to your GitHub repository.
- Please see PS1 for formatting and attribution requirements.
- Note that using chunks of bash code in Qmd may be troublesome.
  - You will need to add `engine: knitr` to the YAML preface of your qmd document. The `jupyter` engine won't work unless you install the Jupyter bash kernel, and even then you can't mix bash and Python code chunks.
  - For the `knitr` engine, you'll need to have R installed on your computer, including the `knitr` package. Quarto will then process the code chunks through `knitr` (which will use the `reticulate` package to handle Python chunks).
  - If you have trouble on your own computer, you can always render your solution for this problem set on an SCF machine (we won't generally use bash chunks in future problem sets). (In particular I'm not quite sure what will happen if you render on Windows.)
  - We can help troubleshoot and feel free to post on Ed.
- You will probably need to use `sed` in a basic way as we have used it so far in class and in the bash tutorial. You should not need to use more advanced functionality nor should you need to use `awk`, but you may if you want to.

---

[Up: contents](index.md) · [Problems →](02-problems.md)
