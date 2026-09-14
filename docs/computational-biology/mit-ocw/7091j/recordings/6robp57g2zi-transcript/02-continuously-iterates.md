---
title: continuously iterates.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/6robp57g2zi-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# continuously iterates.

**Source:** `recordings/6robp57g2zi-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**And so this is obviously a highly computational problem because you not only have to find positions that are maximally consistent with the observed diffraction pattern, but also positions that are actually consistent with physics. So if we have a piece of a molecule here, we can't just put our atoms anywhere. They need to be positioned with well defined distances for the bonds, the bond angles, and so on. So it's a highly coupled problem that we have to solve, and we'll look at some of the techniques that underlie these approaches, although we'll look specifically at how to solve x-ray crystal structures.**

**I mentioned the second most common technique is nuclear magnetic resonance, and this is a technology that does not require the crystals, but requires a very high concentration of soluble protein, which presents its own problems. And the information that you get out of a nuclear magnetic resonance structure is not the electron density locations, but it's actually a set of distances that tell you the relative distance between two atoms, usually protons, in the structure, and that's what's represented by these yellow lines here. And once again, we've got a hard computational problem where we need to figure out a structure of the protein that's consistent with all the physical forces and also puts particular protons at particular distances from each other.**

**So we talk about solving crystal structures, solving NMR structures, because it is the solution to a very, very complicated computational challenge. So these techniques that we're going to look at, while not specifically for the solution of crystal and NMR structures, underlie those technologies. What we're going to focus on is actually perhaps an even more complicated problem, the de novo discovery of protein structures. So if I start off with a sequence, can I actually tell you something important and accurate about the structure?**

**Now, there's a nice summary in a book called Structural Bioinformatics that really deals with a lot of the issues around computational biology is relates to structure, that highlights many of the differences between the kinds of algorithms we've been**

4

**looking at up until now in this course and the kinds of approaches that we need to take in our understanding of protein structure. So the first and most fundamental obvious thing is that we're dealing with three-dimensional structures, so we're moving away from the simple linear representations of the data and dealing with more complicated three-dimensional problems. And therefore, we encounter all sorts of new problems.**

**We no longer a discrete search space. We have a continuous search space, and we'll look at algorithms that try to reduce that continuous search space back down to a discrete one to make it a simpler problem. But perhaps most fundamentally, the difference is that now we have to bring in a lot of physical knowledge to underlie our algorithms. It's not enough to solve this as a complete abstraction from the physics, but we actually have to deal with the physics in the heart of the algorithms. And we'll look at the issues highlighted in red in the rest of this talk.**

**Another thing that's going to emerge is that it would be nice if there was a simple mapping of protein sequence to structures, and if that were the case, you'd imagine that two proteins that are very different in sequence would have different structures. But in fact, that's not the case. You can have two proteins that have almost no sequence similarity at all but adopt the same three-dimensional structure, so clearly, it's an extremely complicated problem made more complicated by the fact that we don't know all the structures. It's not like we're selecting from a discrete set of known structures to figure out what our new molecule is. We have, in potential, infinite number of confirmations and protein chains we need to deal with.**

**OK, so I hope that you've had a chance to look at the material that I've posted online for review of protein structure. If you haven't, please do so. It'll be very helpful in understanding the next few lectures, and I'll assume that you're familiar with the basic elements, protein structure, what alpha helices are, what beta sheets are, primary structure, secondary structure, and so on.**

**And I'll also encourage you to become familiar with amino acids. It's very hard to understand anything in protein structure without having some knowledge of what**

5

**the amino acids are. The textbook has a nice figure that summarizes the many overlapping ways to describe the features in amino acids, so please familiarize yourself with that.**

**So these are resources that we posted online. Also, the Protein Databank, the RCSB, has fantastic resources online for beginning to understand protein structure, so I encourage you to look at their website. In particular, in their website, they have tools that you can download to visualize protein structures, and that's going to be a critical component of understanding these algorithms, to actually understand what these structures look like.**

**I've highlighted, too, that I find particularly easy to use PyMOL and Swiss PDB Viewer. You can not only look at structures with these techniques, you can actually modify them. You can do homology modeling.**

**So before we get into algorithms for understanding protein structure, we need to understand how protein structures are represented. I've already mentioned that there are these repeating units that I'd like you already know about-- alpha helices, beta sheets. We won't go into those in any detail. But the two more quantitative ways of describing protein structure have to do with a three-dimensional coordinates, the XYZ coordinates of every atom, and internal coordinates, and we'll go through those a little bit of detail.**

**So again, this PDB website has a lot of great resources for understanding what these coordinates look like. They have a good description of what's called a PDB file, and those PDB files look like this at the outset. They have what is now called metadata, but at the time was just information about how the protein structure was solved. So it'll tell you what organism the protein comes from, where it was actually synthesized if it wasn't purified from that organism, but if it was made recombinantly, details like that, details about how the crystal structure was determined. The sequence-- most of this won't concern us, but what will concern us is this bottom section shown here in more detail.**

**So let's just look at what each of these lines represents. The lines that contain**

6

**information about the atomic coordinates all begin with the word ATOM, and then there's a index number that just is referenced for each line of the file, tells you what kind of atom it is, what chain in the protein it is, and the residue number. So here, it's starting with residue 100. The sequence here can be arbitrary and may not relate to the sequence of the protein as it appears in SWISS-PROT or Gen Bank.**

**And then the next three columns are the ones that are most important to us, so these are the XYZ coordinates of the atom. So to identify the position of any molecule in three-dimensional space, obviously you need three coordinates, and so those are what those three coordinates are. And they're followed by these two other numbers, which actually are very interesting numbers because they tell us something about how certain we are that the molecule is really-- the atom is really at that position in the crystal structure. So the first of these is the occupancy.**

**In a crystal structure, we're actually getting the information about thousands and thousands of molecules that are in the repeating units of the crystal, and it's possible that there could be some variation in the structure between one unit of the crystal and the next. So you could have a side chain that, in one crystal, is over here and in the next crystal-- a repeating unit of the crystals over there. If there are discrete confirmations, then you imagine that the signal will be reduced, and you'll actually get some superposition of all the possible confirmations.**

**So number one here means that there seems to be one predominate confirmation. But if there is more than one, and their discrete-- if they're continuous, it'll just look like noise. It'll be hard to determine the coordinates. But if they're discrete positions, then you might find, for example, an occupancy of 0.5 and then another line with the other position with an occupancy of 0.5. So that's when there's discrete locations where these atoms are located.**

**The B factor's called the thermal factor, and it tells you how much thermal motion there was in the crystal at that position. Now, what does that mean? If we think about a crystal structure, there'll be some parts of it that are rock solid. In the center, it's highly constrained. The dense core of the protein, not too much is going**

7

**to be changing.**

**But on the surface of the protein, there can be residues that are highly flexible. And so as those are being knocked around in the crystal, they are scattering the x-rays in slightly different ways. But they're not in discrete confirmations, so we're not going to see multiple independent positions. We'll just see some average positions.**

**And that kind of noise can be accounted for with these B factors, where high numbers represent highly mobile parts of the structure, and low numbers represent very stable ones. A very low number here would be, say, a 20. These numbers of 80-- typically, things like that occur at the ends of molecules where there is a lot of structural flexibility.**

**So we have this one way of describing the structure of a protein where we specify the XYZ coordinates of every one of these atoms, and we'd have these other two parameters to represent thermal motion and static disorder. Now, are those coordinates uniquely defined? If I have this structure, is there exactly one way to write down the XYZ coordinates?**

**Hands? How many people say yes? How many people say no? Why not?**

**AUDIENCE: You can rotate it.**

**PROFESSOR: You can rotate it. You set the origin. Right? So there's no unique way of defining it, and that'll come up again later.**

**OK, now, this is a very precise way of describing the three-dimensional coordinates in protein, but it's not a very concise way of representing it. Now, why is that? Well, as the static model represents, there are certain parts of protein structures that are really not going to change very much. The lengths of the bonds change very little in protein structures. The angles, the tetrahedrally coordinated carbon, doesn't suddenly become flat, planar.**

**These things happen very-- there may be very small deformations. So if I had to specify the XYZ coordinates of this carbon, I really don't have too many degrees of**

8

**freedom for where the other carbon can be. It has to lie in a sphere at a certain distance. So instead of representing XYZ coordinates of every atom, I can use internal coordinates.**

**So here in this slide, we have amino acids-- the amino nitrogen, the carbonyl carbon. So this is a single amino acid. Here's the peptide bond that goes to the next one. And as this diagram indicates, the bond between the carbonyl carbon of one amino acid and the amide nitrogen of the next one is planar, so that angle isn't even rotating. So that's one degree of freedom that we've completely removed.**

**The angles that rotate in the backbone or called phi and psi; phi over here, and psi over here. So those are two degrees of freedom that determine how this amino acid is-- the confirmation of this amino acid. So instead of specifying all the coordinates, I can specify the backbone simply by giving two numbers to every amino acid, the phi and psi angles, with the assumption that the omega angle, this peptide backbone, remains constant. And similarly for the side chains, and we'll go into this in more detail later, we can then give the coordinates, the rotation, of rotatable bonds in the side chain and not specify every atom as we go out.**

**OK, so we've got these two different ways of representing protein structure, and we'll see that they're both used. Any questions on this? Great. OK, so if we're looking at protein structures, one question we want to ask is how do we compare two protein structures to each other?**

**So I already mentioned that proteins can have similar structure, whether or not they are highly similar in sequence. So if I have two proteins that are highly homologous, that do have a high level of sequence similarity-- for example, these two orthologs, this one from cow and this one from rat-- you can see, at a distance, they both have very similar structures. They also have 74% sequence similarity, so that's not surprising. But you can get proteins that have very low sequence similarity. They're still evolutionary related, like these orthologs, two different species that have the same protein, or paralogs, a single species that have two similar copies, but non identical copies, in the same protein that maintain the same structure when they**

9

**only have about 20% to 30% sequence similarity.**

**And you can get even more distant relationships. So here are two proteins, both in human, evolutionarily related, but only 4% sequence identity. And yet at a distance, they look almost identical. And those are evolutionary related proteins, but we can also have things that are called analogs, which have no evolutionary relationship, no obvious sequence similarity, and yet adopt almost identical protein structures. So this adds to the complexity of the biological problems that we're going to try to solve.**

**All right, so how do I quantitatively compare two protein structures? So the common measurement is something called RMSD, Root Mean Square Deviation, and here, I have a set of structures that were solved by NMR. And you can see that there's a core of the structure that's well determined and then there are pieces of the structure that are poorly determined. There weren't enough constraints to define them.**

**And these proteins have all been aligned, so the XYZ coordinates have been rotated and translated to give maximal agreement. And what's the agreement measure? It's this Root Mean Square Deviation.**

**So I need to define pairs of atoms in my two structures. If it's, in this case, the same structure, that's really easy. Every atom has a match in this structure that was solved with the same molecule.**

**But if we're dealing with two homologous proteins, then that becomes a little bit more tricky. We need to define which amino acids are going to match up. We can also define whether we care about changes in the side chains, or whether we only care about changes in the backbone, whether we're going to worry about whether the protons in the right places or not. And you'll see that these alignments can be done with either only heavy chain, heavy atoms, meaning excluding the hydrogens, or only main chain atoms, meaning excluding the side chains completely.**

**But once we've defined the pairs of corresponding atoms, then we're going to take the difference in the distance squared, sum of the squares of the distances between**

10

**the corresponding atoms and their x-coordinate, their y-coordinate, and they're z- coordinate. Take the square root of that sum, and that's going to give us the Root Mean Square Deviation. And of course, we have to minimize that Root Mean Square Deviation with these rigid body rotations to account for the fact that I could have my PDB file with the origin of this atom. Or I could have my PDB file with the origin of that atom, and so on.**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [OK. Any questions so far? Yes. →](03-ok-any-questions-so-far-yes.md)
