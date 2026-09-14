---
title: 4. bash shell challenges
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit3-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. bash shell challenges

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit3-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## 4.1 First challenge

Consider the file `cpds.csv`. How would you write a shell command
that returns "There are 8 occurrences of the word 'Belgium' in this file.",
where '8' should instead be the correct number of times the word occurs.

Extra: make your code into a function that can operate on any file
indicated by the user and any word of interest.

## 4.2 Second challenge

Consider the data in the `RTADataSub.csv` file. This is a subset of data
giving freeway travel times for segments of a freeway in an Australian
city. The data are from a kaggle.com competition. We want to try to
understand the kinds of data in each field of the file. The following
would be particularly useful if the data were in many files or the data
were many gigabytes in size.

1. First, take the fourth column. Figure out the unique values in that
column.
2. Next, automate the process of determining if any of the values are
non-numeric so that you don't have to scan through all of the unique
values looking for non-numbers. You'll need to look for the following
regular expression pattern `[^0-9]`, which is interpreted as NOT any
of the numbers 0 through 9.

Extra: do it for all the fields, except the first one. Have your code
print out the result in a human-readable way understandable by someone
who didn't write the code. For simplicity, you can assume you know
the number of fields.


## 4.3 Third challenge

1.  For Belgium, determine the minimum unemployment value (field #6) in
    `cpds.csv` in a programmatic way.
2.  Have what is printed out to the screen look like "Belgium 6.2".
3.  Now store the unique values of the countries in a variable, first
    stripping out the quotation marks.
4.  Figure out how to automate step 1 to do the calculation for all the
    countries and print to the screen.
5.  How would you instead store the results in a new file?


## 4.4 Fourth challenge

Let's return to the `RTADataSub.csv` file and the issue of missing values.

1. Using the data from `RTADataSub.csv`, create a new file without any rows that have an 'x' (which indicate a missing value).
2. Turn the code into a function that also prints out the number of rows that are being removed and that sends its output to stdout so that it can be used with piping.
3. Now modify your function so that the user could provide the missing value string and the input
filename.

## 4.5 Fifth challenge

Consider the `coop.txt` weather station file.

Figure out how to use `grep` to tell you the starting position of the state field.
Hints: search for a known state-country combination and figure out
what flags you can use with `grep` to print out the "byte offset" for the matched
state.

Use that information to automate the first mission where we extracted
the state field using `cut`. You'll need to do a bit of arithmetic using shell commands.

## 4.6 Sixth challenge

Here's an advanced one - you'll probably need to use `sed`, but the
brief examples of text substitution in the using bash tutorial (or in the demos above) should be
sufficient to solve the problem.

Consider a CSV file that has rows that look like this:

```
1,"America, United States of",45,96.1,"continental, coastal"
2,"France",33,807.1,"continental, coastal"
```

While Pandas would be able to handle this using `read_csv()`, using `cut`
in UNIX won't work because of the commas embedded within the fields. The
challenge is to convert this file to one that we can use `cut` on, as
follows.

Figure out a way to make this into a new delimited file in which the
delimiter is not a comma. At least one solution that will work for this
particular two-line dataset does not require you to use regular
expressions, just simple replacement of fixed patterns.

---

[← not clear how to sort by start time](11-not-clear-how-to-sort-by-start-time.md) · [Up: contents](index.md) · [5. Regular expressions →](13-5-regular-expressions.md)
