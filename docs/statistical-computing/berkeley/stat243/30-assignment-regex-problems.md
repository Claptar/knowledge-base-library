---
title: "30. Assignment: regex problems"
course: "Berkeley Stat 243"
chapter: 30
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 30. Assignment: regex problems

## What this covers

This chapter is the course's own practice assignment on regular expressions, given in both the
fall-2024 and fall-2025 offerings of Stat 243. It does not itself teach regular-expression syntax;
it assumes the reader has already worked through the regular-expression section of the course's
bash shell tutorial (linked below), and asks the reader to write patterns for a short list of
matching problems.

## Why regex, and two routes through it

The fall-2025 version of the assignment opens with a reflection worth keeping: regular expressions
are something AI tools now seem to handle quite well, so it is not clear how much of the syntax
still needs to be known by hand. Given that, the fall-2025 assignment offers a choice of two
routes, while the fall-2024 assignment only gave the first:

- **Option 1** — write the regular expressions yourself, matching strings directly. This is the
  whole of the original (fall-2024) assignment.
- **Option 2** — treat the exercise as a testing problem rather than a syntax problem: write an
  extensive set of test strings that should and should not match, then have an AI tool produce a
  candidate regular expression, and check it against the tests with `grep`.

Both routes point first to the same background reading: the regular-expression section of the
course's bash shell tutorial, which explains the syntax needed for the problems below and is not
reproduced here.

## Exercises

### Option 1 — writing the regular expressions directly

Read the regular-expression section of the bash shell tutorial, then give regular-expression
syntax matching each of the following. Any reasonable syntax is fine — try to find more than one
way to answer each one.

1. The word "dog" in any combination of upper and lower case: "dog", "Dog", "dOg", "doG", "DOg",
   and so on.
2. The strings "cat", "caat", "caaat", and so on.
3. The strings "cat", "at", and "t".
4. Two words separated by any amount of whitespace.

### Option 2 — using an AI tool, with your own tests first

(Fall-2025 only.) Skim the same tutorial section to get a general sense of how regular expressions
work, without trying to absorb the syntax in detail. Then choose **one** of the following matching
problems:

- Valid email addresses.
- English words, including hyphenated and possessive forms.
- US phone numbers (or phone numbers from another country of your choice).

For the chosen problem, first write an extensive set of test cases — examples that should match
and examples that should not. Then use an AI chatbot or coding assistant to produce a regular
expression for the problem, and run it against your test cases with `grep` to check it.

## Sources

- Assignment framing and the four Option-1 problems: `berkeley-stat243` fall-2024,
  `units/regex.qmd`, and fall-2025, `units/regex.qmd` — the four problems are identical across
  both years.
- The "why regex vs. AI" framing, the Option 1/Option 2 split, and the three Option-2 matching
  problems: `berkeley-stat243` fall-2025, `units/regex.qmd` only (not present in fall-2024).
- Referred to but not contained in either source: the regular-expression section of the course's
  bash shell tutorial — linked as
  <https://berkeley-scf.github.io/tutorial-using-bash/regex> in the fall-2024 assignment and
  <https://computing.stat.berkeley.edu/tutorial-using-bash/regex> in the fall-2025 assignment.
  This is where the regular-expression syntax needed for the problems above is actually explained;
  it is not part of the supplied material.

---

[← 29. Installing R & RStudio](29-installing-r-rstudio.md) · [Contents](index.md) · [31. Working on the SCF Cluster →](31-working-on-the-scf-cluster.md)
