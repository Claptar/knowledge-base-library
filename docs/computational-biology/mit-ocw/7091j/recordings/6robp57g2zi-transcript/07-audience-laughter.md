---
title: 'AUDIENCE: [LAUGHTER]'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/6robp57g2zi-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [LAUGHTER]

**Source:** `recordings/6robp57g2zi-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: And she actually has solved two structures, neither one of which she's going to give you the sequence to. But she's giving you the coordinates for both of them. They're the same length.**

**And so she asks you, ha, you took 791. You can figure this out. Tell me whether that your sequence is actually in this structure or that structure. She says one of them is exactly right. You just don't know which one.**

**OK, so she gives you the backbone coordinates, so you go. You put your amino acid sequence, say, with Swiss [? PDB. ?] You add to the backbone all the right side chains. But now, you have to make a bunch of decisions for these side chain confirmations. If you make the wrong decision, what happens?**

**Well, you stick this atom close to where some other atom is. Now, you've got an optimization problem, right? You believe that one of these backbone coordinates is correct, but you've got a very highly coupled optimization problem.**

**You need to figure out the right rotations for every single side chain on this protein, and you can't do it one by one. You can't take a greedy approach because if I put this side chain here, and I put this side chain here, they collide, but if this was wrong and supposed to be over there, then maybe this is the right conformation. So I have a coupled problem, so it turns out to be computationally expensive thing to compute. So we're going to look at what to do if we know backbone confirmation, but we don't know the side chain confirmation. We can try to solve that optimization problem, and you'll actually do that in your problem set.**

**Now, what if the backbone confirmation isn't exactly correct? So let's say you do what was first suggested, and you search the sequence database. You take this**

26

**sequence, and you find that it actually has two homologs, two things with similar sequence similarity. There are two proteins with 20% sequence identity that have completely different structures.**

**This one has 20% sequence identity, and this one has 20% sequence identity. So you have no way of deciding which one's which, right? And neither one is going to be the right protein structure.**

**So you know that by putting the side chains onto these protein structures, you do have to solve those problems with side chain optimization, but what, obviously, is the other thing that you're going to need to have to solve? All right, you're going to need to solve the backbone optimization problem, and this becomes even more coupled because when I move this backbone, then the side chains move with it. So now, I've got a very, very complicated optimization problem to deal with. The search space is enormous, and even if I discretize it, it's still very, very large. In fact, there's something famous called the Levinthal Paradox.**

**Of course, Cy Levinthal, who was once upon a time a professor here and then moved to Columbia-- he did a back of the envelope calculation for extremely simple models of protein structure. If you imagine the proteins were to randomly search over all possible confirmations with very rapid switching between possible confirmations, it would take basically the lifetime of the universe for a protein to ever fold. So proteins don't do random searches over all possible confirmations, and they can check out confirmations incredibly rapidly. So we certainly can't do that, so we'll look at the optimization techniques.**

**All right, so we discussed how to use energy optimization functions to try to decide which one's correct, and that even if the structure is the correct one, we have the side chain optimization problem. If the structure's the incorrect one, we've got two problems. We've got the backbone confirmation and the side chain.**

**This is frequently called fold recognition or threading. This choice of, you've got a protein structure. You want to decide if your sequence matches this one or that one.**

27

**There are a couple of other problems that we're going to look at. So this was already raised by one of the students, the idea that we try to predict the secondary structure of this protein, so we'll look at secondary structure prediction algorithms. This was a very early area of computational effort in structural biology, and we'll see that the early methods are remarkably good.**

**We can look for domain structures, and this is really a sequence problem. So we can look through our sequences, and rather than looking for sequence identity or similarity with known structures, we can see whether there are certain patterns, like the hidden Markov models that you looked at in a previous lecture, that can allow us to recognize the domain structure of a protein even without an identical sequence in the database. So we won't go over that kind of analysis anymore, and then we'll spend a good amount of time looking at ways of solving novel structures. So if you don't have a fiendish friend who solved your structure for you, and there is no homologue in the database, all is not lost. You actually can now predict novel structures of proteins simply from the sequence.**

**All right, so a little history as to the prediction of protein structure. It really starts with Linus Pauling, who went on to win the Nobel Prize for this work. And this is in the era-- this paper was published in 1951. This was what computers looked like in 1951, and that thing probably has a lot less computing power than your iPhone or your Android.**

**So Linus Pauling did not solve the structure of the alpha helix, predict that alpha helices existed, using computers. He actually did it entirely with paper models. And in fact, he solved this-- he got the key insights for the alpha helix when he was lying sick in bed. That's a very productive sick leave, you might imagine.**

**He was using paper models, but it wasn't all done while lying in bed. So he and others, the field as a whole, have spend a lot of time observing small molecule distances, so they have some idea what to expect in protein structures. They didn't know the three-dimensional structure, but they knew a lot of the parameters about how far apart things were. And they also knew that hydrogen bonds were going to**

28

**be extremely favorable in protein structures.**

**And so he looked for a repeating structure that would maximize the number of hydrogen bonds that occur within the protein backbone chain. And he knew, also, the backbone-- that the amide bonds would be planar and so on. So there were a lot of principle that underlay this, but it was really a tour de force of just thinking rather than computing.**

**Another really important contribution early on was made by Ramachandran, was at Madras University, and his insight had to do with the fact that not all backbone confirmations were equally favorable. So remember, we have these two rotatable bonds in the backbone. We have the phi angle and the psi angle. And this plot shows that there'll be certain confirmations of phi and psi angles that are observed within these dashed lines, and then the other confirmations, which are almost never observed.**

**Now, how did he figure that out? Once again, it wasn't with computation. It was simply with paper models and figuring out what the distances would be, and then carefully reasoning over those possible structures. So you can get very far in this field, initially, back then, by simple hard thought.**

**OK, so with these two observations, we knew that there were going to be certain kinds of regular secondary structure and that not all backbone confirmations were equally favorable. OK, but now, we want to advance actually predicting structures of particular proteins, not just saying that proteins in general will contain alpha helices. So how do we go about doing that?**

**So the first advances here, we're trying to predict the structure of alpha helices, and this paper in the 1960s introduced the concept of a helical wheel. Now, the idea here, if you'll imagine that this eraser is an alpha helix, I'm going to look down the backbone of the alpha helix. And I'll see that the side chains emerge at regular positions. There's going to be 100 degree rotation between each sequential residue in the backbone as it goes around helix. It's going to be displaced and rotated by 100 degrees, and I could plot, on a piece of paper, the helical projection, which is**

29

**shown here.**

**So here's the first amino acid. 100 degrees later, the second. 100 degrees later, the third. And I can ask whether the residues on that backbone have a sequence that puts all the hydrophobics and hydrophilics on the same side, as in this case, or on different sides.**

**Now, what difference does it make? Well, if I have an alpha helix that's lying on the surface of a protein, this could have one side that's solvent exposed and one side that's protected. So we would expect that some of these alpha helices lying on the service would be amphipathic. Half of them would be hydrophobic, hydrophobic, and half of them would be hydrophilic. And purely, as someone suggested from the pattern of the amino acids, and here the hydrophobicity of the pattern of the amino acids, we could make reasonable predictions of whether this protein forms a particular kind of alpha helix, an amphipathic alpha helix.**

**Now, is that going to help us for all alpha helices? Obviously not, because I can have alpha helices that are totally solvent exposed, and I can have alpha helices that are totally protected. So this pattern will occur in some alpha helices, but not all.**

**So another idea that was raised here and was used early on with great success was to actually figure out whether certain amino acids have a particular alpha helical propensity. Do they occur more frequently in alpha helices? At the time, it was also thought maybe you could find propensities for beta sheets and other structures.**

**So compute the statistics over for every amino acid, shown as a row here. How often is it observed in the database? How often does it occur in alpha helix? And how often does it occur in beta sheet or in a coil? And from these, then, we would compute probabilities and compute using, perhaps, Bayesian statistics to compute the poster expectation for having a certain sequence in alpha helix.**

**They didn't quite use Bayesian statistics here. They came up with a rather ad hoc approach, and when you read it in hindsight, it seems kind of crazy. But actually, you have to remember when this was being done. This is being done before a big**

30

**influence of mathematicians into structural biology. This is 1974, and they used more physical reasoning.**

**They knew something about how alpha helices formed from chemistry. They knew that, typically, there's nucleation event, where a small piece of helix forms initially, and then that extends. They knew that there were these propensities for certain amino acids to form alpha helices, and other amino acids, which tended to break the helix. And they came up with an ad hoc algorithm that counted how often you had strong helix formers, how often you breakers. You can see all the details in the references.**

**The amazing thing is, with this very ad hoc thing and a very, very small database of protein structures, you could look at the total number of residues that they're looking at over all the structures, there's 2,473 and residues, not structures. And now, we have many, many more times than that of structures of proteins. Even with that, in 1974, they were able to achieve 60% accuracy in predicting the secondary structure of proteins, so it's really an astounding accomplishment.**

**And to put that in perspective, there was an evaluation of a whole bunch of secondary structure prediction algorithms done about a decade ago, and things haven't changed that much since then, where between 1974 and 2003, almost 30 years, they went from 60% accuracy to 76% accuracy. OK, well, that's not bad, but it's not a lot for-- you'd expect maybe over 30 years, you could do a lot better. So the simple approach really captured the fundamentals of predicting secondary structure. There's a lot of work that's been done since, and I encourage you to look in the textbook if you're interested, to look at all the newer algorithms that have tried to solve the secondary structure prediction problem. OK.**

**All right, so secondary structure prediction, then-- you can look in the textbook for the modern methods, but the fundamental ideas were laid down by Chou and Fasman in the 1974 paper. We're already said that looking at the kinds of approaches that we discussed earlier in the course can help you solve domain structures. I would like to focus on, at the end of this lecture and the beginning-- and**

31

**the next lecture about how to actually solve novel structures from purely amino acid sequence, and we're going to go back to the idea that there is a potential energy function.**

**We now have both the CHARMM approach and the Rosetta approach to protein structure, and so there is some protein folding landscape. There's an energy function. If you have different conformations, you'll be at different positions in landscape, and we'd like to figure out how to go from some starting confirmation that may be arbitrary and find our way to the minimum energy structure.**

**All right, so there are going to be three fundamental things that we'll talk about in the next lecture. We're going to talk about energy minimization, how to use these potential energy functions that we started off with to go from approximate structures to the refined structure. That's the thought problem I gave you.**

**You have the structure, but you have the wrong side chains. Could you minimize them? And so that's making small changes.**

**We'll discuss molecular dynamics, which actually tries to simulate all the forces on a protein and to actually carry out a physical simulation of the process. That's the CHARMM approach, and we'll see some interesting variants on that. And then we'll look at simulated annealing, which is an optimization technique that's actually quite broad, but can be applied here, to search over large, large conformational spaces, much further than a protein would actually evolve in a molecular dynamic simulation that's simulating protein function.**

**You allow the protein, now, to jump between confirmations that have no real potential to transfer between in a normal room temperature in water, but can be done, obviously, easily in the computer. So I'll stop here. Any questions before we close?**

32

---

[← indicated.](06-indicated.md) · [Up: contents](index.md)
