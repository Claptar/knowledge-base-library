---
title: "29. Installing R & RStudio"
course: "Berkeley Stat 243 Fall 2024"
chapter: 29
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 29. Installing R & RStudio

## What this covers

This chapter answers a purely practical question: how do you get a working copy of R and RStudio,
either on your own machine or through Berkeley's DataHub, so that you can do the rest of the
course's work. It assumes nothing beyond having a computer — no prior R experience — and is the
same setup guide handed out, with only small edits, across four runs of the course (stat243-fall-2021
through fall-2026).

## Installing R

R itself has to be installed before RStudio, since RStudio is an interface to R rather than a
replacement for it. Across every version of the guide the rule is the same: **if your version of R
is older than 4.0.0, install the latest version.** The stat243-fall-2021 edition is more specific
about why the cutoff is 4.0.0 rather than an arbitrary "get the newest" instruction: R 3.5 or 3.6
would work for most of the course, but a couple of topics in Unit 5 assume R 4.0.0 or later, so an
older install will not silently just work.

The download location depends on the operating system:

* **macOS** — install the packaged `.pkg` installer from
  [cran.rstudio.com/bin/macosx](https://cran.rstudio.com/bin/macosx). The guides across different
  years point at whatever the current release was at the time (`R-4.1.0.pkg` in 2021,
  `R-4.2.1.pkg` in later editions) — the number will keep moving, but the CRAN macOS binaries page
  is always the place to get it.
* **Windows** — [cran.rstudio.com/bin/windows/base](https://cran.rstudio.com/bin/windows/base/).
* **Linux** — [cran.rstudio.com/bin/linux](https://cran.rstudio.com/bin/linux/).

## Installing RStudio

Once R is installed, install RStudio from
[rstudio.com/ide/download/desktop](https://www.rstudio.com/ide/download/desktop): scroll down to
the "Installers for Supported Platforms" section and pick the installer for your operating system.
RStudio does not bundle its own copy of R — it finds and uses the R you installed in the previous
step.

## Checking the install: adding a package

A plain R install can run base R code, but most of the course's work depends on being able to add
packages on top of it, so the guide's verification step is to install one and see whether it
works. The chosen test package is **`fields`**:

1. In RStudio, go to **Tools → Install Packages**.
2. In the "Packages" field of the dialog that appears, type `fields` (no quotes).
3. Depending on where the "Install to Library" field points, you may be asked for an administrator
   password — that happens when R tries to write into a system-wide library directory rather than
   one that belongs to your own user account.

If you would rather install packages into a personal directory instead of one that needs admin
rights, the guide gives a two-step fix:

* In R, run `Sys.getenv()['R_LIBS_USER']` to see where R expects your personal package library to
  live.
* Create that directory yourself if it doesn't already exist — on a Mac this might be
  `~/Library/R/4.0/library`.

Once that directory exists, R can install packages there without needing administrator
permissions, because it's a location you already own.

Windows setup has more moving parts (compilers and paths that macOS and Linux don't need), so the
guide points to a separate, more detailed document, *Using R, RStudio, and LaTeX on Windows*,
rather than repeating those steps here.

## An alternative: DataHub

If installing software locally isn't an option, or isn't working, the course also runs on
Berkeley's **DataHub**, a hosted environment reachable from a browser with no local install at all.
Two ways in are given:

* Log in to DataHub following the instructions in the course's *Accessing the Unix Command Line*
  material, then, from the DataHub file browser, click **New** and then **RStudio**.
* Or skip that and go directly to the RStudio interface at
  [r.datahub.berkeley.edu](https://r.datahub.berkeley.edu).

Either route lands you in the same RStudio interface described above, just running on Berkeley's
servers instead of your own machine — useful as a fallback, or simply as the faster way to start
before a local install is sorted out.

## Sources

All four editions of the course's `howtos/RandRStudioInstall` document cover this chapter, and they
are close to identical; differences are noted above where they occur.

* stat243-fall-2021, *On your laptop* (`howtos/RandRStudioInstall.Rmd`) — source of the R 3.5/3.6
  vs. 4.0.0 and Unit 5 remark, and the `R-4.1.0.pkg` version reference.
* fall-2024, fall-2025 and fall-2026 editions of *Installing R & RStudio*
  (`howtos/RandRStudioInstall.md`) — near-identical text to the 2021 edition, minus the Unit 5
  remark, referencing `R-4.2.1.pkg`; used for the general structure and wording followed here.
* Referenced but not supplied as input to this chapter: *Using R, RStudio, and LaTeX on Windows*
  (`howtos/windowsInstall.Rmd`), and *Accessing the Unix Command Line*
  (`howtos/accessingUnixCommandLine.html`), both linked from the documents above for readers who
  need Windows-specific detail or DataHub login steps.
* No slides, transcript or exercises were supplied for this topic.

---

[← 28. R Practice: Structures, Functions, I/O](28-r-practice-structures-functions-i-o.md) · [Contents](index.md) · [30. Assignment: regex problems →](30-assignment-regex-problems.md)
