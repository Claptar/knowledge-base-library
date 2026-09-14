---
title: 3 bash shell examples
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 bash shell examples

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here we’ll work through a few examples to start to give you a feel for using the bash shell to manage your workflows and process data.

First let’s get the files from last year’s 243 class so we have a sufficient body of files we can do interesting things with.

<mark>git clone https://github.com/berkeley-stat243/stat243-fall-2014</mark>

**Our first mission** is some basic manipulation of a data file. Suppose we want to get a sense for the number of weather stations in different states using the _coop.txt_ file.

cd stat243-fall-2014/data cut -b50-70 coop.txt | less cut -b60-61 coop.txt | sort | uniq cut -b60-61 coop.txt | sort | uniq -c

Now I could of course read the data in R at this stage (or I could read the original dataset, though sometimes it’s good to read just the fields of interest to reduce memory use).

**Our second mission** : how can I count the number of fields in a CSV file programmatically?

tail -n 1 cpds.csv | grep -o ’,’ | wc -l nfields=$(tail -n 1 cpds.csv | grep -o ’,’ | wc -l) nfields = ’foo’

**Our third mission** : was _example.pdf_ created in the five most recently modified R code files in the units directory? Note that here grep is expecting a file name as input so we can just use the pipe without the xargs.

cd ../units ls -tr *.R | tail -n 5 | grep pdf ls -tr *.R | tail -n 5 | grep numbers ls -tr *.R | tail -n 5 | xargs grep ’example.pdf’ ls -tr *.R | tail -n 5 | xargs grep -l ’example.pdf’

Notice that man tail indicates it can take input from a FILE or from _stdin_ . But if we want to pass the filenames to grep we need to ensure that grep realizes the input is the file names and

2

not stdin itself. Otherwise we are just grepping for ‘example.pdf’ in the literal strings that are the file name.

**Our fourth mission** : automate the process of determining what R packages are used in all of the R code here and install those packages on a new machine.

grep library unit[1-9]*.R grep --no-filename library *.R grep --no-filename "^library" *.R grep --no-filename "^library" *.R | sort | uniq grep --no-filename "^library" *.R | sort | uniq | cut -d’#’ -f1 grep --no-filename "^library" *.R | sort | uniq | cut -d’#’ -f1 | tee tmp.txt grep -v "help =" tmp.txt _>_ libs.txt sed -e ’s/library(//’ libs.txt | sed -e ’s/quietly = TRUE//g’ | sed -e ’s/;/ _\_ n/g’ sed -e ’s/;/ _\_ n/g’ libs.txt | sed -e ’s/quietly = TRUE//g’ | sed -e ’s/library(//’ _>_ tmp.txt sed -e ’s/[ _\_ , )]//g’ tmp.txt _>_ libs.txt echo "There are $(wc -l libs.txt | cut -d’ ’ -f1) unique packages we will install."

Rscript -e "pkgs _<_ - scan(’libs.txt’, what = ’character’); _\_ install.packages(pkgs, repos = ’http:/cran.cnr.berkeley.edu’)"

**Our fifth mission** : suppose I’ve accidentally started a bunch of jobs (perhaps with a for loop in bash!) and need to kill them.

echo "Sys.sleep(1e5)" _>_ job.R nJobs=30 **for** (( i=1; i _<_ = **${nJobs}** ; i++ )); **do** R CMD BATCH --no-save job.R job- **${i}** .out & **done**

ps -o pid,pcpu,pmem,user,cmd -C R

ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C R | tail -n 30

3

ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C R | tail -n 30 ps -o pid --sort=start_time -C R | tail -n **${nJobs}** | xargs kill

---

[← 2 Using the bash shell](03-2-using-the-bash-shell.md) · [Up: contents](index.md) · [4 bash shell challenges →](05-4-bash-shell-challenges.md)
