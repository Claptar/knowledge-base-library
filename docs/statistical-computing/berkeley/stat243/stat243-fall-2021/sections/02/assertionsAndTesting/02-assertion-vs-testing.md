---
title: Assertion vs. Testing
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/02/assertionsAndTesting.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sections/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Assertion vs. Testing

Assertions check the internal state of a function.  For example, consider a function ```add(x, y)``` which returns ```x + y```.  The function assumes ```x```  is numeric, and an assertion would confirm that this is in the case and return as error if not.  On the other hand, tests check that a function produces the expected output for various inputs.  For example, ensuring that ```add(1, 2)``` returns the number 3.  Tests may include checks that assertions are working properly.

Tests and assertions are similar in that,

- Both are part of ensuring programs run correctly and aspects of defensive programming.
- Both should check small pieces of the code while providing useful error messages, so they tell you exactly where the issue arises.

A couple of important differences between assertions and tests are below:

| Assertions                                                               | Testing                                        |
|--------------------------------------------------------------------------|------------------------------------------------|
| Depends only on the object and method parameters.                        | Can depend on global variables.                |
| Document function properties that are not public.                        | Can only check externally visible properties.  |
| Work with live data, so check cover infinitely many cases.               | Test a small number of cases.                  |
| Excecuted in function calls, so amount of computation should be limited. |                                                |

---

[← References and useful links](01-references-and-useful-links.md) · [Up: contents](index.md) · [Assertions and assertthat →](03-assertions-and-assertthat.md)
