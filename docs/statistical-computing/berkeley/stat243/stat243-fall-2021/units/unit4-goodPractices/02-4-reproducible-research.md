---
title: 4 Reproducible research
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit4-goodPractices.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit4-goodPractices.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit4-goodPractices.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit4-goodPractices.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Reproducible research

The idea of "reproducible research" has gained a lot of attention in recent years because of the increasing complexity of research projects, lack of details in the published literature, failures in being able to replicate or reproduce others' work, fraudulent research, and for other reasons.

We've seen a number of tools that can help with doing reproducible research, including version control systems such as git, the use of scripting such as bash and R scripts, and literate programming tools such as knitr and R Markdown.

Provenance is becoming increasingly important in science. It basically means being able to trace the steps of an analysis back to its origins. Reproducibility and replicability are related concepts:

*Reproducibility* - the idea is that a second person/group could get the exact same results as an existing analysis if they use the same input data, methods, and code. This can be surprisingly hard as time passes even if you're the one attempting to reproduce things.

*Replicability* - the idea is that a second/person could obtain results consistent with an existing analysis when using new data to answer the same scientific question.

Open question: What is required for something to be reproducible? What about replicable? What are the challenges in doing so?

## 4.1 Some basic strategies

• Have a directory for each project with subdirectories with meaningful and standardized names: e.g., *code*, *data*, *paper*

• Keep a document describing your running analysis with dates in a text file (i.e., a lab book).

• Note where data were obtained (and when, which can be helpful when publishing) and pre-processing steps in the lab book. Have data version numbers with a file describing the changes and dates (or in lab book).

• Have a file of code for pre-processing, one or more for analysis, and one for figure/table preparation.
  – The pre-processing may involve time-consuming steps. Save the output of the pre-processing as a file that can be read in to the analysis script.
  – You may want to name your files something like this, so there is an obvious ordering: "1-prep.R", "2-anal.R", "3-figs.R".
  – Have the code file for the figures produce the EXACT manuscript figures, operating on an RData file that contains all the objects necessary to run the figure-producing code; the code producing the RData file should be in your analysis code file (or somewhere else sensible).
  – Alternatively, use *knitr*, *R Markdown*, or *Jupyter notebooks* for your document preparation.

• Note what code files do what in the lab book.

• Keep track of the details of the system and software you are running your code under, e.g., operating system version, software (e.g., R, Python) versions, R or Python package versions, etc.
  – In R, `sessionInfo()` will report all this for you.

## 4.2 Formal tools

1. In some cases you may be able to carry out your complete workflow in a knitr/R Markdown document or in a Jupyter notebook.

2. You might consider using the UNIX utility *make*, which is generally used for compiling code, as a tool for reproducible research: if interested, see the tutorial on *Using make for workflows* or this Journal of Statistical Software articleJournal of Statistical Software article for more details.

3. You might organize your workflow as an R package as described in this article.

4. You can manage the versions of R packages (and dependent packages) used in your project using package management packages such as *renv*, *checkpoint*, and *packrat*.

5. You can manage the configuration of a project using the *config* package. This allows you to set configuration values that control how your code/workflow runs, thereby enabling you to run the workflow under different scenarios (e.g., different input datasets, different models, different model configurations, etc.).

---

[← 1 Good coding practices](01-1-good-coding-practices.md) · [Up: contents](index.md)
