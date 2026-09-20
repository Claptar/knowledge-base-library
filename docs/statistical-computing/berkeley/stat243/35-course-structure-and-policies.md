---
title: "35. Course Structure and Policies"
course: "Berkeley Stat 243 Fall 2024"
chapter: 35
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 35. Course Structure and Policies

## What this covers

This chapter merges the syllabi of the three most recent offerings of Statistics 243 — UC Berkeley's
graduate course in statistical computing, taught by Chris Paciorek in Fall 2024, Fall 2025, and Fall
2026 — into a single description of what the course is, what it expects, and how it is graded. It
assumes nothing about statistical computing itself; what it answers is the practical question a
student asks before or during the term: what is this course actually for, and how do I pass it. Read
alongside it, the differences between the three years are themselves informative, since they show an
instructor revising a course's assessment scheme in real time in response to generative AI.

## What the course covers, and what it does not

Statistics 243 teaches statistical computing using Python, with "statistical" read broadly enough to
include data science and machine learning. It has two halves that recur across all three years:

- **Programming concepts**: data and text manipulation, regular expressions, data structures,
  functions and variable scope, memory use and efficiency, debugging, testing, and parallel
  processing.
- **Statistical computing concepts**: working with large datasets, numerical linear algebra, computer
  arithmetic and precision, simulation studies and Monte Carlo methods, and numerical optimization.

Alongside these, the course covers UNIX/Linux basics — shell scripting and working on remote servers —
and a bit of R. The explicit goal is that this material *complement* the models and methods taught
elsewhere in the statistics/biostatistics graduate curriculum, rather than duplicate it.

The course is deliberately not two things it might be mistaken for. It is not a course in Python —
Python is the vehicle for illustrating computing concepts, not the subject — and it is not a course
in specific statistical, machine-learning, or data-analysis methods.

**Objectives.** By the end of the course, a student should be able to operate effectively in a UNIX
environment and on remote servers and compute clusters; have a solid, principled understanding of
general programming concepts, including advanced Python; be familiar with tools and practices for
reproducible research; and be able to use principles of numerical precision, numerical linear algebra,
optimization, and simulation in statistical and data-science work.

**Topics, in the order taught.** Across Fall 2024 and Fall 2025 the course ran as a single semester
with twelve topic blocks, in this order: introduction to UNIX and compute servers; data formats,
access, and webscraping; debugging and reproducible research; the bash shell, shell scripting, and
version control; programming concepts and advanced Python (the largest block, at nine class days);
parallel processing; databases, hashing, and big data; computer arithmetic; simulation and Monte
Carlo; numerical linear algebra; optimization; and graphics.

**Fall 2026 restructured this into two half-semester, two-credit courses**, Stat 243A and Stat 243B,
offered back to back rather than as one term-long course. 243A carries the programming half — UNIX,
shell and version control, debugging, advanced Python, databases and big data, parallel processing,
and data access/webscraping. 243B carries the numerical half — computer arithmetic, simulation and
Monte Carlo, numerical linear algebra, optimization, and a new unit on optimization for deep learning.
The graphics unit present in 2024/2025 does not appear in the 2026 topic list.

## Prerequisites

The course expects a background in probability and statistics and a basic ability to use a computer,
but not familiarity with a UNIX-style command line. In 2024 and 2025 it additionally listed calculus
and linear algebra as expected background for the whole course, and expected working knowledge of
Python at the level of the department's pre-term computing-skills workshop (the same workshop's
materials are recommended as a general reference throughout, in particular for the units on data
formats, shell scripting, big data, and computer arithmetic). Students without that background are
told to expect to spend the first couple of weeks catching up.

Splitting the course in 2026 let the two halves have different prerequisites: 243A expects the same
Python background as before; 243B expects comfort with calculus and linear algebra and with
programming in Python, though not at the same level of experience as 243A.

## Course sites, sections, and computing resources

Course material — everything except recorded video — is posted on the course website and its GitHub
repository. Announcements, questions, and discussion happen on Ed Discussion, and students are told
explicitly that they are responsible for tracking announcements there (with the suggestion to turn on
email notifications), not for the instructor to relay them elsewhere. Assignments are submitted
through Gradescope (Pensive/Gradescope from 2026), and recorded lectures are posted to the bCourses
Media Gallery.

A GSI leads a weekly two-hour discussion section, offered at two times; the earlier slot is
consistently more in demand, so students are asked to attend their assigned section unless they have
arranged otherwise. Section content varies — demonstrations of tools such as version control and
debugging, group work, discussion of relevant papers and of problem-set solutions — and from 2025
onward also hosts the short per-problem-set quizzes described below.

Most work can be done on a personal laptop; later in the course (243A, from 2026) work moves to the
Statistics Department's Linux cluster, with the SCF JupyterHub or campus DataHub as alternatives for a
shell or notebook (DataHub's limited CPU and memory make it unsuitable for the heavier work later in
the course). Required software is the UNIX command line, Git, Python (Miniforge/Conda recommended),
and Quarto; VS Code was added to the list starting in 2025, moving from an optional tool that year to
one the course uses "extensively" by 2026.

## Class time

Classes are meant to be interactive: the instructor poses questions worked through via in-class
polling or Google Forms, occasionally asks students to prepare material or submit answers before
class, and expects students with more background on a given topic to contribute their perspective
alongside those still catching up, since there is rarely one right way to do something in Python or in
a UNIX environment. Phones are discouraged and laptop use is meant to stay on the material at hand.
Recordings are kept on bCourses for review or to cover an absence.

## How the course is graded, and how that changed

The three years show a single instructor visibly revising the assessment scheme, and the reasoning
behind each change is worth following as closely as the scheme itself.

**Fall 2024 — the baseline.** The grade was 50% problem sets, 25% two in-term quizzes, 15% a final
group project, and 10% participation (in-class Google Forms responses, occasional non-problem-set
assignments, and substantive contribution to Ed Discussion). There was no final exam. Each problem
set was scored 0–3 on three separate components — presentation, technical accuracy, and code quality
— and a late submission cost two points, or four if turned in after grading had begun. Working
together was allowed under specific rules: discuss approaches and share short syntax fixes, but never
complete code or solutions; a ChatGPT-style tool could be used for small sub-parts of a problem but
not for an entire question; and every source of outside help, human or AI, had to be credited, with a
required "Collaboration" section naming any students consulted.

**Fall 2025 — quizzes and an explicit AI policy.** The instructor states plainly that this is the
first time trying the new approach, "in reaction to the impacts of AI." The two in-term quizzes were
renamed mini-exams, and a new, short, closed-book quiz was added *in section*, immediately after each
problem set is due, asking questions directly tied to a subset of that problem set's content. The
framing given for this is a train/test split: the problem set is the training set, where a student has
real freedom — including freedom to use AI tools or classmates for anything short of a complete
solution — and the quiz is the test set, where relying on that freedom instead of understanding the
material shows up as poor performance, i.e. overfitting. Consistent with that framing, problem sets
moved to an essentially complete/incomplete rubric (0–2 per component, rather than 0–3), with
technical understanding assessed by the quiz rather than by grading the problem set itself; a graded,
point-based quiz retake was available by arrangement with the instructor. Grading weights shifted
accordingly: 45% problem sets (15% completion, 30% quiz performance), 30% mini-exams, 15% project, 10%
participation. The requirement for a written Collaboration section was dropped in favor of
attributing specific ideas inline, wherever they came from — a classmate, a chatbot, or an AI coding
assistant.

**Fall 2026 — split into two half-semester courses.** With the course now taught as 243A and 243B,
each carries its own single mini-exam rather than sharing two, and neither retains the joint final
project that appeared in 2024 and 2025. Grading per half-course is 55% problem sets (20% completion,
35% quiz performance), 35% mini-exam, and 10% participation. The AI policy and train/test framing
carry over essentially unchanged, with an added caution that the quiz retake option is meant for real
difficulty, not for disputing a point or two, and should be used "once or twice" at most. Late problem
sets are simply accepted up to a fixed late deadline and then not graded at all, with a pattern of
lateness folded into the participation grade instead of a per-day point deduction.

## Problem-set mechanics and academic integrity

Across all three years, a problem set is prepared in Quarto and submitted twice: a PDF to Gradescope
(Pensive/Gradescope from 2026) by the start of class, timestamped there for lateness purposes, and the
PDF together with code and the Quarto source pushed to a personal GitHub repository. The instructor is
explicit about what full credit requires: a stated goal and strategy before the code for a problem,
key code embedded in the document with longer function definitions moved to an appendix, and — stated
as a rule, not a preference — that "raw code without explanation is not an appropriate solution."
Mathematical derivations may be handwritten and scanned rather than typeset. Every idea taken from
somewhere else — a textbook, a classmate, or an AI tool — needs to be attributed at the point it is
used, both to reinforce ordinary citation practice and, the instructor notes, so a student stays
honest with themselves about how much of the work is actually theirs.

The campus Honor Code sits behind all of this: "As a member of the UC Berkeley community, I act with
honesty, integrity, and respect for others." Concretely, it holds that studying together is
encouraged, but that homework, unless stated otherwise, is submitted as independent work; that
cheating on a quiz or exam brings a failing grade in the course and a report to the campus Center for
Student Conduct; and that plagiarism — copying text or ideas without attribution — brings a failing
grade on the assignment and typically further disciplinary action. The text is identical across all
three years of the syllabus, with only the pointer at its head updated each year to note that the
course's own rules on AI, collaboration, and independence (above) are what actually governs a problem
set.

## Sources

All from the library's converted Berkeley STAT 243 syllabi (CC BY 4.0), read across all three offered
years since each covers the same six sections and the differences between them are the point of this
chapter:

- Fall 2024 — `01-course-description.md` through `06-campus-honor-code.md`
  (`docs/statistical-computing/berkeley/stat243/fall-2024/syllabus/`), converted from
  [`syllabus.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/syllabus.qmd).
- Fall 2025 — the same six files
  (`docs/statistical-computing/berkeley/stat243/fall-2025/syllabus/`), converted from
  [`syllabus.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/syllabus.qmd).
- Fall 2026 — the same six files
  (`docs/statistical-computing/berkeley/stat243/fall-2026/syllabus/`), converted from
  [`syllabus.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/syllabus.qmd).

No slides or lecture transcript were supplied for this entry — the source is administrative rather
than a taught lecture. The syllabus text points to several things it does not itself contain: the
qualitative grading rubric (`rubric` in each year's course GitHub repository), the problem-set
submission how-to (`howtos/submitPS`), the department's computing-skills workshop materials for each
year, and the course's office-hours page. None of these were part of the supplied material and none
of their content appears above.

---

[← 34. Structuring a Simulation Study](34-structuring-a-simulation-study.md) · [Contents](index.md) · [36. Unix, Version Control, and Editors →](36-unix-version-control-and-editors.md)
