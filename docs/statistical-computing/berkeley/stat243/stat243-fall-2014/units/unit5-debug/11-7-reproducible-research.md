---
title: 7 Reproducible research
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Reproducible research

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The idea of “reproducible research” has gained a lot of attention in recent years because of the increasing complexity of research projects, lack of details in the published literature, failures in being able to replicate or reproduce others’ work, fraudulent research, and for other reasons.

We’ve seen a number of tools that can help with doing reproducible research, including version control systems such as git, the use of scripting such as bash and R scripts, and literate programming tools such as knitr, Sweave and R Markdown.

_Provenance_ is becoming increasingly important in science. It basically means being able to trace the steps of an analysis back to its origins. _Replicability_ is a related concept - the idea is that you or someone else could replicate the analysis that you’ve done. This can be surprisingly hard as time passes even if you’re the one attempting the replication.

Open question: What is required for something to be replicable? What are the challenges in doing so?

### **7.1 Some basic strategies**

- Have a directory for each project with meaningful subdirectories: e.g., _code_ , _data_ , _paper_

- Keep a document describing your running analysis with dates in a text file (i.e., a lab book)

- Note where data were obtained (and when, which can be helpful when publishing) and preprocessing steps in the lab book. Have data version numbers with a file describing the changes and dates (or in lab book).

- Have a file of code for pre-processing, one or more for analysis, and one for figure/table preparation.

   - The pre-processing may involve time-consuming steps. Save the output of the preprocessing as a file that can be read in to the analysis script.

   - You may want to name your files something like this, so there is an obvious ordering: “1-prep.R”, “2-anal.R”, “3-figs.R”.

15

   - Have the code file for the figures produce the EXACT manuscript figures, operating on an RData file that contains all the objects necessary to run the figure-producing code; the code producing the RData file should be in your analysis code file (or somewhere else sensible).

   - Alternatively, use _knitr_ (or _Sweave_ or _R Markdown_ or _IPython_ ) for your document preparation.

- Note what code files do what in the lab book.

### **7.2 More formal tools**

1. In some cases you may be able to carry out your complete workflow in a knitr/Sweave/R Markdown document.

2. Or in Python, you may be able to use the iPython Notebook.

3. You might consider using the UNIX utility _make_ , which is generally used for compiling code, as a tool for reproducible research: see http://kbroman.github.io/minimal_make/ for more details.

16

---

[← 6 Tips for running analyses](10-6-tips-for-running-analyses.md) · [Up: contents](index.md)
