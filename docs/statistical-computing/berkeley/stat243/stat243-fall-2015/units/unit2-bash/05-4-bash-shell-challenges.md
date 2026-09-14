---
title: 4 bash shell challenges
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 bash shell challenges

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 First challenge**

Consider the listing of info in _/proc/cpuinfo_ on a Linux machine such as BCE. How would you write a shell command that returns "There are 6 processors on this machine" where 6 is determined based on the contents of _/proc/cpuinfo_ and not based on using _nproc_ .

Note: before trying this out, please set up BCE so that it uses two virtual processors. Go to Settings -> System -> Processor and choose “2 CPU”. Then start up the VM.

### **4.2 Second challenge**

1. For Belgium, determine the minimum unemployment value (field #6) in _cpds.csv_ in a programmatic way.

2. Have what is printed out to the screen look like “Belgium 6.2”.

3. Now store the unique values of the countries in a variable, first stripping out the quotation marks and New Zealand, which causes problems because of the space in its name.

4. Figure out how to automate step 1 to do the calculation for all the countries and print to the screen.

5. How would you instead store the results in a new file?

### **4.3 Third challenge**

Consider the data in the _RTADataSub.csv_ file. This is a subset of data giving freeway travel times for segments of a freeway in an Australian city. The data are from a kaggle.com competition. We want to try to understand the kinds of data in each field of the file. The following would be particularly useful if the data were in many files or the data were many gigabytes in size.

First, take the fourth column. Figure out the unique values in that column.

Next, automate the process of determining if any of the values are non-numeric so that you don’t have to scan through all of the unique values looking for non-numbers. You’ll need to

4

look for the following regular expression pattern “[^0-9]”, which is interpreted as NOT any of the numbers 0 through 9.

Now, do it for all the fields, except the first one. Have your code print out the result in a human-readable way understandable by someone who didn’t write the code.

### **4.4 Fourth challenge**

Here’s an advanced one - you’ll probably need to use sed, but the brief examples of text substitution in the using bash tutorial should be sufficient to solve the problem.

Consider a CSV file that has rows that look like this:

1,"America, United States of",45,96.1,"continental, coastal" 2,"France",33,807.1,"continental, coastal"

While R would be able to handle this using ‘read.table()‘, using _cut_ in UNIX won’t work because of the commas embedded within the fields.

Figure out a way to make this into a new delimited file in which the delimiter is not a comma. At least one solution that will work for this particular two-line dataset does not require you to use regular expressions, just simple replacement of fixed patterns.

---

[← 3 bash shell examples](04-3-bash-shell-examples.md) · [Up: contents](index.md) · [5 Version Control →](06-5-version-control.md)
