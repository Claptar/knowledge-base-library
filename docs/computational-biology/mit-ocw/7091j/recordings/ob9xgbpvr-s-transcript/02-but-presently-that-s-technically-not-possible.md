---
title: But presently, that's technically not possible.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/ob9xgbpvr-s-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# But presently, that's technically not possible.

**Source:** `recordings/ob9xgbpvr-s-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So we'll begin today with a technique that allows us to consider one protein at a time and identify where it occupies the genome. Now there are other kinds of proteins that we can identify in terms of where they are associated with the genome that are not transcriptional regulators, per se. For example, we all know that chromatin is organized on spools called nucleosomes. These nucleosomes are composed of eight different histones that have tails on them, and there can be covalent marks put on these tails. We'll return to this later on when we talk about epigenetics.**

**But I did want to mention today that it's possible to identify where there are histones with specific barks that are present in the genome and what genome sequences they are associated with. So we can look at sequence specific regulators. We could look at a more general epigenetic marks, all using the same technology.**

**And this slide simply recapitulates what we just talked about over here on the lefthand side of the board. But we want to know basically what and where, in terms of these genomic regulators, what they are and where they are in the genome. And today we're going to assume a fairly simple model, which is that regulars that are proximal to a gene, most probably regulated. Although we know in practice, actually, it appears that roughly one third of the regulators that are proximal to a gene actually skip it and regulate a gene further down the genome.**

**It's not really understood very well how the genome folds in three space to allow these transit regulatory interactions to occur. But I'll just point out to you that the simplistic model that proximal binding regulates proximal genes doesn't always hold, especially when we get into mammals and other higher organisms.**

**And as I mentioned, another aspect of this is that certain proteins may need to be modified to become active, and thus there are signaling pathways. You can imagine signaling pathways responding to environmental stimuli outside of cells. These signaling pathways can interact with transcriptional activators and modify what targets they seek in the genome.**

3

**So these sorts of regulatory networks will be talked about specifically in a separate lecture later in the term, but they're extraordinarily important. And a foundational aspect of them is putting together the wiring diagram. And the wiring diagram has to do with where the regulators occupy the genome and what genes those regulators regulate.**

**And in order to do that, we're going to utilize a technique today called ChIP-seq, which stands for chromatin immunoprecipitation followed by sequencing. And we can now reliably identify where regulars bind to the genome within roughly 10 base pairs. So the spatial resolution has gotten exceptionally good with high throughput sequencing, as we'll see, which really is a fantastic era to be in now, because this really wasn't possible 5 or even 10 years ago. And so we now have the tools to be able to take apart the regulatory occupancy of the genome and discern exactly where these proteins are binding.**

**The way that this is done, as I'll describe the protocol to you, in general, and then I'm going to pause for a second and see if anybody has any questions about the specifics. But the essential idea is that you have a collection of cells. Typically you need a lot of cells. We're talking 10 million cells.**

**So for certain kinds of marks, you can get down below a million or even to 100,000 cells. But to get robust signals, you need a lot of cells at present. And all these cells obviously have chromosomes inside of them with proteins that are occupying them.**

**And the essential idea is that you take a flash photography picture of the cell while it's alive. You add a cross linking agent, and that cross links proteins creates bonds between the proteins and the genome, the DNA, where those proteins are sitting. And so you then isolate the chromatin material, and you wind up with pieces of DNA with proteins occupying them, all the proteins. So not just some of the proteins, but all the proteins are non-selectively cross-linked to the genome.**

**You then can take this extract and fragment it. Typically you fragment it by using sonication, which is mechanical energy, which causes the DNA to break at random locations. There are more modern techniques that we'll touch on at the end of**

4

**today's lecture where you could enzymatically digest these fragments right down to where the protein is.**

**But suffice to say, you get small fragments, which you then can immunopurify with an antibody to a protein of interest. So one condition of using this technology is either A, you have a good antibody to a protein that you care about as regulatory, or B, you have tagged this protein such that it has a flag tag, myc tag, or some other epitope tag on it which allows you to use an antibody or other purification methodology for that specific tag. So either you have a good antibody or you have a tag on the protein.**

**One problem with tags on proteins is that they can render the proteins nonfunctional. If they're nonfunctional, then, of course, they're not going to bind where they should bind. And one has to be careful about this, because if you introduce a tag and you have a couple good copies of the protein that are untagged and one copy that is tagged, it's hard to tell whether or not the tagged version is actually doing what you think it does, and one has to be careful.**

**But suffice to say, assuming that you have some way of immunopurifying this protein, you can then use the antibodies to simply purify those fragments that have the protein of interest. After you've purified the protein of interest, you can reverse the cross linking, have a collection of fragments which you then sequence using a high throughput sequencing instrument.**

**Now recall that, in the usually applied protocol, the fragmentation is a random. So you're going to be sequencing both ends of these molecules. For each one, you probably only sequence one end. You're going to sequence an end of these molecules which gives you a sequence tag that is near where the event occurred, but not exactly at it.**

**And we're going to take those tags, and if we have our genome-- here represented as this short, horizontal chalk line-- we'll take our reads, and we will align them to the genome, and try and discern from those aligned reads where the original proteins were binding. Now our job is to do the best possible alignment or discovery**

5

**of where the proteins are binding, given this evidence. So we have a collection of evidence exhibited by the read sequences.**

**The other thing that we will do is we will take the original population of molecules, and we will sequence them as well, sometimes called the whole cell extract sequence, as a control. And we'll see why we need this control a little bit later on. But this is going to be a purified so-called IP for immunoprecipitate fraction, which we'll sequence. And this will be the whole cell extract, which should not be enriched for any particular protein.**

**Now before I go on, I'd be happy to entertain any questions about the details of this protocol, because it's really important that you feel comfortable with it before we talk about the computational analysis of the output. So if anybody has any questions, now would be a great time to ask. Yes.**

**AUDIENCE: I have more of a scientific question. This assumes that we know a transcriptioned factor. Are there are ways, methods to figure out transcription factors so that you can design antibodies to bind to it?**

**PROFESSOR: So the question is, this assumes that we know the regulators that we're interested in ahead of time. And is there a de novo way of discovering heretofore unknown regulators that are binding to the genome? The answer to that question is sometimes, as is usually the case.**

**Later in the term, we'll talk about other methodologies for looking at the regulatory occupancy of the genome that don't depend upon immunopurification, in which case we'll get an understanding of what's going on with the genome at the level of knowing what particular sequences are occupied without knowing what's there. From the sequence, sometimes we can infer the family of the protein that is sitting there.**

**But in general, the holy grail of this, which has not really fully materialized, would be as follows, which is instead of purifying with an antibody and then sequencing, why not purify with a nucleic acid sequence and then do mass spec, to actually take the**

6

**proteins off of the DNA, run them through mass spec, and figure out what's there. And we and others have attempted this. And at times, you get good results. But mass spec is improving greatly, but it's till a fraught process with noise.**

**And there's a paper just published in Nature Methods late last year on something called the CRAPome. Have you heard of this paper before? It is all the junk you get when you run mass spec experiments.**

**And so when you run a mass spec experiment, you can just take all the stuff in the CRAPome out of it, and it actually helps you quite a bit. That gives you an idea what the state of the art of mass spec is. It's a little bit noisy.**

**But I think your question is great. I think we need to get there. We need to get to the place where we can take portions of the genome and run them through mass spec and figure out what is populating it de novo without having to know ahead of time. Any other questions? OK. Great.**

**So the figure on the slide up there also describes the ChIP-seq protocol. And I'll also say that some people believe this would never work. They actually thought that when you did the purification, you would just get so much background sequence that when you map it to the genome, you could never discern any signal whatsoever. And so there are lively debates about this until somebody actually made it work, and then the argument was over because it made everything else completely and totally obsolete. So it wasn't good to be on the wrong side of that argument, I'll tell you that. I wasn't, but all right. I was on the right side.**

**But suffice to say, here's a close-up picture of Mr. Protein-- Ms. Protein-- and what happens when there is breakage around that site, followed by sequencing. And as you can see, the little black lines connecting between the protein and the DNA is supposed to indicate contacts sites. And you can see the little yellow arrows are supposed to indicate breakage sites of the DNA that are being caused by, in this case, mechanical breakage through sonication.**

**And you get reads from both strands of the DNA. Remember that a sequencing**

7

**instrument always sequences from five prime to three prime. So you're going to get the reads on the red strand and on the blue strand, shown here. And when we do the mapping, we know which strand they're mapped on. And the profile is shown in the lower plot, showing the density of map reads versus distance from where we believe the protein is sitting.**

**And the tag density refers to tags or sequence tags or reads that are aligned using the methodology we discussed two lectures ago to the genome we assembled last lecture. So the characteristic shape shown in this picture is something that is not the same for all proteins. It is something that varies from protein to protein. And thus, one of the things that we'll want to do during our discovery of where these proteins are binding is always learn the shape of the read distribution that will come out of a particular binding event.**

**So just to show you some actual data, so you'll get a feel for what we're talking about, this is actual data from the Oct4 protein, which is an embryonic regulator, pluripotency factor, binding to the mouse genome around the SOCS2 gene. And you can see the two distinct peaks on the upper track, both the plus strand reads and the minus strand reads, shown in blue and red respectively. Each one of the black and white bars at the top-- probably can't be read from the back of the room-but each one of those is 1,000 bases, to give you some idea about sort of the scale of the genome that we're looking at here.**

**You can see the SOCS2 gene below. The exons are the solid bars. And then you see the whole cell extract channel, which we talked about earlier. And the whole cell extract channel is simply giving us a background set of reads that are nonspecific.**

**And so you might have a set of, say, 10 or 20 million reads, something like that, for when these experiments that you map to the genome and get a picture that looks like this. So now our job is to take the read sets that we see here, genome wide, and figure out every place that the Oct4 protein is binding to the genome.**

**Now there are several ways that we could approach this question. One way to approach the question would be to simply say, where are the peaks? And so you**

8

**hear this kind of exploration often described as peak finding. Where can you find the peaks? And where is the middle of the peak?**

**Now the problem with this approach is that it works just fine when a peak represents a single binding event. So imagine that these two fingers here are binding events, and they're fairly far apart of the genome. Now as they come closer and closer and closer together, what will happen is that, instead of having two peaks, we're going to wind up having one broad peak.**

**And thus, there's a lot of biology present in this kind of binding of the same protein proximal to itself. So we need to be able to take these sorts of events that occur underneath a single enrichment, or single peak, into two separate binding events. And this is shown in the next couple of slides, right where we look at what we would expect from a single event, in terms of a read enrichment profile once it's aligned to the genome.**

**And we think about a possibility that there are two events, here shown in indiscernible gray and blue and red. And we note that each one of these will have its own specific profile. And then you can consider them to be added together to get the peak that we observe.**

**Now one of the reasons this additive property works is that, remember, we're working with a large population of cells, and regulators don't always occupy a site. And thus, what we're looking at in terms of the reads are the sum of all of the evidence from all of the cells. And so even though the proteins are close to one another, we often can find an additive effect between that proximal binding.**

**So how can we handle this? Well, what we're going to do is we're going to do two key algorithmic things. We're going to model the spatial distribution of the reads that come out of a specific event, as I suggested earlier. And we're going to keep that model up to date.**

**That is, we can learn that model by first running our method using a common distribution of reads, identify a bunch of events that we think are bindings of a single**

9

**protein, take those events and use them to build a better model of what the redistribution looks like, and then run the algorithm again. And with the better distribution, we can do a much better job at resolving events out of multiple events out of single peaks.**

**And the next thing we're going to do is we're going to model the genome at a single base pair level. So we're going to consider every single base as being the center point of a protein binding event, and using that model, try and sort through how we could have observed the reads that we are presented with. And first, the spatial distribution that we build is going to look something like this.**

**And we consider a 400 base pair window, and we learn the distribution of reads, and we build an actual empirical distribution. We don't fit the distribution to it, but rather we can keep an exact distribution or histogram of what we observe, averaged over many, many events. So when we're fitting things, we have the best possible estimate. Yes.**

**AUDIENCE: I was just trying to remember to origin of the [INAUDIBLE] clearly. So within the protocol, are you sequencing with the proteins bound to these fragments?**

**PROFESSOR: No. See, you can't do that. You have to reverse the cross-linking from the DNA. And then there's a step here which we omitted for simplicity, which is, we amplified the DNA.**

**AUDIENCE: So I was just wondering, if there's no protein, why doesn't the polymerase just read through the whole thing from one side? Why is there a peak? There seems to be a loss of signal right where the protein is bound.**

**PROFESSOR: Well, that depends upon how long the reads are and how hard you fragment. And in fact, that can occur. But typically, we're using fairly short reads, like 35 base pair reads. And we're fragmenting the DNA to be, say, perhaps 200 to 300 base pairs along.**

**So we're reading the first 35 base pairs of the DNA fragment, but we're not really all the way through. We could read all the way through if we wanted, but there really**

10

**wouldn't be a point to that. The thing that we're observing here is where the five prime end of the readers, where the leftmost edge of the read is. So even though it might be reading all the way through, we're just seeing the left edge of it. Does that answer your question?**

**AUDIENCE: Yeah.**

**PROFESSOR: OK, great. Any other questions? Yes, at the back. AUDIENCE: So to clarify, this distribution that's being shown up here on both the positive and negative strand--**

**PROFESSOR: Yes. AUDIENCE: This is the position of where the reads started, not the count of the number of times that particular base was shown in the sequencing result. Is that correct? PROFESSOR: Let me repeat the question. What we're observing in the distribution is where the read starts and not the number of times that base shows up in the sequencing data. It is the number of reads whose five prime position start at that base. OK So each read only get one count. Does that help? OK.**

**The other thing that we're going to do, for simplicity, is we're going to assume that the plus and the minus strand distributions are symmetric. So we only learn one distribution, and then we flip it to do the minus strand. And that's shown here, where we can articulate this as this empirical distribution, where the probability or read given a base position is described in terms of the distance between where we are considering the binding of it may have occurred and where the read is.**

**So it's important for us to look at this in some detail so you're comfortable with it. Here's our genome again. And let's assume that we have a binding event at base m along the genome. And we have a read here, r sub n, at some position. The probability that this read was caused by this binding event can be described as probably a read n given the fact that we're considering an event at location m.**

11

**Now of course, it could be that there are other possible locations that have caused this read. And let us suppose that we model all of those positions along the genome as a vector pi. And each element of pi describes the probability or the strength of a binding event having occurred in a particular location. So we can now describe the probability of a read sub n given pi is equal to the summation where i equals 1 to big M, assuming that there is 1 to M bases in this genome, of a p rn given m pi m, like this.**

**So we are mixing together here all of the positions along the genome to try and explain this read. So the probably of the read, given this vector pi, which describes all the possible events that could have created this read, is this formulation, which considers the probability of each position times the probability that an event occurred at that position subject to the constraint that all of a pi i's sum to 1. So we're just assigning probability mass along the genome from whence all of the reads originally came.**

**So this is considering a single read, r sub n, and where that might have originated from. Yes.**

**AUDIENCE: Does the constraint basically state that only one event occurred in this fragment point?**

**PROFESSOR: The question is, does this constraint imply that only one event occurred? No. The constraint is implying that we're going to only have one unit of probability mass to assign along the genome which will generate all of the reads. And thus, this vector describes the contribution of each base to the reads that we observe.**

**So let us say simplistically that it might be that there are only two events in the genome, and we had a perfect solution. Two points in the genome, like m1 and m2, would have 0.5 as their values for pi. And all the other values in the genome would be 0. We're going to try to make this as sparse as possible, as many zeroes as possible.**

**So only at the places in the genome where protein is actually binding will pi i be**

12

**nonzero. Does that make sense? These are great questions. Yes. And if people could say their names first, that would be great. Yes.**

**AUDIENCE: Sara. Just to clarify, the pi vector is completely empirical?**

**PROFESSOR: This distribution is completely empirical. Yes, that's right, Sara, completely empirical. I'll also say, just so you know, that there are many ways of doing this kind of discovery, as you might imagine. The way we're going to describe today was a way that was selected as part of the ENCODE 3 pipeline for the government's ENCODE project.**

**And so what I'm going to talk about today is the methodology that's being used for the next set of data for ENCODE 3 followed by IDR analysis, which is also part of ENCODE 3. So what you're hearing about today is a pipeline that's being used that will be published next year as part of the ENCODE project.**

**These papers, this method's been published. But the analysis of all the Encyclopedia of DNA Elements-- which is what Encode stands for-- the third phase of that is utilizing this. OK, any other questions? Yes.**

**AUDIENCE: Does the shape of this binding event tell you anything about the topology of the actual protein?**

**PROFESSOR: It does, actually. And we'll return to that. But the shape of this binding can tell you something about the class of protein, which is still an area of active research. But also note that that is a little bit confounded by the fact that when you have homotypic binding, which means you have these closely spaced binding events, you get these broader peaks. And so there's a lot of research into what the shapes on the genome mean and what biological function of mechanism they might imply. Yes.**

**AUDIENCE: Can you explain pi one more time?**

**PROFESSOR: Yeah, explain pi one more time, sure. So pi is describing where there are binding events along the genome. So for example, if we just had two binding events, m1 and m2, then pi of m1 would be equal to 0.5, and pi of m2 would be equal to 0.5,**

13

**and all the other values of pi would be 0. So we're just describing with pi where the events are occurring. That gives us the location of the events. OK?**

**And you'll see in a moment why we articulated it that way. But that's what pi is doing. Does that answer your question? OK. Any other questions? Yes. AUDIENCE: In cases when you have two peaks really close together, to a point that there's some sort of [INAUDIBLE] between, how do you constrain your pi? PROFESSOR: How do you constrain the pi when you have closely spaced peaks? AUDIENCE: Yeah. PROFESSOR: Well, you don't constrain it. You actually want-AUDIENCE: [INAUDIBLE] PROFESSOR: Well, I'm going to show you some actual examples of this algorithm running. So I'm going to give you an animation of the algorithm running, so you can actually watch what it does. And you'll see, first it's going to be something that isn't too pleasant, and then we'll fix it.**

**But the key thing here is sparsity. What we want to do is we want to enforce pi being as sparse as possible to explain the data. One of the common problems in any approach to machine learning is that, with a suitably complex model, you can model anything, but it's not necessarily interpretable.**

**So what we want to do here is to make pi as simple as possible to be able to explain the data that we see. However, if a single event cannot explain and observe redistribution at a particular point in the genome, we'll need to bring another event in.**

**All right, so that is how to think about a single read. And now we can just say the probability of our entire read set given pi is quite simple. It's simply the product over all the reads. Sorry. Like so.**

14

**So this is the probability of the entire read set. So we had this previously, which is the probability of a single read. And we take the product of the probability for each individual read to get the likelihood of all the reads.**

**So now all we need to do to solve this problem is this. We need to say that pi is equal to the arg max pi of P R pi, which gives us the maximum likelihood estimate for pi. Now it's easy to write that down, just find the setting for pi that maximizes the likelihood of the observed reads, and proof, you're done, because now you've come up with a pi that describes where the binding events are along the genome at single base pair solution, assuming that pi is modeling every single base. Does everybody see that? Any questions about that? Yes.**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: n is the number of reads. m is a number of bases in the genome. n is the number of reads.**

**AUDIENCE: The length of pi, right? Is that equal to the number of binding events? Or is it equal to just the number of [INAUDIBLE]?**

**PROFESSOR: The length of pi?**

**AUDIENCE: Yeah.**

**PROFESSOR: It's the number of bases in the genome, and hopefully the number of bindings is much, much, much smaller than that. Typical number of binding events is 5 to 30,000 across a genome that has 3 billion bases, something like that. So it's much, much smaller. OK?**

**So this is what we would like to solve. And another way to look at this model, which it may be somewhat more confusing, is as follows, which is that we have these events spread along the genome. And we have the reads shown on the lower line. And the events are generating the reads.**

**So this is called a generative model, because the derivation of the likelihood directly follows from, if we knew where the events were, we could exactly come up with the**

15

**best solution for the assignment of pi, and thus for the likelihood. So this is what we have on the board over here. But we can solve this directly. Yes. Question in the back.**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [AUDIENCE →](03-audience.md)
