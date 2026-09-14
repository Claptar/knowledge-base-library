---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/i59jdq9hk10-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/i59jdq9hk10-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **MITOCW | watch?v=i59JDQ9hk10**

**The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**DOUG So we shall start. I haven't had the pleasure of meeting most of you. I'm Doug LAUFFENBURGER:Lauffenburger. I'm gratefully invited for a guest presentation here. So I'll definitely enjoy it.**

**There should be plenty of time. I'm not racing through a lot of material, so feel free to interrupt me with questions. And of course I'll try to respond as best I can.**

**OK. Who has looked at the background materials that were posted on the web a long time ago, last night? Who already will admit to having looked at it? Good. All right. I guess that means I should do this because otherwise if you've read it already then there'd be no point, right? OK. OK.**

**Well, where we are in your semester-- you're learning a lot of things across the whole spectrum of computational systems biology. I hope I'll add something in here. It's actually a very specific topic.**

**We talk about modeling of cell signaling networks, and in particular, one approach is worth going through today and that's the logic modeling framework.**

**So I'll give you a little bit of a conceptual background for the first 10 or 15 minutes. Then we'll launch into the particular example that was in the main paper. And a little side light with an application of it to a particular cancer problem. And then that should take us pretty much to the end. OK.**

**OK. The biological topic here is cell signaling, primarily mammalian cells. Certainly applicable to microbial cells in a simpler sense. So just to place the context, in mammalian cell biology, I'm a bio-engineer and a cell biologist at the same time.**

**We're very interested in what controls the cell behavior, their phenotypic response.**

1

**We know that it's in fact controlled by what it sees in their environment, growth factors, hormones, extracellular matrix, mechanical forces, cell-cell contacts.**

**A variety of queues in the environment and the way these govern phenotype or control phenotype is that they influence, they regulate what I would call the execution processes. The crucial execution processes such as gene expression, transcription, and translation are governed by extracellular factors. Metabolism, synthesis of new molecules, cytoskeleton, motors, forced generation.**

**These things all carry out phenotype governed by the extracellular stimuli or cues. And it happens via these biochemical signaling pathways that are activated primarily by cell surface receptors in the plasmid membrane-- cascades of biochemical reactions, mostly enzymatic. Some protein-protein docking, mostly post-translational modifications. Kinase phosphate reactions adding and taking off phosphate groups that change protein activities at locations and so forth.**

**It could be other types of post-translation modifications. It could be second messengers, calcium, ATP aces and so forth. So, the extracellular-- now my battery's dead. That's not good. Oh, there we go. Extracellular stimuli, generate the signals. They regulate gene expression, metabolism, cytoskeleton. They carry out phenotype. OK.**

**So we want to learn about cell signaling network operations. There's actually multiple pathways involved. We really need to study many of them in concert to understand what the cells are doing.**

**And a big question is, what kind of information do we need to study this? And on the end, we'd be interested in how phenotypic behavior does arise from variations and mutations in the genomic content of cells.**

**But that genomic content, of course, is not modified, but its effects are influenced by what's the environment to these extracellular cues, log ins and so forth. So they influence what message is expressed.**

**From that message they influence what's actually translated into protein. From**

2

**g y y p**

**those proteins they influence the post-translational modifications and what the proteins are actually doing.**

**And so, in the end, the phenotype is carried out by these protein operations. And the question is, what information level that we might want to study.**

**And of course you would love to have the information content at all levels-genomic information, transcriptional information, translational information, posttranslational information.**

**So integrating all those different data levels can be extremely valuable. In terms of the models I'm going to talk about today, they've essentially been living at the level of protein activities in these signaling pathways. OK.**

**That will be the kind of data sets you'll see that will be analyzed with respect to the models. Obviously, they arise from these underlying mechanisms that, as influenced by the environmental context, altering the signaling protein activities.**

**OK. And what's very interesting and there's going to be more and more progress in the coming years is relating what's in the genomic information-- mutations and variations to what's happening at the protein level. And some of the other instructors in this class are really some of the world's experts in figuring out how to do this.**

**I'd like to just show this example as a motivation for this kind of approach. And that is if you do gene sequencing of many patient tumors-- in this case, I believe this was a paper on pancreatic tumors. This has been shown for pretty much every other type of tumor since then. In any given patient tumor, each one of these bars, there's dozens of mutations in each tumor.**

**And a variety of types-- deletions, amplifications mutations and by and large, they're all different. There's very few mutations themselves that really carry over to a substantial proportion of one patient's tumor to another. There's some special cases that are fairly pervasive, but the predominant of these dozens and dozens of**

3

**mutations and variations are different from one patient to another, and even in the same patient.**

**So what's emerging as a productive way to think about this-- How do all these different types of mutations and specific mutations actually lead to classes of similar pathologies? And that is they tend to reside in what can be identified as pathways-- circuits, machines, things that are actually carrying out function at the protein level.**

**So for instance-- I'm losing this again. For these pancreatic cancers on this wheel are about a dozen different signaling pathways and self-cycle control pathways and apoptosis controlled pathways. And if you look at any individual patient tumors, like this green one or this red one-- two different patients.**

**If you actually look at the mutations at the genomic level, they're entirely different in the green patient tumor versus the red patient tumor. So if you're just trying to match gene mutation to pancreatic cancer, these two patients would look entirely different.**

**But, it turns out, that you can line up their mutations into the same pathways and say, OK, the red tumor and the green tumor both have mutations that affect the TGF beta pathway. They're different mutations, but they've just regulated that pathway.**

**And similarly, you can do that with pretty much all of the other mutations. That these tumors have been dysregulated in terms of particular pathways. But patient to patient to patient, it's happened by different genomic gene sequence mutations.**

**So that the ability to look at these protein level pathways is a way of making really good productive sense of the gene sequencing data. So there's lots of labs trying to go from gene sequence up to pathway modulation. In our case, we're not going to show you that here. We're going to say, this is a motivation for starting at the protein level.**

**And I'd like to show this picture too. Number one because it's such an**

4

**anachronism. This is a circuit board from decades and decades and decades ago that none of you would recognize.**

**But, in the molecular biology world, this kind of a picture, and in its modern form is viewed as a very appealing metaphor for how to think about these signaling pathways and signaling networks that take the extracellular information and turn it into governance of transcription, metabolism, cytoskeleton, and phenotype.**

**So, just this metaphor of circuitry, where in white, the extracellular ligands, growth factors are somehow wired to the blue. The cell surface receptors, or B for instance-- they're wired too. Kinases and other signaling proteins-- they're wired to transcription factors, self-cycle control regulators, apoptosis regulators.**

**So these very famous folks in cancer biology say, what you've got to understand is, these signalling networks as circuitry. And if the circuitry is dysregulated somehow, the wiring is different, then that's what's underlying malignant behavior.**

**So, this is really beautiful but it's pretty much useless, right. Because there's no prediction or calculation or even hypothesis generation one can do from a picture like this. Yes, it's circuitry, but what do I do with it?**

**So, what I want to show you today are efforts to turn them into what I would call an actionable model, a computable model. Yes, it looks kind of like circuitry, but in fact you would know how to do a calculation that would fit it to data and predict new data. And then you have, in fact, a model rather than a metaphor. That's the idea.**

**So, one question is, if you want to turn that into a formal mathematical framework for circuitry that you can calculate-- what kind of mathematics might you use? And in this class you're learning a whole spectrum of things.**

**And one can think about it on one hand, if we knew all of those components and how they interacted, and could estimate rate constance and so forth, we could write differential equations for maybe the dozens and dozens of components and interactions and predict how they would play out dynamically with time.**

5

**For most systems with the complexity that's really controlling cell biology, at this point in time, this is almost impossible. There's only rare cases where enough is known about signaling biochemistry to really write down differential equations for what's going on.**

**At the other extreme, of course, is the type of mathematics one gets out of very, very large data sets, sequencing data sets, transcriptional, and so forth. More informatics type of analysis, where it has to do with multivariate regression and clustering, mutual information.**

**And what we've been working on is someplace up in the middle where you don't have enough mechanistic prior knowledge to write this formal of physics, and yet takes you someplace beyond statistical associations. And this is one of the areas that might be worth your learning in this class.**

**OK, this is really the same set of computational methods, just like it's cast in a little bit different form that delineates competition modeling, really into two kinds of classes.**

**What's traditionally appreciated in most fields of engineering and physics are differential equations that are very theory driven. You have a theory. You have prior knowledge for what's happening. You're writing down the components involved, you're writing down how they interact.**

**And typically, algebraic equations for those differential equations describe your theory, describe your prior knowledge. And now it's formalized and you estimate rate constants and so forth.**

**Another whole class of information is data driven, in which, you really don't have a good theory about what components matter and how they interact. And so you start with data sets and from it you do classification or typologies or associations with different types of mathematics that at least try to make sense and get hypotheses out of these large data sets, where you don't have any theory.**

**One reason that logic modeling appeals to me, is that it actually can be applied in**

6

**either the theory driven or the data driven mode. You can say, I know nothing about my system. I just generate large data sets of signaling network activities induced by different stimuli, but I'm going to try to fit a logic model to it that says how the different components influencing each other in a logic way.**

**Or, you could say, well, I know something. I have some prior knowledge. I may have interact ohms the say what molecular components are present in signaling networks.**

**And so in principle, I kind of know who's involved and who might be influencing whom. And I could write a logic model based on that prior knowledge. And then run calculations and see if it actually makes predictions about experimental data.**

**So that's one nice thing. It's a mathematical formalism that can either be run in data driven mode or in theory driven mode and go back and forth. So that's one reason-- given one lecture to offer, I've decided to offer it on this topic.**

**All right, with me so far? Any questions? Philosophy? OK.**

**So, what we're going to do today is almost take a hybrid of these two. We're going to say, what prior knowledge do we have, and then recognize that it's really not enough. And so how do we now integrate that with empirical data to now come up with logic modeling that, in fact, is actionable and computable?**

**OK. So what kind of prior knowledge do we have? Let's say we wanted to have a logic model for what's in these signaling networks down stream of growth factor receptors, or hormone receptors, or things like that, that then govern gene expression, metabolism and so forth.**

**What prior knowledge do we have? And you folks probably have already seen some of this in the class. There's all kinds of databases of stuff. What's in those databases that might be relevant here?**

**AUDIENCE:**

**[INAUDIBLE] that the protein-protein interactions-- if you switch proteins, they interact with each other, but maybe not necessarily what pathways they're in.**

7

---

[Up: contents](index.md) · [DOUG →](02-doug.md)
