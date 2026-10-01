---
title: "20. Statistics as Inductive Reasoning"
course: "Berkeley Stat 210A"
chapter: 20
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. Statistics as Inductive Reasoning

## What this covers

Before any statistical method can be judged, a prior question has to be settled: what kind of
reasoning is statistics, and why is it inherently risky in a way that a proof is not? This chapter
lays out the scope of Stat 210A, distinguishes deductive from inductive reasoning, states Hume's
problem of induction, and shows the two ways statistics evades that problem — Bayesian updating and
frequentist "inductive behavior" — worked out on one real data set: a large experiment on whether
flipped coins are really fair. It assumes only a first course in probability: the binomial
distribution, expectation, and the idea of a parameter.

## What the theory of statistics is about

Statistics is the study of methods that use data to understand the world. Statistical methods are
used throughout the natural and social sciences, in machine learning and artificial intelligence,
and in engineering — and despite this ubiquity, practitioners are perpetually accused of not
actually understanding what they are doing. Statistical theory is, broadly, the attempt to
understand what we are doing when we use statistical methods.

Most (not all) statistical methods rest on **statistical modeling**: treating the data as a
realization of some **random** data-generating process with attributes, usually called
**parameters**, that are *a priori* unknown. The **analyst**'s job is to use the data to draw
accurate inferences about these parameters, or to make accurate predictions about future data. If
the modeling has been done well — a very big "if" — the unknown parameters correspond to whatever
real-world question motivated the analysis in the first place. Applied courses such as Stat 215A/B
ask whether the modeling exercise actually captures something real about the world; this course
instead asks how the analyst can use the data most effectively *within* the mathematical setup
once it is fixed. The topics are the structure of statistical models, how to evaluate and design
statistical methods, the Bayesian vs. frequentist philosophies, and estimation, confidence
intervals, and hypothesis testing — in parametric and nonparametric settings, in finite samples and
in asymptotic regimes.

Stat 210A sits among several related Berkeley courses. It focuses on *classical* statistical
contexts — inference in finite samples, or in fixed-dimensional asymptotic regimes. Stat 210B
(for which this course is a prerequisite) is more technical and covers empirical process theory and
high-dimensional statistics. Statistical Learning Theory (CS 281A / Stat 241A) overlaps somewhat but
tilts toward machine learning: more time on predictive modeling, optimization, and signal
processing, less on inferential questions such as testing, confidence intervals, and causal
inference. Both courses cover estimation and exponential families.

## Deductive reasoning

Most mathematics courses are entirely concerned with **deductive reasoning**: drawing conclusions
that follow logically from premises. For example:

1. All real, symmetric matrices have real eigenvalues.
2. $A$ is a real, symmetric matrix.
3. *Therefore*, $A$ has real eigenvalues.

Deductive reasoning shows up in everyday life too:

1. No one in my daughter's preschool class has a nut allergy.
2. Zoe is in my daughter's preschool class.
3. *Therefore*, Zoe is not allergic to peanuts.

This kind of argument is *risk-free*: as long as the premises are true, the conclusion must hold.
The premises could of course be false — I might be confusing my neighbor Zoe with a different Zoe
in the class — but that is the *only* way the conclusion could fail.

Deductive arguments can also involve statements about probability:

1. This die has six faces labeled 1 through 6.
2. If I roll it, it is equally likely to land on any face.
3. *Therefore*, the chance of rolling a 4 is exactly $1/6$.

A probability course such as Stat 205A is, in this sense, about deductive arguments like this one:
given a fully specified probabilistic premise, it derives further probabilistic facts with
certainty.

## Inductive reasoning

Statistics, by contrast, is the mathematical science of **inductive reasoning**: reasoning from
observations to general claims about the world. Unlike deduction, such arguments are inherently
*risky* — the conclusion can be false even when every premise is true.

(A terminological trap: **inductive proofs** in mathematics are not inductive reasoning in this
sense. An inductive proof is really an example of *deductive* reasoning, because the inductive step
is a logically valid argument that extends the conclusion to the whole class of objects under
study. Nothing about it is risky.)

A first example:

1. I ate a blueberry from the free sample tray at the supermarket.
2. It was ripe and delicious.
3. *Therefore*, if I buy a carton of blueberries, they will *probably* be ripe and delicious.

The weasel word "probably" is not a rigorous quantitative claim here — it just flags some
uncertainty about the conclusion. The argument is more persuasive if the sample is drawn from the
carton actually being bought:

1. I ate five blueberries at random from the carton I intended to buy.
2. They were all ripe and delicious.
3. *Therefore*, if I buy the carton, the rest of the blueberries will *probably* be ripe and
   delicious.

We could still be wrong — maybe there were only five good blueberries in the whole carton, and
those are exactly the ones we picked — but that is not very likely. Scientists reason inductively
all the time:

1. Water at 1 atm of pressure has been observed to boil at 100°C every time it has been measured in
   the laboratory.
2. *Therefore*, water at 1 atm of pressure *probably* always boils at 100°C.

Inductive reasoning is the basis of all the empirical sciences. It also applies directly to
probability itself:

1. I flipped this penny 1000 times and got 502 heads.
2. *Therefore*, it *probably* has about a 50% chance of landing heads.

For now we can take for granted what it means for a penny to have a 50% chance of landing heads —
something like, its physical properties give it an equal chance of heads or tails (and a negligible
chance of landing on its side or flying off into space). There is real controversy among
philosophers and statisticians about what probability means in general, though not much of it
attaches to ordinary coin flips; this is a thread the course picks up later.

## Hume's problem of induction

Inductive reasoning is not *valid* in the sense logicians or mathematicians mean by the word. It
doesn't matter how many real symmetric matrices you've seen with real eigenvalues — without a
proof, you cannot make the general claim. Mathematics has entertaining examples of patterns that
hold for a long stretch and then break, such as the
[Borwein integral](https://en.wikipedia.org/wiki/Borwein_integral):

$$
\begin{aligned}
\int_0^\infty \frac{\sin x}{x}\,dx &= \frac{\pi}{2} \\[4pt]
\int_0^\infty \frac{\sin x}{x}\cdot\frac{\sin(x/3)}{x/3}\,dx &= \frac{\pi}{2} \\[4pt]
\int_0^\infty \frac{\sin x}{x}\cdot\frac{\sin(x/3)}{x/3}\cdot\frac{\sin(x/5)}{x/5}\,dx &= \frac{\pi}{2} \\[4pt]
&\ \ \vdots \\[4pt]
\int_0^\infty \frac{\sin x}{x}\cdot\frac{\sin(x/3)}{x/3}\cdots\frac{\sin(x/13)}{x/13}\,dx &= \frac{\pi}{2} \\[4pt]
\int_0^\infty \frac{\sin x}{x}\cdot\frac{\sin(x/3)}{x/3}\cdots\frac{\sin(x/15)}{x/15}\,dx &= \frac{\pi}{2} - 2.31 \times 10^{-11}
\end{aligned}
$$

Each integral in this family equals $\pi/2$ exactly — until the pattern silently fails at the last
one. Bertrand Russell made the same point about induction in ordinary life:

> Domestic animals expect food when they see the person who usually feeds them. We know that all
> these rather crude expectations of uniformity are liable to be misleading. The man who has fed
> the chicken every day throughout its life at last wrings its neck instead, showing that more
> refined views as to the uniformity of nature would have been useful to the chicken.

David Hume's *A Treatise of Human Nature* (1739) first posed the **problem of induction**: that
inductive reasoning presumes — seemingly without justification — that yet-to-be-observed cases will
resemble observed ones. This presumption is the **uniformity principle**, and it is hard to see how
to justify it. It cannot be justified by a direct logical argument, since it is not logically valid.
It might seem justifiable by past experience — physical properties of the world do generally seem
uniform across space and time, at a low enough level — but that argument is circular: the future
having resembled the past in the past does not entail that it will resemble the past in the future.

Hume conceded that people have to reason inductively all the time, but he called this a "custom" or
"habit" and challenged philosophers to justify it. Almost 300 years later there is still no fully
satisfactory answer. Most philosophers of science — Karl Popper among them — accept that inductive
reasoning is fallible but hold that there are reasonable ways for scientists to deal with that.

## Two evasions of the problem of induction

Building a *mathematical* science of inductive reasoning looks like trouble from the start: the
first thing known about induction is that it is not mathematically valid. Statisticians have two
main ways of evading this, and they generate the two main frameworks for statistical inference.

**Evasion 1 — Bayesian reasoning.** Whatever our *a priori* beliefs about the world are, we at
least know how to update them in light of experience, using the mathematics of conditional
probability. The prior beliefs themselves may never be justified, but there is (more or less) only
one rational way to update them. With enough experience, we may hope these beliefs "wash out," so
that observers who started with different priors eventually converge.

**Evasion 2 — inductive behavior (frequentist statistics).** Instead of justifying the reasoning
itself, design methods whose *fallibility can be quantified*. As long as certain assumptions hold
about how the data were collected, it may be possible to prove that a method gives correct
conclusions with high probability — without ever certifying that any particular conclusion is
correct.

## Worked example: are coins really fair?

Physical randomizers like coins and dice seem like the firmest possible ground for a theory of
probability. Recent work says otherwise: most human flippers have a somewhat greater than 50%
chance of seeing a coin land on the *same side it started on*, apparently due to the physics of a
rotating object. This was first hypothesized in a theoretical paper by Diaconis, Holmes, and
Montgomery (2007), and confirmed in a large experiment by Bartos et al. (2023), in which 48 human
flippers collectively flipped $n = 350{,}757$ coins, of which $178{,}079$ ($50.77\%$) landed on the
same side they started.

Bartos et al. actually collected far more than this one number: each of the 48 flippers recorded
the full sequence of their flips, the type of coin (46 countries' worth of coins were used), and
even video of themselves flipping. The analysis below, though, uses only the summary statistic
$X = 178{,}079$, the number of flips landing same-side-up.

### Frequentist analysis in the binomial model

The data are easy to analyze under two seemingly innocuous assumptions: the flips are statistically
independent, and every flip has the same probability $\theta$ of landing on the side it started.
Under these assumptions it follows deductively that the probability of exactly $x$ same-side
landings out of $n$ flips is

$$
\binom{n}{x}\theta^x(1-\theta)^{n-x}, \qquad x = 0, 1, \dots, n.
$$

This is the one-parameter **binomial model**, written $X \sim \mathrm{Binom}(n, \theta)$. If
Diaconis–Holmes–Montgomery's prediction is right, $\theta > 0.5$; if the starting side makes no
difference, $\theta = 0.5$.

The frequentist **estimator** of $\theta$ is $\hat\theta = X/n$, here $0.5077$. One thing this
course will prove is that $X/n$ is the best estimator of $\theta$ among all **unbiased**
estimators — those satisfying $\mathbb{E}_\theta\hat\theta = \theta$ for every possible value of
$\theta \in [0,1]$. This is an instance of inductive behavior: using $X/n$ guarantees getting the
answer right *on average*, as precisely as any unbiased estimator can. It is also possible to say
how variable the estimator is: its standard error is $\sqrt{\theta(1-\theta)/n}$. Substituting
$\hat\theta$ for $\theta$ gives a typical error of about $0.00084$, so there is good reason to
believe $\hat\theta = 0.5077$ is about that close to the truth — but not a guarantee for *this
particular* experiment; we could have gotten unlucky.

Can we conclude, *inductively*, that a same-side bias really exists ($\theta > 0.5$)? Even if
$\theta = 0.5$ exactly, $X/n$ would be expected to deviate somewhat from $0.5$ just by chance.
Frequentist analysis evades this question and substitutes another for it — testing the null
hypothesis $\theta = 0.5$ against the alternative $\theta > 0.5$, and reporting a confidence
interval for $\theta$:

```R
binom.test(x = 178079, n = 350757, p = 0.5, alternative = "greater")
```

```
    Exact binomial test

data:  178079 and 350757
number of successes = 178079, number of trials = 350757, p-value <
2.2e-16
alternative hypothesis: true probability of success is greater than 0.5
95 percent confidence interval:
 0.5063091 1.0000000
sample estimates:
probability of success
             0.5076991
```

The $p$-value is the likelihood of observing at least as many same-side flips as were seen, if
$\theta$ really were $0.5$. It is so small here ($p < 2.2 \times 10^{-16}$) that R does not bother
computing its exact value. The probability behind this calculation follows deductively from the
binomial assumptions, but most reasonable people would accept it as sufficient evidence to reject
the null hypothesis — to reach the *inductive* conclusion that $\theta \neq 0.5$. This conclusion is
risky: even a much more conservative threshold, say rejecting only when $p < 10^{-10}$, still leaves
some chance of error in any given experiment. What has been gained is that this chance can be
quantified and controlled, rather than eliminated.

Beyond detecting *that* a bias exists, `binom.test` also returns a $95\%$ **confidence interval**,
$[50.6\%, 50.9\%]$, for $\theta$. (Confidence intervals are developed properly later in the course;
for now, the interval is constructed so that it covers the true $\theta$ with probability at least
$95\%$, whatever value $\theta$ actually takes.) This is again inductive behavior: producing the
interval risks the conclusion "$\theta$ lies between $0.506$ and $0.509$" being wrong, but the
procedure is built so that risk can be quantified and limited in advance.

### Bayesian analysis

A more Bayesian route introduces an explicit distribution for $\theta$ itself — say,
$\theta \sim \mathrm{Unif}[0,1]$. This is a stronger assumption than anything made above: there is
only one draw from the distribution of $\theta$, observed only indirectly through the coin flips, so
it is hard to test. It turns out not to matter very much *which* prior is chosen here — many
different priors would lead to almost the same posterior.

Given this prior, the posterior distribution of $\theta$ after observing $X = x$ can be computed
directly:

$$
\theta \mid X = x \;\sim\; \frac{(n+1)!}{x!\,(n-x)!}\,\theta^x(1-\theta)^{n-x}, \qquad \theta \in [0,1].
$$

This is the **Beta distribution** with parameters $\alpha = x+1$, $\beta = n-x+1$ — a density for
the *parameter* $\theta$, not a distribution for the data $X$. Once the posterior is known, direct
probability statements about $\theta$ become available: for instance, after seeing the data, there
is only a $3.8 \times 10^{-20}$ chance that $\theta \le 0.5$. A $95\%$ Bayesian **credible
interval** — an interval containing $95\%$ of the posterior mass — comes out to $[50.6\%, 50.9\%]$,
coinciding with the frequentist confidence interval to several decimal places here. But the two
intervals mean different things: the credible interval claims, *in this experiment*, a $95\%$
chance that $\theta$ actually falls in that range, whereas the confidence interval only claims that
the *procedure* covers the true value at least $95\%$ of the time across repetitions.

### Questioning the binomial model

Bartos et al. themselves noted that the binomial model is not quite right — some flippers showed
more same-side bias than others. The model can be extended to give each flipper $i$ their own
probability $\theta_i$ over their $n_i$ flips (with $\sum_i n_i = n$); retaining independence gives
$X_i \sim \mathrm{Binom}(n_i, \theta_i)$ independently for $i = 1,\dots,48$.

There was also evidence that individual flippers improved over time. Accommodating that means
expanding further, to $X_{i,t} \sim \mathrm{Bernoulli}(\theta_{i,t})$ independently for
$i = 1,\dots,48$ and $t = 1,\dots,n_i$, perhaps with the monotonicity constraint
$\theta_{i,1} \ge \theta_{i,2} \ge \cdots \ge \theta_{i,n_i}$ for each $i$. With
$n = 350{,}757$ parameters — one per data point — this is effectively a **nonparametric** model.

## Questions the course returns to

This one example already previews several recurring questions.

- **Bayesian vs. frequentist frameworks.** What are the pros and cons of each? Where does a prior
  come from, and how much does the choice of prior matter to the analysis?
- **Sufficiency.** The first (binomial) analysis summarized the whole data set by the single number
  $X$, even though far more was recorded (the full sequence of flips for every flipper, in
  particular). It turns out that, under the binomial model, nothing is lost by reducing the data to
  $X$ alone. What is it about the structure of the binomial model that makes this reduction
  lossless?
- **Estimation.** What is a good way to estimate the parameters of each of these models? In the
  model with a separate $\theta_i$ per flipper, how should — or shouldn't — the estimate for one
  flipper be informed by data from the other 47? In the time-varying model, what functional form for
  $\theta_{i,t}$ would be reasonable, and how would it be estimated?
- **Testing.** In the basic binomial model, testing $H_0: \theta \le 0.5$ against
  $H_1: \theta > 0.5$ turns out to have a unique best solution: reject when $X$ is large. Testing
  whether the flippers really need different $\theta_i$'s — $H_0: \theta_1 = \cdots = \theta_{48}$
  against "not all equal" — is a harder problem, for two reasons: the null hypothesis has a
  *nuisance parameter* that can affect the null distribution of any test statistic, and the
  $48$-dimensional alternative can move away from the $1$-dimensional null in many different
  directions, some of which a given test will be much better at detecting than others.
- **Asymptotics.** Nothing in the actual computation ever evaluates $350{,}757!$, even though such
  quantities appear in the formulas. In practice the binomial model is replaced by an appropriate
  Normal approximation, $X \sim \mathcal{N}(n\theta, n\theta(1-\theta))$ — an immediate consequence
  of the central limit theorem here, but a technique that extends to many settings where the
  approximation is far less obvious in advance.

## Sources

This chapter merges the introduction to the Stat 210A course reader, which is offered under CC BY
4.0 and appears with essentially identical prose across three converted terms of the course. The
base text follows the fall-2024 and fall-2026 conversions (identical to each other, converted
losslessly from the underlying `.qmd` source):

- `berkeley-stat210a/fall-2024/reader/introduction/01-about-stat-210a.md`
- `berkeley-stat210a/fall-2024/reader/introduction/02-deductive-vs-inductive-reasoning.md`
- `berkeley-stat210a/fall-2024/reader/introduction/03-the-problem-of-induction.md`
- `berkeley-stat210a/fall-2024/reader/introduction/04-statistical-evasions-in-practice-coin-flipping.md`
  (and their fall-2026 duplicates).

The R console output shown under "Frequentist analysis in the binomial model" is reproduced from the
fall-2025 conversion of the same reader page (`berkeley-stat210a/fall-2025/reader/introduction/04-...`,
converted from rendered `.html` rather than raw `.qmd`), which captured the executed code-chunk
output that the plain `.qmd` source does not itself contain. The `fall-2025/units/reader/...` copies
supplied alongside these are duplicates of the fall-2025 reader files and were not used separately.
No slide deck or lecture transcript was supplied for this chapter — the course reader is the primary
source, and the display of the Borwein integral has been re-set from a source formatting artifact
(`[10pt]` spacing markers rendered as literal text) into a standard aligned display; the mathematical
content is unchanged.

---

[← 19. Course Overview and Schedule](19-course-overview-and-schedule.md) · [Contents](index.md) · [21. The James-Stein Estimator →](21-the-james-stein-estimator.md)
