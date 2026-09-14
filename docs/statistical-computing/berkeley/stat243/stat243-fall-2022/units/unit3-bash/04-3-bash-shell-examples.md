---
title: 3. bash shell examples
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit3-bash.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit3-bash.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. bash shell examples

**Source:** [`units/unit3-bash.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit3-bash.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Here we'll work through a few examples to start to give you a feel for
using the bash shell to manage your workflows and process data.

First let's get the files from the 243 class in 2021 so we have a
sufficient body of files we can do interesting things with.

```bash
git clone https://github.com/berkeley-stat243/stat243-fall-2021
```

**Our first mission** is some basic manipulation of a data file. Suppose
we want to get a sense for the number of weather stations in different
states using the *coop.txt* file.

```bash
cd stat243-fall-2021/data
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

**Our second mission**: how can I count the number of fields in a CSV
file programmatically?

```bash
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

**Our third mission**: was *example.pdf* created by code in the five most
recently modified R code files in the units directory?

```bash
cd ../units
grep -l 'example.pdf' unit13-graphics.R
ls -tr *.R
## if unit13-graphics.R is not amongst the 5 most recently used,
## let's artificially change the timestamp so it is recently used.
touch unit13-graphics.R

ls -tr *.R | tail -n 5
ls -tr *.R | tail -n 5 | grep pdf
ls -tr *.R | tail -n 5 | grep "13-gr"
ls -tr *.R | tail -n 5 | xargs grep 'example.pdf'
ls -tr *.R | tail -n 5 | xargs grep -l 'example.pdf'
## here's how we could do it by explicitly passing the file names
## rather than using xargs
grep -l 'example.pdf' $(ls -tr *.R | tail -n 5)
```

Notice that `man tail` indicates it can take input from a FILE or from
*stdin*. Here it uses *stdin*, so it is gives the last five lines of the
output of *ls*, not the last five lines of the files indicated in that
output.

`man grep` also indicates it can take input from a FILE or from *stdin*.
However, we want grep to operate on the content of the files indicated
in stdin. So we use *xargs* to convert *stdin* to be recognized as
arguments, which then are the FILE inputs to *grep*.

Here are some of the ways we can pass information from a command to somewhere else:

- piping allows us to pass information from one command to another command via stdout to stdin
- `$()` allows us to store the result of a command in a variable
    - also used to create a temporary variable to pass the output from one command as an option or argument (e.g., the FILE argument) of another command
- file redirection operators such as `>` and `>>` allow us to pass information from a command into a file

**Our fourth mission**: write a function that will move the most recent
*n* files in your Downloads directory to another directory.

In general, we want to start with a specific case, and then generalize
to create the function.

```bash
ls -rt ~/Downloads | tail -n 1

## sometimes the ~ behaves weirdly in scripting, so let's use full path
mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
   /accounts/vis/paciorek/Downloads | tail -n 1)" ~/Desktop

function mvlast() {
    mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
       /accounts/vis/paciorek/Downloads | tail -n 1)" $1
}
```

Note the need for the quotes to deal with cases where a file has a space in its name.

If we wanted to handle multiple files, we could do it with a loop:

```bash
function mvlast() {
    for ((i=1; i<=${1}; i++)); do
        mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
           /accounts/vis/paciorek/Downloads | tail -n 1)" ${2}
    done
}
```

Side note: if we were just moving files from the current working directory and with files without spaces in their names, it should be possible to use `tail -n ${1}` without the loop.

**Our fifth mission**: automate the process of determining what R
packages are used in all of the R code here and install those packages
on a new machine.

```bash
grep library unit[1-9]*.R
grep --no-filename library *.R
grep --no-filename "^library" *.R
grep --no-filename "^library" *.R | sort | uniq
grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1
grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1 | \
    tee libs.txt
grep -v "help =" libs.txt > tmp2.txt
sed 's/;/\n/g' tmp2.txt | sed 's/ //g' |
    sed 's/library(//' | sed 's/)//g' > libs.txt
## note: on a Mac, use 's/;/\\\n/g'   -- see https://superuser.com/questions/307165/newlines-in-sed-on-mac-os-x
echo "There are $(wc -l libs.txt | cut -d' ' -f1) \
unique packages we will install."
## note: on Linux, wc -l puts the number as the first characters of the output
## on a Mac, there may be a bunch of spaces preceding the number, so try this:
## echo "There are $(wc -l libs.txt | tr -s ' ' | cut -d' ' -f2) \
## unique packages we will install."


## @knitr mission5a               -
Rscript -e "pkgs <- scan('libs.txt', what = 'character'); \
install.packages(pkgs, repos = 'https://cran.r-project.org')"
```

You wouldn't want to use this code to accomplish this task in reality - there are packages such as *renv* and *packrat* that can accomplish this. The main point was to illustrate how one can quickly hack together some code to do fairly complicated tasks.

**Our sixth mission**: suppose I've accidentally started a bunch of jobs
(perhaps with a for loop in bash!) and need to kill them. (This example uses
syntax from the Managing Processes page of the bash tutorial, so it goes
beyond what you were asked to read for this Unit.)

```bash
echo "Sys.sleep(1e5)" > job.R
nJobs=30
for (( i=1; i<=${nJobs}; i++ )); do
   R CMD BATCH --no-save job.R job-${i}.out &
done

---

[← 2. Using the bash shell](03-2-using-the-bash-shell.md) · [Up: contents](index.md) · [on Linux →](05-on-linux.md)
