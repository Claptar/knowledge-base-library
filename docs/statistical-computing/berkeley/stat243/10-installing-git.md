---
title: "10. Installing Git"
course: "Berkeley Stat 243"
chapter: 10
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Installing Git

## What this covers

This chapter answers a narrow, practical question: how do you get Git — the version control
software used throughout the course — running on your own machine and connected to RStudio. It
assumes only that you have decided to use Git for coursework and need the mechanics of installing
and wiring it up; it does not cover what Git is for or how to use it, which belong to other parts
of the course.

## Getting Git onto your machine

Git can be installed by downloading the appropriate binary for your operating system from the
[official downloads page](http://git-scm.com/downloads).

If you are working on the SCF (the department's shared computing facility), Git is already
installed there. Logging in to an SCF machine and using Git requires no separate installation
step.

## Using Git through RStudio

RStudio can drive Git through RStudio projects, rather than requiring the command line directly.
Two external guides cover the mechanics of setting this up:

- [Using GitHub with R and RStudio](http://www.molecularecologist.com/2013/11/using-github-with-r-and-rstudio/)
- [RStudio's own guidelines on version control with Git and SVN](https://support.rstudio.com/hc/en-us/articles/200532077-Version-Control-with-Git-and-SVN)

RStudio needs to know where the Git executable lives on disk, and this is the step most likely to
need manual fixing:

- **On Windows**, the executable is typically installed somewhere like
  `"C:/Program Files (x86)/Git/bin/git.exe"`.
- **On macOS**, you can find the executable's location by running `which git` in Terminal.
- Once you have that path, confirm RStudio is pointed at it: go to
  **Tools -> Options -> Git/SVN -> Git executable** and check the location shown there matches.

## Sources

- Berkeley STAT 243 (Fall 2021), howto note *GitInstall*:
  `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/howtos/gitInstall.md` in the
  knowledge-base-library, converted from
  [`howtos/gitInstall.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/howtos/gitInstall.Rmd).
  No accompanying slides, transcript or exercises were supplied for this item — it is a standalone
  installation howto rather than a lecture.

---

[← 9. Reading: Adaptive Rejection Sampling for Gibbs Sampling](09-reading-adaptive-rejection-sampling-for-gibbs-sampling.md) · [Contents](index.md) · [11. Course Structure and Prerequisites →](11-course-structure-and-prerequisites.md)
