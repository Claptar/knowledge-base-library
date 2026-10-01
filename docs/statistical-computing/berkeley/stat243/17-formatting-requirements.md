---
title: "17. Formatting requirements"
course: "Berkeley Stat 243"
chapter: 17
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Formatting requirements

## What this covers

Every problem set in Stat 243 opens with a short, un-mathematical section titled "Formatting
requirements," followed by the actual problems. This chapter is about that opening section: what a
computational solution has to look like before it is even graded on content, and why the rules are
shaped the way they are. It draws on four offerings of the same problem set 1 supplied here — Fall
2021, Fall 2024, Fall 2025 and Fall 2026 — because the requirements are close to identical in intent
across all four but the concrete tooling changed each time, which is itself informative about what
the rules are actually protecting. It assumes nothing beyond having some code to submit; the specific
languages and libraries the exercises use (R, Python, bash, web scraping, an HTTP API) appear only as
illustration.

## A rendered document, not a report about one

Reading straight down the requirements, the sentence that explains all the others is this one, from
the grading-rubric note repeated (with small wording changes) in every year:

> "the output should be produced as a result of the code chunks being run during the rendering
> process, not by copy-pasting of output from running the code separately (and definitely not as
> screenshots)."

The clearest statement of *why* comes from a problem rather than the rules: the 2026 climate-data
question tells students that "you can't say 'I downloaded the data from such-and-such website' or 'I
unzipped the file'; you need to provide the ... code that someone else could run to repeat what you
did." Put those together and the whole chapter is really one requirement stated twice: the artifact
you submit has to be capable of regenerating itself, because that is the only way a grader — or you,
in six months — can trust that the output shown actually came from the code shown.

The mechanism for this across all four years is the same: a single **dynamic document** — an R
Markdown/knitr file named `ps1.Rmd`, or a LaTeX+knitr file `ps1.Rtex`, in 2021; a Quarto file
`ps1.qmd` from 2024 on — that interleaves prose with executable code chunks and is *rendered* to
produce the submitted PDF. Nothing in the PDF should exist that the render did not put there.

Two wrinkles worth keeping separate from the general rule:

- **You can still keep code outside the document.** Longer functions can live in a separate `.py`
  file (or an R file read in via a chunk), and be *displayed* inside the qmd using
  `inspect.getsource()` — so the file stays importable and lintable while the rendered document still
  proves that the code shown is the code that ran.
- **Not every chunk type behaves the same way.** The 2026 offering, which uses bash chunks instead of
  Python, warns explicitly that bash chunks do not retain variables from one chunk to the next the
  way Python chunks do — a state-management gotcha specific to that year's tooling, and reason enough
  for the instructions to say: test a dummy file with a bash chunk well before the deadline.

## What must actually be submitted, and where

Two destinations, every year: a rendered **PDF to a grading portal** (Gradescope in
2021/2024/2025, "Pensive" in 2026), and the **full set of working files committed to GitHub** — the
source document, any separate code files it reads in, and the final PDF — named according to that
year's submission-guidelines page. From 2024 on, one more file joins that list: an **environment
file**, based on pip or Conda, recording the package versions the code was actually run with.

That environment file is a good example of how the general rule only becomes concrete through a
specific problem: the formatting section just says "your environment file (see problem 4d)" and
points forward — the actual instruction for what to put in it, and why, lives inside problem 4
(reproducing the exact versions needed to re-run a webscraping or API function later). The formatting
rules do not re-explain reproducibility each time; they assume it and delegate the specifics to the
problem that needs it.

## The code itself: text, comments, and attribution

Independent of the document format, three requirements are stable across all four years:

- The solution is not just code. It needs prose describing how the problem was approached and what
  the steps were.
- The code needs comments — at the level of what each function or block does, and additionally,
  wherever a line or construct might be hard to read, a comment saying what it does.
- Output should be illustrative, not exhaustive: short examples that demonstrate the code works, not
  full dumps, and always produced by the render rather than pasted in (the point already made above,
  restated here as a grading instruction).

One requirement appears explicitly only in the 2021 and 2024 formatting sections supplied here,
though it may well persist elsewhere in the syllabus for the other years: name any students you
worked with (or state that you worked alone), and note in text or code comments any specific idea or
code borrowed from another student or another source. The 2024 wording extends this explicitly to
"ChatGPT or the like" — the only place across the four years where the rules visibly react to a tool
that did not exist when the 2021 version was written.

## How the requirements tracked the toolchain

| Year | Document format | Chunk language | Grading portal | New wrinkle |
|---|---|---|---|---|
| Fall 2021 | `ps1.Rmd` / `ps1.Rtex` (knitr) | R | Gradescope | — |
| Fall 2024 | `ps1.qmd` (Quarto) | Python | Gradescope | code shown via `inspect.getsource()`; explicit "ChatGPT or the like" attribution clause |
| Fall 2025 | `ps1.qmd` (Quarto) | Python | Gradescope | Python module file for problem 4 named explicitly among the required GitHub files |
| Fall 2026 | `ps1.qmd` (Quarto) | bash | "Pensive" | bash chunks don't preserve state between chunks; `sed` encouraged, `awk` discouraged |

The content of the requirements barely moved — comment your code, show your reasoning in prose,
submit both a rendered PDF and the material that rendered it — while the specific tool for enforcing
"the output must come from running the code" changed with whatever language the problems were
written in that year.

## Exercises

The course's own problem set 1, restated cleanly from the offerings supplied, grouped by the
recurring themes rather than repeated year by year. Not solved here.

1. **Disk versus memory.** Read the linked lecture notes on computer architecture and, in a few
   sentences, explain the difference between disk and memory. (The 2024/2025/2026 versions add: note
   what kind of situation would run you out of disk space, and what kind would run you out of memory.
   The 2021 version instead points at a short piece on the memory hierarchy and the CPU cache, and
   asks only that you get the big picture of what a cache is.)

2. **Text versus binary storage.** (2021, 2024, 2025 — dropped in 2026.)
   a. Generate a matrix of random standard-normal numbers, with a fixed number of columns, sized so
      that it occupies a target amount of disk space (about 16 MB in 2024/2025, about 100 MB in
      2021). Show, in typeset arithmetic, how you chose the number of rows.
   b. Write the matrix out both as a plain-text CSV and as a binary file (a pickle in Python; an
      `.Rda` file with `save()` and `compress = FALSE` in R). Explain the size of each file, and
      estimate from first principles — not by counting characters programmatically — how many
      characters the CSV should contain. Would rounding every number to four decimal places before
      writing have changed the comparison?
   c. Explain why writing one number per row, rather than several separated by commas, does not
      shrink the file by much.
   d. Compare the time to read the CSV against the time to read the binary file, reading a few times
      and noting that the first read of a file can be slower than later ones because the operating
      system caches it in memory.
   e. Time reading a fixed-size chunk from the start of the file against reading the same size chunk
      from partway through it (using `nrows`/`skiprows` in pandas, or `skip`/`nrows` in R, or a
      connection read sequentially in R). Does the timing tell you whether the reader has to pass
      over the earlier rows to get there, or can skip them?
   f. (2021 only) Write a second matrix of the same size but with every entry equal, compress it, and
      compare its compressed size to the compressed size of the random matrix. What does the
      comparison suggest about what compression can and cannot do?

3. **Applying the course's code-style guidance.** Read the "code syntax and style" material from the
   good-practices unit and put it to work in your solution to the webscraping/API problem below.
   Lint the code (with `ruff` or a tool of your choice). In a few sentences, say what in your solution
   reflects that reading, and note anywhere you disagree with its stylistic advice.

4. **Extracting structured data from the live web**, in one of three forms depending on the year:
   a. *(2021)* Given a song title and artist, search a lyrics site programmatically, resolve the case
      where the search returns a disambiguation table rather than a single song, and return the
      lyrics, artist and album(s) — failing gracefully, and without hardcoding a match. Throttle
      repeated requests to avoid triggering rate-limit errors from the site.
   b. *(2024)* Given a researcher's name, locate their Google Scholar ID from the HTML of a search
      page, construct and submit the citation-query request for that ID, and parse the resulting HTML
      into a table of title, authors, journal, year and citation count. Handle the case where Google
      Scholar starts returning 429 errors because it has detected automated use.
   c. *(2025)* Using the GitHub REST API, retrieve the commit history of a public repository into a
      dataframe, respecting both the 100-results-per-request limit and the 60-requests-per-hour rate
      limit; plot the distribution of commits per committer; and write a function that identifies the
      most active committer and reports information about them, with a verbosity flag.

5. **The ethics of scraping.** (2021, 2024.) Read the `robots.txt` file of the site(s) you queried in
   the previous exercise, alongside the course's material on the ethics of webscraping, and say
   whether what you did there looks permitted.

6. **A shell-only reproducible pipeline.** (2026, replacing 2 and 4 above.) Using only bash — except
   for a small plotting script — download a chosen span of years of daily climate-station data from
   the Global Historical Climatology Network into a temporary location, reporting the number of
   observations found per year (including zero); identify a specific weather station programmatically
   from the network's station list, without hardcoding its ID, and subset the downloaded data to that
   station's maximum-temperature readings for one month; hand the result to a short script that plots
   one boxplot per calendar day; and then generalize the download-and-subset step into a shell
   function, parameterized by a location string, a variable name and a year/month range, that
   validates its own arguments, supports a `-h` help flag, and removes the raw files it downloaded.

## Sources

- Formatting-requirements section of problem set 1, four offerings of Stat 243 (Berkeley), converted
  to markdown from the course repositories:
  - Fall 2024: `docs/statistical-computing/berkeley/stat243/fall-2024/ps/ps1/01-formatting-requirements.md`
    (CC BY 4.0, lossless conversion from `ps1.qmd`).
  - Fall 2025: `docs/statistical-computing/berkeley/stat243/fall-2025/ps/ps1/01-formatting-requirements.md`
    (CC BY 4.0, lossless).
  - Fall 2026: `docs/statistical-computing/berkeley/stat243/fall-2026/ps/ps1/01-formatting-requirements.md`
    (CC BY 4.0, lossless).
  - Fall 2021: `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/ps/ps1/01-formatting-requirements.md`
    (CC0-1.0, reconstructed by a model from a PDF with no text layer — used here only for its stated
    policies, not for any exact wording or equation).
- Problems section of the same problem set, same four offerings, used for the Exercises:
  `docs/statistical-computing/berkeley/stat243/fall-2024/ps/ps1/02-problems.md`,
  `docs/statistical-computing/berkeley/stat243/fall-2025/ps/ps1/02-problems.md`,
  `docs/statistical-computing/berkeley/stat243/fall-2026/ps/ps1/02-problems.md`,
  `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/ps/ps1/02-problems.md`.
- Referred to but not contained in these files, and not part of this chapter: the "dynamic documents"
  tutorial, the CMU computer-architecture notes, the course's Unit 2 (reading/writing data), Unit 4
  (good programming practice) and Unit 5 (string processing) materials, the grading rubric pages, and
  the yearly submission-guidelines pages — each is linked from the source documents but its content
  was not supplied here.
- No slides or lecture transcript were supplied for this chapter; the material is entirely from the
  course's own written problem-set instructions.

---

[← 16. The Final Project](16-the-final-project.md) · [Contents](index.md) · [18. Reproducible Shell Scripting and Testing →](18-reproducible-shell-scripting-and-testing.md)
