---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/6robp57g2zi-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/6robp57g2zi-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**OK, so that was, in part, an excuse to play a little New Age music in class, but more fundamentally, it was to remind you that, despite the fact that we're going to show you a lot of static pictures of proteins, they're actually extremely dynamic. And they**

11

**have well defined structures, but they may have more than one well defined structure, especially those molecules that are doing work. They're actually moving things along. They have multiple structures. And so when we consider the protein structure, it's an approximation, and we're always going to mean the protein structures, not singular one.**

**OK, so what determines the protein structure? Well, I've told you it's physics. Fundamentally, it's a physical problem, so the optimal protein structure has to be an energetic minimum. There has to be no net force acting on the protein.**

**The force is negative derivative of the potential energy, so that derivative has to be 0. So we have to have a minimum of protein structure. Now, that doesn't mean that there's exactly one minimum.**

**Those proteins that had multiple confirmations in that movie obviously had multiple minima that they could adopt depending on other circumstances, but there has to be at least a local minimum. So if we knew this U, this potential energy function, and we could take the derivative of it, we could identify the protein structure or the protein structures by simply identifying the minima in that potential energy function. Now, would that life were so simple, right?**

**But we will see that there are ways of parameterizing the U and using it to optimize the structure so it finds this, at least local, minimum. And we're going to look primarily at two different ways of describing the potential energy function. One of them, we're going to look at the problem like a physicist one, and the other way, we're going to look at it as a statistician would.**

**So the physicist wants to describe, as you might imagine, the physical forces that underlie the protein structure, and so as much as possible, we're going to try to write down equations that represent those forces. Now, we're not always going to be able to do that because a lot of forces involved are quantum mechanical. The mere fact the two solid objects don't pass through each other is because of exclusion principles that deal with quantum mechanics.**

12

**We're not going to write down quantum mechanical equations for every atom in our protein structure, but we will write down equations that approximate those. And wherever possible, we're going to try to tie the terms in our equations into something identifiable in physics, and a very good example of this approach is the CHARMM program. And these approaches actually were the ones that won the Nobel Prize in chemistry this past year.**

**At the other end of the spectrum are the statistical approaches. Here, we don't really care what the underlying physical properties are. We want equations that capture what we see in nature.**

**Now, often, these two approaches will align very well. There'll be some approximations that the physicist makes to capture a fundamental physical force. That's simply the best way to describe what you see nature, and so those two terms may look indistinguishable in the CHARMM version or my favorite statistical approach, which is Rosetta.**

**So we'll see that some terms in these functions agree between CHARMM and Rosetta. Well, there'll be places where they fundamentally disagree on how to describe the molecular potential energy function because one is trying to describe the physical forces and the other one is trying to describe the statistical ones. Do we have any native speakers of German in the audience?**

**AUDIENCE: I'm a speaker.**

**PROFESSOR: You want to read the joke for us? AUDIENCE: Yeah. Institute for Quantum Physics, and it says "You can find yourself here or here."**

**PROFESSOR: OK. AUDIENCE: [LAUGHTER]**

**PROFESSOR: All right, so for the video, it's the Institute for Quantum Mechanics. And you go to a map at MIT, and it'll say, you find, "You are here." Right? But in the Institute for**

13

**Quantum Mechanics, it says "You're either here or here."**

**So that's the physicist approach. We really do have to think about those quantum mechanical features, whereas on the right-hand side is the statisticians approach. It says "Data don't make any sense. We'll have to resort to statistics." OK? So the statistician can get pretty far without understanding the underlying physical forces.**

**All right, so let's look at this physicist approach first, so we're going to break down the potential energy function into bonded terms and non-bonded terms. So the bonded terms, as they sound, are going to be atoms that are close to each other in the bonded structures, so certainly these two atoms, because they're connected by a single bond, are going to be bonded terms. But we'll see groups of three or four atoms near each other will also be bonded terms. And the non-bonded terms will be when I have another molecule that comes close, but isn't directly connected. What are the physical forces between these two ?**

**So these bonded terms then first break down into a lot of sub terms. I'll show you the functional forms here. We'll just look at a few of them in detail and then give you a sense of what the other ones are.**

**So this first one is the bonded term that describes, actually, the distance between two bonded atoms. Now, again, this is fundamentally quantum mechanical property, but it would be too computationally expensive to describe the quantum mechanics and not really necessary because you can do pretty well by just describing this as a stiff spring. So that's what this quadratic form of the equation represents.**

**So we simply define b naught here as the equilibrium position between these two atoms, particular types. There would be two tetrahedral coordinated carbons, and that would be determined by looking at a lot of very, very high resolution structures in small molecule crystals so we know what the typical distance for this bond is. We get that as a parameter. There would be a big file in the CHARMM program that lists all those parameters for every one of these bonded terms, and then if there's a small deviation from that, because the molecules stretched a bit in your refinement process, there would be a penalty to pull it back in just like a spring pulls it back in.**

14

**Now, it turns out that when you go this route, you have to actually come up with a lot of equations to maintain the geometry because, again, we're going to have to not only worry about these distance bonds, but we need to worry about angles. So we've got the angle between this bond and this bond. What keeps that in place?**

**So we need to add another term that's a second term here to make the angle between these fixed, and then we have to deal with what are called dihedral angles to make sure that these four atoms lie in the allowed geometry. And so each one of these terms accounts for something like that. This last term over here makes sure that the phi and psi angles are consistent with what we see in quantum mechanics as corrected for any deviations that we see in these small molecules so a lot of terms with a lot of parameters they're trying to capture the best description of what we observe in each one is motivated by the fact that there is some quantum mechanical principle underlying it. So-- yes?**

**AUDIENCE: Why is the [INAUDIBLE]?**

**PROFESSOR: I actually don't know the answer to that. But there's a reference there that I'm sure will give you the answer. OK, now what about these non-bonded terms? So nonbonded terms of the set are molecules that are distant from each other in the structure of the protein, but close to each other in three-dimensional space. And there are two fundamental forces here.**

**The first one is called the Leonard Jones potential, and the second one of the electrostatic one. And the Leonard Jones potential itself has these two terms. One is an R6 term, a negative r to the 6th dependency. The other one is positive nr to the 12th.**

**The negative r to the 6th is an attractive potential. That's why it's negative, and it's because of small induced dipoles that occur in the electron clouds of each of these atoms that pull the molecules together. And the 1 over r to the 6th dependency has to do with the physics of two dipoles interacting.**

15

**The r over 12 term is an approximation to a quantum mechanical force. So the reason the two molecules don't pass through each other, as we said already, is because quantum mechanical forces. That would be very expensive to compute, so we come up with a term that's easy to compute. And of course, an r 12 term is simply the square of an r to the 6th term, so if you already computed 1 over r to the 6th between two atoms, you just square that, and you get 1 over r to the 12th. So it's very computationally efficient, and you adjust the parameters, these r mins, so that it works out so that these things agree reasonably well with the crystal structures. And these are crystal structures of small molecules that we know in great detail.**

**And then the electrostatics is what you might expect for electrostatics. It's got a potential that varies as 1 over the distance, and as the product of those charges, these can be full charges or they can be partial charges. And there's a term here, this epsilon, which is the dielectric constant, and that represents the fact that, in vacuum, there'd be much greater force pulling two oppositely charged molecules together than in water because the water's going to shield. And so these electrostatic terms, this dihedral dielectric potential term, can vary from one, which is vacuum, to, say, 80 for water. And setting that is a bit of an art.**

**OK, so what do these potentials look like? Those are shown here. This is the, in dark lines, the sum of the van der Waals potential. It consists of that attractive term, which has the r over 6 dependency, and the repulsive term with the r over 12. And why does it go up so high at short distances?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Right, because you can't have molecules that overlap. You'll see that there's a minimum, so there's an optimal distance barring any other forces between two atoms. So that's roughly what these hard sphere distances represent in the scale models. And then the electrostatic potential also, obviously, has attractive term, but it's going to blow up as you get to small values, increasingly favorable.**

**And so the net sum of those two is shown here, the combination of van der Waals**

16

**and electrostatics. It, again, has a strong minimum but becomes highly positive as you get to close distances. OK, any questions on these forces? Yes?**

**AUDIENCE: Do the van der Waals equal the Leonard Jones potential? Or is that something else? PROFESSOR: Yeah, typically, those two terms are used interchangeably. Yeah. Other questions? OK. All right, so that's how the physicist would describe the potential energy function. Rosetta, as I told you, is an example of the statistical approach. It rejects all this sharp definition of trying to compute exactly the right distance between two atoms by having a stiff spring between them and says let's just fix a lot of these angles.**

**So we're going to fix the distance between two atoms. There's no point in having them vary by tiny, tiny fractions in the bond length. We're going to fix a tetrahedral coordination of our tetrahedral carbons. We're not going to let them deform because that never would happen in reality, and so we're going to focus our search over the space entirely over the rotatable bonds.**

**So remember, how many rotatable bonds did we have in the backbone? We had two, right? We had the phi and the psi angles, and then the side chains then will have rotatable bonds over the side chains.**

**So in this example, this is a cysteine. Here's the backbone. Here's the sulfur. And we have exactly one rotatable bond of interest because we don't really care where the hydrogen is located.**

**So we've got this chi 1 angle. If there were more atoms out here, this would be called chi 2 and chi 3. And these can rotate, but they don't rotate freely. We don't observe, in crystal structures, every possible rotation of these angles, and that's what this plot on the left represents.**

**For this side chain, there's a chi 1, a chi 2, and a chi 3, and the dark regions represent the observed confirmations over many, many crystal structures. And you**

17

**can see it's highly non uniform. Now why is that?**

**I see people with their hands trying to figure it out in the back. So why is that? Figure that's what you guys are doing. If not, it's very interesting sign language.**

**So if we look down one of these tetrahedral carbon-carbon bonds, we have apparently a free rotation. But in fact, some these confirmations, we're going to have a lot of steric clashes between the atoms on one carbon and the atoms on the other, and so this is not a favorable confirmation. The favorable confirmation is offset, and that propagates throughout all the chains in the protein.**

**So there'll be certain angles that are highly preferred, and other ones that are not. These highly preferred angles are called rotamers, and so we'll use the term a lot. It stands for rotational isomers.**

**And so now, we've turned our continuous problem of figuring out what the optimal angle is for this chi 1 rotation into a discrete problem where maybe there are only two or three possible options for that rotation. And so now, we can decide is this better than this one or this one? Questions on rotamers or any of this? Excellent.**

**OK, so how do we determine-- we've decided then we're going to describe the protein entirely by these internal coordinates-- the phi, the psi, the backbone, the chi angles of the side chain. We still need a potential energy function, right? That hasn't told us how to find the optimal settings, and we're going to try to avoid the approach of CHARMM, where we actually look at quantum mechanics to decide what all the terms are. So how do they actually go about doing this?**

**Well, they take a number of high resolution crystal structures, and they characterize certain properties in those crystal structures. For example, they might characterize how often a certain aliphatic carbon-- how often aliphatic carbons are near amide nitrogens, and they might measure the distance-- they do measure the distance between these amide nitrogens and aliphatic carbons across all the crystal structures and determine how often those distances occur. And you can actually turn those observations, then, into a potential energy function by simply using**

18

**Boltzmann's equation. So we can figure out how frequently we get certain distances on the x-axis is distance, on the y-axis is frequency, number of entries in the crystal structure, and then by Boltzmann's Law, we can compute the density of states over some reference, which is actually very hard to define. And you can look at some of the references referred to in the slides to figure out how currently that's defined, but we have to find some arbitrary reference state to figure out the probability of being any one of these states is going to be a function, a logarithmic function, of the frequency of those states.**

**All right, so we've got an energy term that's determined solely by the observations of distances, that doesn't say I know that this one's charge and this one isn't. It just says here's an oxygen attached to a carbon with double bonds. Here's a carbon that's not. How often are they at any particular distance? And we go through lots and lots of other properties, and we'll go into detail now to what those other terms are to look through high resolution crystal structures, see what certain properties are, turn those into potential energy functions that we can then use to identify the optimum rotations for the side chain and the backbone.**

**Oh, and I should also point out that when we do this, we'll have different terms for different things. We'll have a term for distances between different kinds of atoms. We'll have terms for some of these other pieces of potential energy that we'll describe in subsequent slides, and we're going to need to decide how to weight all of those, all those independent terms, to get them to give us reasonable protein structures when we're done. And that, once again, is a curve fitting exercise, finding the numbers that best fit the data without any guiding physical principle underneath it.**

**So you'll be using PyRosetta. And in PyRosetta, you'll see the terms on the board for the potential energy functions, the different features of the potential energy function, and I'll step you through a few of these just so you know what you're using. There'll also be files in PyRosetta installation that will give you the relative weights for each of these terms.**

19

**OK, so these first are the van der Waals, and here, the shape of the curve looks just like we saw before. It has to, in some sense because they're trying to solve the same physical problem, but the motivation is very different. There's no attempt to decide that it should be a 1 over r to the 6th because of dipole-dipole interactions. And simply, how do I find the function that accurately represents what I see in the database? So again, computed, this is the fa attractive and the fa repulsive, and those are determined based on the statistics of what's observed in the crystal structures.**

**This one, the hbond, breaks down into backbone and side chain, long range and short range. And the goal of the hbonds-- so hydrogen bonds are one of the principal determinants of protein structure, and you'll see that in the reading materials that are posted online. And one of the critical things about a hydrogen bond is that it needs to be nearly planar. So the line between-- the angle between this atom, which has the hydrogen attached, and this one, which is the free electron pair, has to be as close to linear as possible. And the more it deviates from linear, the weaker the hydrogen bond will be.**

**And so this hydrogen bonding potential has terms that describe the distance between the atoms that are donating and accepting the hydrogen as well as the angle between them, and it's been parameterized to represent, separately, things that are far from each other, close to each other, things that are side chain, or main chain. And here's where it's really the statistician against the physicist. Why divide up side chain and main chain? There's no physical principle that drives you to do that. It's simply because that's what gives the best fit to the data, so the statistician is not afraid to add terms that make their models better fit reality, even if they don't represent any fundamental physical principle.**

**And we'll see it gets even more dramatic with some these other terms. So this is the Ramachandran plot, which you'll also see in your reading. It represents the observed frequencies of phi and the psi angles. And as you know that there are only a couple positions on this phi and psi plot that are frequently observed, representing the different regular secondary structures primarily, alpha helix and beta sheet is**

20

---

[← [END VIDEO PLAYBACK]](04-end-video-playback.md) · [Up: contents](index.md) · [indicated. →](06-indicated.md)
