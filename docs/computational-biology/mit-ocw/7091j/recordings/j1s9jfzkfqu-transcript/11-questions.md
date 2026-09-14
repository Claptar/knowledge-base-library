---
title: Questions?
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/j1s9jfzkfqu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Questions?

**Source:** `recordings/j1s9jfzkfqu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So what we've seen so far has been the Rosetta approach to solving protein structures. And it really is, throw everything at it. Any trick that you've got. Let's look into the databases. Let's take homologous proteins. Right? So we have these high, medium, low levels homologues. And even when we're doing a homologue, we don't restrict ourselves to that protein structure.**

**But for certain parts, we'll go into the database and find the structures of peptides of length three to nine. Pull those out of the [? betas. ?] Plug those in. Our potential energy functions are grab bag information, some of which has strong physical principles, some which is just curve fitting to make sure that we keep the hydrophobics inside and hydrophilics outside.**

**So we throw any information that we have at the problem, whereas our physicist has disdain for that approach. He says, no, no. We're going to this purely by the book. All of our equations are going to have some physical grounding to them. We're not going to start with homology models. We're going to try to do the**

23

**simulation that I showed you a little movie of for every single protein we want to know the structure of.**

**Now, why is that problem hard? It's because these potential energy landscapes are incredibly complex. Right? They're very rugged. Trying to get from any current position to any other position requires a go over many, many minima.**

**So the reason it's hard to do, then, is it's primarily a computing power issue. There's just not enough computer power to solve all of these problems. So what one group, DE Shaw, did was they said, well, we can solve that by just spending a lot of money, which fortunately they had.**

**So they designed hardware that actually solves individual components of the potential energy function in hardware rather than in software. So they have a chip that they call Anton that actually has parts of it that solve the electrostatic function, the van der Waals function.**

**And so in these chips, rather than in software, you are doing as fast as you conceivably can to solve the energy terms. And that allows you to sample much, much more space. Run your simulations for much, much longer in terms of real time.**

**And they do remarkably well. So here are some pictures from a paper of theirs-- a couple of years ago now-- with the predicted and the actual structures. I don't even remember which color is which, but you can see it doesn't much matter. They get them down to very, very high resolution.**

**Now, what do you notice about all these structures?**

**AUDIENCE: They're small.**

**PROFESSOR: They're small, right? So obviously there's a reason for that. That's when you can do in reasonable compute time, even with a high-end computing that's special purpose. So we're still not in a state where they can fold any arbitrary structure.**

**What else do you notice about them? Yeah, in the back.**

24

**AUDIENCE: They have very well-defined secondary structures. PROFESSOR: They have very well-defined secondary structures. And they're specifically what, mostly? AUDIENCE: Alpha helixes. PROFESSOR: Alpha helixes, right. And it turns out that a lot more information is encoded locally in an alpha helix than in a beta sheet, which is going to be contingent on what that piece of protein comes up against. Right? Whereas in the alpha helix, we saw that you can get 60% accuracy with very crude algorithms, right? So we're going to do best with these physics approaches when we have small proteins that are largely alpha helical. But in later papers-- well here's even an example. Here's one that has a certain amount of beta sheet. And the structures are going to get larger with time. So it's not an inherent problem. It's just a question of how fast the hardware is today versus tomorrow. OK, a third approach. So we had the statistical approach. We have the physics approach. The third approach, that I won't go into detail but you can play around was literally yourselves, is a game where we have humans who try to identify the right structure, just as humans do very well in other kinds of pattern recognition problems.**

**So you can try this video game where you're given structures to try to solve and say, oh, should I make that helical? Should I rotate that side chain? So give it a try. Just Google FoldIT, and you can find out whether you can be the best gamers and beat the hardware.**

**All right. So so far we've been talking about solving the structures of individual proteins. We've seen there is some success in this field. It's improved a lot in some ways. Between CASP1 and CASP5 I think there's been huge improvements. Between CASP5 and CASP10, maybe the problems have gotten hard. Maybe there have been no improvements. We'll leave that for others to decide.**

25

**What I'd like to look at in the end of this lecture and the beginning of the next lecture are problems of proteins interacting with each other, and can we predict those interactions? And that'll, then, lead us towards even larger systems and network problems.**

**So we're going to break this down to three separate prediction problems. The first of these is predicting the effect of a point mutation on the stability of a known complex. So in some ways, you might think this is an easy problem. I've got two proteins. I know their structure. I know they contract. I want to predict whether a mutation stabilizes that interaction or makes it fall apart. That's the first of the problems.**

**We can try to predict the structure of particular complexes, and we can then try to generalize that and try to predict every protein that interacts with every other protein. We'll see how we do on all of those.**

**So we'll go into one of these competition papers, which are very good at evaluating the fields. This competition paper looked at what I call the simple problem. So you've got two proteins of known structure. The authors of the paper, who issued the challenge, knew the answer for the effect of every possible mutation at a whole bunch of positions along these proteins on the-- well, an approximation to the free energy of binding.**

**So they challenged the competitors to try to figure out, we give you the structure, we tell you all the positions we've mutated, and you tell us whether those mutations made the complex more stable or made the complex less stable. Now specifically, they had two separate protein structures.**

**They mutated 53 positions in one. 45 positions in another. They didn't directly measure the free energy of binding for every possible complex, but they used a high throughput assay. We won't go into the details, but it should track, more or less, with the free energy. So things that seem to be more stable directors here probably are lower free energy complexes.**

**OK, so how would you go about trying to solve this? So using these potential energy**

26

**functions that we've already seen, you could try to plug in the mutation into the structure. And what would you have to do then in order to evaluate the energy? Before you evaluate the energy.**

**So I've got known structure. I say, position 23 I'm mutating from phenylalanine to alanine. I'll say alanine to phenylalanine. Make it a little more interesting. OK? So I'm now stuck on this big side chain. So what do I need to do before I can evaluate the structure energy?**

**AUDIENCE: Make sure there's no clashes.**

**PROFESSOR: Make sure no clashes, right? So I have to do one of those methods that we already described for optimizing the side chain confirmation, and then I can decide, based on the free energy, whether it's an improvement or makes things worse.**

**OK, so let's see how they do. So here's an example of a solution. The submitter, the person who has the algorithm for making a prediction, decides on some cutoff in their energy function, whether they think this is improving things or making things worse. So they decide on the color. Each one of these dots represents a different mutation.**

**On the y-axis is the actual change in binding, the observed change in binding. So things above zero are improved binding. Below zero are worse binding. And here are the predictions on the submitter scale. And here the submitter said that everything in red should be worse and everything green should be better. And you can see that there's some trend. They're doing reasonably well in predicting all these red guys as being bad, but they're not doing so well in the neutral ones, clearly, and certainly not doing that well in the improved ones.**

**Now, is this one of the better submitters or one of the worst? You'd hope that this is one of the worst, but in fact this is one of the top submitters. In fact, not just the top submitter but top submitter looking at mutations that are right at the interface where you'd think they'd do the best, right?**

**So if there's some mutation on the backside of the protein, there's less structural**

27

**p ,**

**information about what that's going to be doing in the complex. There could be some surprising results. But here, these are amino acid mutations right at the interface.**

**So here's an example of the top performer. This is the graph I just showed you, focusing only at the [? residues ?] of the interface, and all sites. And here's an average group. And you can see the average groups are really doing rather abysmally. So this blue cluster that's almost entirely below zero were supposed to be neutral. And these green ones were supposed to be improved, and they're almost entirely below zero. This is not encouraging story.**

**So how do we evaluate objectively whether they're really doing well? So we have some sort of baseline measure. What is it the sort of baseline algorithm you could use to predict whether a mutation is improving or hurting this interface? So all of their algorithms are going to use some kind of energy function. What have we already seen in earlier parts of this course that we could use?**

**Well, we could use the substitution matrices, right? We have the BLOSUM substitution matrix that tells us how surprised we should be when we see an evolution, that Amino Acid A turns into Amino Acid B. So we could use, in this case, the BLOSUM matrix. That gives us for each mutation a score. It ranges from minus 4 to 11. And we can rank every mutation based on the BLOSUM matrix for the substitution and say, OK, at some value in this range things should be getting better or getting worse.**

**So here's an area under the curve plot where we've plotted the false positives and true positive rates as I change my threshold for that BLOSUM matrix. So I compute what the mutation BLOSUM matrix is, and then I say, OK, is a value of 11 bad or is it good? Is a value of 10 bad or good? That's what this curve represents. As I vary that threshold, how many do I get right and how many do I get wrong?**

**If I'm doing the decisions at random, then I'll be getting roughly equal true positives and false positives. They do slightly better in the random using this matrix. Now, the**

28

**best algorithm at predicting that uses energies only does marginally better. So this is the best algorithm at predicting. This is this baseline algorithm using just the BLOSUM matrix. You can see that the green curve predicting beneficial mutations is really hard. They don't do much better than random. And for the deleterious mutations, they do somewhat better.**

**So we could make these plots for every single one of the algorithms, but a little easier is to just compute the area under the curve. So how much of the area? If I were doing perfectly, I would get 100% true positives and no false positives, right? So my line would go straight up and across and the area under the curve would be one.**

**And if I'm doing terribly, I'll get no true positives and all false positives. I'd be flatlining and my area would be zero. So the area under the curve, which is normalized between zero and one, will give me a sense of how well these algorithms are doing.**

**So this plot-- focus first on the black dots-- shows at each one of these algorithms what the area under the curve is for beneficial and deleterious mutations. Beneficial on the x-axis, deleterious mutations on the y-axis. The BLOSUM matrix is here.**

**So good algorithms should be above that and to the right. They should having a better area under the curve. And you can see the perfect algorithm would have been all the way up here. None of the black dots are even remotely close. The G21, which we'll talk about a little bit in a minute, is somewhat better than the BLOSUM matrix, but not a lot.**

**Now, I'm going to ignore the second round in much detail, because this is a case where people weren't doing so well in the first round so they went out and gave them some of the information about mutations at all the positions. And that really changes the nature of problem, because then you have a tremendous amount of information about which positions are important and how much those mutations are making. So we'll ignore the second round, which I think is an overly generous way of comparing these algorithms.**

29

**OK, so what did the authors of this paper observe? They observed that the best algorithms were only doing marginally better than random choice. So three times better. And that there seemed to be a particular problem looking at mutations that affect polar positions.**

**One of the things that I think was particularly interesting and quite relevant when we think about these things in a thermodynamic context is that the algorithms that did better-- none of them could be really considered to do really well-- but the algorithms that did better didn't just focus on the energetic change between forming the native complex over here and forming this mutant complex indicated by the star. But they also focused on the affect of the mutation on the stability of the mutated protein.**

**So there's an equilibrium not just moving between the free proteins and the complex, but also between moving between the free proteins that are folded and the free proteins that are unfolded. And some of these mutations are affecting the energy of the folded state, and so they're driving things to the left, to the unfolded. And if you don't include that, then you actually get into trouble.**

**And I've put a link here to some lecture notes from a different course that I teach where you can look up some details and more sophisticated approaches that actually do take into account a lot of the unfolded states.**

**So the best approach-- best of a bad lot-- consider the effects of mutations on stability. They also model packing, electrostacks, and solvation. But the actual algorithms that they used were a whole mishmash of approaches. So there didn't seem to emerge a common pattern in what they were doing, and I thought I would take you through one of these to see what actually they were doing.**

**So the best one was this machine learning approach, G21. So this is how they solved the problem. First of all, they dug through the literature and found 930 cases where they could associate a mutation with a change in energy. These had nothing to do with proteins under consideration. They were completely different structures.**

30

**But they were cases where they actually had energetic information for each mutation.**

**Then we go through and try to predict what the structural change will be in the protein, using somebody else's algorithm, FoldX. And now, they describe each mutant, not just with a single energy-- we have focused, for example, on PyRosetta, which you'll use in process-- but they actually had 85 different features from a whole bunch of different programs.**

**So they're taking a pretty agnostic view. They're saying, we don't know which of these energy functions is the best, so let's let the machine learning decide. So every single mutation that's posed to them as a problem, they have 85 different parameters as to whether it's improving things or not.**

**And then, they had their database of 930 mutations. For each one of those they had 85 parameters. So those are label trending data. They know whether things are getting better or worse. They actually don't even rely on a single machine learning method. These actually used five different approaches.**

**We'll discuss Bayesian nets later in this course. Most of these others we won't cover at all, but they used a lot of different computational approaches to try to decide how to go from those 85 parameters to a prediction of whether the structures improved or not.**

**So this actually shows the complexity of this apparently simple problem, right? Here's a case where I have two proteins of known structure. I'm making very specific point mutations, and even so I do only marginally better than random. And even throwing at it all the best machine learning techniques. So there's clearly a lot in protein structure that we don't yet have parametrized in these energy functions.**

**So maybe some of these other problems are actually not as hard as we thought. Maybe instead of trying to be very precise in terms of the energetic change for a single mutation at an interface, we'd do better trying to predict rather crude parameters of which two proteins interact with each other. So that's what we're**

31

**going to look at in the next part of the course. We're going to look at whether we can use structural data to predict which two proteins will interact.**

**So here we've got a problem, which is a docking problem. I've got two proteins. Say they're of known structure, but I've never seen them interact with each other. So how do they come together? Which faces of the proteins are interacting with each other? That's called a docking problem.**

**And if I wanted to try to systematically figure out whether Protein A and Protein B interact with each other, I would have to do a search over all possible confirmations, right? Then I could use the energy functions to try to predict which one has the lowest energy. But it actually would be a computationally very inefficient way to do things.**

**So we could imagine we wanted to solve this problem. For each potential partner, we could evaluate all relative positions and orientations. Then, when they come together we can't just rely on that, but as we've seen several times now we're going to have to do local confirmational changes to see how they fit together for each possible docking. And then, once we've done that, we can say, OK, which of these has the lowest energy of interaction?**

**So that, obviously, is going to be too computationally intensive to do on a large scale. It could work very well if you've got a particular pair or proteins that you need to study. But on a big sale, if we wanted to predict all possible interactions, we wouldn't really be able to get very far. So what people typically do is use other kinds of information to reduce the search space. And what we'll see in the next lecture, then, are different ways to approach this problem.**

**Now, one question we should ask is, what role is structural homology going to play? Should I expect that any two proteins that interact with each other-- let's say that that Protein A and I know its interactors. So I've got A known to interact with B. Right? So I know this interface.**

**And now I have protein C, and I'm not sure if it interacts or not. Should I expect the**

32

**interface of C, that touches A, to match the interface of B? Should these be homologous? And if not precisely homologous, then are there properties that we can expect that should be similar between them?**

**So different approaches we can take. And there are certainly cases where you have proteins that interact with a common target that have no overall structure similarity to each other but do have local structural similarity. So here's an example of subtilisn, which is shown in light gray, and pieces of it that interactive with the target are shown in red.**

**So here are two proteins that are relatively structurally homologous-- they interact at the same region. That's not too surprising. But here's a subtilisn inhibitor that has no global structural similarity to these two proteins, and yet its interactions with subtilisn are quite similar.**

**So we might expect, even if C and B don't look globally anything like each other, they might have this local similarity.**

**OK, actually I think we'd like to turn back your exams. So maybe I'll stop here. We'll return the exams in the class, and then we'll pick up at this point in the next lecture.**

33

---

[← Good questions. Any other questions?](10-good-questions-any-other-questions.md) · [Up: contents](index.md)
