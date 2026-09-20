---
title: "19. Problem Set 3"
course: "Berkeley Stat 243 Fall 2024"
chapter: 19
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 19. Problem Set 3

## What this covers

This chapter is not a lecture but a problem set: "Problem Set 3" of Berkeley's Stat 243
(Statistical Computing), assigned in three different offerings of the course (fall 2021, fall 2024,
fall 2025). All three point back to the course's Unit 5 material and test the same three skills,
dressed in different languages, packages and text corpora: reading how a real Python or R package's
namespace is actually assembled out of nested `import` statements and `__init__.py` files; using
regular expressions and string processing to turn a corpus of real spoken transcripts into
structured per-speaker data; and redesigning a working solution's architecture in the *other*
programming paradigm (functional versus object-oriented) without writing any code for it. It assumes
the reader has already gone through Unit 5's own material on package and module structure (not
itself supplied to this chapter), can read the source tree of an installed package, knows basic
regex syntax, and — for the transcript problem — already has the HTML-downloading code the course
supplies separately as `ps3prob3.py`.

## How the assignment varies across the three offerings

**Package internals.** Every offering asks the same kind of question about a widely used package:
after `import`ing it, what ends up visible, and by what chain of files did it get there? Fall 2024
uses `statsmodels`; fall 2025 uses `pandas`. In both cases the task is to pick specific objects
inside the package and, for each, say what kind of object it is (function, class, or class method,
naming the class and any inheritance if relevant), which file it is actually defined in, and how the
relevant `__init__.py` file(s) make it reachable under its public name. Two practical techniques
recur across both variants: `grep -R <pattern> <directory>` searches an entire source tree for a
name, and building an isolated environment — e.g. `conda create -n test_env python=3.12 statsmodels`
for the 2024 variant, or the pandas equivalent for 2025 — lets you edit the *installed* package's
files (comment out a line, add a print statement, set a debugger breakpoint inside an `__init__.py`)
without touching anything else on the machine.

**Transcripts into structured data.** The other recurring problem takes a corpus of real spoken
text and asks for a full pipeline: strip out everything that was not actually spoken (stage
directions such as "Laughter" and "Applause"), split what remains into chunks — one chunk per
uninterrupted turn by a single speaker, merging consecutive chunks from the same speaker into one —
tokenize each chunk into words, and compute per-speaker, per-transcript statistics such as word and
character counts and average word length. Fall 2024 and fall 2025 both use transcripts of six US
presidential debates (2000, 2004, 2008, 2012, 2016, 2020) from the Commission on Presidential
Debates, chosen because they cover domestic policy and so roughly control for topic; fall 2021 uses
State of the Union addresses from The American Presidency Project instead, done entirely in R
including the downloading. Fall 2025 additionally reframes the exercise around AI-assisted coding:
the student is expected to lean on an AI coding assistant to produce the pipeline, understand every
line of what it produces, and report on the experience (the prompt used, the assistant's errors,
what was learned from the generated code, and an overall verdict) — a framing absent from fall 2024
and fall 2021, whose versions of the problem are solved directly.

**Redesigning in the other paradigm.** Fall 2024 and fall 2025 both close the transcript exercise
with a design-only problem: whichever paradigm (functional or object-oriented) the student used to
solve it, sketch the *other* one — no code, just the classes-with-fields-and-methods or the
functions-with-inputs-and-outputs that the alternative design would need, each with a short comment
on its purpose. Fall 2021 asks the mirror version explicitly as its own second problem, always
object-oriented (the State of the Union exercise was to be done with vectorized R functions and
`lapply`/`sapply` or `purrr::map`, so the redesign asks for the OOP version of that), suggesting R6
classes or the class model of Python or C++, and additionally asking how each method draws on other
fields or methods of its class.

**What is specific to one offering.** Fall 2025 alone opens with an independent short exercise on
detecting numeric literals with regular expressions. Fall 2021 alone closes with an unrelated
problem about deliberately misusing an R language feature to intercept console input, and is also
the only offering where the transcript-processing code (downloading included) has to be written from
scratch rather than supplied.

## Exercises

### 1. Package namespaces and imports

Two variants of the same investigation were assigned; work whichever package you have to hand, or
try the reasoning on any comparable package.

**`statsmodels` variant (fall 2024).**

a. Consider only `import statsmodels` on its own, with no further `import`s. What ends up in the
   `statsmodels` namespace this creates? In which module file is the package's version number
   stored? What is the absolute path to the installed package on your machine?
b. The usual invocation is `import statsmodels.api as sm`. Describe, in terms of which files get
   read, what happens when this line runs. Then describe what kind of object `MICE` is, how it is
   imported, and where it is defined — and do the same for `GLM`.
c. What is in the namespace of `sm.gam`? Describe how the importing works and in which modules the
   objects that appear there are actually defined.
d. What is `sm.distributions.monotone_fn_inverter` — a function, a class, or a class method? How is
   it imported, and in what file is it defined?

**`pandas` variant (fall 2025).**

After `import pandas`, for each of the following: say which namespace it (or its class) belongs to,
which file or module it is defined in, whether it is a function, a class, or a class method (naming
the class and any relevant inheritance), and trace the `import` statement(s) in the relevant
`__init__.py` file(s) that put it where it is.

a. `pandas.core.config_init.is_terminal`
b. `pandas.read_csv`
c. `pandas.arrays.BooleanArray`
d. `pandas.DataFrame.to_csv`

### 2. Detecting numeric literals with regular expressions (fall 2025)

a. Two AI-generated candidate regular expressions for detecting an integer or real number, positive
   or negative, were offered: `-?[0-9]+(\.[0-9]+)?` and `-?(\d+(\.\d+)?|\.\d+)`. What is the
   substantive difference between what the two patterns would match? Is one better than the other?
b. Make the problem concrete: you are writing a CSV reader in Python, and one sub-task is deciding
   whether the text between two commas (with any surrounding quotes already stripped) is a number.
   Write a Python function that takes that text and returns either the detected numeric substring or
   `None`. It should catch plain reals such as `0.35`, `-.35`, `+72`; scientific notation such as
   `1.6e-8` (an integer-or-real mantissa with an integer exponent); and numbers written with a
   thousands separator, such as `12,345.72` (which appears in a raw CSV field as
   `,"12,345.72",`). Everything else should be rejected. (Handling European-style numbers such as
   `12.345,73` as well is an optional extension, not a requirement.)
c. Build a test suite covering a wide range of cases. An informal one — looping over a list of test
   strings and checking the results by hand — is enough; formal `pytest` machinery is not required.

### 3. From transcript to structured speech data

The underlying task is the same regardless of corpus: take a set of real spoken transcripts, strip
out everything that was not actually spoken, split what remains into chunks — one chunk per
uninterrupted turn of speech by a single speaker, merging consecutive chunks from the same speaker
into one — and compute per-speaker statistics from the result.

**Presidential debates (fall 2024, fall 2025).** Work with the transcripts of the 2000, 2004, 2008,
2012, 2016 and 2020 US presidential debates, downloaded and lightly preprocessed by the supplied
`ps3prob3.py`.

a. Split the spoken text of each debate into chunks by speaker (including the moderator), merging
   consecutive chunks from the same speaker and stripping out any non-spoken formatting (such as
   "Laughter" and "Applause" tags). Report the number of chunks per speaker.
b. Tokenize each chunk into individual words — an existing NLP tokenizer or hand-written regular
   expressions are both acceptable; perfect accuracy on spoken text is not expected.
c. For each candidate, in each debate, compute the number of words, the number of characters and the
   average word length, and compare these across candidates and over time.
d. Check your functions against simple test inputs; this does not need to be a formal test suite.
e. *(Extra credit.)* Count occurrences of a chosen set of words or word stems per candidate — for
   example: I, we, America{,n}, democra{cy,tic}, republic, Democrat{,ic}, Republican, free{,dom},
   terror{,ism}, safe{,r,st,ty}, {Jesus, Christ, Christian} — and make one or two plots commenting
   briefly on what they show.

The fall 2025 version of this problem additionally asks you to lean on an AI coding assistant to
produce the pipeline in (a)-(d), while understanding every line of the resulting code in detail:

f. Report the prompt you used to first ask the assistant for help.
g. Describe some errors, minor or major, the assistant's code made.
h. Describe something you learned about Python from reading through the AI-generated code.
i. Report on the overall experience: how much you needed to modify the code yourself or by
   iterating with the assistant, whether any syntax needed further investigation, and whether this
   style of coding felt more efficient than writing the code unaided.

**State of the Union addresses (fall 2021, in R).** Unlike the debate variant, no downloading code
is supplied: the pipeline, from fetching the HTML to the finished statistics, has to be built
entirely in R.

a. From The American Presidency Project's index page, extract the URL of each speech and read each
   one into R.
b. For each speech, extract the body of the speech and its year.
c. Strip out all text that was not spoken by the president, saving it separately; count how many
   times "Laughter" and "Applause" each occur.
d. Extract words and sentences from each speech as character vectors, one element per sentence and
   one per word, handling the special cases you find as far as reasonably possible.
e. For each speech, compute the number of words and characters and the average word length.
f. Count occurrences of a chosen set of words or word stems, for example: I, we, America{,n},
   democra{cy,tic}, republic, Democrat{,ic}, Republican, free{,dom}, war, God (not counting "God
   Bless"), "God Bless" itself, {Jesus, Christ, Christian}, and any others you think are interesting.
g. Assemble the results into one or more well-structured data objects.
h. Make basic plots of how these variables change over time, and of whether they differ between
   Republican and Democratic presidents since Franklin Roosevelt (1932). This does not need to be an
   extensive analysis — just illustrate what a fuller exploratory analysis would look like.
i. *(Extra credit.)* Devise additional variables that quantify the speeches in some interesting way,
   and plot how they change over time.

(Hint: if a list ends up with element names that are themselves huge strings — a whole speech or a
whole HTML page — `names(myObj) <- NULL` clears them.)

### 4. Redesigning your solution in the other paradigm

Having solved the transcript-processing exercise in one paradigm, sketch — design only, do not write
any code — a solution in the other one.

- If your solution was object-oriented, design the functional-programming version: for each function
  you would need, list its inputs and its output, with a short comment on its purpose.
- If your solution was functional, design the object-oriented version: for each class you would
  need, list its fields and its methods, with a short comment on the purpose of each, and note where
  a method relies on other fields or methods of the class (or of a related class, if there is an
  inheritance structure).

### 5. Hijacking the console's quit keystroke (fall 2021)

a. Suppose you want typing `k` alone at the R or RStudio console, followed by enter, to quit R
   immediately with no confirmation prompt. What R function call, with what argument, quits R
   without asking any questions? What sequence of steps does R actually carry out when you type `k`
   and press enter — and how could you arrange for your quit call to run in its place? (Keep this
   code in a chunk that does not evaluate when the document is knitted: if it works, it will quit R
   before knitting can finish.)
b. Now try to achieve the same effect by typing `q` instead of `k`. Does it work? If so, explain how
   your own `q` and R's built-in `q()` function manage to coexist.

## Sources

- `docs/statistical-computing/berkeley/stat243/fall-2024/ps/ps3.md` — converted losslessly from
  `ps/ps3.qmd` in the berkeley-stat243 fall-2024 repository, CC BY 4.0. Source for Exercises 1
  (`statsmodels` variant), 3 (debate-processing, parts a-e), and 4.
- `docs/statistical-computing/berkeley/stat243/fall-2025/ps/ps3.md` — converted losslessly from
  `ps/ps3.qmd` in the berkeley-stat243 fall-2025 repository, CC BY 4.0. Source for Exercise 2, for
  Exercise 1 (`pandas` variant), and for Exercise 3 (debate-processing, all parts including the
  AI-assistance parts f-i).
- `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/ps/ps3.md` — reconstructed by a
  model from a PDF with no extractable text layer (berkeley-stat243 stat243-fall-2021 repository,
  CC0-1.0); its own source note flags the prose as a paraphrase and every detail as unverified.
  Source for Exercise 3 (State of the Union variant), Exercise 4 (as the offering's own second
  problem), and Exercise 5. Treat exact wording, hints and word lists drawn from this file as a
  pointer to the original PDF rather than settled fact.
- Referred to by all three problem sets but not contained in any of them, and not reproduced here:
  the course's Unit 5 material on package and module structure, which every offering assumes has
  already been covered; the earlier problem set(s) each offering points back to for formatting (and,
  in 2024, attribution) requirements; the `ps3prob3.py` download-and-preprocessing script, supplied
  separately in each course's GitHub repository; the source code of `statsmodels`, `pandas`, and R
  itself; and the transcripts themselves, hosted at debates.org (the Commission on Presidential
  Debates) and at the American Presidency Project (UC Santa Barbara).

---

[← 18. Reproducible Shell Scripting and Testing](18-reproducible-shell-scripting-and-testing.md) · [Contents](index.md) · [20. Problem Set 4 →](20-problem-set-4.md)
