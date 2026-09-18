---
title: Loading (and saving) data
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/RPractice/R-practice.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`sections/RPractice/R-practice.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Loading (and saving) data

1. Load the earnings data (e.g., `sections/01/data/heights.dta`) from the 2020 Github repository. Don't copy the data to your current working directory or change your current working directory in R to the directory with the data. In other words, you will have to either specify the full path to the file or the relative path from your current location. Save the result as `earnings`.
   (a) What does `class(earnings)` return?
   (b) What does `str(earnings)` return?
   (c) What does `length(earnings)` return?
   (d) What does `dim(earnings)` return?
   (e) Use `sapply` to find the class of each column of `earnings`.
   (f) Use `sapply` to call `summary` on just the height-related columns of `earnings`.

2. Make sure you remember how to load CSV (e.g., `sections/01/data/cpds.csv`) and text files with white space separators (e.g., `sections/01/data/stateIncome.txt`).

3. Saving R objects
   (a) Use `ls()` to examine the objects in your working environment
   (b) Save some of those objects to a R data file in the directory above whereever your are currently located
   (c) Open a new R prompt (you may want to open a new terminal and leave the one you are currently using alone)
   (d) From your new R prompt, verify that you don't have any objects in your working environment
   (e) Load the R data file you saved previously
   (f) Use `ls()`, `class()`, `str()`, `names()`, and anything else you can think of to exam the R objects you loaded

---

[← Functions](02-functions.md) · [Up: contents](index.md)
