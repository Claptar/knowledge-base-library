---
title: Formatting requirements
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps1.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/ps/ps1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Formatting requirements

**Source:** [`ps/ps1.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As discussed in the syllabus, please turn in (1) a copy on paper, as this makes it easier for us to handle AND (2) an electronic copy through Git following Jarrod’s instructions.

Your electronic solution should be in the form of a plain text file named _ps1.txt_ , with the shell code included. Ideally (but not required for this first problem set), your file would be a Latex (named _ps1.Rtex_ ) or R Markdown file (named _ps1.Rmd_ ), with the shell code in chunks demarcated using one of the following types of syntax:

- Latex with knitr:

%% begin.rcode chunkName, engine='bash' % # try a basic shell command % ls %% end.rcode

• R Markdown:

```{r, engine='bash'} ls ```

If you do choose to use Latex/R Markdown for the entire problem set, see the hints in Problem 5 for how to create a PDF or HTML file using the _knitr_ package in R.

For problems 3 and 4, your solution should start with a brief textual description of how you solved the problem, with the code following, including description of what your code does interspersed with the code. Do not just give us raw code.

1

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Technical requirements for your solutions to Problems 3 and 4 →](03-technical-requirements-for-your-solutions-to-problems-3-and.md)
