---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/ob9xgbpvr-s-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/ob9xgbpvr-s-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So the question is, does this depend upon you having discrete binding events? What biological assumptions are we making in this model about whether or not a protein is actually fixed and welded to the genome in a particular location or whether or not it's drifting around? And this might be of particular interest, for example, if we're looking at histones, which are known to slide up and down the genome, and we're immunoprecipitating them. What will this give us?**

**We are making the assumption that we're dealing with proteins that have punctate binding properties, that actually are point binding proteins. And thus what we're going to get out of this, as you'll see, is going to be a single location. There are other methodologies, which I won't describe today, for essentially deconvolving the motion of a protein on the genome and coming up with its middle or mean position while allowing it to move. But today's algorithm is designed for point binding proteins. Good question, OK?**

**All right. So just to be clear, what we're going to do is we're going to initialize everything, such that we'll begin by initializing pi to be 1 over the size of the genome. And at the very end of this, the strength of a binding event will be simply the number of reads assigned to that event by summing up our estimate of g.**

**And the nice thing about this is that because the number of reads assigned to an event, in some sense, is scaled relative to the total number of reads in the experiment, we can algorithmically take our genome and chop it up into independent pieces and process them all in parallel, which is what this methodology does. All right.**

**So let's have a look at what happens when we run this algorithm. So here we are. This is synthetic data. I have events planted at 500 and 550 base pairs. The x-axis is between 0 and 1,400 base pairs. And the y-axis is pi from 0 to 1.**

**So here we go. It's running. And this is one base pair resolution. And it is still running-- and stop. Well, we get sort of a fuzzy mess there, don't we? And the reason we're getting a fuzzy mess there is that we have got a lot of reads we've created, and there are a lot of different genome positions that are claiming some**

19

**responsibility for this, which my friend, Mr. Sparsity, doesn't like, right? We need to clean this up somehow.**

**And let's see what happens when we actually look at actual data. So here is that original data I showed you for the two Oct4 binding events next to the SOCS2 gene. And I'll run the algorithm on these data. And you can see it working away here.**

**And once again, it's giving us a spread of events, and you can see it even beginning to fill in along where there's noise in the genome and stopped here. And it's assigning the probability mass of pi all over the place. It is not sparse at all.**

**So does anybody have any suggestions for how to fix this? We've worked all might. We've got our algorithm running. We thought it was going to be totally great. When we run it, it gives us this unfortunate, smeary kind of result. What could we do? Any ideas at all? Yes.**

**AUDIENCE: Add a prior where most of the reads are.**

**PROFESSOR: Add a prior. You saw the word no prior, a little tip off. Yeah, absolutely, good point. Add a prior.**

**So what we're going to do is we're going to try and add a prior that's going to prejudice pi to be 0 to create sparsity. So we like pi being 0. So we'll add what's called a negative Dirichlet prior, which looks like this, which is the probability of pi there is proportional to 1 over pi to the m raised to the alpha power. And as pi gets smaller, that gets much, much bigger.**

**And thus, if we add this prior, which happens to be a very convenient prior to use, we can force pi to be 0 in many cases. And when we take that prior into account and we compute the maximum a posteriori values for pi, the update rules are very similar, except that what's interesting is that the rule on the left for computing our estimate of g is identical. But on the right, what we do is we take the number of reads that we observe at a particular location and we subtract alpha from it, which was that exponent in our prior.**

20

**And what that simply means is that if you don't have alpha reads, you're history. You're going to get eliminated. So this is going to do something called component elimination. If you don't have enough strength, you're going to get zapped to zero.**

**Now you don't want to do this too aggressively early on. You want to let things sort of percolate for a while. So what this algorithm does is it doesn't eliminate all of the components that don't have alpha reads at the outset. It lets it run for a little while. But it provides you with a way of ensuring that components get eliminated and set to zero when they actually don't have enough support in the read set.**

**So once again, all we're going to do is we're going to add this prior on pi, which we will wind up multiplying times that top equation. We'll get the joint probability of r and pi in this case, and then we're going to maximize it using this EM adaptation. And when we do so, let me show you what happens to our first example that we had.**

**OK, that's much cleaner, right? We actually only have two events popping out of this at the right locations. All right. So that's looking good. And the probability is summed to 1, which we like. And then we'll run this on the Oct4 data. And you can see now, instead of getting the mushing around those locations, what's going to happen is that most of the probability mass is going to be absorbed into just a couple components around those binding events.**

**Now another way to test this is to ask whether or not, if we looked at what we believe are closely spaced homotypic events, in this case, for CTCF, with that prior, we still can recover those two events being next to each other in the genome. And so if we run this, you can see it running along here.**

**Each one of these iterations, by the way, is an EM step. And there you go. And you can see that even from the sparse data you see above-- that's the actual data being used, all those little bars up there, read counts for the five prime ends of the reads-we can recover the position of those binding events. Question, yes.**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: It depends upon the number of reads, but it's somewhere around three or four. I**

21

**mean, if you look at the GPS paper, which I posted, it tells you how alpha is set. Yes. AUDIENCE: Do you use wholesale extract data when you are trying to compute? PROFESSOR: Question, do we use wholesale extract data? I told you all how important it was, and I haven't mentioned it again. We're about to get to that, because that's very important. I'm glad you asked that question. Yes. AUDIENCE: It looks like, along the genome coordinates, each event is only one base pare, but binding is usually more than one base pair. So is that the center of the binding? PROFESSOR: Yes. Well, it's the center of the read distribution function. Whether or not it's the center of the binding of the protein, I really can't tell. OK, great. And I'll just point out that a power of this method is its ability to take apart piles of reads like this and to these so-called homotypic binding events, where you can see where the motif is. And you can see this method will take apart that pile of reads into two independent events, whereas other popular methods, of which there are many for analyzing these type of ChIP-seq data, don't take apart the event into multiple events, because most of them make the assumption that one pile of reads equals one binding event.**

**Now back to our question about wholesale extract. What happens if you get to a part of the genome that looks like this? We're going to go back to our Oct4 data. And we have our Oct4 IP track, which is above, and then our wholesale extract tract is down there on the bottom.**

**What would you say? Would you say those are really Oct4 binding events? Or do you think something else is going on there? If so, what might it be? Any ideas about what's going on here? Yes.**

**AUDIENCE: Regions with a lot of repeats in the genome? PROFESSOR: Regions with repeats in the genome? Yes. In fact, you can see repeats annotated in**

22

**green right there. And as you recall from last time when we talked about assembly, it's very difficult to actually get the number of repeat elements correct. And a consequence of that is if you underestimate the number of repeat elements in the genome and you collapse them, when you do sequencing of the genome and you remap it, you're going to get regions of the genome were a lot of reads pile up, because they're actually coming from many different places in the genome, but they only have one place to align.**

**And these towers of reads, as they're called, can create all sorts of artifacts. So in order to judge the significant of events, what we'll do is a two-step process. First, we will run our discovery pipeline and discover where all the events are in the IP channel without regard to the wholesale extract channel, in this particular case. And then we will filter the events and say which of the events are real in view of the data from the wholesale extract channel.**

**And so the way to represent this is what is the likelihood we would have seen those IP reads at random given the wholesale extract channel? So how can we formulate this problem? Well imagine that we take all of the reads that we see in both channels and we add them together. So we get a total number of reads at a particular location in the genome.**

**If, in fact, they were going to occur at random, we'd be doing a coin flip. Some reads will go on the IP channel. Some reads will go on the wholesale extract channel. So now we can ask what's the probability we observed greater than a certain number of reads on the IP channel at chance, assuming a coin flipping model where we've added the reads together.**

**Another way to view that is what's the chance that we have observed less than a certain number of reads in the wholesale extract channel assuming a coin flipping model? And that will give us a p-value under the null hypothesis that, in fact, there is no binding event and simply what's going on is that we have reads being flipped between the two channels out of a pool of the total number of reads.**

**And if we take that approach, we can formulate it as the binomial in the following**

23

**way. We can compute a p-value for a given binding event using the data from both the IP channel and from the control channel. And the way that we do this is that we look at the number of reads assigned to an event, because we already know that number. We've computed that number.**

**And we take a similar window around the control channel. We count the number of reads in it and ask whether or not the reads in the IP channel is significantly larger enough than the reads in the control channel to reject the null hypothesis that, in fact, they occurred at random.**

**So this is the way that we compute the p-values for events. So once we've computed the p-values for events, we still have our multiple hypothesis correction problem, which is that if we have 100,000 events, we need to set our p-value's cut off and appropriate value. And I think that you may have heard about this before in recitation. But the way that this is done in this system is to use a BenjaminiHochberg correction.**

**And the essential idea is that we take all of the p-values and we organize them from smallest to largest. And we're going to take a set of the top events, say 1 through 4, and call them significant. And we call them significant under the constraint that p- value sub i is less than or equal to i over n, where n is the total number of events times alpha, which is our desired false discovery rate.**

**So this allows us in a principled way to select the events that we believe are significant up to a false discovery rate, which might be, for example, 0.05 for something that's typically used for a false discovery rate. So we've talked about how to discover events, how to judge their significance individually, how to take a ranked list of events from a given experiment and determine which ones are significant up to a desired false discovery rate.**

**The false discovery means that, let's say, that we have 1,000 events that come out. If this false discovery rate was 0.1, we would expect 100 of them to be false positives. So it's the fraction of positives that we detect that we think are going to be false. And we can set that to be whatever we want.**

24

**Now let's talk about the analysis of these sort of data. There's a question up here. Yes.**

- **AUDIENCE: So this randomness, does that correct to the fact that in your previous slide the coin isn't necessarily fair?**

- **PROFESSOR: Oh, the null hypothesis assumed that the coin was fair, that reads could either occur. That in this case, for example, that the reads were either occurring in the control channel or in the IP channel with equal likelihood, assuming because they were coming from the same process, which was not related to the IP itself. They're coming from some underlying noise process.**

- **AUDIENCE: So typically you'd have some fixed number of reads, and so in the IP channel, the bulk of your reads was in your peaks. Then you would have fewer in your--**

- **PROFESSOR: So the question is, how do you normalize for the number of reads and how they're being spent? Because in the IP channel, you're spending the reeds on IP enriched events. In the wholesale extract channel, you're not spending the reads on those, so you have more reads to go around for bad things, so to speak. So what this algorithm does-- which I'm glad you brought it up-- is it takes regions of the genome that are event free, and it matches them up against one another and fits a model against them to be able to scale the control reads so that the number of reads in the IP and extract channel are the same in the regions that are free of events. And so it matches things, so it is 0.5. OK?**

- **AUDIENCE: Even if wasn't 0.5, wouldn't this rank list correct with that? PROFESSOR: No, it would not. Let us suppose that we made a horrible mistake and that we let these events through because our p was wrong. They would have a very large number of reads, and they would be very significant. As a consequence, they would float up to the top of this list as having the lowest p-values, or the most significant, and they would pop through this. So we would report them as binding events, which is not desirable.**

25

**These are all great questions. Any other questions at all? So we've talked about this.**

**The next question you might have would be, you've done two replicates of the same chip. You always want to do two of every experiment, if not three or four. And I know it's expensive, but you don't know where you are if you only do one of something. Trust me.**

**So assuming you've done two experiments that were identical ChIP experiments, and you would like to know whether or not the results between those two experiments are concordant. How might you go about determining this? Does anybody have any ideas?**

**Let me suggest something to you. Imagine that we create two lists-- one for experiment x and one for experiment y. And we're going to put in this list, in rank order, the strongest events and where they occur in the genome. And let us suppose that we are able to match events across experiments when they're in the same location.**

**So what we'll do is we'll say Event one occurs here. Event 13 occurs here and here. Event 9 occurs here and here. Event 10 is matched. Event 11 occurs here. Event 57 occurs here.**

**And these are ranked in order of significance. They're not completely concordant, and they're ranked according to the significance in this particular experiment and this particular experiment. And we would like to know whether or not we think these two experiments are good replicates of one another.**

**Now the nice thing about converting this into a rank test is that we are no longer sensitive to the number of reads or any specific numeric values represented by each one of these events. We're simply ranking them in terms of their importance and asking whether or not they appear to be quite similar.**

**So one way to do this is simply to take a rank correlation, which is a correlation**

26

**between the ranks of identical events in the two lists. And so, for example, imagine in the lower right-hand corner of this slide shows you an example of X and Y values, although there's not really a linear relationship between them, and the Pearson correlation coefficient is 0.88.**

**If we look at the right correlation, which is defined by the equation on the left, which is really simply the correlation between their rank values, the Spearman correlation for rank is 1. They're perfectly matched. So if you want to consider whether or not two experiments are very similar, I'd suggest you consider rank based tests. But we can do even more than this.**

**Imagine that we would like to know at what point along this list things are no longer concordant, that we would like to consider all the events that are consistent among these two experiments. And we assume that there is a portion of the experiment results that are concordant and part that is discordant. And we want to learn where the boundary is.**

**So what we'll do is this. We will look at the number of events that are concordant up to a particular point. Let's see here, make sure we get the parametrization right. So if we have lists that are n long, psi of n of t is the number of events that are paired in the top n times t events.**

**So t is simply the fraction. If is 0.25, that would mean that in the top 25% of the events, the number of events that are paired. Actually, it's the fraction of events. Sorry.**

**So assuming that we had perfect replicates, what we would see would be that psi of n of t would look like this. Yes?**

**AUDIENCE: What is t?**

**PROFESSOR: t is the fraction of the events that we're considering. So this t might be equal to 0.25. If this was 10, then this would be-- oh, sorry. I think this t equal 0.5. If n was equal to 10, this would be the first five events. So t is the fraction. n is the total number of events.**

27

**So if this is t, which is the fraction which goes from 0 to 1, and this is psi of n of t, this would be a perfectly matched set of replicates. A 0.5, 0.5 of the events are matched, which is perfect. Can't do any better than that.**

**So this is simply telling us, as we take larger and larger fractions of our event, what fraction of them are matched up to that point? Question.**

**AUDIENCE: So this assumes that the rank order is important for the correlation, right? The higher rank they are, we expect them to be better correlated. For example, if in the middle they were the best correlated, but not the top or bottom in terms of the ranking, then you might have a weird looking--**

**PROFESSOR: Yeah. The question is, doesn't this assume that we care most about the events up here, as opposed to the events, for example, in the middle. And this analysis is done to consider how many of the top events we take that we think are consistent across replicates.**

**So it starts at the top as a consequence of that assumption. This is the definition of psi n, which is the fraction of the top events that are paired in the top events. It's roughly linear from the point where events are no longer reproducible. And psi prime of n is the derivative of that function.**

**And graphically, if we look at these, we can see that there's perfect correspondence on the left point up to some point. And then the hypothesis of this irreproducible discovery rate is at that point things stop being in correspondence because you've hit the noise part of the event population. and you get to junk. And as soon as you get to junk, things fall apart.**

**And what this methodology does is it attempts to fit the distribution to both the correspondence and the non-correspondence parts of the population, and you get to set a parameter, which is the probability that you're willing to accept something that's part of the junk population of the non-correspondence population.**

**And the way this is used, for example, in the ENCODE project is that all ChIP-seq**

28

**experiments are done in parallel. Event discovery is done independently on them. All of the events from each independent experiment are ranked from 1 to n. And then IDR is done on the results to figure out which of the events are consistent across replicates. And obviously, if you've had a very bad replicate, you get a very small number of events, if any at all. But if you have good replicates, then you get a large number of events.**

**A secondary question is, imagine you had processing algorithm A and processing algorithm B. It might be that processing algorithm A typically gave you more reproducible events than processing algorithm B, that whenever you ran A, you could get much further down this curve before things fell apart. Does that mean that A is necessarily better, or not? What do you think? Would you always pick algorithm A if that was the case? Any insight on this? Yes?**

**AUDIENCE:**

**No, probably, because there's experimental considerations to it.**

**PROFESSOR: Yeah. I would go with [INAUDIBLE] experimental considerations. But the reason you might not pick it is it might be that if algorithm A always gave you the same wrong answers in the same order, it would score perfectly on this, right? It doesn't mean that it's right. It just means it's consistent.**

**So for example, it could be calling all the towers as events, and it could always give you, for every experiment, the same results. In fact, one interesting thing to do is to run this kind of analysis against your experiment, and an outlier shouldn't match your experiment. It should fail. It's always good to run negative controls when you're doing data analysis.**

**So this IDR analysis simply allows you to pick alpha, which is the probability of the rate of repairs for the irreproducible part of the mixture that you're willing to accept. And the way this is used is, as I said, is that here you see different ways of analyzing ChIP-seq data. And the little vertical tick mark indicates how many peaks they get before they can't go any further because they hit the IDR bound alpha. And some methodologies can produce far more events consistently than other methods can.**

29

**So that's just something for you to keep in mind. And I will not have time to present all the rest of this. But I did want to point out one thing to you, which is that the methodology we talked about today is able to resolve where things are in the genome at exceptional spatial resolution, within 20 base pairs genome wide. And it's always run genome wide at single base pair solution.**

**And it can do things like compute for pairs of transcription factors that have been profiled using ChIP-seq, the spacing between them for spacings that are significant. And so you can see that we're beginning to understand the regulatory grammar of the genome in terms of the way factors organize together and they interact to implement the combinatorial switches that' we've talked about.**

**That's it for today. You guys have been totally great. We'll see you on Tuesday for RNA-seq. And have a great weekend until then.**

30

---

[← [LAUGHTER]](04-laughter.md) · [Up: contents](index.md)
