---
title: Comments
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/ps/ps2.qmd
source_file: sources/berkeley-stat243/fall-2025/ps/ps2.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Comments

**Source:** [`ps/ps2.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/ps/ps2.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

- This covers material in Units 3 and 4.
- It's due at 10 am (Pacific) on September 19, both submitted as a PDF to Gradescope as well as committed to your GitHub repository.
- Please see PS1 for formatting and attribution requirements.
- Note that using chunks of bash code in Qmd may be troublesome.
  - You will need to add `engine: knitr` to the YAML preface of your qmd document (as seen in `unit2-dataTech.qmd` in the class repository). The default `jupyter` engine won't run both bash and Python chunks in the same document because Jupyter notebooks are associated with a single 'kernel' (i.e., a single language for the code chunks).
  - For the `knitr` engine, you'll need to have R installed on your computer, including the `knitr` package. Quarto will then process the code chunks through `knitr` (which will use R's `reticulate` package to handle Python chunks).
  - If you have trouble on your own computer, you can always render your solution for this problem set on an SCF machine (we won't generally use bash chunks in future problem sets). (In particular I'm not quite sure what will happen if you render on Windows.)
  - You can control which installed Python is used by the `knitr` engine using the syntax shown in the first code chunk of `unit2-dataTech.qmd`. This will work on the SCF as well as on your laptop (for the latter, you'll of course need to point to a `python` (or `python3`) on your machine.
  - We can help troubleshoot and feel free to post on Ed.
  - **Test things out well before the due date with a dummy qmd file with both a bash chunk and a Python chunk and make sure things work.**
- Using `sed` in a basic way as shown in the bash tutorial might be useful. You should not need to use more advanced functionality nor should you need to use `awk`, but you may if you want to.

---

[Up: contents](index.md) · [Problems →](02-problems.md)
