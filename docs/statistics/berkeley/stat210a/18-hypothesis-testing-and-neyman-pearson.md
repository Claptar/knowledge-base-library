---
title: "18. Hypothesis Testing and Neyman-Pearson"
course: "Berkeley Stat 210A Fall 2024"
chapter: 18
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. Hypothesis Testing and Neyman-Pearson

## What this covers

This chapter sets up the frequentist theory of hypothesis testing and proves its first optimality
result. It answers: how do you formalize a testing problem and a test, what does it mean for a test
to be "good," and — for the simplest possible problem, a single distribution against a single rival
distribution — which test is actually best? That last question is answered by the Neyman–Pearson
lemma, and the chapter then asks how far that answer extends when the alternative is not a single
point but a whole range of parameter values. It assumes familiarity with densities with respect to a
common dominating measure, one-parameter exponential families, and Lagrangian arguments for
constrained optimization.

## Setting up a testing problem

Start from a model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ — possibly "nonparametric," if $\theta$
is an infinite-dimensional object such as a density — and split the parameter space into two competing
claims about where $\theta$ actually lies:

- **Null hypothesis:** $H_0 : \theta \in \Theta_0$
- **Alternative hypothesis:** $H_1 : \theta \in \Theta_1$

The two pieces should be *disjoint* ($\Theta_0 \cap \Theta_1 = \emptyset$) and *exhaustive*
($\Theta_0 \cup \Theta_1 = \Theta$). Often only $\Theta_0$ is stated explicitly, and $\Theta_1$ is
understood to be everything else, $\Theta \setminus \Theta_0$.

Two examples worth keeping in mind throughout:

**Example ($Z$-test).** We observe $Z \sim N(\theta, 1)$ — commonly a summary statistic $Z(X)$
computed from a larger data set — and want to say something about $\theta$. The two standard versions
are the *one-sided* problem $H_0: \theta \le \theta_0$ vs. $H_1: \theta > \theta_0$, and the *two-sided*
problem $H_0: \theta = \theta_0$ vs. $H_1: \theta \ne \theta_0$.

**Example (two-sample nonparametric test).** We observe two independent samples,
$X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} P$ and $Y_1, \dots, Y_m \stackrel{\text{i.i.d.}}{\sim} Q$,
and want to test $H_0: P = Q$ against $H_1: P \ne Q$, without assuming anything further about $P$ and
$Q$.

A hypothesis is **simple** if it pins down the data distribution completely, and **composite**
otherwise. Of the hypotheses above, only the point null $H_0: \theta = \theta_0$ is simple; the rest
are composite.

### Why this needs a decision procedure at all

We would like the data $X \sim P_\theta$ to tell us which hypothesis is true, but pure deduction
usually cannot do this: if every $P_\theta$ has the same support, then *any* data set is logically
consistent with *every* value of $\theta$. Something has to be added beyond the data itself.

There are two standard ways around this. The Bayesian route is to beg the question: put a prior on
$\theta$ and report the posterior probabilities $\Lambda(\Theta_0 \mid X) = \mathbb{P}(\theta \in
\Theta_0 \mid X)$ and $\Lambda(\Theta_1 \mid X) = \mathbb{P}(\theta \in \Theta_1 \mid X)$. This is
clean, but in many applied settings it is regarded as unappealing: scientists and regulators often go
to a great deal of trouble to design experiments whose *only* stochastic assumptions are ones almost
nobody would dispute, and adding a prior on top of that reintroduces exactly the kind of assumption
they were trying to avoid.

The frequentist route instead changes the subject: rather than reasoning inductively about which
hypothesis is true, it commits in advance to a *behavior* — a decision rule, applied the same way
every time the experiment is run. Formally, the rule outputs one of two actions:

1. **Reject** $H_0$ (declare it implausible; $H_1$ must hold), or
2. **Accept** $H_0$ (continue to believe it).

Note the built-in asymmetry: $H_0$ is the privileged default, the thing that must be disconfirmed
rather than the thing that must be established. The usual analogy is a criminal trial, where the
defendant is innocent until proven guilty.

Of course, real credence in a hypothesis should move continuously as evidence accumulates — it would
be absurd to flip from total belief in $H_0$ to total belief in $H_1$ exactly at the instant some
statistic crosses a threshold. But some real decisions genuinely are dichotomous: does the FDA approve
the drug, or not; does the experimental design need to control for some variable, or not. It's worth
keeping some critical distance from the idea that a test is really "accepting" or "rejecting" a
hypothesis in any deep epistemic sense.

In many of the standard settings — including two-sided $Z$-testing and the two-sample nonparametric
problem above — there are always points in $H_1$ that fit the data even better than $H_0$ does. So even
granting the conceit of a dichotomous decision, it is rarely plausible that we would ever "accept"
$H_0$ in the sense of regarding $H_1$ as disconfirmed. For this reason it is usually more honest to say
we "fail to reject $H_0$" rather than that we accept it — "accept" survives below only as a technical
term, and "fail to reject" is the phrase less likely to mislead a non-statistician.

## The critical function

A test is described completely by its **critical function** (or **test function**) $\phi$:

$$
\phi(x) = \begin{cases}
0 & \text{accept } H_0 \\
\gamma \in (0,1) & \text{reject with probability } \gamma \\
1 & \text{reject } H_0.
\end{cases}
$$

Allowing $\phi(x)$ to take intermediate values — *randomizing* the decision at some sample points — is
useful in the theory, as the next section shows, though it is almost never done in practice. When
$\phi$ takes only the values $0$ and $1$ it is **non-randomized**, and it partitions the sample space
$\mathcal{X}$ into a **rejection region** $R = \{x : \phi(x) = 1\}$ and an **acceptance region**
$A = \{x : \phi(x) = 0\}$.

Most tests are built by picking a real-valued **test statistic** $T(X)$ and a **critical threshold**
$c$, and rejecting when $T(X)$ is large. We say $\phi$ *rejects for large $T(X)$* if

$$
\phi(x) = \begin{cases}
0 & T(x) < c \\
\gamma \in (0,1) & T(x) = c \ \text{(if } \phi \text{ is randomized)} \\
1 & T(x) > c.
\end{cases}
$$

Much of the art of designing a test lies in choosing a statistic $T(X)$ that discriminates as sharply
as possible between $H_0$ and $H_1$.

## Errors, level, and power

Testing has two ways to go wrong: a **Type I error** (false positive) rejects a true $H_0$, and a
**Type II error** (false negative) fails to reject a false $H_0$. (Mnemonic: Type I is the error rate we
control first, when deciding whether to reject at all; Type II is secondary.) The goal, informally, is
to make the Type II error probability as small as possible under $H_1$, while keeping the Type I error
probability under a prespecified bound $\alpha \in [0,1]$. When $H_0$ or $H_1$ is composite there is no
longer *a* Type I or Type II error rate — it can depend on exactly which point of $\Theta_0$ or
$\Theta_1$ is sampled from.

The whole behavior of a test is captured by its **power function**

$$
\beta_\phi(\theta) = \mathbb{E}_\theta[\phi(X)] = \mathbb{P}_\theta(\text{reject } H_0).
$$

In these terms the goal is

$$
\operatorname*{maximize}_{\phi} \ \beta_\phi(\theta) \ \text{ for } \theta \in \Theta_1
\qquad \text{subject to} \qquad \beta_\phi(\theta) \le \alpha \ \text{ for } \theta \in \Theta_0.
$$

A test $\phi$ is a **level-$\alpha$ test** if $\sup_{\theta \in \Theta_0} \beta_\phi(\theta) \le \alpha$;
if this supremum is strictly below $\alpha$ the test is called **conservative**. The near-universal
choice $\alpha = 0.05$ traces back to an offhand remark of Ronald Fisher's, that he liked to use $0.05$
in his own scientific work — reportedly "the most influential offhand remark in the history of
science" (Brad Efron).

If $H_0$ is composite the optimization above has *multiple constraints* (one supremum over $\Theta_0$,
but really a constraint at every $\theta \in \Theta_0$); if $H_1$ is composite it has *multiple
objectives*, one power value to maximize at every $\theta \in \Theta_1$. The central question of this
chapter is whether a single test $\phi^*$ can optimize all of these objectives simultaneously.

## Worked example: the $Z$-test

Suppose we observe $Z(X) \sim N(\theta, 1)$. For the one-sided problem, a natural choice is the
**right-tailed test** $\phi_1(z) = \mathbb{1}\{z > z_\alpha\}$, rejecting for large $Z$, where
$z_\alpha = \Phi^{-1}(1 - \alpha)$ is the upper-$\alpha$ quantile of $N(0,1)$ and $\Phi$ is the standard
normal CDF. For the two-sided problem, a natural choice is the **two-tailed test**
$\phi_2(z) = \mathbb{1}\{|z| > z_{\alpha/2}\}$, rejecting for large $|Z|$.

<figure>
<svg viewBox="0 0 420 235" role="img" aria-label="Null and alternative normal densities with the one- and two-tailed rejection regions and the power they buy under the alternative">
  <line x1="30" y1="200" x2="400" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 380.0,200.0 L 380.0,199.7 L 376.2,199.5 L 372.3,199.2 L 368.5,198.9 L 364.6,198.5 L 360.8,197.8 L 357.0,197.0 L 353.1,195.9 L 349.3,194.5 L 345.4,192.7 L 341.6,190.4 L 337.8,187.5 L 333.9,184.0 L 330.1,179.7 L 326.2,174.6 L 322.4,168.7 L 318.5,161.8 L 314.7,154.1 L 310.9,145.4 L 307.0,136.0 L 303.2,125.9 L 299.3,115.3 L 295.5,104.4 L 291.7,93.5 L 287.8,82.8 L 284.0,72.7 L 280.1,63.5 L 276.3,55.4 L 272.5,48.9 L 268.6,44.0 L 264.8,41.0 L 260.9,40.0 L 257.1,41.1 L 253.3,44.1 L 249.4,49.0 L 245.6,55.7 L 241.7,63.7 L 237.9,73.0 L 234.1,83.1 L 230.2,93.8 L 226.4,104.8 L 226.4,200.0 Z" fill="currentColor" fill-opacity="0.12" stroke="none"/>
  <path d="M 238.7,200.0 L 238.7,70.9 L 233.5,84.7 L 229.2,96.8 L 226.4,104.8 L 226.4,200.0 Z" fill="#d97706" fill-opacity="0.45" stroke="none"/>
  <path d="M 40.0,200.0 L 48.5,199.9 L 57.0,199.8 L 65.5,199.6 L 74.0,199.0 L 82.5,197.9 L 91.0,195.8 L 99.5,192.0 L 108.0,185.8 L 116.5,176.1 L 125.0,162.3 L 133.5,144.1 L 142.0,122.1 L 150.5,98.1 L 159.0,74.8 L 167.5,55.4 L 176.0,43.2 L 184.5,40.2 L 193.0,47.1 L 201.5,62.5 L 210.0,83.8 L 218.5,107.8 L 227.0,131.3 L 235.5,151.9 L 244.0,168.3 L 252.5,180.4 L 261.0,188.6 L 269.5,193.8 L 278.0,196.8 L 286.5,198.5 L 295.0,199.3 L 303.5,199.7 L 312.0,199.9 L 320.5,200.0 L 329.0,200.0 L 337.5,200.0 L 346.0,200.0 L 354.5,200.0 L 363.0,200.0 L 371.5,200.0 L 380.0,200.0" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <path d="M 40.0,200.0 L 48.5,200.0 L 57.0,200.0 L 65.5,200.0 L 74.0,200.0 L 82.5,200.0 L 91.0,200.0 L 99.5,200.0 L 108.0,200.0 L 116.5,200.0 L 125.0,199.9 L 133.5,199.9 L 142.0,199.7 L 150.5,199.2 L 159.0,198.2 L 167.5,196.4 L 176.0,193.0 L 184.5,187.3 L 193.0,178.3 L 201.5,165.4 L 210.0,148.1 L 218.5,126.8 L 227.0,103.0 L 235.5,79.2 L 244.0,58.8 L 252.5,44.9 L 261.0,40.0 L 269.5,44.9 L 278.0,58.8 L 286.5,79.2 L 295.0,103.0 L 303.5,126.8 L 312.0,148.1 L 320.5,165.4 L 329.0,178.3 L 337.5,187.3 L 346.0,193.0 L 354.5,196.4 L 363.0,198.2 L 371.5,199.2 L 380.0,199.7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 3"/>
  <line x1="226.4" y1="200" x2="226.4" y2="35" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3" opacity="0.6"/>
  <line x1="238.7" y1="200" x2="238.7" y2="35" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3" opacity="0.6"/>
  <line x1="182.8" y1="200" x2="182.8" y2="35" stroke="currentColor" stroke-width="0.75" opacity="0.35"/>
  <text x="183" y="28" text-anchor="middle" font-size="12" fill="currentColor">p&#8320;</text>
  <text x="261" y="28" text-anchor="middle" font-size="12" fill="currentColor">p&#952;&#8321;</text>
  <text x="182.8" y="216" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="215" y="228" text-anchor="middle" font-size="11" fill="currentColor">z&#945;</text>
  <text x="255" y="216" text-anchor="middle" font-size="11" fill="currentColor">z&#945;&#8725;&#8322;</text>
  <text x="261" y="216" text-anchor="middle" font-size="11" fill="currentColor">&#952;&#8321;</text>
</svg>
<figcaption>The null density $p_0$ (solid) and the alternative $p_{\theta_1}$ (dashed) at $\alpha = 0.1$,
$\theta_1 = 2.3$. The pale region beyond $z_\alpha$ under $p_{\theta_1}$ is the power of the one-tailed
test; the darker sliver between $z_\alpha$ and $z_{\alpha/2}$ is power the one-tailed test claims but the
two-tailed test gives up, because the two-tailed test only starts rejecting further out, at
$z_{\alpha/2}$.</figcaption>
</figure>

The two tests' power functions both pass through $\alpha$ at $\theta = 0$, but they behave differently
away from it: the two-tailed power function is symmetric around $0$, while the one-tailed power
function stays *below* $\alpha$ for every $\theta < 0$ and rises *above* the two-tailed power function
for every $\theta > 0$ — visibly so in the figure, since the two-tailed test only starts rejecting at
the larger threshold $z_{\alpha/2} > z_\alpha$. The right-tailed test is technically a valid level-$\alpha$
test of the *two-sided* hypothesis too, but nobody would want to use it there, since it has less than
$\alpha$ power to reject when $\theta < 0$. What the comparison does show is that no single test can be
best throughout the two-sided alternative: the two-tailed test loses to the right-tailed test whenever
$\theta > 0$, and by symmetry a left-tailed test would win whenever $\theta < 0$. For the *one-sided*
problem, though, we might hope that the right-tailed test is best for every $\theta$ in the alternative
— and, as the next sections show, it is.

## The Neyman–Pearson lemma

To find out what "best" should mean and when it is achievable, start with the simplest possible
testing problem: a simple null $H_0 : X \sim P_0$ against a simple alternative $H_1 : X \sim P_1$.
Without loss of generality $P_0$ and $P_1$ have densities $p_0, p_1$ with respect to a common
dominating measure $\mu$ (one always exists — take $\mu = P_0 + P_1$).

The optimal level-$\alpha$ test rejects for large values of the **likelihood ratio statistic**

$$
\mathrm{LR}(X) = \frac{p_1(X)}{p_0(X)},
$$

that is,

$$
\phi(x) = \begin{cases}
1 & \mathrm{LR}(x) > c \\
\gamma & \mathrm{LR}(x) = c \\
0 & \mathrm{LR}(x) < c,
\end{cases}
$$

with $c$ and $\gamma \in (0,1)$ chosen so that $\mathbb{E}_0 \phi(X) = \alpha$ exactly. (By convention
$\mathrm{LR}(x) = \infty$ if $p_1(x) > p_0(x) = 0$ — including such an $x$ in the rejection region buys
power for free — and $\mathrm{LR}(x)$ is left undefined where $p_0(x) = p_1(x) = 0$, since such points
never arise under either hypothesis.)

**Why this is the right test.** The power of a test with rejection region $R$ is $\int_R p_1 \,
d\mu$, and its Type I error budget is $\int_R p_0 \, d\mu$. If $\mathcal{X}$ were discrete these would
just be sums over $x \in R$, and the sensible way to build $R$ is to collect the points that buy the
most power $p_1(x)$ per unit of error budget $p_0(x)$ spent. $p_1(x)$ is the "bang," $p_0(x)$ is the
"buck," and $\mathrm{LR}(x)$ is exactly the bang-for-buck ratio — so the best rejection region consists
of the points where that ratio is highest.

**Theorem (Neyman–Pearson lemma).** The likelihood-ratio test $\phi^*$ with $\mathbb{E}_0 \phi^*(X) =
\alpha$ maximizes power among all level-$\alpha$ tests of $H_0 : X \sim P_0$ against $H_1 : X \sim
P_1$.

**Proof.** The claim is that $\phi^*$ solves

$$
\operatorname*{maximize}_{\phi} \ \int \phi(x) p_1(x) \, d\mu(x)
\quad \text{subject to} \quad \int \phi(x) p_0(x) \, d\mu(x) \le \alpha.
$$

Its Lagrangian is

$$
\mathcal{L}(\phi; \lambda) = \int \phi(x) p_1(x)\, d\mu(x) - \lambda \int \phi(x) p_0(x) \, d\mu(x)
= \int \phi(x)\left(\frac{p_1(x)}{p_0(x)} - \lambda\right) dP_0(x).
$$

Maximizing this over all functions $\phi : \mathcal{X} \to [0,1]$ is a pointwise problem: at each $x$
the integrand is positive when $\mathrm{LR}(x) > \lambda$, so $\phi(x)$ should be as large as possible
there ($\phi(x) = 1$), and negative when $\mathrm{LR}(x) < \lambda$, so $\phi(x)$ should be as small as
possible there ($\phi(x) = 0$); the value of $\phi(x)$ where $\mathrm{LR}(x) = \lambda$ doesn't affect
the value of the integral at all. So *any* test agreeing with $\phi^*$ off the boundary $\mathrm{LR} =
\lambda$ maximizes the Lagrangian at $\lambda = c$ — in particular $\phi^*$ itself does.

Now take any other test $\phi$ with $\mathbb{E}_0 \phi(X) \le \alpha$. Then

$$
\mathbb{E}_1 \phi(X) \le \mathbb{E}_1\phi(X) - c\big(\mathbb{E}_0\phi(X) - \alpha\big)
\le \mathbb{E}_1 \phi^*(X) - c\big(\mathbb{E}_0 \phi^*(X) - \alpha\big) = \mathbb{E}_1 \phi^*(X),
$$

where the first inequality uses $\mathbb{E}_0\phi(X) \le \alpha$ and $c \ge 0$, the second uses that
$\phi^*$ maximizes the Lagrangian at $\lambda = c$, and the last uses $\mathbb{E}_0 \phi^*(X) = \alpha$
exactly. $\blacksquare$

The randomization parameter $\gamma$ exists to hit the constraint exactly when $\mathrm{LR}(X)$ has
atoms. Take $c_\alpha$ to be the upper-$\alpha$ quantile of the distribution of $\mathrm{LR}(X)$ under
$P_0$; if $\mathrm{LR}(X)$ is discrete it can happen that

$$
\mathbb{P}_0(\mathrm{LR}(X) > c_\alpha) < \alpha \le \mathbb{P}_0(\mathrm{LR}(X) \ge c_\alpha).
$$

The error budget is then "topped off" at exactly $\alpha$ by rejecting with probability

$$
\gamma = \frac{\alpha - \mathbb{P}_0(\mathrm{LR}(X) > c_\alpha)}{\mathbb{P}_0(\mathrm{LR}(X) = c_\alpha)}
$$

whenever $\mathrm{LR}(X) = c_\alpha$ exactly.

## Worked example: a binomial test

Take $X \sim \mathrm{Binom}(n, \theta)$, thought of as measuring the same-side bias of a human coin
flipper (an allusion to the Diaconis–Holmes–Montgomery study of coin-flip physics), and test
$H_0 : \theta = 0.5$ against $H_1 : \theta = 0.51$. The Neyman–Pearson lemma says to reject for large
values of

$$
\mathrm{LR}(X) = \frac{p_{0.51}(X)}{p_{0.5}(X)}
= \frac{0.51^X\, 0.49^{n-X}}{0.5^n}
= \left(\frac{0.49}{0.5}\right)^n \left(\frac{0.51}{0.49}\right)^X.
$$

Because $\mathrm{LR}(X)$ is a strictly increasing function of $X$, rejecting for large $\mathrm{LR}(X)$
is exactly the same as rejecting for large $X$: the optimal test rejects when $X$ exceeds its
upper-$\alpha$ quantile $c_\alpha$ under $P_{0.5}$.

Since $p_{0.5}(x) = \binom{n}{x} 2^{-n}$ only takes multiples of $2^{-n}$, a level like $\alpha = 0.05$
generally cannot be hit exactly by any non-randomized threshold — the boundary has to be randomized.
Concretely, with $n = 100$: the $0.95$ quantile of $\mathrm{Binom}(100, 0.5)$ is $c_\alpha = 58$, and
$\mathbb{P}_{0.5}(X > 58) = 0.044$, short of the requested $0.05$. So the test rejects outright for
$X > 58$, and additionally rejects with probability

$$
\gamma = \frac{0.05 - 0.044}{\mathbb{P}_{0.5}(X = 58)} \approx 0.26
$$

when $X = 58$ exactly, which fills the remaining error budget.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Binomial(100, 0.5) probability mass function with the accept and reject regions of the optimal level-0.05 test">
  <line x1="35" y1="190" x2="365" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="45.0" y1="190" x2="45.0" y2="150.8" stroke="currentColor" stroke-width="5"/>
  <line x1="58.5" y1="190" x2="58.5" y2="137.1" stroke="currentColor" stroke-width="5"/>
  <line x1="72.0" y1="190" x2="72.0" y2="121.5" stroke="currentColor" stroke-width="5"/>
  <line x1="85.5" y1="190" x2="85.5" y2="104.7" stroke="currentColor" stroke-width="5"/>
  <line x1="99.0" y1="190" x2="99.0" y2="88.0" stroke="currentColor" stroke-width="5"/>
  <line x1="112.5" y1="190" x2="112.5" y2="72.9" stroke="currentColor" stroke-width="5"/>
  <line x1="126.0" y1="190" x2="126.0" y2="60.7" stroke="currentColor" stroke-width="5"/>
  <line x1="139.5" y1="190" x2="139.5" y2="52.7" stroke="currentColor" stroke-width="5"/>
  <line x1="153.0" y1="190" x2="153.0" y2="50.0" stroke="currentColor" stroke-width="5"/>
  <line x1="166.5" y1="190" x2="166.5" y2="52.7" stroke="currentColor" stroke-width="5"/>
  <line x1="180.0" y1="190" x2="180.0" y2="60.7" stroke="currentColor" stroke-width="5"/>
  <line x1="193.5" y1="190" x2="193.5" y2="72.9" stroke="currentColor" stroke-width="5"/>
  <line x1="207.0" y1="190" x2="207.0" y2="88.0" stroke="currentColor" stroke-width="5"/>
  <line x1="220.5" y1="190" x2="220.5" y2="104.7" stroke="currentColor" stroke-width="5"/>
  <line x1="234.0" y1="190" x2="234.0" y2="121.5" stroke="currentColor" stroke-width="5"/>
  <line x1="247.5" y1="190" x2="247.5" y2="137.1" stroke="currentColor" stroke-width="5"/>
  <line x1="261.0" y1="190" x2="261.0" y2="160.8" stroke="currentColor" stroke-width="5"/>
  <line x1="261.0" y1="160.8" x2="261.0" y2="150.8" stroke="#d97706" stroke-width="5"/>
  <line x1="274.5" y1="190" x2="274.5" y2="162.1" stroke="#d97706" stroke-width="5"/>
  <line x1="288.0" y1="190" x2="288.0" y2="170.9" stroke="#d97706" stroke-width="5"/>
  <line x1="301.5" y1="190" x2="301.5" y2="177.5" stroke="#d97706" stroke-width="5"/>
  <line x1="315.0" y1="190" x2="315.0" y2="182.1" stroke="#d97706" stroke-width="5"/>
  <line x1="328.5" y1="190" x2="328.5" y2="185.3" stroke="#d97706" stroke-width="5"/>
  <line x1="342.0" y1="190" x2="342.0" y2="187.3" stroke="#d97706" stroke-width="5"/>
  <line x1="355.5" y1="190" x2="355.5" y2="188.5" stroke="#d97706" stroke-width="5"/>
  <text x="261" y="205" text-anchor="middle" font-size="11" fill="currentColor">c&#945; = 58</text>
  <text x="365" y="205" text-anchor="end" font-size="12" fill="currentColor">X</text>
</svg>
<figcaption>The $\mathrm{Binom}(100, 0.5)$ mass function. Bars for $X \le 57$ are the acceptance region;
bars for $X \ge 59$ (amber) are the rejection region; the bar at $X = c_\alpha = 58$ is split between
accepting (below) and rejecting with probability $\gamma \approx 0.26$ (above), which is what tops the
Type I error rate up to exactly $\alpha = 0.05$.</figcaption>
</figure>

In practice randomized tests are hardly ever used — the conservative test $\phi^*(X) = \mathbb{1}\{X >
58\}$ is itself a likelihood-ratio test, and is the most powerful test at its own (slightly smaller)
level $0.044$.

Now ask what changes if, having read a more recent empirical estimate, we had instead wanted
$H_1 : \theta = 0.508$. Repeating the calculation,

$$
\mathrm{LR}(X) = \left(\frac{0.492}{0.5}\right)^n \left(\frac{0.508}{0.492}\right)^X,
$$

which is again increasing in $X$, so the test again rejects for large $X$ — and, controlling the same
Type I error at the same null, it is *exactly the same test* $\phi^*$ as before. The same would happen
for any alternative $\theta_1 > 0.5$ (an alternative $\theta_1 < 0.5$ would instead reject for small
$X$). So $\phi^*$ is simultaneously the best test of $H_0 : \theta = 0.5$ against every alternative in
the *composite* hypothesis $H_1 : \theta > 0.5$. A test that is best against every point of the
alternative simultaneously is called **uniformly most powerful**.

## Uniformly most powerful tests

**Definition.** A test $\phi^*$ is a **uniformly most powerful (UMP)** level-$\alpha$ test of $H_0$
against $H_1$ if it is a valid level-$\alpha$ test and $\beta_{\phi^*}(\theta) \ge \beta_\phi(\theta)$
for every $\theta \in \Theta_1$ and every other valid level-$\alpha$ test $\phi$.

What made the binomial example UMP was that the likelihood ratio was increasing in $X$ *no matter which
alternative was chosen* — so rejecting for large $X$ was simultaneously optimal against all of them.
That is the property to isolate:

**Definition.** A family $\mathcal{P} = \{P_\theta : \theta \in \Theta \subseteq \mathbb{R}\}$ has
**monotone likelihood ratios (MLR)** in the statistic $T(X)$ if, for every $\theta_1 < \theta_2$, the
ratio $p_{\theta_2}(x)/p_{\theta_1}(x)$ is a non-decreasing function of $T(x)$.

**Theorem.** Suppose $\mathcal{P}$ has MLR in $T(X)$, and consider $H_0 : \theta \le \theta_0$ against
$H_1 : \theta > \theta_0$ for some $\theta_0 \in \Theta$. If $\phi^*(X)$ rejects for large $T(X)$, then
$\phi^*$ is UMP at level $\alpha = \mathbb{E}_{\theta_0}\phi^*(X)$.

**Proof.** Let $\phi$ be any other level-$\alpha$ test, and fix any $\theta_1 > \theta_0$. Restricted to
the simple problem $H_0 : \theta = \theta_0$ vs. $H_1 : \theta = \theta_1$, $\phi$ is still a valid
level-$\alpha$ test, and so is $\phi^*$ by assumption. Since $p_{\theta_1}(X)/p_{\theta_0}(X)$ is a
non-decreasing function of $T(X)$ by MLR, $\phi^*$ *is* a likelihood-ratio test for this simple problem,
so by Neyman–Pearson $\beta_{\phi^*}(\theta_1) \ge \beta_\phi(\theta_1)$.

It remains to check $\phi^*$ is actually level $\alpha$ over all of $\Theta_0$, not just at the
boundary $\theta_0$ — first note $\beta_{\phi^*}(\theta_1) \ge \alpha$ for $\theta_1 > \theta_0$, by
comparison with the trivial test $\phi \equiv \alpha$ that ignores the data entirely. Now let
$\bar\phi(X) = 1 - \phi^*(X)$, which rejects for *small* $T(X)$ (equivalently, for large $-T(X)$); by
the same MLR argument applied in reverse, $\bar\phi$ is a level-$(1-\alpha)$ likelihood-ratio test of
$H_0 : \theta = \theta_0$ against $H_1 : \theta = \theta_1$ for any $\theta_1 < \theta_0$. Hence for such
$\theta_1$,

$$
1 - \alpha \le \beta_{\bar\phi}(\theta_1) = 1 - \beta_{\phi^*}(\theta_1),
$$

i.e. $\beta_{\phi^*}(\theta_1) \le \alpha$ for $\theta_1 < \theta_0$, which together with
$\beta_{\phi^*}(\theta_0) = \alpha$ gives $\sup_{\theta \le \theta_0} \beta_{\phi^*}(\theta) = \alpha$.
$\blacksquare$

The main source of MLR families is exponential families:

**Example (one-parameter exponential family).** Let $X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim}
p_\eta(x) = e^{\eta T(x) - A(\eta)} h(x)$. For $\eta_1 < \eta_2$, the likelihood ratio for the full
sample is

$$
\frac{\prod_i p_{\eta_2}(x_i)}{\prod_i p_{\eta_1}(x_i)}
= \exp\left\{ (\eta_2 - \eta_1) \sum_i T(x_i) - n\big(A(\eta_2) - A(\eta_1)\big) \right\},
$$

which is increasing in $\sum_i T(x_i)$ whenever $\eta_2 > \eta_1$ (and decreasing in it otherwise). So
$\mathcal{P}$ has MLR in $\sum_i T(X_i)$, and every likelihood-ratio test of a one-sided hypothesis in
$\eta$ rejects for large values of $\sum_i T(X_i)$ — giving a UMP test for free, by the theorem above.

## Sources

All material in this chapter comes from the "Hypothesis Testing and the Neyman–Pearson Lemma" section
of the STAT 210A course reader (Berkeley), which is essentially unchanged across the offered years:

- Text and worked examples: `berkeley-stat210a` reader, section "Hypothesis Testing," converted at
  `statistics/berkeley/stat210a/fall-2024/reader/hypothesis-testing/01-hypothesis-testing.md`,
  `02-the-critical-function.md`, and `03-optimal-testing.md` (identical content also at
  `fall-2026/reader/hypothesis-testing/`, and the same text converted from the HTML build at
  `fall-2025/reader/hypothesis-testing/01-1-hypothesis-testing.md` through `03-3-optimal-testing.md`,
  duplicated again under `fall-2025/units/reader/hypothesis-testing/`). The fall-2024/2026 version was
  used as the base text, since it carries the plotting code inline rather than as external images.
- Both figures in this chapter — the $Z$-test rejection-region plot and the binomial acceptance/rejection
  bar chart — were redrawn as SVG from the R code embedded in `02-the-critical-function.md` and
  `03-optimal-testing.md` respectively (parameters $\alpha = 0.1$, $\theta_1 = 2.3$ for the first; $n =
  100$, $\alpha = 0.05$ for the second), reproducing the same plots shown in the reader rather than the
  external PNGs linked from the fall-2025 HTML conversion.
- No lecture transcript or slide deck was supplied for this chapter; the course reader is the only
  source. The reader mentions but does not itself contain the Diaconis–Holmes–Montgomery study of
  coin-flip bias referenced in the binomial example.
- No exercises were supplied with this material.

---

[← 17. Standing Homework Conventions](17-standing-homework-conventions.md) · [Contents](index.md) · [19. Course Overview and Schedule →](19-course-overview-and-schedule.md)
