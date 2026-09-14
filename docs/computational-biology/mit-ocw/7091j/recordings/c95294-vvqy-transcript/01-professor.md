---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/c95294-vvqy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/c95294-vvqy-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**OK. So we've been talking about predicting structure proteins. At the end of the last lecture we started to talk a little bit about predicting interactions, and that's going to be the focus of today's lecture. And we identified a couple of different possible prediction challenges.**

**One was quantitative predictions of what happens when you make specific mutations in a known protein complex. We talked about trying to predict the structure of, say, just a pair of proteins, and then trying to do that on the global scale for all known proteins.**

**And so last time, if you recall, we thought that initially maybe this would be a simple problem. We have proteins of known structure with a complex. Structure of the complex is also known. And we want to make predictions as to the change in affinity when there's a specific mutation made.**

**In principle, this should be easy because we have all those different formulations for the potential energy function. And so if we figure out what the local structural changes are that are due to the insertion or deletion of some side chain, then we should be able to predict the change in the potential energy, and therefore the change in the energy of the complex. But in fact, it turned out that it was very, very hard to do that.**

**And so this plot compared-- the black circles were the prediction algorithms for this problem, compared to just simply a substitution matrix, the BLOSUM substitution matrix defined in terms of the area under the curve for beneficial mutations and deleterious mutations. And you can see that very, very few of the black dots get far away from what is the really simple default model. A lot of them do worse.**

1

**So OK, well maybe that's not such a simple problem because it requires a highly quantitative prediction. Maybe we'll do better just trying to predict which proteins interact at all. And so that's going to be the focus of today's lecture.**

**Now, that also had a problem, right? Because even if I know the structure of two proteins, I don't know necessarily what surfaces of those proteins interact. And so I have to figure out this docking problem of which part of protein A interacts with which part of protein B.**

**That's the beginning of my problem, and then I have to make a series of subsequent decisions. So I'm going to have to figure out for any potential partner of my protein, I need to figure out the docking problem, the relative position orientation. Now, in this little cartoon, it's shown as a completely static protein that approaches another static protein. The only thing that's changing is the relative coordinates.**

**But of course, there will be local changes in confirmation, perhaps even global ones. And so we need to be able to make some estimates as to what those structural rearrangements will be when the two proteins interact. And then after we've come up with our best estimate of the structural rearrangements, only then can we come up with an estimate of the energy interaction and decide whether it's better than some threshold.**

**OK. So one of the problems that's pretty obvious from this is that this kind of approach in principle, if we do it rigorously through all the steps, would be extremely slow. Now, another part that's perhaps a little bit less obvious is that it's going to be very prone to false positives. And why do you think that might be? What am I not taking into account here?**

**AUDIENCE: Are you not taking into account the desolvation [INAUDIBLE].**

**PROFESSOR: So one answer is I'm not taking account of the desolvation, but in fact, I can do that. Right? So some of the potential energy functions we looked at, the statistician's version rather than the physicist's makes it pretty easy to incorporate the**

2

**desolvation. Any other thoughts as to what I'm not taking into account? What other protein should I be considering when I'm considering an interaction problem?**

**So I've isolated, in this case, two proteins. I'm saying, in a universe where these are the only two proteins that exist, will they have a favorable energy interaction? What I really need to know is whether that energy interaction is more favorable than all the competing interactions that they could have.**

**So even if I find something that's potentially a good interaction, it may not be the best possible interaction. And if I consider then the concentration of this protein and the concentration of all the other molecules out there that have a higher affinity, then it could turn out that this is actually a rather poor substrate for my protein, a rather poor interaction partner. So we have that false positive problem. OK.**

**But let's focus on the computational efficiency problem, because that's at least one that we can come up with some nice algorithms to try to solve. So what we want to do is try to limit our search space. If I want to figure out-- I have a query protein and I want to ask, what does it interact with, instead of trying to do the pairwise comparison of this protein with every other protein in the database, and doing very precise structural calculations on all of those, maybe there's some way that I can prefilter the set of proteins that it might interact with.**

**And that's what we're going to look at. So we're going to try to officially choose potential partners before we're doing any structural comparison. And then once we have those partners, we're going to try to avoid having to do detailed calculations until we have a relatively high degree of confidence that these proteins could interact by other criteria.**

**And we're going to look at two papers that describe algorithms for solving this problem, and they're both uploaded to the website. The first thing that we'll look at is called PRISM that actually uses structural calculations. And then we'll look at PrePPI, which deals with everything purely at-- without actually explicitly calculating the structures.**

3

**OK. So what does PRISM do? Well, it's based on the notion that there are a limited number of architectures that we could look at for which proteins can interact. And so if we can identify those architectures, then we can try to figure out whether a protein is a potential partner of another one before we do the detailed, costly calculations.**

**In addition, in those architectures, not all amino acids are going to be equal, but there are going to be some that contribute more to the energy than others. And so by identifying those critical residues, we can once again focus our computational energy on those complexes that are most likely to be important.**

**OK. So it has these two components-- a rigid-body structural comparison. So that's that two proteins are not changing their own coordinates, they're just being brought together in different conformations. And then once the proteins have passed a series of checks, then we allow for flexible refinement using the kinds of energies we looked at in the previous lectures to decide how high affinity this complex could be.**

**And the critical thing is that we're going to make some of these early decisions after the rigid-body comparison using structural similarity, evolutionary conservation, and particularly looking at these regions that are called hotspots. These are sites where most of the free energy of interaction occurs during an interface. So it's not, as I said, uniformly distributed.**

**So I showed you this slide last time. It shows chymotrypsin in a light gray and its interaction with some protein partners. These two share some global similarity to each other, whereas this partner is quite different from either of these two globally. But you can see that at the interface, it's actually quite similar. And so this gives you hope that even if you can't find a direct homologue-- so if you were trying to figure out, what does this protein in yellow interact with, and you searched the database and you couldn't find anything that was its structural homologue, but if you could figure out to look for homologues of the lower regions that interact, you might be able to figure out that it interacts with the same protein as this one and this one. OK.**

**So what about this idea of hotspots? And this was an idea that was first developed**

4

**in 1995 by this paper, Clackson and Wells, where they were looking at the interaction of a cell surface receptor with its ligand approaching. And they did systematic mutagenesis across the surface of the interface to see when I mutate any single amino acid to alanine, how much it affects the energy of interaction.**

**What they found was things were highly non-uniform. So this lower curve shows the change in free energy when you mutate particular individual amino acids to alanine. And you can see there are big losses of free energy at some places, and other places there's almost no change in the free energy binding. In a few places you actually get a benefit from mutating a side chain to alanine.**

**So in this particular case, and it's held up over many, many cases then, the free energy of binding is not uniform across the surface, but it's distributed in what has been called hotspots. So here is a structure of the human growth hormone and its receptor. And in red are the few amino acids that contribute very, very large amounts-- more than one and a half kcals per mole-- to the energy of interaction.**

**And it doesn't correspond with any simple structural parameter. So it's not the amino acids that have the biggest surface area, for example, or anything like that. So it's not trivial to figure out what these regions are, although there are some prediction algorithms.**

**So there are studies, and subsequent ones have indicated that roughly 10% of the amino acids at the interface are the ones that have the biggest contribution. There are some trends, but none of these are hard rules. These tend to be rich in these three amino acids-- tryptophan, arginine, and tyrosine.**

**If you might imagine, these are regions of the protein that are highly complimentary. So there'll be a patch on one side that's a hotspot matching up with another patch on the other protein that's also a hotspot. And it's kind of an interesting note that around these regions where the hotspots occur, there are other amino acids that exclude solvent from the interface. And they call that an o-ring. So these are some of the features that tend to occur with protein interfaces.**

5

**So in this PRISM algorithm, what they do is the following. They start off with a template-- two proteins that are known to interact-- and they define the interface simply by close approach of amino acids in one chain to amino acids in the other. So in this case, shown in these balls are regions of the proteins that interact.**

**And then they isolate the interfacial residues. Ignore the rest of the protein, because we said that the parts that interact in different proteins could be homologous even if the global structures of the proteins are not, right? So we're going to do our structural similarity calculations purely on the interface residues and not on the entire structure.**

**So then with that template, you can then look at lots of proteins and see whether they have any structural match to pieces that interact. So here they've identified this protein, ASPP2, which has structural homology to I kappa b at the interface. Although globally it's quite different.**

**And now, once they have this potential partner for NF kappa b, this ASPP2, they're going to test whether there's a good structural match, whether specifically in the regions that are hotspots-- they have an algorithm for predicting hotspots-- whether the match is good, whether it's sequence conservation at those hotspots. And only then do they do the refinement to do the flexible refinement of the type that we looked at in the previous lecture, energy minimization, and other approaches to figure out what the best possible structure of this complex would be, and then what it's free energy would be.**

**So here's their description of the problem. They have template proteins and targets. They do a structure alignment. They asked whether it passes some thresholds. These are very, very fast calculations to do. And only if they pass these fast calculations do you do more detailed calculations. And finally, only if it passes this do you do the very computationally expensive refinement.**

**And then one critical thing to remember from this algorithm is that it doesn't require the template and its query to be perfectly matched in structure. In fact, the elements of the structure at the interface could come from different parts of the chain. So they**

6

**don't take into account the chain order.**

**So if I had a beta sheet structure in one protein that looks like this, in my query these two proteins could be very indirectly connected. I don't care that there's a huge gap in the insertion. I just care that locally at the interface, one protein looks a lot like the other. There was a question in the back.**

---

[Up: contents](index.md) · [C95294 vvqy transcript Part 02 — →](02-c95294-vvqy-transcript-part-02.md)
