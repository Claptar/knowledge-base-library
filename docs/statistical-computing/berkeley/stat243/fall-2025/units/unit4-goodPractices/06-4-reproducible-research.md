---
title: 4. Reproducible research
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit4-goodPractices.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit4-goodPractices.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Reproducible research

**Source:** [`units/unit4-goodPractices.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit4-goodPractices.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

The idea of "reproducible research" has gained a lot of attention in
the last decade because of the increasing complexity of research projects,
lack of details in the published literature, failures in being able to
replicate or reproduce others' work, fraudulent research, and for other
reasons.

We've seen a number of tools that can help with doing reproducible
research, including version control systems such as git, the use of
scripting such as bash and Python scripts, and literate programming tools
such as Quarto and Jupyter notebooks.

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

## Some basic strategies for reproducible analyses

- Have a directory for each project with subdirectories with
    meaningful and standardized names: e.g., `code`, `data`, `paper`. The Journal of the American Statistical Association (JASA) has a [template GitHub repository](https://github.com/jasa-acs/repro-template) with some suggestions.
- Have a file of code for pre-processing, one or more for analysis,
    and one for figure/table preparation.
    - The pre-processing may involve time-consuming steps. Save the
        output of the pre-processing as data file(s) that can be read in to
        the analysis script.
    - You may want to name your files something like this, so there is
        an obvious ordering: "1-prep.py", "2-analysis.py", "3-figs.py".
    - Have the code file for the figures produce the **exact** manuscript/report
        figures, operating on a file (e.g., a pickle file) that contains all the
        objects necessary to run the figure-producing code; the code
        producing the pickle file should be in your analysis code file
        (or somewhere else sensible).
    - Alternatively, use Quarto or Jupyter notebooks
        for your document preparation.
- Keep a document describing your running analysis with dates in a
    text file (i.e., a lab book).
- Note where data were obtained (and when, which can be helpful when
    publishing) and pre-processing steps in the lab book. Have data
    version numbers with a file describing the changes and dates (or in
    lab book). If possible, have all changes to data represented as code that processes the data relative to a fixed baseline dataset.
- Note what code files do what in the lab book.
- Keep track of the details of the system and software you are running
    your code under, e.g., operating system version, software (e.g., Python, R) versions, Python or R package versions, etc.
    - `pip list` and `conda list` will show you version numbers for installed packages.
    - `pip freeze > requirements.txt` and `conda env export > env.yml` will create a recipe file for your environment.
    - `pip install -r requirements.txt` and `conda env create -f env.yml` will build that environment on your machine.
    - Note that if you want to give the environment to someone use a different operating system, you can run into problems because these  commands can embed operating system-specific versions, but recording the package versions is nonetheless important for reproducibility.

## Formal tools

1. In some cases you may be able to carry out your complete workflow in
    a Quarto document or in a Jupyter notebook.
2. You might consider workflow/pipeline management software such as Drake or other
    tools discussed in the [CRAN Reproducible Research Task View](https://cran.r-project.org/web/views/ReproducibleResearch.html). Alternatively, one can use the *make* tool, which is generally
    used for compiling code, as a tool for reproducible research: if
    interested, see the tutorial on [Using make for workflows](http://github.com/berkeley-scf/tutorial-make-workflows) or this
    [Journal of Statistical Software article](https://www.jstatsoft.org/article/view/v094c01)
    for more details.
3. You might organize your workflow as a Python or R package as described (for the R case) in
    [this article](https://doi.org/10.1080/00031305.2017.1375986).
4. Package management:
    - Python: You can manage the versions of Python packages (and dependent packages) used in your project using Conda environments (or virtualenvs).
    - R: You can manage the versions of R packages (and dependent packages)
    used in your project using package management packages such as
    `renv` and `packrat`. Unfortunately, the useful `checkpoint` package relies on snapshots of CRAN that are not available after January 2023.
5. If your project uses multiple pieces of software (e.g., not just Python or R), you can set up a reproducible environment using *containers*, of which Docker containers are the best known. These provide something that is like a lightweight virtual machine in which you can install exactly the software (and versions) you want and then share with others. Docker container images are a key building block of various tools such as GitHub Actions and the [Binder project](https://mybinder.org). Alternatively (and often much easier) Conda is a general package manager that can install lots of non-Python packages and can also be used in many circumstances.

---

[← 3. Tips for running analyses](05-3-tips-for-running-analyses.md) · [Up: contents](index.md)
