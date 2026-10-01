---
title: "8. The Final Project"
course: "Berkeley Stat 156"
chapter: 8
source: "https://github.com/berkeley-stat156/fall-2024"
licence: "CC BY-NC 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 156](https://github.com/berkeley-stat156/fall-2024), licensed CC BY-NC 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. The Final Project

## What this covers

This chapter is not a lecture but the final-project brief for Stat 156/256: what an acceptable
project looks like, what the writeup for each type of project should contain, and where to find
papers and data to build one from. It assumes the causal-inference toolkit the rest of the course
builds — identification assumptions, propensity scores, inverse probability weighting (IPW),
treatment-effect bounds, and Fisherian rerandomization tests — since the project asks you to apply
that toolkit to a real paper or dataset rather than to learn it here.

## The two project formats

The project is done in groups of three, and the course recommends one of two forms.

**Replication and re-analysis.** You pick an academic paper whose original data (or comparable
data) is public, and you reproduce its results and then re-analyze them with methods from the
course. A specific instruction governs which version of the data to use: many papers post a
dataset alongside the publication that has already been cleaned to match the published tables
exactly. Unless the paper is an experimental study, you should *not* start from that cleaned
version — the point of the exercise is that your group downloads the raw data and does its own
cleaning to approximately match the paper's sample selection, so that you have actually rebuilt
the empirical pipeline rather than inherited it.

**Applied data analysis.** You pose your own applied research question against a publicly
available dataset — for instance, one drawn from an academic paper — and choose a course method
suited to answering it. Here a cleaned dataset is acceptable, because the object of the exercise
is the choice and justification of method, not the reconstruction of someone else's cleaning
pipeline.

A third option exists outside these two templates: a literature review paired with simulation
studies comparing several methods. The guidelines do not specify a format for this option; instead
they route it through an office-hour appointment with the GSIs, which is worth noting because it
means this path is negotiated rather than templated.

## Writing up a replication and re-analysis

The suggested writeup is framed deliberately as a paper "ready to be submitted to a journal," not
as a homework report, and it has four parts.

**Paper summary and summary statistics.** State the paper's research question and its answer,
describe the datasets it uses, clean the data, and reproduce a summary-statistics table (mean,
median, interquartile range, and so on for the key variables and covariates). The guidelines are
explicit that this table need not match the paper's exactly: "90% of the effort in an observational
empirical paper is cleaning the data," and it is fine not to reproduce the paper's cleaning exactly.

**Replicating the main result.** Describe the paper's identification strategy — whether it runs a
randomized experiment or leans on a policy change or other natural experiment — and state its
identifying assumptions in both English and mathematics. Reproduce the main result and interpret
it. Then appraise the identification assumptions critically: for an experiment, was it actually
balanced, and did it achieve what the authors claim it achieves? For a natural experiment, what
confounding could undermine the "as-if random" story?

**Replicating a robustness check or extension.** Empirical papers in economics and the social
sciences typically follow the main result with a section — "Robustness Checks" for observational
studies, "Extensions" for experimental ones — whose job is to convince the reader the main result
survives scrutiny of the identification assumption, or to bring out a subtlety in how it should be
read. Pick at least one such check from the paper, replicate it, and write up what it is actually
checking.

**Re-analysis.** Apply a method from the course — IPW estimators, treatment-effect bounds, or
Fisherian rerandomization tests are the course's own examples — to the paper's main result, justify
why that method is appropriate for the paper's setting, and compare what it gives you against the
paper's original result. If the two disagree materially, the writeup should conjecture or analyze
why.

## Writing up an applied data analysis

The same four-part shape recurs, but organized around a question you posed rather than a paper you
are reproducing.

**Problem formulation.** Introduce and motivate the research question, summarize what related
literature has found, and state the question precisely.

**Method.** Propose one or more methods from the course, described both conceptually and in
mathematical notation. Justify why the method fits the question, state the assumptions under which
it answers the question — again in both English and math — and discuss where the method falls
short.

**Results and discussion.** Present and interpret the results in English, tie them back to the
original question, compare them against prior work, and revisit the method's limitations in light
of what was actually found.

**Robustness check.** As above, this section exists to test whether the result survives scrutiny
of one of the method's key assumptions; describe the check, run it, and explain what passing or
failing it would mean.

## Robustness checks and extensions, in general

Both writeup templates lean on the same convention from empirical social science: a result is
followed by a section that stress-tests it rather than simply restating it. The label depends on
the study design — "Robustness Checks" when the study is observational and the worry is a violated
identification assumption, "Extensions" when the study is experimental and the worry is more often
about how far the headline result generalizes or what it means in a related setting. Either way,
the section's purpose is the same: give the reader a reason to believe the main result is not an
artifact of one particular specification.

## Finding papers to replicate

Data-sharing requirements make some fields much easier to replicate from than others, and the
guidelines point at fields where journals have made this a policy rather than a courtesy.

| Field | Journals to look in |
| --- | --- |
| Economics | American Economic Review, American Economic Journal: Applied Economics, American Economic Journal: Economic Policy (all AEA journals, which have required data and code since 2005 where it can be shared); also the Quarterly Journal of Economics, Journal of Political Economy, and Journal of Labor Economics, which have adopted data-sharing policies within roughly the last five years |
| Epidemiology and biostatistics | Biostatistics, Biometrics, American Journal of Epidemiology, Statistics in Medicine, Statistical Methods in Medical Research, PLOS ONE Epidemiology |
| Sociology and political science | American Journal of Political Science (data-sharing since 2014), Sociological Methods & Research (since 2009) |

The course also suggests a specific list of observational-study papers as replication candidates:

- Daron Acemoglu and Joshua D. Angrist, "Consequences of Employment Protection? The Case of the
  Americans with Disabilities Act," *Journal of Political Economy*, 2001
- Daron Acemoglu, David H. Autor and David Lyle, "Women, War and Wages: The Effect of Female Labor
  Supply on the Wage Structure at Mid-Century," *Journal of Political Economy*, 2004
- Elizabeth O. Ananat, "The Wrong Side(s) of the Tracks: The Causal Effects of Racial Segregation
  on Urban Poverty and Inequality," *American Economic Journal: Applied Economics*, 2011
- Maximilian Auffhammer and Ryan Kellogg, "Clearing the Air? The Effects of Gasoline Content
  Regulation on Air Quality," *American Economic Review*, 2011
- Patricia Cortes and Jose Tessada, "Low-Skilled Immigration and the Labor Supply of Highly Skilled
  Women," *American Economic Journal: Applied Economics*, 2011
- David Deming, "Early Childhood Intervention and Life-Cycle Skill Development: Evidence from Head
  Start," *American Economic Journal: Applied Economics*, 2009
- Daniel K. Fetter, "How Do Mortgage Subsidies Affect Home Ownership? Evidence from the Mid-Century
  GI Bills," *American Economic Journal: Economic Policy*
- Alexander M. Gelber, "How Do 401(k)s Affect Saving? Evidence from Changes in 401(k) Eligibility,"
  *American Economic Journal: Economic Policy*, 2011
- Jonathan Gruber and Samuel A. Kleiner, "Do Strikes Kill? Evidence from New York State," *American
  Economic Journal: Economic Policy*, 2012
- Hilary W. Hoynes and Diane Schanzenbach, "Consumption Responses to In-Kind Transfers: Evidence
  from the Introduction of the Food Stamp Program," *American Economic Journal: Applied Economics*,
  2009
- David S. Johnson, Jonathan A. Parker and Nicholas S. Souleles, "Household Expenditure and Income
  Tax Rebates of 2001," *American Economic Review*, 2006
- David S. Johnson, Robert McClelland, Jonathan A. Parker and Nicholas S. Souleles, "Consumer
  Spending and the Economic Stimulus Payments of 2008," *American Economic Review*, 2013
- Melissa S. Kearney and Phillip B. Levine, "Early Childhood Education by Television: Lessons from
  Sesame Street," *American Economic Journal: Applied Economics*, 2019
- Jeanne Lafortune, "Making Yourself Attractive: Pre-marital Investments and the Returns to
  Education in the Marriage Market," *American Economic Journal: Applied Economics*, 2013
- Phillip B. Levine, Robin McKnight and Samantha Heep, "How Effective Are Public Policies to
  Increase Health Insurance Coverage among Young Adults?," *American Economic Journal: Economic
  Policy*, 2011
- Gianmarco Ottaviano, Giovanni Peri and Greg C. Wright, "Immigration, Offshoring and American
  Jobs," *American Economic Review*, 2013
- Albert Saiz and Susan Wachter, "Immigration and the Neighborhood," *American Economic Journal:
  Economic Policy*, 2011
- Betsey Stevenson and Justin Wolfers, "Bargaining in the Shadow of the Law: Divorce Laws and
  Family Distress," *Quarterly Journal of Economics*, 2006
- Li L, Greene T., "A weighting analogue to pair matching in propensity score analysis," *The
  International Journal of Biostatistics*, 2013
- Baiocchi M, Cheng J, Small D.S., "Instrumental Variable Methods for Causal Inference" (tutorial in
  biostatistics)
- Kurth, Tobias, et al., "Results of multivariable logistic regression, propensity matching,
  propensity adjustment, and propensity-based weighting under conditions of nonuniform effect,"
  *American Journal of Epidemiology*, 2006
- Franklin, Jessica M., et al., "Comparing the performance of propensity score methods in
  healthcare database studies with rare outcomes," *Statistics in Medicine*, 2017
- Austin, Peter C., and Elizabeth A. Stuart, "Moving towards best practice when using inverse
  probability of treatment weighting (IPTW) using the propensity score to estimate causal treatment
  effects in observational studies," *Statistics in Medicine*, 2015

The last several entries on the biostatistics side of the list — Li & Greene, Baiocchi–Cheng–Small,
Kurth et al., Franklin et al., and Austin & Stuart — are themselves methods papers on propensity
scores and instrumental variables rather than applied studies to replicate outright; they read
naturally as background for a project that uses IPW or propensity-score methods, alongside a
substantive paper drawn from the list above them or found independently.

## Finding datasets

Where a project needs a dataset rather than (or in addition to) a specific paper's replication
files, the guidelines point to several general-purpose repositories:

- **ICPSR** — a user-supported repository at the University of Michigan holding thousands of
  datasets; most major universities subscribe, and datasets download after registration.
- **IPUMS** — harmonized census and survey data from around the world, hosted at the University of
  Minnesota.
- **Panel Study of Income Dynamics (PSID)** — the longest-running longitudinal household survey in
  the world, widely used in the social sciences.
- **National Longitudinal Survey of Youth (NLSY)** — longitudinal data on young adults, also
  common in social-science work.
- **National Health and Nutrition Examination Surveys (NHANES)** — a health study commonly used in
  epidemiology and public health.
- **Harvard Dataverse** — a code-and-data repository spanning a broad range of academic papers;
  the guidelines note that a project should check carefully for data on Dataverse that is *not*
  already cleaned, for the same reason raw data is preferred for a replication project above.
- A final entry, evidently a source of US government open data, is cut off mid-sentence in the
  original document and is reproduced here as it stands rather than completed by guesswork.

## Sources

All four parts of this chapter come from the same converted PDF, `ProjectGuidelines.pdf`
(berkeley-stat156, fall 2024, CC BY-NC 4.0):

- Project format and group size —
  [`01-stat-156-256-project-guidelines.md`](https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/ProjectGuidelines.pdf)
- Replication-and-re-analysis writeup structure —
  `02-suggested-writeup-for-replication-re-analysis.md`
- Applied-data-analysis writeup structure —
  `03-suggested-writeup-for-applied-data-analysis.md`
- Journal list, suggested papers, and dataset repositories —
  `04-how-to-find-academic-papers-for-replication.md`

No slide deck, transcript, or exercise set was supplied for this chapter — the project guidelines
are the only material. The source PDF had no extractable text layer, so all four files were
reconstructed by a model reading the page images; each carries the note that the prose is a
paraphrase in places, and the one incomplete list item under *Finding datasets* is a direct
consequence of that reconstruction rather than an omission introduced here. Nothing about the
course's own causal-inference methods (IPW, propensity scores, treatment-effect bounds,
rerandomization tests) is explained in this material — they are referenced by name as tools the
project should apply, and their content belongs to earlier chapters of the course.

---

[← 7. Course Reading Guide](07-course-reading-guide.md) · [Contents](index.md) · [9. Introduction to Causal Inference →](09-introduction-to-causal-inference.md)
