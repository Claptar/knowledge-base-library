---
title: "12. Version Control and Dynamic Documents"
course: "Berkeley Stat 243 Fall 2024"
chapter: 12
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Version Control and Dynamic Documents

## What this covers

This chapter is a practical setup guide for turning in problem sets in the course: how to get a
local Git repository talking to a GitHub repository, how to write a problem set as a *dynamic
document* that mixes narrative and executable R code (R Markdown, and its older relatives R Sweave
and Rtex), and what house style is expected of the R code itself. It assumes no prior exposure to
Git, knitr, or R Markdown, and no mathematics — it is entirely about the tools.

## Version control with Git and GitHub

A repository can be started two ways: create it on GitHub first and `git clone` it down, or run
`git init` locally and connect it to a remote afterwards. Starting on GitHub is the more common
route for a new problem set repo:

- sign in to GitHub, click the `+` next to your avatar, choose **New repository**;
- give it a name (e.g. `demo-repo`) and a short description;
- add a `.gitignore` for R, so that machine-generated files such as `.Rhistory` never get committed;
- click **Create repository**.

The repository now exists on GitHub but not on your machine. `git clone` copies it down:

```
git clone https://github.com/berkeley-scf/tutorial-git-basics
```

### The add–commit–push cycle

It is customary to add a `README.md` at the top level describing what the repository is for:

```
echo "# Demo Repo" >> README.md
```

At this point the file exists in the working directory, but Git has not recorded anything about it
— `git status` will report it as *untracked*. Git works in three stages, and a new or changed file
has to be moved through all three explicitly:

```
git add README.md      # stage the change
git commit -m "Create README"   # record it in the local history
```

`git status` after each step shows the file moving from untracked, to staged, to part of a commit.
Committing only updates the *local* repository; the remote copy on GitHub is untouched until you
push:

```
git push origin master
```

This uploads the commit from the local branch (`master`) to the remote (`origin`). Refreshing the
GitHub page in a browser should now show the updated `README.md`.

If a collaborator (or you, from another machine) has changed the remote repository, your local copy
is now behind it. Attempting to push in that state fails; the fix is to pull first, merging the
remote changes into your local copy before pushing your own:

```
git pull
```

### The workflow, end to end

Put together, the cycle for getting any change from your machine onto GitHub is:

1. **Pull** — only needed if the local repo might be out of date with the remote.
2. **Edit** — make or change files locally.
3. **Add** — stage the files you touched.
4. **Commit** — record the staged changes with a helpful message.
5. **Push** — upload the commit to the remote branch.

<figure>
<svg viewBox="0 0 660 190" role="img" aria-label="The git workflow as a cycle: pull, edit, add, commit, push, and back to pull.">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0 0, 8 4, 0 8" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <rect x="20" y="40" width="90" height="50" rx="4"/>
    <rect x="150" y="40" width="90" height="50" rx="4"/>
    <rect x="280" y="40" width="90" height="50" rx="4"/>
    <rect x="410" y="40" width="90" height="50" rx="4"/>
    <rect x="540" y="40" width="90" height="50" rx="4"/>
  </g>
  <g font-size="13" text-anchor="middle" fill="currentColor">
    <text x="65" y="70">Pull</text>
    <text x="195" y="70">Edit</text>
    <text x="325" y="70">Add</text>
    <text x="455" y="70">Commit</text>
    <text x="585" y="70">Push</text>
  </g>
  <g stroke="currentColor" stroke-width="1.5" fill="none" marker-end="url(#arrow)">
    <line x1="110" y1="65" x2="148" y2="65"/>
    <line x1="240" y1="65" x2="278" y2="65"/>
    <line x1="370" y1="65" x2="408" y2="65"/>
    <line x1="500" y1="65" x2="538" y2="65"/>
    <path d="M 585 90 C 585 150, 65 150, 65 90"/>
  </g>
  <text x="330" y="175" text-anchor="middle" font-size="12" fill="currentColor">repeat: pull again before the next round of edits</text>
</svg>
<figcaption>The basic Git–GitHub workflow: pull to sync, edit locally, then add, commit, and push
the change back to the remote before the cycle repeats.</figcaption>
</figure>

## Dynamic documents: combining code and narrative

A problem set is not just code — it needs to be handed in with commentary, and its output (numbers,
plots) needs to match the code that produced it. The traditional way to do this is to run the code
separately and paste the results into a report; the fragility of that approach (results going stale
the moment the code changes) is what dynamic documents solve. An **R Markdown** (`.Rmd`) file lets a
single plain-text file hold both the narrative and the R code that produces the numbers the
narrative refers to, so the report and the computation cannot drift apart. RStudio also supports
other dynamic-document formats (`.Rnw`, `.Rpres`, `.Rhtml`), but `.Rmd` is the default.

Rendering an `.Rmd` file is called **knitting**. In RStudio this is the "Knit HTML" button (a ball
of yarn and knitting needles), or the shortcut `Command+Shift+K` (Mac) / `Ctrl+Shift+K` (Windows).

### Anatomy of an `.Rmd` file

An `.Rmd` file is plain text and uses three syntaxes at once:

- A **YAML header** at the very top, delimited by a line of three dashes (`---`) before and after.
  This sets document-wide metadata: `title`, `author`, `date`, `output`, and so on.
- The **body**, everything below the header, written mostly in **Markdown** (with LaTeX math
  allowed inline).
- **R**, embedded in the body inside blocks of code.

Code appears in the body two ways: as a **code chunk** — a block of R set off from the surrounding
narrative — or as **inline code**, a short expression embedded directly in a sentence.

One recurring point of confusion: `#` means something different depending on where it appears.
Inside a code chunk it is an R comment, exactly as in a `.R` script. Outside a code chunk, in the
Markdown body, `#` marks a heading level instead.

### What knitting actually does

Knitting an `.Rmd` file runs through three phases:

1. **Parsing** — the file is read line by line and classified into YAML, Markdown text, or R code.
2. **Execution** — the R code is run where required, and its commands and/or output are captured.
3. **Rendering** — everything is assembled into a single output document in the requested format
   (HTML, PDF, Word, ...).

### Code chunk options

A handful of chunk options control what happens in the execution and rendering phases:

- `cache`: whether to store results so the chunk need not be re-run on the next knit (`TRUE`/`FALSE`).
- `eval`: whether the code is evaluated at all (`TRUE`/`FALSE`).
- `echo`: whether the code itself is shown in the output — `TRUE`, `FALSE`, or specific line numbers.
- `error`: whether an error in the chunk halts knitting (`TRUE`/`FALSE`).
- `results`: how output is displayed — `markup`, `asis`, `hold`, or `hide`.
- `comment`: the character prefixed to each line of printed output, `##` by default, or `""` for a
  cleaner look.

Inline code — a short R expression evaluated in the middle of a sentence, e.g. `` `r 2 + 2` `` — lets
narrative text report a computed number (here, 4) without it ever being typed by hand, so the text
cannot go stale relative to the code.

### LaTeX in R Markdown

Rmarkdown documents can contain LaTeX math, rendered through an external LaTeX installation. Inline
math is set off with single dollar signs, e.g. `$\beta$` renders as $\beta$. Display equations use
double dollar signs, `$$ ... $$`, for anything larger — for example a piecewise definition such as

$$
D(\theta_l,T_x) = \left\{
         \begin{array}{ll}
             \theta_{l[0]}^{'}=\theta_l 								& \quad i = 0 \\
             \theta_{l[i+1]}^{'} = \theta_{l[i]}^{'} *F(\overline{L_{[t-i-T_x]}})	& \quad i \leq T_l
         \end{array}
     \right.
$$

## Alternatives to R Markdown: Sweave and Rtex

R Markdown is not the only way to knit code and narrative together.

**R Sweave** (`.Rnw`) produces a LaTeX document instead of Markdown-based output. The chunk options
are the same ones used for `.Rmd` (`cache`, `eval`, `echo`, and so on), but the delimiter syntax for
a chunk is different: a chunk opens with `<<>>=` and closes with `@`, rather than the triple
backtick fences used in `.Rmd`. To create one, choose **File → New File → R Sweave** in RStudio, and
compile with the **Compile PDF** button.

By default RStudio processes `.Rnw` files with the older Sweave engine rather than knitr; knitr is
the more actively maintained of the two and formats output better. To switch, change **RStudio →
Preferences → Sweave** to weave `.Rnw` files using knitr. One side effect: a new Sweave file created
before switching engines will contain the line `\SweaveOpts{concordance=TRUE}`, which must be
removed once the engine is changed to knitr.

**Rtex** is a third option: also a LaTeX-based format, also processed through knitr. RStudio's
support for it is weaker than for `.Rmd` or `.Rnw` — there is no menu item to create one, and it
must be compiled from the command line.

## Code style

Beyond the mechanics of writing and knitting a document, a problem set is graded partly on the
readability of the R code itself. There is no requirement to follow any particular published style
guide exactly — pick a style, and apply it consistently — but the following are expected regardless
of which guide (if any) is used as a starting point:

- use whitespace to make code easier to read;
- keep lines to no more than 80 characters;
- give objects and functions meaningful names that are not excessively long;
- comment the code;
- indent consistently, so that the blocks a piece of code is organised into are visually clear.

One specific naming rule: **do not use periods inside object or function names**, even though this
is what Google's R style guide recommends. The reason is that R's S3 object system gives periods a
specific meaning (a method name like `predict.lm` is dispatched on the class after the dot), and
periods carry object-oriented meaning in other languages too. Prefer `calculate_mle` or
`calculateMLE` over `calculate.mle`.

## Sources

- Berkeley STAT 243, Fall 2021, discussion section 01, *Getting started with Git and GitHub*
  (converted `sections/01/intro_git_knitr.Rmd`, CC0-1.0):
  - Git and GitHub workflow — [`01-getting-started-with-git-and-github.md`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/01/intro_git_knitr.Rmd)
  - knitr and R Markdown anatomy, chunk options, LaTeX — [`02-knitr-and-r-markdown-files.md`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/01/intro_git_knitr.Rmd)
  - R Sweave and Rtex — [`03-r-sweave.md`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/01/intro_git_knitr.Rmd)
  - Code style expectations — [`04-code-style.md`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/01/intro_git_knitr.Rmd)
- No slides, transcript, or exercise set were supplied for this section; it is lab-handout material
  rather than a lecture.
- The section referred to, but did not itself contain, several external resources: the Berkeley SCF
  tutorials on [Git basics](https://github.com/berkeley-scf/tutorial-git-basics) and
  [dynamic documents](https://github.com/berkeley-scf/tutorial-dynamic-docs); an example Sweave file
  `example_sweave.Rnw` said to accompany the section; the [R Markdown cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf)
  and [full guide](https://bookdown.org/yihui/rmarkdown/); [knitr in a knutshell](http://kbroman.org/knitr_knutshell/);
  a [Sweave tutorial](https://www.r-bloggers.com/sweave-tutorial-1-using-sweave-r-and-make-to-generate-a-pdf-of-multiple-choice-questions/);
  and the [tidyverse](https://style.tidyverse.org/), [Google](https://google.github.io/styleguide/Rguide.xml),
  and [an additional](https://jef.works/R-style-guide/) R style guides. None of these were read for
  this chapter; only what the section itself states is included above.

---

[← 11. Course Structure and Prerequisites](11-course-structure-and-prerequisites.md) · [Contents](index.md) · [13. Using Git for Collaboration →](13-using-git-for-collaboration.md)
