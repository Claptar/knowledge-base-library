---
title: "79. Stat 210A: Course Information"
course: "Berkeley Stat 210A"
chapter: 79
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 79. Stat 210A: Course Information

## What this covers

This chapter is not lecture mathematics: it collects the front matter of UC Berkeley's Stat 210A —
an introductory Ph.D.-level course in theoretical statistics, taught by Will Fithian — as recorded
in the syllabi posted for three consecutive offerings, Fall 2024, Fall 2025 and Fall 2026. It
answers two questions: what the course is about and how it sits among Berkeley's other statistics
courses, and how the mechanics of grading and assessment were run, and changed, across the three
years. It assumes nothing beyond knowing, in general terms, how a graduate course is organized.

## What the course is about

Stat 210A's own framing starts from a complaint: statistics is used everywhere, and its
practitioners are perpetually accused of not really understanding what they are doing. Statistical
theory is the study of what exactly an analyst is doing, formally, when they use data to draw
conclusions. Most — not all — statistical methods rest on **statistical modeling**: treating the
observed data as the realization of a random data-generating process governed by unknown
**parameters**, and using the data to infer those parameters, or to predict future data, accurately.
Applied courses such as Stat 215A/B ask whether a model has captured something true about the
world; Stat 210A instead takes the model as given and asks how an analyst can use the data most
effectively within it — what makes one estimator, confidence interval, or test better than another,
and how the frequentist and Bayesian answers to that question relate.

The syllabus lists the topics as: statistical decision theory (frequentist and Bayesian),
exponential families, point estimation, hypothesis testing, resampling methods, estimating
equations and maximum likelihood, empirical Bayes, large-sample theory, high-dimensional testing,
and multiple testing and selective inference — covered in both finite samples and asymptotic
regimes, and in both parametric and nonparametric settings. Fall 2024's course-information page
adds that it is "a fast-paced and demanding course intended to prepare students for research
careers in statistics."

**Prerequisites:** linear algebra, real analysis, probability, and (undergraduate) statistics.

### Where it sits among Berkeley's other courses

- **Stat 210B** (210A is a prerequisite) is more technical and covers empirical process theory and
  high-dimensional statistics — the asymptotic and high-dimensional regimes that 210A only touches.
- **CS 281A / Stat 241A** (Statistical Learning Theory) overlaps on estimation and exponential
  families, but leans toward prediction — classification and regression, optimization, signal
  processing — and, in the instructor's judgement, spends less time on inferential questions like
  hypothesis testing, confidence intervals, and causal inference.
- **Stat 215A/B** are the applied counterpart: they ask whether the modeling exercise has actually
  captured something interesting about reality, a question 210A sets aside by construction.

## How the three offerings were run

Will Fithian taught all three offerings; each had a different graduate student instructor (GSI).

| | Fall 2024 | Fall 2025 | Fall 2026 |
|---|---|---|---|
| GSI | Dohyeong Ki | Zhexiao Lin | Chase Mathis |
| Lecture | Tue/Thu 11:00–12:30, Evans 60 | Tue/Thu 9:30–11:00, Evans 60 | Tue/Thu 2:00–3:30, Stanley 106 |
| Small-group meeting | Recitation, every 2nd Friday | Recitation, every 2nd Friday, Evans 332 | Weekly tutorial (mandatory, new format) |
| Final exam | Wed Dec 18, 8–11am | Tue Dec 16, 3–6pm | Tue Dec 15, 8–11am |

Every year follows the same pattern around Thanksgiving: the Tuesday lecture that week moves to
Zoom, the Thursday lecture is cancelled, and office hours are suspended or moved online. All three
years used the same three platforms for course logistics — bCourses for lecture videos and
homework solutions, an Ed Discussion page for announcements and technical discussion ("no homework
spoilers"), and Gradescope for homework submission — under a new course number on each platform
each year.

## Grading: the assessment design changed from year to year

The headline numbers moved every year, and reading the three grading pages together shows a
consistent reason why: each year's change targets whatever part of the previous year's scheme could
be produced without doing the statistics.

**Fall 2024** was the simple version: 50% weekly problem sets, 50% final exam. Problem sets were
graded for correctness, with the lowest two dropped, no late submissions accepted, and generative
AI explicitly banned ("No generative AI allowed for problem sets"). Collaboration was allowed if
acknowledged, but each student had to write up their own solution. The instructor's own warning was
that although the final is nominally half the grade, it "typically accounts for most of the
variance in final course grades" — so treating the homework as the easy half and coasting on it
costs more than it saves.

**Fall 2025** added a component described on the syllabus as "new this semester": a ten-minute
**Tuesday quiz**, given at the start of class, consisting of an extra part of one of the problems
from the homework due the previous Wednesday night. Weights shifted to 40% homework, 20% quizzes,
40% final, with the lowest two homework grades and lowest three quiz grades dropped. The
collaboration policy carried over unchanged — no consulting old solutions, no generative AI — but
the stated purpose of the quiz makes explicit what the drop-in-average concern in 2024 only implied:
"your odds of solving it will be higher if you have read and understood the [homework] solutions."
The quiz exists to make sure students actually engage with the graded solutions once they are
released, not merely bank a homework grade and move on.

**Fall 2026** restructured the scheme more substantially. Weekly homework itself became
**ungraded** for correctness — worth 10% for completion only — and generative AI use on it was
explicitly permitted for the first time: students "are welcome to work with each other or consult
articles, textbooks, or generative AI," though "strongly recommended" to write it up unaided.
Solutions are released fifteen minutes after the due time. In place of graded homework, the course
introduced mandatory weekly small-group **tutorial sections**: each student must come prepared to
present a solution from the previous week's homework — orally at the board or on paper, without
notes — and answer questions about the steps as they go. Tutorial attendance is worth 10% and the
correctness of what is presented, 20%; the grading rule for the latter is a student's best
$8 + \lceil n/2\rceil$ solutions out of $n$ times called on, so being called on more often can only
help a grade, never hurt it. Weekly quizzes stay at 20% of the total (best 9 scores, no makeups),
and the final exam remains 40%.

Set side by side, the shape of the change across three years is the same move made twice: once a
part of the grade can be produced without the work — a solved-by-AI homework set, a homework grade
banked without reading the posted solution — the instructor moves weight off it and onto something
that cannot be outsourced: a timed quiz, an oral presentation given without notes, a proctored
final. The 2026 syllabus does not retain the 2024/2025 commentary about the final exam accounting
for most of the grade's variance; by then the graded weight is already spread across five
components rather than concentrated in the final and the homework.

## References

All three years point to the same reading list. The instructor's own note is that the course's
notes are self-contained, and these are for a different presentation of the same material:

- Keener, *Theoretical Statistics: Topics for a Core Course* (Springer, 2010) — closest in level
  and presentation style to the course.
- Lehmann and Casella, *Theory of Point Estimation* (Springer, 1998) — a detailed reference for the
  estimation material.
- Lehmann and Romano, *Testing Statistical Hypotheses* (Springer, 2005) — a detailed reference for
  the testing and confidence-interval material.
- Hacking, *Probability and Inductive Logic* (Cambridge, 2001) — probability and statistics from a
  philosophical point of view.
- Candès, Stats 300C lecture notes (Stanford, 2016) — covers some of the later material in the
  course.

For prerequisite review: Axler, *Linear Algebra Done Right*; Abbott, *Understanding Analysis*;
Adhikari and Pitman, *Probability for Data Science*.

## Integrity and accommodations

All three years state the same policies. Violating the collaboration policy or otherwise cheating
is a failing grade for the semester and a report to the University Office of Student Conduct, under
the Berkeley honor code. Students needing disability accommodations are asked to come forward as
soon as possible; scheduling conflicts (religious observances, interviews, team travel) should be
raised in writing by the second week of the semester. A separate exam-accommodation form covers
conflicts with the final itself — the instructor's stated preference is always for everyone to sit
the exam in Berkeley at the scheduled time, with the deadline to request an exception moving earlier
each year: October 4 in 2024, October 3 in 2025, September 18 in 2026.

## Sources

- Fall 2024 syllabus (`berkeley-stat210a/fall-2024/syllabus.qmd`, CC BY 4.0): course information,
  about page, references, and grading — `docs/statistics/berkeley/stat210a/fall-2024/syllabus/01-course-information.md`
  through `04-grading.md`.
- Fall 2025 syllabus (`berkeley-stat210a/fall-2025/syllabus.html`, CC BY 4.0):
  `docs/statistics/berkeley/stat210a/fall-2025/syllabus/01-course-information.md` through
  `04-grading.md`. This is the version used above for Fall 2025 detail; a near-duplicate capture at
  `docs/statistics/berkeley/stat210a/fall-2025/units/syllabus/` (from `units/syllabus.html`) records
  an earlier draft of the same page — GSI listed as "TBD" and a garbled sentence in the drop-policy
  paragraph — and was not separately reproduced.
- Fall 2026 syllabus (`berkeley-stat210a/fall-2026/syllabus.qmd`, CC BY 4.0):
  `docs/statistics/berkeley/stat210a/fall-2026/syllabus/01-course-information.md` through
  `04-grading.md`.
- The "About Stat 210A" text (what the theory of statistics is, the topic list, prerequisites, and
  the comparison to other Berkeley courses) is essentially identical word-for-word across all three
  years' `02-about-stat-210a.md` pages, and is presented once above rather than three times; the
  Fall 2025 and Fall 2026 versions add a link to a course FAQ page (not itself supplied) under
  prerequisites.
- No slides, transcript, or exercises were supplied for this entry.

---

[← 78. Sufficiency and Minimal Sufficiency (part 2)](78-sufficiency-and-minimal-sufficiency-part-2.md) · [Contents](index.md) · [80. p-Values →](80-p-values.md)
