---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/j1s9jfzkfqu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/j1s9jfzkfqu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So you're close. Right. So the statistical-- or maybe you said the right thing, actually. So the statistical approach keeps a lot of the pieces the protein rigid, whereas the physics approach allows all the atoms to move independently. So one of the key differences, then, is that in the physics approach, two atoms that are bonded to each other still move apart based on a spring function. It's a very stiff spring, but the atoms move independently.**

**In the statistical approach, we just fix the distance between them. Similarly for a tetrahedrally coordinated atom, in the physics approach those angles can deform. In the statistical approach, they're fixed. Right? So in the statistical approach, we have more or less fixed geometry. In the physics approach, every atom moves independently.**

**Anyone else remember another key difference? Where do the energy functions come from? Volunteers? All right.**

**So in the physics approach, they're all derived as much as possible from physical principles, you might imagine. Whereas in the statistical approach, we're trying to recreate what we see in nature, even if we don't have a good physical grounding for it.**

**So this is most dramatic in trying to predict the solvation free energies. Right? How much does it cost you if you put a hydrophobic atom into a polar environment? Right? So in the physics approach, you actually have to have water molecules. They have to interact with matter. That turns out to be really, really hard to do.**

**In the statistical approach, we come up with an approximation. How much solvent accessible surface area is there on the polar atom when it's free? When it's in the protein structure? And then we scale the transfer energies by that amount.**

**OK, so these are then the main differences. Gotta be careful here. So we've got fixed geometry this the statistical approach. We often use discrete rotamers. Remember? The side-chain angles, in principle, can rotate freely. But there were only a few confirmations are typically observed, so we often restrict ourselves to the**

2

**most commonly observed combinations of the psi angles.**

**And then we have the statistical potential that depends on the frequency at which we observe things in the database. And that could be the frequency at which we observe particular atoms at precise distances. It could be the fraction of time that something's solvent accessible versus not.**

**And the other thing that we talked about a little bit last time was this thought problem. If I have a protein sequence and I have two potential structures, how could I use these potential energies-- whether they're derived from the physics approach or from the statistical approach-- how could I use these potential energies to decide which of the two structures is correct?**

**So one possibility is that I have two structures. One of them is truly the structure and the other is not. Right? Your fiendish lab mate knows the structure but refuses to tell you. So in that case, what would I do? I know that one of these structures is correct. I don't know which one. How could I use the potential energy function to decide which one's correct? What's going to be true of the correct structure?**

**AUDIENCE: Minimal energy.**

**PROFESSOR: It's going to have lower energy. So is that sufficient? No. Right? There's a subtlety we have to face here.**

**So if I just plug my protein sequence onto one of these two structures and compute the free energy, there's no guarantee that the correct one will have lower free energy. Why? What decision do I have to make when I put a protein sequence onto a backbone structure?**

**Yes.**

**AUDIENCE: How to orient the side chain.**

**PROFESSOR: Exactly. I need to decide how to orient the side chains. If I orient the side chains wrong, then I'll have side chains literally overlapping with each other. That'll have**

3

**incredibly high energy, right? So there's no guarantee that simply having the right structure will give you the minimal free energy until you correctly place all the side chains.**

**OK, but that's the simple case. Now, that's in the case where you've got this fiendish friend who knows the correct structure. But of course, in the general domain recognition problem, we don't know the correct structure. We have homologues. So we have some sequence, and we believe that it's either homologous to Protein A or to Protein B, and I want to decide which one's correct. So in both cases, the structure's wrong. It's this question of how wrong it is, right?**

**So now the problem actually becomes harder, because not only do I need to get the right side chain confirmations, but I need to get the right backbone confirmation. It's going to close to one of these structures, perhaps, but it's never going to be identical.**

**So both of these situations are examples where have to do some kind of refinement of an initial starting structure. And what we're going to talk about for the next part of the lecture are alternative strategies for refining a partially correct structure.**

**And we're going to look at three strategies. The simplest one is called energy minimization. Then we're going to look at molecular dynamics and simulated annealing.**

**So energy minimization starts with this principle that we talked about last time I remember that came up here, that a stable structure has to be a minimum of free energy. Right? Because if it's not, then there are forces acting on the atoms and that are going to drive it away from that structure to some other structure.**

**Now, the fact that it is a minimum of free energy does not guarantee that is the minimum of free energy. So it's possible that there are other energetic minima. Right? The protein structure, if it's stable, is at the very least a local energetic minimum. It may also be the global free energy minimum. We just don't know the answer to that.**

4

**Now, this was a big area of debate in the early days of the protein structure field, whether proteins could fold spontaneously. If they did, then it meant that they were at least apparently global free energy minima. Chris Anfinsen actually won the Nobel Prize for demonstrating that some proteins could fold independently outside of the cell. So at least some proteins had all the structural information implicit in their sequence, right? And that seems to imply that there are global free energy minimum.**

**But there are other proteins, we now know, where the most commonly observed structure has only a local free energy minimum. And it's got very high energetic barriers that prevent it from actually getting to the global free energy minimum. But regardless of the case, if we have an initial starting structure, we could try to find the nearest local free energy minimum, and perhaps that is the stable structure.**

**So in our context, we were talking about packing the side chains on the surface of the protein that we believe might be the right structure. So imagine that this is the true structure and we've got the side chain, and it's making the dashed green lines represent hydrogen bonds. It's making a series of hydrogen bonds from this nitrogen and this oxygen to pieces of the rest of the protein.**

**Now, we get the crude backbone structure. We pop in our side chains. We don't necessarily-- in fact, we almost never-- will choose randomly to have the right confirmation to pick up all these hydrogen bonds. So we'll start off with some structure that looks like this, where it's rotated, so that instead of seeing both the nitrogen and the oxygen, you can only see the profile.**

**And so the question is whether we can get from one to by following the energetic minima. So that's the question. How would we go about doing this?**

**Well, we have this function that tells us the potential energy for every XYZ coordinate of the atom. That's what we talked about last time, and you can go back and look at your notes for those two approaches. So how could we minimize this free energy minimum? Well, it's no different from other functions that we want to minimize, right? We take the first derivative. We look for places where the first**

5

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [derivative is zero. →](03-derivative-is-zero.md)
