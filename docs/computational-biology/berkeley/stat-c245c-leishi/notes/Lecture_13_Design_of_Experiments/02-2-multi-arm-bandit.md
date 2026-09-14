---
title: 2 Multi-arm Bandit
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_13_Design_of_Experiments.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_13_Design_of_Experiments.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Multi-arm Bandit

**Source:** [`notes/Lecture_13_Design_of_Experiments.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_13_Design_of_Experiments.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Greedy search**

The multi-armed bandit problem has been the subject of decades of intense study in statistics, operations research, electrical engineering, computer science, and economics. A “one-armed bandit” is a somewhat antiquated term for a slot machine, which tends to “rob” players of their money. The colourful name for our problem comes from a motivating story in which a gambler enters a casino and sits down at a slot machine with multiple levers, or arms, that can be pulled. When pulled, an arm produces a random payout drawn independently of the past. Because the distribution of payouts corresponding to each arm is not listed, the player can learn it only by experimenting. As the gambler learns about the arms’ payouts, she or he faces a dilemma: in the immediate future one expects to earn more by **exploiting** arms that yielded high payouts in the past, but by continuing to **explore** alternative arms she may learn how to earn higher payouts in the future. Can she develop a sequential strategy for pulling arms that balances this trade-off and maximizes the cumulative payout earned? See the illustrative example in Figure 1.

**Example 1.** _Suppose there are K actions, and when played, any action yields either a success or a failure. Action k ∈{_ 1 _, . . . , K} produces a success with probability θk ∈_ [0 _,_ 1] _. The success probabilities θ_ 1 _, . . . , θK are unknown to the agent, but are fixed over time. Therefore, these probabilities can be learned by experimentation. The objective, roughly speaking, is to maximize the cumulative number of successes over T periods, where T is relatively large compared to the number of arms K._

The “arm” in different applications represents different objectives. For example, in clinical trials, an arm represents a treatment among several therapeutic interventions. Patients arrive at the clinic sequentially and receive different treatment. A success is associated with some beneficial health outcomes. In _online_ advertisement, an arm represent different banner ads that can be displayed on a website. Users arriving at the site are shown versions of the website with different banner ads. A success is associated either with a click on the ad, or with a conversion (a sale of the item being advertised). The parameter _θk_ represents

5


Figure 1: Illustration of multi-armed bandit problems with the slot machine example.

either the click-through- rate or conversion-rate among the population of users who frequent the site. The website hopes to balance exploration and exploitation in order to maximize the total number of successes.

A naive approach shown in Figure 1 to this problem involves allocating some fixed fraction of time periods to **exploration** (figuring out the success rate of each slot machine), and in each such period sampling an arm uniformly at random. Then select successful actions in the next time period. Then one can iterate this procedure multiple times in the hope of finding the most successful action after sufficient long time. This algorithm is also called greedy algorithms. Greedy algorithms serve as perhaps the simplest and most common approach to online decision problems. Suppose at each action step _t_ , we are given _K_ different choices of actions. The following two steps are taken to generate each action:

1. Estimate a model from historical data _Ht−_ 1 = _{_ ( _A_ 1 _, Y_ 1) _, . . . ,_ ( _At−_ 1 _, Yt−_ 1) _}_ , where _At−_ 1 is the action taken, and _Yt−_ 1 is the observed outcome at _t −_ 1 step

2. Select the action _At_ that is optimal for the estimated model, breaking ties in an arbitrary manner. The action _At_ = arg max _k{_ Reward estimated for action k using _Ht−_ 1 _}_

Such an algorithm is greedy in the sense that an action is chosen solely to maximize immediate reward. A shortcoming of the greedy approach, which can severely curtail performance, is that it does not actively explore.

To see its drawback more concretely, suppose there are three actions with mean rewards _θ ∈_ R<sup>3</sup> . In particular, each time an action _k_ is selected, a reward of 1 is generated with probability _θk_ . Otherwise, a reward of 0 is generated. The mean rewards are not known to the agent. Instead, the agent’s knowledge in any given time period about these mean rewards can be expressed in terms of conditional distributions. Suppose, conditional on the observed history, the distribution of rewards is plotted in Figure 2.

6


Figure 2: Illustration of multi-armed bandit problems with greedy algorithms.

The greedy algorithm would select action 1, since that offers the maximal expected mean reward. The algorithm is also likely to avoid action2, since it is extremely unlikely that _θ_ 2 _> θ_ 1. Although there is some chance that _θ_ 3 _> θ_ 1, the agent would need to try action 3, but the greedy algorithm will unlikely ever do that. The algorithm fails to account for uncertainty in the mean reward of action 3, which should entice the agent to explore and learn about that action.

_ε−_ greedy exploration is one method to force the algorithm to explore. It applies the greedy action with probability 1 _− ε_ and otherwise selects an action uniformly at random. Though this form of exploration can improve behavior relative to a purely greedy approach, it wastes resources by failing to “write off” actions regardless of how unlikely they are to be optimal. In the example in Figure 2, we can see that action 2 has almost no chance of being optimal, and therefore, does not deserve experimental trials, while the uncertainty surrounding action 3 warrants exploration. However, _ε−_ greedy exploration allocates an equal number of experimental trials to each action. Though only half of the exploratory actions are wasted in this example, the issue is exacerbated as the number of possible actions increases. Thompson sampling, introduced more than eight decades ago, provides an alternative to dithering that more intelligently allocates exploration effort.

Note that the above part of lecture note for greedy search is largely based on the comprehensive overview of Thompson sampling in Russo et al. (2017).

Let’s now take a pause here. In healthcare, in what kind of applications, do you think multi-arm bandits will be helpful?

### **2.2 Thompson sampling**

Thompson sampling is an algorithm for online decision problems where actions are taken sequentially in a manner that must balance between exploiting what is known to maximize immediate performance and investing to accumulate new information that may improve future performance. As it depends on bayesian statistics, we will first introduce Bayesian analysis in our next class.

7

---

[← 1 Clinical Trial Design](01-1-clinical-trial-design.md) · [Up: contents](index.md) · [References →](03-references.md)
