---
title: 3 bash shell examples
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit3-bash.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 bash shell examples

**Source:** [`units/unit3-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here we’ll work through a few examples to start to give you a feel for using the bash shell to manage your workflows and process data.

First let’s get the files from the 243 class in 2020 so we have a sufficient body of files we can do interesting things with.

<mark>git clone https://github.com/berkeley-stat243/stat243-fall-2020</mark>

**Our first mission** is some basic manipulation of a data file. Suppose we want to get a sense for the number of weather stations in different states using the _coop.txt_ file.

2

cd stat243-fall-2020/data gunzip coop.txt.gz cut -b50-70 coop.txt | less cut -b60-61 coop.txt | sort | uniq cut -b60-61 coop.txt | sort | uniq -c

Now I could of course read the data in R at this stage (or I could read the original dataset, though sometimes it’s good to read just the fields of interest to reduce memory use).

**Our second mission** : how can I count the number of fields in a CSV file programmatically?

tail -n 1 cpds.csv | grep -o ',' | wc -l nfields=$(tail -n 1 cpds.csv | grep -o ',' | wc -l) nfields=$((${nfields}+1)) echo $nfields ## alternatively, we can use ` bc ` nfields=$(echo "${nfields}+1" | bc)

Trouble-shooting: How could the syntax above get the wrong answer?

Extension: We could write a function that can count the number of fields in any file.

Extension: How could I see if all of the lines have the same number of fields?

**Our third mission** : was _example.pdf_ created in the five most recently modified R code files in the units directory?

cd ../units grep -l 'example.pdf' unit13-graphics.R ls -tr *.R ## if unit13-graphics.R is not amongst the 5 most recently used, ## let's artificially change the timestamp so it is recently used. touch unit13-graphics.R ls -tr *.R | tail -n 5 ls -tr *.R | tail -n 5 | grep pdf ls -tr *.R | tail -n 5 | grep "13-gr" ls -tr *.R | tail -n 5 | xargs grep 'example.pdf' ls -tr *.R | tail -n 5 | xargs grep -l 'example.pdf'

3

---

[← 2 Using the bash shell](03-2-using-the-bash-shell.md) · [Up: contents](index.md) · [Unit 03 — bash Part 05 — →](05-unit-03-bash-part-05.md)
