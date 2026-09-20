---
title: "73. A Curved Gaussian Family"
course: "Berkeley Stat 210A Fall 2024"
chapter: 73
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 73. A Curved Gaussian Family

## What this covers

This chapter preserves a single exam problem: part of Question 1 from the Fall 2018 final
examination for STAT 210A (Prof. William Fithian), on a two-dimensional Gaussian family whose
mean vector is traced out by a single real parameter. It assumes the reader already has the
course's definitions of a sufficient statistic, a minimal sufficient statistic, and a complete
statistic — the exam itself tells students they may use "any results from lecture or homework...
without rederiving them." Those definitions are not repeated here because they are not in this
source; see the course's own lecture notes for them.

The source materials for this task are two copies of the same converted PDF (from the
`fall-2024` and `fall-2026` mirrors of the course repository), and the conversion breaks off
after the first sub-part of the first problem. What follows is exactly what survived that
conversion — no later parts of the problem, and no solutions, despite the file being named
"Solution2018."

## The family

The exam sets up $n$ i.i.d. bivariate observations

$$X_1, \ldots, X_n = \begin{pmatrix} X_{1,1} \\ X_{1,2} \end{pmatrix}, \ldots,
\begin{pmatrix} X_{n,1} \\ X_{n,2} \end{pmatrix} \stackrel{\text{i.i.d.}}{\sim} N_2(\mu(\theta), I_2),$$

for a single real parameter $\theta \in \mathbb{R}$, where

$$\mu(\theta) = \begin{pmatrix} \theta \\ \theta^2 \end{pmatrix}.$$

So each observation is a bivariate normal with identity covariance, but the mean is not free to
range over all of $\mathbb{R}^2$: as $\theta$ varies, $\mu(\theta)$ traces out the parabola
$\{(t, t^2) : t \in \mathbb{R}\}$, a one-dimensional curve inside the two-dimensional mean space.
That is the sense in which the exam calls this a "curved" Gaussian family — a single scalar
parameter is being asked to do the work of a two-dimensional mean, and the family sits inside a
larger, full two-parameter Gaussian model without filling it out.

The problem supplies the univariate Gaussian density as a reminder:

$$\frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{ -\frac{(x - \mu)^2}{2\sigma^2} \right\}.$$

## Exercises

**1(a).** For the curved Gaussian family above, show that $T(X) = \sum_i X_i \in \mathbb{R}^2$
is a minimal sufficient statistic, but is not complete.

(The exam problem is worth 20 points total, 4 points per part, and is explicitly marked as
having further parts; the conversion available for this chapter stops here, so parts (b) onward
are not reproduced.)

## Sources

- Both copies of the converted exam booklet are identical in the portion recovered:
  `docs/statistics/berkeley/stat210a/fall-2024/old-exams/solution2018.md` and
  `docs/statistics/berkeley/stat210a/fall-2026/old-exams/solution2018.md`, each converted from
  `old-exams/solution2018.pdf` in the respective course repository mirror (Fall 2018 final exam,
  Prof. William Fithian, STAT 210A, Berkeley; licensed CC BY 4.0).
- Both files carry a fidelity note that the source PDF had no usable text layer and was
  reconstructed by a model, with every equation unverified; the conversion is truncated after
  part (a) of Problem 1 in both copies, so parts (b) and later, and any other problems on the
  exam, are not available in either input and are not reproduced here.
- The exam instructions permit students to use, without proof, "any results from lecture or
  homework" — i.e. the course's definitions of sufficiency, minimal sufficiency and completeness
  — but the lecture material itself was not among the inputs for this chapter.

---

[← 72. Score, Fisher Information, and CRLB (part 2)](72-score-fisher-information-and-crlb-part-2.md) · [Contents](index.md) · [74. Sufficiency, Minimax, and Asymptotic Theory →](74-sufficiency-minimax-and-asymptotic-theory.md)
