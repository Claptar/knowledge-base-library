---
title: Statistical models
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Statistical models

**Source:** [`reader/estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Until now, we have been discussing the topic of *probability*. Roughly speaking, in probability we fully specify the distribution of some random variables, and then ask what we can say about aspects of the distribution. For example, given a complete description of the rules for generating a random walk, we might ask how long, in expectation, it will take to reach a certain threshold. This is an essentially *deductive* exercise: while the mathematics might be complicated, and the questions concern probabilities, they ask generally have unambiguous answers.

In statistics, we do essentially the opposite: beginning with the *data* --- the Latin word for "given" --- we work backwards to draw inferences about the data-generating distribution. This is an *inductive* exercise, for which the answers will inevitably be more ambiguous.

We will generally use the letter $X$ to denote the full data set, which we assume is drawn randomly from some unknown distribution $P$ over the *sample space* $\cX$. Let $\cP$ denote a family of candidate probability distributions, called the *statistical model*. We presume the analyst is assuming that *some* $P\in \cP$ is the true data-generating distribution $P$, but without knowing which one.

### Example: three models for coin flipping

In lecture 1, we discussed a study in which 48 participants flipped coins $n=350,757$ total times, observing that the coin landed on the same side it began $X=178,079$ total times, about $50.8\%$. We discussed three possible models for how the data were generated, in order from simplest to most complicated:

**Model 1 (Binomial):** All $n$ flips are independent, and land same-side up with the same probability $\theta \in (0,1)$. Then, $X$ follows a binomial distribution:
$$
X \sim \text{Binom}(n, \theta), \quad \text{ for some } \theta \in [0,1].
$$
Formally, we can say the family of distributions is $\cP = \{\text{Binom}(n, \theta):\; \theta \in (0,1)\}$, a set of distributions indexed by a single real parameter $\theta$.

Note that in the previous example, the integer $n$ is another important variable in the problem, but we implicitly assumed that it was "known" by the analyst, meaning that it is the same for all $P \in \cP$. The parameter $\theta$, by contrast, is termed "unknown" in the sense that it varies over the family $\cP$. This is a critical distinction, and $n$ is not really considered a parameter of the binomial model except in certain rare applied settings where it is actually unobserved.

The binomial model has a known distribution given by the pmf:
$$
p_\theta(x) = \binom{n}{x} \theta^x (1-\theta)^{n-x}, \quad \text{ for } x= 0,1,\ldots,n.
$$
In other words, each distribution $P_\theta = \text{Binom}(n,\theta)$ has density $p_\theta$ with respect to the counting measure on the sample space $\cX = \{0,1,\ldots,n\}$.

**Model 2 (Independent binomials):** A second, more general model retains the independence assumption but allows for each of the 48 flippers to have a different same-side bias. Then, if $n_i$ are the number of flips by the $i$th flipper, $\theta_i \in (0,1)$ is that flipper's same-side probability, and $X_i$ is the number of same-side outcomes, we can write our model as
$$
X_i \simind \text{Binom}(n_i,\theta_i), \quad \text{ for } i = 1,\ldots,48.
$$
This model contains the first model, since it allows for the possibility that all $\theta_i$ share a common value, but is considerably more general, being indexed by $48$ real parameters instead of one, or equivalently by a parameter vector $\theta = (\theta_1,\ldots,\theta_{48}) \in (0,1)^{48}$.

Multiparameter models are more complicated to study than single-parameter models, because methodological choices become more ambiguous and context-dependent. For example, in this example we would likely believe that data from the first $47$ flippers, besides informing us about $\theta_1$ through $\theta_47$, also indirectly inform us about what values for $\theta_{48}$ are more or less likely. Later in the course, we'll discuss various strategies for estimating the full $\theta$ vector that allow us to encode this belief.

**Model 3 (Bias reducing over time):** A still more general model allows each flipper's same-side bias to change over time as they gain more practice; Bartos et al. observed that each flipper's same-side probability started above $50\%$ but gradually decayed toward $50\%$ as the experiment went on. Thus, if $\theta_{i,j}$ represents the probability of heads for the $i$th flipper's $j$th flip, and $X_{i,j}\in \{0,1\}$ represents an indicator of whether that flip landed same-side up, we have the model
$$
X_{i,j} \simind \text{Bernoulli}(\theta_{i,t}), \quad \text{ for } i=1,\ldots, 48, \text{ and } j=1,\ldots,n_i.
$$
This model, with $n$ total parameters (one for every flip) seems a bit *too* large: for example, by sending $\theta_{i,j} \to X_{i,j}$, for every $i$ and $j$, we can perfectly explain the entire data set. We can rein in this pathological behavior by imposing sensible constraints, for example by requiring that the same-side bias is never negative and decays over time for each flipper:
$$
\theta_{i,1} \geq \theta_{i,2} \geq \cdots \geq \theta_{i,n_i} \geq 0.5, \quad \text{ for } i=1,\ldots,48.
$$
We are essentially dealing with a nonparametric model at this point, and this constraint is an example of a *shape constraint*.

An alert reader might have noticed that the sample space kept changing as we changed the model. This is not because the model affects what data we observe: the experimenters recorded each flipper's entire sequence of flips. Rather, it is because the model affects what data we *retain* after summarizing it as compactly as we can without losing information. Next week, when we study the topic of *sufficiency*, we will learn why.

### Parametric vs nonparametric models

Many of the models we will consider in this class are *parametric*, typically meaning that they are indexed by finitely many real parameters. That is, we have $\cP = \{P_\theta:\; \theta \in \Theta\}$, for some *parameter space* $\Theta$ that is typically in $\RR^d$ for some $d$. Then $\theta$ is called the *parameter* or *parameter vector*, and $d$ is called the *model dimension*.

In other models, there is no natural way to index $\cP$ using $d$ real numbers. We call these *nonparametric* models. Sometimes excited authors referred to their methods as "assumption-free," but essentially all nonparametric models still make some assumptions about the data distribution. For example, we might assume independence between multiple observations, or shape constraints such as monotonicity.

**Example (Nonparameric model):** Suppose we observe an i.i.d. sample of size $n$ from a distribution $P$ on the real line. Even if we do not want to assume anything about $P$, the i.i.d. assumption will play an important role in the analysis. We might write this model as

$$
X_1,\ldots,X_n \simiid P, \quad \text{ for some distribution } P \text{ on } \RR.
$$

Formally, if $X = (X_1,\ldots,X_n)$, we can write the family as $\cP = \{P^n:\; P \text{ is a distribution on } \RR\}$, where $P^n$ represents the $n$-fold product of $P$ on $\RR^n$.

**Notation:** Much of what we will learn in this course applies to parametric and nonparametric models alike, and indeed there is no crisp demarcation between parametric and nonparametric models in practice. It will often be convenient to use notation $\cP = \{P_\theta :\; \theta \in \Theta\}$, without specifying what kind of set $\Theta$ is; in particular there is nothing to stop $\theta$ from being an infinite-dimensional object such as a density function. We can work in this notation without any loss of generality, since we could always take $\theta = P$ and $\Theta = \cP$.

### Statistical inference: What is $\theta$?

Returning to the simplest model, suppose the analyst observes $X \sim \text{Binom}(n,\theta)$ and wants to know what $\theta$ is. How might we think about answering this question?

**Skeptic's Answer:** If we consult a philosophical *skeptic* influenced by Hume, they might tell us simply that we don't know what $\theta$ is: it could be anything! Indeed, it is true that any outcome $X$ is perfectly logically consistent with any parameter value $\theta \in (0,1)$: if $\theta$ is $0.1$, it may be astronomically unlikely that we would observe an outcome as large as $X = 178,079$, but it is possible. So, the skeptic has a point in that we actually cannot logically rule out any value.

**Bayesian Answer:** If instead we consult a Bayesian, they will get around Hume's answer by introducing a new assumption, that $\theta$ had some distribution over $(0,1)$ before we saw the data, and all we need to do to upon seeing the data is to calculate the conditional distribution of $\theta$ given $X$, according to Bayes' rule. The Bayesian will still admit they don't know exactly what $\theta$ is, but they can make precise probability statements about, for example, the probability that $\theta \leq 0.1$ (or the probability that $\theta \leq 0.5$).

A practical advantage of this approach is that it reduces the problem to a simple matter of calculation. In general, the calculations for a Bayesian problem can be difficult (especially if we try to use a prior that reflects our "true" subjective beliefs), but conditioning on evidence is conceptually straightforward.

Different Bayesians with different prior distributions will also have different opinions after seeing the data. A Bayesian with a strong enough conviction that $\theta$ is below $0.1$ could be surprised by our having observed so many same-side flips, but nevertheless remain unimpressed. However, in this problem we could plausibly argue that most "reasonable" Bayesians will arrive at a posterior belief very similar to the Bartos's, for reasons we'll discuss later in the semester.

**Frequentist Answer:** Finally, a frequentist will simply change the subject: instead of trying to tell us what $\theta$ is, the frequentist will propose a *method* for using $X$ to guess or *estimate* the value of $\theta$, for example via the *estimator* $\delta_0(X) = X/n$. The frequentist may offer various arguments and proofs that their estimator is ubiased, or optimal in some sense; and may be able to quantify in great precision how accurate the estimator is.

For example, if $n=350,757$ then the frequentist can say (without knowing what value $\theta$ takes) that $\delta_0(X)$ has expectation $\theta$ and standard deviation no greater than $1/2\sqrt{n} \approx 8.4\times 10^{-4}$, or $0.084\%$. Hence, it's very unlikely that $\delta_0(X)$ will miss the true value of $\theta$ by more than a single percentage point.

This all goes very well until you calculate the estimator, $\delta_0(X) = 50.8%$, and try to claim that $\theta$ is probably within a percentage point of that value. At that point, the frequentist will demur: all of the previous calculations were done with respect to the randomness in the *data*, without making any assumption that $\theta$ is random; once the data is realized there is no randomness left so there is no basis for making probabilistic statements about $\theta$. The frequentist is no longer willing to say anything about *this* experiment's $\theta$ value or estimation error; they only want to talk about what will happen the next time you observe a binomial experiment.

This is not just a pedantic point or a matter of dogmatically denying the metaphysical position that $\theta$ is random: as we've just seen, if we did assume a prior for $\theta$, we could choose one for which most of the prior's mass would remain below $10\%$, and we wouldn't be contradicting any of the frequentist's calculations above.

For the remainder of this lecture, we'll adopt the frequentist's methodological perspective: we approach a new problem without having yet observed the data, and try to come up with a method that will perform well with high probability. We will be particularly interested in *evaluating* and *comparing* the performance of different estimators we could choose.

---

[Up: contents](index.md) · [Estimation in statistical models →](02-estimation-in-statistical-models.md)
