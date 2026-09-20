---
title: "16. The Final Project"
course: "Berkeley Stat 243 Fall 2024"
chapter: 16
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. The Final Project

## What this covers

STAT 243 (Statistical Computing) closes with a group final project: three students build a small
statistical software package end to end, under a public grading rubric, rather than answering a
problem set. This chapter is not about a lecture but about that project handout, which has been
posed three times with two different technical cores — an adaptive rejection sampler (Fall 2024)
and a genetic algorithm for variable selection (Fall 2021, in R; Fall 2025, in Python). It lays out
what the assignment asks for and how the requirements were graded, and what stayed fixed and what
changed as the instructor revised it across years. It assumes the reader already knows, from
earlier in the course, how to structure a package, write tests, vectorize code and use Git — the
project is where those skills get combined on one deliverable. It does not explain adaptive
rejection sampling or genetic algorithms themselves: the handouts only point at where those are
described (a set of unit notes and two textbook references) rather than reproduce them, and no
lecture material on either algorithm was supplied alongside these handouts.

## Why the project exists, and how it is graded

The project is done in groups of three, assigned randomly, and is deliberately not meant to be a
huge undertaking once split across the group — the stated goals are experience working
collaboratively and producing "a well-designed, well-tested piece of software." It is graded as a
letter grade worth about as much as two problem sets (two problem sets/quizzes, in the 2025
version) of the final grade.

Two rules govern how the work may be done, repeated in every year's handout:

- **Cite what you use.** Standard citation practice applies to any paper, code, online resource, or
  chatbot whose ideas the team draws on.
- **Work only within the group.** Consulting classmates outside the team is not allowed; asking the
  instructor or TA is fine. The Fall 2025 version adds an explicit AI policy: AI tools may be used
  for brainstorming and for small components of the coding, but the team must decide the structure
  — object-oriented vs. functional, what functions or methods, what arguments — itself, and must
  understand and be able to defend any AI-produced code.

The deliverable is a package the instructor can install and run **without help**, and grading
leans heavily on running the instructor's own test cases against it — not just the team's. That
single fact shapes almost every other requirement below: an interface that only the authors can
drive, or that silently assumes inputs the instructor's tests don't respect, fails regardless of
whether the algorithm itself is implemented correctly.

## The rubric, and how it recurs across both assignments

Both versions of the project — adaptive rejection sampling and the genetic algorithm — are graded
against the same shape of rubric, adapted to the algorithm:

1. **Input validity and a reasonable interface.** For the sampler, the primary input is a Python
   function computing the (possibly unnormalized) density of interest, evaluated in a vectorized
   way, plus the number of values wanted; the code must check inputs and, since a full a priori
   test of log-concavity is not required, must instead catch — numerically, as the algorithm runs —
   cases where the upper and lower bounds it has constructed are not actually bounding the density.
   For the genetic algorithm, the interface constraint is stricter still in the later offering (see
   below): a fixed function name and fixed argument and output shape, so the same grading script
   runs against every team's code unmodified.

2. **Formal testing under a stochastic algorithm.** Both algorithms produce random output, so "test
   against a known answer" is not available directly; each handout calls this out explicitly and
   leaves the team to work out how to test a sampling or search procedure whose result varies run
   to run — comparing samples to the true distribution, or search results to a known-good variable
   set, rather than comparing single values. Unit tests are additionally required for the
   individual, non-trivial computations that make up the algorithm, separately from the end-to-end
   test.

3. **Modular code with a consistent design.** Functions or methods should implement discrete tasks,
   with one style — functional or object-oriented — held consistently across the codebase, and
   consistent naming.

4. **Vectorize what can be vectorized around an inherently sequential core.** Adaptive rejection
   sampling updates its envelope after each accepted or rejected point, and a genetic algorithm's
   generations depend on the previous generation, so neither algorithm can be made embarrassingly
   parallel outright — but the work inside one step (evaluating a density at many points; scoring
   an entire population's fitness) can be. The 2025 genetic-algorithm version makes this explicit
   with an `n_workers` argument (default 1) for optionally parallelizing the fitness evaluation or
   the cross-validation across a single machine's cores.

5. **Documentation with runnable examples.** A standard docstring (or, in the 2021 R version, an
   `.Rd` help page, hand-written or generated via `roxygen2`) is required for the primary function,
   including a working example; auxiliary functions need only a one-line docstring stating what
   they do.

6. **No borrowing the algorithm itself.** Standard building blocks — `numpy`/`scipy`/`jax`/`pytorch`
   in Python, base R and `stats` in R — are fine to call, but the code must not use or mimic an
   existing implementation of adaptive rejection sampling or of the genetic operators being
   implemented; that is the part of the assignment the team is meant to write.

## Fall 2024: an adaptive rejection sampler

The task is to implement adaptive rejection sampling, described in the course's own Unit 9 notes
(Section 5) and, in more detail, in Section 2.2 of Gilks et al. (1992) — neither of which is part
of this handout; the PDF of the paper was distributed separately in the class repository. The
result is a Python package, `ars`, whose primary function (also called `ars`) is the one a user
calls to sample.

Beyond the shared rubric above, two requirements are specific to this version:

- **Gradient estimation, in two stages.** The team should start with numerical differentiation to
  get the gradients the algorithm needs, but an "A" solution is expected to also support automatic
  differentiation via JAX or PyTorch. The handout is explicit about *why* this buys nothing from a
  GPU here: AD is being used only for its differentiation capability, not for GPU-scale batching,
  because the problem cannot be arranged as a large number of identical calculations run at once.
- **Restriction on outside code.** Any `scipy`/`numpy`/`jax`/`pytorch` call is fair game as a
  building block, but the code must not use or resemble any external implementation of adaptive
  rejection sampling specifically.

The deliverable has two parts. The package itself lives in a private repository (`ars-dev`, on
GitHub) shared with the instructor, and must include the primary `ars` function, supporting code,
`pytest` tests the instructor can run directly, and a docstring with worked examples. Alongside the
code, a short (2–4 page) PDF report, written as a Quarto document, summarizes the design —
functions vs. modularity vs. object orientation — the testing performed, and results on example
distributions, and must include a paragraph naming each team member's specific contribution. The
report is submitted on paper, annotated with the GitHub repository's URL.

## Fall 2021 (R) and Fall 2025 (Python): a genetic algorithm for variable selection

Both years pose the same problem — use a genetic algorithm to select variables in a regression
model — pointing at Section 3.4 of Givens and Hoeting's *Computational Statistics* for the
algorithm's details, which again are not part of this handout.

**Fall 2021 (R).** The package, named `GA`, exposes a primary function `select` that takes a
dataset and a regression type (linear or GLM), passing most of that straight through to `lm()` or
`glm()`. The default objective is AIC, but the interface should allow a user-supplied objective
function, and ideally the genetic operators themselves (beyond the defaults from Givens and
Hoeting) should be extensible by the user. The team may use only base R and the standard `stats`
package for model fitting and similar standard functionality — everything else must be their own
code. Results are demonstrated on two or more examples, worked directly into the function's R help
page. Deliverables: an installable package (via `R CMD INSTALL` on the built `.tar.gz`, or
`install_github`), `testthat` tests runnable as `testthat::test_package('GA')` — checked to still
work when the package is installed outside the team's own development environment — `roxygen2` or
hand-written `.Rd` documentation, and a PDF report in R Markdown or LaTeX.

**Fall 2025 (Python).** The same problem, reimplemented in Python and against a fixed baseball
dataset (from Givens and Hoeting, supplied in the class repository) that the instructor uses for
grading. The defining difference from 2021 is that the team's package, named `GA`, must follow the
instructor's own template repository (`GA-dev`): the primary function `select` and its output
dictionary must conform to a fixed shape, though extra arguments and extra output fields are
allowed. This exists so the instructor's own `test.py` and `assess.py` scripts — an initial version
of which is supplied in the template — run against every team's code without modification; failing
to pass them is called out as something that will "badly hurt" the grade, independent of how good
the variable selection itself turns out to be. Specific requirements layered on top of the shared
rubric:

- **Fitness is 10-fold cross-validated $R^2$**, computed as one minus the ratio of summed squared
  prediction error to the summed squared deviation of the observations from their mean.
- **`pop_size` and `n_gen`** must be arguments to `select`, controlling population size and number
  of generations, so the instructor can bound the run time.
- **A `penalty` argument for prediction methods with built-in regularization.** Some fitting
  methods effectively ignore some predictors on their own, so a CV-$R^2$ fitness may not by itself
  reward a sparse model. Where a `penalty` value $\lambda$ is supplied, fitness is instead
  $$R^2 - \lambda f,$$
  where $f$ is the fraction of the available predictors the model selected — chosen by the
  instructor for grading so that a "moderate" $\lambda$ should push the *default* settings toward a
  reasonably sparse solution.
- **Start with plain linear regression** and get the genetic algorithm working there before
  extending, optionally, to another prediction method — which the handout notes is a natural place
  for individual team members to explore something of their own interest.

The deliverable substitutes a README for the separate PDF report: it presents the package and how
to use it, with demos, and must still include the paragraph on each member's contribution. If the
team wants the demos regenerated automatically, the README can be written as a `.qmd` file and
rendered to `README.md` with `quarto render`. Submission is a form, not a paper copy, and hosting
on `github.berkeley.edu` rather than `github.com` is flagged as costing the team the ability to run
their tests automatically via GitHub Actions.

## What moved between the two genetic-algorithm offerings

Lined up against each other, the 2021 and 2025 versions of the same assignment show what the
instructor tightened over four years, all in the direction of making grading at scale reliable:

- **Interface freedom traded for a fixed template.** 2021 asks for a sensible interface the team
  designs; 2025 hands the team a template repository whose function signature and output shape are
  not negotiable, precisely so the instructor's held-out tests run unmodified.
- **The fitness metric changed from a statistical criterion to a predictive one.** AIC, in 2021,
  penalizes model complexity analytically; cross-validated $R^2$, in 2025, measures held-out
  predictive accuracy directly, with sparsity enforced separately through the `penalty` argument
  when the fitting method needs it.
- **Parallelism became an explicit, graded argument** (`n_workers`) rather than an optional
  extension.
- **An AI-use policy was added**, absent from the earlier handout.
- **The written report became a README**, generated from the same tooling as the code rather than
  submitted as a separate document.
- **Grading infrastructure moved into the repository itself**, via a template test suite runnable
  through GitHub Actions.

## The collaboration process required in every version

Independent of which algorithm, every year's handout prescribes the same process, not just the
same product:

- **Design before dividing the work.** Map out the modular components the package needs and how
  they fit together, and what the primary function will do, before writing code.
- **Pair review.** After one person writes a component, a second team member tests it and improves
  it together with the original author; pair programming is suggested as an option for some of the
  development.
- **Git and GitHub throughout**, not only at submission — the 2025 version adds a suggestion to use
  branches and pull requests once a basic working package exists.
- **A named division of labour.** Every year's report or README must include a paragraph stating
  which team member was responsible for which part of the work.

## Exercises

The course's own final-project tasks, stated here without the algorithmic detail they point at
(Unit 9 notes and Gilks et al. (1992) for the sampler; Section 3.4 of Givens and Hoeting for the
genetic algorithm) and without a solution, since each is a term-length group deliverable rather
than a problem with an answer to check.

1. **Adaptive rejection sampler (Python).** Implement adaptive rejection sampling as an installable
   Python package `ars` with a primary sampling function `ars`. The function's main input should be
   a vectorized Python function computing a (possibly unnormalized) density; the sampler should
   catch, as it runs, cases where its bounding envelope fails to actually bound the density. Start
   the gradient computation with numerical differentiation, and add support for automatic
   differentiation (via JAX or PyTorch) for full credit. Test the sampler by comparing its output
   distribution to the true one, and unit-test the non-trivial internal computations separately.

2. **Genetic algorithm for variable selection (R).** Implement a genetic algorithm for variable
   selection in linear and generalized linear regression as an installable R package `GA`, with a
   primary function `select`. Default to AIC as the objective but allow a user-supplied one; use
   `lm()`/`glm()` for fitting. Demonstrate the package on at least two examples, and test both the
   overall (stochastic) procedure and its individual internal computations.

3. **Genetic algorithm for variable selection (Python, following a fixed interface).** Implement
   the same idea as a Python package `GA` with a primary function `select`, conforming to a
   specified function signature and output shape. Use 10-fold cross-validated $R^2$ as the fitness
   measure, with `pop_size` and `n_gen` controlling the search, and a `penalty` argument producing
   fitness $R^2 - \lambda f$ (with $f$ the fraction of predictors selected) for fitting methods that
   otherwise would not be penalized for including all of them. Begin with plain linear regression
   before considering other prediction methods.

## Sources

- Fall 2024 project handout: `docs/statistical-computing/berkeley/stat243/fall-2024/project/project/01-problem.md`
  and `.../02-formatting-requirements-and-additional-information.md` (converted from
  `berkeley-stat243/fall-2024/project/project.qmd`, CC BY 4.0) — the adaptive-rejection-sampler
  assignment and its deliverables.
- Fall 2025 project handout: `docs/statistical-computing/berkeley/stat243/fall-2025/project/project.md`
  (converted from `berkeley-stat243/fall-2025/project/project.qmd`, CC BY 4.0) — the Python
  genetic-algorithm assignment, template repository, and formatting requirements.
- Fall 2021 project handout: `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/project/project/01-problem.md`
  and `.../02-formatting-requirements-and-additional-information.md` (model-reconstructed from a
  PDF with no text layer, `berkeley-stat243/stat243-fall-2021/project/project.pdf`, CC0-1.0;
  flagged in the source as a paraphrase with unverified equations, though no equations from it are
  quoted here) — the R genetic-algorithm assignment.
- Referred to by these handouts but not supplied to this chapter: the course's own Unit 9 notes
  (Section 5, on adaptive rejection sampling); Gilks, W. R., Best, N. G. and Tan, K. K. C. (1992),
  Section 2.2, on adaptive rejection sampling (PDF distributed only in the class repository);
  Section 3.4 of Givens, G. H. and Hoeting, J. A., *Computational Statistics*, on genetic
  algorithms; the instructor's `GA-dev` template repository and its `assess.py`/`test.py` scripts;
  and the `baseball.dat` dataset used for the 2025 grading examples.

---

[← 13. Using Git for Collaboration](13-using-git-for-collaboration.md) · [Contents](index.md) · [17. Formatting requirements →](17-formatting-requirements.md)
