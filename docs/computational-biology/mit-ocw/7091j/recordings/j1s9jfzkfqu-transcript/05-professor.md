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

**OK, I think you get the idea here. Oh, it won't let me give up. OK, here we go.**

**OK, so these are the equations that are governing the motion in an example like that. Now, the advantage of this is we're actually simulating the protein folding. So if we do it correctly, we should always get the right answer. Of course, that's not what happens in reality.**

**Probably the biggest problem is just computational speed. So these simulations-even very, very short ones like the one I showed you-- so how long does it take a protein to fold in vitro? A long folding might take a millisecond, and for a very small**

8

**protein like that it might be orders of magnitude faster. But to actually compute that could take many, many, many days. So a lot of computing resources going into this.**

**Also, if we want to accurately represent solvation-- the interaction of the protein with water, which is what causes the hydrophobic collapse, as we saw-- then you actually would have to have water in those simulations. And each water molecule adds a lot of degrees of freedom, so that increases the computational cost, as well.**

**So all of these things determine the radius of convergence. How far away can you be from the true structure and still get there? For very small proteins like this, with a lot of computational resources, you can get from an unfolded protein to the folded state. We'll see some important advances that allow us to get around this, but in most cases we only can do relatively local changes.**

**So that brings us to our third approach for refining protein structures, which is called simulated annealing. And the inspiration for this name comes from metallurgy and how to get the best atomic structure in a metal. I don't know if any of you have ever done any metalworking. Anyone?**

**Oh, OK, well one person. That's better than most years. I have not, but I understand that in metallurgy-- and you can correct me if I'm wrong-- that by repeatedly raising and lowering the temperature, you can get better metal structures. Is that reasonably accurate? OK. You can talk to one of your fellow students for more details if you're interested.**

**So this similar idea is going to be used in this competition approach. We're going to try to find the most probable confirmation of atoms by trying to get out of some local minima by raising the energy of the system and then changing the temperatures, or raising and lowering it according to some heating and cooling schedule to get the atoms into their most probable confirmation, the most stable conformation.**

**And this goes back to this idea that we started with the local minima. If we're just doing energy minimization, we're not going to be able to get from this minimum to this minimum, because these energetic barriers are in the way. So we need to raise**

9

**the energy of the system to jump over these energetic barriers before we can get to the global free energy minimum.**

**But if we just move at very high temperature all the time, we will sample the entire energetic space but it's going to take a long time. We're going to be sampling a lot of confirmations that are low probability, as well. So this approach allows us to balance the need for speed and the need to be at high temperature where we can overcome some of these barriers.**

**So one thing that I want to stress here is that we've made a physical analogy to this metallurgy process. We're talking about raising the temperature of the system and let the atoms evolve under forces, but it's in no way meant to simulate what's going on in protein folding. So molecular dynamics would try to say, this is what's actually happening to this protein as it folds in water.**

**Simulated annealing is using high temperature to search over spaces and then low temperature. But these temperatures much, much higher than the protein would ever encounter, so it's not a simulation. It's a search strategy.**

**OK, so the key to this-- and I'll tell you the full algorithm in a second-- but at various steps in the algorithm we're trying to make decisions about how to move from our current set of coordinates to some alternative set of coordinates. Now, that new set of coordinates we're going to call test state. And we're going to decide whether the new state is more or less probable than the current one. Right?**

**If it's lower in energy, then what's it going to be? It's going to be more probable, right? And so in this algorithm, we're always going to accept those states that are lower in free energy than our current state.**

**What happens when the state is higher in free energy than our current state? So it turns out we are going to accept it probabilistically. Sometimes it's going to move up in energy and sometimes not, and that is going to allow us to go over some those energetic barriers and try to get to new energetic states that would not be accessible to purely minimization.**

10

**So the form of this is the Boltzmann equation, right? The probability of some test state compared to the probability of a reference state is going to be the ratio of these two Boltzmann equations-- the energy of the test state over the energy of the current state. So it's the e to the minus difference in energy over KT. And we'll come back to where this temperature term comes from in a second.**

**OK, so here's the full algorithm. We will either iterate for a fixed number of steps or until convergence. We'll see we don't always converge. We have some initial confirmation. Our current confirmation will be state n, and that we can compute as energy from those potential energy functions that we discussed in the last meeting.**

**We're going to choose a neighboring state at random. So what does neighboring mean? So if I'm defining this in terms of XYZ coordinates, for every atom I've got a set of XYZ coordinates I'm going to change them a few of them by small amount. Right? If I change them all by large amounts, I have a completely different structure. So I'm going to make small perturbations. And if I'm doing this with fixed backbone angles and just rotating the side chains, then what would a neighboring state be?**

**Any thoughts? What would a neighboring state be? Anyone? Change a few of the side chain angles, right? So we don't want to globally change the structure. We want some continuity between the current state and the next state.**

**So we're going to chose an adjacent state in that sense, so the state space. And then here are the rules. If the new state has an energy that's lower than the current state, we simply accept the new state. If not, this is where it gets interesting. Then, we accept that higher energy with a probability that's associated with the difference in the energies. So if the difference is very, very large, there's a low probability it'll accept. If the differences are slightly higher, than there's a higher probability that we accept. If we reject it, we just drop back to our current state and we look for a new test state. OK? Any questions on how we do this?**

---

[← [END VIDEO PLAYBACK]](04-end-video-playback.md) · [Up: contents](index.md) · [Question, yes. →](06-question-yes.md)
