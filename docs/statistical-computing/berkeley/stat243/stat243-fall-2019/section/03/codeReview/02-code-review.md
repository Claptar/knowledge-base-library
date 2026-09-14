---
title: Code Review
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/03/codeReview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/03/codeReview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Code Review

**Source:** [`section/03/codeReview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/03/codeReview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Today we will practice paired code review for PS1. In order for this of benefit,
you will need to be as honest with your partner as possible. If something is actually
hard to follow, tell them!  If you thought that something they did was clever,
also tell them!

### Procedure
You will each spend 10 minutes reading your partner's code while he/she will be
available to answer questions you have about their work. I will float around and
can make any clarifying points. After that, we will go through Chris' solution to
problem 4b and see what makes sense or what could be made clearer.

### Some guiding questions

1. Is the code visually easy to break apart? Can you see the entire body of the
functions without scrolling up/down left/right? The general rule-of-thumb is no
more than 80 in either direction (80 character width, 80 lines. The first restriction
should be practiced more religiously)

2. Are there "magic numbers" present in the code? i.e. Hard-coded values or indices.
In this assignment, some indices are acceptable given the structure of the scraped
page, but they should be accompanied by some documentation about the assumed
structure of the data.

3. Is it clear why each variable is being created? Names are good guidance here.

4. Is the code separated into logical "steps"? Or is it just one big blob?
If you have descriptive function names, then you can get away without comments.
Otherwise, each chunk of code should have a short comment explaining its purpose.

5. Are the input tests reasonable? Do they seem to catch every case that came
to your mind as you wrote your function?

---

[← PS1 Notes](01-ps1-notes.md) · [Up: contents](index.md)
