---
title: 3. bash shell examples
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit3-bash.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. bash shell examples

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

Here we'll work through a few examples to start to give you a feel for
using the bash shell to manage your workflows and process data.

First let's get the files from GitHub to have a set of
files we can do interesting things with.

```bash
#| eval: false
git clone https://github.com/berkeley-stat243/stat243-fall-2023
```

One important note is that most of the shell commands that work with
data inside files (in contrast to commands like `ls` and `cd`)
work only with text files and not binary files. Also the
commands operate on a line-by-line basis.

**Our first mission** is some basic manipulation of a data file. Suppose
we want to get a sense for the number of weather stations in different
states using the *coop.txt* file.

```bash
#| eval: false
cd stat243-fall-2023/data
gzip -cd coop.txt.gz | less
gunzip coop.txt.gz
cut -b50-70 coop.txt | less
cut -b60-61 coop.txt | uniq
cut -b60-61 coop.txt | sort | uniq
cut -b60-61 coop.txt | sort | uniq -c
## all in one line with no change to the original file:
gzip -cd coop.txt.gz | cut -b60-61 coop.txt | sort | uniq -c
```

I could have done that in R or Python, but it would have required
starting the program up and reading all the data into memory.

If you feel that manually figuring out the position of the state field
is inconsistent with our emphasis on programmatic workflows, see
the fifth challenge below.

**Our second mission**: how can I count the number of fields in a CSV
file programmatically?

```bash
#| eval: false
tail -n 1 cpds.csv | grep -o ',' | wc -l
nfields=$(tail -n 1 cpds.csv | grep -o ',' | wc -l)

nfields=$((${nfields}+1))
echo $nfields

## alternatively, we can use `bc`
nfields=$(echo "${nfields}+1" | bc)
```


Trouble-shooting: How could the syntax above get the wrong answer?

Extension: We could write a function that can count the number of fields
in any file.

Extension: How could I see if all of the lines have the same number of
fields?

**Our third mission**: was the `sqlite3` package in the five most
recently modified Quarto Markdown files in the units directory?

```bash
#| eval: false
cd ../units
grep -l 'import sqlite3' unit7-bigData.qmd
ls -tr *.qmd
## if unit7-bigData.qmd is not amongst the 5 most recently used,
## let's artificially change the timestamp so it is recently used.
touch unit7-bigData.qmd

ls -tr *.qmd | tail -n 5
ls -tr *.qmd | tail -n 5 | grep sqlite3
ls -tr *.qmd | tail -n 5 | grep "unit7-bigData"
ls -tr *.qmd | tail -n 5 | xargs grep 'import sqlite3'
ls -tr *.qmd | tail -n 5 | xargs grep -l 'import sqlite3'
## here's how we could do it by explicitly passing the file names
## rather than using xargs
grep -l 'import sqlite3' $(ls -tr *.R | tail -n 5)
```

Notice that `man tail` indicates it can take input from a FILE or from
`stdin`. Here it uses `stdin`, so it is gives the last five lines of the
output of `ls`, not the last five lines of the files indicated in that
output.

`man grep` also indicates it can take input from a FILE or from `stdin`.
However, we want grep to operate on the content of the files indicated
in stdin. So we use `xargs` to convert `stdin` to be recognized as
arguments, which then are the FILE inputs to `grep`.

Here are some of the ways we can pass information from a command to somewhere else:

- Piping allows us to pass information from one command to another command via stdout to stdin.
- `$()` allows us to store the result of a command in a variable.
    - also used to create a temporary variable to pass the output from one command as an option or argument (e.g., the FILE argument) of another command
- File redirection operators such as `>` and `>>` allow us to pass information from a command into a file.

**Our fourth mission**: write a function that will move the most recent
*n* files in your Downloads directory to another directory.

In general, we want to start with a specific case, and then generalize
to create the function.

```bash
#| eval: false
ls -rt ~/Downloads | tail -n 5

---

[← 2. Using the bash shell](02-2-using-the-bash-shell.md) · [Up: contents](index.md) · [create dummy test files without any spaces →](04-create-dummy-test-files-without-any-spaces.md)
