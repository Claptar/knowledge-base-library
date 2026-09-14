---
title: Introduction
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab2-testing.md
source_file: sources/berkeley-stat243/fall-2024/labs/lab2-testing.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`labs/lab2-testing.md`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab2-testing.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Today we will spend some time getting familiar with some of the programming tools that can help make your code more robust and resilient to errors and boundary conditions - tools like unit tests and exceptions (and next week we will spend some time on debugging misbehaving code).

Testing is what you do when you finish implementing a piece of code and want to try it out to see if it works. Running your code manually and seeing if it works is a workable strategy for simple one-time scripts that do simple tasks, but there are situations (like writing a function that others will repeatedly use, or like running the same piece of code on hundreds of files or URLs) where it is prudent to test your code ahead of its actual use or deployment. In today's lab, we are going to use `pytest` to test for correct behavior and verify that exceptions are raised in the right situations.

---

[Up: contents](index.md) · [Lab Exercise →](02-lab-exercise.md)
