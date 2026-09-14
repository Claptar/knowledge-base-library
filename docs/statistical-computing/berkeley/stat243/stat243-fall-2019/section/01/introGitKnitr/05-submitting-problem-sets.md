---
title: Submitting problem sets
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/01/introGitKnitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/01/introGitKnitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Submitting problem sets

**Source:** [`section/01/introGitKnitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/01/introGitKnitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

> ### Learning Objectives:
>
> - Ensure repository is setup correctly
> - Discuss Code Styles
> - Turning in homework

### 0) Useful Links
- [Homework Submission](https://github.com/berkeley-stat243/stat243-fall-2019/blob/master/howtos/submitting-electronically.txt)
- [Hadley Wickham Style Guide](https://style.tidyverse.org/)
- [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml)
- [Weird One with Links](https://jef.works/R-style-guide/)

You don't need to follow the exact style of any of those - use your own judgment and figure out what style you like and be consistent in using that style. But you should do the following:

 - use white space to make it easier to read your code
 - have your code lines be no more than 80 characters
 - give your objects and functions meaningful (and not overly long) names
 - comment your code
 - indent your code as needed so one can see what lines of code go together in a block

You should NOT include periods in names of objects (this contradicts Google's style guide). The reason is that periods are used to mean something specific in R's S3 object oriented programming syntax (e.g., `predict.lm`) and that periods are used in other languages specifically for object-oriented syntax. So I'd suggest either `calculate_mle` or `calculateMLE`, not `calculate.mle`.

---

[← 7) LaTeX](04-7-latex.md) · [Up: contents](index.md)
