---
title: Unit 03 — bash Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit3-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit3-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — bash Part 06 —

**Source:** [`units/unit3-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit3-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

/accounts/gen/vis/paciorek/Downloads | tail -n 1)" ~/Desktop

function mvlast() {

mv "/accounts/gen/vis/paciorek/Downloads/$(ls -rt \ /accounts/gen/vis/paciorek/Downloads | tail -n $2)" $1 }

**Our fifth mission** : automate the process of determining what R packages are used in all of the R code here and install those packages on a new machine.

grep library unit[1-9]*.R grep --no-filename library *.R grep --no-filename "^library" *.R grep --no-filename "^library" *.R | sort | uniq grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1 grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1 | \ tee libs.txt grep -v "help =" libs.txt > tmp2.txt sed 's/;/\n/g' tmp2.txt | sed 's/ //g' |

4

sed 's/library(//' | sed 's/)//g' > libs.txt ## note: on a Mac, use 's/;/\\\n/g' -- see echo "There are $(wc -l libs.txt | cut -d' ' -f1) \ unique packages we will install." ## note: on Linux, wc -l puts the number as the first characters of the output ## on a Mac, there may be a bunch of spaces preceding the number, so try this: ## echo "There are $(wc -l libs.txt | tr -s ' ' | cut -d' ' -f2) \ ## unique packages we will install."

Rscript -e "pkgs <- scan('libs.txt', what = 'character'); \ install.packages(pkgs, repos = 'https://cran.r-project.org')"

**Our sixth mission** : suppose I’ve accidentally started a bunch of jobs (perhaps with a for loop in bash!) and need to kill them.

echo "Sys.sleep(1e5)" > job.R nJobs=30 for (( i=1; i<=${nJobs}; i++ )); do R CMD BATCH --no-save job.R job-${i}.out & done

ps -o pid,pcpu,pmem,user,cmd -C R ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C R | tail -n 30 ps -o pid --sort=start_time -C R | tail -n ${nJobs} | xargs kill # on a Mac: ps -o pid,pcpu,pmem,user,command | grep exec/R # not clear how to sort by start time ps -o pid,command | grep exec/R | cut -d' ' -f1 | tail -n ${nJobs} | xargs

---

[← Unit 03 — bash Part 05 —](05-unit-03-bash-part-05.md) · [Up: contents](index.md) · [4 bash shell challenges →](07-4-bash-shell-challenges.md)
