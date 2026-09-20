---
title: "129. Stat 153 Course Syllabus"
course: "Berkeley Stat 153 Fall 2024"
chapter: 129
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 129. Stat 153 Course Syllabus

## What this covers

This chapter is not a lecture but the syllabus material for UC Berkeley's Stat 153, *Introduction to
Time Series* (cross-listed at the graduate level as Stat 248). Three of the five syllabi collected for
the course carry real content — Fall 2024, Spring 2025, and Spring 2026 — and this chapter merges
them, since each offering keeps most of the previous one's structure. It assumes nothing beyond
knowing what a syllabus is for; it exists to give the surrounding context for the rest of the course's
chapters: what background the lectures assume, what topics they are meant to cover, and how the course
is assessed.

## What the course covers

Fall 2024 (instructor Ryan Tibshirani) describes the course as covering "the basics of time series
analysis and prediction," with the class "mostly focused on computational and practical aspects, with
a limited emphasis on theory" — theory is included mainly to build "a better root understanding of the
nature of the topic at hand." Spring 2025 (instructor Aditya Guntuboyina) frames it the same way: time
series, and sequential data more generally, is data with a temporal order, and the course's aim is to
build mathematical models that give plausible descriptions of such data. Spring 2026 (instructor
Liberty Hamilton) adds concrete examples of what a time series is — hourly temperature readings, stock
market fluctuations, brain responses to a stimulus — with the same aim: uncovering regular patterns,
including cycles and trends, and modeling them.

The stated topic lists are close across offerings but not identical:

- **Fall 2024:** measures of dependence, stationarity, regression, smoothing, spectral analysis, ARIMA
  models, ETS models, advanced forecasters, scoring and calibration, ensembling.
- **Spring 2025:** multiple linear regression models (time-dependent covariates), nonlinear regression
  models, regularized high-dimensional linear regression, variance models and spectral analysis,
  lagged regressions and ARIMA models, recurrent neural networks.
- **Spring 2026:** the same six items as Spring 2025, plus self-supervised models, with applications
  drawn from speech processing, neuroscience, astronomy, and epidemiology.

The list grows mainly at the modeling end between 2024 and 2026: high-dimensional regression,
recurrent networks, and self-supervised models are not mentioned in the 2024 topic list but appear
from 2025 onward.

## Prerequisites

All three offerings state the same core requirement: undergraduate probability at the level of Stat
134 or Data 140 (Spring 2026 also accepts EE 126), with Stat 133 and Stat 135 recommended and Stat 135
allowed concurrently — Spring 2026 adds that some students have found the course "challenging without
prior completion of Stat 135."

The programming expectation changes across offerings. Fall 2024 assumes "a basic level of fluency"
with R; homework uses R, with Python examples "if we are able to pull it off." By Spring 2025,
students are free to use any language for homework, but lectures and labs use Python. Spring 2026
makes Python a prerequisite outright: "labs, homework, and projects will be completed in the Python
language, and familiarity with Python is a prerequisite." The course moved from an R-based to a
Python-based class between 2024 and 2026.

## Stat 153 versus Stat 248 (and Stat 158)

The course is cross-listed: Stat 153 is the undergraduate section and Stat 248 the graduate one
(Spring 2026 also lists a Stat 158 cross-listing). The two offerings that describe this — Spring 2025
and Spring 2026 — agree on the mechanism: each homework carries one to three extra questions that only
Stat 248 students must answer, and the exams for the two sections may differ. The one change between
years is at the end of the course: Stat 153 keeps a final exam in both years, but by Spring 2026
Stat 248 substitutes a final project for the final exam (with details announced later in the term);
the Spring 2025 syllabus does not mention a 248-specific difference in the final assessment beyond the
extra homework questions.

## Materials

No offering requires a textbook. Fall 2024 gives no reference text at all. Spring 2025 points students
to Shumway and Stoffer's *Time Series Analysis and Its Applications* — used as required reading in
earlier years of the course, and strong on ARIMA modeling and spectral analysis — as well as to
Tibshirani's Fall 2024 materials and to Guntuboyina's own Fall 2022 lecture notes, with the caveat that
the Fall 2022 notes "will have some overlap" with the current course "but there will be many
departures as well." Spring 2026 recommends the same Shumway and Stoffer book (4th or 5th edition; the
5th is free online through Springer via the campus library proxy) and otherwise supplies lecture notes
and book-chapter PDFs directly, posted after each lecture.

## Assessment and policy

Grading is close to fixed across offerings — 50% homework, 20% midterm, 30% final — which the Spring
2025 syllabus states as a formula:

$$50\% \ \text{Homework} + 20\% \ \text{Midterm} + 30\% \ \text{Final},$$

with each homework assignment worth an equal share; Fall 2024 and Spring 2026 state the same
percentages in prose. Spring 2026 adds an alternative for Stat 153/248: the grade may instead be
computed as 50% homework + 50% final exam or project, whichever is higher.

The late-work policy differs sharply by year. Fall 2024 grants five late days, which a student can
allocate however they like across the semester's homeworks; beyond that, late homework is not accepted
except in a genuine emergency. Spring 2025 and Spring 2026 instead grant **120 late hours** for the
whole semester, applicable across all homeworks, after which no further credit is given for lateness.

Academic-integrity language is consistent across the offerings that state it: students may discuss
homework in small groups but must write up their own solutions (and, by Spring 2026, their own code),
must never read or copy another student's solutions, and must cite any book or online source used
without copying it verbatim. Spring 2026 is the only syllabus of the three that names generative AI
directly: any use of tools such as ChatGPT, Claude, or Gemini must be checked and verified step by
step, and cited — for example, "Consulted ChatGPT for Problem 1.4, Shumway and Stoffer for Problem
1.5."

Fall 2024 and Spring 2026 both close with a "take care of yourself" note, pointing students toward the
campus Academic Accommodations Hub for support during the semester; Spring 2026 adds a request not to
attend class while sick.

## Sources

- Fall 2024 syllabus (instructor Ryan Tibshirani):
  `docs/statistics/berkeley/stat153/fall-2024/syllabus/syllabus.md` — course description, topics,
  prerequisites, evaluation, homework and late-day policy, "take care of yourself" note.
- Spring 2025 syllabus (instructor Aditya Guntuboyina):
  `docs/statistics/berkeley/stat153/spring-2025/syllabus.md` — course description, topics,
  prerequisites, programming language, reference materials, homework schedule, exam dates, grading
  formula, Stat 153/248 differences, academic integrity. This page was converted by a model from a PDF
  with no text layer (marked "reconstructed" fidelity in its source note); its prose is a paraphrase
  and should be treated as a pointer to the original PDF rather than a verbatim quotation.
- Spring 2026 course-information page (instructor Liberty Hamilton):
  `docs/statistics/berkeley/stat153/spring-2026/syllabus/01-course-information.md` — course
  description, prerequisites, materials, exams, grading, Stat 153/248/158 cross-listing, late policy,
  academic integrity including the generative-AI policy, accommodations, "take care of yourself" note.
- Fall 2025 and Fall 2026 "syllabus" pages
  (`docs/statistics/berkeley/stat153/fall-2025/syllabus.md` and
  `docs/statistics/berkeley/stat153/fall-2026/syllabus.md`) are placeholder text — a generic "Dept
  999" template filled with Lorem ipsum — and contain no actual information about this course; nothing
  from them is used here.
- No slides, transcript, or exercises were supplied for this chapter.

---

[← 128. Supplementary Reading List](128-supplementary-reading-list.md) · [Contents](index.md) · [130. Finger Tapping Regression Exercise →](130-finger-tapping-regression-exercise.md)
