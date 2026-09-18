---
title: 'Assignment: regex problems'
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/regex.qmd
source_file: sources/berkeley-stat243/fall-2025/units/regex.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/regex.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/regex.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Assignment: regex problems

In the past, we've spent time learning how to create regular expressions. Regular expressions are something that AI tools seem to do quite well, so it's not clear to me at the moment to what extent we'll need to know the syntax of regular expressions in detail in the future.

Given that, you have two options for this assignment. If you'd like to get some experience with regular expression syntax and writing them, choose Option 1. If you don't think this seems useful to you and instead want to try using AI, choose Option 2.

As with the bash problems due on Monday, this is an assignment, not a problem set, so submit to Gradescope in any format you like.

## Option 1: Practicing with regular expressions

Read the [regular expression section of the bash shell tutorial](https://computing.stat.berkeley.edu/tutorial-using-bash/regex) and provide regular expression syntax to match the strings in the following scenarios. Any reasonable syntax is fine, and even better, challenge yourself to figure out multiple ways to answer each question.

1. Match the strings "dog", "Dog", "dOg", "doG", "DOg", etc. (The word 'dog' in any combination of lower and upper case.)
2. Match the strings "cat", "caat", "caaat", etc.
3. Match the strings "cat", "at", and "t".
4. Match two words separated by any amount of whitespace.

## Option 2: Using AI for regular expressions, with extensive testing

Skim through the [regular expression section of the bash shell tutorial](https://computing.stat.berkeley.edu/tutorial-using-bash/regex) to get a sense for the how they work without trying to absorb the syntax details.

Choose **one** of the following pattern matching exercises. First write an an extensive set of tests, with examples that should be matched and examples that should not be matched. Then use an AI tool (ChatBot or AI coding assistant) to produce a regular expression and run the regular expression using `grep` on your test cases.

- Match valid email addresses
- Match English words, including hyphenated and possessive words
- Match US phone numbers (or phone numbers from some other country)

---

[Up: contents](../index.md)
