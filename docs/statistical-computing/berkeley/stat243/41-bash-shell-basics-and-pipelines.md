---
title: "41. Bash Shell Basics and Pipelines"
course: "Berkeley Stat 243"
chapter: 41
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 41. Bash Shell Basics and Pipelines

## What this covers

This chapter answers a practical question: how do you get UNIX-style command-line tools to do the
data wrangling you would otherwise reach for R or Python to do — reading a file once, in one pass,
without loading it into memory? It assumes you can already open a terminal and run a single command
like `ls` or `cd`, and it builds from there to chaining commands together, writing small bash
functions, and a first orientation to regular expressions. The detailed syntax of any one command
(`cut`, `sed`, `grep`'s many flags, and so on) is not repeated here; it lives in the shell tutorial
the course points to, cited at the end.

## The shell as an interface

The shell is the program that sits between you and the operating system. When you open a terminal
window you are talking to a shell — commonly `bash`, sometimes `zsh` (the default on modern MacOS)
or one of `sh`, `csh`, `tcsh`, `ksh`. 'UNIX' here means the family of operating systems descended
from the UNIX system built at Bell Labs in the 1970s, which includes MacOS and the Linux
distributions (Ubuntu, Debian, CentOS, Fedora, and others). Windows' PowerShell and `cmd.exe` are
command-line interfaces but not UNIX ones, and are not part of this material.

UNIX commands are deliberately narrow: each one does a single job well and fast, and the shell
composes them. That design is decades old and can feel old-fashioned, but it is still how modern
scientific computing gets automated and made reproducible — and once the vocabulary is familiar,
it is also simply fast to type.

Across the years this course has run, the shell unit has pointed to an external tutorial for the
mechanics of using bash (variables, quoting, `ssh`/`scp`, and so on) rather than reproducing it in
the slides — that tutorial is named in the Sources section below. What the lecture itself adds is
the vocabulary for combining commands, and a set of worked examples that show why you would bother.

## Pipes, substitution, and redirection: the core vocabulary

Three mechanisms let you move information between commands, and almost everything below is built
out of them:

- **Piping** (`|`) sends the standard output (`stdout`) of one command directly into the standard
  input (`stdin`) of the next, so a chain of narrow commands acts as one computation over the data,
  streaming through it rather than storing all of it.
- **Command substitution** (`` $(...) ``) runs a command and drops its output in place — either
  captured into a variable, or spliced directly into another command's argument list.
- **Redirection** (`>` and `>>`) sends a command's output into a file instead of the screen,
  overwriting or appending respectively.

A wrinkle worth holding onto from the start: a command like `tail` or `grep` can take its input
either from a named file argument or from `stdin`. Piping something into `tail` means it operates
on whatever came down the pipe, not on a file — a distinction the third worked example below turns
on.

## Worked examples

The following are the "missions" the course works through live, building each one up from a first
attempt to a general version. They use two running datasets: *coop.txt*, a fixed-width file of
weather station locations, and *cpds.csv*, the Comparative Political Data Set, together with
*RTADataSub.csv*, a Kaggle dataset of Australian freeway travel times. None of these files are part
of this material — see Sources.

### Mission 1 — a field from a compressed file, without loading it

How many weather stations are in each state, using *coop.txt*? First get a feel for the file, then
narrow in on the field that holds the state code:

```bash
cd fall-2025/data
gzip -cd coop.txt.gz | less
gunzip coop.txt.gz
cut -b50-70 coop.txt | less        # scan a range of byte columns to spot the field
cut -b60-61 coop.txt | uniq        # the state code lives at bytes 60-61
cut -b60-61 coop.txt | sort | uniq
cut -b60-61 coop.txt | sort | uniq -c

## the whole thing in one line, and the compressed file is never decompressed to disk:
gzip -cd coop.txt.gz | cut -b60-61 coop.txt | sort | uniq -c
```

<figure>
<svg viewBox="0 0 660 160" role="img" aria-label="A pipeline: a compressed file flows through gzip, cut, sort, and uniq to produce per-state counts">
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
</marker>
</defs>
<g fill="none" stroke="currentColor" stroke-width="1.5">
<rect x="10" y="55" width="110" height="50"/>
<rect x="140" y="55" width="110" height="50"/>
<rect x="270" y="55" width="110" height="50"/>
<rect x="400" y="55" width="110" height="50"/>
<rect x="530" y="55" width="110" height="50"/>
</g>
<g font-size="12" text-anchor="middle" fill="currentColor">
<text x="65" y="76">coop.txt.gz</text>
<text x="65" y="92">(file)</text>
<text x="195" y="84">gzip -cd</text>
<text x="325" y="84">cut -b60-61</text>
<text x="455" y="84">sort</text>
<text x="585" y="84">uniq -c</text>
</g>
<g stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)">
<line x1="120" y1="80" x2="138" y2="80"/>
<line x1="250" y1="80" x2="268" y2="80"/>
<line x1="380" y1="80" x2="398" y2="80"/>
<line x1="510" y1="80" x2="528" y2="80"/>
</g>
<text x="330" y="130" text-anchor="middle" font-size="11" fill="currentColor">each arrow is one stage's stdout piped into the next stage's stdin</text>
</svg>
<figcaption>The pipeline that answers "how many weather stations per state?" in one pass over the
file, with nothing ever loaded into R or Python.</figcaption>
</figure>

The point is not that this is impossible in R or Python — it is that doing it there means starting
the interpreter and reading the whole file into memory first, whereas the shell streams through it.

### Mission 2 — counting fields in a CSV programmatically

```bash
tail -n 1 cpds.csv | grep -o ',' | wc -l
nfields=$(tail -n 1 cpds.csv | grep -o ',' | wc -l)

nfields=$((${nfields}+1))
echo $nfields

## alternatively, arithmetic via `bc`:
nfields=$(echo "${nfields}+1" | bc)
```

The idea: count the commas on one line and add one for the final field. Left open by the lecture,
worth sitting with rather than looking up: *how could this syntax get the wrong answer?* (Section
4.6 below, on fields with embedded commas, is closely related.) Left as further extensions: write
this as a function that counts fields in any file, and figure out how to check that every line in
the file has the same number of fields.

### Mission 3 — searching only the most recently touched files

Was the `requests` package imported in any of the five most recently modified Quarto files in the
units directory?

```bash
cd ../units
grep -l 'import requests' unit4-goodPractices.qmd
ls -tr *.qmd                                   # oldest to newest
touch unit4-goodPractices.qmd                  # force it to be "recent", for the demo

ls -tr *.qmd | tail -n 5
ls -tr *.qmd | tail -n 5 | grep "unit4-goodPractices"

ls -tr *.qmd | tail -n 5 | xargs grep 'import requests'
ls -tr *.qmd | tail -n 5 | xargs grep -l 'import requests'
```

This is where the file-argument-versus-`stdin` wrinkle bites: `tail` here reads from `stdin`, so it
returns the last five lines of `ls`'s *output* (five filenames), not the last five lines of any
file. `grep`, in turn, needs those filenames as arguments, not as text piped into it — piping them
in would have `grep` search the list of names themselves for the word `requests`, not the file
contents. `xargs` bridges this: it takes what comes down the pipe and turns it into arguments for
the next command. The equivalent without `xargs`, using command substitution to splice the file
list directly into `grep`'s argument list:

```bash
grep -l 'import requests' $(ls -tr *.R | tail -n 5)
```

So there are three ways to move information from one command to the next: piping (stdout to
stdin), `$(...)` (capturing or splicing a result), and file redirection (`>`, `>>`, output to a
file).

### Mission 4 — a function to move the *n* most recent files

Start from a single concrete case, then generalize into a function — the general pattern for
building any shell function:

```bash
ls -rt ~/Downloads | tail -n 5
touch ~/Downloads/test{1..4}                   # dummy files with no spaces, for testing
ls -rt ~/Downloads | tail -n 5

## `~` can behave oddly inside scripts, so spell out the full path:
mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
   /accounts/vis/paciorek/Downloads | tail -n 1)" ~/Desktop

function mvlast() {
    mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
       /accounts/vis/paciorek/Downloads | tail -n 1)" $1
}
```

The quotes around the `mv` target matter: without them, a filename containing a space would be
split into two arguments. (An earlier version of this example, working without those quotes, notes
that a file with a space in its name breaks it — double quotes are exactly what is needed, and are
awkward here only because the shell itself also uses double quotes to mark string boundaries.)

Handling more than one file needs a loop:

```bash
function mvlast() {
    for ((i=1; i<=${1}; i++)); do
        mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
           /accounts/vis/paciorek/Downloads | tail -n 1)" ${2}
    done
}
```

If instead you only need to move files sitting in the current directory, and none of their names
contain spaces, a single `tail -n ${1}` can stand in for the loop.

### Mission 5 — harvesting dependencies across many files

Automate finding every Python package imported anywhere in the course's `.qmd` files, so they can
all be installed on a fresh machine:

```bash
grep import *.qmd
grep --no-filename import *.qmd
grep --no-filename "^import" *.qmd
grep --no-filename "^import " *.qmd
grep --no-filename "^import " *.qmd | sort | uniq
grep --no-filename "^import " *.qmd | cut -d'#' -f1
grep --no-filename "^import " *.qmd | cut -d'#' -f1 | sed  "s/as .*//"
grep --no-filename "^import " *.qmd | cut -d'#' -f1 | \
                   sed  "s/as .*//" | sed "s/import //" > tmp.txt
sed "s/,/\n/g" tmp.txt | sed "s/ //g" | sort | uniq | tee requirements.txt

echo "There are $(wc -l requirements.txt | cut -d' ' -f1) unique packages we will install."

pip install -r requirements.txt
```

Each line tightens the pattern: anchor to the start of the line (`^import `) to avoid matching
`import` inside a comment or a longer word, strip trailing `# comment` text with `cut -d'#' -f1`,
strip `as alias` and the word `import` itself with `sed`, then split comma-separated imports onto
their own lines before sorting and de-duplicating. `tee` both writes the result to
*requirements.txt* and echoes it to the screen, so the pipeline's final step is visible without a
separate `cat`.

Two portability notes surfaced by exactly this kind of script:

- On MacOS, `sed`'s newline substitution needs different escaping than on Linux (`'s/,/\\\n/g'`).
- `wc -l`'s output is formatted differently on the two systems: the count comes first on Linux, but
  may be preceded by padding spaces on MacOS, so a more robust version pipes through `tr -s ' '`
  before taking the field with `cut`.

This is not the tool you would use in production — a real Python or R project manager
(`pip`/`conda`, or R's `renv`/`packrat`) already solves dependency-tracking properly. The point of
building it by hand is to see how quickly a chain of narrow commands can do something that looks,
at first, like it needs a real program. (An earlier run of this course did the identical exercise
for an all-R codebase: grep for `^library` calls across `.R` files instead of `^import` across
`.qmd` files, then hand the resulting package list to `install.packages()` instead of `pip`. The
technique doesn't care which language it's harvesting from.)

### Mission 6 — killing a runaway batch of jobs

Suppose a `for` loop just launched thirty background jobs and they need to be stopped. (This uses
`ps` and process management, which goes beyond the tutorial page the unit otherwise assigns.)

```bash
# a 'here document' writes a small script inline:
cat > job.py << EOF
import time
time.sleep(1e5)
EOF

nJobs=30
for (( i=1; i<=${nJobs}; i++ )); do
   python job.py > job-${i}.out &
done

# on Linux, sort by start time and take the newest nJobs:
ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C python | tail -n 30
ps -o pid --sort=start_time -C python | tail -n ${nJobs} | xargs kill

# on a Mac, there is no simple sort-by-start-time flag:
ps -o pid,command | grep python | cut -d' ' -f1 | tail -n ${nJobs} | xargs kill
```

If the jobs were started all at once, their process IDs are usually consecutive, in which case
brace expansion is a shortcut for `kill` over a whole range at once:

```bash
kill {871841..871870}
```

## Regular expressions

Regular expressions ("regex") are a small domain-specific language for describing patterns in
text, used inside UNIX tools (`grep`, `sed`, `awk`) and inside Python's `re` and R's `stringr`.
Full regex syntax is not part of this material — it lives in the external tutorial named in
Sources, and Unit 5 of the course returns to it for string processing in Python. What belongs here
is the orientation: what regex are for, when *not* to reach for them, and how the flavors differ.

Regex are well suited to:

- extracting pieces of text out of a larger document,
- turning matched text into variables,
- cleaning and reformatting text into a uniform shape, and
- mining unstructured or semi-structured text by treating it as data (including, in principle,
  scraping the web).

They are the wrong tool when a format has real structure that a dedicated parser already
understands — HTML, XML, JSON. A library that knows the grammar of those formats will do the job
more reliably than a regex trying to approximate it, and the regex version is more likely to break
on an edge case the format's own grammar handles for free.

### Extended, basic, and Perl-flavoured regex

The same-looking regex syntax is not quite one language. `man grep` distinguishes *basic* regular
expressions (the least functionality), *extended* regular expressions (the standard, and what the
course's reference tutorial documents in full), and *Perl*-style regular expressions (a superset,
with extra functionality such as lookaround and named groups that this course does not cover). In
practice:

- In bash, `grep -E` (or `egrep`) turns on extended regex; `grep -P` turns on Perl-style regex.
- Python's `re` module uses syntax described as "similar to" Perl's.
- R's `stringr` uses *ICU* regular expressions, themselves based on Perl's.

Extended regex syntax should carry over to Python and R without much friction, but an unexplained
mismatch in behavior is often exactly this version difference showing up.

### Building and debugging a regex

Because the syntax is so concise, the advice that applies to any other code applies here too:
build a regex up in small pieces rather than writing the whole pattern at once, and check what each
piece actually matched. `re.findall` in Python, `str_detect` in R's `stringr`, and the interactive
tester at regex101.com are all useful for seeing *what* was matched, which is most of what makes
debugging a wrong regex tractable.

## Exercises

The course's own challenge problems for this unit. Different years of the course phrase the same
challenge slightly differently; where they differ in a way that changes the problem, both versions
are given.

1. Consider the file `cpds.csv`. Write a shell command that returns "There are 8 occurrences of the
   word 'Belgium' in this file.", where 8 is replaced by the correct count. Extend your code into a
   function that takes any file and any word of interest as arguments.

2. Consider `RTADataSub.csv`, a subset of freeway travel-time data for an Australian city. First,
   find the unique values in the fourth column. Then automate checking whether any of those values
   are non-numeric, using the pattern `[^0-9]` (anything that is not one of the digits 0-9), rather
   than scanning the unique values by eye. As an extension, do this for every column except the
   first, and print the result in a form someone who didn't write the code could read; you may
   assume the number of columns is known in advance.

3. For Belgium, find the minimum unemployment value (field 6) in `cpds.csv`, programmatically, and
   print it as "Belgium 6.2". Then: store the unique country names in a variable, having stripped
   the surrounding quotation marks (and, since one entry is "New Zealand", having dealt with the
   space inside a country's own name). Automate the calculation across every country, and print
   each result to the screen — and then figure out how to write the results to a new file instead.

4. Return to `RTADataSub.csv` and its missing values, marked with `x`. Create a new file with every
   row containing an `x` removed. Turn this into a function that also reports, to `stdout`, how many
   rows it removed — written so that the function's own output can be piped further. Then generalize
   the function so the caller supplies both the missing-value marker and the input filename.

5. Consider the `coop.txt` weather-station file again. Use `grep` to find the byte offset at which
   the state field starts, by searching for a known state/country combination and finding the flag
   that makes `grep` print a byte offset for a match. Use that offset to automate the field
   extraction that Mission 1 did by eye with `cut`, doing the necessary arithmetic in the shell.

6. A CSV file has quoted fields that themselves contain commas:

   ```
   1,"America, United States of",45,96.1,"continental, coastal"
   2,"France",33,807.1,"continental, coastal"
   ```

   `cut` cannot handle this correctly, because it treats every comma as a field separator (a real
   CSV parser, such as pandas' `read_csv`, can). Find a way to turn this into a new file delimited by
   something other than a comma, so that `cut` becomes usable on it. At least one solution for this
   particular file needs nothing beyond simple, fixed-pattern substitution — no regex required.

7. Write regular expressions that match exactly:

   - the strings "cat", "at", and "t" (and nothing else);
   - "cat", "caat", "caaat", and so on — any number of `a`s, one or more, followed by "t";
   - "dog" in any mixture of upper and lower case ("Dog", "dOg", "DOg", ...);
   - any line consisting of exactly two words separated by any amount of whitespace, allowing for
     (but not requiring) leading or trailing whitespace;
   - any positive number, with or without a decimal point.

8. More open-ended: what regex would detect a number, whether integer- or real-valued? Approach it
   test-driven — before writing the pattern, write out the test cases: strings you want it to match,
   tricky strings that are not numbers and must not match, and "corner cases" you suspect might trip
   up a first attempt.

## Sources

- Shell basics, the six worked "missions", the six challenge problems, and the regular-expressions
  orientation: berkeley-stat243 fall-2025, `units/unit3-bash.qmd`, converted as
  `fall-2025/units/unit3-bash/01-1-shell-basics.md` through `04-5-regular-expressions.md`. Used as
  the primary text (CC BY 4.0).
- Cross-checked against the near-identical fall-2024 version of the same file
  (`fall-2024/units/unit3-bash/01-1-shell-basics.md` through `04-5-regular-expressions.md`, CC BY
  4.0). fall-2025 adds the MacOS `ls --all` caveat, two extra references, and the `kill {a..b}`
  brace-expansion shortcut in Mission 6; otherwise the two are the same text.
- Cross-checked against stat243-fall-2021, `units/unit3-bash.pdf`
  (`stat243-fall-2021/units/unit3-bash/01-unit-3-the-bash-shell-and-unix-utilities.md` through
  `05-5-regular-expressions.md`, CC0-1.0). This file is a model's reconstruction of a PDF with no
  extractable text layer and is flagged by its own header as unverified prose; it is used here only
  for material that does not appear in the later years — the R/`library()` variant of Mission 5, the
  unquoted-filename caveat in Mission 4, the "New Zealand" caveat in Exercise 3, and the five
  concrete regex-matching problems in Exercise 7.
- **Not used**: this task's input list also included four files from berkeley-stat243 fall-2026,
  `units/unit3-goodPractices.qmd` (an overview, "Good coding practices", "Debugging and
  recommendations for avoiding bugs", and "Reproducible research"). In the fall-2026 offering the
  shell material moved to `unit2-bash` and unit 3 became a different topic entirely (coding style,
  debugging, and reproducibility); those four files belong to that other topic, not to shell basics,
  and nothing from them appears above.
- Referred to by the lecture but not supplied as material: the external bash shell tutorial the
  unit is built around (`berkeley-scf.github.io/tutorial-using-bash`, also mirrored at
  `computing.stat.berkeley.edu/tutorial-using-bash`) and its regex page; Newham and Rosenblatt,
  *Learning the bash Shell*, 2nd ed.; Irving et al., *Research Software Engineering with Python*;
  Duncan Temple Lang's regular-expressions tutorial (illustrated in R); sections 9.9 and 11 of Paul
  Murrell's *Introduction to Data Technologies*; the `stringr` regex cheatsheet; the regex101.com
  interactive tester; and the datasets and repositories the worked examples operate on but do not
  contain — `coop.txt(.gz)`, `cpds.csv`, `RTADataSub.csv`, and the `berkeley-stat243/fall-2025` and
  `stat243-fall-2020` GitHub repositories cloned during the examples.

---

[← 40. Data Storage, Formats, and I/O](40-data-storage-formats-and-i-o.md) · [Contents](index.md) · [42. Good Practices, Debugging, and Reproducibility →](42-good-practices-debugging-and-reproducibility.md)
