---
title: here, and it bleached.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/dp4nqipuh6w-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# here, and it bleached.

**Source:** `recordings/dp4nqipuh6w-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**But what they're really asking is at the beginning, how many fluorescent proteins did I see? And I think the camera actually maybe was collecting still during that bleaching step. It's just that it wasn't kind of part of it. Their analysis is in some ways really just based on this. Or in other experiments, you can go look to confirm that it bleaches single step here.**

**OK. So we spent a long time talking like the general idea of how to design these experiments and so forth. I'm not going to say very much about the design of the experiments, except that they did a number things. They used this Venus protein that has a faster maturation than traditional GFP.**

**They also targeted it to the membrane, not by putting Venus into the membrane-that would be tricky, I think-- but rather by attaching the Venus protein to another protein that is put in the membrane. And indeed, this TSR membrane protein, we're going to be talking about it in a couple of weeks when we're discussing the chemotaxis network that is in E. coli for how E. coli find food and so forth.**

**I think that in reading these papers, it's interesting. Sometimes, authors make kind of a side comment that just illuminates kind of how difficult everything was. And I think that they had a nice one in here, where they said that they were checking with TSR to make sure that the behavior of the TSR Venus and just Venus were similar in terms of the amount of fluorescence.**

**And then, they say, no notable difference was observed, indicating that the introduction of the TSR sequence does not change the yield of Venus production, which is not the case for many other membrane targeting sequences that we tested.**

**So this is like, a little add-on onto the sentence that is like, I mean, six months of somebody's life was dedicated to trying-- you can just imagine all the over coffee, their frustration. They tried all of these different things, and they always got-- and for an awful lot of these things, I would have still been very much interested in the study, even if the addition of TSR did change the kinetics. Because I think that still is**

25

**very interesting.**

**But they really wanted this to be just airtight, or maybe the referees need to be-- I don't know. But you can tell that they just went to a lot of work to try to find the thing where everything would be just right. Now, once they kind of described their setup, they had this wonderful paragraph, I think. They say, oh, these proteins, they're generating bursts, and the number in the bursts varies, and there's spread, and so forth.**

**And they very nicely tell us, with this data, we can ask four questions. And they say, do these gene expression bursts occur randomly in time? That's going to be yes. How many mRNA new molecules are responsible for each gene expression burst under the repressed conditions? One.**

**What is the distribution of the number of protein molecules in each burst? It's going to be geometrically distributed. And what is the origin of the temporal spread of the individual bursts? And now, I think that this is nice, just to give a reader a kind of like, heads up of where we're heading.**

**And the origin of the temporal spread is actually-- they're arguing is actually the Venus maturation time. So in that case, the fact that there's a finite time for maturation of the Venus ends up allowing them to measure the bursts in an interesting way.**

**Before we get into the details of that, though, I want to make sure that we're all clear about what they mean by a burst. Because this is something that is oddly-- it feels like it's the most trivial statement ever. But I think what we're going to find is that there's a lot of confusion about it.**

**This is a question, how is it that you go from the data to the quantities that they plot and that they're interested in? We want to get a sense of how many proteins are made in each one of these bursts? And so they have in Figure 3B, they plot the number of protein molecules produced. Number of proteins produced. It's a function of time.**

26

**And they have these things. And This was a cell division event. And here they say, we have 2, 4. And here at 25 minutes, we have this thing here, and it looks like. And then this thing goes on. And there's 50, we have another, and so forth.**

**This is a zoom in of Figure 3B, the top panel. So what I want to know is, what is the size of the first burst?**

**So you can either look at my beautifully drawn illustration, or you can look at the paper in front of you. So this is a paper analyzing the size distribution of protein bursts observed in living cells. Right? That's the point of this paper. Now, the question is, from the data they're collecting, we want to know what is the size of the protein burst? The first protein burst.**

**Now, there's no calculation for you to do. There's not much of one. So I'm not going to give you maybe anymore time to figure this out. So let's see where we are. Ready? Three, two, one.**

**All right. So we got at least a majority of the group is saying that it's indeed 3. Now, the issue here is that the weight of the experimental design is working so that every three minutes, what we're asking is, how many Venus molecules kind of folded in that previous three minutes? And then, any of them that there are, we count, and then we kill them.**

**And then, the next. And indeed, what happened here is that every three minutes, they're asking this question. No proteins. And then here, they see one. Now, that's not yet a protein burst. That's maybe a protein verse. But it could be that we're in the middle of a protein burst. And indeed, what we see is that the next time point, the next three minutes, we see, oh, actually, now there's two new proteins that were produced in that next three minutes.**

**So indeed, this whole thing is a protein burst. So we got 1 plus 2. So that was the calculation I was referring to. And so what they're plotting is the distribution of these different protein burst sizes. Now, this is a small protein burst. They see some that get up to be 10, 15. And that corresponds to some of these cases, where they see**

27

**something that looks, for example, more like-- yeah, question?**

**AUDIENCE: [INAUDIBLE]. PROFESSOR: Yeah, right. AUDIENCE: [INAUDIBLE]. PROFESSOR: Yes, exactly. And ultimately, first of all, the number of protein bursts per cell cycle, per hour in these conditions, is of order one. And then the width, the time, of a protein burst is five, seven minutes. Something like that typically. So this gives you a sense of how frequently they will overlap. And indeed, what you expect from this is that 15% of them are actually that they see as one burst might actually have been two though. It's also worth mentioning that-- right. So what I just said is in the model, where you know that it's always just one mRNA that is produced each time, what they say is they think is that the promoter is tightly repressed by the Lac repressor.**

**Ever now and then, the Lac repressor falls off, and it's going to bind again. But some fraction of that time, when the repressor unbinds, you get the RNA p binding, and then you get a transcription event.**

**And I think that in general, it is just one mRNA that is produced there. So just a single RNA polymerase bound, and made an mRNA. But I'm sure that some fraction of the time, it was actually two that were produced during that time. And those would certainly show up as one protein burst. Right? Because the lifetime of the mRNAs in this situation is of order what?**

**Yeah. It was, I think, one and a half minutes maybe? It was short. Yeah. One and a half minutes. What that means is that on this time scale, if there were two mRNAs produced, they would look like the same mRNA.**

**But from this data what they conclude is that there's typically only one mRNA produced in each protein burst, and there's not that many protein bursts per hour of the cell division, so they won't overlap too much. But it's going to happen at some**

28

**rate. All right.**

**What they see is that the distribution of the protein bursts-- we said it was roughly one per cell division time, which they found was 55 minutes here. And they found that the number of protein bursts per cell cycle was distributed Poisson**

**So let me write this down somewhere. The number of protein bursts per cell cycle. So this was distributed as a Poisson with mean [INAUDIBLE] lambda of around 1. 1.2. They call this n cycle. So I'll be consistent. So this n cycle to the 1.2.**

**Now, you guys-- the Poisson is a distribution that we're going to be spending a lot of time thinking about. So the normal way that we write it is that if it's the probability of observing some number n-- and this is a number n bursts per cycle in this case, p of n. We normally write it as a function of the mean lambda, where it's lambda to the n over n factorial.**

**And then for normalization, we have to write e to the minus lambda here. We're going to spend a lot of time thinking about the Poisson next class. So I would say that if it's been a while since you've thought about probability distributions, then you should play via textbook, Wikipedia, whatnot, with the Poisson, the exponential, the geometric, and also the gamma distributions. Because we're going to be using those in the next class.**

**Now, in this distribution, what it basically ends up being is that sometimes, you see zero bursts. Sometimes you see one. Every now and then, you see two. It's kind of what this means.**

**There's one other thing that is, I think, a bit tricky often, which is how they calculated that it was typically one mRNA that led to each of these proteins bursts. Can somebody remind us kind of experimentally what they had to do in order to get at that?**

**The average RNA per cell, right. Right, so they did this RT-PCR. So what they did, they reverse transcribed. They converted the mRNA into DNA, and they amplified to**

29

**get a sense of how much mRNA there was. And from that, the formula, when you first look at it, it feels kind of mysterious, or something like that.**

**But it's one of those things that you just have to keep track of like, units and so forth. So you can basically think about the number of mRNA. And this is indeed, this is per cell. But cell, this doesn't have units, right? But if we wanted the expectation value, the number of the mRNA that's going to be per cell, well, that's going to be given by the number of the mRNA per burst, times the number of bursts per unit time.**

**So this is some rate burst, and then also times the lifetime of the mRNA. Now in this formula, there's also the added factor, where they have like, the time of the cell cycle. But that's just because this could have been bursts per minute, lifetime of mRNA minutes.**

**But then, if you want to put in the extra term, then you have to say, oh, the cell cycle is 55 minutes. So then you have to do that conversion of time into the proper units. So that's what ends up happening.**

**Are there any questions about what happened here? Now, what we're going to do next lecture is kind of go through a simplified model of gene expression, where there's just some rate of mRNA formation, mRNA degradation, the mRNA makes protein, proteins get degraded. And then in that model, we want to try to understand how everything is distributed.**

**And we're going to relate that back to some of the experimental data in this paper. In particular, for example, this geometric distribution of protein burst sizes is something that you expect from the most basic simple model that you would have written down. So from that same point, it's not a surprise. It is often assumed this thing should be geometrically distributed, and it was. And that's wonderful.**

**From my standpoint, I think that even things that we assume to be true, we should still check to see if they are true. And in other cases, they may not be, and so forth. Are there any questions about this paper? No? OK. Then I will see you our next class.**

30

---

[← [STUDENT CHATTER]](05-student-chatter.md) · [Up: contents](index.md)
