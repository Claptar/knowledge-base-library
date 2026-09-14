---
title: C95294 vvqy transcript Part 02 —
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/c95294-vvqy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# C95294 vvqy transcript Part 02 —

**Source:** `recordings/c95294-vvqy-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: That's right. So the question was, how do you search a database for 3D structure? You do structural similarity comparisons that are based on the 3D coordinates. The simplest way to do it, but not the most efficient, is to find the rigid-body superpositions that minimize the root mean squared deviation, which was a metric we gave in one of the previous lectures.**

**There are faster things you can do as well. You could imagine that you could look at certain global features of elements of secondary structure and so on. And there's been a lot of work making those algorithms very fast. Other questions? Good question.**

**So they give an example in their papers that starting off with this known structural complex, cyclin-dependent kinase, the cyclin, and p27, the inhibitor. And then looking for structural matches. So we can identify this potential structure match. You refined it, get an energy of interaction. Try another one that has no global structural similarity. Again, once it passes all the checks, you compute the refinement and the energy. And similarly with this side.**

**And so from this initial complex, where we had these two proteins which were known to interact in the PDP they can make predictions that these other proteins are likely to interact even though, again, at the global level, there's very little sequence similarity. Is that clear?**

**OK. So the advantage of this is that it eventually does do these structural refinements that allow us to figure out the best match between two potential**

7

**interacting proteins. But that's also its weakness because that takes a lot of computational time.**

**So this other approach called PrePPI never actually does those structural refinements of the type we talked about in the previous lecture. So if so, how does it figure out whether the two proteins are likely to interact? So this is their schematic, and we'll go through the steps.**

**So you start off with two query proteins that you want to know if they interact. And you do sequence similarity to a database of known structures. So you find sequence homologues to those proteins. And so they call those homology models. MA and MB.**

**And now they look through the database for all the structural homologues, not sequence homologues, but structural homologues of MA and MB. So they get a series of neighbors that they call NA 1 through n and NB 1 to n. So these are the neighbors of these homologues.**

**And they asked whether any of these neighbors, anything in this row, anything in this row, are known to interact. And that potential interaction then could be a model for the interaction of the query, right? So far so good.**

**Then they do a sequence alignment. They sequence alignment of MA and MB, which are the known structural homologues of the queries, and the two proteins that are known to interact. And so now they've got this potential model for the interaction of the queries made up of two proteins of known structure that have homologues that are known to interact. OK? So it's two steps removed from the actual interaction.**

**Now, while their figure says that they do a structural superposition, that's not, in fact, what they do. If you look at it carefully, it's a sequence analysis. And I'll take you through the steps in a second. So they mean structured in a rather loose way. So they're only doing sequence comparisons here. They're never actually building a homology model for the queries. OK**

8

**So this figure comes from the supplement where, for some mysterious reason, they've changed all the nomenclature. So things that previously were called NA and NB have now been called TA and TB. Take what you get. So this is a pair of interacting proteins where the structure of the interaction is known. And they're structural neighbors of NA and NB, which you don't know whether they interact or not.**

**They identify interacting residues in this structure. That's why it's represented by these black lines connecting blue dots. So these are interacting residues from the two template proteins and neighbors NA and NB. And they asked whether the amino acids in MA and MB also are good matches for this interface. And they have a number of criteria for doing that.**

**So they come up with five measures. The first of those measures is a structural similarity between these MA proteins and the MA and MB and NA and NB. Then similarity-- OK, similarity is the structural similarity. Then they asked, how many of the amino acids at this interface, and what fraction of the amino acids at the interface can be aligned? So this is a sequence-based alignment of MA and-- well, it's here called TA, but was previously called MA. Just to make life complicated. So this is the sequence-based alignment.**

**These are they interacting residues, all the blue ones in the structure of TA and TB interacting. And they asked, what fraction and what number of these amino acids are aligned in this sequence alignment? So here they come up with a number. In this case, I guess, it's four amino acids in this-- four pairs, I should say, of the amino acids-- one, two, three, and four, indicated by these four lines-- are both interacting in the structure of the complex and can be aligned to sequences in MA and MB.**

**And then they use these other algorithms that are based primarily on machine learning looking at protein interfaces to decide whether the sequence of the amino acids that are going to sit at those places in the interface are likely to be residues that typically occur at interfaces. So this is the kind of statistics that I showed you before from those old papers that said 10% of the amino acids are in these**

9

**hotspots. Certain kinds of amino acids are predominant there. So the number of algorithms, and they list a bunch, that they use to come up with a score to decide whether these residues, in fact, are statistically likely to be good matches. So they have these criteria and they decide then that some fraction of the amino acids at this interface in MA and MB are likely to be reasonable ones to be at the interface.**

**So with all that done, they then use all of these different scores with a Bayesian classifier, and we'll talk a little bit later in this lecture and probably the next lecture as well as to what a Bayesian classifier is. But they plug all those scores in that they've derived from these proteins to decide whether these two proteins are likely to interact.**

**So the advantage of this approach is it's extremely fast. Everything we've talked about are very, very quick calculations. Even the structural alignments are fast. The sequence alignments, of course, are. So we get through the whole database very quickly. So they've actually computed the potential attraction partners of every pair of proteins in various genomes based solely on these alignments.**

**The disadvantage-- so what's the disadvantage of this method?**

**AUDIENCE: Can't get a de novo interaction?**

**PROFESSOR: We can't get any de novo interaction, so if there's no neighboring structures that interact, they'll never come up with it. So that's an important point. And then the other problem is, because it doesn't have the structural refinement, it's given up on that slow calculation, so also loses a lot of potential specificity. All the conformational changes that can occur will be lost to an algorithm like this.**

**So we have these two competing approaches. Yes, questions in the back.**

**AUDIENCE: Couldn't this method actually be used as an input to, say, a refinement step, for example?**

**PROFESSOR: The question was, could you use this kind of approach as an input to the refinement step? And absolutely one could. Is there another question back there? Other**

10

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [questions? →](03-questions.md)
