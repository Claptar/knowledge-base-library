---
title: Practice problems
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Practice problems

**Source:** [`labs/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Although it is not required to code in this manner, we are going to practice working in a test-driven format.  It is a coding practice where you first write the tests, then write a function that will pass those tests, and update the function and tests as needed.   Coding in this way is called [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development).

Suppose we want to write a function `calculator(x, y, operation)` that takes in two numbers `x` and `y` as well as a string `operation` indicating whether to perform addition, subtraction, multiplication, or division.  This function should return a numeric value.

1. Write a test that will check whether `calculator` (which you have not written yet) returns an error when `x` and `y` are not numeric and when `operation` is not in the expected set of operations (i.e. addition, subtraction, multiplication, and division). Save these tests in a file called `tests-calculator.R`.  Hint: use the expectation `expect_error()`.  You may want to write custom error messages in your assertions.

2. Start writing your `calculator` function to pass the tests written in 1).  Use the `assertthat` package to produce errors if `x` or `y` are not numeric or when `operation` is not in the expected set of operations.  You can choose what you expect the user to call each operation in the function.  Save this function as `calculator.R`

3. Use the `test_files("tests-calculator.R")` to see if your function is operating as you hope. Note this assumes you are in the directory that holds `tests-calculator.R`.

4. Write a test that checks whether the addition piece of your calculator produces the correct results with the following input:

    1. `x = 1` and `y = 9`
    2.  `x = 100`, `y = -5`
Also, check that the value returned is a scalar.  Save these tests in a file called `tests-calculator.R`.  If you think of any other tests feel free to add them.

5. Add the addition functionality to `calculator()` and call `test_files("tests-calculator.R")` again.

6. Continue iterating through this process for substraction, multiplication, and division.  Make sure your function elegantly handles division when the demoninator is 0.

7.  If you have time, add new functionality to your calulator (e.g. square root).

---

[← run from R console](13-run-from-r-console.md) · [Up: contents](index.md) · [Acknowledgements →](15-acknowledgements.md)
