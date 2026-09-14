---
title: Statistical models
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Statistical models

**Source:** [`reader/estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Until now, we have been discussing the topic of *probability*. Roughly speaking, in probability we fully specify the distribution of some random variables, and then ask what we can say about the distribution. For example, given a complete description of the rules for generating a random walk, we might ask how long, in expectation, it will take to reach a certain threshold. This is an essentially *deductive* exercise: while the mathematics might be very hard, the questions we ask generally have unambiguous answers.

In statistics, we do essentially the opposite: beginning with the *data* --- the Latin word for "given" --- we work backwards to draw inferences about the data-generating distribution. This is an *inductive* exercise, for which the answers will inevitably be more ambiguous.

We will generally use the letter $X$ to denote the full data set, which we assume is drawn randomly from some unknown distribution $P$ over the *sample space* $\cX$. Let $\cP$ denote a family of candidate probability distributions, called the *statistical model*. We assume the analyst knows that one of the elements of $\cP$ is the true data-generating distribution $P$, but does not know which one. The set $\cX$ in which $X$ is

**Example (Binomial):** As a simple example, we can imagine an analyst who flips a biased coin $n$ times, getting $X$ heads and $n-X$ tails. If we assume the successive flips are independent, and each has a common probability $\theta$ of landing heads, we can write the model as

$$
X \sim \text{Binom}(n, \theta), \quad \text{ for some } \theta \in [0,1].
$$

Formally, we could say the family of distributions is $\cP = \{\text{Binom}(n, \theta):\; \theta \in [0,1]\}$, a set of distributions indexed by the real parameter $\theta$.

Note that in the previous example, the integer $n$ is another important variable in the problem, but we implicitly assumed that it was "known" by the analyst, meaning that it is the same for all $P \in \cP$. The parameter $\theta$, by contrast, is termed "unknown" in the sense that it varies over the family $\cP$.

### Parametric vs nonparametric models

Many of the models we will consider in this class are *parametric*, typically meaning that they are indexed by finitely many real parameters. That is, we have $\cP = \{P_\theta:\; \theta \in \Theta\}$, typically for some *parameter space* $\Theta \subseteq \RR^d$. Then $\theta$ is called the *parameter* or *parameter vector*.

In other models, there is no natural way to index $\cP$ using $d$ real numbers. We call these *nonparametric* models. Sometimes excited authors referred to their methods as "assumption-free," but essentially all nonparametric models still make some assumptions about the data distribution. For example, we might assume independence between multiple observations, or shape constraints such as unimodality.

**Example (Nonparameric model):** Suppose we observe an i.i.d. sample of size $n$ from a distribution $P$ on the real line. Even if we do not want to assume anything about $P$, the i.i.d. assumption will play an important role in the analysis. We might write this model as

$$
X_1,\ldots,X_n \simiid P, \quad \text{ for some distribution } P \text{ on } \RR.
$$

Formally, if $X = (X_1,\ldots,X_n)$, we can write the family as $\cP = \{P^n:\; P \text{ is a distribution on } \RR\}$, where $P^n$ represents the $n$-fold product of $P$ on $\RR^n$.

**Notation:** Much of what we will learn in this course applies to parametric and nonparametric models alike, and indeed there is no crisp demarcation between parametric and nonparametric models in practice. It will often be convenient to use notation $\cP = \{P_\theta :\; \theta \in \Theta\}$, without specifying what kind of set $\Theta$ is; in particular there is nothing to stop $\theta$ from being an infinite-dimensional object such as a density function. We can work in this notation without any loss of generality, since we could always take $\theta = P$ and $\Theta = \cP$.

### Bayesian vs Frequentist inference

Thus far we have assumed the data $X$ follows a distribution $P_\theta$, for some unknown parameter $\theta$ which can be any arbitrary member of the set $\Theta$. In some contexts we will introduce an additional assumption we can call the *Bayesian assumption*: that $\theta$ is itself random, drawn from some known distribution $\Lambda$ that we call the *prior*.

A major advantage of this assumption is that it reduces the problem of inference about $\theta$ to simply calculating the conditional distribution of $\theta$ given $X$.

The philosophical ramifications of this assumption, as well as its practical advantages and disadvantages, will be a major theme later in the course, but for now we will simply say it is an assumption we are sometimes, but not always, willing to make. From a mathematical perspective, it makes no more or less sense to assume $\theta$ is random than it does to assume $\theta$ is fixed and unknown.

For the remainder of this lecture, and until our unit on Bayesian inference, we will refrain from making this assumption, instead regarding $\theta$ as taking an arbitrary fixed value in $\Theta$.

---

[Up: contents](index.md) · [Estimation in statistical models →](02-estimation-in-statistical-models.md)
