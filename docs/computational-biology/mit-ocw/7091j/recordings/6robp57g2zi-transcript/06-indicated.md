---
title: indicated.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/6robp57g2zi-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# indicated.

**Source:** `recordings/6robp57g2zi-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**And rather than trying to capture the fact that protein should form alpha helices by having really good forces all around, they simply prefer angles that are observed in the Ramachandran plot. So we're going to give a potential energy function that's going to penalize you if your phi and psi ends up over here, and reward you if your phi and psi ends up in one of these positions. So from the physicist, this is cheating, and for the statistician, it makes perfect sense. Shouldn't laugh at that.**

**OK, and this same will be true for the row numbers. So we said that, for the side chains, there are certain angles that we prefer over others because that's what we observe in the database. Again, we're not going to try to get them by making sure that there's repulsion between these two atoms when they're eclipsed. We're going to get there simply by saying the potential energy is lower when you're in one of these staggered confirmations than you're one of the eclipse confirmations.**

**OK, now, the place where the difference between the statistician and the physicist is most dramatic comes when we look at the salvation terms. So a lot of what goes on in protein structure-- determines protein structure, I should say, is the interaction of the protein with water. It's bathed in a bath of 55 molar water molecules, highly polar. They normally are hydrogen bonding with each other. When the protein sits in there, the protein has to start hydrogen bonding with them.**

**And where do we find hydrophobic residues in a protein structure, with your hands? Outside or inside? Inside, right? So the hydrophobic residue's all going to be buried inside. Why is that?**

**Well, it's actually really, really hard to describe in terms of fundamental physical principles. In fact, it's really hard to describe the structure of water by fundamental physical principles. Simulations that try to get water to freeze were only successful a few years ago. So we've tried to simulate water using basic physical principles. It's very hard to get it to form ice when you lower the temperature, so it's going to be even harder, then, to represent how a complicated protein structure immersed in the water actually interacts with those water molecules.**

21

**So you've got all these water molecules interacting with polar residues or non-polar residues. The physicist really struggles to represent those. And just to show you why that is, let me show you, again, a little movie. Unfortunately, no new age music with this one. I apologize.**

**So what's shown here is a sphere immersed in a bunch of water molecules. The red is the oxygen. The little white parts are the hydrogens. You can see them wiggling around.**

**And what's the fundamental feature that you observe? All right, they're forming almost a cage around this hydrophobic molecule. Why is that? Yeah?**

**AUDIENCE: It's hard for them to interact with a non-polar residue.**

**PROFESSOR: Right, so it's hard for them to interact with a non-polar residue. So the water molecules want to minimize their potential energy. They're going to do that by forming hydrogen bonds with something. In bulk solvent, they form it with other water molecules.**

**Here, they can't form any hydrogen bonds with a sphere, so they have to dance to this complicated dance to try to form hydrogen bonds with each other with this thing stuck in middle of them. And this is, at its heart, the fundamental driving force between the hydrophobic effect, that which causes the hydrophobic residues to be buried inside of the protein. Very, very hard, as I said, to simulate using fundamental physical forces.**

**So what does the statistician do? The statistician has a mixture of experimental observation and statistics at their benefit, so we can measure how hydrophobic any molecule is. We can take carbons and drop them to non-polar solvents, into polar solvents, and determine what fraction of time a molecule will spend in a polar environment versus a non-polar environment, and from that, get a free energy for the transfer of any atom from a hydrophobic environment to a hydrophilic environment. That can give us is delta G Ref, shown over here.**

22

**OK, now, in a protein, that molecule is not fully solvent exposed even when it's on the surface, because water molecules trying to come at it from this direction can't get to it, from this direction can't get to it. So the transfer energy for this carbon to go from fully solvent exposed to buried is different from the isolated carbon. And so the statistician says, OK, I'll come up with a function to describe that. I will describe what else is near this atom in the rest of the protein structure.**

**That's what the term on the right does. It's a sum over all other neighboring atoms and describes the volume of the neighboring group. Is the thing next to it really big or really small? Usually not described, necessarily, at the level of atoms. It might be side chains depending on which program is doing it.**

**But I have some measure of the volume of the neighbors. If that volume is really large, then this thing is already in a hydrophobic environment even when it's taking water because it's surrounded by bulky things. If the neighbors are small, then it's a more hydrophilic environment when it's taking in water, and that's going to modulate this free energy. Is this function clear?**

**OK, so by combining this observation from small molecule transfer experiments and these observations based on the structure of the protein, we can get an approximation for the hydrophobic effect. How expensive is it to have this piece of the protein in solvent versus in the hydrophobic core? And again, we never had to do any quantum mechanical calculations.**

**We never had to actually explicitly compute the interaction of this molecule with solvent. We don't need any water in the structure. It's simply the geometry of the protein that's going to give us a good approximation to the energy function.**

**All right, so you can look through all the details of these online in the Rosetta documentation that we provided to get a better sense of what all these functions are, but you can see there are a lot of terms. It's increasingly incremental. You find something wrong with your models. You add a term to try to account for that. Again, not driven necessarily by the physical forces.**

23

**OK, so what have we seen so far? We've seen the motivation for this unit, to begin with protein structures, that the protein structure really helps us understand the biological molecules that we're looking at. These structures are going to influence our understanding of all biology, so we need to be good at predicting these protein structures or solving them when we have experimental data. The computational methods that we're going to use-- we're going to focus on solving protein structures de novo, predicting them, but those same techniques are going to underlie the methods that are used to solve x-ray crystallography in an MR.**

**And fundamentally then, we have these two approaches to describing the potential energy. That's the statistician and the physicist's approach. And remember, the key simplifications of the statistician are that we used a fixed geometry.**

**We're not trying to figure out the XYZ coordinates of every atom. We're simply trying to figure out the bond angles. We're going to use rotamers, so we're going to turn our continuous choices often into discrete ones. And we're going to derive statistical potentials to present the potential energy, which may or may not have a clear physical basis.**

**All right, so let's start with a little thought experiment as we try to get into some of these prediction algorithms. So I have a sequence. It's about, I don't know, 100 amino acids long, and here are two protein structures. One is predominantly alpha helical. One is predominantly beta sheet.**

**How could I tell-- this is not a rhetorical question. I want you to think for second. How could I tell whether the sequence prefers the structure on the top or the structure on the bottom? So we have, actually, a lot of the tools in place. Yes, in the back.**

**AUDIENCE: Can you, based on previously known sequences, know which sequence is predominant in which [INAUDIBLE]?**

**PROFESSOR: OK, so the answer was we could look at previously known sequences. We can look for homology, and that's actually going to be a very powerful tool. So if there is a**

24

**homologue in the database that is closely related to this protein, and it has a known structure, then problem solved. What if there isn't? What's my next step? Yes?**

- **AUDIENCE: What if you start with a description of the secondary structure, say the helices and the sheet, and you counted how often a particular amino acid showed up in each of those structures? Could you then compute maybe a likelihood across a stretch of amino acids?**

- **PROFESSOR: Great. So that answer was what if I looked at these alpha helices and beta sheets and computed how often certain amino acids occur in alpha helices versus beta sheets, and then I looked in my protein structure and checked whether I have the right amino acids that are more favorable than alpha helices or beta sheets. And we'll see that's an approach that's been used successfully. That's secondary structure prediction. OK, other ideas. Yep?**

**AUDIENCE: So if you have the position of the 3D structure, you can feed your sequence through the structure and then put it through your energy function, see which one is the lower [INAUDIBLE].**

**PROFESSOR: Excellent. So another thing I can do is, if I have these two structures, I have their precise three-dimensional structures, I could try to put my sequence onto that structure, actually put the right side chains for my sequence into that backbone confirmation. And then what would I do? I would actually measure the potential energy of the protein in top structure and the potential energy of the protein in the bottom structure.**

**If the potential energy is higher, is that the favorable structure or the unfavorable structure? Favorable? Unfavorable? Right, it's the unfavorable. So I want the lower free energy structure.**

**OK, so let's think about-- that's correct, and that's where we're headed. But what are going to be some of the complexities of that approach? So first of all, what about these side chains? I have to now take a backbone structure that had some other amino acid sequence on it, and I have to put these new side chains on. Right?**

25

**If I put those on in the wrong way-- let's say, this is the true one-- let's say one of these is the true structure. Let's begin with a simplification. All right, so let's say your fiendish labmate has actually solved the structure of your protein, but refuses tell you what the answer is.**

---

[← PROFESSOR](05-professor.md) · [Up: contents](index.md) · [AUDIENCE: [LAUGHTER] →](07-audience-laughter.md)
