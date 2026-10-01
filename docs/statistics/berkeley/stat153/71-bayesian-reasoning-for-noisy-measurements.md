---
title: "71. Bayesian Reasoning for Noisy Measurements"
course: "Berkeley Stat 153"
chapter: 71
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 71. Bayesian Reasoning for Noisy Measurements

## What this covers

This chapter answers a single question: if you observe a noisy equation for an unknown number,
what, precisely, can you say about that number? It works the question as a small Bayesian
calculation — first for one noisy equation, then for two — and the point of doing so is to set up
the reasoning that later justifies fitting a line (or a constant) to data by least squares. It
assumes Bayes' rule, and the normal and uniform densities.

## A single noisy equation

Start with two versions of the same puzzle.

**Simple question 1.** You have two numbers $a$ and $b$, and you are told $a + b = 7$. What can you
say about $a$? Nothing specific — $a$ could be anything, with $b$ making up the difference.

**Simple question 2.** Same setup, but now you are also told $b$ is small in magnitude. Intuitively,
$a$ should be close to $7$, since $a = 7 - b \approx 7$. The rest of this section makes that
intuition precise.

To formalize "$b$ is small," treat $a$ and $b$ as independent random variables:

$$a \sim \text{Unif}(-C, C) \quad \text{for a very large } C, \qquad b \sim N(0, \sigma^2), \quad
\sigma^2 = 0.5.$$

The uniform prior on a huge interval $(-C, C)$ is a way of saying "no information about $a$ before
seeing the data" — it is flat over any range of values that will actually matter. The normal prior
on $b$ with small $\sigma^2$ is what encodes "$b$ is small in magnitude."

Write $y = a + b$, so that $y \mid a \sim N(a, \sigma^2)$, and ask for the distribution of $a$ given
that $y = 7$ was observed. By Bayes' rule,

$$
\begin{aligned}
f_{a \mid y = 7}(a) &= \frac{f_{y \mid a}(7)\, f_a(a)}{f_y(7)} \\
&\propto f_{y \mid a}(7)\, f_a(a) \\
&= \frac{1}{\sqrt{2\pi}\,\sigma} \exp\left\{-\frac{(a - y)^2}{2\sigma^2}\right\}
   \cdot \frac{I\{-C < a < C\}}{2C} \\
&\propto \frac{1}{\sigma} \exp\left(-\frac{(a - 7)^2}{2\sigma^2}\right).
\end{aligned}
$$

The second line drops $f_y(7)$ because it does not depend on $a$. In the third line, $\frac{1}{2C}$
is a constant and the indicator does not bind — $C$ is so large that it never excludes the values of
$a$ the exponential actually favors. What survives is exactly the shape of a normal density in $a$,
centered at the observed value $7$:

$$a \mid a + b = 7 \;\sim\; N(7, \sigma^2).$$

This is the payoff: the naive answer to Simple Question 2 — "$a$ is about $7$" — turns out to be
exactly right once the vague word "small" is turned into a normal prior for $b$ and "no prior
information" is turned into a flat prior for $a$. The posterior mean of $a$ is the observed value,
and the posterior spread is exactly the noise variance $\sigma^2$: the less you trust the
measurement, the wider your remaining uncertainty about $a$.

## Two noisy equations for the same unknown

**Question 3.** Now suppose there is a single unknown $a$, but it is measured twice, each time with
its own noise term:

$$a + b_1 = 7, \qquad a + b_2 = 10.$$

The two readings disagree — $7$ against $10$ — so whatever value $a$ takes, the noise has to absorb
some of that discrepancy. This is one step closer to the regression setting: one parameter, several
noisy equations constraining it, and no reason to expect them to agree exactly.

As before, assume independence and put flat priors where there is no prior information:

$$a \sim \text{Unif}(-C, C), \qquad b_1, b_2 \sim N(0, \sigma^2), \qquad \log \sigma \sim
\text{Unif}(-C, C).$$

The new ingredient is that $\sigma$ — how noisy the measurements are — is no longer assumed known.
It gets the same "no information" treatment as $a$ did, except applied to $\log \sigma$ rather than
$\sigma$ itself, since $\sigma$ has to stay positive. Writing $y_1 = a + b_1$ and $y_2 = a + b_2$,
the object of interest is now the *joint* posterior

$$a, \sigma \mid y_1, y_2,$$

built from the joint density $f_{a, \sigma \mid y_1, y_2}$ by the same Bayes'-rule argument as
before. The lecture notes break off at exactly this point, mid-formula, before the posterior is
worked out — so the completed calculation for Question 3 is not part of this chapter. What the setup
already shows is the shape of the argument that later justifies fitting a regression line: an
unknown quantity, several noisy linear equations relating it to observed values, and a noise model
whose spread is itself estimated rather than assumed.

## Sources

- Berkeley Stat 153, Fall 2026, Lecture Three (Sept 3), "Linear Regression Math": all of Simple
  Questions 1–2, their Bayesian solution, and the Question 3 setup are from
  `docs/statistics/berkeley/stat153/fall-2026/HandwrittenNotesLectureThree153248Fall2026.md` in the
  library repository — a model's reconstruction of a handwritten-notes PDF with no text layer
  (CC BY 4.0). That file's own banner flags every equation in it as unverified, since it was read
  off scanned handwriting rather than transcribed from typeset source; the equations above are
  reproduced as given there.
- No slide deck or lecture transcript was supplied for this session, and no exercises were supplied.
- The source notes end mid-derivation, in the middle of writing out the joint density
  $f_{a,\sigma\mid y_1,y_2}$ for Question 3 — the resolution of that question (the joint posterior,
  and whatever the lecture drew from it about fitting $a$) is not present in the material and is
  not reconstructed here.

---

[← 70. Bayesian Shrinkage and Variance Models](70-bayesian-shrinkage-and-variance-models.md) · [Contents](index.md) · [72. Ridge Regression as Bayesian Inference →](72-ridge-regression-as-bayesian-inference.md)
