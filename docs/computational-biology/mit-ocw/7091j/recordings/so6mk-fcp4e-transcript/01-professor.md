---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/so6mk-fcp4e-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/so6mk-fcp4e-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So you'll recall last time we were working on protein-protein interactions. We're going to do a little bit to finish that up, with a topic that will be a good transition to the study of the gene regulatory networks. And the precise things we're going to discuss today, we're going to start off with Bayesian networks of protein-protein interaction prediction. And then we're going to get into gene expression data, at several different levels. We'll talk about some basic questions, of how to compare the two expression vectors for a gene, distance metrics. We'll talk about how to cluster gene expression data. The idea of identifying signatures of sets of genes, that might be predictive of some biological property. For example, a susceptibility to a disease.**

**And then we'll talk about a number of different ways that people have developed to try to identify gene regulatory networks. That often goes by the name of modules. I don't particularly like that name. But that's what you'll find in the literature. And we're going to focus on a few of these, that have recently been compared head to head, using both synthetic and real data. And we'll see some of the results from that head to head comparison.**

**So let's just launch into it. Remember last time we had started this unit looking at the structural predictions for proteins. And we started talking about how to predict protein-protein interactions. Last time we talked about both computational methods, and also experimental data, that could give us information about protein-protein interactions. Ostensibly measuring direct interactions, but we saw that there were possibly very, very high error rates. So we needed ways of integrating lots of different kinds of data in a probabilistic framework so we could predict for any pair proteins what's the probability that they interact. Not just the fact that they were detected in one assay or the other.**

1

**And we started to talk about Bayesian networks in this context. Both useful as we'll see today, for predicting protein-protein interactions, and also for the gene regulatory network problem. So the Bayesian networks are a tool for reasoning probabilistically. That's the fundamental purpose. And we saw that they consisted of a graph, the network. And then the probabilities that represent the probability for each edge, the conditional probability tables. And that we can learn these from the data, either in a completely objective way, where we learn both the structure and the probability. Or where we impose the structure initially, and then we simply learn the probability tables.**

**And we had nodes that represented the variables. They could be hidden nodes, where we don't know what the true answer is, and observed nodes, where we do. So in our case, we're trying to predict protein-protein interactions. There's some hidden variable that represents weather protein A and B truly interact. We don't know that answer. But we do know whether that interaction was detected in an experiment one, two, three or 4. Those are the effects, the observed. And so we want to reason backwards from the observations, to the hidden causes.**

**So last time we talked about the high throughput experiments, that directly we're measuring out protein-protein interactions. We talked about yeast two hybrid and affinity capture mass spec-- here listed as pull-downs. And those could be used to predict protein-protein directions, by themselves. But we want to find out what other kinds of data we can use to amplify these results, to give us independent information about whether two proteins interact.**

**And one thing you could look at is whether the expression of the two genes that you think might interact are similar. So if you look over many, many different conditions, you might expect the two proteins that interact with each other, would be expressed under similar conditions. Certainly if you saw two proteins that had exactly opposite expression patterns, you would be very unlikely to believe that they interacted.**

**So the question is, how much is true at the other end of the spectrum? If things are very highly correlated, do they have a high probability of interaction? So this graph**

2

**is a histogram for proteins that are known to interact, proteins that were shown in these high throughput experiments to interact, and proteins that are known not to interact, of how similar the expression is. On the far right are things that have extremely different expression patterns, a high distance. And we'll talk specifically about what distance is in just a minute. But these are very dissimilar expression patterns. These are very similar ones.**

**So what do you see from this plot we looked at the last time? We saw that the interacting proteins are shifted a bit to the left. So the interacting ones have a higher probability of having similar expression patterns than the ones don't interact. But we couldn't draw any cut off, and say everything with this level expression similarity is guaranteed to interact. There's no way to divide these. So this will be useful in a probabilistic setting. But by itself, it would not be highly predictive.**

**We also talked about evolutionary patterns, and we discussed whether the red or the green patterns here, would be more predictive. And which one was it, anyone remember? How many people thought the red was more predictive? How many the green? Right, the greens win. And we talked about the coevolution in other ways.**

**So the paper that, I think, was one of the first to do this really nicely, try to predict protein-protein interaction patterns using Bayesian networks, is this one from Mark Gerstein's lab. And they start off as we talked about previously, we need some gold standard interactions, where we know two proteins really do interact or don't. They built their gold standard data set. The positive trending data, they took from a database called MIPS, which is a hand-curated database that digs into the literature quite deeply, to find out whether two proteins interact or not. And then the negative data they took were proteins that were identified as being localized to different parts of the cell. And this was done in yeast, to where there is pretty good data for a lot of proteins, to subcellular localization.**

**So these are the data that went into their prediction. These were the experiments we've already talked about, the affinity capture mass spec and the yeast two hybrid. And then the other kinds of data they used were expression correlation, one just**

3

**talked about. They also looked at annotations, whether proteins had the same annotation for function. And essentiality. So in yeast, it's pretty easy to go through every gene in the genome, knock it out, and determine whether that kills the cell or not. So they can label every gene in yeast, as to whether it's essential for survival or not.**

**And you can see here, the number of interactions that were involved. And they decided to break this down into two separate prediction problems. So one was an experimental problem, using the four different large scale data sets in yeast from protein-protein interactions, to predict expression. The other one wore these other kinds of data, that were less direct. And they used slightly different kinds of Bayesian networks. So for this one, they used a naive Bayes. And what's the underlying assumption of the naive Bayes? The underlying assumption is that all the data are independent. So we looked at this previously. We discussed how you could, if you're trying to identify the likelihood ratio, and use it to rank things. You primarily need to focus on this term. Because this term will be the same for every pair of proteins that you're examining. Yes?**

**AUDIENCE: Could you state again whether in a naive Bayes, all data are dependent or independent? PROFESSOR: Independent.**

**AUDIENCE: OK.**

**PROFESSOR: OK. So let's actually look at some of their data. So in this table, they're looking at the likelihood ratio that two proteins interact, based on whether the two proteins are essential. One is essential, and one is a nonessential. Both are nonessential. So that's what these two codes here mean. EE, both essential. NN, both nonessential, and any one and the other. And so they've computed for all those protein pairs, how many in their gold standard, are EE, how many are EN, how many are NN? So here are the numbers for the EE. There are just over 1,000, out of the 2,000, roughly 2,000 that are EE. So that comes up with a probability of being essential,**

4

**given that I know that you're positive. You're in the gold standard of roughly 50%, right? And you can assume something similar for the negatives. So these are the ones that definitely don't interact. So the probability of both being essential, given that it's negative, is about 15%, 14%. And so then the likelihood ratio comes out to just under four. So there's a fourfold increase in probability that something is interacting, given that it's essential, then not.**

**And this is the table for all of the terms, for all of the different things that they were considering, that were not direct experiments. So this is the sensuality. This is expression correlation, with various values for the threshold, how similar the expression had to be. And these are the terms from the databases for annotation. And then for each of these, then we get a likelihood ratio of how predictive it is. So it's kind of informative to look at some of these numbers. We already saw that essentiality is pretty weak, predicted the fact that two genes are essential. It only gives you a slightly increased chance that they're interacting than not. But if two things, two genes have extremely high expression correlation, then they're more than a hundredfold more likely to interact than not.**

**And the numbers for the annotations are significantly less than that. So this is a naive Bayes. We're going to multiply all those probabilities together. Now for the experimental data, they said, well, these are probably not all independent. The probably that you pick something up in one two hybrid experiment, is probably highly correlated with the probability that you pick it up in another two hybrid experiment. And one would hope that there's some correlation between things are identifying in two hybrid and affinity caption mass spec. Although we'll see whether or not that's the case.**

**So they used what they refer to as a fully connected Bayes. And what do we mean by that? Remember, this was the naive Bayes, where everything is independent. So the probability of some observation is the product of all the individual probabilities.**

**But in a fully connected Bayes, we don't have that independence assumption. So you need to actually explicitly compute what the probability is for an interaction,**

5

**based on all the possible outcomes in those experiments. So that's not that much harder.**

**We simply have a table now, where these columns represent each of the experimental data types-- the affinity capture mass spec and the two hybrids. Ones indicate that it was detected, Zero is that it's not. And then we simply look again in our gold standard, and see how often a protein that had been detected in whatever the setting is here, in all of them except Ito, how often was it, how many of the gold positives do we get? And how many of the gold negatives? And then we can compute the probabilities.**

**Now it's important to look at some of the numbers in these tables and dig in. Because you'll see the numbers here are really, really small. So they have to be interpreted with caution. So some of the things that might not hold up with much larger data sets. You might imagine the things that are experimentally detected in all of the high-throughput assays would be the most confident. That doesn't turn out to be the case.**

**So these are sorted by the law of likelihood ratio, and the best one is not 1, 1, 1. It's up there. But it's not the top of the pack. And that's probably just the statistics of small numbers. If the databases were larger, experiments were larger, it probably would work out that way. So any question about how they formulated this problem, as a Bayesian network, or how they implemented it? OK.**

**So the results then-- so once we have these likelihood ratios, we can try to choose a threshold for deciding what we're going to consider to be a true interaction and not. So here they've plotted for different likelihood ratio thresholds. On the x-axis, how many of the true positives you get right, versus how many you get wrong. So the true positive over the false positive. And you can arbitrarily decide, OK, well I want to be more-- I want to get more right than wrong. Not a bad way to decide things. So your passing grade here is 50%.**

**So if I draw a line, a horizontal line, and wanted to get more right than wrong, you'll see that any of the individual signals that they were using, essentiality, database**

6

**sanitation, and so on-- all of those fall below that. So individually, they predict more wrongs than rights. But if you combine the data using this Bayesian network, then you can choose a likelihood threshold, where you do get more right than wrong. And you can set your threshold wherever you want. Similarly for the direct experimental data, you do better by combining-- these are light pink lines, than you would with any of the individual data sets.**

**So this shows the utility of combining the data, and reasoning from the data probabilistically. Any questions? So we'll return to Bayesian networks in a bit in the context of discovering gene regulatory networks.**

**So we now want to move to gene expression data. And the primary reason to be so interested in gene expression data is simply that there's a huge amount of it out there. So just a short time ago we passed the million mark, with a number of expression data sets that had been collected in the databases. There's much less of any other kind of high throughput data. So if you look at proteomics or highthroughput genetic screens, there are tiny numbers, compared to gene expression data. So obviously techniques for analyzing gene expression data are going to play a very important role for a long time to come.**

**Some of what I'm going to discuss today is covered in your textbooks. I encourage you to look at text section 16.2. The fundamental thing that we're interested in doing, is seeing how much biological knowledge we can infer from the gene expression data. So we might imagine that genes that are coexpressed under particular sets and conditions, have functional similarity, reflect common regulatory mechanisms, and our goal then, is to discover those mechanisms. So fundamental to this then, any time we have a pair of genes-- and we look at their gene expression data-- we want to decide how similar they are.**

**So let's imagine that we had these data for four genes. And it's a time series experiment. And we're looking at the different expression levels. And we want some quantitative measure to decide which two genes are most similar. Well, it turns out it's a lot more subtle than we might think. So at first glance, oh, it's pretty obvious**

7

**that these two are the most similar. But it really depends on what kind of similarity you're asking about.**

**So we can describe any expression data set for any gene, is simply a multidimensional vector. Where this is the set of expression values we detected for the first gene, across all the different experimental conditions and so on, for the second. And what would be the most intuitive way of describing the distance between two multi-dimensional vectors? It would simply be Euclidean distance, right? So that's perfectly reasonable.**

**So we can decide that the distance between two gene expression data sets, is simply the square root of the sum of the squares of the distances. So we'll take the sum over all the experimental conditions that we've looked at. Maybe it's a time series. Maybe it's different perturbations. And look at the difference in expression of gene A and gene B in that condition, K. And then evaluating this will tell us how similar two genes are in their expression profiles.**

**Well, that's a specific example of a distance metric. It turns out that there's a formal definition for a distance metric. Distances have the following properties. They're always greater than zero. We never have negative distances. They are equal to zero under exactly one condition-- the two data points are the same. And they're symmetric. So the distance from A to B is the same as the distance from B to A.**

**Now, to be a true distance, then you also have to satisfy the triangle inequality, that the distance from x to z is less than or equal to the sum of the distances through a third point. But we will find out that we don't actually need that for similarity measures. So we can have either a true distance metric for comparing gene expression data sets, or similarity measures as well.**

**So let's go back to the simple example. So we decided that the red and the blue genes were nearly identical, in terms of their distance metrics. But that's not always exactly what we care about. So in biological settings, frequently the absolute level of gene expression is on some arbitrary scale. Certainly with expression arrays, it was completely arbitrary. It had to do with fluorescence properties, and how well probes**

8

---

[Up: contents](index.md) · [hybridize to each other. →](02-hybridize-to-each-other.md)
