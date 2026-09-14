---
title: influenced by the student's school's grade inflation policies.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/c95294-vvqy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# influenced by the student's school's grade inflation policies.

**Source:** `recordings/c95294-vvqy-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**AUDIENCE: But wouldn't the grades be influenced by the--**

**PROFESSOR: But the grades would be. That's right. So some of the variables I can remove and others-- some of the joint probability statements I don't need to worry about and others I do. And which ones I need to consider is determined by the graph structure. Yes. AUDIENCE: How is the graph structure determined?**

**PROFESSOR: OK. So how is the graph structure determined? So it's determined in one of two ways. I can draw it in advance because I believe that I know something about my setting, I believe that these data are independent. Then it has that structure like this. Cause and a bunch of independent effects.**

**Or perhaps I claim to know that actually two of these things have a common parent as well. In some cases I know. We'll also talk about how to learn the structure from the data, which is the more common setting in regulatory networks. So in these kinds of problems when trying to decide how to integrate different proteomic data sets, typically people make arbitrary decisions about what the structure is based on their knowledge of the system.**

**But if you're trying to figure out de novo which proteins interact with which, which proteins regulate which genes, then you have to learn it from the data. And we'll talk about how to do that in a second. Great questions. Any other questions? Anything in the quiet half of the room?**

**OK. So as I said, this part of it, I think you can usually come up with cases that give you fairly good intuition. One of the things that is true in these Bayesian networks which most people find a little bit surprising at first is something called explaining away. So let's look at this Bayesian network.**

**I go outside and I detect that things are slippery on the grass. So that could be for a lot of reasons, but one possible reason is that the grass is wet. OK. What are the**

28

**causes of the grass being wet? Well, it could have rained or the sprinklers might have been on.**

**And depending on this as an example-- so a lot of the Bayesian networks were developed in Stanford by Judea Pearl and colleagues. And of course, in California it doesn't rain that often. So there the season is a strong determiner of these things. Not so much around here.**

**So in this example that they like to do, so does the probability that it's raining depend on whether the sprinkler is on or not? Now, the answer should be no, right? I mean, in reality, when you think about-- there's no causal relationship between the sprinkler being on and the rain. But in fact, when we're reasoning over these networks, we actually are influenced.**

**In a probabilistic model, if I know that it's raining, and I know the grass is wet, then what do I think about the sprinkler being on? Do I think it's just as likely? No, I think it's less likely, right? If I go outside and see the grass is wet, there are clouds, the rain is coming down, is the sprinkler likely to be on or not? It's likely to be off, right?**

**So there's no causal relationship, but there's the probabilistic relationship through the graph structure. And that's called explaining away. And you can take a whole course on how to understand which relationships you can detect and which not. This is not the place to try to go into that, but I hope you'll be familiar with this problem. And I'll try to give you a toy example that makes it a little bit more obvious in terms of the equations where this comes from.**

**So imagine this very silly game where we play, we toss coins. We toss a coin twice. And if it turns up heads both times, you get a point. If it turns up tails both times, you get a point. But if one's a head and one's a tail, you don't get any points.**

**Now, does the probability that I tossed a head on the first time depend on whether I toss a tail on the second time? So causally, obviously not, right? First of all, it happened earlier in time. And secondly, the coin tosses are completely independent.**

29

**But what happens when I know the outcome? What if I know what score you got? So if I know your score, then is the probability that I tossed the heads on the first time independent of whether I got a tail on the second time? What do you think? How many people think it is independent then?**

**How many people think it's not independent. Very good. It's not independent. And obviously, here's the math to prove it, but your intuition does the same thing. So what's the probability that I tossed a head on the second time given that I got a one, I scored, and I tossed a tail on the first time? Obviously, it's zero, right?**

**So here's the probability of getting a head in the first time and scoring one, and tails on the second time is exactly zero. So that's called explaining away. You can reduce your belief in certain parents based on what you know about the children. Think of this coin toss example or the rain in California and the sprinklers.**

**All right. So as this come up several times, how do we obtain the Bayesian network structure? There are two problems that we need to be able to solve. We need to be able to learn the structure, and we need to be able to learn these probability tables.**

**If we know structure, how do we get the probabilities? Well, we need to identify some objective function we're going to try to optimize, and then choose values for all probability distributions that optimize that objective function. And that's the kind of thing we've been doing all along, just like in the Gibbs sampler. We need some objective function or protein structure. We need some objective function that we're going to try to optimize.**

**So there are two common ones that are used a lot. There's maximum likelihood and the maximum posterior. So maximum likelihood is defined as the set of param-theta is all the parameters, all the probability distributions, the probability of getting a score of one given that you had heads and tails, whatever it may be. The probability of getting admitted given that you had certain GREs and certain grades.**

**So we want to find the set of parameters, all those probability distributions, that maximize this. The probability of the data, our training data, given those**

30

**parameters. That's a pretty obvious one.**

**And the maximum posterior includes some of our beliefs about the prior probability of the data and the prior probability of the parameters. This is a little bit less intuitive because you have to ask, well, where do those numbers come from? And that, again, is a whole course unto itself.**

**OK. Now, how do you find these parameters? Again, it's the kinds of search problems that we've looked at before, various kinds of hill climbing. So gradient descent, expectation maximization, Gibbs sampling, which you've looked at explicitly. And again, the full details of how to do that are outside of our scope today.**

**OK. So in our example of this coin toss game, we would use one of these two functions to try to decide what's the probability of getting heads or tails for any given score. That's what the kinds of parameters are.**

**Now, the structure problem actually turns out to be really, really hard, because there are a very exponentially large number of potential structures to draw from. And unless you've got some prior knowledge, it can be impossible, depending on how much data you have, to actually build this structure.**

**So there are many algorithms that have been proposed. And a lot of our settings, we're going to use some kind of prior knowledge to reduce the search space. So if we're trying to talk about transcriptional regulatory networks, it's very common to assume that there are only some kinds of nodes that can be causes and other kinds of nodes that can be effects, right?**

**So in gene expression it would be effect, and then you would limit your causes to only be transcription factors. It would generally be signaling molecules or something like that, and not allow all 20,000 genes to be causes and all 20,000 genes to be effects.**

**So there are lot of resources to learn more about Bayesian networks. As I said, you can have whole courses on this. I think there are a lot of good tutorials at this website. I've also put in the notes a little toy example for you to work through all the**

31

**probabilities, which I think, in the interest of time, we won't go through in detail.**

**All right. So to motivate what we're going to do in the next lecture, I just want to talk about other kinds of data that you could bring to bear on this problem of predicting which proteins interact. We'll see, then, how that gets fed into an interaction Bayesian network to make the predictions.**

**So we've talked about affinity capture and two-hybrid, but what other kinds of data could we use to predict the probability interaction? Well, one thing you could use would be gene expression data. And the idea is that if two proteins interact, they should be present in the cell at the same time, right?**

**So we talked about this a little bit. If they're anti-correlated, it seems very unlikely they interact. What about if they're correlated, but not perfectly correlated? So here's a plot that shows a histogram of proteins that are known to interact, proteins that are known not to interact. So empty circles are known interacting proteins, the dark circles are non-interacting proteins, and the other ones are based on the experimental data.**

**And the distance here is the difference between expression profiles. And we'll talk in coming lecture about exactly how to compute distance between expression profiles. But the further to the right it is, the less similar the expression profiles are across large data sets. So what you see is the interacting proteins tend to be shifted more to the left, more similar expression profiles than the non-interacting ones.**

**But what do you notice about this? There's no way to draw a line and say, everything to the right of this is in one class and everything to the left is another, right? So by itself, it's not going to get us very far. There are plenty of noninteracting proteins that have very highly correlated gene expression and plenty of interacting proteins that have poorly correlated gene expression. So it's a trend, not a rule.**

**Now, what about evolution? So if I look over many, many organisms, I might expect what? The proteins that interact with each other are going to appear in the same**

32

**species, right? So let's look at these two cases. We've got a bunch of-- eight different genomes. And I've got gene 1 and gene 2, which I suspect might interact, and gene 3 and gene 4, which I suspect might interact.**

**Now, looking at these two patterns of evolution, which one do we have more confidence in that it interacts? The red one or the green one? So what do we notice about the difference between them? What's true of the red one compared to the green one? Yeah.**

**AUDIENCE: The red one is only in one branch of the tree.**

**PROFESSOR: The red one is only one branch in the tree and the green one is scattered across. So let's take a vote. Do we believe that the red one is better evidence of interaction or the green one is better evidence of interaction? Red? Green? Can I have an advocate of green. Someone explain their rationale? Anyone in the quiet side of the room? All right, Ed. AUDIENCE: Because red is only on one branch of the tree, I'd expect that they're naturally more correlated with each other. They have less-- they appear together in [INAUDIBLE] so I'd expect [INAUDIBLE].**

**PROFESSOR: OK. So the argument is that red only occurs in one part of the tree. And so there could be a very simple explanation for all the reds being in one part of the tree and one not, which would be a single loss and gain event. Right? Somewhere early on, perhaps here, I gain those two proteins. And then they're inherited throughout the genome, like most of genes get inherited throughout the genome. Whereas here, we've got independent events of gain and loss. And at each one of these independent events, we're getting them moving jointly, either in or out of the genome. So there's more evidence for green to be interacting than red. Everyone buy that? Even some of the advocates of red? Questions? Yes. AUDIENCE: Could there be a way of either objectively or mathematically [INAUDIBLE] that way, or is it just the reasoning [INAUDIBLE]?**

33

**PROFESSOR:**

**One can do the statistics on it with known ones, right? I think that's probably the best way. And we'll actually see that in one of these papers that uses-- well, actually, now I don't recall whether they use this co-evolution. But yeah, there are plenty of papers that actually have done the statistics on that. So it is supported.**

**And a related kind of question is what's called the Rosetta Stone approach. Unfortunately, of the term Rosetta gets used far too much in computational biology. So this has nothing to do with the other Rosetta that we've been talking about. And this has to do with how often you find the same pair of genes in the same genome versus split up in different genomes. OK.**

**So what we're going to look at next time then is an approach that combines these kinds of data with the protein interaction physical measurements through the twohybrid and the affinity capture mass spec that actually uses the Bayesian networks we talked about this time to predict whether two proteins are likely to interact based on all of the available data. These evolutionary arguments, the [? sentiality ?] arguments, and then the interaction data. Any final questions? OK, see you next time.**

34

---

[← and the two-hybrid. Questions on those technologies? Yes.](04-and-the-two-hybrid-questions-on-those-technologies-yes.md) · [Up: contents](index.md)
