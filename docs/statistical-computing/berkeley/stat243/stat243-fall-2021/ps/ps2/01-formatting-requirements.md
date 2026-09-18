---
title: Formatting requirements
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/ps2.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/ps/ps2.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`ps/ps2.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/ps2.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Formatting requirements

September 8, 2021

## Comments:

- This covers material in Units 3 and 4.
- It's due at 10 am on September 17, both submitted as a PDF to Gradescope as well as committed to your GitHub repository as documented in the howtos/submitting-electronically.txt file.
- Please note my comments in the syllabus about when to ask for help and about working together. In particular, please give the names of any other students that you worked with on the problem set and indicate in the text or in code comments any specific ideas or code you borrowed from another student.

1. Your electronic solution should be in the form of an R markdown file named ps2.Rmd or a $\text{\LaTeX}$+knitr file named ps2.Rtex, with bash and R code chunks included in the file (or read in from a separate code file).
Please see the dynamic documents tutorial or Lab 1 materials for more information on how to do this, including dealing with bash code chunks and line breaks.

2. Your PDF submission should be the PDF produced from your Rmd/Rtex. Your GitHub submission should include the Rtex/Rmd file, any code files containing chunks that you read into your Rtex/Rmd file, and the final PDF, all named according to the guidelines in howtos/submitting-electronically.txt.

3. Note that using chunks of bash code in Rmd/Rtex/Rnw can sometimes be troublesome, particularly on Windows machine. Some things to try if you are having trouble: (a) set the terminal to be the Ubuntu subsystem if you are on Windows; (b) if using RStudio, you may only be able to run bash chunks if you have the notebook mode on; (c) using single versus double quotes in your Rmd/Rtex document may make a difference. If you can't produce a PDF that includes the bash chunk output, feel free to not run those chunks and just paste in the output you get manually. Please post on Piazza if you have trouble.

4. You will probably need to use *sed* in a basic way as we have used it so far in class and in the tutorial on bash. You should not need to use more advanced functionality nor should you need to use *awk*, but you may if you want to.

5. Your solution should not just be code - you should have text describing how you approached the problem and what the various steps were.

6. Your code should have comments indicating what each function or block of code does, and for any lines of code or code constructs that may be hard to understand, a comment indicating what that code does. You do not need to show exhaustive output but in general you should show short examples of what your code does to demonstrate its functionality.

---

[Up: contents](index.md) · [Problems →](02-problems.md)
