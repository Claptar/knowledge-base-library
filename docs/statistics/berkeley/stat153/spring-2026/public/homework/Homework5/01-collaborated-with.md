---
title: Collaborated with
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Collaborated with

## Student ID: {-}

## Collaborated with: {-}

Due May 7 at 11:59pm. Grading will be completed within 14 days of the late deadline (remember you have 120 late hours you can use across the semester).

*Instructions:* Please complete the homework by filling out this Jupyter notebook and exporting the final file as a PDF or .html file. (Go to File menu -> Save and Export Notebook as -> choose PDF or html, save, and upload this file as your submission.

You should ideally write out your solutions as markdown / LaTeX within this notebook. If you do decide to include any handwritten notes, these must be incorporated into one PDF (including all your code, solutions, etc) and each problem must be clearly labeled with the question number. Everything must be submitted as one single PDF. Points will be deducted if questions are not clearly labeled and formatting guidelines are not followed.

Remember, if you collaborated with anyone, you should list their names on this document, but your answers must be your own (unique, not a copy of/identical to a friend's). This homework will be graded for completion, so while you may use external tools to help you in completing it, it is recommended that you try to figure out the solutions and understand them yourself.

## Instructions:

Below is some helpful information for you as you solve these homework problems. "Part 0" will also cover some important intro material to help supplement what you saw in Lecture.

These models don't work well in the datahub, so you'll want to install pytorch on your own computer.

## Convolution output shape formula

For a 1D convolution with input length $L$, kernel size $k$, padding $p$, and stride $s$, the output length is

$$L_{\text{out}} = \left\lfloor \frac{L + 2p - k}{s} \right\rfloor + 1.$$

You may apply this over multiple independent batches and using different numbers of filters (with some kernel size).

For 2D, the same formula applies independently to each spatial dimension.

---

[Up: contents](index.md) · [Receptive field →](02-receptive-field.md)
