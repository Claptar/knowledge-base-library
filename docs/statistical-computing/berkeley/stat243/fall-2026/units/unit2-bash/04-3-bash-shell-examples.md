---
title: 3. bash shell examples
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit2-bash.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit2-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. bash shell examples

**Source:** [`units/unit2-bash.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit2-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Here we'll work through a few examples to start to give you a feel for
using the bash shell to manage your workflows and process data.

First let's get the files from GitHub to have a set of
files we can do interesting things with.

```bash
#| eval: false
git clone https://github.com/berkeley-stat243/fall-2026
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
cd fall-2026/data
gzip -cd coop.txt.gz | less
gunzip coop.txt.gz
cut -b50-70 coop.txt | less
cut -b60-61 coop.txt | uniq
cut -b60-61 coop.txt | sort | uniq
cut -b60-61 coop.txt | sort | uniq -c
## Do it all in one line with no change to the original file:
gzip -cd coop.txt.gz | cut -b60-61 | sort | uniq -c
```

What if I want to save the result in a file?

```bash
#| eval: false
gzip -cd coop.txt.gz | cut -b60-61 | sort | uniq -c > station_count_states.txt
```

And what if I want it comma-delimited?

```bash
#| eval: false
sed "s/ /,/g" station_count_states.txt
sed "s/ +/,/g" station_count_states.txt
sed -E "s/ +/,/g" station_count_states.txt
sed -E "s/ +/,/g" station_count_states.txt | cut -d"," -f2,3 > station_count_states.csv
```

Alternatively, one could use a tool called `awk` (which we won't cover),
which has a lot of functionality for flexibly working with data fields in text files.
`awk` would also allow us to switch the order of the columns.

I could have done that in Python or R, but standard usage would have required
starting the program up and reading all the data into memory.

Instead, here's how we could operate line by line in Python.

```python
#| eval: false
with open("station_count_states.txt", "r") as file:
    for line in file:
        result = ",".join(line.split()[::-1])
        print(f"{result}")
```

It's not hard to use that to create a Python script you could run from the command line as a command line tool.

```bash
cat to_csv
```

In this case the script requires input from stdin and not from a file (with a little bit more work we could make it more flexible and more consistent with the UNIX commands that can work either with stdin or a file), so we need to use `cat` to get the text from the file to pass into the script.

```bash
#| eval: false
cat station_count_states.txt | ./to_csv > station_count_states.csv
```

We need `./` before `to_csv` because the shell doesn't know to look in the working directory for a program/command called `to_csv` (i.e., the working directory is not on the "PATH").

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

## Alternatively, we can use `bc`.
nfields=$(echo "${nfields}+1" | bc)
```


Trouble-shooting: How could the syntax above get the wrong answer?

Extension: We could write a function that can count the number of fields
in any file.

Extension: What are some ways we could count the number of fields in *each* row?


**We'll work on Challenge #1 here.**

**Our third mission**: was the `requests` package in the five most
recently modified Quarto Markdown files in the units directory?

```bash
#| eval: false
cd ../units
grep -l 'import requests' unit3-goodPractices.qmd
ls -tr *.qmd
## If unit3-goodPractices.qmd is not amongst the 5 most recently used,
## let's artificially change the timestamp so it is recently used.
touch unit3-goodPractices.qmd

ls -tr *.qmd | tail -n 5
ls -tr *.qmd | tail -n 5 | grep requests
ls -tr *.qmd | tail -n 5 | grep "unit3-goodPractices"
ls -tr *.qmd | tail -n 5 | xargs grep 'import requests'
ls -tr *.qmd | tail -n 5 | xargs grep -l 'import requests'
```

Notice that `man tail` indicates it can take input from a FILE or from
`stdin`. Here it uses `stdin`, so it is gives the last five lines of the
output of `ls`, not the last five lines of the files indicated in that
output.

`man grep` also indicates it can take input from a FILE or from `stdin`.
However, we want grep to operate on the content of the files indicated
in stdin. So we use `xargs` to convert `stdin` to be recognized as
arguments, which then are the FILE inputs to `grep`.

An alternative to `xargs` is to embed the `ls` invocation, using `$()`,
to explicitly pass the file names as the argument to `grep`:

```bash
#| eval: false
grep -l 'import requests' $(ls -tr *.qmd | tail -n 5)
```


Here are some of the ways we can pass information from a command to somewhere else:

- Piping allows us to pass information from one command to another command via stdout to stdin.
- `$()` allows us to store the result of a command in a variable.
    - also used to create a temporary variable to pass the output from one command as an option or argument (e.g., the FILE argument) of another command
- File redirection operators such as `>` and `>>` allow us to pass output from a command into a file.

**We'll work on Challenge #2 here.**

**Our fourth mission**: write a function that will move the most recent
*n* files in your Downloads directory to another directory.

In general, we want to start with a specific case, and then generalize
to create the function.

```bash
#| eval: false
ls -rt ~/Downloads | tail -n 5

---

[← 2. Using the bash shell](03-2-using-the-bash-shell.md) · [Up: contents](index.md) · [Create dummy test files with names with and without spaces. →](05-create-dummy-test-files-with-names-with-and-without-spaces.md)
