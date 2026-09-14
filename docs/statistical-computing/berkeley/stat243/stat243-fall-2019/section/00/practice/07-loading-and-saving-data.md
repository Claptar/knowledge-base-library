---
title: Loading (and saving) data
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/00/practice.tex
source_file: sources/berkeley-stat243/stat243-fall-2019/section/00/practice.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Loading (and saving) data

**Source:** [`section/00/practice.tex`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/00/practice.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

1.  Load the earnings data (e.g., `section/00/data/heights.dta`) from the 2019 github repository. Don’t copy the data to your current working directory or change your current working directory in R. In other words, you will have to either specify the full path to the file or the relative path from your current location. Save the result as `earnings`.

    1.  What does `class(earnings)` return?

    2.  What does `str(earnings)` return?

    3.  What does `length(earnings)` return?

    4.  What does `dim(earnings)` return?

    5.  Use `sapply` to find the class of each column of `earnings`.

    6.  Use `sapply` to call `summary` on just the two height-related columns of `earnings`.

    7.  Make a boxplot with just the two height-related columns of `earnings`. Give it a title.

    8.  Make a histogram of `earnings$yearbn`. Make sure the y-axis is a density not a count. Change the title and the label on the x-axis. Change the title and the label on the x-axis.

2.  Make sure you remember how to load CSV (e.g., `section/00/data/cpds.csv`) and text files with white space separators (e.g., `section/00/data/stateIncome.txt`).

3.  Saving R objects

    1.  Use `ls()` to examine the objects in your working environment

    2.  Save some of those objects to a R data file in the directory above whereever your are currently located

    3.  Open a new R prompt (you may want to open a new terminal and leave the one you are currently using alone)

    4.  From your new R prompt, verify that you don’t have any objects in your working environment

    5.  Load the R data file you saved previously

    6.  Use `ls()`, `class()`, `str()`, `names()`, and anything else you can think of to exam the R objects you loaded

---

[← Functions](06-functions.md) · [Up: contents](index.md)
