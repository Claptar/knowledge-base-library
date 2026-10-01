---
title: "25. Induction and the Coin-Flip Example"
course: "Berkeley Stat 210A"
chapter: 25
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 25. Induction and the Coin-Flip Example

## What this covers

This chapter opens the course by asking what separates *deductive* reasoning, where true premises force
a true conclusion, from *inductive* reasoning, where a finite set of observations is used to support a
general claim that could turn out false. It assumes nothing beyond being able to read a probability
statement such as a binomial mass function. It ends by using a live dispute about whether a flipped coin
is fair to introduce, in miniature, every kind of question the course will spend the semester on:
Bayesian versus frequentist frameworks, sufficiency, estimation, testing, and asymptotics.

## Deduction: reasoning that cannot go wrong

**Deduction** is drawing inferences that follow logically from premises. If the premises are true and the
argument is valid, the conclusion is guaranteed true — the only way a deductive argument can mislead you
is if one of its premises was false to begin with. Two examples of the form:

- All real, symmetric matrices have real eigenvalues; $A$ is a symmetric matrix; therefore $A$ has real
  eigenvalues.
- No one in my daughter's preschool class has a peanut allergy; Zoe is in my daughter's preschool class;
  therefore Zoe is not allergic to peanuts.

Call this **risk-free**: valid argument plus true premises gives a true conclusion, full stop. Deduction
can also produce probability statements, when a probability appears among the premises: this die has six
faces $1, 2, \dots, 6$, each equally likely, therefore the chance of rolling a $4$ is $1/6$. The
probability here is deduced, not estimated — it follows from the assumptions about the die exactly as the
eigenvalue claim follows from the assumptions about $A$.

## Induction: reasoning that can go wrong

**Induction** moves from observations to a general claim, and it is **risky**: it can be, and sometimes
will be, wrong. Three examples:

- I ate a free sample strawberry at the supermarket and it was ripe and delicious; therefore I should
  (probably) buy a whole carton. (This would be more convincing if the sample had been drawn at random
  from the carton rather than handed to me by the store.)
- Water at $1\,\text{atm}$ pressure has always been observed to boil at $100^\circ\text{C}$; therefore all
  water at $1\,\text{atm}$ (probably) boils at $100^\circ\text{C}$.
- I flipped this coin $1000$ times and got $502$ heads; therefore it (probably) has about a $50\%$ chance
  of landing heads.

None of these arguments is deductively valid — in each case the conclusion goes beyond anything the
premises logically force. **Statistics** is defined, for the purposes of this course, as *the mathematical
science of inductive reasoning*: it is the discipline that tries to say precisely how risky an inductive
claim is, and how to make it as safe as possible.

## The problem of induction

Inductive reasoning is not logically valid, and this is not a fixable gap — it is a genuine philosophical
problem. **Hume's** observation is that every inductive argument implicitly presumes that unobserved cases
will resemble observed ones, and nothing forces that presumption to be true. So how could that presumption
ever be justified?

- Not by a logical proof — there is none.
- Not by appeal to the fact that induction has worked well in the past — that appeal is itself an
  inductive argument, so using it to justify induction is circular.

Hume conceded that we cannot help reasoning inductively regardless, and called the habit of doing so
"custom" or "habit" rather than something with a rational foundation.

Statistics does not solve Hume's problem — it evades it, and it does so in one of two ways, which are the
two frameworks the rest of the course keeps returning to:

1. **Bayesian reasoning.** Whatever your prior beliefs happen to be, there is a definite, consistent way
   to update them in light of new evidence. This does not justify the prior itself; it only guarantees
   that the *updating* is done correctly once a prior is granted.
2. **"Inductive behavior" (frequentist statistics).** If the observations come from a reasonable
   experiment, methods can be designed whose conclusions are correct with high probability — and this can
   be *proved*. The guarantee here attaches to the method's long-run behavior, not to the truth of any
   single conclusion it produces.

## Case study: is a flipped coin fair?

**Diaconis, Holmes, and Montgomery (2007)** built a physical model of a coin flip based on the coin's
precession while spinning in the air, and used it to predict that a coin is a bit more likely to land on
the same side it started on — about $51\%$ for a typical human flipper.

**Bartoš et al. (2023)** tested this at scale: $350{,}757$ coin flips, carried out by $48$ flippers using
coins from $46$ countries, of which $178{,}079$ landed on the same side they started on — about $50.8\%$,
consistent with the prediction.

### Two analyses of the same data

**Frequentist.** Model each flip as independent with the same probability $\theta$ of a same-side outcome,
so the count $X$ of same-side flips out of $n$ is Binomial:

$$\mathbb{P}_\theta(X = x) = \binom{n}{x}\theta^x(1-\theta)^{n-x}.$$

This produces a $95\%$ confidence interval $[50.6\%, 50.9\%]$ for $\theta$. What that $95\%$ means is a
statement about the *procedure*, fixed before any data are seen: however the true $\theta$ sits, the
construction guarantees

$$\mathbb{P}_\theta\big(\mathrm{CI}(X) \text{ covers } \theta\big) \ge 95\% \quad (\text{here, almost exactly } 95\%).$$

**Bayesian.** Same binomial likelihood, but now add a $\mathrm{Unif}[0,1]$ prior on $\theta$. This produces
a $95\%$ credible interval — numerically the same $[50.6\%, 50.9\%]$ in this case. The natural question to
raise about it: whose prior opinion was actually uniform on $[0,1]$?

### The model was wrong

Here is the twist: the pooled binomial model does not actually hold for this data set. Different flippers
had different personal values of $\theta$, and most flippers' values moved *closer to* $50\%$ as they
practiced over the course of the experiment. So both intervals above — the confidence interval and the
credible interval — were computed under an assumption the data itself violates.

## The questions this course is organized around

The coin-flipping example is used to introduce, in one setting, the whole vocabulary of the course.

**Frameworks.** What are the pros and cons of the Bayesian and frequentist approaches? Where does a prior
actually come from, and does that choice matter to the final answer? What does "probability" even mean
under each framework?

**Sufficiency.** Both analyses above threw away the order and identity of the $350{,}757$ individual flips
and summarized the whole data set as the single number $X = 178{,}079$. Did that summary lose anything? (It
did not, under the binomial model.) What is it about the structure of a model that licenses this kind of
compression?

**Estimation.** "What's a good way to estimate..." turns out to have several nested versions:

1. the overall $\theta$ in the pooled binomial model — there is no single estimator that is best for every
   possible $\theta$; $X/n$ is the "obvious" choice when $n$ is as large as $350{,}000$ (unless $\theta$
   itself happens to be tiny, e.g. $10^{-6}$), and a much less obvious question when $n$ is small, e.g.
   $n = 35$;
2. $\theta_i$ for an individual flipper $i$, under the finer model $X_i \overset{\text{ind.}}{\sim}
   \mathrm{Binom}(n_i,\theta_i)$ for $i = 1,\dots,m$ — how should data from the *other* flippers be used to
   help estimate flipper $i$'s own $\theta_i$?
3. how quickly $\theta_{i,t}$, a single flipper's bias, is changing between flip $1$ and flip $n_i$ — a
   variety of models, parametric and nonparametric, could describe this drift.

**Testing.** How do we efficiently test hypotheses like:

1. $H_0: \theta \le 50\%$ vs $H_1: \theta > 50\%$ (one-sided) — a uniquely best test exists;
2. $H_0: \theta = 50\%$ vs $H_1: \theta \ne 50\%$ (two-sided) — a natural choice exists;
3. $H_0: \theta_i = \theta$ for all flippers vs $H_1$: the $\theta_i$ vary — here the common value $\theta$,
   under the null, is a **nuisance parameter**: it affects the null distribution of any test statistic, and
   there are many different ways the $\theta_i$ could fail to be equal, and which of those you actually
   have in mind should affect which test you choose;
4. $H_0$: each flipper's $\theta_i$ is constant through their own sequence of flips vs $H_1: \theta_{i,t}$
   tends to be decreasing in $t$ — this one can be tested nonparametrically.

**Asymptotics.** No one calculated $350{,}757!$ to get an exact binomial probability. In practice, a count
this large is handled through a normal approximation,

$$X \sim N\big(n\theta,\, n\theta(1-\theta)\big) \quad \text{or, per flipper,} \quad X_i \overset{\text{ind.}}{\sim} N\big(n_i\theta_i,\, n_i\theta_i(1-\theta_i)\big),$$

and the course cares about when such approximations are good, and how to build comparable approximations
for the more complicated models that show up later.

## Sources

This chapter is drawn entirely from the model-reconstructed handwritten slides for STAT210A's first
lecture (no transcript or slide deck in the ordinary sense was supplied for this task):

- `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture01-intro/01-course-introduction.md` and
  `02-coin-flipping.md` (source PDF `handwritten/lecture01-intro.pdf`, berkeley-stat210a fall-2024,
  CC BY 4.0).
- The same two pages recur, with identical content, as
  `fall-2025/units/handwritten/lecture01-intro/01-course-introduction.md` / `02-coin-flipping.md`, and, in
  a second wording, as `fall-2025/handwritten/lecture01-intro/01-deductive-vs-inductive-reasoning.md` /
  `02-coin-flipping.md` and `fall-2026/handwritten/lecture01-intro/01-deductive-vs-inductive-reasoning.md`
  / `02-coin-flipping.md`. All four pairs cover the same lecture; only the file names and provenance
  metadata differ.

Both source pages are flagged `fidelity: reconstructed` — a model read PDF pages with no text layer, so
equations are unverified. The binomial mass function above is taken from the fall-2024 rendering,
$\theta^x(1-\theta)^{n-x}$; the fall-2025/fall-2026 rendering has $x^\theta(1-\theta)^{n-x}$ at the same
spot, which is evidently a transcription slip rather than a different formula.

The lecture's own outline lists "Syllabus" as its first item; no syllabus content appears in either
rendering of the notes, so none is reproduced here.

---

[← 24. Measures, Integrals, and Densities](24-measures-integrals-and-densities.md) · [Contents](index.md) · [26. Statistical Models and Decision Theory →](26-statistical-models-and-decision-theory.md)
