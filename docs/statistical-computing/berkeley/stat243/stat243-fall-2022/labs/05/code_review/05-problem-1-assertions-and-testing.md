---
title: 'Problem 1: Assertions and testing'
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/05/code_review.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Problem 1: Assertions and testing

**Source:** [`labs/05/code_review.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

## a. Assertions

In the function below, I added an assertion to check for...
which guards against... and gives helpful feedback to the user
telling them to...

```

Note that you have to include a space between the final `#` and the header text,
or the header won't render correctly, e.g.:

```markdown
#Header
```

produces the following non-header text:

#Header

If you're having trouble with Markdown, see [2.5 Markdown syntax](https://bookdown.org/yihui/rmarkdown/markdown-syntax.html)
from the _R Markdown: The Definitive Guide_ book.

## A Couple of Useful Tools in RStudio

You can autoindent your code in RStudio using Command or Ctrl + I. You can also
autoformat your code with Shift + Command or Ctrl + A. There are some other
useful shortcuts in the Code menu.

## Extra Credit

This is something additional, above and beyond the basic homework. Repeating the
analysis already performed, but with different parameters, is not novel.

## Code Testing

You should have already tested all aspects of your R code before you submit it.
Your code should run properly if you restart RStudio and render your `.Rmd`. I
have seen several assignments where students renamed a variable at the last
second which causes their code to break, are referencing a global variable that
doesn't exist in the `.Rmd`, etc. which tells me they did not fully test that
their code works before submitting. When reasonable, the functions you create
should have a set of small but thoughtful examples showing that the code works
as expected.

## Simple is Often Better

You should always be thinking of ways to make your code as simple as possible
(while maintaining correctness, numerical precision, speed, etc.). For example,
the following three chunks of code all do the same thing:

```r
total <- 0
for (i in 1:length(x)) {
    total <- total + x[i]
}
total / length(x)
```

```r
sum(x) / length(x)
```

```r
mean(x)
```

But the third option is preferred. Simple code helps with debugging (as
there are fewer lines of code to check), improves readability (both for
yourself and others), and can often (though not always) result in faster
code.

## Plots and Comments

Plots need to have a title, axis labels, and a key if there are several types of
data. Both code _and_ comment lines should be ~80 characters in length, e.g.:

```r
####################

---

[← and this comment should instead be in the text above the code chunk :(](04-and-this-comment-should-instead-be-in-the-text-above-the-cod.md) · [Up: contents](index.md) · [Wrap your comments →](06-wrap-your-comments.md)
