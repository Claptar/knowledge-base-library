---
title: "5. Code Review and Homework Habits"
course: "Berkeley Stat 243"
chapter: 5
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Code Review and Homework Habits

## What this covers

This chapter is not a lecture but a discussion-section handout: a set of instructions for a
peer code review exercise on a problem set, plus a running list of the practical habits the
course expects in every homework submission. It assumes the reader is already writing R code
for problem sets in this course and is asking a narrower question: what actually makes code
easy for someone else — a reviewer, a grader, or your future self — to read and trust?

## The paired code-review exercise

In this section meeting, students do a paired code review of one problem from a problem set.
The point of the exercise depends on honesty: if a partner's code is hard to follow, say so;
if something in it is clever, say that too. Politeness that hides the actual reaction defeats
the purpose.

The procedure:

1. Pair up (a group of three if the section has an odd number of people).
2. Spend about fifteen minutes reading one partner's code, asking them questions about it.
3. Switch roles and review the other partner's code the same way.
4. Each person fills out a short survey summarizing how their approach differed from their
   partner's, noting anything that struck them as novel. The survey is graded on thoughtfulness
   (a couple of sentences is enough for credit), not on correctness — and if you miss section,
   the expectation is to find a partner elsewhere and still submit it.

### Guiding questions for a review

These are the questions to actually ask while reading someone else's code, and they generalize
past this one exercise — they are a checklist for reading (or writing) any piece of analysis
code:

1. **Is the code visually easy to break apart?** Can you see an entire function body without
   scrolling in either direction? The rule of thumb is about 80 characters of width and about
   80 lines of length — the width limit is the one worth following more strictly.
2. **Are the data structures easy to parse?** Is it clear what information lives in which
   object, and is the type of each object appropriate to what it holds?
3. **Are the functions easy to parse?** Is it clear what each one does, what is being passed
   into it, and what it returns?
4. **What do the regular expressions handle?** Were any edge cases missed? Was anything handled
   particularly well, or with an expression you wouldn't have thought of yourself?
5. **Are the plots well made?** Labeled clearly, easy to read values off of, and do they give
   you confidence the code produced correct output?
6. As an extra step: compare object-oriented designs on a different problem, and be able to
   explain the reasoning behind your own design, not just describe it.

The common thread across the first three questions is that "correct" and "readable" are
separate properties of code, and a review is specifically aimed at the second one — you already
know your own code runs; the exercise is finding out whether someone else can follow it without
you standing next to them.

## General habits for problem sets

Separately from the review exercise, the section collects a set of standing expectations for
every homework submission.

**Answer the question that was asked.** Being creative beyond the assignment is welcome, but
every part of every question — including written-response parts — has to be answered directly.
An elegant analysis that never states the answer the question asked for is throwing away points
for something that was already done.

**Include your code**, either inline as you go or gathered into an appendix at the end if that
reads more cleanly. The same applies to the code that produced any plots.

**Use the editor's tools.** In RStudio, autoindent is Ctrl/Cmd+I and autoformat is
Shift+Ctrl/Cmd+A; there are further shortcuts under the Code menu. These cost nothing and remove
a whole category of "the reviewer can't read this" complaints before they start.

**Bonus and extra credit means novel, not repeated.** Rerunning the same analysis with
different parameter values does not count as bonus work — it has to go beyond what the basic
assignment already asked for.

**Suppress package noise, not real problems.** Use `suppressPackageStartupMessages()`, or set
`warning = FALSE` and `message = FALSE`, in a code chunk that *only* loads packages — and
nowhere else. If a warning is coming from your actual analysis code, the fix is to resolve
whatever is causing it, not to hide it.

**Test before you submit.** The code should run cleanly from a fresh RStudio session and a full
knit of the `.Rmd`. A recurring failure mode is renaming a variable at the last minute, or
referencing something that only exists as a leftover global in the live session and not in the
document itself — both are signs the code was never actually run start to finish before
submission. Where it's reasonable, a function you write should come with a few small,
deliberately chosen examples demonstrating that it behaves as expected.

**Simplicity is the ultimate sophistication.** Always be looking for the simplest version of
the code that is still correct, numerically sound, and fast enough. Three pieces of code that
compute the same mean:

```r
total = 0
for (i in 1:length(x)) {
  total = total + x[i]
}
total/length(x)
```

```r
sum(x)/length(x)
```

```r
mean(x)
```

The third is the one to write. Simpler code is easier to debug because there is less of it to
check, easier for you and others to read later, and — though not guaranteed — often faster as
well.

**Plots need a title, axis labels, and a legend** if more than one kind of data appears on them.
Code and comments should stay near 80 characters per line: a comment that runs on as one long
paragraph is worse than the same explanation wrapped onto several short lines, because the
long version forces the reader to scroll sideways to take in a single sentence.

**Vectorize where R already gives you the tool.** R is vectorized natively for arithmetic
(addition, subtraction, multiplication, division), and many built-in functions carry their own
vectorization — check the documentation before writing a loop. Two ways of doing the same
elementwise division:

```r
x <- 1:100
y <- 100:1

mHold <- mapply(FUN = "/", x, y)
dHold <- x/y

all.equal(mHold, dHold)
identical(mHold, dHold)
```

and two ways of drawing multinomial samples row-by-row from a matrix of probabilities:

```r
myprobs <- matrix(data = c(0.1,0.1,0.8, 1/3,1/3,1/3), nrow = 2, byrow = T)

apHold <- t(apply(X = myprobs, MARGIN = 1, FUN = rmultinom, n = 1, size = 100))
edHold <- extraDistr::rmnom(n = 2, size = 100, prob = myprobs)

all.equal(apHold, edHold)
identical(apHold, edHold) # why false?
```

The `apply` version and the purpose-built vectorized function (`extraDistr::rmnom`) give
`all.equal`-equivalent but not `identical` results — a reminder that "does the same thing"
and "produces the same bits" are different claims, worth checking separately. Benchmarking the
two approaches (with `microbenchmark::microbenchmark`) is the way to find out whether the
vectorized version is actually faster, rather than assuming it must be.

## Sources

- Notes: `sections/05/CodeReview/01-code-review-instructions.md` — the paired code-review
  procedure and the six guiding questions.
- Notes: `sections/05/CodeReview/02-general-notes-about-homeworks.md` — the nine general
  homework notes, including the simplicity and vectorizing code examples.
- Both are converted from `sections/05/CodeReview.Rmd`, Berkeley STAT243 (Fall 2021), CC0-1.0.
- No slide deck, transcript, or problem set was supplied for this chapter; the review survey
  itself (`tinyurl.com/s243-code-review`) is referenced by the notes but its contents are not
  part of the source material.

---

[← 4. The Cohort Location Model](04-the-cohort-location-model.md) · [Contents](index.md) · [6. Debugging in R →](06-debugging-in-r.md)
