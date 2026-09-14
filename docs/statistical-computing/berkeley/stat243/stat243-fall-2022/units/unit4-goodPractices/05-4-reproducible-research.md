---
title: 4. Reproducible research
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit4-goodPractices.md
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit4-goodPractices.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Reproducible research

**Source:** [`units/unit4-goodPractices.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit4-goodPractices.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

The idea of "reproducible research" has gained a lot of attention in
the last decade because of the increasing complexity of research projects,
lack of details in the published literature, failures in being able to
replicate or reproduce others' work, fraudulent research, and for other
reasons.

We've seen a number of tools that can help with doing reproducible
research, including version control systems such as git, the use of
scripting such as bash and R scripts, and literate programming tools
such as knitr and R Markdown.

*Provenance* is becoming increasingly important in science. It basically
means being able to trace the steps of an analysis back to its origins.
*Reproducibility* and *replicability* are related concepts:

*Reproducibility* - the idea is that a second person/group could get the
exact same results as an existing analysis if they use the same input
data, methods, and code. This can be surprisingly hard as time passes
even if you're the one attempting to reproduce things.

*Replicability* - the idea is that a second/person could obtain results
consistent with an existing analysis when using new data to answer the
same scientific question.

Open question: What is required for something to be reproducible? What
about replicable? What are the challenges in doing so?

## Some basic strategies

- Have a directory for each project with subdirectories with
    meaningful and standardized names: e.g., *code*, *data*, *paper*. The Journal of the American Statistical Association (JASA) has a [template GitHub repository](https://github.com/jasa-acs/repro-template) with some suggestions.
- Have a file of code for pre-processing, one or more for analysis,
    and one for figure/table preparation.
    - The pre-processing may involve time-consuming steps. Save the
        output of the pre-processing as a file that can be read in to
        the analysis script.
    - You may want to name your files something like this, so there is
        an obvious ordering: "1-prep.R", "2-analysis.R", "3-figs.R".
    - Have the code file for the figures produce the **exact** manuscript/report
        figures, operating on a file (e.g., .Rda file) that contains all the
        objects necessary to run the figure-producing code; the code
        producing the .Rda file should be in your analysis code file
        (or somewhere else sensible).
    - Alternatively, use *knitr*, *R Markdown,* or *Jupyter notebooks*
        for your document preparation.
- Keep a document describing your running analysis with dates in a
    text file (i.e., a lab book).
- Note where data were obtained (and when, which can be helpful when
    publishing) and pre-processing steps in the lab book. Have data
    version numbers with a file describing the changes and dates (or in
    lab book). If possible, have all changes to data represented as code that processes the data relative to a fixed baseline dataset.
- Note what code files do what in the lab book.
- Keep track of the details of the system and software you are running
    your code under, e.g., operating system version, software (e.g., R,
    Python) versions, R or Python package versions, etc.
    - In R, *sessionInfo()* will report all this for you.

## Formal tools

1. In some cases you may be able to carry out your complete workflow in
    a knitr/R Markdown document or in a Jupyter notebook.
2. You might consider workflow/pipeline management software such as Drake or other
    tools discussed in the [CRAN Reproducible Research Task View](https://cran.r-project.org/web/views/ReproducibleResearch.html). Alternatively, one can use the *make* tool, which is generally
    used for compiling code, as a tool for reproducible research: if
    interested, see the tutorial on [Using make for workflows](http://github.com/berkeley-scf/tutorial-make-workflows) or this
    [Journal of Statistical Software article](https://www.jstatsoft.org/article/view/v094c01)
    for more details.
3. You might organize your workflow as an R package as described in
    [this article](https://doi.org/10.1080/00031305.2017.1375986).
4. Package management:
    - R: You can manage the versions of R packages (and dependent packages)
    used in your project using package management packages such as
    *renv*, *checkpoint*, and *packrat*.
    - Python: You can manage the versions of Python packages (and dependent packages) used in your project using Conda environments (or virtualenvs).
5. If your project uses multiple pieces of software (e.g., not just R or Python), you can set up a reproducible environment using *containers*, of which Docker containers are the best known. These provide something that is like a lightweight virtual machine in which you can install exactly the software (and versions) you want and then share with others. Docker container images are a key building block of various tools such as GitHub Actions and the [Binder project](https://mybinder.org)
6. You can manage the configuration of a project using the *config*
    package. This allows you to set configuration values that control
    how your code/workflow runs, thereby enabling you to run the
    workflow under different scenarios (e.g., different input datasets,
    different models, different model configurations, etc.).

---

[← 3. Tips for running analyses](04-3-tips-for-running-analyses.md) · [Up: contents](index.md)
