---
title: 4. bash shell challenges
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit3-bash.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit3-bash.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. bash shell challenges

**Source:** [`units/unit3-bash.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit3-bash.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## 4.1 First challenge

Consider the file *cpds.csv*. How would you write a shell command
that returns "There are 8 occurrences of the word 'Belgium' in this file.",
where '8' is actually the correct number of times the word occurs.

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
3. Now, do it for all the fields, except the first one. Have your code
print out the result in a human-readable way understandable by someone
who didn't write the code.


## 4.3 Third challenge

1.  For Belgium, determine the minimum unemployment value (field #6) in
    *cpds.csv* in a programmatic way.
2.  Have what is printed out to the screen look like "Belgium 6.2".
3.  Now store the unique values of the countries in a variable, first
    stripping out the quotation marks.
4.  Figure out how to automate step 1 to do the calculation for all the
    countries and print to the screen.
5.  How would you instead store the results in a new file?


## 4.4 Fourth challenge

Let's return to the `RTADataSub.csv` file and the issue of missing values.

1. Create a new file without any rows that have an 'x' (which indicate a missing value).
2. Turn the code into a function that also prints out the number of rows that are being removed and that sends its output to stdout so that it can be used with piping.
3. Now modify your function so that the user could provide the missing value string, the input
filename and the output filename as arguments.

## 4.5 Fifth challenge

Here's an advanced one - you'll probably need to use *sed*, but the
brief examples of text substitution in the using bash tutorial should be
sufficient to solve the problem.

Consider a CSV file that has rows that look like this:

```
1,"America, United States of",45,96.1,"continental, coastal"
2,"France",33,807.1,"continental, coastal"
```

While R would be able to handle this using *read.table()*, using *cut*
in UNIX won't work because of the commas embedded within the fields. The
challenge is to convert this file to one that we can use *cut* on, as
follows.

Figure out a way to make this into a new delimited file in which the
delimiter is not a comma. At least one solution that will work for this
particular two-line dataset does not require you to use regular
expressions, just simple replacement of fixed patterns.

---

[← not clear how to sort by start time](07-not-clear-how-to-sort-by-start-time.md) · [Up: contents](index.md)
