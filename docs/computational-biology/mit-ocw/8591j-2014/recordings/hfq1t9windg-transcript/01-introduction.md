---
title: Introduction
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/hfq1t9windg-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/hfq1t9windg-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**MITOCW | watch?v=hfq1T9windg**

**The following content is provided under a creative commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: So today the basic idea is to try to understand the toggle switch. How such a thing can be made, why it represents a memory module. But then we'll relatively quickly get into two themes that are going to be useful throughout the rest of the semester. First is these dimensionless equations that often pop up in the analysis of these gene circuits. And it's absolutely essential that you understand how to get to the dimensionless equations, and also what these parameters end up meaning.**

**And then we'll, at the end, talk about stability analysis. How is it that you can determine whether a particular set of interacting pieces in a cell or in an ecosystem whatnot-- once you get it in the form of an equation, how's is it you can determine whether a particular fixed point or a particular location is going to be stable to perturbations? This is going to be useful for us to determine where the gene network is going to kind of move towards. Also it'll be useful for us to determine whether a gene network is going to oscillate. And later, it'll be relevant in the context of predator prey oscillations, and a bunch of things.**

**So can somebody maybe explain briefly the idea of the toggle switch? Yes, please.**

**AUDIENCE: You have these two genes that repress expression to each other. So when one of them is large, the other one is not expressed. [INAUDIBLE].**

**PROFESSOR: Perfect. So you'll have two genes that are going to mutually repress each other. So in this case, each of them will be a transcription factor of some sort that will bind to the other promoter and repress it. So there are various levels of abstraction that we might use to describe such things.**

**So we might, for example, just say A repressing B, B repressing A. Of course when**

1

**you write it that way, it doesn't have to be in the context of a gene network. This A's and B's could just be chemicals, they could be species eating each other. It could be almost anything.**

**Now in this framework, to get a basic sense of why this thing might have two alternative stable states, is that often we like to take the Boolean approximation. This thing will not always work, but it's a useful thing to do to just kind of first get a sense of what might possibly be happening. So we might say, 0 corresponds to some sort of low. 1 might correspond to high.**

**And of course, these things have to be put it in quotes, because we haven't specified what we mean by this. But it's useful to just make sure that we're all thinking about the same things. And then in the context of A and B, we can just say, well, there's a number of different states it could possibly be in. And you can ask whether this assignment of logic values keeps everybody happy.**

**And so you might ask, well, is 0, 0 a mutually happy state? And of course then you have to say well, if you're in the 0 state, you're not repressing the other guy, but maybe 0 is sort of your equilibrium anyway. So what we have to do is we have to make the assumption that when you're not being repressed, in that case the promoter will be actively making that protein. So then you'll go to some sort of high or 1 state. So in that case, you say, if you start out with both repressed, maybe both of them should start trying to increase their levels. So this, in some ways, is not a stable state.**

**Similarly here, this is also not a stable state. Because in this case, they're both going to be trying to repress one another. So then they'll both start coming down and then the situation may resolve into one of these two. So this is just where either A or B is on, and repressing the other one.**

**And so for example, in context of the repressilator, on Thursday, this is just a useful way to start imagining how this A repressing B, repressing C repressing A-- how such a loop can lead to oscillations. This kind of analysis does not at all prove that there are oscillations in any given manifestation of this thing. But it's useful to just**

2

**make sure that you're roughly getting the idea of what the system might be doing.**

**Now in many cases, we'll want to be a little bit more explicit, and draw the gene network in more detail. And there are multiple manifestations of the Thomas Switch. There are many of them that have been made. So the important thing is not too necessarily keep track of exactly what the components are, but in one case for example, we might have A corresponding to something here. It's coming back and repressing again.**

**Expression of this B. And this might all be on one piece of DNA. Whereas this B here will come back and repress A.**

**Now one thing that is-- and I just want to mention here, they also have a GFP. And this actually is a case where those two can be expressed off of a single promoter. So this is often done in bacteria where there's a single promoter-- so RNA polymerase actually will transcribe both of these genes. This repressor B, as well as this fluorescent protein. So there are going to be alternative loading sites for the ribosome in that case. And eukaryotes typically do not do this. Yeah?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: That's right. So--**

**AUDIENCE: And it will transcribe everything until--**

**PROFESSOR: Exactly. So here comes-- so an RNA polymerase down here made this whole thing. And now you might have two separate locations where the ribosome loads and makes this protein B. And then a different ribosome would make this GFP.**

**AUDIENCE: And when does it stop? It just keeps going down?**

**PROFESSOR: Yes. So there's a termination sequence.**

**AUDIENCE: No, no, but it would B and then GFP, and then it would just keep going?**

**PROFESSOR: No. The ribosome is told to basically start here and end here. So then it just makes**

3

**the B protein. And then another ribosome binds here. AUDIENCE: If you had more proteins on the same strand after GFP-PROFESSOR: And when you say protein, you're referring to the ribosome. [INTERPOSING VOICES] AUDIENCE: I mean G's right? PROFESSOR: Oh! OK, you're saying if there were another gene? AUDIENCE: No, if you have more genes coded, if you're coding for more proteins after GFP-- if you have more genes on a [INTERPOSING VOICES] --it will just keep going for an arbitrarily long-[INAUDIBLE]. PROFESSOR: Arbitrary is always a dangerous word. But they can be more than two. And actually at the biophysics retreat that some of you guys were at just last two days, there was a great talk by Gene-Wei Li, who's going to be a new incoming biology faculty member. And he was talking about the FO F1 ATP synthase. So it's the thing responsible for making ATP.**

**He analyzes process work. And there are many sub units. So there are half a dozen or so. And so it's a very long transcript. And then what he showed is that actually you have different rates of synthesis of the different genes on this one transcript. And in some cases you want actually more copies of one of the subunits than another one. And so then actually if the final protein, if it needs 12 of these, only one of these, then actually you can make 12 times as much of this, because you just have more translation here than you did here. And then it's great, because then you have all the right ratios, all the components to make the protein. So you can actually have additional regulation even at that stage.**

4

**It's possible not everybody followed that discussion, and my apologies. But feel free to just erase it from your brain if you're too confused. But what you need to keep track of here is the level of GFP is going to be perhaps proportional to the level of B. Because they're being expressed at the same time.**

**Now in order for this thing to be a memory module, you also want to be able to reset the state. So if you were in this state, you'd like to be able to somehow get it to move to this state instead. Does anybody remember what the inputs were in the context of the sample toggle switch, that it was in that review?**

---

[Up: contents](index.md) · [AUDIENCE →](02-audience.md)
