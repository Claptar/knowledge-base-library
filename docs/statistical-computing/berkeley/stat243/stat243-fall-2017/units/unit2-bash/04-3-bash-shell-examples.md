---
title: 3 bash shell examples
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 bash shell examples

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here we’ll work through a few examples to start to give you a feel for using the bash shell to manage your workflows and process data.

First let’s get the files from the 243 class in 2015 so we have a sufficient body of files we can do interesting things with.

<mark>git clone https://github.com/berkeley-stat243/stat243-fall-2015</mark>

**Our first mission** is some basic manipulation of a data file. Suppose we want to get a sense for the number of weather stations in different states using the _coop.txt_ file.

cd stat243-fall-2014/data gunzip coop.txt.gz cut -b50-70 coop.txt | less cut -b60-61 coop.txt | sort | uniq cut -b60-61 coop.txt | sort | uniq -c

Now I could of course read the data in R at this stage (or I could read the original dataset, though sometimes it’s good to read just the fields of interest to reduce memory use).

**Our second mission** : how can I count the number of fields in a CSV file programmatically?

tail -n 1 cpds.csv | grep -o ',' | wc -l nfields=$(tail -n 1 cpds.csv | grep -o ',' | wc -l) nfields=$(echo "${nfields}+1" | bc)

2

**Our third mission** : was _example.pdf_ created in the five most recently modified R code files in the units directory? Note that here grep is expecting a file name as input so we can just use the pipe without the xargs.

cd ../units ls -tr *.R | tail -n 5 ls -tr *.R | tail -n 5 | grep pdf ls -tr *.R | tail -n 5 | grep optim ls -tr *.R | tail -n 5 | xargs grep 'example.pdf' ls -tr *.R | tail -n 5 | xargs grep -l 'example.pdf'

Notice that man tail indicates it can take input from a FILE or from _stdin_ . Here it uses _stdin_ , so it is gives the last five lines of the output of _ls_ , not the last five lines of the files indicated in that output.

man grep also indicates it can take input from a FILE or from _stdin_ . However, we want grep to operate on the content of the files indicated in stdin. So we use _xargs_ to convert _stdin_ to be recognized as arguments, which then are the FILE inputs to _grep_ .

**Our fourth mission** : automate the process of determining what R packages are used in all of the R code here and install those packages on a new machine.

grep library unit[1-9]*.R grep --no-filename library *.R grep --no-filename "^library" *.R grep --no-filename "^library" *.R | sort | uniq grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1 grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1 | \ tee libs.txt grep -v "help =" libs.txt > tmp2.txt sed 's/;/\n/g' tmp2.txt | sed 's/ //g' | sed 's/library(//' | sed 's/)//g' > libs.txt echo "There are $(wc -l libs.txt | cut -d' ' -f1) \ unique packages we will install."

Rscript -e "pkgs <- scan('libs.txt', what = 'character'); \ install.packages(pkgs, repos = 'http:/cran.cnr.berkeley.edu')"

3

**Our fifth mission** : suppose I’ve accidentally started a bunch of jobs (perhaps with a for loop in bash!) and need to kill them.

echo "Sys.sleep(1e5)" > job.R nJobs=30 for (( i=1; i<=${nJobs}; i++ )); do R CMD BATCH --no-save job.R job-${i}.out & done

ps -o pid,pcpu,pmem,user,cmd -C R ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C R | tail -n 30 ps -o pid --sort=start_time -C R | tail -n ${nJobs} | xargs kill

---

[← 2 Using the bash shell](03-2-using-the-bash-shell.md) · [Up: contents](index.md) · [4 bash shell challenges →](05-4-bash-shell-challenges.md)
