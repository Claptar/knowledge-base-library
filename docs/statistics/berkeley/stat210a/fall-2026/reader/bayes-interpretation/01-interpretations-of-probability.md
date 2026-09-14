---
title: Interpretations of Probability
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/bayes-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Interpretations of Probability

**Source:** [`reader/bayes-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

In this lecture, we will examine more closely the interpretation of Bayesian inference, and the controversy that has at times surrounded it. But first, we must ask the question: Why do we model anything as random? Probability distributions have a crisp mathematical definition as normalized finite measures, but they have also been a very useful conceit in statistics --- of both the frequentist and Bayesian varieties. But how do we justify attaching this mathematical definition to things in the real world?

There is a wide variety of candidate interpretations of probability, which you can find catalogued in the Stanford Encyclopedia of Philosophy's [entry on the subject](https://plato.stanford.edu/entries/probability-interpret/). From the perspective of statistical practice, the most important distinction is arguably whether we are willing to assign probabilities to unknown parameters, or only to the data set. Methodologically, this has led to a break between *Bayesians* who argue we are on solid ground assigning probabilities to both $\theta$ and $X$, and *frequentists* who argue we should refrain from assigning probabilities to $\theta$, and assign them only to $X$.

## Aleatory probabilities

Frequentists tend to adopt a more modest view that we should only assign a probability to the chance that an event will happen, and then only to certain kinds of events. Uncertainty about chance events happening is called *aleatory uncertainty* after the Roman word for a die (Caesar famously said "*alea iacta est*" --- the die is cast --- after crossing the Rubicon).

Strictly speaking, the *frequentist interpretation* of an event's probability is the relative frequency with which it occurs in a well-specified, and preferably large, *reference class* of similar trials. This interpretation is most concrete in the case of physical experiments: for example, there are many radium-226 atoms in the universe at any given time, and it has been observed that in any given time interval, a certain fraction of them will spontaneously emit alpha particles and decay to the radium-222 isotope. The half-life for this decay can be measured precisely by observing many such atoms (about $1600$ years) and faced with a new radium-226 atom we can estimate the likelihood that it will decay after a year as $2^{-1/1600}$, or $0.0004$, where the probability statement only requires us to accept that there is nothing special about the atom we have been presented with to distinguish it from the reference class of all the other radium atoms in the world. By contrast, many frequentists would deny that it is reasonable to assign a probability to a one-off event like whether the Democratic Party nominee will win the next presidential election.

The frequentist definition is appealing, but it can become more problematic when we try to extend it to other types of events to which statisticians regularly assign probabilities without thinking twice. If we have a coin or a die, we can imagine throwing it many times, but what is the right reference class if we are asking whether a certain patient will recover from lung cancer after a chemotherapy treatment? If we take into account information any clinician would likely know about the patient --- that she is a Japanese woman, that she is 83 years old, that her cancer was caught before spreading to other tissues etc. --- each of these pieces of information should affect the probability by narrowing the reference class to relevant examples. Nowadays we can also sequence her genome, as well as the genome of her tumor, but once we have done so we will have reduced her case to a reference class of size one. And yet, if we are considering which of several different treatments to prescribe, we would like to do more than shrug off the question of which treatment is most likely to cure her illness.

Even in the case of coin tossing, we have discussed in [Lecture 1](../introduction/index.md) that the probability of a coin landing on the same side as it began depends on who is flipping it, and may change over time as they acquire more skill. As the Greek Heraclitus eloquently put it, "A man cannot step into the same river twice, because it is not the same river, and he is not same man."

Other bases for aleatory probability may come from detailed knowledge of the physical system that let us judge its *propensity* to produce certain outcomes. For example, if we toss a near-perfectly symmetric six-sided die, we can argue simply from the symmetry of the system that it is equally likely to land on each face. In some cases, a statistician can directly infuse an experiment with well-specified aleatory randomness by carefully controlling the experimental conditions, for example by randomly sampling survey respondents from a well-specified population, or by randomly assigning the treatment or control condition to each participant in an experiment. In these cases, there is little controversy about what the probabilities mean.

## Epistemic probabilities

By contrast, Bayesians tend to be comfortable assigning probabilities not only to whether an event will happen, but also to whether something is true about the world, for example whether someone committed a crime they are accused of, or whether a certain theory of physics is true. Such probabilities can reflect the evidence for, or a person's subjective credence (degree of belief) in a proposition. Uncertainty about what is true is called *epistemic uncertainty*.

If we want to define the probability as an *objective* measure of evidence for a proposition, we need some objective way of arriving at prior probabilities. One classical proposal for how to do this is to start from a "principle of indifference," by enumerating all possibilities and placing equal prior probability on each. However, this proposal runs into objections that it is arbitrary or question-begging (why should all possibilities be equally likely?) and is not even well-defined when the number of possibilities is infinite (as most parameter spaces are).

We can sidestep these issues by adopting the *subjectivist* view, which holds that probabilities reflect a particular observer's personal degrees of belief in various propositions --- as reflected, say, by the odds at which they are willing to place a bet on the truth or falsehood of a given proposition. If the observer in question is rational, in the sense of having self-consistent beliefs about the world, then it is claimed that their degrees of belief in all possible propositions should form a probability measure, and that they should update their beliefs on evidence according to Bayes' rule.

Defining personal probabilities becomes practically difficult when there are many unknowns, as there are for many real-world questions, because it requires us to take a position on the *joint* distribution for all unknowns in the problem. For example, suppose we are analyzing a microbiome data set to study the effect of some treatment on the abundance of thousands of different species with complex taxonomic and ecological relationships to each other. It is hard enough to specify our subjective prior over the possible ways the treatment could affect the abundance distribution for a single species; to come up with a believable *joint* prior distribution over all of these species is more taxing still, and it is difficult to credit that anyone has ever conducted a true subjective Bayesian analysis in such a context.

Ultimately, these different interpretations of probability all have their advantages and drawbacks, and they coexist with each other in statistical practice. While statisticians of fifty years ago had bitter arguments about which interpretation is "correct," nowadays most statisticians take a pragmatic view that the appropriate interpretation depends on the context. Even scientists who have no philosophical objection to talking about subjectivist probabilities may still prefer not to preface their data analyses by statements like "it's my personal opinion that the mass of the Higgs boson is..." On the other hand, consider someone running a small grocery store, who must decide how much inventory of various items to order for the holiday season. There is no need for such a person to justify their business decisions as objective, so it would be wise for them to bring their fuzzy intuitions into the analysis, especially when they do not have much data to go on.

## A coin flipping example

Consider the following class demonstration that seems to show the close relationships between these different sorts of uncertainty. Suppose the professor in a lecture hall brings a coin out from his pocket and asks the class to predict the probability it will land heads (he reassures the students that it is not a trick coin and he is not a sleight-of-hand artist, and he is a trustworthy sort so they believe him). Virtually all students will agree at this point that there is a $50\%$ chance that the coin will land heads, as a matter of aleatory uncertainty.

Now the professor flips the coin in the air, and on the way down he catches it between his hands. He now asks the students what is the chance that it landed heads. Now, there is typically a divide between the students: some will argue that it is still $50\%$ because they haven't learned anything since he flipped the coin (so we are in the same epistemic position as before), while the others will say that the randomness in the system has already been realized, so there is either a $0\%$ or $100\%$ chance, and we just don't know which.

Next, the professor opens his hands and peeks at the coin, but does not tell the students what he sees. He asks again what is the chance that it landed heads. Of the students who previously stuck to $50\%$, some may feel that they can no longer say what the probability is, because evidence has emerged that they have not seen. The subjectivists, however, will be perfectly comfortable admitting that *to them*, it is still $50\%$, even though *to the professor* it has collapsed to $0\%$ or $100\%$.

But how much has really changed, from the students' perspective, since the moment before the professor flipped the coin? Even then, we might have argued that the laws of physics are sufficiently deterministic that the outcome of the coin toss was foreordained. Likewise, even randomization into treatment and control is typically based on pseudo-random number generators that are really deterministic "under the hood." On that view, perhaps aleatory uncertainty is always based implicitly on appeals to (subjective) ignorance.


## Practical considerations

Our philosophical beliefs need not govern our choice of method in any given case: just as dyed-in-the-wool philosophical frequentists may select Bayesian estimators with a view toward minimizing some average-case risk of interest, philosophical subjectivists may prefer to avoid introducing their personal probabilities into a scientific analysis. In addition, it can be mathematically convenient not to introduce a prior, in many problems.

**Example: Nonparametric estimation of the median** Suppose that we observe an independent sample of $n$ continuous random variables from an unknown probability density; that is,
$$
X_1,\ldots,X_n\simiid p, \quad \text{ where } p \text{ is any probability density on } \mathbb{R}.
$$
Suppose furthermore that we are interested in estimating the median $m(p) = \text{Median}(p)$. If we stop here, there is a natural choice of estimator: the sample median, i.e.
$$
\text{Median}(X) = \begin{cases} X_{(\frac{n+1}{2})} \quad&\text{ if } n \text{ is odd}\\ \frac{1}{2}(X_{(\frac{n}{2})}+X_{(\frac{n}{2}+1)}) \quad&\text{ if } n \text{ is even}\end{cases}
$$
This estimator has a lot to recommend it: it's robust to outliers, it's nonparametric, and for large $n$ its distribution is approximately $N\left(m(p), \frac{1}{4np(m)} \right)$. But it is not Bayes estimator for any reasonable prior distribution on $p$.

If we approach this as a Bayesian estimation problem, we cannot stop with specifying the likelihood model: the first step is to define our prior distribution over the *infinite-dimensional* object $p$. If we did manage to specify our true prior, we'd then have to calculate the posterior, which could be a very difficult calculation. At the end of our analysis, if our estimator was not very close to the sample median, we'd probably think we had chosen a bad prior.

---

[Up: contents](index.md) · [Where Does the Prior Come From? →](02-where-does-the-prior-come-from.md)
