---
title: chromosomes.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/zyw2aede6wu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# chromosomes.

**Source:** `recordings/zyw2aede6wu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So when we're doing assembly, oftentimes we'll find that these allelic differences are going to pop up in terms of non-concordance of our reads. And we'll have to ultimately decide if we want to make a single diploid approximation of a human genome or we want to attempt to assemble a diploid genome. And if we're going to do a diploid genome, then we have to be quite careful and use somewhat different assembly techniques.**

**But the common reference genome is haploid. It's only considering one chromosomal sequence. Is that clear to everybody? OK, great. So we're going to talk about two general approaches to assembly today. We're going to talk about overlap layout consensus assemblers as exemplified by a string graph assembler. And we're also going to talk about De Bruijn graph assemblers today.**

**Now, overlap consensus assemblers were the first ones that were used in the Human Genome Project because reads were longer back then. However, as the number of reads has increased, those assemblers are more difficult to utilize in part because of the need to find overlaps between reads, as we'll see in a moment.**

**Whereas to De Bruijn graph assemblers are somewhat more efficient. But they lose certain kinds of information. So let's begin with these overlap layout consensus assemblers. And we're going to talk about three steps to build contigs and the scaffolding step can be thought of a similar between either the overlap layout consensus assemblers or De Bruijn graph-based assemblers.**

**So we're going to first build an overlap graph. What's an overlap graph? The essential idea is that when we take our collection of reads, we look for overlaps between the suffix of one read and the prefix of another read. And if we think of all of our reads, we want to build a graph that describes all of such overlaps.**

**And just to be clear, I'm not going to be talking today about the reverse complement of these reads. Actual assemblers have to represent that. But it just duplicates all the nodes at edges. So we're going to try and keep things uncluttered by-- that's**

5

**OK. Thank you. We're going to try and keep things uncluttered by not considering those today.**

**Now, one of the challenges is how to construct those overlaps. And we're going to be talking about graphs a lot. So I thought it was worthwhile just to review terminology. We're going to represent overlap graphs as directed graphs, which consists of a set of vertices, which are the objects represented by the circles in the edges, which are the lines and a directed edge goes from one vertex to another.**

**And there's also an equivalent representation in notational form on the lower part of the right of the slide as well as a graphical representation. We're going to be using the graphical representations of these directed graphs today. So the overlap graph is simply a representation of the overlap between reads.**

**And we pick a minimum length of overlap at times. But for the next few slides, I'm simply going to represent each node as an individual read. And the edges will be annotated with the amount of overlap between the reads. So if I hand you a set of reads, all we need to do is to compute this overlap graph. We'll talk about how to do that in a moment.**

**And you'll see graphically then what comes out of the process of computing the overlap graph. Now, it's possible that overlap graphs are cyclic because there are circular chromosomes. And as we'll see, it's also possible to get a cyclic graph out of a linear chromosome if in fact there are repetitive structures in the chromosome that cause a graph to cycle back on itself.**

**So how to find overlaps in efficient time is a key problem. And that's one of the reasons that people have shied away from using these types of assemblers is because the cost of computing overlaps has been thought to be N-squared where N is the number reads because you have to compare all the reads to one another.**

**However, a really clever algorithm was devised that used the technology we talked about last time. You recall the idea of the FM index and Burroughs-Wheeler transforms allowed us to index a genome and then to look up reads in time**

6

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [proportional to the length of the read. →](03-proportional-to-the-length-of-the-read.md)
