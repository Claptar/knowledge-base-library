---
title: "5. Instrumental Variables and Noncompliance"
course: "Berkeley Stat 156 Fall 2024"
chapter: 5
source: "https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf"
licence: "CC BY-NC 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 156 Fall 2024](https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf), licensed CC BY-NC 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Instrumental Variables and Noncompliance

## What this covers

This chapter works through the identification arguments behind Homework 5 of Stat 156: recovering
a causal effect of treatment from data on an instrument $Z$, actual treatment taken $D$, and an
outcome $Y$, when not everyone assigned to treatment actually takes it up. It assumes the
potential-outcomes framework and the vocabulary of Relevance, Exclusion Restriction and
Exchangeability from earlier in the course — those are used here but not re-derived, since the
lecture that introduced them is not part of the material supplied for this chapter. What follows is
the setup the homework's ten problems ask you to work with; the problems themselves, not their
solutions, are the point.

## The noncompliance problem

Write $Z \in \{0, 1\}$ for the instrument — an assignment, encouragement, or eligibility signal —
and $D \in \{0, 1\}$ for whether treatment is actually taken. $D$ need not equal $Z$: someone
assigned $Z = 1$ can decline treatment. **One-sided noncompliance** is the restriction that
deviation only runs one way: $Z = 0$ implies $D = 0$. Nobody gets treated without being assigned to
be; the only slack is that some of the assigned do not take it up.

Potential outcomes carry both arguments before anything is observed: $D(z)$ is the treatment a unit
would take under assignment $z$, and $Y(z, d)$ is the outcome under assignment $z$ and treatment
$d$. The three assumptions from the course, restated as they appear in the homework:

- **Relevance.** $Z$ is associated with $D$ — in the classical linear case, $\operatorname{cov}(D, Z) \neq 0$.
- **Exclusion restriction.** $Y(Z = z, D = d) = Y(D = d)$: the instrument affects the outcome only
  through the treatment it induces, never directly.
- **Exchangeable IV.** $Z \perp\!\!\!\perp \big(D(Z = z), Y(Z = z)\big)$: the instrument is
  independent of the potential values of treatment and outcome, exactly as if it had been assigned
  at random, whether or not it actually was.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Causal diagram for an instrument Z acting on outcome Y only through treatment D, with an unobserved factor U driving both D and Y">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="55" y1="150" x2="150" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="175" y1="150" x2="270" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="150" y1="60" x2="70" y2="138" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="175" y1="60" x2="260" y2="138" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <circle cx="40" cy="150" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="160" cy="150" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="280" cy="150" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="160" cy="45" r="16" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="40" y="154" text-anchor="middle" font-size="12" fill="currentColor">Z</text>
  <text x="160" y="154" text-anchor="middle" font-size="12" fill="currentColor">D</text>
  <text x="280" y="154" text-anchor="middle" font-size="12" fill="currentColor">Y</text>
  <text x="160" y="49" text-anchor="middle" font-size="12" fill="currentColor">U</text>
  <text x="100" y="140" text-anchor="middle" font-size="11" fill="currentColor">relevance</text>
  <text x="160" y="185" text-anchor="middle" font-size="11" fill="currentColor">no direct arrow: exclusion restriction</text>
</svg>
<figcaption>The instrument moves the outcome only by moving the treatment (no arrow straight from
Z to Y), and nothing feeds into Z itself (no arrow into Z from the unobserved U driving both D and
Y) — that second absence is what exchangeability buys.</figcaption>
</figure>

## Two identification targets under one-sided noncompliance

Problem 1 asks for two causal contrasts, each written purely in terms of quantities you could
estimate from data — no potential outcomes on the right-hand side. The effect of removing
treatment on the whole population:
$$E[Y - Y(D = 0)] = E[Y] - E[Y \mid Z = 0]$$
and the effect of removing treatment on the treated:
$$E[Y - Y(D = 0) \mid D = 1] = \frac{E[Y] - E[Y \mid Z = 0]}{\mathbb{P}(D = 1)}.$$
Both hold under Relevance, Exclusion Restriction, Exchangeability, and one-sided noncompliance. The
lever in both proofs is the same: one-sided noncompliance forces everyone observed at $Z = 0$ to
also have $D = 0$, so their observed outcome already *is* $Y(D=0)$; exchangeability then lets you
drop the conditioning on $Z = 0$ to get an unconditional statement about $Y(D=0)$. Working out
exactly how that step goes, and how the second identity follows from the first by conditioning on
$D = 1$, is Exercise 1 below.

## The structural-equations picture and the two-stage model

Problem 2 gives the same setup a linear, structural-equation form. At the level of potential
outcomes:
$$D(Z = z) = \alpha_0 + \alpha_1 z + \nu, \qquad Y(Z = z, D = d) = \beta_0 + \beta_1 d + \epsilon.$$
These are statements about what *would* happen under a hypothetical assignment $z$. What is actually
fit to data is the corresponding equation in the *observed* $Z$ and $D$:
$$D = \alpha_0 + \alpha_1 Z + \nu, \qquad Y = \beta_0 + \beta_1 D + \epsilon.$$
The first equation is the **first stage** — regress the treatment taken on the instrument. The
second is the **second stage** — regress the outcome on the treatment. Moving from the
potential-outcome model to this observed-data model, under Relevance, Exclusion Restriction and
Exchangeable IV, is supposed to also hand you three more familiar-looking conditions on the
observed-data equations:

(a) **Relevance:** $\operatorname{cov}(D, Z) \neq 0$
(b) **Exclusion restriction:** $Z$ does not appear in the second-stage equation for $Y$
(c) **Exchangeable IV:** $\operatorname{cov}(Z, \nu) = \operatorname{cov}(Z, \epsilon) = 0$

Showing that the potential-outcome assumptions really do collapse to exactly these three, once $z$
is set to the realized $Z$, is Exercise 2.

## The Wald estimator and two-stage least squares

Problems 3 and 4 are about two other ways of writing the same coefficient $\beta_1$. The first is a
ratio of observable differences — the classical **Wald estimator** for a binary instrument — set
equal to a ratio of covariances:
$$\frac{E[Y \mid Z = 1] - E[Y \mid Z = 0]}{E[D \mid Z = 1] - E[D \mid Z = 0]} = \frac{\operatorname{cov}(Y, Z)}{\operatorname{cov}(D, Z)}.$$
The left side is what you would compute directly by comparing the two instrument arms; the right
side is the same quantity in covariance form, which is the form that generalizes once $Z$ is not
just binary. Their equality is Exercise 3.

The second rewrites $\beta_1$ yet again: it is also the coefficient from a population regression of
$Y$ on the *fitted values* from a population regression of $D$ on $Z$. That two-step recipe —
regress $D$ on $Z$, keep only the predicted $D$, then regress $Y$ on the prediction — is exactly
**two-stage least squares (2SLS)**. The predicted $D$ keeps only the part of the treatment variation
driven by the instrument and discards the part correlated with the second-stage error $\epsilon$,
which is what makes the second regression identify $\beta_1$ rather than something confounded.
Proving that this 2SLS coefficient equals $\beta_1$ under $\operatorname{cov}(D, Z) \neq 0$ and
$\operatorname{cov}(Z, \nu) = \operatorname{cov}(Z, \epsilon) = 0$ is Exercise 4.

## Exercises

Due 2024-11-12, 11:59pm PT. (Submit code for any coding parts, and assign Gradescope pages to the
matching problem — the assignment notes that points are deducted otherwise.)

1. Under Relevance, Exclusion Restriction, Exchangeability, and one-sided noncompliance ($Z = 0$
   implies $D = 0$), prove
   $$E[Y - Y(D = 0)] = E[Y] - E[Y \mid Z = 0]$$
   and
   $$E[Y - Y(D = 0) \mid D = 1] = \frac{E[Y] - E[Y \mid Z = 0]}{\mathbb{P}(D = 1)}.$$

2. Under the standard IV assumptions — relevance ($Z$ is associated with $D$), exclusion restriction
   ($Y(Z = z, D = d) = Y(D = d)$), and exchangeable IV
   ($Z \perp\!\!\!\perp (D(Z = z), Y(Z = z))$) — show that the structural equation model
   $$D(Z = z) = \alpha_0 + \alpha_1 z + \nu, \qquad Y(Z = z, D = d) = \beta_0 + \beta_1 d + \epsilon$$
   implies the observed two-stage model
   $$D = \alpha_0 + \alpha_1 Z + \nu, \qquad Y = \beta_0 + \beta_1 D + \epsilon$$
   together with the three classical IV assumptions: (a) $\operatorname{cov}(D, Z) \neq 0$;
   (b) $Z$ is not included in the second-stage $Y$ equation; (c)
   $\operatorname{cov}(Z, \nu) = \operatorname{cov}(Z, \epsilon) = 0$.

3. Prove
   $$\frac{E[Y \mid Z = 1] - E[Y \mid Z = 0]}{E[D \mid Z = 1] - E[D \mid Z = 0]} = \frac{\operatorname{cov}(Y, Z)}{\operatorname{cov}(D, Z)}.$$

4. Assume a classical two-stage IV model with $\operatorname{cov}(D, Z) \neq 0$ and
   $\operatorname{cov}(Z, \nu) = \operatorname{cov}(Z, \epsilon) = 0$. Show that $\beta_1$ equals the
   coefficient from a population regression of $Y$ on the predicted value from a population
   regression of $D$ on $Z$.

5. Problem 20.2 from *A First Course in Causal Inference*.

6. Problem 21.7 from *A First Course in Causal Inference*.

7. Problem 17.4 from *A First Course in Causal Inference*.

8. Problem 17.6 from *A First Course in Causal Inference*.

9. Problem 18.1 from *A First Course in Causal Inference*.

10. Problem 18.2 from *A First Course in Causal Inference*.

## Sources

Everything above is drawn from a single source: `HW5.md` (Stat 156, Berkeley, Fall 2024), converted
from `HW5.pdf`. That conversion is itself a model's reconstruction of a PDF with no extractable text
layer, so its equations are marked unverified at the source and are reproduced here as given, not
independently re-checked. No slide deck or lecture transcript was supplied for this chapter — the
homework's own phrasing ("recall from lecture," "in lecture we presented") points to a lecture on
instrumental variables and noncompliance that this chapter does not have access to, so the
exposition above states only the definitions and claims the homework itself states, and stops short
of the proofs, which are exactly what the ten problems ask for. Problems 5–10 point to *A First
Course in Causal Inference*, a textbook not included in the supplied material; their statements are
not reproduced here for that reason.

---

[← 4. Confounding, Backdoor Paths, M-Bias](04-confounding-backdoor-paths-m-bias.md) · [Contents](index.md) · [7. Course Reading Guide →](07-course-reading-guide.md)
