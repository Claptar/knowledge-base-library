---
title: 3 bash shell examples
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit3-bash.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit3-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 bash shell examples

Here we'll work through a few examples to start to give you a feel for using the bash shell to manage your workflows and process data.

First let's get the files from the 243 class in 2020 so we have a sufficient body of files we can do interesting things with.

```bash
git clone https://github.com/berkeley-stat243/stat243-fall-2020
```

**Our first mission** is some basic manipulation of a data file. Suppose we want to get a sense for the number of weather stations in different states using the *coop.txt* file.

```bash
cd stat243-fall-2020/data
gunzip coop.txt.gz
cut -b50-70 coop.txt | less
cut -b60-61 coop.txt | sort | uniq
cut -b60-61 coop.txt | sort | uniq -c
```

Now I could of course read the data in R at this stage (or I could read the original dataset, though sometimes it's good to read just the fields of interest to reduce memory use).

**Our second mission:** how can I count the number of fields in a CSV file programmatically?

```bash
tail -n 1 cpds.csv | grep -o ',' | wc -l
nfields=$(tail -n 1 cpds.csv | grep -o ',' | wc -l)
nfields=$((${nfields}+1))
echo $nfields

## alternatively, we can use `bc`
nfields=$(echo "${nfields}+1" | bc)
```

Trouble-shooting: How could the syntax above get the wrong answer?

Extension: We could write a function that can count the number of fields in any file.

Extension: How could I see if all of the lines have the same number of fields?

**Our third mission:** was *example.pdf* created in the five most recently modified R code files in the units directory?

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
```

```bash
## here's how we could do it by explicitly passing the file names
## rather than using xargs
grep -l 'example.pdf' $(ls -tr *.R | tail -n 5)
```

Notice that `man tail` indicates it can take input from a FILE or from *stdin*. Here it uses *stdin*, so it is gives the last five lines of the output of *ls*, not the last five lines of the files indicated in that output.

`man grep` also indicates it can take input from a FILE or from *stdin*. However, we want *grep* to operate on the content of the files indicated in stdin. So we use *xargs* to convert *stdin* to be recognized as arguments, which then are the FILE inputs to *grep*.

**Our fourth mission:** write a function that will move the most recent $n$ files in your Downloads directory to another directory.

In general, we want to start with a specific case, and then generalize to create the function.

```bash
ls -rt ~/Downloads | tail -n 1

## sometimes the ~ behaves weirdly in scripting, so let's use full path
mv "/accounts/gen/vis/paciorek/Downloads/$(ls -rt \
/accounts/gen/vis/paciorek/Downloads | tail -n 1)" ~/Desktop

function mvlast() {
mv "/accounts/gen/vis/paciorek/Downloads/$(ls -rt \
/accounts/gen/vis/paciorek/Downloads | tail -n $2)" $1
}
```

That code only works if the files don't have spaces in their names. If there are spaces, we need double quotes around each file name, which is hard to do in the shell because double quotes are interpreted by the shell as giving the beginning and ending of strings, rather than being passed along for further processing.

**Our fifth mission:** automate the process of determining what R packages are used in all of the R code here and install those packages on a new machine.

```bash
grep library unit[1-9]*.R
grep --no-filename library *.R
grep --no-filename "^library" *.R
grep --no-filename "^library" *.R | sort | uniq
grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1
```

```bash
grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1 | \
tee libs.txt
grep -v "help =" libs.txt > tmp2.txt
sed 's/;/\n/g' tmp2.txt | sed 's/ //g' |
sed 's/library(//' | sed 's/)//g' > libs.txt
## note: on a Mac, use 's/;/\\\n/g' -- see https://superuser.com/questions/307165/newlines-in-sed-on-mac-os-x
echo "There are $(wc -l libs.txt | cut -d' ' -f1) \
unique packages we will install."
## note: on Linux, wc -l puts the number as the first characters of the output
## on a Mac, there may be a bunch of spaces preceding the number, so try this:
## echo "There are $(wc -l libs.txt | tr -s ' ' | cut -d' ' -f2) \
## unique packages we will install."

Rscript -e "pkgs <- scan('libs.txt', what = 'character'); \
install.packages(pkgs, repos = 'https://cran.r-project.org')"
```

**Our sixth mission:** suppose I've accidentally started a bunch of jobs (perhaps with a for loop in bash!) and need to kill them.

```bash
echo "Sys.sleep(1e5)" > job.R
nJobs=30
for (( i=1; i<=${nJobs}; i++ )); do
R CMD BATCH --no-save job.R job-${i}.out &
done

ps -o pid,pcpu,pmem,user,cmd -C R
ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C R | tail -n 30
ps -o pid --sort=start_time -C R | tail -n ${nJobs} | xargs kill

# on a Mac:
ps -o pid,pcpu,pmem,user,command | grep exec/R
# not clear how to sort by start time
ps -o pid,command | grep exec/R | cut -d' ' -f1 | tail -n ${nJobs} | xargs kill
```

---

[← 2 Using the bash shell](02-2-using-the-bash-shell.md) · [Up: contents](index.md) · [4 bash shell challenges →](04-4-bash-shell-challenges.md)
