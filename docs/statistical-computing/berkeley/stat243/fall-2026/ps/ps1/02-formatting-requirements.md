---
title: Formatting requirements
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/ps/ps1.qmd
source_file: sources/berkeley-stat243/fall-2026/ps/ps1.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Formatting requirements

**Source:** [`ps/ps1.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/ps/ps1.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

1. Your electronic solution should be in the form of an Quarto file named `ps1.qmd`, with bash code chunks. Please see Lab 1, the Quarto and PS submission howtos on the course website, and the [dynamic documents tutorial](https://computing.stat.berkeley.edu/tutorial-dynamic-docs) for more information on how to do this. If you want to initial work in a Jupyter notebook, that is fine, but you'll need to run `quarto convert file.ipynb` to generate a qmd file before rendering to PDF and submitting.

2. Using chunks of bash code in Qmd may be troublesome:
  - Variables are not retained from bash chunk to bash chunk (i.e., state is not preserved between chunks), unlike with Python code chunks.
  - We can help troubleshoot and feel free to post on Ed.
  - **Test things out well before the due date with a dummy qmd file with a bash chunk to make sure things work.** We're quite happy to help in advance. We're not happy to help the night before the PS is due.

3. Your PDF submission to Pensive should be the PDF produced from your qmd. Your GitHub submission should include the qmd file and the final PDF, all named according to the [submission guidelines](https://stat243.berkeley.edu/fall-2026/howtos/submitPS.html).

4. Your solution should not just be shell code - you should have text describing how you approached the problem and what the various steps were. Your code should have comments indicating what each function or block of code does, and for any lines of code or code constructs that may be hard to understand, a comment indicating what that code does.

5. You do not need to (and should not) show exhaustive output, but in general you should show short examples of what your code does to demonstrate its functionality. Please see the [grading rubric](https://stat243.berkeley.edu/fall-2026/rubric.html), and note that the output should be produced as a result of the code chunks being run during the rendering process, not by copy-pasting of output from running the code separately (and definitely not as screenshots).

6. Using `sed` in a basic way as shown in the bash tutorial might be useful. You should not need to use more advanced functionality nor should you need to use `awk`, but you may if you want to.

---

[← Comments](01-comments.md) · [Up: contents](index.md) · [Problems →](03-problems.md)
