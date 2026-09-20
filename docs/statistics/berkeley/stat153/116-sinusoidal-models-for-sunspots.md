---
title: "116. Sinusoidal Models for Sunspots"
course: "Berkeley Stat 153 Fall 2024"
chapter: 116
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 116. Sinusoidal Models for Sunspots

## What this covers

This chapter covers the opening of Lecture 13 of STAT 153/248 (Spring 2025): a recap of the
sinusoidal regression models used earlier in the course to fit the annual sunspots series, which
the lecture uses as the motivating example before introducing a new, higher-dimensional model built
from many sinusoids at once. It assumes you already know ordinary linear regression and have seen a
sinusoid (or a small handful of sinusoids at unknown frequencies) fitted to a time series by
regression — as done earlier in the course, in Lecture 8, on the sunspots data. Only the recap
survives in the material supplied for this chapter; the new high-dimensional model itself, and its
stated connection to the high-dimensional regression models studied the week before, is not part of
what was converted and so is not covered below.

## The sunspots data and a single unknown frequency

The running example, used repeatedly earlier in the course, is the annual sunspots series $y_t$.
The simplest sinusoidal regression model fit to it is

$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad \epsilon_t \sim N(0, \sigma^2). \tag{1}$$

Here $\beta_0$ is a constant level, the pair $\beta_1, \beta_2$ multiplies a cosine and a sine at a
common frequency $f$, and $f$ itself is an unknown parameter — not fixed in advance, but part of
what is fit to the data, alongside the $\beta$'s and the noise variance $\sigma^2$.

## Adding more frequencies

The same idea extends by adding a second cosine–sine pair at a second unknown frequency $f_2$
(renaming the first frequency $f_1$):

$$y_t = \beta_0 + \beta_1 \cos(2\pi f_1 t) + \beta_2 \sin(2\pi f_1 t) + \beta_3 \cos(2\pi f_2 t) + \beta_4 \sin(2\pi f_2 t) + \epsilon_t, \tag{2}$$

and again by adding a third, at a further unknown frequency $f_3$:

$$y_t = \beta_0 + \beta_1 \cos(2\pi f_1 t) + \beta_2 \sin(2\pi f_1 t) + \beta_3 \cos(2\pi f_2 t) + \beta_4 \sin(2\pi f_2 t) + \beta_5 \cos(2\pi f_3 t) + \beta_6 \sin(2\pi f_3 t) + \epsilon_t. \tag{3}$$

In all three models $\epsilon_t \sim N(0, \sigma^2)$, and $f$ (model (1)) or $f_1, f_2, f_3$ (models
(2) and (3)) are unknown frequency parameters. Comparing the three equations, the pattern is that
each additional frequency contributes one more unknown frequency and one more cosine–sine pair of
coefficients to the mean function: model (1) has one frequency and two sinusoid coefficients, model
(2) has two frequencies and four coefficients, model (3) has three frequencies and six.

These models were used earlier in the course to understand particular features of the sunspots
series — the lecture recap says as much, and starts to say what happens when model (1) is fit to
the data, but the supplied material breaks off mid-sentence at exactly that point (see Sources).

## Where the recap is heading

The lecture's own framing, before the recap, is that having reviewed these fixed-number-of-frequency
models, it will go on to discuss "a high-dimensional model involving sinusoids," and that this model
connects to the high-dimensional regression models studied the previous week — while also being
"somewhat different" from them. Neither the new model nor the nature of that connection is present
in the material supplied for this chapter.

## Sources

Everything above comes from one file: `LectureThirteen153248Spring2025.md`, covering Lecture 13 of
STAT 153 & 248 ("Time Series"), Spring 2025, UC Berkeley, taught by Aditya Guntuboyina, dated March
5, 2025 — specifically its opening paragraph and the section "1 Recap: Sunspots Data." No slide
deck, transcript or problem set was supplied alongside it.

Two things the lecture points to that are not in the supplied material:

- **Lecture 8** of the same course, where models (1)–(3) were first fit to the sunspots data.
- **The high-dimensional sinusoidal model** that this lecture's introduction promises, and its
  connection to the high-dimensional regression models "studied last week" — the supplied file ends
  partway through the recap, mid-sentence, before either is introduced.

The source file itself is flagged in its own front matter as a model's reconstruction of a PDF with
no text layer (`fidelity: reconstructed`), so its prose is a paraphrase in places and its equations
are unverified against the original slides; it is a pointer into that PDF rather than a citable
transcription of it.

---

[← 115. High-Dimensional Regression and Regularization](115-high-dimensional-regression-and-regularization.md) · [Contents](index.md) · [117. Bayesian Priors and Least Squares →](117-bayesian-priors-and-least-squares.md)
