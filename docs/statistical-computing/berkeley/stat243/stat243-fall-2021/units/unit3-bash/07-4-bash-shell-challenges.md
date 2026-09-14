---
title: 4 bash shell challenges
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit3-bash.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 bash shell challenges

**Source:** [`units/unit3-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 First challenge**

Consider the file _unit3-bash.sh_ . How would you write a shell command that returns "There are 2 occurrences of the word ’bash’ in this file."

Extra: make your code into a function that can operate on any file indicated by the user and any word of interest.

### **4.2 Second challenge**

1. For Belgium, determine the minimum unemployment value (field #6) in _cpds.csv_ in a programmatic way.

2. Have what is printed out to the screen look like “Belgium 6.2”.

3. Now store the unique values of the countries in a variable, first stripping out the quotation marks and removing the space in “New Zealand”, which causes problems because of the space in its name.

4. Figure out how to automate step 1 to do the calculation for all the countries and print to the screen.

5. How would you instead store the results in a new file?

### **4.3 Third challenge**

Consider the data in the _RTADataSub.csv_ file. This is a subset of data giving freeway travel times for segments of a freeway in an Australian city. The data are from a kaggle.com competition. We want to try to understand the kinds of data in each field of the file. The following would be particularly useful if the data were in many files or the data were many gigabytes in size.

First, take the fourth column. Figure out the unique values in that column.

Next, automate the process of determining if any of the values are non-numeric so that you don’t have to scan through all of the unique values looking for non-numbers. You’ll need to look for the following regular expression pattern “[^0-9]”, which is interpreted as NOT any of the numbers 0 through 9.

Now, do it for all the fields, except the first one. Have your code print out the result in a human-readable way understandable by someone who didn’t write the code.

6

### **4.4 Fourth challenge**

Here’s an advanced one - you’ll probably need to use _sed_ , but the brief examples of text substitution in the using bash tutorial should be sufficient to solve the problem.

Consider a CSV file that has rows that look like this:

- 1,"America, United States of",45,96.1,"continental, coastal" 2,"France",33,807.1,"continental, coastal"

While R would be able to handle this using _read.table()_ , using _cut_ in UNIX won’t work because of the commas embedded within the fields. The challenge is to convert this file to one that we can use _cut_ on, as follows.

Figure out a way to make this into a new delimited file in which the delimiter is not a comma. At least one solution that will work for this particular two-line dataset does not require you to use regular expressions, just simple replacement of fixed patterns.

---

[← Unit 03 — bash Part 06 —](06-unit-03-bash-part-06.md) · [Up: contents](index.md) · [5 Regular expressions →](08-5-regular-expressions.md)
