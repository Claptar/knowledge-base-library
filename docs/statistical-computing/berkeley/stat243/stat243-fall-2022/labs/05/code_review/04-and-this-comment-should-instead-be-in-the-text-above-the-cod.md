---
title: and this comment should instead be in the text above the code chunk :(
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/05/code_review.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# and this comment should instead be in the text above the code chunk :(

**Source:** [`labs/05/code_review.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

how_to_lose_points <- function(...) { ... }
```
:::

## Include Your Code

Most people include it as they go along, which is fine. If you find that messy,
put an appendix at the end with all of the function definitions. This applies to
code for plots as well.

## Include Relevant Outputs

Where appropriate, include some sample outputs from your code. You don't have to
do this for every single function, but be sure to give outputs if the question
asks for it to avoid points off, e.g. "print out or plot the number of chunks
for the candidates" or "report the number of observations in each year by
printing the information to the screen".

If outputs are long and you can't truncate them, then create an appendix section
at the end of your document and put them there, with a subheading for the
relevant problem. Please also be sure to include a note that you did so in the
text, e.g. "The output can be found in the Appendix."

## Avoid Unnecessary Outputs

Please use `suppressPackageStartupMessages()` or set `warning = FALSE` and
`message = FALSE` in a code chunk that **only** loads the packages. Please on't
use these chunk options on other chunks. If something is going wrong ou need to
fix it, as opposed to not printing the warning.

## Use Good Formatting to Make Clear What Problem You're Answering

You have the power of Markdown in your hands, so use it! While you're free to
use the `.Rmd` source code for the problem set instructions as a template, the
instructions are written as a list, and `.Rmd` is finicky when adding text or
code chunks between sequential list items.

It can often be less error-prone to start a new `.Rmd` from scratch and just use
header tags like `#` (top level section) and `##` (second level section) to
separate your problems and sub-problems.

For example:

```markdown

---

[← To answer this problem, I wrote the code below which does x, y, and z...](03-to-answer-this-problem-i-wrote-the-code-below-which-does-x-y.md) · [Up: contents](index.md) · [Problem 1: Assertions and testing →](05-problem-1-assertions-and-testing.md)
