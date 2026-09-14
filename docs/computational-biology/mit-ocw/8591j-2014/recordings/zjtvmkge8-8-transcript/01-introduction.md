---
title: Introduction
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/zjtvmkge8-8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/zjtvmkge8-8-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **MITOCW | watch?v=zJTVMkGe8-8**

**NARRATOR: The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: So in terms of what we're going to be discussing today, it's various aspects of feedforward loops. So first of all, we will go over this idea of a network motif in more detail. We talked it about a little bit in the context of auto regulation. There is a simple argument there that auto regulation is a network motif. And in order to understand how to detect network motifs, in general we have to look at a little more detail at these subgraphs and the frequency that they'll appear and so forth.**

**And then after seeing that the feed-forward loop is a network motif, then there's this question-- oh, well what might be the functional significance? And in the chapter that you just read, you found this so-called coherent type one feed-forward loop has a nice attribute-- that it's sign sensitive delay element. The incoherent type one has the feature that it's a pulse generator, and kind of related to that, it can also speed up the response time. So it can make the response time for turning on shorter. So speed up response rate if you'd like.**

**We'll also maybe say a little bit that there's been later work demonstrating that the incoherent type one can also access a fold detector. So it can sense changes in the fold change of concentrations of proteins. And then finally, we'll say something about how you can extend these ideas of a network motif to larger structures. In particular, how you get useful temporal programs.**

**So we start out with this network that is kind of-- our base network is this transcription network characterized in E. coli. And we've already talked about it some. So there's going to be some measure the number of nodes and the number of edges. So we have N nodes, and we have E edges. This is from experimental measurements of-- what is it that regulates what? Now from this, we'll have some set of directed edges, because indeed, we know that there's going to be some**

1

**transcription factor that will regulates some other protein.**

**And what we want to know is are there patterns that occur more regularly than what you'd expect based on chance. Now auto regulation we found indeed appeared more regularly, or more frequently than you would expect by chance. And there are a limited number of other network motifs that have that property. And in particular, we'll kind of analyze this idea of the feed-forward loop. Now in the network that we kind of talked about a lot, there were around 400 genes or proteins, and then around 500 observed edges.**

**And this would be interactions or regulation. Now there's this idea of sparseness. Can somebody remind us maybe what this is supposed to tell us about? Yes. AUDIENCE: There should be roughly N squared in total edges. PROFESSOR: So there's N squared possible edges. AUDIENCE: If you just connected everything that you connected, and so N is about the order of E. So roughly, there's only 1 out of 500-PROFESSOR: And we should be clear, this N squared possible-- we might even want to add directed edges since we're-- and what we see is that the actual number of edges that we observe in this real network is actually around order N. So this sparseness, which is also this probability P-- if we're going to make a network somehow that has some similar property to the observed network, there's some probably P that an actual edge will appear.**

**And this is given by the observed number of edges divided by the total possible number of edges, which is indeed N squared. And what you see is that, at least in this network, this P is much less than one. So this is what we mean by sparse. Now you can also think about the question of how many edges does a typical gene have emanating from it? Well, you can see that it's around one.**

**Of course, each edge connects two things, so if you were to say on average, each gene has of one edge going out, and one edge going in. Of course, there might be**

2

**a reason to believe that these averages are not as-- well they can be misleading. And why might the average be misleading? Yes.**

**AUDIENCE: The distribution for heavy tails.**

**PROFESSOR: Right, it's going to be a distribution with heavy tails, in particular on which side? So the average is always the average, but I guess the question is there are going to be some proteins, or some genes with many of these outgoing edges. And more generally, do you expect that-- there's a natural limitation in all this. Part of the value of this approach is that we're abstracting away from a lot of the microscopic or the biological details. But every now and then it's good to go in and think about it a little bit.**

**So there's a good reason you'd expect many proteins to not have any outgoing edges, and why would that be? Yes.**

**AUDIENCE: For example, a detector protein, that only evolved one specific function or another. PROFESSOR: So there are some proteins that have rather specific functions, you might say. And I think that's true. I think that's part of it. But there's maybe something that's maybe even a little bit more general that's worth pointing out here. Yeah.**

**AUDIENCE: Anything that's not a transcription factor.**

**PROFESSOR: Anything that's not a transcription factor, right. We say transcription factor, we don't ever really quite specify. But what it means is that it's something that can affect the transcription of other things. So we're talking about the function of it when we say transcription factor. And a majority of the proteins in any genome are not transcription factors. What that means is that they, to first order, cannot, at least directly influence the transcription of other genes.**

**So this is a reflection of this power law distribution that we observe. And so you could argue well maybe not a surprise that this outgoing edge distribution is power law, because we know that there are some transcription factors that control many things, and there are many proteins they don't control the transcription of any other**

3

---

[Up: contents](index.md) · [proteins directly. →](02-proteins-directly.md)
