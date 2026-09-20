---
title: "4. Where Does the Prior Come From?"
course: "Berkeley Stat 210A Fall 2024"
chapter: 4
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Where Does the Prior Come From?

## What this covers

Every Bayesian calculation starts from a prior $\pi(\theta)$, and every Bayesian owes an answer to
the question of where that prior came from. This chapter surveys the interpretations of probability
that make the question urgent, then works through the four sources practitioners actually reach
for — subjective belief, objective or "vague" rules, experience with similar problems, and sheer
computational convenience — with the worked examples (a coin's bias, a binomial parameterized two
ways, a population of hierarchical Gaussian or Beta-Binomial problems) that show what each source
buys and what it costs. It assumes the basics of Bayesian updating (prior times likelihood gives
posterior) and comfort with exponential families, Fisher information, and conjugate priors.

## Why model anything as random?

Probability distributions have a clean mathematical definition as normalized measures, but nothing
in that definition tells you when it is licensed to attach a probability to something in the real
world. Statisticians have historically split over this, and the split runs along a specific line:
are we willing to assign a probability to an *event* only, or also to a fixed but unknown
*parameter*? Frequentists take the first, more modest position; Bayesians take the second.

**Aleatory uncertainty** is uncertainty about whether a chance event will occur — named for the
Latin word for a die (*alea iacta est*, "the die is cast," as Caesar is supposed to have said on
crossing the Rubicon). The frequentist interpretation of an aleatory probability is a relative
frequency over a well-specified *reference class* of similar trials: a radium-226 atom decays with
some probability in a given interval because, watching enough atoms, a fixed fraction of them do —
the half-life ($\approx 1600$ years) is measured this way, and a probability like $2^{-1/1600}$ for
a new atom just says there is nothing special distinguishing this atom from the reference class of
all the others. This works cleanly for repeated physical trials (coin flips, particles at a double
slit) and for randomness a statistician deliberately builds into an experiment (randomly sampling
survey respondents, randomly assigning treatment and control) — in both cases there is little
controversy about what the number means.

It works less cleanly elsewhere. What is the right reference class for whether a particular
83-year-old Japanese woman will recover from a chemotherapy treatment? Each fact you add about her
narrows the class — and once you have sequenced her tumor's genome, the reference class has size
one. Even ordinary coin flipping is not immune: whether a coin lands the way it started depends on
who is flipping it and can change as they get better at it, prompting the Heraclitean remark that a
man cannot step into the same river twice, because neither the river nor the man is the same.
Some aleatory probabilities instead rest on a *propensity* argument from the physics of the system —
a symmetric die should land on each face equally often by symmetry, with no reference class needed.

**Epistemic uncertainty** is uncertainty about what is *true*, not about what will *happen* — whether
a defendant committed the crime, whether a given theory of physics is correct. Bayesians are
comfortable putting a probability on this. If you want that probability to be an *objective* measure
of the evidence, one classical route is a "principle of indifference": enumerate the possibilities and
weight them equally. This is question-begging (why should they be equally likely?) and, worse, is not
even well defined once the possibilities are infinite, which is the normal case for a parameter space.
The alternative is the **subjectivist** view: a probability is a particular person's degree of belief,
readable off the odds at which they would bet on a proposition. A rational person's beliefs, in this
view, form a coherent probability measure and should update by Bayes' rule as evidence comes in. This
is philosophically clean but practically hard once there are many unknowns, because it commits you to
a *joint* prior over all of them — try specifying your subjective joint belief about how a treatment
affects the abundances of a few thousand interacting microbiome species, and you will see why almost
no one claims to have run a truly subjective Bayesian analysis on a problem that large.

In practice these philosophical commitments rarely dictate method choice. A committed frequentist may
choose a Bayes estimator because it minimizes some average-case risk; a committed subjectivist running
a scientific study may avoid writing "in my personal opinion, the mass of the Higgs boson is..." A
small-business owner facing a low-data decision about holiday inventory, by contrast, has no need to
justify the decision as objective, and should bring their fuzzy intuitions to bear.

### A coin in the air

A demonstration sharpens the aleatory/epistemic divide. A professor takes out a coin, and the class
agrees there is a $50\%$ chance it lands heads — pure aleatory uncertainty. The professor flips it and
catches it between his hands, unseen, and asks again. Now the class splits: some say still $50\%$,
because nothing has been learned since the flip; others say the outcome is now fixed at $0\%$ or
$100\%$, we just do not know which. The professor peeks at the coin without revealing it, and asks a
third time. Subjectivists are comfortable saying it is still $50\%$ *to them*, even though it has
collapsed to $0$ or $1$ *to the professor* — two people, two probabilities, both legitimate, because
a subjective probability is indexed to what its holder knows.

But push on the boundary: even before the flip, the outcome was arguably already determined by the
laws of physics acting on exactly how the coin was thrown. Randomized treatment assignment is usually
generated by a pseudo-random number generator that is deterministic under the hood. If that is right,
aleatory uncertainty was never really different in kind from epistemic uncertainty — it was
epistemic uncertainty about a deterministic process all along, dressed up as a die being cast.

## Two ways to evade the problem of induction

Neither school actually answers "given the data I saw, what is $\theta$?" outright — both dodge it,
in different directions. A frequentist devises an estimator, proves it is precise (off by no more
than $0.1$, say, at most $1\%$ of the time), and reports $\delta(X)$ for the realized $X$ — but if
pressed on whether $\theta$ is therefore *probably* close to $\delta(X)$, a strict frequentist may
deny the question is meaningful: $X$ has already been observed, so there is no probability left in
the problem, only the pre-data distribution of the *procedure*. This evades induction by answering a
different question.

A Bayesian evades it by begging the question instead. Given a prior $\pi(\theta)$, the posterior
$\pi(\theta\mid x)$ licenses exactly the probability statements about $\theta$ that a frequentist
refuses to make — but those statements are only as good as an assumption, made before the data
arrived, about what $\theta$'s distribution was. So a Bayesian has to be ready to say where the prior
came from. (Bayesians sometimes retort that the likelihood model is no less subjective a choice — fair
in some cases — but at least a likelihood is usually checkable by repeated sampling, in a way a prior
over a single fixed parameter is not.)

It can also be reasonable to want no prior at all. Suppose $X_1,\dots,X_n$ are drawn i.i.d.\ from an
unknown density $p$ on $\mathbb{R}$, and the target is the median $m(p)$. The sample median is a
genuinely good estimator here — robust to outliers, nonparametric, and for large $n$ approximately
$N\!\left(m(p), \tfrac{1}{4np(m)^2}\right)$ — but it is *not* the Bayes estimator for any believable
prior on $p$. A Bayesian route would have to put a prior on the infinite-dimensional object $p$
itself, grind through a posterior that is horrific to compute for anything but a special prior, and
report something like $\mathbb{E}[m\mid X]$. If that answer came out far from the sample median, the
natural reaction would be to suspect the prior, not the sample median — which is itself a sign that,
in this problem, the prior was buying nothing.

## Where does the prior come from?

Four sources of a prior on $\theta$ recur in practice.

### Source 1: subjective belief

The most direct route is introspection: what do you actually believe, before seeing data? Flip a
coin $20$ times and see $7$ heads — an estimate of $0.5$ is probably more sensible than the raw
frequency $0.35$, which is exactly what a prior like $\pi(\theta)\propto\theta^{10}(1-\theta)^{10}$
(a Beta prior with ten pseudo-heads and ten pseudo-tails) would produce after combining with the
data.

A richer version of the same idea: introspecting about a new coin's bias might produce a prior that
puts most of its mass in a central bump around $0.5$ — say a $\text{Beta}(400,400)$ — but reserves
some probability for the coin being rigged, via a pair of spikes near the extremes (a
$\text{Beta}(0.1,0.1)$, capturing "always heads" or "always tails"), plus a small residual uniform
component to cover whatever else might be true. Flip such a coin ten times and see $7$ heads: the
posterior mean comes out around $0.52$ — much more sensible than the UMVU estimator $X/n=0.7$, which
takes the small sample entirely at face value. Flip it ten times and see $10$ heads instead: the
posterior swings hard toward the rigged-coin spike, giving a posterior mean around $0.98$ — the
prior's built-in suspicion of trick coins is exactly what lets it react so much faster than a naive
frequency estimate would.

Subjective priors have real advantages: they bring genuine information to bear, and the resulting
posterior has a clean interpretation as "my beliefs, updated." The costs are equally real. The
posterior inherits the prior's subjectivity — it is embarrassing to preface a published result with
"in my opinion..." And it becomes close to impossible once $\theta$ is high-dimensional or the model
is nonparametric: nobody has plausibly specified a genuine subjective *joint* prior over how a
treatment affects a few thousand microbiome species, or over a million SNPs' effects on disease risk.

### Source 2: objective or vague priors

If subjectivity is the problem, one response is to remove it by fiat: pick a prior that encodes no
information, a "principle of indifference" made precise. This is trivial on a finite parameter space
and much less obvious once $\Theta$ is continuous, because any continuous prior assigns zero mass to
every individual point — "equal weight to every point" is not a coherent instruction; the best you
can do is spread weight equally over equal-sized neighborhoods.

**The flat prior.** Put a uniform density on $\Theta$; if $\Theta$ is unbounded, use
$\lambda(\theta)=1$ as an *improper* (non-normalizable) prior anyway. Often the posterior is
perfectly normalizable even though the prior is not: with $\theta\sim\lambda(\theta)=1$ on
$\mathbb{R}$ and $X\mid\theta\sim N(\theta,\sigma^2)$, mechanically multiplying prior by likelihood
gives $\lambda(\theta\mid x)\propto \exp\!\big(-(\theta-x)^2/2\sigma^2\big)$, i.e.\
$\theta\mid x\sim N(x,\sigma^2)$ — a perfectly good, normalized posterior, with posterior mean
$\bar x$, coinciding with the UMVU estimator.

**Flatness depends on parameterization.** Put a flat prior on the success probability $\theta$ of a
$\text{Binom}(n,\theta)$ model, and look at the induced prior on the natural (logit) parameter
$\eta(\theta)=\log\frac{\theta}{1-\theta}$, with inverse $\theta(\eta)=\frac{e^\eta}{1+e^\eta}$. The
change-of-variables formula gives
$$
\lambda^{(\eta)}(\eta) = |\dot\theta(\eta)|\,\lambda^{(\theta)}(\theta(\eta)) = \frac{e^\eta}{(1+e^\eta)^2},
$$
which vanishes as $|\eta|\to\infty$: the interval $\eta\in[-11,-10]$, which corresponds to
$\theta\in[1.7\times10^{-5}, 4.5\times10^{-5}]$, gets almost no prior mass under a flat-in-$\theta$
prior, even though it is one unit wide in $\eta$. Go the other way — put a flat prior on $\eta$
instead — and the induced prior on $\theta$ works out to $\propto\frac{1}{\theta(1-\theta)}$, the
limit of a $\text{Beta}(\alpha,\alpha)$ as $\alpha\to 0$, which piles mass at the two extremes
$\theta\approx 0,1$. "Flat" is not a parameterization-free idea.

**The Jeffreys prior** fixes this by making the choice of coordinates irrelevant. Define
$$
\lambda_{\text{Jeff}}(\theta) \;\propto\; |J(\theta)|^{1/2},
$$
where $J(\theta)$ is the Fisher information (its determinant, in general). This is invariant under
smooth reparameterization, and can be shown to spread prior mass evenly with respect to
Kullback–Leibler distance between nearby models rather than with respect to a coordinate's own
Lebesgue measure. Checking invariance directly in the binomial model: the Fisher information for the
natural parameter is $J^{(\eta)}(\eta)=\text{Var}_\eta(X)$, and by the chain rule the Fisher
information for $\theta$ is
$$
\dot\eta(\theta)^2\,\text{Var}_\theta(X) = \big(\theta(1-\theta)\big)^{-2}\cdot n\theta(1-\theta) = \frac{n}{\theta(1-\theta)},
$$
so
$$
\lambda_{\text{Jeff}}^{(\theta)}(\theta)\;\propto\;\sqrt{\frac{1}{\theta(1-\theta)}}\;\propto\;\text{Beta}\!\left(\tfrac12,\tfrac12\right).
$$
Redo the calculation directly in $\eta$: $J(\eta)=\text{Var}_\eta(X)=n\frac{e^\eta}{(1+e^\eta)^2}$, so
$\lambda_{\text{Jeff}}^{(\eta)}(\eta)\propto\sqrt{e^\eta}/(1+e^\eta)$ — and applying the ordinary
change-of-variables formula to $\lambda_{\text{Jeff}}^{(\theta)}$ reproduces exactly this same
density. The two computations agree, as invariance promises they must.

**Vague priors can still be dangerous.** Losing normalizability can cost you real decision-theoretic
guarantees, such as admissibility. Take $X\sim N_d(\mu,I_d)$ and try to estimate $\rho^2=\|\mu\|^2$.
A flat (equivalently here, Jeffreys) prior on $\mu$ leaves the posterior equal to the likelihood,
$N_d(x,I_d)$, so the posterior mean of $\mu$ is the very reasonable $X$ — but the posterior mean of
$\rho^2$ is
$$
\delta_\lambda(X) = \mathbb{E}\big[\|\mu\|^2\mid X\big] = \|X\|^2 + d,
$$
compared with the UMVU estimator $\|X\|^2-d$. The flat-prior Bayes estimator has added a bias of
$2d$ for no reduction in variance, so its MSE exceeds the UMVU's by $4d^2$ — a penalty that swamps
the $O(d)$ variance of $\|X\|^2$ itself once $d$ is even moderately large. The mechanism is
geometric: for small $\epsilon$, the event $\|\mu\|\in[r,r+\epsilon]$ is a thin spherical shell of
volume $\propto r^{d-1}\epsilon$, so the implied density on $r=\|\mu\|$ grows rapidly with $r$. A
prior that looks perfectly flat and uninformative in the coordinates $\mu$ is, once you look at its
implied belief about $\|\mu\|$, extremely confident that $\|\mu\|$ is huge.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A ball in high dimension has almost all of its volume in a thin shell near its boundary, not near the center">
  <circle cx="160" cy="110" r="85" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="160" cy="110" r="70" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <circle cx="160" cy="110" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="160" y1="110" x2="245" y2="110" stroke="currentColor" stroke-width="1"/>
  <text x="200" y="103" font-size="12" fill="currentColor" text-anchor="middle">r</text>
  <text x="160" y="114" font-size="12" fill="currentColor" text-anchor="middle">small</text>
  <text x="160" y="127" font-size="12" fill="currentColor" text-anchor="middle">‖&#956;‖</text>
  <text x="160" y="35" font-size="12" fill="currentColor" text-anchor="middle">shaded shell: most of the volume, once d is large</text>
</svg>
<figcaption>A flat prior on $\mu\in\mathbb{R}^d$ looks uninformative in coordinates, but the shell
$\|\mu\|\in[r,r+\epsilon]$ has volume growing like $r^{d-1}\epsilon$: almost all of the prior's mass
sits far from the origin once $d$ is even moderately large, which is why its posterior mean for
$\|\mu\|^2$ is badly biased upward.</figcaption>
</figure>

A second, subtler cost: if the prior was nobody's actual belief before the data, whose belief does
the posterior represent afterward?

**When it doesn't matter: intersubjective agreement.** With enough data in a low-dimensional
parameter space, the likelihood can rule out almost everything except a narrow window, and *any*
reasonable prior — flat, Jeffreys, someone's genuine subjective prior, even a strongly opinionated
one — is close enough to flat on that narrow window that the posteriors converge. In a toy version,
$X\sim\text{Binom}(10^4,\theta)$ with observed $X=3000$: the likelihood has standard deviation
$\approx\sqrt{n}/n\approx 0.005$ around $\hat\theta=0.3$, is negligible outside $[0.29,0.31]$, and
essentially any prior is flat there, so $\pi(\theta\mid x)\propto\text{Lik}(\theta\mid
x)\approx\exp\!\big(-(\theta-0.3)^2/2(0.005)^2\big)$, giving $\theta\mid x\approx N(0.3,(0.005)^2)$
regardless of which reasonable prior you started from. The same thing happens at real scale: a large
coin-flipping data set with $n=350{,}757$ trials and $X=178{,}079$ same-side results produces a
likelihood so sharply peaked near $X/n\approx 0.508$ that a flat prior, a Jeffreys prior, a genuine
subjective prior, and even a strongly biased prior worth "$100$ pseudo-successes, $0.1$
pseudo-failures" all give visually indistinguishable posteriors — because whatever their differences
elsewhere, all four are roughly flat on the tiny interval where the likelihood actually lives. Data
swamps everyone's prior.

The high-dimensional pathology above is really about what happens *without* that swamping: the flat
or Jeffreys prior on the Gaussian sequence model $X\mid\theta\sim N(\theta,I_d)$ still gives
$\mathbb{E}[\theta\mid x]=x$ (matching the UMVU estimator) for $\theta$ itself, but for a different
functional — such as the $\ell_1$-penalized estimator $\hat\mu_j=\text{sign}(x_j)(|x_j|-\lambda)_+$,
whose properties are controlled by a James–Stein-type bound
$\|\hat\mu\|_2^2\le\|x\|_2^2-2d\lambda+d\lambda^2$ — the same shell-volume effect that biased
$\|\mu\|^2$ resurfaces, because "flat in $\theta$" is once again not "flat" in whatever coordinate
the estimand actually depends on.

### Source 3: prior or concurrent experience

The strongest source, when it is available, is genuine prior or concurrent experience with other
instances of a similar problem: if you are willing to say a whole *population* of $\theta$ values was
drawn from a common distribution, even a frequentist can be comfortable treating that distribution as
a real prior, estimable from the pooled data. Two closely related ways to exploit this:

- **Empirical Bayes** — treat the prior's parameters as unknown constants, estimate them (typically
  by maximum likelihood, from the model with the individual $\theta_i$'s marginalized out), and plug
  the estimate into the Bayes formula.
- **Hierarchical Bayes** — put a further prior (a **hyperprior**) on the prior's own parameters and
  do full Bayesian inference on the whole stack.

**Batting averages.** Suppose player $i=1,\dots,m$ has had $n_i$ at-bats and true batting average
$\theta_i$. A hierarchical model treats $(\alpha,\beta)$ as hyperparameters with a hyperprior
$\pi_0(\alpha,\beta)$, then $\theta_i\mid\alpha,\beta\sim\text{Beta}(\alpha,\beta)$ and
$X_i\mid\theta_i,n_i\sim\text{Binom}(n_i,\theta_i)$. Given $\alpha,\beta$, the posterior is
$\theta_i\mid X\sim\text{Beta}(\alpha+X_i,\beta+n_i-X_i)$, with posterior mean
$\frac{\alpha+X_i}{\alpha+\beta+n_i}$. If $m$ is large, the pooled data pin down $\alpha,\beta$ almost
exactly, and the choice of hyperprior stops mattering much — but there is a real **reference class
problem** left over: *which* players' data should count as informative about player $i$'s prior?

**A worked instance: hierarchical Beta-Binomial.** Take $m=48$ coin flippers (the same data set
behind the intersubjective-agreement example above), each with their own same-side bias, and assume
$$
\theta_i \overset{\text{iid}}{\sim} \text{Beta}(\alpha,\beta), \qquad
X_i \mid \theta \overset{\text{ind}}{\sim} \text{Binom}(n_i,\theta_i).
$$
For fixed $\alpha,\beta$ the posterior mean is $\delta_{i;\alpha,\beta}(X)=\mathbb{E}[\theta_i\mid
X]=\frac{X_i+\alpha}{n_i+\alpha+\beta}$, which depends only on $X_i$: conditional on the
hyperparameters, the $m$ flippers' problems are entirely independent of each other. Solving one such
problem in isolation, you would just pick $\alpha,\beta$ by hand — uniform ($\alpha=\beta=1$),
Jeffreys ($\alpha=\beta=1/2$), or some informative pseudo-count. But solving $m$ of them at once, you
can *learn* $\alpha,\beta$ from the data: marginalizing $\theta_i$ out gives the likelihood
$X_i\sim\text{Beta-Binom}(n_i,\alpha,\beta)$, from which $\alpha,\beta$ can be estimated by maximum
likelihood (empirical Bayes) and plugged back in, or given a hyperprior $\lambda_0(\alpha,\beta)$ and
integrated out properly (hierarchical Bayes):
$$
\delta_i(X)=\mathbb{E}[\theta_i\mid X]=\mathbb{E}\big[\mathbb{E}[\theta_i\mid X,\alpha,\beta]\mid
X\big]=\int_{\alpha,\beta}\frac{X_i+\alpha}{n_i+\alpha+\beta}\,d\lambda(\alpha,\beta\mid X).
$$
The final estimator is a *mixture* over the single-problem estimators, weighted by the posterior over
$(\alpha,\beta)$ given the whole data set — meaning the other $47$ flippers' data really does inform
player $i$'s estimate, even though conditional on the true hyperparameters they are irrelevant to each
other. With $m$ large, this is close to the best of both worlds: an informative prior for each
individual $\theta_i$, with the hyperparameters themselves pinned down by so much pooled data that
almost everyone would agree on them.

**Worked example: the Gaussian hierarchical model.** The same phenomenon, with cleaner algebra,
appears when
$$
\theta_i \overset{\text{iid}}{\sim} N(0,\tau^2), \qquad X_i\mid\theta_i \overset{\text{ind}}{\sim} N(\theta_i,1), \qquad i=1,\dots,d.
$$
For fixed $\tau^2$ the Bayes estimator is the linear shrinkage rule $\frac{\tau^2}{1+\tau^2}X_i$.
Reparameterize by the *shrinkage factor* $\zeta=\zeta(\tau^2)=\frac{1}{1+\tau^2}\in(0,1)$, so this is
$\delta_\zeta(X)=(1-\zeta)X$. Putting a hyperprior on $\tau^2$ (equivalently on $\zeta$) gives
$$
\mathbb{E}[\theta_i\mid X] = \mathbb{E}\big[(1-\zeta)X_i \mid X\big] = \big(1-\mathbb{E}[\zeta\mid X]\big)X_i = \delta_{\hat\zeta}(X),
$$
so the hierarchical Bayes rule is exactly the single-problem shrinkage rule with the shrinkage factor
replaced by its posterior mean $\hat\zeta=\mathbb{E}[\zeta\mid X]$ — hierarchical Bayes here *is*
plugging a Bayes estimate of the hyperparameter into the formula you would use if you knew it.

To find $\hat\zeta$, marginalize $\theta$ out: since
$\text{Var}(X_i\mid\zeta)=\text{Var}(\theta_i\mid\zeta)+\mathbb{E}[\text{Var}(X_i\mid\zeta,\theta_i)]=\tau^2+1=1/\zeta$,
the marginal likelihood is $X\mid\zeta\sim N_d(0,I_d/\zeta)$, an exponential family with sufficient
statistic $T(X)=\|X\|^2\sim\frac{1}{\zeta}\chi^2_d$. A conjugate (scaled-$\chi^2$) prior
$\zeta\sim\frac1s\chi^2_k$ gives posterior $\zeta\mid X\sim\frac{1}{s+\|x\|^2}\chi^2_{k+d}$, hence
$\mathbb{E}[\zeta\mid X]=\frac{k+d}{s+\|x\|^2}$ (the prior should really be truncated to $(0,1)$ since
$\zeta$ lives there, but for large $d$ the posterior concentrates in $(0,1)$ anyway and the
difference washes out).

The empirical-Bayes route to the same problem — estimate $\zeta$ from $T(X)=\|X\|^2\sim\chi^2_d/\zeta$
and plug it into $(1-\zeta)X$ — has three natural choices. Any Bayes posterior mean recovers the
hierarchical estimator above. The MLE, for an exponential family, solves
$\mathbb{E}_\zeta T(X)=d/\zeta=\|x\|^2$, giving $\hat\zeta_{\text{MLE}}=d/\|X\|^2$. And the UMVU
estimator comes from a direct calculation: writing $T(X)=Y/\zeta$ for $Y\sim\chi^2_d$,
$$
\mathbb{E}\!\left[\frac{1}{Y}\right] = \int_0^\infty \frac1y\cdot\frac{1}{\Gamma(d/2)2^{d/2}}y^{d/2-1}e^{-y/2}\,dy
= \frac{\Gamma\!\left(\frac{d-2}{2}\right)2^{(d-2)/2}}{\Gamma\!\left(\frac d2\right)2^{d/2}} = \frac{1}{d-2}
$$
for $d>2$ (the last integrand is a $\chi^2_{d-2}$ density, so it integrates to $1$, and the Gamma
ratio simplifies using $\Gamma(x+1)=x\Gamma(x)$). Since $\mathbb{E}[1/\|X\|^2]=\zeta\,\mathbb{E}[1/Y]$,
this makes $\frac{d-2}{\|X\|^2}$ unbiased for $\zeta$, giving the empirical Bayes estimator
$$
\delta_{\text{JS}}(X) = \left(1-\frac{d-2}{\|X\|^2}\right)X.
$$
This is the **James–Stein estimator** — arrived at here simply as the UMVU plug-in for the shrinkage
factor in a Gaussian hierarchical model, and interesting enough in its own right that it gets its own
treatment shortly.

A slightly more general version of the same calculation lets the common mean be unknown too:
$\theta_i\sim N(\mu,\tau^2)$, $X_i\mid\theta_i\sim N(\theta_i,\sigma^2)$. Averaging over $\mu,\tau^2$
gives posterior mean $\mathbb{E}\big[\frac{\tau^2}{\tau^2+\sigma^2}X_i+\frac{\sigma^2}{\tau^2+\sigma^2}\mu
\,\big|\,X\big]$. Writing $B=\tau^2+\sigma^2$ for the marginal variance of each $X_i$, the marginal
model is $X_i\mid\mu,B\sim N(\mu,B)$, so $\bar X\sim N(\mu,B/n)$ and
$S^2=\frac{1}{n-1}\sum_i(X_i-\bar X)^2\sim\frac{B}{n-1}\chi^2_{n-1}$. With an inverse-gamma conjugate
prior $\pi(B\mid\lambda,\nu)\propto B^{-\nu/2-2}e^{-\lambda/2B}$, the posterior is
$B\mid X\sim\text{InvGamma}\!\left(\frac{n+\nu}{2},\frac{\lambda+(n-1)S^2}{2}\right)$, giving
$\mathbb{E}[1/B\mid X]=\frac{n+\nu}{\lambda+(n-1)S^2}$ and, after simplification, the shrinkage rule
$$
\delta_i(x) = \frac{(n-3)S^2}{(n-1)S^2+\lambda}X_i + \frac{\lambda+2S^2}{(n-1)S^2+\lambda}\bar X,
$$
which shrinks each observation toward the *grand mean* $\bar X$ rather than toward $0$ — the natural
generalization once the common center is itself unknown. (If $\lambda$ is small, it can help to
truncate the prior to $B\ge\sigma^2$, since $B<\sigma^2$ would correspond to a nonsensical negative
$\tau^2$.)

### Source 4: convenience priors

Bayesian computation is often the bottleneck, so a real motive for choosing a prior is simply that it
makes the posterior tractable — in practice this usually means an exponential family, often one
conjugate to the likelihood. One principled reason exponential families keep showing up here is the
**maximum entropy principle**, a generalization of the principle of indifference. For a density $p$
relative to a base measure $\mu$ on $\mathcal X$, entropy is
$$
H(p) = -\int_{\mathcal X} p(x)\log p(x)\,d\mu(x).
$$
When $\mu$ is a finite measure, $H(p) = \log\mu(\mathcal X) - D_{\mathrm{KL}}(p\,\|\,p_{\text{unif}})$,
so maximizing entropy with no constraints just recovers the uniform density. Impose instead a moment
constraint $\mathbb{E}_p T(X)=\nu$ for some statistic $T(X)\in\mathbb{R}^s$: the entropy-maximizing
density subject to that constraint is $p(x)=e^{\eta'T(x)-A(\eta)}$ for whatever $\eta$ satisfies the
constraint — that is, constrained maximum-entropy distributions are exactly exponential families. So
if all you are willing to commit to about your prior on $\theta$ is its mean $\nu$ and variance
$\sigma^2$, and you want to stay maximally noncommittal beyond that, the entropy-maximizing choice
with sufficient statistic $(\theta,\theta^2)$ is — when the base measure is Lebesgue measure on
$\mathbb{R}$ — exactly $N(\nu,\sigma^2)$: the Gaussian prior is not merely convenient, it is the
least additional assumption you can make once mean and variance are fixed.

The persistent worry is the same one as for vague priors: if the prior was chosen for tractability
rather than belief, whose belief does the posterior represent? Return to the nonparametric median
example: define a prior over the infinite-dimensional $p$, grind through a posterior (horrific unless
the prior was chosen for convenience), and report $\mathbb{E}[m\mid X]$. If that differs substantially
from the sample median — the good, robust, nonparametric frequentist answer — should the Bayes answer
be trusted, or does it just reveal that the convenience prior smuggled in an assumption nobody
actually holds?

## The flexibility — and the limits — of Bayes

Once a full specification $(\pi,P,L,g(\theta))$ — prior, likelihood, loss, estimand — is on the table,
every decision problem reduces to the single formula
$$
\delta(x) = \arg\min_d \int L(\theta,d)\,\pi(\theta\mid x)\,d\theta,
$$
and the posterior becomes a one-stop shop for answering any question about $\theta$. This is a real
strength: nothing here requires an exponential family or a completeness argument, no estimator needs
to be $U$-estimable, and the loss need not be convex or otherwise well-behaved — the framework is
highly expressive by construction, because the entire problem has been reduced to a (possibly very
hard) integral. The caveat is exactly that "possibly very hard": the whole apparatus is only as useful
as your ability to actually carry out the computation, which is a separate topic in its own right.

## Sources

- Three parallel course-reader treatments of the same lecture, converted from Berkeley STAT 210A:
  - `berkeley-stat210a/fall-2024/reader/bayes-interpretation.qmd` — terse outline form (three
    interpretations of probability, four sources of priors with the Beta pseudo-count example, the
    Gaussian-sequence-model/$\ell_1$ pathology sketch, the batting-average hierarchical example, and
    the "flexibility of Bayes" summary), split as
    `docs/statistics/berkeley/stat210a/fall-2024/reader/bayes-interpretation/01-where-does-the-prior-come-from.md`
    and `.../02-gaussian-hierarchical-model.md` (general $\mu,\tau^2,\sigma^2,B$ shrinkage estimator).
  - `berkeley-stat210a/fall-2025/reader/bayes-interpretation.html` — the fully written-out prose
    version, split across
    `docs/statistics/berkeley/stat210a/fall-2025/reader/bayes-interpretation/01-interpretations-of-probability-and-sources-of-priors.md`
    through `04-3-example-hierarchical-gaussian-model.md`: aleatory/epistemic distinction, the
    coin-in-the-air demonstration, the nonparametric-median motivating example, the flat/Jeffreys
    derivations and binomial worked check, the $\|\mu\|^2$ admissibility example and its
    spherical-shell explanation, the large real coin-flip data set (the Bartosz et al. study,
    $n=350{,}757$), the maximum-entropy justification for exponential-family priors, the
    Beta-Binomial hierarchical model for $m=48$ coin flippers, and the $\zeta$-parameterized Gaussian
    hierarchical model culminating in the James–Stein estimator.
  - `berkeley-stat210a/fall-2025/units/reader/bayes-interpretation.html` — the same terse outline as
    the fall-2024 reader, split at
    `docs/statistics/berkeley/stat210a/fall-2025/units/reader/bayes-interpretation/01-introduction.md`
    through `03-3-gaussian-hierarchical-model.md`.
  - `berkeley-stat210a/fall-2026/reader/bayes-interpretation.qmd` — the same prose treatment as the
    fall-2025 reader (with the underlying R plotting code for the figures the reader describes but
    this chapter does not reproduce), split at
    `docs/statistics/berkeley/stat210a/fall-2026/reader/bayes-interpretation/01-interpretations-of-probability.md`
    through `03-example-hierarchical-gaussian-model.md`.
- Where the terse and prose versions covered the same ground, the prose version's derivations and
  worked numbers are used; the terse-only material (the Beta pseudo-count warm-up example, the
  batting-average example, the $\ell_1$/James–Stein preview under the Gaussian sequence model, the
  general-mean Gaussian hierarchical model, and the "flexibility of Bayes" summary) is folded in
  alongside it rather than repeated from both.
- The lecture points at material it does not itself contain: Homework 5 (admissibility of estimators
  built from improper priors; the intersubjective-agreement binomial calculation) and Homework 6 (the
  KL-neighborhood characterization of the Jeffreys prior), neither of which is among the supplied
  files, and a forthcoming lecture on Bayesian computation, referenced here only as "the topic of the
  next lecture." The James–Stein estimator is flagged in the source as getting fuller treatment "in
  two lectures" — this chapter only derives it as a byproduct of the hierarchical Gaussian model.

---

[← 3. Bayes Risk and Bayes Estimator](03-bayes-risk-and-bayes-estimator.md) · [Contents](index.md) · [5. Completeness →](05-completeness.md)
