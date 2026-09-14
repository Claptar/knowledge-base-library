---
title: Code style
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/01/intro_git_knitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/01/intro_git_knitr.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Code style

**Source:** [`sections/01/intro_git_knitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/01/intro_git_knitr.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

### Useful Links
- [Homework Submission](https://github.com/berkeley-stat243/stat243-fall-2019/blob/master/howtos/submitting-electronically.txt)
- [Hadley Wickham Style Guide](https://style.tidyverse.org/)
- [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml)
- [Weird One with Links](https://jef.works/R-style-guide/)

### Additional notes on style
You don't need to follow the exact style of any of those - use your own judgment and figure out what style you like and be consistent in using that style. But you should do the following:

 - use white space to make it easier to read your code
 - have your code lines be no more than 80 characters
 - give your objects and functions meaningful (and not overly long) names
 - comment your code
 - indent your code as needed so one can see what lines of code go together in a block

You should NOT include periods in names of objects (this contradicts Google's style guide). The reason is that periods are used to mean something specific in R's S3 object oriented programming syntax (e.g., `predict.lm`) and that periods are used in other languages specifically for object-oriented syntax. So I'd suggest either `calculate_mle` or `calculateMLE`, not `calculate.mle`.

---

[← Rtex](04-rtex.md) · [Up: contents](index.md)
