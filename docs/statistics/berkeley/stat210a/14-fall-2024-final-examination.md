---
title: "14. Fall 2024 Final Examination"
course: "Berkeley Stat 210A"
chapter: 14
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Fall 2024 Final Examination

## What this covers

This chapter is the Fall 2024 final examination for Stat 210A (Theoretical Statistics), Prof. Will
Fithian. Only the exam's own material was supplied — a title page of instructions and the first two
problems — and the second of those breaks off mid-statement in the source, so this chapter carries
one complete problem and one partial one. It assumes everything the semester built toward
multivariate Gaussian inference and Bayesian decision theory: the $\chi^2$, $t$ and $F$ distributions
arising from Gaussian samples, unbiased risk estimation, and the mechanics of a conjugate Bayesian
model (posterior computation, Bayes estimators under a loss function, and Bayes/minimax risk). No
solutions are given, in keeping with the exam's own instructions.

## About the exam

The exam is organized as a sequence of problems worth about 20 points each, split into 5-point
parts, each opening with a short list of "useful facts" — standard densities and identities the
student may use without re-derivation. The exam's own ground rules, worth keeping in mind when
working the problems below, were:

- Results proved in lecture or on homework may be used without re-derivation, provided it is clear
  which result is being invoked; regularity conditions for named theorems need not be checked
  explicitly.
- Within a multi-part problem, the result of an earlier part may be assumed even if it was not
  itself proved.
- Parts marked with a star (*) are the ones expected to be hardest; they carry no extra points, so
  they are not necessarily worth more time than the unstarred parts.
- Answers should be neat and the reasoning justified — the exam states it is primarily testing
  understanding of concepts, not just final answers.

## Exercises

### 1. Six Gaussians (20 points, 5 points per part)

*Useful fact:* the density of $Z \sim N(\theta, \sigma^2)$ is
$$\frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{ -\frac{(x - \theta)^2}{2\sigma^2} \right\}.$$

Suppose we observe independent Gaussians $X_1, \ldots, X_6$ with $X_i \sim N(\theta_i, \sigma^2)$.
Different parts assume $\sigma^2 > 0$ known or unknown.

(a) Assume $\sigma^2 = 1$ is known. Suppose we want to test
$$H_0 : \theta_2 = \theta_3 \text{ and } \theta_4 = \theta_5 = \theta_6,$$
against the alternative that $\theta$ is any other vector in $\mathbb{R}^6$. Suggest a $\chi^2$ test
statistic and specify its degrees of freedom.

(b) Continue to assume $\sigma^2 = 1$, and consider the estimator
$$\delta(X) = \gamma \cdot \big( X_1,\ \overline{X}_{23},\ \overline{X}_{23},\ \overline{X}_{456},\ \overline{X}_{456},\ \overline{X}_{456} \big),$$
where $\gamma \in [0,1]$ is a fixed constant, $\overline{X}_{23} = \frac{X_2+X_3}{2}$, and
$\overline{X}_{456} = \frac{X_4+X_5+X_6}{3}$. Give an unbiased estimator of the MSE of $\delta(X)$.

(c) Now assume $\sigma^2$ is unknown, but it is known that $\theta_2 = \theta_3$ and
$\theta_4 = \theta_5 = \theta_6$ — that is, what was a null hypothesis to test in part (a) is now a
modeling assumption. Suggest a confidence interval, based on Student's $t$-distribution, for
$g(\theta) = \theta_4 - \theta_3$. Specify its degrees of freedom.

(d) Under the same assumptions as part (c), suppose we want to test
$H_0 : \theta_1 = \theta_2 = \cdots = \theta_6$ against the alternative that $\theta$ is any other
vector in $\mathbb{R}^6$ satisfying $\theta_2 = \theta_3$ and $\theta_4 = \theta_5 = \theta_6$.
Suggest an $F$ test statistic and specify its degrees of freedom.

### 2. Inverse gamma prior (20 points, 5 points per part)

*Useful facts:*

- A $\chi^2_d$ random variable has mean $d$ and variance $2d$.
- If $Y$ is a $\mathrm{Gamma}(\alpha,\beta)$ random variable (rate parametrization) it has density
  $$\frac{\beta^\alpha}{\Gamma(\alpha)} y^{\alpha-1} \exp\{-\beta y\}$$
  on $(0,\infty)$, with mean $\alpha/\beta$ and variance $\alpha/\beta^2$, defined for
  $\alpha,\beta>0$.
- The inverse-gamma distribution $\mathrm{IG}(\alpha,\beta)$ is the law of $W = 1/Y$ for
  $Y \sim \mathrm{Gamma}(\alpha,\beta)$: $W \in (0,\infty)$ has density
  $$\frac{\beta^\alpha}{\Gamma(\alpha)} w^{-\alpha-1} \exp\{-\beta/w\}.$$
  Here $\beta$ is a scale parameter; $W$ has mean $\frac{\beta}{\alpha-1}$ for $\alpha>1$ and
  variance $\frac{\beta^2}{(\alpha-1)^2(\alpha-2)}$ for $\alpha>2$, again defined for
  $\alpha,\beta>0$.
- The squared relative error loss is
  $$L_{\mathrm{rel}}(d,\theta) = \left(\frac{d-\theta}{\theta}\right)^2 = \left(\frac{d}{\theta}-1\right)^2,$$
  with risk $R_{\mathrm{rel}}(\delta(\cdot),\theta) = \mathbb{E}_\theta[L_{\mathrm{rel}}(\delta(X),\theta)]$.

The problem statement opens: "Consider the Bayesian model with $\theta \sim \ldots$" — and the
supplied source breaks off there in every copy available (see Sources). Neither the rest of the
model, nor parts (a) through (e), were recoverable from the material handed to this chapter, so
they are not reproduced here.

## Sources

- All three supplied notes are the same document, mirrored across three later course offerings'
  `old-exams/` folders: the Fall 2024 final examination for Berkeley Stat 210A, Prof. Will Fithian —
  [`fall-2024/old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2024.pdf),
  [`fall-2025/old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf),
  and
  [`fall-2026/old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2024.pdf).
  All three are machine reconstructions of a PDF with no text layer, and the source markdown flags
  every equation as unverified, so the statements above should be checked against the original PDF
  before being treated as exact.
- All three mirrors of Problem 2 end at the identical point, mid-sentence, immediately after the
  "useful facts" and the opening words of the Bayesian model — the question booklet evidently
  continues past this in the original PDF, but nothing past this point was supplied to this
  chapter. For reference, the same course's Fall 2018 final (this library's chapter 11, Problem 3,
  "Inverse gamma prior") opens with an almost verbatim-identical list of useful facts and problem
  title, but its Bayesian model and parts should not be assumed to carry over — they are a
  different exam and are recorded separately.
- No slides, transcript, or separate problem set were supplied for this chapter, and the source's
  "answers continued" pages were blank in the original, so no solutions are recorded anywhere in
  the source material.
- The exam's own reference facts (the Gaussian density, and the $\chi^2$/gamma/inverse-gamma facts
  and the relative-error loss definition for Problem 2) are reproduced above exactly as printed on
  the exam, since the exam supplies them for use without proof.

---

[← 13. Final Exam Review Problems](13-final-exam-review-problems.md) · [Contents](index.md) · [16. Hierarchical Bayes →](16-hierarchical-bayes.md)
