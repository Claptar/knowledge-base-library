---
title: Formatting requirements
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/ps2.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/ps/ps2.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Formatting requirements

**Source:** [`ps/ps2.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/ps2.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Your electronic solution should be in the form of an R markdown file named _ps2.Rmd_ or a L<sup>A</sup> TEX+knitr file named _ps2.Rtex_ , with bash and R code chunks included in the file (or read in from a separate code file).

Please see the _dynamic documents_ tutorial or Lab 1 materials for more information on how to do this, including dealing with bash code chunks and line breaks.

2. Your PDF submission should be the PDF produced from your Rmd/Rtex. Your GitHub submission should include the Rtex/Rmd file, any code files containing chunks that you read into your Rtex/Rmd file, and the final PDF, all named according to the guidelines in _howtos/submitting-electronically.txt_ .

3. Note that using chunks of bash code in Rmd/Rtex/Rnw can sometimes be troublesome, particularly on Windows machine. Some things to try if you are having trouble: (a) set the terminal to be the Ubuntu subsystem if you are on Windows; (b) if using RStudio, you may only be able to run bash chunks if you have the notebook mode on; (c) using single versus double quotes in your Rmd/Rtex document may make a difference. If you can’t produce a PDF that includes the bash chunk output, feel free to not run those chunks and just paste in the output you get manually. Please post on Piazza if you have trouble.

4. You will probably need to use _sed_ in a basic way as we have used it so far in class and in the tutorial on bash. You should not need to use more advanced functionality nor should you need to use _awk_ , but you may if you want to.

5. Your solution should not just be code - you should have text describing how you approached the problem and what the various steps were.

1

6. Your code should have comments indicating what each function or block of code does, and for any lines of code or code constructs that may be hard to understand, a comment indicating what that code does. You do not need to show exhaustive output but in general you should show short examples of what your code does to demonstrate its functionality.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Problems →](03-problems.md)
