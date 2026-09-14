---
title: Getting help online
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/04/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Getting help online

**Source:** [`labs/04/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Online forums / mailing lists

There are online forums that have lots of useful postings.
In general if you have an error, others have already posted about it.

- Simple web searches - *a la Google*
    - You may want to include "in R" or preface your question with "R yada yada yada"
- [Stack overflow](http://stackoverflow.com): R stuff will be tagged with 'R'
    - [http://stackoverflow.com/questions/tagged/r](http://stackoverflow.com/questions/tagged/r)
- R help special interest groups (SIG) such as r-sig-hpc (high performance computing),
r-sig-mac (R on Macs), etc.
    - To search a SIG you might include the name of the SIG in the search string
- [Rseek.org](http://Rseek.org) for web searches restricted to sites that have information on R
- [R-help mailing list](https://stat.ethz.ch/mailman/listinfo/r-help)

!!! note "Note"
Of course these are also helpful for figuring out how to do things, not
just for fixing bugs. For example, this [blogpost](http://www.r-bloggers.com/the-guerilla-guide-to-r/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29)
has a guide to R based simply on Stack Overflow posts.
:::

## Asking questions online

If you've searched the archive and haven't found an answer to your problem, you
can often get help by posting to the R-help mailing list or one of the other
lists mentioned above. A few guidelines (generally relevant when posting to mailing
lists beyond just the R lists):

- Search the archives and look through relevant R books or manuals first.
    - [Advanced R](http://adv-r.had.co.nz/) by Hadley Wickham
- Boil your problem down to the essence of the problem, giving an example,
including the output and error message
    - Former GSI's first [SO](https://stackoverflow.com/questions/49822833/r-package-call-c-function-within-rcpp) post
        - Notice the not-so-polite comments, see the remark below
    - Former GSI's second [SO](https://stackoverflow.com/questions/56298503/r-vignette-fails-on-internal-package-function) question
- Say what version of R, what operating system and what operating system version you're using.
    - Provide `sessionInfo()` and `Sys.info()`. These show the current state of your machine
- Read the [R mailing list posting guide](https://www.r-project.org/posting-guide.html).

The R mailing lists are a way to get free advice from the experts, who include
some of the world's most knowledgeable R experts - seriously - members of the R
core development team contribute frequently. The cost is that you should do your
homework and that sometimes the responses you get __may be blunt__, along the lines
of “read the [manual](https://cran.r-project.org/manuals.html)”. Chris considers it a
pretty good tradeoff - where else do you get the foremost experts in a domain actually helping you?

---

[← Common errors](05-common-errors.md) · [Up: contents](index.md) · [Pair debugging exercise →](07-pair-debugging-exercise.md)
