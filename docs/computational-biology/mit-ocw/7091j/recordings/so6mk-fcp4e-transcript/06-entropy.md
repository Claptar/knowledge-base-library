---
title: entropy.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/so6mk-fcp4e-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# entropy.

**Source:** `recordings/so6mk-fcp4e-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So things with a high mutual information, means that one variable gives the significant knowledge of what the other variable is doing. It reduces my uncertainty. That's the critical idea. OK. So we looked at correlation before. There could be settings where you have very low correlation between two variables, but have high mutual information. So consider these two genes, protein A and protein b, and the blue dots are the relationship between them. You can see that there's a lot of information content in these two variables. Knowing the value of A gives me a high confidence in the value of B. But there's no linear relationship that describes these. So if I use mutual information, I can capture situations like this, that I can't capture with correlation. And these kinds of situations actually occur.**

**So for example in a feed-forward loop-- say we've got a regulator A, and it directly activates B. It also directly activates C. But C inhibits B. So you've got the path on the left-hand sides that are pressing the accelerator. And the path on the right hand side pressing the stop pedal. That's called an incoherent feed-forward loop. And you can get under different settings, different kinds of results, where this is one of those examples.**

**You can get much more complicated behavior. [INAUDIBLE] are papers that have really mapped out these behaviors across many parameters settings. You can get switches in the behavior. But in a lot of these settings, you will have high mutual information between two variables, even if you don't have any correlation, linear correlation between them.**

**A well-publicized algorithm that uses mutual information to infer gene regulatory networks is called ARACNe. They go through and they compute the mutual information between all pairs of genes in their data set. And now one question you have with mutual information is, what defines a significant level of mutual information?**

**So an obvious way to do this, to try to figure out what's significant, is to do randomizations. And so that's what they did. They shuffled the expression data, to**

33

**compute mutual information among pairs of genes, where there isn't actually a need-- there shouldn't be any relationships. Because the data had been shuffled. And then you can decide whether the observed mutual information is significantly greater than when you get from the randomized data.**

**Now, the other thing that happens with mutual information is that indirect effects still apply to degrees of mutual information. So let's consider the set of genes that are shown on this. So you've got G2, which is actually a regulator of G1 and G3. So G2 is going to have high mutual information with G1, and with G3.**

**Now, what's it going to be about G1 and G3? They're going to behave very similarly, as well. So it'll be a high degree of mutual information between G1 and G3. So if I just rely on mutual information, I can't tell what's a regulator and what's a fellow at the same level of regulation. They're both being affected by something above them. I can't tell the difference between those two.**

**So they use what's called the data processing inequality, where they say, well, these regulatory interactions should have higher mutual information, than this, which is just between two common targets in the same parent. And so they drop from their network, those things which are the lower of the three in a triangle.**

**So that was the original ARACNe algorithm, and then they modified it a little bit, to try to be more specific in terms of the regulators that were being picked up. And so they called this approach MINDy. And the core idea here, is that in addition to the transcription factors, you might have another protein that turns a transcription factor on or off. So if I look over different concentrations of the transcription factor, different levels of expression between transcription factors, I might find that there are some cases where this other protein turns it on, and other cases where it turns it off.**

**So here, consider these two data sets. Looking at different concentrations of particular transcription factor and different expression levels, and in one case-- the blue ones, the modulator isn't present at all, or present at it's lowest possible level. And in the red case, it's present as a high level. And you can see that when the**

34

**modulator is present only in low levels, there's no relationship between a target and it's transcription factor. Or when the modulator is present at a high level, then there's this linear response of the target to it's transcription factor. So this modulator seems to be a necessary component. So they went through and defined a whole bunch of settings like this. And then systematically search the data for these modulators.**

**So they started off with the expression data set, genes in rows, experiments in columns. They do a set of filtering to remove things that are going to be problematic for the analysis. They look, for example, for settings where you have-- they had to start with a list of modulators and transcription factors, and they moved the ones where there isn't enough variation, and so on. And then they examine, for every modulator and transcription factor pair, cases where the modulator is present at its highest level, and where it's present at it's lowest level. So when the modulator is present at a high level-- let's say, when the modulator is present at a high level, there's a high mutual information between the transcription factor and the target. When the modulator is absent, there's no mutual information. That's a setting we looked at before. That would suggest that the modulator is an activator. It's a positive modulator.**

**You can have the opposite situation, where when the modulator is present at low levels, there's mutual information between a transcription factor and it's target. When the modulator is present at a high level, you don't see anything. That would suggest that the modulator is a negative regulator. And then there are scenarios where there's either uniformly high information content between transcription factor target, or uniformly low. So the modulator doesn't seem to be doing anything.**

**So we break it down into these categories. And you can look at all the different categories, in their supplemental tables. One thing that's kind of interesting is they assume that regardless of how high the transcription factor goes, you'll always see an increase in the expression of the target. So there is no saturation, which is an unnatural assumption in these data sets. OK. So I think I'll close with this example, from their experiment. And then in the next lecture, we'll look at how these different**

35

**methods fare against each other in the DREAM challenge.**

**So they specifically wanted to find regulators of MYC. So here's data for a particular regulator, SDK 38. Here's the set of expression of tumors where SDK 38 expression is lowest. And a set of tumors where SDK 38 expression is highest. And they're sorted by the expression level of MYC. So on the left hand side, you'll see there's no particular relationship between the expression level of MYC and the targets. In the right hand side, there is a relationship between the expression level of MYC and targets. So having, apparently-- at least at this level of mutual information, having higher levels of SDK 38, cause a relationship to occur. That would be example of an activator.**

**OK. So this technique has a lot of advantages, and allows you to search rapidly over very large data sets, to find potential target transcription factor relationships, and also potential modulators. It has some limitations. Where the key limitations is that the signal has to be present in the expression data set.**

**So in the case of a protein like p53, where we know it's activated by all sort of other processes, phosphorylation or NF-kappaB, where it's regulated by phosphorylation, you might not get any signal. So there has to be a case where the transcription factor itself, is changing expression. It also won't work if the modulator is always highly correlated with its target, for some other biological reason. So the modulator has to be on, for other reasons, when the target is, then you'll never be able to divide the data in this way.**

**One of the other things I think that is problematic with these networks is that you get such large networks, and they're very hard to interpret. So in this case, this is the nearest neighbors of just one node in ARACNe. This is the mutual information network of microRNA modulators that has a quarter of a million interactions. And in these data sets, often you end up selecting a very, very large fraction of all the potential modulators. So of all the candidate transcription factors in modulators, it comes up with an answer that's roughly 10% to 20% of them are regulating any particular gene, which seems awfully high.**

36

**OK. So any questions on the methods we've seen so far? OK. So when we come back on Thursday, we'll take a look at head to head of how these different methods perform on both the synthetic and the real data sets.**

37

---

[← AUDIENCE](05-audience.md) · [Up: contents](index.md)
