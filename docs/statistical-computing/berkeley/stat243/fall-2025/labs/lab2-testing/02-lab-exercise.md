---
title: Lab Exercise
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab2-testing.md
source_file: sources/berkeley-stat243/fall-2025/labs/lab2-testing.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Lab Exercise

**Source:** [`labs/lab2-testing.md`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab2-testing.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

1- Write a function in Python that finds a number in a string using regular expressions. The number can be positive or negative, integer-valued, or real, and numbers less than one can also be of the form 0.96 or .96. It can be assumed that no numbers appear in scientific notation. Refer to [String processing and regular expressions in Python](https://stat243.berkeley.edu/fall-2025/units/unit5-programming.html#string-processing-and-regular-expressions-in-python) for a quick overview of Python's `re` package. You may use AI to generate the regex, but be sure you understand the output.

2- Write an interface for that function (a function name and arguments), but do not implement the function yet (you can have it return an `None`, or an empty string for now). We will do this in a good old fashioned .py file (not a notebook or a quarto file).

3- Build a test suite using the `pytest` package to test that your function works as intended. Add at least 8 test cases with justification for each. Try to cover the main use cases, and as many potential corner cases or boundary conditions as possible.

4- Now run the test suite. It should fail for all your tests (unless one of them was passing an empty string).

5- Implement the function. You can do this at one go, or case by case. As you implement a case, you can rerun the test suite and see some of the tests relevant to that cases stopping to fail. When all the tests pass, you are done. This is called test-driven development.

6- If some cases are still failing, that's alright, for the purposes of this lab we don't need to ensure all edge cases are dealt with.

7- Make sure you raise an exception to trap invalid input types.

8- Add a test to check that an exception is properly raised when the function is given invalid input types.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Acknowledgements →](03-acknowledgements.md)
