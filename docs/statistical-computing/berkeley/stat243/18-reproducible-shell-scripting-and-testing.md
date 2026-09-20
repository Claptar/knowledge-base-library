---
title: "18. Reproducible Shell Scripting and Testing"
course: "Berkeley Stat 243 Fall 2024"
chapter: 18
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. Reproducible Shell Scripting and Testing

## What this covers

This chapter works through Problem Set 2 of Statistical Computing (stat243), given in three
different years (stat243-fall-2021, fall-2024, fall-2025) with the same two-part structure each
time: turn a manual, one-off command-line analysis into a script that could be handed to someone
else and rerun, and add documentation, defensive error-handling and automated tests to code
already written for Problem Set 1. It assumes basic shell commands, `sed`, and either R or Python
at the level built up in PS1, plus the dynamic-document toolchain (R Markdown or Quarto) used to
submit that assignment.

## Reproducibility as a submission requirement, not a virtue

Across all three years, the comments state the same rule in slightly different words: "you can't
say 'I downloaded the data from such-and-such website' or 'I unzipped the file'; you need to give
us the bash code that we could run to repeat what you did" (fall 2024 / fall 2025), and
identically in spirit in 2021 ("Your solution should not just be code – you should have text
describing how you approached the problem"). The point of the requirement is to make
reproducibility costly to fake: a narrated description of what you clicked on cannot be checked,
but a shell script can be rerun. Every step of the problem set — downloading, subsetting,
plotting — has to exist as saved commands, not as a memory of what was typed at a prompt.

## Building a shell pipeline that downloads and subsets data

The running example in fall 2024 and fall 2025 is to automate a small piece of climate-data
analysis: for a given weather station and month, download the yearly data files from the Global
Historical Climatology Network, subset to the station and variable of interest, and combine the
result into one file, so the pipeline can be rerun for a different station or month without being
edited by hand. Doing this cleanly forces a few shell habits that the comments flag explicitly:

- Download into a temporary directory, and only for the years actually needed — not the whole
  archive.
- Report what happened as you go (fall 2025: print the number of observations found for each
  year, including zero, to stdout — but *only* that, not the download's own progress messages). A
  script that mixes its real output with incidental logging is not safely pipeable to another
  command.
- Look up the station's ID **programmatically**, from the `ghcnd-stations.txt` index file one
  level up in the same data repository, rather than typing in a code found by eye. A hard-coded ID
  silently stops being reproducible the moment someone reruns the script against a different
  station.
- Use `sed` for the text processing — extracting the station's line, subsetting to TMAX and to
  March. None of the three years' problems need `awk`'s field-oriented programming, though it is
  never disallowed.

The same "look it up, don't type it in" and "print only what's asked for" discipline reappears in
the 2021 problem set's agricultural-data exercise below, which adds a technique worth naming on
its own.

## Reverse-engineering a download URL from a web page

The stat243-fall-2021 exercise on UN FAO crop data describes, and expects reuse of, a piece of
detective work done in class: rather than clicking through a web form by hand, inspect the HTTP
requests the page issues (via the browser's developer tools, under Network) and recover the actual
GET request its "Download" button sends — something of the shape

```
http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc
```

Once that URL is known, downloading a different crop's data is a matter of substituting its
`itemCode` — the whole web form becomes one parameterised shell command. Two shell gotchas go with
this: the URL needs to be quoted when passed to a download command, because the shell would
otherwise try to interpret characters such as `&` and `:` itself; and a URL that has been broken
across lines (by a PDF or an editor) must not pick up a stray carriage return, or the request
silently fails.

A second gotcha in the same exercise concerns the downloaded file itself: a CSV of country names
is not safe to split on commas, because some names *contain* commas inside quoted fields. The fix
is to convert the file to a different delimiter first — with `sed`, `awk`, or a one-line call out
to `Rscript` or Python from the shell — before doing any further field-based processing.

## From a script to a function: arguments, help, and cleanup

All three years ask for the same generalisation: turn the ad hoc script into a shell function that
takes structured arguments (a location, a variable, a time period) and can be reused without
editing its body — and to make it behave like a well-mannered command-line tool rather than a
script only its author can run:

- **Validate the argument count and content**, and fail with a message that says what went wrong,
  rather than failing partway through with a cryptic error — for instance, when the location
  string does not identify a single weather station.
- **Support a help flag.** Both the weather-station function (`get_weather -h`, 2024/2025) and the
  FAO function (`myfun -h`, 2021) are required to print usage information when invoked this way —
  the same idiom either way, independent of what the function actually computes.
- **Clean up after yourself.** The function must delete the raw files it downloaded, or download
  into the operating system's temporary location in the first place, so repeated calls do not
  silently accumulate data on disk.
- **Quote your comparisons.** The recurring hint for the `if` tests inside these functions is to
  write

```
if [ "${var}" == "some string" ]
if [ "${var}" != "some string" ]
```

  — the quotes exist so a value containing spaces or shell-special characters is compared as one
  piece of text, rather than being re-split and reinterpreted by the shell.

## Mixing languages inside one reproducible document

The comments for both 2024 and 2025 flag a specific failure: a Quarto (`.qmd`) document with both
a bash chunk and a Python chunk, run with the default `jupyter` engine, does not work, because a
Jupyter notebook is built around a single persistent *kernel* — one running process holding the
state for one language — and two chunks in different languages cannot share it. The fix in both
years is to add `engine: knitr` to the document's YAML header. `knitr`, R's chunk-execution
engine, runs each chunk as its own process rather than routing everything through one kernel, so a
bash chunk and a Python chunk (via R's `reticulate` package, which `knitr` uses transparently) can
coexist in one document. The costs are real: this requires R and the `knitr` package to be
installed even when no R code is written, and, in fall 2025, the specific Python interpreter that
`reticulate` reaches for can be pinned by configuration shown in the class repository's own
`unit2-dataTech.qmd`. Because this toolchain is fragile in exactly the ways that are hard to debug
under deadline pressure, the comments repeat the same advice each year: build a small dummy
document with one bash chunk and one Python chunk and confirm it renders *before* writing the real
analysis, and fall back to a class computing-facility (SCF) machine if it does not work locally —
behaviour on Windows in particular is called out as unreliable. If even that fails, the boxplot
figure for the analysis may be produced by running the Python code separately and inserting the
image by hand.

The stat243-fall-2021 problem set predates Quarto and uses the equivalent R Markdown / LaTeX+knitr
toolchain (`ps2.Rmd` or `ps2.Rtex`), where the same class of bash-chunk trouble appears, especially
on Windows. Its suggested workarounds are to run the terminal inside the Windows Ubuntu subsystem,
to turn on RStudio's notebook mode, and to check whether single versus double quotes in the
document change the outcome. If a bash chunk's output genuinely cannot be captured automatically,
the fallback there is simply to paste the output in by hand rather than to omit it.

## Documentation, defensive programming, and testing

The second half of the problem set, every year, is not new code but *hardening* code already
written for PS1: adding documentation, catching the ways it can fail, and testing it. The specific
tools differ by language, but the design questions are the same each year:

- **Document at the function level.** Add doc strings that say what a function does — fall 2025
  additionally asks for at least one worked example in the doc string for user-facing functions,
  with lighter documentation acceptable for internal helpers.
- **Decide what a failure should do.** For each way a user's input could be wrong, or an external
  dependency could fail (a server refusing the request, the machine being offline), decide whether
  the function should **raise** an error and stop, or **catch** it and return something such as
  `None` so the caller can continue. This is presented as a real design choice, not a single
  correct answer: an error worth stopping for and an error worth absorbing look different
  depending on what the function promises to its caller. The fall-2025 version sharpens this
  further for code that parses structured data returned by a web API: since the shape of that JSON
  is not fully under your control, the code should be robust to a key being missing or structured
  differently than expected, and should prefer a warning over a silent failure when execution can
  reasonably continue.
- **Test the tricky cases, not just the typical one.** In Python this means using `pytest` to write
  "a thoughtful set of unit tests"; in the 2021, R-based version of the same assignment, the
  equivalent tools are `assertthat`, for formal assertions inside the function itself that catch
  bad input at the point it enters, and `testthat`, for a separate suite of unit tests. Both years'
  instructions single out the same instinct: think about which inputs are likely to break the
  code, not only which inputs make it work.

## Reproducibility as something to evaluate, not just practice

The stat243-fall-2021 problem set closes with an exercise that turns the lens around: instead of
writing reproducible code, read about reproducible-research practice and then critique someone
else's. The reading list (any one item, though more are welcome) is:

- Christensen et al., *Transparent and Reproducible Social Science Research*, chapter 11;
- Gentzkow and Shapiro, on code and data for the social sciences;
- Wilson et al., *Best Practices for Scientific Computing* (arXiv:1210.0530);
- Millman and Perez, on reproducible research (class repository,
  `stat243-fall-2014/section/millman-perez.pdf`);
- the Preface, Basic Reproducible Workflow Template, and Lessons Learned chapters of *The Practice
  of Reproducible Research*.

Having read one, the assignment asks for a short written reflection on which practices seem
compelling versus not, which are already used and which are not (and why, beyond simple
unawareness), why researchers do not consistently adopt them, and which practices belong more to
data analysis versus to software engineering.

The second half of that exercise is a concrete case study: skim the methods section of a supplied
paper (`ps/clm.pdf`) and look at the authors' own shared code (the `hhLocation` repository), then
judge — from the documentation alone, without working through the code line by line — whether
someone else could actually reproduce the analysis. The questions the problem set poses double as
a checklist for evaluating any shared analysis code: can you tell, just from what is there, where
the data was collected, where it was cleaned, where the statistics were computed, and where each
figure was produced; are the files, comments, naming and workflow good or lacking; and does the
project document its workflow as a whole, not just its individual files.

## Exercises

The Death Valley and PS1-hardening problems are given here in their clearer, later (fall 2025)
phrasing; the fall 2024 problem set sets the same two tasks in near-identical words. The three
problems after those are specific to stat243-fall-2021 and use a different dataset and a
different language's testing tools.

**1. Automating a weather-station query** (fall-2024 / fall-2025 PS2, Problem 1). A friend is
planning a wedding in Death Valley National Park in March and wants it as late in the month as
possible without a high chance of a very hot day. Using data from the Global Historical
Climatology Network, automate the following almost entirely in the bash shell — every step must
exist as shell commands saved in your solution, not narrated as something done by hand.

a. Download yearly climate data for a small set of years of interest (not the whole archive) into
   a temporary directory. As you process the files, report to stdout the number of observations
   found for each year, including years with none, and avoid printing anything else, such as
   download progress.

b. Subset the downloaded data to the station corresponding to Death Valley, to the TMAX (maximum
   daily temperature) variable, and to March, and combine the result into a single file. Determine
   the Death Valley station's ID programmatically from the `ghcnd-stations.txt` index file, rather
   than typing it in by hand.

c. In a Python (or R) chunk, take the single file from (b) and produce one plot of side-by-side
   boxplots of the maximum daily temperature for each calendar day of March.

d. Generalise (a) and (b) into a shell function taking (1) a location string, (2) the weather
   variable of interest, and (3) the time period of interest (years and month), and returning the
   result without the per-year row counts from (a). The function should detect and report, with a
   useful message, a wrong number of arguments or a location string that does not identify a
   single station; should print help when invoked as `get_weather -h`; and should remove the raw
   downloaded files, or download them to the operating system's temporary location.

**2. Hardening PS1 code** (fall-2024 / fall-2025 PS2, Problem 2). Add documentation,
error-handling and tests to the data-retrieval and processing functions you wrote for PS1 (a
modified version of your PS1 solution is fine).

- Add informative doc strings, with at least one example, to every user-facing function, and at
  least basic doc strings to internal ones.
- Add exception handling for the ways a run could go wrong — invalid user input, a server refusing
  the request, being offline — deciding case by case whether to raise an error or to catch it and
  return `None`. Where the code parses structured data from an external source, such as JSON from
  an API, make it robust to that data's shape varying from what you expect, issuing a warning
  rather than failing outright where execution can reasonably continue.
- Write a thoughtful set of unit tests with `pytest`.

**3. Assertions and tests, R version** (stat243-fall-2021 PS2, Problem 1). Add assertions and
testing to your PS1 solution.

a. Use the `assertthat` package to add formal assertions that catch the various ways a user could
   call your functions incorrectly, and anything else that could go wrong, such as not being
   online.

b. Use the `testthat` package to write a small but thoughtful set of tests, aimed particularly at
   tricky cases that might cause problems.

**4. Scraping agricultural production data by URL** (stat243-fall-2021 PS2, Problem 2). The UN FAO
publishes crop-production data through a web form; inspecting the page's own HTTP requests (via
the browser's developer tools) reveals that its "Download" button issues a GET request of the form
`DownloadHandler.ashx?DataFilter=itemCode:526&DataMartId=FAO&Format=csv&...`, where `526` is the
item code for apricots.

a. Using the shell, download the apricot data at this URL, strip out the metadata and the
   global-total row, and subset to the year 2005. Using the "area harvested" column, find the ten
   regions using the most land for apricot production. Then automate this to report the top five
   regions for each of 1965, 1975, 1985, 1995 and 2005, without repeating the code once per year.
   As before, every step must be a saved shell command, not a narrated manual step. Note that
   country names in the CSV can themselves contain commas, so naive comma-splitting will not work;
   converting to a different delimiter first is one way around this.

b. Write a bash function taking a single item code (e.g. 526 for apricots, 572 for avocados) that
   downloads the corresponding data and prints the CSV contents to stdout, so the output could be
   piped to another Unix command. The function should detect a wrong number of arguments and give
   a useful error, and should print help when invoked as `myfun -h`.

**5. Reading and evaluating reproducible-research practice** (stat243-fall-2021 PS2, Problem 3).

a. Read at least one of: Christensen et al., *Transparent and Reproducible Social Science
   Research* (ch. 11); Gentzkow and Shapiro, on code and data for the social sciences; Wilson et
   al., *Best Practices for Scientific Computing*; Millman and Perez, on reproducible research; or
   the Preface and two named chapters of *The Practice of Reproducible Research*. In a short
   written answer (10-15 sentences), address which of the practices described strike you as
   compelling versus not, which you already use and why, why researchers do not consistently adopt
   these practices, and which practices belong more to data analysis versus to software
   engineering, and which to both.

b. Skim the methods section of the supplied paper `ps/clm.pdf`, then look at the authors' shared
   code at the `hhLocation` repository. Without reading it line by line, assess whether you can
   tell from the materials where the data was collected, cleaned, analysed and plotted; what is
   good and what could be improved about the documentation, comments, organisation, naming,
   workflow and data provenance; and whether the authors document their overall workflow, and
   whether that documentation is effective.

## Sources

- `docs/statistical-computing/berkeley/stat243/fall-2024/ps/ps2/01-comments.md` and
  `02-problems.md` — fall-2024 PS2, converted losslessly from `ps/ps2.qmd` (CC BY 4.0).
- `docs/statistical-computing/berkeley/stat243/fall-2025/ps/ps2/01-comments.md` and
  `02-problems.md` — fall-2025 PS2, converted losslessly from `ps/ps2.qmd` (CC BY 4.0); the
  exposition above follows this version's phrasing where fall-2024 and fall-2025 overlap.
- `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/ps/ps2/01-formatting-requirements.md`
  and `02-problems.md` — stat243-fall-2021 PS2. This file is marked `route: llm`,
  `fidelity: reconstructed`: the source PDF had no text layer, and a model reconstructed this
  markdown from the page images, so the prose may paraphrase the original in places. It is used
  here for the year's distinctive material — the `assertthat`/`testthat` exercise, the FAO/apricots
  exercise, and the reproducible-research reading exercise — which does not appear in the later
  years' problem sets.
- Referred to by the source material but not supplied to this chapter, and not otherwise available
  here: stat243's Unit 3 and Unit 4 materials (the lecture content these problem sets build on);
  PS1 and its formatting and attribution requirements; the bash tutorial and Lab 1 / Lab 2
  materials; the class repository's `unit2-dataTech.qmd`; "Chris' solutions" to PS1; the
  `howtos/submitting-electronically.txt` file (2021); and, for Exercise 5, the five reproducibility
  readings themselves, the paper `ps/clm.pdf`, and the `hhLocation` code repository.

---

[← 17. Formatting requirements](17-formatting-requirements.md) · [Contents](index.md) · [19. Problem Set 3 →](19-problem-set-3.md)
